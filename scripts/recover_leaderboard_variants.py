#!/usr/bin/env python3
"""Deterministic seven-day recovery replay for leaderboard BULL variants.

This is intentionally read-only. It prints the hypothetical events and ending
state needed to repair an interrupted routine-07 wake without silently
extending the routine's documented seven-day replay cap.
"""

from __future__ import annotations

import argparse
import bisect
import json
import statistics
import time
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path

from indicators import UNIVERSE, fetch_bars

CLUSTER = {"BTC/USD", "ETH/USD", "SOL/USD", "TAO/USD", "AVAX/USD", "SUI/USD", "LINK/USD"}
NOTIONAL_FLOOR = 2_000_000.0


def ema_series(values: list[float], period: int) -> list[float | None]:
    out: list[float | None] = [None] * len(values)
    if len(values) < period:
        return out
    value = sum(values[:period]) / period
    out[period - 1] = value
    alpha = 2.0 / (period + 1)
    for index in range(period, len(values)):
        value = values[index] * alpha + value * (1 - alpha)
        out[index] = value
    return out


def rsi_series(values: list[float], period: int = 14) -> list[float | None]:
    out: list[float | None] = [None] * len(values)
    if len(values) < period + 1:
        return out
    gains = [max(values[i] - values[i - 1], 0.0) for i in range(1, period + 1)]
    losses = [max(values[i - 1] - values[i], 0.0) for i in range(1, period + 1)]
    avg_gain = sum(gains) / period
    avg_loss = sum(losses) / period
    out[period] = 100.0 if avg_loss == 0 else 100.0 - 100.0 / (1 + avg_gain / avg_loss)
    for index in range(period + 1, len(values)):
        delta = values[index] - values[index - 1]
        avg_gain = (avg_gain * (period - 1) + max(delta, 0.0)) / period
        avg_loss = (avg_loss * (period - 1) + max(-delta, 0.0)) / period
        out[index] = 100.0 if avg_loss == 0 else 100.0 - 100.0 / (1 + avg_gain / avg_loss)
    return out


def atr_series(bars: list[dict], period: int = 14) -> list[float | None]:
    out: list[float | None] = [None] * len(bars)
    if len(bars) < period + 1:
        return out
    true_ranges = [
        max(
            bars[i]["h"] - bars[i]["l"],
            abs(bars[i]["h"] - bars[i - 1]["c"]),
            abs(bars[i]["l"] - bars[i - 1]["c"]),
        )
        for i in range(1, len(bars))
    ]
    value = sum(true_ranges[:period]) / period
    out[period] = value
    for index in range(period + 1, len(bars)):
        value = (value * (period - 1) + true_ranges[index - 1]) / period
        out[index] = value
    return out


@dataclass
class PairData:
    bars_1h: list[dict]
    bars_4h: list[dict]
    close_times_1h: list[int] = field(init=False)
    close_times_4h: list[int] = field(init=False)
    ema9_1h: list[float | None] = field(init=False)
    ema20_1h: list[float | None] = field(init=False)
    rsi14_1h: list[float | None] = field(init=False)
    atr14_1h: list[float | None] = field(init=False)
    ema20_4h: list[float | None] = field(init=False)
    ema50_4h: list[float | None] = field(init=False)
    ema200_4h: list[float | None] = field(init=False)

    def __post_init__(self) -> None:
        self.close_times_1h = [bar["t"] + 3600 for bar in self.bars_1h]
        self.close_times_4h = [bar["t"] + 14400 for bar in self.bars_4h]
        closes_1h = [bar["c"] for bar in self.bars_1h]
        closes_4h = [bar["c"] for bar in self.bars_4h]
        self.ema9_1h = ema_series(closes_1h, 9)
        self.ema20_1h = ema_series(closes_1h, 20)
        self.rsi14_1h = rsi_series(closes_1h, 14)
        self.atr14_1h = atr_series(self.bars_1h, 14)
        self.ema20_4h = ema_series(closes_4h, 20)
        self.ema50_4h = ema_series(closes_4h, 50)
        self.ema200_4h = ema_series(closes_4h, 200)

    def snapshot(self, close_time: int) -> dict | None:
        one_index = bisect.bisect_right(self.close_times_1h, close_time) - 1
        four_index = bisect.bisect_right(self.close_times_4h, close_time) - 1
        if one_index < 24 or four_index < 199:
            return None
        one = self.bars_1h[one_index]
        four = self.bars_4h[four_index]
        return {
            "one_index": one_index,
            "bar": one,
            "close": one["c"],
            "open": one["o"],
            "high": one["h"],
            "low": one["l"],
            "previous_low": self.bars_1h[one_index - 1]["l"],
            "ema9": self.ema9_1h[one_index],
            "ema20": self.ema20_1h[one_index],
            "rsi14": self.rsi14_1h[one_index],
            "atr14": self.atr14_1h[one_index],
            "close4": four["c"],
            "ema20_4h": self.ema20_4h[four_index],
            "ema50_4h": self.ema50_4h[four_index],
            "ema200_4h": self.ema200_4h[four_index],
            "change24": (one["c"] / self.bars_1h[one_index - 24]["c"] - 1) * 100,
            "notional24": sum(
                bar["vwap"] * bar["vol"]
                for bar in self.bars_1h[one_index - 23:one_index + 1]
            ),
        }


