# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md`; the log remains the source of truth.
> **Last rebuild:** 2026-07-29T17:52:00Z manual scheduler-outage recovery. The BTC position opened
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
- Current regime: **3/15 positive, median -1.56%** →
  5a FAIL, SBD CLEAR.

## Active kill-switch state

- Daily loss cap: CLEAR (flat today)
- Consecutive-loss cap: CLEAR
- Max drawdown: **5.30%**, below 12.5% warning and 25% halt thresholds
- Equity floor: **$10,481.82 > $7,500**
- Exposure and cluster caps: CLEAR (flat)
- **All Ring 3 kill switches CLEAR.**
