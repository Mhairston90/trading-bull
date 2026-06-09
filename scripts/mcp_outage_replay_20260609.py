#!/usr/bin/env python3
"""
MCP-outage replay — 2026-06-09 interactive session.

Kraken MCP was unavailable from 2026-06-02T15:00Z through 2026-06-09 (folder
rename broke the server path). This script reconstructs what BULL main v0.4
would have done at every missed overnight (13:00Z) / EOD (04:00Z) entry-scan
wake, and resolves the LAB variants' open HYPE/USD position, using Kraken's
public REST OHLC endpoint (same venue/bars the MCP would have served).

Outputs a wake-by-wake audit log to stdout and caches raw OHLC JSON under
scripts/replay_cache_20260609/ for audit.

Replay conventions (matched to memory/strategy.md v0.4 + trade_log precedent):
- Entry scans only at wakes; entry price = close of last closed 1H bar.
- Exits evaluated at every 1H close (no intra-bar exits) for MAIN.
- Stop = entry - 2*ATR14(1H, Wilder); target = entry + 4*stop_distance.
- Size = equity*0.015 / stop_distance (6dp).
- Breakeven ratchet: stop -> entry once a 1H close shows unrealized >= 2R.
- Exit precedence at a close: stop-hit, 4R-target, two-consecutive-EMA.
- SBD classification at wakes (<=1/15 positive 24h AND median <= -1.0%);
  while active, EMA exit uses 9-EMA instead of 20-EMA (still 2-bar confirm).
- Regime gate 5a: <4/15 pairs positive 24h at scan -> reject all entries.
- Volume floor 4a: sum(vwap*volume) of last 24 1H bars >= $2.0M.
- RSI floor/cap: 55 < RSI14 <= 80. 1H close > EMA20, 4H close > EMA50.
- Max 1 entry/wake (rule 8, highest universe rank first), max 4 open (rule 6),
  cluster {BTC,ETH,SOL,TAO,AVAX,SUI,LINK} <= 2 (6a), portfolio risk cap 4% (7),
  24h same-pair cooldown after stop-out (5b).
- VARIANT HYPE position uses intra-bar stop check (low <= stop -> exit at stop)
  per routine-07 precedent ("min since entry 66.22 > stop 66.13").
"""

import json
import os
import time
import urllib.request
from datetime import datetime, timezone, timedelta

CACHE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "replay_cache_20260609")
os.makedirs(CACHE_DIR, exist_ok=True)

UNIVERSE = [  # (rank order = universe.md 2026-06-01), kraken api symbol
    ("BTC/USD", "XXBTZUSD"),
    ("ETH/USD", "XETHZUSD"),
    ("SOL/USD", "SOLUSD"),
    ("HYPE/USD", "HYPEUSD"),
    ("XRP/USD", "XXRPZUSD"),
    ("SUI/USD", "SUIUSD"),
    ("TAO/USD", "TAOUSD"),
    ("XDG/USD", "XDGUSD"),
    ("NEAR/USD", "NEARUSD"),
    ("ADA/USD", "ADAUSD"),
    ("LINK/USD", "LINKUSD"),
    ("LTC/USD", "XLTCZUSD"),
    ("FARTCOIN/USD", "FARTCOINUSD"),
    ("TRX/USD", "TRXUSD"),
    ("AVAX/USD", "AVAXUSD"),
]
CLUSTER = {"BTC/USD", "ETH/USD", "SOL/USD", "TAO/USD", "AVAX/USD", "SUI/USD", "LINK/USD"}

START_EQUITY = 10254.63
LOSS_STREAK_START = 4
REPLAY_START = datetime(2026, 6, 2, 13, 0, tzinfo=timezone.utc)

VARIANT_HYPE = dict(entry=68.06, stop=66.13, target=75.80,
                    opened=datetime(2026, 5, 30, 13, 0, tzinfo=timezone.utc))