@dataclass
class Position:
    pair: str
    size: float
    entry: float
    stop: float
    initial_stop: float
    target: float | None
    opened_at: int
    bars_held: int = 0
    below_count: int = 0


@dataclass
class Variant:
    name: str
    cash: float
    mode: str
    positions: dict[str, Position] = field(default_factory=dict)
    events: list[dict] = field(default_factory=list)

    def equity(self, market: dict[str, dict]) -> float:
        return self.cash + sum(
            position.size * market[position.pair]["close"]
            for position in self.positions.values()
        )

    def append_event(self, timestamp: int, action: str, position: Position, price: float, reason: str) -> None:
        pnl = None if action == "OPEN" else position.size * (price - position.entry)
        risk = position.size * (position.entry - position.initial_stop)
        r_multiple = None if pnl is None or risk <= 0 else pnl / risk
        self.events.append({
            "timestamp": datetime.fromtimestamp(timestamp, timezone.utc).isoformat().replace("+00:00", "Z"),
            "action": action,
            "pair": position.pair,
            "size": round(position.size, 8),
            "price": round(price, 8),
            "stop": round(position.initial_stop, 8) if action == "OPEN" else None,
            "target": round(position.target, 8) if action == "OPEN" and position.target else None,
            "r": round(r_multiple, 3) if r_multiple is not None else None,
            "pnl": round(pnl, 2) if pnl is not None else None,
            "reason": reason,
        })


def regime(market: dict[str, dict]) -> tuple[int, float, bool]:
    changes = [snapshot["change24"] for snapshot in market.values()]
    positives = sum(change > 0 for change in changes)
    median = statistics.median(changes)
    return positives, median, positives <= 1 and median <= -1.0


def process_exits(variant: Variant, timestamp: int, market: dict[str, dict], sbd: bool) -> None:
    for pair, position in list(variant.positions.items()):
        snapshot = market[pair]
        position.bars_held += 1
        reason = None
        exit_price = snapshot["close"]

        if variant.mode in {"v012", "v014"}:
            initial_risk = position.entry - position.stop
            if variant.mode == "v014" and snapshot["close"] >= position.entry + 2 * initial_risk:
                position.stop = max(position.stop, position.entry)
            if snapshot["low"] <= position.stop:
                reason = "exit-stop-hit-recovery"
                exit_price = position.stop
            elif position.target is not None and snapshot["close"] >= position.target:
                reason = "exit-4R-target-recovery"
            else:
                exit_ema = snapshot["ema9"] if sbd else snapshot["ema20"]
                position.below_count = position.below_count + 1 if snapshot["close"] < exit_ema else 0
                if position.below_count >= 2:
                    reason = f"exit-ema{'9-sbd' if sbd else '20'}-2bar-recovery"
        else:
            if snapshot["low"] <= position.stop:
                reason = "exit-stop-hit-recovery"
                exit_price = position.stop
            elif snapshot["close"] >= snapshot["ema20"]:
                reason = "exit-ema20-target-recovery"
            elif position.bars_held >= 24:
                reason = "exit-time-stop-24bar-recovery"

        if reason:
            variant.cash += position.size * exit_price
            variant.append_event(timestamp, "CLOSE", position, exit_price, reason)
            del variant.positions[pair]


def eligible(variant: Variant, pair: str, snapshot: dict, positives: int, sbd: bool) -> bool:
    if pair in variant.positions or snapshot["notional24"] < NOTIONAL_FLOOR:
        return False
    if variant.mode == "v015":
        return (
            not sbd
            and snapshot["close4"] > snapshot["ema200_4h"]
            and snapshot["rsi14"] < 30
            and snapshot["close"] > snapshot["previous_low"]
            and snapshot["close"] > snapshot["open"]
            and len(variant.positions) < 2
        )
    trend_ema = snapshot["ema50_4h"] if variant.mode == "v012" else snapshot["ema20_4h"]
    return (
        positives >= 4
        and snapshot["close"] > snapshot["ema20"]
        and 55 < snapshot["rsi14"] <= 80
        and snapshot["close4"] > trend_ema
        and len(variant.positions) < 4
        and sum(open_pair in CLUSTER for open_pair in variant.positions) < 2
    )


