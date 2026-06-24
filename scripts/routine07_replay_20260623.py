#!/usr/bin/env python3
"""
Routine-07 replay — 2026-06-23 22:00 PT wake (UTC 2026-06-24T05:00Z).

Last rebuild: 2026-06-14T05:00Z. Gap = ~10 days (>7-day cap).
Per 2026-06-09 precedent, Kraken REST reaches 30 days → full 10-day gap recoverable.
Replay window: 2026-06-14T05:00Z → 2026-06-24T01:00Z (~9.83 days, ~236 1H bars).
Unrecoverable gap: none (Kraken REST 720-bar history covers ~30 days).

Note: routine fires at 22:00 PT but current UTC is ~00:28Z June 24 (pre-EOD-wake at 04:00Z).
Last eligible entry wake evaluated: OVERNIGHT 2026-06-23T13:00Z.
EOD 2026-06-24T04:00Z is still ~3.5h in the future — not evaluated this run.
Indicators.py authoritative output for current-bar state provided separately.

Date label: 2026-06-23 PT (per date-labeling guard — use PT calendar date, not UTC).

Variant open positions at replay start (2026-06-14T05:00Z):
  v0.3-vol-compression:  SOL/USD LONG 155 @ 68.49, stop 67.560, target 72.210, 1-bar EMA20 exit
  v0.5-cluster-cap-tight: BTC/USD LONG 0.1655 @ 64320.2, stop 63897.22, target 66012.12, 1-bar EMA20 exit; cluster 1/1
  v0.7-vol-comp-defensive: TAO/USD LONG 9 @ 274.733, stop 259.015, target 337.606, 1-bar EMA20 exit
  v0.12-sbd-exit: BTC/USD LONG 0.1631 @ 64320.2, stop 63897.22, target 66012.12, W22-G 2-bar exit; SBD CLEARED
  v0.13-trend-confirm: SOL/USD LONG 155 @ 68.49, stop 67.560, target 72.210, W22-G 2-bar exit
  v0.14-recovery-trend: BTC/USD LONG 0.1651 @ 64320.2, stop 63897.22, target 66012.12, W22-G 2-bar exit

Flat variants (no open positions): v0.4-mr, v0.8, v0.9, v0.15.

Exit rules:
  Standard (v0.3, v0.5, v0.7): 1-bar — exit at next close if 1H close < 1H EMA20
  W22-G (v0.12, v0.13, v0.14): 2-bar — exit when 2nd consecutive 1H close < 1H EMA20
  Stop: exit at stop price if 1H LOW <= stop (intra-bar stop check)
  4R target: exit at target if 1H HIGH >= target
  Priority: stop > 4R target > EMA exit (stop and target checked intra-bar)
"""

import json, math, time, urllib.request, os
from datetime import datetime, timezone, timedelta

CACHE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "replay_cache_20260623")
os.makedirs(CACHE_DIR, exist_ok=True)

UNIVERSE = [
    ("BTC/USD", "XXBTZUSD"), ("ETH/USD", "XETHZUSD"), ("SOL/USD", "SOLUSD"),
    ("HYPE/USD", "HYPEUSD"), ("XRP/USD", "XXRPZUSD"), ("SUI/USD", "SUIUSD"),
    ("TAO/USD", "TAOUSD"), ("XDG/USD", "XDGUSD"), ("NEAR/USD", "NEARUSD"),
    ("ADA/USD", "ADAUSD"), ("LINK/USD", "LINKUSD"), ("LTC/USD", "XLTCZUSD"),
    ("FARTCOIN/USD", "FARTCOINUSD"), ("TRX/USD", "TRXUSD"), ("AVAX/USD", "AVAXUSD"),
]
CLUSTER = {"BTC/USD","ETH/USD","SOL/USD","TAO/USD","AVAX/USD","SUI/USD","LINK/USD"}
VOL_FLOOR = 2_000_000

REPLAY_START = datetime(2026, 6, 14, 5, 0, tzinfo=timezone.utc)
# Current UTC ~00:30Z June 24; last closed OVERNIGHT wake 13:00Z June 23
REPLAY_END   = datetime(2026, 6, 24, 1, 0, tzinfo=timezone.utc)

# Wake times (UTC hour): OVERNIGHT=13, MIDDAY=20 (skip by default), EOD=4 (next calendar day)
ENTRY_WAKE_HOURS = {13, 4}  # midday (20) skipped per variant rules

