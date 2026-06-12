#!/usr/bin/env python3
"""
BULL wake-time indicator engine.

Why this exists: routine wakes used to compute EMAs/RSI/ATR "in-line" (model
arithmetic over raw bars). On 2026-06-11 a ~60-bar-seeded 4H 50-EMA came out
$584 low, flipping BTC rule 3 to a false PASS and producing two void-entry
corrections (v0.5, v0.12). This script makes the math deterministic: full
720-bar warm-up, Wilder RSI/ATR, one converged table the wake reads instead
of computing.

Usage (from repo root):
    python scripts/indicators.py            # markdown table to stdout
    python scripts/indicators.py --json indicators.json
    python scripts/indicators.py --pair BTC/USD

What it computes per universe pair (closed bars only — the still-forming
candle is dropped):
    1H: close, EMA20, RSI14 (Wilder), ATR14 (Wilder), 30d mean ATR14,
        24h %change (close vs close 24 bars back), 24h notional (sum vwap*vol)
    4H: close, EMA50, EMA20 (v0.14), warm-up bar count
    Rule margins (strategy.md v0.4):
        R1  1H close > 1H EMA20
        R2  RSI14 >= 55 ; R2a RSI14 < 80
        R3  4H close > 4H EMA50   (R3-20: vs EMA20, for v0.14)
        R4a 24h notional >= $2.0M
        5c  vol-comp gates: ATR < 0.5x / 0.7x 30d mean ATR (v0.3 / v0.7)
        sizing helpers: 2xATR stop distance, 4R target
    Regime (gate 5a / SBD): count of pairs positive 24h, median 24h %.
        5a PASS if >= 4/15 positive; SBD ACTIVE if <= 1 positive AND median <= -1.0%.

Confidence: 4H 50-EMA needs >= 200 bars to converge (routine spec 2026-06-11).
Pairs with < 150 4H bars are flagged LOW-CONFIDENCE on R3.

This script reads public Kraken REST only. It makes no trade decisions —
sizing, cluster caps, cooldowns, and entry/exit choices stay with the routine,
which has portfolio state.
"""

import argparse
import json
import statistics
import sys
import time
import urllib.request
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