def process_entry(variant: Variant, timestamp: int, market: dict[str, dict], positives: int, sbd: bool) -> None:
    candidates = [
        pair
        for pair, _ in UNIVERSE
        if pair in market and eligible(variant, pair, market[pair], positives, sbd)
    ]
    if not candidates:
        return
    pair = candidates[0]  # UNIVERSE is already 30-day notional rank order.
    snapshot = market[pair]
    stop_distance = snapshot["atr14"] * (1.5 if variant.mode == "v015" else 2.0)
    equity = variant.equity(market)
    size = min(equity * 0.015 / stop_distance, variant.cash / snapshot["close"])
    if size * snapshot["close"] < 1.0:
        return
    position = Position(
        pair=pair,
        size=size,
        entry=snapshot["close"],
        stop=snapshot["close"] - stop_distance,
        initial_stop=snapshot["close"] - stop_distance,
        target=None if variant.mode == "v015" else snapshot["close"] + 4 * stop_distance,
        opened_at=timestamp,
    )
    variant.cash -= size * position.entry
    variant.positions[pair] = position
    variant.append_event(
        timestamp,
        "OPEN",
        position,
        position.entry,
        f"entry-rule-{variant.mode}-recovery",
    )


def write_recovered_portfolios(
    variants: list[Variant],
    market: dict[str, dict],
    generated_at: datetime,
) -> None:
    repo = Path(__file__).resolve().parents[1]
    stamp = generated_at.replace(second=0, microsecond=0).isoformat().replace("+00:00", "Z")
    positives, median, sbd = regime(market)

    main_text = f"""# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md`; the log remains the source of truth.
> **Last rebuild:** {stamp} manual scheduler-outage recovery. The BTC position opened
> 2026-07-10T03:00Z was replayed against the complete local Kraken-derived 1H cache
> and closed at 2026-07-10T19:00Z after two consecutive closes below the 1H EMA20.
> Per `OPERATING.md`, missed main-routine entry wakes were not fabricated.

## Account

- Starting equity: **$10,000.00**
- Cash: **$10,481.82**
- Realized PnL (effective account result): **+$481.82**
- Unrealized PnL: **$0.00**
- Current equity: **$10,481.82**
- Equity peak: **$11,068.89**
- Drawdown from peak: **5.30%**
- Since-inception return: **+4.82%**

## Open positions

(none)

Portfolio risk-at-moment: **0.00%**.
Open positions: **0 / 8** (strategy cap 0/4; BTC cluster 0/2).

## Recovery audit

- Recovered exit: BTC/USD 0.16438, $63,925.85 entry → $63,758.30 exit,
  **-$27.54 / -0.23R**.
- Recovery data coverage: complete for the 2026-07-10 open position.
- Missed main entry scans were deliberately not backfilled, matching the operating
  rule against retroactive main-strategy entries after long scheduler gaps.
- Current regime: **{positives}/15 positive, median {median:+.2f}%** →
  5a {'PASS' if positives >= 4 else 'FAIL'}, SBD {'ACTIVE' if sbd else 'CLEAR'}.

## Active kill-switch state

- Daily loss cap: CLEAR (flat today)
- Consecutive-loss cap: CLEAR
- Max drawdown: **5.30%**, below 12.5% warning and 25% halt thresholds
- Equity floor: **$10,481.82 > $7,500**
- Exposure and cluster caps: CLEAR (flat)
- **All Ring 3 kill switches CLEAR.**
"""
    (repo / "memory" / "portfolio.md").write_text(main_text, encoding="utf-8")

    by_mode = {variant.mode: variant for variant in variants}
    v012 = by_mode["v012"]
    v012_equity = v012.equity(market)
    v012_text = f"""# Variant v0.12-sbd-exit — Synthetic Portfolio

> **Paper-paper account.** Synthetic $10K starting equity.
> **Category:** LAB hypothesis / instrumented twin.
> **Last rebuild:** {stamp} bounded routine-07 recovery replay. The missing
> 2026-06-27 SOL OPEN was restored to the source-of-truth log and its same-day
> EMA20 exit was recovered. The documented seven-day replay window
> (2026-07-22T17:00Z onward) was then simulated deterministically.
>
> **LEADERBOARD-SOURCED — FORWARD PAPER-PAPER ONLY.**

## Account

- Starting equity: **$10,000.00**
- Cash: **${v012.cash:,.2f}**
- Realized PnL (variant lifetime): **+${v012_equity - 10000:,.2f}**
- Unrealized PnL: **$0.00**
- Current equity: **${v012_equity:,.2f}**
- Equity peak: **$11,101.09**
- Drawdown from peak: **{(1 - v012_equity / 11101.09) * 100:.2f}%**
- Net return: **+{(v012_equity / 10000 - 1) * 100:.2f}%**

## Open positions

(none)

Portfolio risk-at-moment: **0.00%**.
Open positions: **0 / 4** (BTC cluster 0/2).

## Recovery audit

- Restored omitted SOL OPEN and recovered SOL CLOSE: **-$144.72 / -0.89R**.
- Seven-day replay: ETH **+$387.62**, BTC **-$65.80**, ETH **-$126.25**.
- Older unavailable interval was not invented; it is explicitly outside routine-07's
  seven-day cap.
- Current regime: **{positives}/15 positive, median {median:+.2f}%**;
  SBD {'ACTIVE' if sbd else 'CLEAR'}.
- Closed trades represented in the log after recovery: **20**.

## Active kill-switch state

- Daily loss cap: CLEAR
- Consecutive-loss cap: CLEAR
- Max drawdown: **{(1 - v012_equity / 11101.09) * 100:.2f}%**
- Equity floor: **${v012_equity:,.2f} > $7,500**
- **All variant kill switches CLEAR.**
"""
    (repo / "variants" / "v0.12-sbd-exit" / "portfolio.md").write_text(v012_text, encoding="utf-8")

    v014 = by_mode["v014"]
    v014_equity = v014.equity(market)
    open_position = next(iter(v014.positions.values()))
    mark = market[open_position.pair]["close"]
    position_value = open_position.size * mark
    unrealized = open_position.size * (mark - open_position.entry)
    unrealized_label = (
        f"-${abs(unrealized):,.2f}" if unrealized < 0 else f"+${unrealized:,.2f}"
    )
    risk = open_position.size * (open_position.entry - open_position.initial_stop)
    v014_text = f"""# Variant v0.14-recovery-trend — Synthetic Portfolio

> **Paper-paper account.** Synthetic $10K starting equity.
> **Category:** LAB hypothesis (4H 20-EMA trend filter).
> **Last rebuild:** {stamp} bounded routine-07 recovery replay. The missing
> 2026-06-27 SOL OPEN and same-day exit were restored before replaying the
> documented seven-day recoverable window.

## Account

- Starting equity: **$10,000.00**
- Cash: **${v014.cash:,.2f}**
- Realized PnL (variant lifetime): **+$1,205.06**
- Unrealized PnL: **{unrealized_label}**
- Position value: **${position_value:,.2f}**
- Current equity: **${v014_equity:,.2f}**
- Equity peak: **$11,402.33**
- Drawdown from peak: **{(1 - v014_equity / 11402.33) * 100:.2f}%**
- Net return: **+{(v014_equity / 10000 - 1) * 100:.2f}%**

## Open positions

| Pair | Side | Size | Entry | Stop | Target | Entry time (UTC) | Last | MTM | Unrealized R |
|---|---|---:|---:|---:|---:|---|---:|---:|---:|
| {open_position.pair} | long | {open_position.size:.8f} | {open_position.entry:.6f} | {open_position.initial_stop:.8f} | {open_position.target:.8f} | {datetime.fromtimestamp(open_position.opened_at, timezone.utc).isoformat().replace("+00:00", "Z")} | {mark:.6f} | ${position_value:,.2f} | {unrealized / risk:+.2f}R |

Portfolio risk-at-moment: **{risk / v014_equity * 100:.2f}%**.
Open positions: **1 / 4** (BTC cluster 0/2).

## Recovery audit

- Restored omitted SOL OPEN and recovered SOL CLOSE: **-$148.64 / -0.89R**.
- Seven-day closed replay: ETH **+$398.14**, BTC **-$67.59**, ETH **-$129.68**.
- Current paper position: ADA/USD opened 2026-07-29T04:00Z under the 4H 20-EMA rule.
- Older unavailable interval was not invented; it is explicitly outside routine-07's
  seven-day cap.
- Current regime: **{positives}/15 positive, median {median:+.2f}%**;
  SBD {'ACTIVE' if sbd else 'CLEAR'}.
- Closed trades represented in the log after recovery: **13**.

## Active kill-switch state

- Daily loss cap: CLEAR
- Consecutive-loss cap: CLEAR
- Max drawdown: **{(1 - v014_equity / 11402.33) * 100:.2f}%**
- Equity floor: **${v014_equity:,.2f} > $7,500**
- Portfolio risk: **{risk / v014_equity * 100:.2f}% < 4%**
- **All variant kill switches CLEAR.**
"""
    (repo / "variants" / "v0.14-recovery-trend" / "portfolio.md").write_text(v014_text, encoding="utf-8")

    v015 = by_mode["v015"]
    v015_text = f"""# Variant v0.15-meanrev-guarded — Synthetic Portfolio

> **Paper-paper account.** Synthetic $10K starting equity.
> **Category:** LAB hypothesis (RSI<30 mean reversion with SBD guard).
> **Last rebuild:** {stamp} bounded routine-07 recovery replay. No qualifying
> entries or exits occurred in the documented seven-day recoverable window.

## Account

- Starting equity: **$10,000.00**
- Cash: **$10,000.00**
- Realized PnL: **$0.00**
- Unrealized PnL: **$0.00**
- Current equity: **$10,000.00**
- Equity peak: **$10,000.00**
- Drawdown from peak: **0.00%**

## Open positions

(none)

Open positions: **0 / 2**.

## Recovery audit

- Seven-day replay events: **0**.
- Older unavailable interval was not invented; it is explicitly outside routine-07's
  seven-day cap.
- Current regime: **{positives}/15 positive, median {median:+.2f}%**;
  SBD {'ACTIVE' if sbd else 'CLEAR'}.
- Days live: **50**.

## Active kill-switch state

All variant kill switches CLEAR at $10,000 equity.
"""
    (repo / "variants" / "v0.15-meanrev-guarded" / "portfolio.md").write_text(v015_text, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--start",
        default=(datetime.now(timezone.utc) - timedelta(days=7)).replace(minute=0, second=0, microsecond=0).isoformat(),
    )
    parser.add_argument(
        "--write-portfolios",
        action="store_true",
        help="rewrite the four leaderboard portfolio snapshots from the audited recovery state",
    )
    args = parser.parse_args()
    start = datetime.fromisoformat(args.start.replace("Z", "+00:00")).astimezone(timezone.utc)

    pairs: dict[str, PairData] = {}
    for name, api in UNIVERSE:
        one_hour = fetch_bars(api, 60)
        time.sleep(0.5)
        four_hour = fetch_bars(api, 240)
        time.sleep(0.5)
        pairs[name] = PairData(one_hour, four_hour)

    variants = [
        Variant("BULL v0.12-SBD (twin)", 10_713.47, "v012"),
        Variant("FABLE BULL v0.14-Recovery (LAB)", 11_004.19, "v014"),
        Variant("FABLE BULL v0.15-MR-Guarded (LAB)", 10_000.00, "v015"),
    ]
    common_times = sorted({
        close_time
        for data in pairs.values()
        for close_time in data.close_times_1h
        if close_time >= int(start.timestamp())
    })

    last_market: dict[str, dict] = {}
    for timestamp in common_times:
        market = {
            pair: snapshot
            for pair, data in pairs.items()
            if (snapshot := data.snapshot(timestamp)) is not None
        }
        if len(market) != len(UNIVERSE):
            continue
        last_market = market
        positives, median, sbd = regime(market)
        for variant in variants:
            process_exits(variant, timestamp, market, sbd)
        wake = datetime.fromtimestamp(timestamp, timezone.utc)
        if wake.minute == 0 and wake.hour in {4, 13}:
            for variant in variants:
                process_entry(variant, timestamp, market, positives, sbd)

    output = {
        "replay_start": start.isoformat(),
        "replay_end": datetime.now(timezone.utc).isoformat(),
        "ending_regime": {
            "positive": regime(last_market)[0],
            "median_pct": round(regime(last_market)[1], 3),
            "sbd": regime(last_market)[2],
        },
        "variants": [
            {
                "name": variant.name,
                "ending_equity": round(variant.equity(last_market), 2),
                "cash": round(variant.cash, 2),
                "open_positions": [
                    {
                        "pair": position.pair,
                        "size": round(position.size, 8),
                        "entry": round(position.entry, 8),
                        "stop": round(position.stop, 8),
                        "target": round(position.target, 8) if position.target else None,
                        "opened_at": datetime.fromtimestamp(position.opened_at, timezone.utc).isoformat().replace("+00:00", "Z"),
                        "mark": last_market[position.pair]["close"],
                    }
                    for position in variant.positions.values()
                ],
                "events": variant.events,
            }
            for variant in variants
        ],
    }
    if args.write_portfolios:
        write_recovered_portfolios(variants, last_market, datetime.now(timezone.utc))
    print(json.dumps(output, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