def fetch_ohlcv(api_sym, interval_min):
    fn = os.path.join(CACHE_DIR, f"{api_sym}_{interval_min}.json")
    if os.path.exists(fn):
        with open(fn) as f:
            return json.load(f)
    url = f"https://api.kraken.com/0/public/OHLC?pair={api_sym}&interval={interval_min}"
    for attempt in range(3):
        try:
            with urllib.request.urlopen(url, timeout=30) as r:
                data = json.loads(r.read())
            if data.get("error"):
                raise RuntimeError(f"{api_sym}: {data['error']}")
            with open(fn,"w") as f:
                json.dump(data, f)
            return data
        except Exception as e:
            if attempt == 2: raise
            time.sleep(2)

def parse_bars(raw, api_sym):
    result_key = [k for k in raw["result"] if k != "last"][0]
    bars = raw["result"][result_key]
    out = []
    for b in bars:
        ts = datetime.fromtimestamp(b[0], tz=timezone.utc)
        out.append({"ts": ts, "open": float(b[1]), "high": float(b[2]),
                    "low": float(b[3]), "close": float(b[4]), "volume": float(b[6]),
                    "vwap": float(b[5])})
    return out

def wilder_ema(bars, key, period):
    """Wilder-style EMA (RSI/ATR). SMA-seeded."""
    vals = [b[key] for b in bars]
    ema = sum(vals[:period]) / period
    result = [None] * period
    for v in vals[period:]:
        ema = (ema * (period - 1) + v) / period
        result.append(ema)
    return result

def compute_ema(vals, period):
    """SMA-seeded EMA."""
    result = [None] * (period - 1)
    ema = sum(vals[:period]) / period
    result.append(ema)
    for v in vals[period:]:
        ema = ema + (v - ema) * (2 / (period + 1))
        result.append(ema)
    return result

def compute_indicators_1h(bars_1h):
    """Add ema20, atr14, rsi14 to each bar (None for warm-up bars)."""
    closes = [b["close"] for b in bars_1h]
    highs  = [b["high"]  for b in bars_1h]
    lows   = [b["low"]   for b in bars_1h]

    # EMA20 of close
    ema20 = compute_ema(closes, 20)

    # ATR14 (Wilder): TR = max(H-L, |H-Cp|, |L-Cp|)
    trs = [highs[0] - lows[0]]
    for i in range(1, len(bars_1h)):
        tr = max(highs[i]-lows[i], abs(highs[i]-closes[i-1]), abs(lows[i]-closes[i-1]))
        trs.append(tr)
    atr14_vals = [None]*14
    atr = sum(trs[:14])/14
    atr14_vals.append(atr)
    for tr in trs[14:]:
        atr = (atr*13 + tr)/14
        atr14_vals.append(atr)

    # RSI14 (Wilder)
    gains = [0.0]
    losses = [0.0]
    for i in range(1, len(closes)):
        d = closes[i]-closes[i-1]
        gains.append(max(d, 0))
        losses.append(max(-d, 0))
    rsi14 = [None]*14
    avg_g = sum(gains[1:15])/14
    avg_l = sum(losses[1:15])/14
    if avg_l == 0:
        rsi14.append(100.0)
    else:
        rs = avg_g/avg_l
        rsi14.append(100 - 100/(1+rs))
    for i in range(15, len(closes)):
        avg_g = (avg_g*13 + gains[i])/14
        avg_l = (avg_l*13 + losses[i])/14
        if avg_l == 0:
            rsi14.append(100.0)
        else:
            rs = avg_g/avg_l
            rsi14.append(100 - 100/(1+rs))

    for i, b in enumerate(bars_1h):
        b["ema20"] = ema20[i]
        b["atr14"] = atr14_vals[i]
        b["rsi14"] = rsi14[i]
    return bars_1h

def compute_indicators_4h(bars_4h):
    """Add ema50, ema20_4h to each bar."""
    closes = [b["close"] for b in bars_4h]
    # EMA50 (>=200 bars for convergence)
    ema50 = compute_ema(closes, 50)
    ema20_4h = compute_ema(closes, 20)
    for i, b in enumerate(bars_4h):
        b["ema50"] = ema50[i]
        b["ema20_4h"] = ema20_4h[i]
    return bars_4h

