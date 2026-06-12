#!/usr/bin/env python3
"""
BULL ops watchdog — "who watches the watchmen".

Every incident in BULL's history was a silent failure this script would have
caught on day one instead of day nine:
  - 2026-06-02: .mcp.json pointed at a renamed folder -> 9 days of routine-07
    skips (check G: MCP config paths exist)
  - 2026-05-24: ccdScheduledTasksEnabled silently false -> no routine fires
    (check E)
  - 2026-05-24: OPERATING.md edit stranded uncommitted for 2.5 weeks (check C)
  - 2026-06-10/11: +1-day date mislabels stamped future timestamps that would
    have truncated replay windows (check B)
  - 2026-05-31..06-08: variant HYPE position un-MTM'd for 9 days (check D)

Checks:
  A. Routine heartbeat — each routine slot has committed within its cadence
  B. Future timestamps — Last rebuild / Last refresh / trade-log rows <= now
  C. Dirty working tree — stranded uncommitted/untracked files
  D. Stale open-position MTM — open position + portfolio rebuild older than 30h
  E. Scheduler flag — ccdScheduledTasksEnabled true in claude_desktop_config.json
  F. Unpushed commits — local main ahead of origin/main (push failures)
  G. MCP config paths — every absolute path in .mcp.json exists on disk

Usage (from repo root, wired into routine VERIFY steps):
  python scripts/watchdog.py              # report; exit 0 clean, 1 findings
  python scripts/watchdog.py --telegram   # also alert via telegram_send.py on findings

Findings never block a routine by themselves — the routine notes them and
continues unless a finding is independently a kill-switch condition.
"""

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# max hours since last commit mentioning each routine slot
HEARTBEAT_HOURS = {
    "routine-01": 80,   # Mon-Fri 06:00 PT; 80h spans a weekend
    "routine-02": 80,
    "routine-03": 80,
    "routine-04": 200,  # weekly (Sat)
    "routine-05": 200,  # weekly (Sun)
    "routine-06": 200,  # weekly (Fri)
    "routine-07": 30,   # daily incl. weekends
}
FUTURE_TOLERANCE = timedelta(hours=2)
STALE_MTM_HOURS = 30
ISO_RE = re.compile(r"(20\d\d-\d\d-\d\d)T(\d\d):(\d\d)(?::\d\d)?Z")
DESKTOP_CONFIG = os.path.expandvars(r"%APPDATA%\Claude\claude_desktop_config.json")


