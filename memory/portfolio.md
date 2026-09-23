# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md`; the log remains the source of truth.
> **Last rebuild:** 2026-09-23T13:15:00Z routine-01-overnight — first main-routine wake since 2026-07-10 (~74d scheduler outage).
> Book was flat pre-wake (last position BTC 2026-07-10 closed at scheduler-outage-recovery rebuild 2026-07-29).
> One NEW OPEN this wake: NEAR/USD rule-8 winner.

## Account

- Starting equity: **$10,000.00**
- Cash: **$7,750.72**
- Realized PnL (effective account result): **+$481.82**
- Unrealized PnL: **-$4.85** (NEAR MTM 4.72836 → 4.6409 live, 577.6 × -$0.08746)
- Current equity: **$10,476.97**
- Equity peak: **$11,068.89**
- Drawdown from peak: **5.34%**
- Since-inception return: **+4.77%**

## Open positions

| Pair | Side | Size | Entry | Stop | Target | Unrealized R | Notional | Entered |
|------|------|-----:|------:|-----:|-------:|-------------:|---------:|---------|
| NEAR/USD | long | 577.6 | 4.72836 | 4.45616 | 5.81716 | -0.32R (live 4.6409) | $2,731.10 entry / $2,680.79 MTM | 2026-09-23T13:00Z |

Portfolio risk-at-moment: **1.500%** (NEAR full stop-distance × size / equity, breakeven ratchet unarmed).
Open positions: **1 / 8** (strategy cap 1/4; BTC cluster 0/2).

## Post-outage entry rationale

- First routine-01-overnight wake since 2026-07-10 (~74-day scheduler gap).
- Wake fired 06:13 PT (+13min vs 06:00 PT cron target) — treated as ON-SCHEDULE for entry-discipline purposes.
- `indicators.py` 720-bar convergence at 13:13:42Z: regime **4/15 positive, median -0.86% → 5a PASS (exactly at 4-floor), SBD CLEAR**.
- Rule-8 winner: **NEAR/USD (rank 7)** — only full tech-PASS candidate.
  - R1 PASS: 1H close 4.726 > EMA20 (+$0.2405)
  - R2 PASS: RSI14 69.1 > 55 (+14.09)
  - R2a PASS: 69.1 <= 80 (no climactic cap breach)
  - R3 PASS: 4H close > 4H EMA50 (+$1.008); R3-20 confirm +$0.4774
  - R4a PASS: 24h notional $30.67M >> $2.0M floor
  - R5/R5b PASS: no existing position, no cooldown active (74d since any NEAR touch)
  - R5a PASS: 4/15 positive (at threshold)
  - R6/R6a/R7: 0/4 cap, 0/2 cluster (NEAR non-cluster), risk 1.5% ≤ 4%
  - R8: sole tech-PASS → default winner
- Sentiment PASS: live NEAR spread 2-5bps (4.6388/4.6408 top-of-book), $30.8M 24h notional matches bar-close basis. Live-ticker 24h +4.86% vs bar-close +2.98% — DIVERGENCE POSITIVE (live LEADING bar-close higher, opposite direction from the 07-07 lesson's bearish-divergence concern; not a veto).
- Intra-bar drift: 4.6409 live vs 4.726 bar-close = -1.79% pullback in first 14min of new bar. Logged as informational; entry price convention remains bar-close × 1.0005 slippage per prior wakes.

## Active kill-switch state

- Daily loss cap: **-0.05%** (MTM only, no realized today). CLEAR (5% cap, 4.95pp headroom).
- Consecutive-loss cap: N/A across 74-day gap; last trading days on record all flat/no-trade after 07-10 CLOSE. Reset to 0-streak per open book.
- Max drawdown: **5.34%** from peak $11,068.89. CLEAR (25% cap, 12.5% warn, 7.16pp headroom).
- Equity floor: **$10,476.97 > $7,500** (+$2,976.97 above). CLEAR.
- Exposure: 1.500% / 4% used. CLEAR.
- Cluster cap: 0/2 (NEAR outside BTC-cluster set). CLEAR.
- Universe/liquidity: NEAR is universe rank 7. CLEAR.
- MCP availability: Kraken REST + MCP OK. Telegram OK. CLEAR.
- **All Ring 3 kill switches CLEAR.**