def compute_regime(bars_by_pair, ts_utc):
    """Count pairs with positive 24h change at ts_utc. Returns (positives, median_pct)."""
    changes = []
    for pair_name, _ in UNIVERSE:
        bars = bars_by_pair.get(pair_name, {}).get("1h", [])
        ref = [b for b in bars if b["ts"] <= ts_utc]
        if len(ref) < 25:
            continue
        close_now  = ref[-1]["close"]
        close_24h  = ref[-25]["close"]
        if close_24h > 0:
            pct = (close_now - close_24h) / close_24h * 100
            changes.append(pct)
    if not changes:
        return 0, 0.0
    positive = sum(1 for c in changes if c > 0)
    changes_sorted = sorted(changes)
    n = len(changes_sorted)
    median = (changes_sorted[n//2] + changes_sorted[(n-1)//2]) / 2
    return positive, median

def get_4h_bar_at(bars_4h, ts_utc):
    """Return the last 4H bar whose open time <= ts_utc."""
    candidates = [b for b in bars_4h if b["ts"] <= ts_utc]
    return candidates[-1] if candidates else None

def vol_24h(bars_1h, ts_utc):
    """Sum of vwap*volume for 24 bars ending at ts_utc."""
    recent = [b for b in bars_1h if b["ts"] <= ts_utc][-24:]
    return sum(b["vwap"]*b["volume"] for b in recent)

def main():
    print(f"\n=== BULL routine-07 replay — 2026-06-23 22:00 PT ===")
    print(f"Replay: {REPLAY_START.isoformat()} to {REPLAY_END.isoformat()}")
    print(f"Gap: ~10 days (>7-day cap; fully recoverable via Kraken REST 720-bar/30-day history)\n")

    # === FETCH ALL DATA ===
    print("Fetching OHLCV for all 15 pairs (1H + 4H) — fresh cache...")
    bars_by_pair = {}
    for pair_name, api_sym in UNIVERSE:
        raw1h = fetch_ohlcv(api_sym, 60)
        raw4h = fetch_ohlcv(api_sym, 240)
        bars_1h = compute_indicators_1h(parse_bars(raw1h, api_sym))
        bars_4h = compute_indicators_4h(parse_bars(raw4h, api_sym))
        bars_by_pair[pair_name] = {"1h": bars_1h, "4h": bars_4h}
        print(f"  {pair_name}: {len(bars_1h)} 1H bars, {len(bars_4h)} 4H bars")
        time.sleep(0.3)

    print()

    # === VARIANT STATE at replay start (2026-06-14T05:00Z) ===
    variants = {
        "v0.3": {
            "equity": 10625.39, "cash": 9.44, "realized": 625.39, "peak": 10643.90,
            "exit_rule": "1bar",
            "position": {"pair": "SOL/USD", "side": "long", "size": 155, "entry": 68.49,
                         "stop": 67.560, "target": 72.210, "risk_usd": 144.15,
                         "open_ts": datetime(2026,6,14,4,0,tzinfo=timezone.utc),
                         "below_ema_streak": 0},
            "trades": [],
            "kill_daily_loss": False, "kill_consec_loss_days": 0,
            "kill_dd_pct": 0.17, "cluster_used": {"SOL/USD"},
            "rule": "momentum", "vol_comp_threshold": 0.5,
        },
        "v0.5": {
            "equity": 10644.07, "cash": 0.0, "realized": 644.07, "peak": 10662.61,
            "exit_rule": "1bar",
            "position": {"pair": "BTC/USD", "side": "long", "size": 0.1655, "entry": 64320.2,
                         "stop": 63897.22, "target": 66012.12, "risk_usd": 69.99,
                         "open_ts": datetime(2026,6,14,4,0,tzinfo=timezone.utc),
                         "below_ema_streak": 0},
            "trades": [],
            "kill_daily_loss": False, "kill_consec_loss_days": 0,
            "kill_dd_pct": 0.17, "cluster_used": {"BTC/USD"},
            "cluster_cap": 1,
            "rule": "momentum",
        },
        "v0.7": {
            "equity": 10000.00, "cash": 7527.40, "realized": 0.0, "peak": 10000.00,
            "exit_rule": "1bar",
            "position": {"pair": "TAO/USD", "side": "long", "size": 9, "entry": 274.733,
                         "stop": 259.015, "target": 337.606, "risk_usd": 141.46,
                         "open_ts": datetime(2026,6,14,4,0,tzinfo=timezone.utc),
                         "below_ema_streak": 0},
            "trades": [],
            "kill_daily_loss": False, "kill_consec_loss_days": 0,
            "kill_dd_pct": 0.0, "cluster_used": {"TAO/USD"},
            "rule": "momentum", "vol_comp_threshold": 0.7,
        },
        "v0.12": {
            "equity": 10491.28, "cash": 0.62, "realized": 491.28, "peak": 10606.00,
            "exit_rule": "2bar",
            "position": {"pair": "BTC/USD", "side": "long", "size": 0.1631, "entry": 64320.2,
                         "stop": 63897.22, "target": 66012.12, "risk_usd": 68.98,
                         "open_ts": datetime(2026,6,14,4,0,tzinfo=timezone.utc),
                         "below_ema_streak": 0},
            "trades": [],
            "kill_daily_loss": False, "kill_consec_loss_days": 0,
            "kill_dd_pct": 1.08, "cluster_used": {"BTC/USD"},
            "rule": "momentum",
        },
        "v0.13": {
            "equity": 10618.05, "cash": 2.10, "realized": 618.05, "peak": 10643.90,
            "exit_rule": "2bar",
            "position": {"pair": "SOL/USD", "side": "long", "size": 155, "entry": 68.49,
                         "stop": 67.560, "target": 72.210, "risk_usd": 144.15,
                         "open_ts": datetime(2026,6,14,4,0,tzinfo=timezone.utc),
                         "below_ema_streak": 0},
            "trades": [],
            "kill_daily_loss": False, "kill_consec_loss_days": 0,
            "kill_dd_pct": 0.24, "cluster_used": {"SOL/USD"},
            "rule": "momentum",
        },
        "v0.14": {
            "equity": 10619.30, "cash": 2.04, "realized": 619.30, "peak": 10645.15,
            "exit_rule": "2bar",
            "position": {"pair": "BTC/USD", "side": "long", "size": 0.1651, "entry": 64320.2,
                         "stop": 63897.22, "target": 66012.12, "risk_usd": 69.77,
                         "open_ts": datetime(2026,6,14,4,0,tzinfo=timezone.utc),
                         "below_ema_streak": 0},
            "trades": [],
            "kill_daily_loss": False, "kill_consec_loss_days": 0,
            "kill_dd_pct": 0.24, "cluster_used": {"BTC/USD"},
            "rule": "momentum",
        },
        "v0.4-mr": {
            "equity": 10000.00, "cash": 10000.00, "realized": 0.0, "peak": 10000.00,
            "position": None, "trades": [],
            "kill_daily_loss": False, "kill_consec_loss_days": 0,
            "kill_dd_pct": 0.0, "cluster_used": set(),
            "rule": "mean-rev", "rsi_threshold": 25,
        },
        "v0.8": {
            "equity": 9850.00, "cash": 9850.00, "realized": -150.00, "peak": 10000.00,
            "position": None, "trades": [],
            "kill_daily_loss": False, "kill_consec_loss_days": 0,
            "kill_dd_pct": 1.50, "cluster_used": set(),
            "rule": "mean-rev", "rsi_threshold": 30,
        },
        "v0.9": {
            "equity": 10000.00, "cash": 10000.00, "realized": 0.0, "peak": 10000.00,
            "position": None, "trades": [],
            "kill_daily_loss": False, "kill_consec_loss_days": 0,
            "kill_dd_pct": 0.0, "cluster_used": set(),
            "rule": "mean-rev", "rsi_threshold": 20,
        },
        "v0.15": {
            "equity": 10000.00, "cash": 10000.00, "realized": 0.0, "peak": 10000.00,
            "position": None, "trades": [],
            "kill_daily_loss": False, "kill_consec_loss_days": 0,
            "kill_dd_pct": 0.0, "cluster_used": set(),
            "rule": "mean-rev", "rsi_threshold": 30, "sbd_guard": True,
        },
    }

    # === REPLAY LOOP ===
    btc_bars = bars_by_pair["BTC/USD"]["1h"]
    replay_bars_ts = [b["ts"] for b in btc_bars if REPLAY_START <= b["ts"] <= REPLAY_END]
    print(f"Replay bars in window: {len(replay_bars_ts)} 1H closes\n")

    all_events = []  # (ts, variant, event_type, pair, price, pnl_r, pnl_usd, note)

    def close_position(vname, v, ts, price, reason):
        pos = v["position"]
        risk = pos["risk_usd"]
        pnl_usd = (price - pos["entry"]) * pos["size"]
        pnl_r = pnl_usd / risk if risk > 0 else 0
        v["realized"] += pnl_usd
        v["cash"] = v["cash"] + pos["entry"] * pos["size"] + pnl_usd
        v["equity"] = v["cash"]
        if v["equity"] > v["peak"]:
            v["peak"] = v["equity"]
        v["kill_dd_pct"] = max(0, (v["peak"] - v["equity"]) / v["peak"] * 100)
        v["cluster_used"].discard(pos["pair"])
        v["trades"].append(("CLOSE", ts, pos["pair"], pos["size"], pos["entry"], price, pnl_r, pnl_usd, reason))
        all_events.append((ts, vname, "CLOSE", pos["pair"], price, pnl_r, pnl_usd, reason))
        print(f"  [{vname}] CLOSE {pos['pair']} {pos['size']} @ {price:.4f} {reason} => {pnl_r:+.2f}R / ${pnl_usd:+.2f}")
        v["position"] = None

    prev_sbd_state = False
    wake_count = 0
    entry_events = 0

    for ts in replay_bars_ts:
        pair_bars_at_ts = {}
        for pair_name, _ in UNIVERSE:
            b1h = bars_by_pair[pair_name]["1h"]
            cur = next((b for b in b1h if b["ts"] == ts), None)
            pair_bars_at_ts[pair_name] = cur

        btc_bar = pair_bars_at_ts.get("BTC/USD")
        if not btc_bar:
            continue

        # --- EXIT CHECKS (every 1H close) ---
        for vname, v in list(variants.items()):
            pos = v.get("position")
            if not pos:
                continue
            pair = pos["pair"]
            bar = pair_bars_at_ts.get(pair)
            if not bar:
                continue

            # Intra-bar stop check
            if bar["low"] <= pos["stop"]:
                close_position(vname, v, ts, pos["stop"], "exit-stop-hit")
                continue

            # 4R target check
            if bar["high"] >= pos["target"]:
                close_position(vname, v, ts, pos["target"], "exit-4R-target")
                continue

            # EMA exit
            ema20 = bar.get("ema20")
            if ema20 is None:
                continue
            if bar["close"] < ema20:
                pos["below_ema_streak"] = pos.get("below_ema_streak", 0) + 1
                exit_rule = v.get("exit_rule", "1bar")
                if exit_rule == "1bar" and pos["below_ema_streak"] >= 1:
                    close_position(vname, v, ts, bar["close"], "exit-ema20-1bar")
                elif exit_rule == "2bar" and pos["below_ema_streak"] >= 2:
                    close_position(vname, v, ts, bar["close"], "exit-ema20-2bar")
            else:
                pos["below_ema_streak"] = 0

        # --- ENTRY SCAN (only at wake-equivalent bars) ---
        if ts.hour not in ENTRY_WAKE_HOURS:
            continue

        wake_count += 1
        positives, median_pct = compute_regime(bars_by_pair, ts)
        sbd_active = (positives <= 1 and median_pct <= -1.0)

        regime_5a = positives >= 4

        print(f"\n--- Wake {ts.isoformat()} | Regime: {positives}/15 pos, median {median_pct:+.2f}% | 5a={'PASS' if regime_5a else 'FAIL'} | SBD={'ACTIVE' if sbd_active else 'CLEAR'}")

        if not regime_5a:
            print(f"    => 5a FAIL: no momentum entries")
            # Mean-rev still scans independently of 5a
        else:
            # Entry scan for momentum variants
            momentum_variants_needing_entry = [
                vn for vn in ["v0.3","v0.5","v0.7","v0.12","v0.13","v0.14"]
                if variants[vn].get("position") is None and not variants[vn].get("kill_daily_loss")
            ]

            if momentum_variants_needing_entry:
                eligible_pairs = []
                for rank, (pair_name, _) in enumerate(UNIVERSE):
                    bar = pair_bars_at_ts.get(pair_name)
                    if not bar or bar.get("ema20") is None or bar.get("rsi14") is None or bar.get("atr14") is None:
                        continue

                    if bar["close"] <= bar["ema20"]:
                        continue
                    if bar["rsi14"] < 55 or bar["rsi14"] > 80:
                        continue
                    b4h = get_4h_bar_at(bars_by_pair[pair_name]["4h"], ts)
                    if not b4h or b4h.get("ema50") is None:
                        continue
                    r3_50 = bar["close"] > b4h["ema50"]
                    r3_20 = (bar["close"] > b4h.get("ema20_4h", 0)) if b4h.get("ema20_4h") else False

                    v24 = vol_24h(bars_by_pair[pair_name]["1h"], ts)
                    if v24 < VOL_FLOOR:
                        continue

                    atr = bar["atr14"]
                    stop = bar["close"] - 2 * atr
                    target = bar["close"] + 4 * 2 * atr
                    all_1h = bars_by_pair[pair_name]["1h"]
                    atrs_before = [b["atr14"] for b in all_1h if b["ts"] <= ts and b["atr14"] is not None][-720:]
                    mean_atr_30d = sum(atrs_before) / len(atrs_before) if atrs_before else None
                    vol_comp_05 = (atr < 0.5 * mean_atr_30d) if mean_atr_30d else False
                    vol_comp_07 = (atr < 0.7 * mean_atr_30d) if mean_atr_30d else False

                    eligible_pairs.append({
                        "pair": pair_name, "rank": rank, "close": bar["close"],
                        "ema20": bar["ema20"], "rsi14": bar["rsi14"], "atr": atr,
                        "r3_50": r3_50, "r3_20": r3_20, "stop": stop, "target": target,
                        "vol_comp_05": vol_comp_05, "vol_comp_07": vol_comp_07, "v24h": v24,
                    })

                eligible_pairs.sort(key=lambda x: x["rank"])

                for vname in momentum_variants_needing_entry:
                    v = variants[vname]
                    cluster_cap = v.get("cluster_cap", 2)

                    for ep in eligible_pairs:
                        pair_name = ep["pair"]
                        in_cluster = pair_name in CLUSTER
                        cluster_slots_used = sum(1 for p in v.get("cluster_used", set()) if p in CLUSTER)
                        if in_cluster and cluster_slots_used >= cluster_cap:
                            continue

                        if vname == "v0.14":
                            if not ep["r3_20"]:
                                continue
                        else:
                            if not ep["r3_50"]:
                                continue

                        if vname in ("v0.3", "v0.13"):
                            if not ep["vol_comp_05"]:
                                continue
                        elif vname == "v0.7":
                            if not ep["vol_comp_07"]:
                                continue

                        if vname == "v0.13":
                            b1h_list = bars_by_pair[pair_name]["1h"]
                            prior = [b for b in b1h_list if b["ts"] < ts and b["ema20"] is not None]
                            if not prior or prior[-1]["close"] <= prior[-1]["ema20"]:
                                continue

                        price = ep["close"]
                        stop = ep["stop"]
                        target = ep["target"]
                        risk_pct = 0.015
                        risk_usd = v["equity"] * risk_pct
                        stop_dist = price - stop
                        if stop_dist <= 0:
                            continue
                        size = risk_usd / stop_dist

                        print(f"  [{vname}] OPEN {pair_name} {size:.4f} @ {price:.4f}, stop {stop:.4f}, target {target:.4f} | RSI{ep['rsi14']:.1f} R3_50={'Y' if ep['r3_50'] else 'N'} R3_20={'Y' if ep['r3_20'] else 'N'} vc5/{ep['vol_comp_05']} vc7/{ep['vol_comp_07']}")

                        v["position"] = {
                            "pair": pair_name, "side": "long", "size": size,
                            "entry": price, "stop": stop, "target": target,
                            "risk_usd": risk_usd, "open_ts": ts, "below_ema_streak": 0,
                        }
                        v["cash"] -= price * size
                        v["cluster_used"].add(pair_name)
                        v["trades"].append(("OPEN", ts, pair_name, size, price, stop, target, risk_usd))
                        all_events.append((ts, vname, "OPEN", pair_name, price, None, None, f"RSI{ep['rsi14']:.1f}"))
                        entry_events += 1
                        break

        # Mean-rev entry scan (independent of 5a)
        for vname in ["v0.4-mr","v0.8","v0.9","v0.15"]:
            v = variants[vname]
            if v.get("position"):
                continue

            if vname == "v0.15" and sbd_active:
                continue

            rsi_thresh = v.get("rsi_threshold", 25)
            for pair_name, _ in UNIVERSE:
                bar = pair_bars_at_ts.get(pair_name)
                if not bar or bar.get("rsi14") is None:
                    continue
                if bar["close"] <= bar["open"]:
                    continue
                if bar["rsi14"] >= rsi_thresh:
                    continue
                b4h = get_4h_bar_at(bars_by_pair[pair_name]["4h"], ts)
                if not b4h or b4h.get("ema50") is None:
                    continue
                if bar["close"] <= b4h["ema50"]:
                    continue
                if vol_24h(bars_by_pair[pair_name]["1h"], ts) < VOL_FLOOR:
                    continue

                atr = bar.get("atr14", 0)
                stop = bar["close"] - 1.5 * atr
                target = bar["close"] + 3 * 1.5 * atr
                risk_usd = v["equity"] * 0.015
                stop_dist = bar["close"] - stop
                if stop_dist <= 0:
                    continue
                size = risk_usd / stop_dist
                print(f"  [{vname}] OPEN {pair_name} {size:.4f} @ {bar['close']:.4f} MR RSI{bar['rsi14']:.1f}<{rsi_thresh}")
                v["position"] = {"pair": pair_name, "side": "long", "size": size,
                                 "entry": bar["close"], "stop": stop, "target": target,
                                 "risk_usd": risk_usd, "open_ts": ts, "below_ema_streak": 0}
                v["cash"] -= bar["close"] * size
                v["cluster_used"].add(pair_name)
                v["trades"].append(("OPEN", ts, pair_name, size, bar["close"], stop, target, risk_usd))
                all_events.append((ts, vname, "OPEN", pair_name, bar["close"], None, None, f"MR RSI{bar['rsi14']:.1f}<{rsi_thresh}"))
                entry_events += 1
                break

        prev_sbd_state = sbd_active

    # === SUMMARY ===
    print("\n\n=== REPLAY SUMMARY ===")
    print(f"Total wakes evaluated: {wake_count}")
    print(f"Total entry events: {entry_events}")
    print()

    final_btc_bars = bars_by_pair["BTC/USD"]["1h"]
    final_bar = max((b for b in final_btc_bars if b["ts"] <= REPLAY_END), key=lambda b: b["ts"], default=None)
    btc_current = final_bar["close"] if final_bar else None

    # Regime at last EOD wake (2026-06-23T04:00Z)
    eod_ts = datetime(2026, 6, 23, 4, 0, tzinfo=timezone.utc)
    positives_eod, median_eod = compute_regime(bars_by_pair, eod_ts)
    sbd_eod = (positives_eod <= 1 and median_eod <= -1.0)

    # Regime at current OVERNIGHT (2026-06-23T13:00Z)
    overnight_ts = datetime(2026, 6, 23, 13, 0, tzinfo=timezone.utc)
    positives_overnight, median_overnight = compute_regime(bars_by_pair, overnight_ts)
    sbd_overnight = (positives_overnight <= 1 and median_overnight <= -1.0)

    # Current regime (latest bar)
    positives_now, median_now = compute_regime(bars_by_pair, REPLAY_END)
    sbd_now = (positives_now <= 1 and median_now <= -1.0)

    print(f"Regime at EOD 2026-06-23T04:00Z: {positives_eod}/15 pos, median {median_eod:+.2f}% | 5a={'PASS' if positives_eod>=4 else 'FAIL'} SBD={'ACTIVE' if sbd_eod else 'CLEAR'}")
    print(f"Regime at OVERNIGHT 2026-06-23T13:00Z: {positives_overnight}/15 pos, median {median_overnight:+.2f}% | 5a={'PASS' if positives_overnight>=4 else 'FAIL'} SBD={'ACTIVE' if sbd_overnight else 'CLEAR'}")
    print(f"Current regime (latest bar): {positives_now}/15 pos, median {median_now:+.2f}% | 5a={'PASS' if positives_now>=4 else 'FAIL'} SBD={'ACTIVE' if sbd_now else 'CLEAR'}")
    print(f"BTC current close: ${btc_current:,.1f}" if btc_current else "BTC: N/A")
    print()

    for vname, v in variants.items():
        pos = v.get("position")
        if pos:
            pair_bars = bars_by_pair[pos["pair"]]["1h"]
            cur = max((b for b in pair_bars if b["ts"] <= REPLAY_END), key=lambda b: b["ts"], default=None)
            mtm = cur["close"] if cur else pos["entry"]
            unreal = (mtm - pos["entry"]) * pos["size"]
            total_equity = v["cash"] + mtm * pos["size"]
            dd = max(0, (v["peak"] - total_equity) / v["peak"] * 100) if v["peak"] > 0 else 0
            print(f"{vname}: equity ${total_equity:,.2f} ({'+' if total_equity>=10000 else ''}{(total_equity-10000)/10000*100:.2f}%) | open {pos['pair']} {pos['size']:.4f} @ {pos['entry']:.3f} MTM {mtm:.3f} ({'+' if unreal>=0 else ''}{unreal:.2f} unreal) | DD {dd:.2f}% | new_trades: {len(v['trades'])}")
        else:
            dd = max(0, (v["peak"] - v["equity"]) / v["peak"] * 100) if v["peak"] > 0 else 0
            print(f"{vname}: equity ${v['equity']:,.2f} ({'+' if v['equity']>=10000 else ''}{(v['equity']-10000)/10000*100:.2f}%) | flat | DD {dd:.2f}% | new_trades: {len(v['trades'])}")

    print()
    print("=== TRADE LOG (new events this replay) ===")
    for ev in all_events:
        ts_str = ev[0].strftime("%Y-%m-%dT%H:%MZ")
        if ev[2] == "CLOSE":
            print(f"{ts_str} {ev[1]} CLOSE {ev[3]} @ {ev[4]:.4f} {ev[7]} => {ev[5]:+.2f}R / ${ev[6]:+.2f}")
        else:
            print(f"{ts_str} {ev[1]} OPEN  {ev[3]} @ {ev[4]:.4f} {ev[7]}")

    out = {
        "wake_label": "2026-06-23 22:00 PT",
        "replay_start": REPLAY_START.isoformat(),
        "replay_end": REPLAY_END.isoformat(),
        "regime_eod_0623": {"positives": positives_eod, "median": round(median_eod,2), "sbd": sbd_eod},
        "regime_overnight_0623": {"positives": positives_overnight, "median": round(median_overnight,2), "sbd": sbd_overnight},
        "regime_current": {"positives": positives_now, "median": round(median_now,2), "sbd": sbd_now},
        "btc_current_close": btc_current,
        "total_wakes": wake_count, "total_entries": entry_events,
        "variants": {}, "events": []
    }

    for vname, v in variants.items():
        pos = v.get("position")
        state = {"cash": v["cash"], "realized": v["realized"], "peak": v["peak"],
                 "position": None, "equity": None, "dd_pct": None, "new_trades": len(v["trades"]),
                 "trades_detail": []}
        if pos:
            pair_bars = bars_by_pair[pos["pair"]]["1h"]
            cur = max((b for b in pair_bars if b["ts"] <= REPLAY_END), key=lambda b: b["ts"], default=None)
            mtm = cur["close"] if cur else pos["entry"]
            total_equity = v["cash"] + mtm * pos["size"]
            state["equity"] = total_equity
            state["dd_pct"] = max(0, (v["peak"] - total_equity) / v["peak"] * 100) if v["peak"] > 0 else 0
            state["position"] = {
                "pair": pos["pair"], "size": pos["size"], "entry": pos["entry"],
                "stop": pos["stop"], "target": pos["target"], "risk_usd": pos["risk_usd"],
                "open_ts": pos["open_ts"].isoformat(), "mtm": mtm,
                "unreal_usd": (mtm - pos["entry"]) * pos["size"],
                "unreal_r": (mtm - pos["entry"]) * pos["size"] / pos["risk_usd"] if pos["risk_usd"] else 0,
            }
        else:
            state["equity"] = v["equity"]
            state["dd_pct"] = max(0, (v["peak"] - v["equity"]) / v["peak"] * 100) if v["peak"] > 0 else 0
        # Trades
        for t in v["trades"]:
            if t[0] == "CLOSE":
                state["trades_detail"].append({"type":"CLOSE","ts":t[1].isoformat(),"pair":t[2],"size":t[3],"entry":t[4],"exit":t[5],"pnl_r":t[6],"pnl_usd":t[7],"reason":t[8]})
            else:
                state["trades_detail"].append({"type":"OPEN","ts":t[1].isoformat(),"pair":t[2],"size":t[3],"price":t[4],"stop":t[5],"target":t[6],"risk_usd":t[7]})
        out["variants"][vname] = state

    for ev in all_events:
        entry = {"ts": ev[0].isoformat(), "variant": ev[1], "type": ev[2], "pair": ev[3],
                 "price": ev[4], "pnl_r": ev[5], "pnl_usd": ev[6], "note": ev[7]}
        out["events"].append(entry)

    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "replay_result_20260623.json")
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nResults written to {out_path}")
    return out

if __name__ == "__main__":
    main()