def git(*args):
    r = subprocess.run(["git", "-C", REPO, *args],
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    return r.returncode, (r.stdout or "").strip(), (r.stderr or "").strip()


def parse_iso(line):
    m = ISO_RE.search(line)
    if not m:
        return None
    d, hh, mm = m.group(1), int(m.group(2)), int(m.group(3))
    y, mo, dd = (int(x) for x in d.split("-"))
    return datetime(y, mo, dd, hh, mm, tzinfo=timezone.utc)


def check_heartbeats(now, findings):
    code, out, err = git("log", "--since=12.days", "--format=%ct\x1f%s")
    if code != 0:
        findings.append(f"A heartbeat: git log failed: {err}")
        return
    latest = {}
    for line in out.splitlines():
        ts, _, subj = line.partition("\x1f")
        m = re.search(r"routine-0\d", subj)
        if m:
            key = m.group(0)
            t = int(ts)
            if t > latest.get(key, 0):
                latest[key] = t
    for slot, max_h in HEARTBEAT_HOURS.items():
        t = latest.get(slot)
        if t is None:
            findings.append(f"A heartbeat: no {slot} commit in the last 12 days "
                            f"(cadence allows {max_h}h) — routine may be dead")
            continue
        age_h = (now - datetime.fromtimestamp(t, tz=timezone.utc)).total_seconds() / 3600
        if age_h > max_h:
            findings.append(f"A heartbeat: {slot} last committed {age_h:.0f}h ago "
                            f"(threshold {max_h}h) — check scheduler / MCP")


def iter_state_files():
    yield os.path.join(REPO, "memory", "portfolio.md")
    yield os.path.join(REPO, "memory", "leaderboard.md")
    yield os.path.join(REPO, "memory", "trade_log.md")
    vdir = os.path.join(REPO, "variants")
    if os.path.isdir(vdir):
        for name in os.listdir(vdir):
            if name == "archive":
                continue
            for fn in ("portfolio.md", "trade_log.md"):
                p = os.path.join(vdir, name, fn)
                if os.path.isfile(p):
                    yield p


def check_future_timestamps(now, findings):
    limit = now + FUTURE_TOLERANCE
    for path in iter_state_files():
        rel = os.path.relpath(path, REPO)
        try:
            with open(path, encoding="utf-8") as f:
                for i, line in enumerate(f, 1):
                    interesting = ("Last rebuild" in line or "Last refresh" in line
                                   or re.match(r"\s*\|\s*20\d\d-", line))
                    if not interesting:
                        continue
                    ts = parse_iso(line)
                    if ts and ts > limit:
                        findings.append(f"B future-timestamp: {rel}:{i} has "
                                        f"{ts.isoformat()} (now {now.isoformat(timespec='minutes')}) "
                                        f"— +1-day mislabel bug class")
        except OSError as e:
            findings.append(f"B future-timestamp: cannot read {rel}: {e}")


def check_dirty_tree(findings):
    code, out, _ = git("status", "--porcelain")
    if code == 0 and out:
        entries = out.splitlines()
        shown = ", ".join(e.strip() for e in entries[:10])
        more = f" (+{len(entries)-10} more)" if len(entries) > 10 else ""
        findings.append(f"C dirty-tree: {len(entries)} uncommitted change(s): {shown}{more} "
                        f"— stranded work from a previous session?")


def check_stale_mtm(now, findings):
    for path in iter_state_files():
        if not path.endswith("portfolio.md"):
            continue
        rel = os.path.relpath(path, REPO)
        try:
            text = open(path, encoding="utf-8").read()
        except OSError:
            continue
        m = re.search(r"## Open positions\n(.*?)(?=\n## |\Z)", text, re.S)
        if not m or not re.search(r"\|\s*[A-Z]+/USD", m.group(1)):
            continue  # no open positions
        rebuild_line = next((ln for ln in text.splitlines() if "Last rebuild" in ln), "")
        ts = parse_iso(rebuild_line)
        if ts is None:
            findings.append(f"D stale-MTM: {rel} has open position(s) but no parsable "
                            f"Last rebuild timestamp")
        elif (now - ts).total_seconds() / 3600 > STALE_MTM_HOURS:
            findings.append(f"D stale-MTM: {rel} has open position(s) but last rebuild "
                            f"{(now - ts).total_seconds()/3600:.0f}h ago (threshold {STALE_MTM_HOURS}h)")


def check_scheduler_flag(findings):
    try:
        cfg = json.load(open(DESKTOP_CONFIG, encoding="utf-8"))
    except OSError:
        findings.append(f"E scheduler-flag: cannot read {DESKTOP_CONFIG} — "
                        f"cannot confirm scheduled tasks are enabled")
        return
    except json.JSONDecodeError as e:
        findings.append(f"E scheduler-flag: {DESKTOP_CONFIG} is not valid JSON ({e})")
        return
    val = cfg.get("ccdScheduledTasksEnabled")
    if val is False:
        findings.append("E scheduler-flag: ccdScheduledTasksEnabled is FALSE — "
                        "no BULL routine will fire (2026-05-24 incident class)")


def check_unpushed(findings):
    code, out, _ = git("rev-list", "--count", "origin/main..HEAD")
    if code == 0 and out.isdigit() and int(out) > 0:
        findings.append(f"F unpushed: local main is {out} commit(s) ahead of origin/main "
                        f"— routine pushes may be failing")


def check_mcp_paths(findings):
    mcp = os.path.join(REPO, ".mcp.json")
    if not os.path.isfile(mcp):
        return
    text = open(mcp, encoding="utf-8").read()
    for m in re.finditer(r"[A-Za-z]:[/\\][^\"']+", text):
        p = m.group(0)
        if not os.path.exists(p):
            findings.append(f"G mcp-path: .mcp.json references missing path {p} — "
                            f"MCP server cannot start (2026-06-02 outage class)")


def sanitize_tg(text):
    # telegram_send.py forces Markdown parse_mode; these chars cause HTTP 400
    return re.sub(r"[_*`\[\]]", "-", text)


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description="BULL ops watchdog")
    ap.add_argument("--telegram", action="store_true",
                    help="send a Telegram alert if there are findings")
    args = ap.parse_args()

    now = datetime.now(timezone.utc)
    pt = now.astimezone(ZoneInfo("America/Los_Angeles"))
    findings = []

    check_heartbeats(now, findings)
    check_future_timestamps(now, findings)
    check_dirty_tree(findings)
    check_stale_mtm(now, findings)
    check_scheduler_flag(findings)
    check_unpushed(findings)
    check_mcp_paths(findings)

    print(f"# BULL watchdog — {now.isoformat(timespec='seconds')} "
          f"(PT {pt:%Y-%m-%d %H:%M})")
    if not findings:
        print("ALL CLEAR — heartbeats, timestamps, tree, MTM, scheduler flag, push state, MCP paths OK")
        sys.exit(0)

    print(f"{len(findings)} FINDING(S):")
    for f in findings:
        print(f"  - {f}")

    if args.telegram:
        msg = sanitize_tg(
            f"BULL WATCHDOG - {len(findings)} finding(s) at {pt:%Y-%m-%d %H:%M} PT\n"
            + "\n".join(f"- {f}" for f in findings[:10])
            + (f"\n(+{len(findings)-10} more)" if len(findings) > 10 else "")
        )
        r = subprocess.run([sys.executable, os.path.join(REPO, "scripts", "telegram_send.py"), msg],
                           capture_output=True, text=True)
        print(f"telegram: {'sent' if r.returncode == 0 else 'FAILED: ' + (r.stderr or '').strip()}")

    sys.exit(1)


if __name__ == "__main__":
    main()