def fetch(pair_api, interval_min):
    fn = os.path.join(CACHE_DIR, f"{pair_api}_{interval_min}.json")
    if os.path.exists(fn):
        with open(fn) as f:
            return json.load(f)
    url = f"https://api.kraken.com/0/public/OHLC?pair={pair_api}&interval={interval_min}"
    with urllib.request.urlopen(url, timeout=30) as r:
        data = json.loads(r.read())
    if data.get("error"):
        raise RuntimeError(f"{pair_api}: {data['error']}")
    with open(fn, "w") as f:
        json.dump(data, f)
    time.sleep(1.1)  # public API rate courtesy
    return data


def bars_of(data):
    res = data["result"]
    key = [k for k in res if k != "last"][0]
    out = []
    for c in res[key]:
        out.append(dict(t=int(c[0]), o=float(c[1]), h=float(c[2]), l=float(c[3]),
                        c=float(c[4]), vwap=float(c[5]), vol=float(c[6])))
    return out


def ema_series(closes, period):
    k = 2.0 / (period + 1)
    out, e = [], None
    for c in closes:
        e = c if e is None else c * k + e * (1 - k)
        out.append(e)
    return out


def rsi_series(closes, period=14):
    out = [None] * len(closes)
    gains, losses = 0.0, 0.0
    ag = al = None
    for i in range(1, len(closes)):
        ch = closes[i] - closes[i - 1]
        g, l = max(ch, 0.0), max(-ch, 0.0)
        if i <= period:
            gains += g
            losses += l
            if i == period:
                ag, al = gains / period, losses / period
                out[i] = 100.0 if al == 0 else 100 - 100 / (1 + ag / al)
        else:
            ag = (ag * (period - 1) + g) / period
            al = (al * (period - 1) + l) / period
            out[i] = 100.0 if al == 0 else 100 - 100 / (1 + ag / al)
    return out


def atr_series(bars, period=14):
    out = [None] * len(bars)
    trs = []
    a = None
    for i in range(1, len(bars)):
        tr = max(bars[i]["h"] - bars[i]["l"],
                 abs(bars[i]["h"] - bars[i - 1]["c"]),
                 abs(bars[i]["l"] - bars[i - 1]["c"]))
        if a is None:
            trs.append(tr)
            if len(trs) == period:
                a = sum(trs) / period
                out[i] = a
        else:
            a = (a * (period - 1) + tr) / period
            out[i] = a
    return out


print("Fetching Kraken OHLC (public REST)...")
H1, H4 = {}, {}
for name, sym in UNIVERSE:
    H1[name] = bars_of(fetch(sym, 60))
    H4[name] = bars_of(fetch(sym, 240))
    print(f"  {name}: {len(H1[name])} 1H bars ({datetime.fromtimestamp(H1[name][0]['t'], tz=timezone.utc):%m-%d %H:%M} -> "
          f"{datetime.fromtimestamp(H1[name][-1]['t'], tz=timezone.utc):%m-%d %H:%M}), {len(H4[name])} 4H bars")

# Drop the still-forming last bar (timestamp == current hour/4h open)
now = int(time.time())
for name, _ in UNIVERSE:
    if H1[name][-1]["t"] > now - 3600:
        H1[name] = H1[name][:-1]
    if H4[name][-1]["t"] > now - 14400:
        H4[name] = H4[name][:-1]

IND = {}
for name, _ in UNIVERSE:
    closes1 = [b["c"] for b in H1[name]]
    closes4 = [b["c"] for b in H4[name]]
    IND[name] = dict(
        ema20=ema_series(closes1, 20),
        ema9=ema_series(closes1, 9),
        rsi=rsi_series(closes1, 14),
        atr=atr_series(H1[name], 14),
        ema50_4h=ema_series(closes4, 50),
    )


def idx_last_closed(bars, ts):
    """Index of last bar fully closed at datetime ts (1H bars)."""
    epoch = int(ts.timestamp())
    lo = None
    for i, b in enumerate(bars):
        if b["t"] + 3600 <= epoch:
            lo = i
        else:
            break
    return lo


def idx_last_closed_4h(bars, ts):
    epoch = int(ts.timestamp())
    lo = None
    for i, b in enumerate(bars):
        if b["t"] + 14400 <= epoch:
            lo = i
        else:
            break
    return lo


