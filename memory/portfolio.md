# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md`; the log remains the source of truth.
> **Last rebuild:** 2026-09-26T20:00Z routine-02-midday (PT 2026-09-26 13:00) — SOL/USD open position marked to live Kraken ticker $121.03; no exits triggered (19:00Z close 121.11 > EMA20 120.94 → rule 1 not armed); static stop 119.0198 not pierced intrabar (24h low 119.84).

## Account

- Starting equity: **$10,000.00**
- Cash: **$1,173.45** ($10,264.60 − $9,091.15 SOL position cost)
- Realized PnL: **+$264.60** ($309.52 + (-$44.92 ADA))
- Unrealized PnL: **-$3.01** (SOL: 75.09 × ($121.03 − $121.07) = -$3.00; small rounding)
- Current equity: **$10,261.59**
- Equity peak: **$11,068.89**
- Drawdown from peak: **7.29%**
- Since-inception return: **+2.62%**

## Open positions

| Pair | Side | Size | Entry | Stop | Target | Cost | Unrealized R | Notes |
|------|------|-----:|------:|-----:|-------:|-----:|-------------:|-------|
| SOL/USD | long | 75.09 | 121.07 | 119.0198 | 129.2708 | $9,091.15 | -0.02R | Age 8h; 2×ATR stop 2.0502; risk $153.95 = 1.500% equity; live $121.03; BTC-cluster 1/2 |

Portfolio risk-at-moment: **1.500%** (SOL $153.95 / $10,261.59).
Open positions: **1 / 8** (strategy cap 1/4; BTC cluster 1/2 — SOL in cluster).

## Day summary — PT 2026-09-26

- **Day PnL**: **-$47.93 / -0.46%** (ADA -$44.92 realized + SOL -$3.01 unrealized MTM at 20:00Z).
- **Trades opened**: **1** (SOL/USD long at 12:00Z, entry-rule-v0.4-momentum-rule8-winner).
- **Trades closed**: **1** (ADA/USD long at 06:00Z, exit-ema20-2bar-recovery-missed-scheduler-replay).
- **Win rate today**: **0/1 (0.00%)** on closed trades.
- **Time-in-trade (SOL, ongoing)**: **8h** (12:00Z → 20:00Z snapshot).

## Rolling benchmark (07-10 last live equity → 09-26 midday latest)

- **BULL 30d** (08-27 → 09-26T20Z): **-2.11%** (SOL MTM add -0.03pp to prior -2.08%).
- **BULL 7d** (09-19 → 09-26T20Z): **-2.11%** (same window).
- **BTC-hold 30d** (approx 08-27 close ~$79.5k → 09-26T20Z live ~$84.03k): **+5.70%**.
- **BTC-hold 7d** (09-19 close ~$76.4k → 09-26T20Z live ~$84.03k): **+9.99%**.
- **BULL vs BTC-hold 30d**: **-7.81pp behind** BTC.
- **BULL vs BTC-hold 7d**: **-12.10pp behind** BTC.
- **90d benchmark**: not-yet-computable (post-outage cross-window with 74d gap; will resume at next EOD after 10-15).

## Midday exit-rule evaluation — SOL/USD

**Rule 1 (W22-G, two-bar 20-EMA break)**: NOT ARMED.
- EMA20 series (SMA-seeded 09-22T17Z over first 20 bars = 118.1605, iteratively rolled α=2/21):
  - 18:00Z: close 121.03, EMA20 120.9245 → ABOVE (+$0.1055)
  - 19:00Z: close 121.11, EMA20 120.9422 → ABOVE (+$0.1678)
- Neither of the last two closed bars is below EMA20 → cannot form a 2-bar break.

**Rule 1-SBD (9-EMA)**: NOT APPLICABLE. Regime not SBD (3/15 positive, median -0.89% — SBD requires ≤1 positive AND median ≤ -1.0%).

**Rule 2 (static 2×ATR stop 119.0198)**: NOT HIT.
- 20:00Z live low so far $120.99; 24h low $119.84 (both since entry, 12:00Z onwards); gap $0.822 above stop.

**Rule 3 (4R target 129.2708)**: NOT HIT.
- Current $121.03; 8.24 below target.

**Verdict**: hold SOL. No trade_log write.

## Active kill-switch state (routine-02-midday 2026-09-26T20:00Z / PT 2026-09-26 13:00)

- Daily loss cap (PT 2026-09-26): **-0.46%** (ADA -$44.92 realized + SOL -$3.01 MTM). CLEAR (5% cap, 4.54pp headroom).
- Consecutive-loss cap: **2 losses** (NEAR 09-23, ADA 09-26). Streak = 2 of 7. CLEAR.
- Max drawdown: **7.29%** from peak $11,068.89. CLEAR (25% cap, 12.5% warn, 5.21pp headroom — no threshold crossed this wake).
- Equity floor: **$10,261.59 > $7,500** (+$2,761.59 above). CLEAR.
- Exposure: **1.500% / 4% used** (SOL position). CLEAR.
- Cluster cap: **1/2 BTC-cluster** (SOL). CLEAR.
- Universe/liquidity: SOL notional ~$38.3M > $2M floor. CLEAR.
- 5b cooldown: no active cooldowns.
- **Regime 5a: FAIL 3/15 positive, median -0.89%** — informational only (routine 02 bars entries by spec). Reversal from overnight 6/15 PASS.
- **5a-SBD: CLEAR** (both legs: 3/15 > 1 AND median -0.89% > -1.0%; leg-2 headroom only $0.11 to floor).
- MCP availability: Kraken ticker + OHLCV both healthy. CLEAR.
- **All Ring 3 kill switches CLEAR.**

## Ops notes

- **On-schedule Monday-Fri fire:** routine-02-midday cron `0 13 * * 1-5` fired 2026-09-26T20:00Z. Wait — 2026-09-26 is Saturday (per overnight wake note this morning). Second consecutive off-schedule Saturday fire. Slot `bull-02-midday` confirmed. Routed to routine-04-harness per overnight note.
- **Regime deterioration overnight → midday:** 5a positive count 6→3 in ~7h (BTC -0.07, SUI -2.80, XRP -2.93, ADA -1.73 all rolled negative). Median -0.15% → -0.89%. Still SBD-CLEAR but leg-2 has narrowed to $0.11 headroom above -1.0% floor. Regime is deteriorating but not yet defensive.
- **SOL trade is near-flat (-0.02R at 20:00Z live).** Well inside noise; no action.
- **Cash buffer:** $1,173.45 preserved.
- Watchdog: not run this wake (routine 02 spec doesn't invoke). Prior 8-finding alert stands from overnight.
- Not last trading day of month → no monthly archive this wake.
