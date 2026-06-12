#!/usr/bin/env python3
"""
BULL git hook checks — mechanical enforcement of guards that previously lived
only as prose in routine specs.

Blocks at commit time:
  1. Secrets — telegram bot token / firecrawl key formats, or assignments to
     TELEGRAM_BOT_TOKEN / TELEGRAM_BULL_CHAT_ID / FIRECRAWL_API_KEY (mandate:
     secrets never enter this repo)
  2. Future timestamps — staged Last rebuild / Last refresh lines and
     trade-log rows dated > now+2h (the +1-day UTC/PT mislabel class that
     stamped 2026-06-13 timestamps on 2026-06-11)
  3. Commit-message dates — "routine-XX-name YYYY-MM-DD" subjects must carry
     the PT calendar date (today or yesterday PT; never the future). Routines
     03/06/07 fire past UTC midnight and mislabeled +1 day twice.

Modes:
  --staged            pre-commit hook: scan staged diff (checks 1+2)
  --commit-msg FILE   commit-msg hook: validate routine subject date (check 3)
  --install           write .git/hooks/pre-commit and commit-msg shims

Routines must NOT bypass with --no-verify; a hook rejection means the wake is
about to write a known bug class — fix the content, don't skip the check.
"""

import argparse
import os
import re
import stat
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ISO_RE = re.compile(r"(20\d\d-\d\d-\d\d)T(\d\d):(\d\d)(?::\d\d)?Z")
FUTURE_TOLERANCE = timedelta(hours=2)

SECRET_PATTERNS = [
    (re.compile(r"\b\d{8,10}:[A-Za-z0-9_-]{30,}\b"), "telegram bot token format"),
    (re.compile(r"\bfc-[A-Za-z0-9]{16,}\b"), "firecrawl API key format"),
    (re.compile(r"(TELEGRAM_BOT_TOKEN|TELEGRAM_BULL_CHAT_ID|FIRECRAWL_API_KEY)"
                r"\s*[:=]\s*['\"]?[A-Za-z0-9]"), "secret env var assigned a literal value"),
]
PLACEHOLDER_HINTS = ("your", "xxx", "...", "<", "example", "placeholder")


def git(*args):
    r = subprocess.run(["git", "-C", REPO, *args],
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    return r.returncode, (r.stdout or ""), (r.stderr or "")


def parse_iso(line):
    m = ISO_RE.search(line)
    if not m:
        return None
    d, hh, mm = m.group(1), int(m.group(2)), int(m.group(3))
    y, mo, dd = (int(x) for x in d.split("-"))
    return datetime(y, mo, dd, hh, mm, tzinfo=timezone.utc)


def staged_added_lines():
    """Yield (path, line_text) for every added line in the staged diff."""
    code, out, err = git("diff", "--cached", "--unified=0")
    if code != 0:
        sys.exit(f"pre-commit: git diff --cached failed: {err}")
    path = None
    for line in out.splitlines():
        if line.startswith("+++ b/"):
            path = line[6:]
        elif line.startswith("+") and not line.startswith("+++") and path:
            yield path, line[1:]


def check_staged():
    now = datetime.now(timezone.utc)
    limit = now + FUTURE_TOLERANCE
    problems = []
    for path, text in staged_added_lines():
        for pat, label in SECRET_PATTERNS:
            m = pat.search(text)
            if m and not any(h in text.lower() for h in PLACEHOLDER_HINTS):
                problems.append(f"SECRET ({label}) in {path}: {text.strip()[:80]}")
        if path.startswith(("memory/", "variants/")) and path.endswith(".md"):
            interesting = ("Last rebuild" in text or "Last refresh" in text
                           or re.match(r"\s*\|\s*20\d\d-", text))
            if interesting:
                ts = parse_iso(text)
                if ts and ts > limit:
                    problems.append(
                        f"FUTURE TIMESTAMP in {path}: {ts.isoformat()} "
                        f"(now {now.isoformat(timespec='minutes')}) — "
                        f"+1-day UTC/PT mislabel? Label with the PT calendar date.")
    return problems


def check_commit_msg(msg_file):
    try:
        first = open(msg_file, encoding="utf-8", errors="replace").readline().strip()
    except OSError as e:
        sys.exit(f"commit-msg: cannot read {msg_file}: {e}")
    m = re.search(r"routine-\d\d-\S+\s+(\d{4})-(\d{2})-(\d{2})", first)
    if not m:
        return []  # only routine-labeled subjects are date-checked
    label = datetime(int(m.group(1)), int(m.group(2)), int(m.group(3))).date()
    today_pt = datetime.now(ZoneInfo("America/Los_Angeles")).date()
    if label > today_pt:
        return [f"COMMIT-MSG DATE {label} is in the future (today PT is {today_pt}). "
                f"Routines that fire past UTC midnight must label with the PT date, "
                f"not the UTC date."]
    if (today_pt - label).days > 1:
        return [f"COMMIT-MSG DATE {label} is {(today_pt - label).days} days old "
                f"(today PT is {today_pt}) — wrong wake label?"]
    return []


SHIM = """#!/bin/sh
# auto-installed by scripts/pre_commit_check.py --install
exec python "$(git rev-parse --show-toplevel)/scripts/pre_commit_check.py" {mode}
"""


def install():
    code, hooks_dir, err = git("rev-parse", "--git-path", "hooks")
    if code != 0:
        sys.exit(f"install: {err}")
    hooks_dir = os.path.join(REPO, hooks_dir.strip()) if not os.path.isabs(hooks_dir.strip()) \
        else hooks_dir.strip()
    os.makedirs(hooks_dir, exist_ok=True)
    for name, mode in (("pre-commit", "--staged"), ("commit-msg", '--commit-msg "$1"')):
        p = os.path.join(hooks_dir, name)
        with open(p, "w", encoding="utf-8", newline="\n") as f:
            f.write(SHIM.format(mode=mode))
        os.chmod(p, os.stat(p).st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
        print(f"installed {p}")


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description="BULL git hook checks")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--staged", action="store_true")
    g.add_argument("--commit-msg", metavar="FILE")
    g.add_argument("--install", action="store_true")
    args = ap.parse_args()

    if args.install:
        install()
        return

    problems = check_staged() if args.staged else check_commit_msg(args.commit_msg)
    if problems:
        print("COMMIT BLOCKED by scripts/pre_commit_check.py:")
        for p in problems:
            print(f"  - {p}")
        print("Fix the content (do not bypass with --no-verify).")
        sys.exit(1)


if __name__ == "__main__":
    main()