def regime(ts):
    """(n_positive, median_24h_change, per-pair changes) at scan time ts."""
    chs = {}
    for name, _ in UNIVERSE:
        i = idx_last_closed(H1[name], ts)
        if i is None or i < 24:
            continue
        chs[name] = (H1[name][i]["c"] - H1[name][i - 24]["c"]) / H1[name][i - 24]["c"] * 100
    vals = sorted(chs.values())
    n_pos = sum(1 for v in vals if v > 0)
    m = len(vals)
    med = vals[m // 2] if m % 2 else (vals[m // 2 - 1] + vals[m // 2]) / 2
    return n_pos, med, chs


# ---------- wake list ----------
wakes = []
d = REPLAY_START
end = datetime.now(timezone.utc)
while d <= end:
    wakes.append(("overnight" if d.hour == 13 else "eod", d))
    d = d + timedelta(hours=9 if d.hour == 4 else 15)  # 04Z -> 13Z same day; 13Z -> 04Z next day

# ---------- main replay ----------
equity = START_EQUITY
open_pos = []   # dicts: pair, size, entry, stop, target, dist, opened, be_armed
closed = []
cooldown_until = {}   # pair -> dt (24h after stop-out)
sbd_active = False
loss_streak = LOSS_STREAK_START
daily_realized = {}   # PT date -> $
log = []


def pt_day(ts):
    return (ts - timedelta(hours=7)).date()


def close_position(pos, ts, price, tag):
    global equity
    r = (price - pos["entry"]) / pos["dist"]
    pnl = pos["size"] * (price - pos["entry"])
    equity += pnl
    daily_realized[pt_day(ts)] = daily_realized.get(pt_day(ts), 0.0) + pnl
    closed.append(dict(pair=pos["pair"], ts=ts, price=price, r=r, pnl=pnl, tag=tag, pos=pos))
    log.append(f"  CLOSE {pos['pair']} @ {price:.6g} ({ts:%Y-%m-%dT%H:%M}Z) {tag} "
               f"R={r:+.2f} PnL=${pnl:+.2f} equity=${equity:,.2f}")


def replay_exits(upto):
    """Walk 1H closes for open positions up to datetime `upto`."""
    for pos in list(open_pos):
        bars = H1[pos["pair"]]
        ind = IND[pos["pair"]]
        i0 = idx_last_closed(bars, pos["last_checked"]) + 1 if pos.get("last_checked") else idx_last_closed(bars, pos["opened"]) + 1
        i1 = idx_last_closed(bars, upto)
        below = pos.get("below_count", 0)
        for i in range(i0, i1 + 1):
            bts = datetime.fromtimestamp(bars[i]["t"] + 3600, tz=timezone.utc)
            c = bars[i]["c"]
            # breakeven ratchet first (a close can't be both >=2R and at stop)
            if not pos["be_armed"] and (c - pos["entry"]) >= 2 * pos["dist"]:
                pos["stop"] = max(pos["stop"], pos["entry"])
                pos["be_armed"] = True
                log.append(f"  RATCHET {pos['pair']} breakeven armed @ {bts:%m-%d %H:%M}Z (close {c:.6g} >= +2R)")
            if c <= pos["stop"]:
                tag = "exit-stop-hit-mcp-outage-replay"
                close_position(pos, bts, c, tag)
                if c <= pos["entry"] - pos["dist"] * 0.5:  # genuine stop-out -> 5b cooldown
                    cooldown_until[pos["pair"]] = bts + timedelta(hours=24)
                open_pos.remove(pos)
                break
            if (c - pos["entry"]) >= 4 * pos["dist"]:
                close_position(pos, bts, c, "exit-4R-target-mcp-outage-replay")
                open_pos.remove(pos)
                break
            ema = ind["ema9"][i] if sbd_active else ind["ema20"][i]
            if c < ema:
                below += 1
                if below >= 2:
                    tag = ("exit-ema9-sbd-confirm" if sbd_active else "exit-ema20-confirm") + "-mcp-outage-replay"
                    close_position(pos, bts, c, tag)
                    open_pos.remove(pos)
                    break
            else:
                below = 0
        else:
            pos["below_count"] = below
            pos["last_checked"] = upto


for wake_name, wts in wakes:
    log.append(f"\n== {wake_name.upper()} wake {wts:%Y-%m-%dT%H:%M}Z ==")
    # 1) exits up to this wake
    replay_exits(wts)
    # 2) kill switches
    day = pt_day(wts)
    if daily_realized.get(day, 0.0) < -0.05 * equity:
        log.append("  KILL: daily loss >5% — entries halted this wake")
        continue
    # 3) regime
    n_pos, med, chs = regime(wts)
    sbd_now = (n_pos <= 1 and med <= -1.0)
    sbd_active = sbd_now
    log.append(f"  regime: {n_pos}/15 positive, median {med:+.2f}% -> "
               f"{'SBD ACTIVE' if sbd_now else ('5a FAIL' if n_pos < 4 else 'OK')}")
    if n_pos < 4:
        continue
    # 4) entry scan, universe-rank order, max 1 per wake
    for name, _ in UNIVERSE:
        if any(p["pair"] == name for p in open_pos):
            continue
        if name in cooldown_until and wts < cooldown_until[name]:
            log.append(f"  {name}: 5b cooldown until {cooldown_until[name]:%m-%d %H:%M}Z")
            continue
        if len(open_pos) >= 4:
            log.append("  rule 6: 4 open positions — no entry")
            break
        i = idx_last_closed(H1[name], wts)
        j = idx_last_closed_4h(H4[name], wts)
        if i is None or j is None or i < 30:
            continue
        b = H1[name][i]
        ind = IND[name]
        c1, e20, r14, a14 = b["c"], ind["ema20"][i], ind["rsi"][i], ind["atr"][i]
        c4, e50 = H4[name][j]["c"], ind["ema50_4h"][j]
        vol24 = sum(x["vwap"] * x["vol"] for x in H1[name][i - 23:i + 1])
        checks = dict(
            r1_ema=c1 > e20,
            r2_rsi=55 < r14 <= 80,
            r3_4h=c4 > e50,
            r4a_vol=vol24 >= 2_000_000,
        )
        if not all(checks.values()):
            fails = ",".join(k for k, v in checks.items() if not v)
            log.append(f"  {name}: blocked ({fails}) close={c1:.6g} ema20={e20:.6g} rsi={r14:.1f} "
                       f"4h={c4:.6g} ema50_4h={e50:.6g} vol24=${vol24/1e6:.1f}M")
            continue
        cluster_n = sum(1 for p in open_pos if p["pair"] in CLUSTER)
        if name in CLUSTER and cluster_n >= 2:
            log.append(f"  {name}: cluster cap (6a)")
            continue
        risk_now = sum((p["entry"] - p["stop"]) * p["size"] / equity for p in open_pos if p["stop"] < p["entry"])
        if risk_now + 0.015 > 0.04:
            log.append(f"  {name}: risk cap (7) {risk_now:.3f}+1.5%>4%")
            continue
        dist = 2 * a14
        size = round(equity * 0.015 / dist, 6)
        pos = dict(pair=name, size=size, entry=c1, stop=c1 - dist, target=c1 + 4 * dist,
                   dist=dist, opened=wts, be_armed=False, below_count=0, last_checked=wts)
        open_pos.append(pos)
        log.append(f"  OPEN {name} long {size:.6g} @ {c1:.6g} stop {c1-dist:.6g} target {c1+4*dist:.6g} "
                   f"(rsi {r14:.1f}, vol24 ${vol24/1e6:.0f}M, atr {a14:.6g}) equity=${equity:,.2f}")
        break  # rule 8: one entry per wake

# final exit sweep to latest closed bar
replay_exits(end)

print("\n".join(log))
print("\n===== MAIN SUMMARY =====")
print(f"closed trades: {len(closed)}")
for c in closed:
    print(f"  {c['pos']['opened']:%m-%dT%H:%M}Z OPEN {c['pair']} {c['pos']['size']:.6g} @ {c['pos']['entry']:.6g} "
          f"-> {c['ts']:%m-%dT%H:%M}Z {c['tag']} @ {c['price']:.6g} R={c['r']:+.2f} PnL=${c['pnl']:+.2f}")
print(f"open positions at end: {len(open_pos)}")
for p in open_pos:
    bars = H1[p["pair"]]
    mtm = bars[idx_last_closed(bars, end)]["c"]
    upnl = p["size"] * (mtm - p["entry"])
    print(f"  {p['pair']} {p['size']:.6g} @ {p['entry']:.6g} stop {p['stop']:.6g} target {p['target']:.6g} "
          f"opened {p['opened']:%m-%dT%H:%M}Z MTM {mtm:.6g} uPnL ${upnl:+.2f} be_armed={p['be_armed']}")
print(f"equity (cash basis): ${equity:,.2f}")

# ---------- momentum-variant full replay ----------
# v0.5 / v0.10 / v0.11 / v0.12 from 2026-05-31T13:00Z (first wake after the last
# successful routine-07 sim, whose data cutoff was 2026-05-31T05:00Z).
# All four share v0.2 entry rules (v0.5: cluster cap 1 instead of 2).
# Exit modes: v0.5/v0.11 single-bar EMA20; v0.10 2-bar EMA20; v0.12 single-bar
# EMA20 (EMA9 while SBD active at last wake classification). v0.11 adds the
# breakeven-at-2R ratchet. Variant convention: stop is INTRA-BAR at stop price
# (v0.2 convention); EMA/4R exits at 1H close.

VSTART = datetime(2026, 5, 31, 13, 0, tzinfo=timezone.utc)
vwakes = []
d = VSTART
while d <= end:
    vwakes.append(d)
    d = d + timedelta(hours=9 if d.hour == 4 else 15)


def replay_variant(name, equity0, exit_mode, breakeven=False, sbd_exit=False, cluster_cap=2):
    eq = equity0
    pos = dict(pair="HYPE/USD", size=77 if equity0 == 10000.0 else 76,
               entry=68.06, stop=66.13, target=75.80, dist=1.93,
               opened=VARIANT_HYPE["opened"], be_armed=False, below=0)
    positions = [pos]
    vclosed = []
    vlog = [f"\n----- {name} (start equity ${equity0:,.2f}, exit={exit_mode}{'+BE' if breakeven else ''}{'+SBD' if sbd_exit else ''}) -----"]
    sbd = False
    cooldowns = {}

    def vexits(upto):
        nonlocal eq
        for p in list(positions):
            bars = H1[p["pair"]]
            ind = IND[p["pair"]]
            i0 = idx_last_closed(bars, p.get("chk", p["opened"])) + 1
            i1 = idx_last_closed(bars, upto)
            for i in range(i0, i1 + 1):
                bts = datetime.fromtimestamp(bars[i]["t"] + 3600, tz=timezone.utc)
                lo, c = bars[i]["l"], bars[i]["c"]
                if breakeven and not p["be_armed"] and (c - p["entry"]) >= 2 * p["dist"]:
                    p["stop"] = max(p["stop"], p["entry"])
                    p["be_armed"] = True
                    vlog.append(f"  RATCHET {p['pair']} stop->breakeven @ {bts:%m-%d %H:%M}Z")
                if lo <= p["stop"]:  # intra-bar stop, exit AT stop price
                    px = p["stop"]
                    r = (px - p["entry"]) / p["dist"]
                    pnl = p["size"] * (px - p["entry"])
                    eq += pnl
                    vclosed.append((p, bts, px, r, pnl, "exit-stop-hit"))
                    vlog.append(f"  CLOSE {p['pair']} @ {px:.6g} ({bts:%m-%dT%H:%M}Z) exit-stop-hit R={r:+.2f} PnL=${pnl:+.2f} eq=${eq:,.2f}")
                    if px < p["entry"]:
                        cooldowns[p["pair"]] = bts + timedelta(hours=24)
                    positions.remove(p)
                    break
                if (c - p["entry"]) >= 4 * p["dist"]:
                    r = (c - p["entry"]) / p["dist"]
                    pnl = p["size"] * (c - p["entry"])
                    eq += pnl
                    vclosed.append((p, bts, c, r, pnl, "exit-4R-target"))
                    vlog.append(f"  CLOSE {p['pair']} @ {c:.6g} ({bts:%m-%dT%H:%M}Z) exit-4R-target R={r:+.2f} PnL=${pnl:+.2f} eq=${eq:,.2f}")
                    positions.remove(p)
                    break
                ema = ind["ema9"][i] if (sbd_exit and sbd) else ind["ema20"][i]
                if c < ema:
                    p["below"] += 1
                    need = 2 if exit_mode == "2bar" else 1
                    if p["below"] >= need:
                        r = (c - p["entry"]) / p["dist"]
                        pnl = p["size"] * (c - p["entry"])
                        eq += pnl
                        tag = "exit-ema20-confirm" if exit_mode == "2bar" else ("exit-ema9-sbd" if (sbd_exit and sbd) else "exit-ema-cross")
                        vclosed.append((p, bts, c, r, pnl, tag))
                        vlog.append(f"  CLOSE {p['pair']} @ {c:.6g} ({bts:%m-%dT%H:%M}Z) {tag} R={r:+.2f} PnL=${pnl:+.2f} eq=${eq:,.2f}")
                        positions.remove(p)
                        break
                else:
                    p["below"] = 0
            else:
                p["chk"] = upto

    for wts in vwakes:
        vexits(wts)
        n_pos, med, _ = regime(wts)
        sbd = (n_pos <= 1 and med <= -1.0)
        if n_pos < 4:
            vlog.append(f"  wake {wts:%m-%dT%H:%M}Z regime {n_pos}/15 med {med:+.2f}% -> {'SBD' if sbd else '5a FAIL'} (no entries)")
            continue
        for pname, _ in UNIVERSE:
            if any(p["pair"] == pname for p in positions):
                continue
            if pname in cooldowns and wts < cooldowns[pname]:
                continue
            if len(positions) >= 4:
                break
            i = idx_last_closed(H1[pname], wts)
            j = idx_last_closed_4h(H4[pname], wts)
            if i is None or j is None or i < 30:
                continue
            b = H1[pname][i]
            ind = IND[pname]
            c1, e20, r14, a14 = b["c"], ind["ema20"][i], ind["rsi"][i], ind["atr"][i]
            c4, e50 = H4[pname][j]["c"], ind["ema50_4h"][j]
            vol24 = sum(x["vwap"] * x["vol"] for x in H1[pname][i - 23:i + 1])
            if not (c1 > e20 and 55 < r14 <= 80 and c4 > e50 and vol24 >= 2_000_000):
                continue
            cl_n = sum(1 for p in positions if p["pair"] in CLUSTER)
            if pname in CLUSTER and cl_n >= cluster_cap:
                continue
            risk_now = sum((p["entry"] - p["stop"]) * p["size"] / eq for p in positions if p["stop"] < p["entry"])
            if risk_now + 0.015 > 0.04:
                continue
            dist = 2 * a14
            size = round(eq * 0.015 / dist, 6)
            positions.append(dict(pair=pname, size=size, entry=c1, stop=c1 - dist, target=c1 + 4 * dist,
                                  dist=dist, opened=wts, be_armed=False, below=0, chk=wts))
            vlog.append(f"  OPEN {pname} {size:.6g} @ {c1:.6g} stop {c1-dist:.6g} target {c1+4*dist:.6g} "
                        f"({wts:%m-%dT%H:%M}Z wake, rsi {r14:.1f}) eq=${eq:,.2f}")
            break
    vexits(end)
    print("\n".join(vlog))
    print(f"  -> final: {len(vclosed)} closes, {len(positions)} open, equity ${eq + sum(p['size']*(H1[p['pair']][idx_last_closed(H1[p['pair']], end)]['c']-p['entry']) for p in positions):,.2f} "
          f"(cash ${eq:,.2f})")
    for p in positions:
        mtm = H1[p["pair"]][idx_last_closed(H1[p["pair"]], end)]["c"]
        print(f"     OPEN {p['pair']} {p['size']:.6g} @ {p['entry']:.6g} stop {p['stop']:.6g} MTM {mtm:.6g} uPnL ${p['size']*(mtm-p['entry']):+.2f}")
    return eq, positions, vclosed


print("\n===== MOMENTUM-VARIANT FULL REPLAY (2026-05-31T13:00Z -> now) =====")
replay_variant("v0.5-cluster-cap-tight", 10000.00, "1bar", cluster_cap=1)
replay_variant("v0.10-exit-confirm", 10000.00, "2bar")
replay_variant("v0.11-breakeven-2R", 10000.00, "1bar", breakeven=True)
replay_variant("v0.12-sbd-exit", 9863.26, "1bar", sbd_exit=True)

# ---------- gate verification for non-momentum variants ----------
# vol-comp variants (v0.3/v0.7/v0.13): require 1H ATR14 < threshold x 30d-mean ATR
#   (v0.3/v0.13 threshold 0.5, v0.7 0.7) ON TOP of the momentum rules above.
# mean-rev variants (v0.4-mr/v0.8/v0.9): require M1 4H close > 4H 200-EMA AND
#   M2 1H RSI14 < {25,30,20}. Verify whether any pair passed at any gap wake.
print("\n===== NON-MOMENTUM VARIANT GATE CHECK (all gap wakes) =====")
viol = []
for wts in vwakes:
    for pname, _ in UNIVERSE:
        i = idx_last_closed(H1[pname], wts)
        j = idx_last_closed_4h(H4[pname], wts)
        if i is None or j is None or i < 40:
            continue
        ind = IND[pname]
        atr_now = ind["atr"][i]
        atr_hist = [a for a in ind["atr"][max(14, i - 719):i + 1] if a is not None]
        atr_mean30 = sum(atr_hist) / len(atr_hist)
        closes4 = [b["c"] for b in H4[pname]]
        ema200_4h = ema_series(closes4, 200)[j]
        c4 = H4[pname][j]["c"]
        r14 = ind["rsi"][i]
        if atr_now < 0.7 * atr_mean30:
            viol.append(f"  {wts:%m-%dT%H:%M}Z {pname}: VOL-COMP gate OPEN (atr {atr_now:.4g} < 0.7x mean {atr_mean30:.4g})"
                        + (" [also <0.5x]" if atr_now < 0.5 * atr_mean30 else ""))
        if c4 > ema200_4h and r14 < 30:
            viol.append(f"  {wts:%m-%dT%H:%M}Z {pname}: MEAN-REV M1 PASS + RSI {r14:.1f} < 30 (M2 candidate)")
print("\n".join(viol) if viol else "  (no wake/pair combination opened any vol-comp or mean-rev gate — all 6 variants correctly idle)")

# ---------- variant HYPE resolution ----------
print("\n===== VARIANT HYPE/USD RESOLUTION =====")
vb = H1["HYPE/USD"]
vi = IND["HYPE/USD"]
start_i = idx_last_closed(vb, VARIANT_HYPE["opened"]) + 1
be_level = VARIANT_HYPE["entry"] + 2 * (VARIANT_HYPE["entry"] - VARIANT_HYPE["stop"])
events = []
below20 = below9 = 0
be_armed_ts = None
for i in range(start_i, len(vb)):
    bts = datetime.fromtimestamp(vb[i]["t"] + 3600, tz=timezone.utc)
    lo, hi, c = vb[i]["l"], vb[i]["h"], vb[i]["c"]
    if be_armed_ts is None and c >= be_level:
        be_armed_ts = bts
        events.append((bts, f"breakeven 2R armed (close {c:.6g} >= {be_level:.6g})"))
    if lo <= VARIANT_HYPE["stop"]:
        events.append((bts, f"STOP HIT intra-bar (low {lo:.6g} <= 66.13)"))
        break
    if hi >= VARIANT_HYPE["target"]:
        events.append((bts, f"TARGET touched intra-bar (high {hi:.6g} >= 75.80)"))
    if c < vi["ema20"][i]:
        below20 += 1
        if below20 == 1:
            events.append((bts, f"1st close < EMA20 (close {c:.6g} < ema {vi['ema20'][i]:.6g}) -> SINGLE-BAR EMA exit would fire here @ {c:.6g}"))
        if below20 == 2:
            events.append((bts, f"2nd consec close < EMA20 (close {c:.6g} < ema {vi['ema20'][i]:.6g}) -> 2-bar EMA exit fires @ {c:.6g}"))
    else:
        below20 = 0
print(f"entry 68.06 @ 2026-05-30T13:00Z, stop 66.13, target 75.80, 2R/breakeven level {be_level:.4g}")
for ts, msg in events:
    print(f"  {ts:%Y-%m-%dT%H:%M}Z  {msg}")