UNIVERSE = [  # rank order = memory/universe.md 2026-06-01; kraken REST symbol
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

RSI_FLOOR = 55.0
RSI_CAP = 80.0
NOTIONAL_FLOOR = 2_000_000.0
CONVERGED_4H_BARS = 200
LOW_CONFIDENCE_4H_BARS = 150


def fetch_bars(pair_api, interval_min, retries=3):
    url = f"https://api.kraken.com/0/public/OHLC?pair={pair_api}&interval={interval_min}"
    last_err = None
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(url, timeout=30) as r:
                data = json.loads(r.read())
            if data.get("error"):
                raise RuntimeError(str(data["error"]))
            res = data["result"]
            key = [k for k in res if k != "last"][0]
            bars = [dict(t=int(c[0]), o=float(c[1]), h=float(c[2]), l=float(c[3]),
                         c=float(c[4]), vwap=float(c[5]), vol=float(c[6]))
                    for c in res[key]]
            # drop the still-forming bar
            now = time.time()
            if bars and now - bars[-1]["t"] < interval_min * 60:
                bars = bars[:-1]
            return bars
        except Exception as e:  # noqa: BLE001 - report after retries
            last_err = e
            time.sleep(2 * (attempt + 1))
    raise RuntimeError(f"{pair_api} {interval_min}m: fetch failed after {retries} tries: {last_err}")


def ema(closes, period):
    if len(closes) < period:
        return None
    e = sum(closes[:period]) / period  # SMA seed
    k = 2.0 / (period + 1)
    for c in closes[period:]:
        e = c * k + e * (1 - k)
    return e


def rsi_wilder(closes, period=14):
    if len(closes) < period + 1:
        return None
    gains, losses = 0.0, 0.0
    for i in range(1, period + 1):
        d = closes[i] - closes[i - 1]
        gains += max(d, 0.0)
        losses += max(-d, 0.0)
    avg_g, avg_l = gains / period, losses / period
    for i in range(period + 1, len(closes)):
        d = closes[i] - closes[i - 1]
        avg_g = (avg_g * (period - 1) + max(d, 0.0)) / period
        avg_l = (avg_l * (period - 1) + max(-d, 0.0)) / period
    if avg_l == 0:
        return 100.0
    return 100.0 - 100.0 / (1.0 + avg_g / avg_l)


def atr_wilder_series(bars, period=14):
    if len(bars) < period + 1:
        return []
    trs = []
    for i in range(1, len(bars)):
        h, l, pc = bars[i]["h"], bars[i]["l"], bars[i - 1]["c"]
        trs.append(max(h - l, abs(h - pc), abs(l - pc)))
    out = [sum(trs[:period]) / period]
    for tr in trs[period:]:
        out.append((out[-1] * (period - 1) + tr) / period)
    return out


def analyze_pair(name, api):
    h1 = fetch_bars(api, 60)
    time.sleep(1.0)  # public API rate courtesy
    h4 = fetch_bars(api, 240)
    time.sleep(1.0)

    c1 = [b["c"] for b in h1]
    c4 = [b["c"] for b in h4]
    close1, close4 = c1[-1], c4[-1]

    atr_series = atr_wilder_series(h1)
    atr = atr_series[-1] if atr_series else None
    atr_mean_30d = (sum(atr_series[-720:]) / len(atr_series[-720:])) if atr_series else None

    ema20_1h = ema(c1, 20)
    rsi = rsi_wilder(c1)
    ema50_4h = ema(c4, 50)
    ema20_4h = ema(c4, 20)

    chg24 = (close1 / c1[-25] - 1.0) * 100.0 if len(c1) >= 25 else None
    notional24 = sum(b["vwap"] * b["vol"] for b in h1[-24:])

    return dict(
        pair=name,
        bars_1h=len(h1), bars_4h=len(h4),
        ts_1h_close=datetime.fromtimestamp(h1[-1]["t"] + 3600, tz=timezone.utc).isoformat(),
        ts_4h_close=datetime.fromtimestamp(h4[-1]["t"] + 14400, tz=timezone.utc).isoformat(),
        close_1h=close1, ema20_1h=ema20_1h, rsi14_1h=rsi,
        atr14_1h=atr, atr14_30d_mean=atr_mean_30d,
        close_4h=close4, ema50_4h=ema50_4h, ema20_4h=ema20_4h,
        chg24_pct=chg24, notional24=notional24,
        r1_margin=close1 - ema20_1h if ema20_1h else None,
        r2_margin=rsi - RSI_FLOOR if rsi is not None else None,
        r2a_ok=rsi is not None and rsi < RSI_CAP,
        r3_50_margin=close4 - ema50_4h if ema50_4h else None,
        r3_20_margin=close4 - ema20_4h if ema20_4h else None,
        r4a_ok=notional24 >= NOTIONAL_FLOOR,
        volcomp_05_open=(atr is not None and atr_mean_30d is not None
                         and atr < 0.5 * atr_mean_30d),
        volcomp_07_open=(atr is not None and atr_mean_30d is not None
                         and atr < 0.7 * atr_mean_30d),
        stop_dist_2atr=2 * atr if atr else None,
        low_confidence_4h=len(h4) < LOW_CONFIDENCE_4H_BARS,
    )


def fmt_pf(margin, low_conf=False):
    if margin is None:
        return "n/a"
    tag = "PASS" if margin > 0 else "FAIL"
    if low_conf:
        tag += "?"
    return f"{tag} {margin:+,.4g}"


def main():
    # Windows consoles default to cp1252; the table uses arrows/≥/×
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description="BULL wake-time indicator engine")
    ap.add_argument("--json", metavar="FILE", help="also write full results as JSON")
    ap.add_argument("--pair", metavar="PAIR", help="single pair only, e.g. BTC/USD")
    args = ap.parse_args()

    pairs = [(n, a) for n, a in UNIVERSE if not args.pair or n == args.pair.upper()]
    if not pairs:
        sys.exit(f"unknown pair {args.pair!r}; expected one of {[n for n, _ in UNIVERSE]}")

    now_utc = datetime.now(timezone.utc)
    now_pt = now_utc.astimezone(ZoneInfo("America/Los_Angeles"))
    print(f"# BULL indicators — generated {now_utc.isoformat(timespec='seconds')} "
          f"(PT calendar date: {now_pt:%Y-%m-%d}, {now_pt:%H:%M} PT)")
    print(f"# closed bars only; EMAs SMA-seeded over full history; RSI/ATR Wilder; "
          f"4H 50-EMA converged at >={CONVERGED_4H_BARS} bars\n")

    results, failures = [], []
    for name, api in pairs:
        try:
            results.append(analyze_pair(name, api))
        except Exception as e:  # noqa: BLE001 - keep scanning remaining pairs
            failures.append((name, str(e)))

    if len(results) >= 2:
        chgs = [r["chg24_pct"] for r in results if r["chg24_pct"] is not None]
        positives = sum(1 for c in chgs if c > 0)
        med = statistics.median(chgs)
        gate5a = positives >= 4
        sbd = positives <= 1 and med <= -1.0
        print(f"## Regime: {positives}/{len(chgs)} positive 24h, median {med:+.2f}% "
              f"→ 5a {'PASS' if gate5a else 'FAIL'}; SBD {'ACTIVE' if sbd else 'CLEAR'}\n")

    print("| Pair | 1H close | R1 (>EMA20) | R2 (RSI≥55) | R2a (<80) | R3 (4H>EMA50) | "
          "R3-20 (v0.14) | 24h % | R4a notional | ATR14 | 2×ATR stop | vol-comp .5/.7 | 4H bars |")
    print("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for r in results:
        lc = r["low_confidence_4h"]
        print(f"| {r['pair']} | {r['close_1h']:,.6g} "
              f"| {fmt_pf(r['r1_margin'])} "
              f"| {fmt_pf(r['r2_margin'])} (RSI {r['rsi14_1h']:.1f}) "
              f"| {'OK' if r['r2a_ok'] else 'FAIL'} "
              f"| {fmt_pf(r['r3_50_margin'], lc)} (EMA {r['ema50_4h']:,.6g}) "
              f"| {fmt_pf(r['r3_20_margin'], lc)} "
              f"| {r['chg24_pct']:+.2f} "
              f"| {'OK' if r['r4a_ok'] else 'FAIL'} ${r['notional24']/1e6:,.2f}M "
              f"| {r['atr14_1h']:,.5g} "
              f"| {r['stop_dist_2atr']:,.5g} "
              f"| {'OPEN' if r['volcomp_05_open'] else 'shut'}/{'OPEN' if r['volcomp_07_open'] else 'shut'} "
              f"| {r['bars_4h']}{' LOW-CONF' if lc else ''} |")

    if failures:
        print("\n## FETCH FAILURES (routine must treat these pairs as UNKNOWN, not FAIL):")
        for name, err in failures:
            print(f"- {name}: {err}")

    if args.json:
        with open(args.json, "w", encoding="utf-8") as f:
            json.dump(dict(generated_utc=now_utc.isoformat(),
                           pt_date=f"{now_pt:%Y-%m-%d}",
                           results=results,
                           failures=dict(failures)), f, indent=1)
        print(f"\n(JSON written to {args.json})")

    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
