# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md`; the log remains the source of truth.
> **Last rebuild:** 2026-09-26T04:15Z routine-03-eod (PT 2026-09-25 21:15) — new ADA/USD long opened this wake on 04:00Z 1H bar close; regime 5a PASS 13/15, SBD CLEAR; rule 8 selected ADA as highest 30d notional rank among full-pass candidates (SUI 8, TAO 9, ADA 6, LINK 13, AVAX 12).

## Account

- Starting equity: **$10,000.00**
- Cash: **$5,371.06** ($10,309.52 − $4,938.46 ADA position cost)
- Realized PnL: **+$309.52**
- Unrealized PnL: **$0.00** (fresh entry at bar-close 0.256346, MTM equal to entry)
- Current equity: **$10,309.52**
- Equity peak: **$11,068.89**
- Drawdown from peak: **6.86%**
- Since-inception return: **+3.10%**

## Open positions

| Pair | Side | Size | Entry | Stop | Target | Cost | Unrealized R | Notes |
|------|------|-----:|------:|-----:|-------:|-----:|-------------:|-------|
| ADA/USD | long | 19263 | 0.256346 | 0.248318 | 0.288458 | $4,938.46 | +0.00R | 2×ATR stop = 0.008028; risk $154.63 = 1.500% equity; rule-8 winner rank 6 |

Portfolio risk-at-moment: **1.500%** (ADA $154.63 / $10,309.52).
Open positions: **1 / 8** (strategy cap 1/4; BTC cluster 0/2 — ADA not in cluster).

## Day summary — PT 2026-09-25

- **Day PnL**: **$0.00 / 0.00%** (fresh entry at end-of-day, no realized moves yet).
- **Trades opened**: **1** (ADA/USD long, entry-rule-v0.4-momentum-rule8-winner).
- **Trades closed**: **0**.
- **Win rate today**: **N/A** (no closed trades).
- **Time-in-trade**: N/A.

## Rolling benchmark (07-10 last live equity → 09-25 EOD)

- **BULL 30d** (08-26 → 09-25): **−1.64%** (unchanged; ADA opened at bar close so no MTM impact yet).
- **BULL 7d** (09-18 → 09-25): **−1.64%** (same window).
- **BTC-hold 30d** (approx 08-26 close ~$79.0k → 09-26T04Z live ~$83.94k): **+6.26%**.
- **BTC-hold 7d** (09-18 close ~$76.4k → 09-26T04Z live ~$83.94k): **+9.87%**.
- **BULL vs BTC-hold 30d**: **−7.90pp behind** BTC.
- **BULL vs BTC-hold 7d**: **−11.51pp behind** BTC.
- **90d benchmark**: not-yet-computable (post-outage cross-window with 74d gap; will resume at next EOD after 10-15).

## EOD entry scan — 5 full-pass candidates, ADA won rule-8 tiebreak

**Regime (indicators.py 04:12Z snapshot):** 13/15 positive 24h, median +3.23% → **5a PASS** (margin +9 vs 4-floor), **5a-SBD CLEAR** both legs.

**Full-pass rule set (R1+R2+R2a+R3):**
| Pair | Rank | 1H close | R1 (EMA20) | R2 (RSI) | R3 (4H EMA50) | 2×ATR | 24h% |
|---|---:|---:|---|---|---|---:|---:|
| ADA/USD | **6** | 0.256346 | +0.001191 | 55.2 (+0.17) | +0.01794 | 0.008028 | +3.53 |
| SUI/USD | 8 | 1.169 | +0.03462 | 65.1 (+10.09) | +0.2046 | 0.06089 | +15.51 |
| TAO/USD | 9 | 311.76 | +3.24 | 59.0 (+4.03) | +27.28 | 11.279 | +5.90 |
| AVAX/USD | 12 | 10.626 | +0.1009 | 56.6 (+1.56) | +0.6158 | 0.35077 | +4.43 |
| LINK/USD | 13 | 14.0333 | +0.2083 | 61.9 (+6.91) | +1.269 | 0.41489 | +4.62 |

**Rule 8 winner: ADA/USD** (rank 6, ties broken by 30d notional rank per strategy.md; ADA lowest rank number = highest volume among passers). Remaining 4 pairs are re-evaluated at next wake per rule 8; if any fall out of eligibility (RSI drop below 55, EMA cross, etc.), they are skipped by design.

**FARTCOIN/USD passed technical (R1+R2+R2a+R3) but is not in the universe** (dropped 07-01 refresh; ONDO replaced it at rank 14). Correctly skipped.

## Active kill-switch state (EOD 2026-09-26T04:15Z / PT 2026-09-25 21:15)

- Daily loss cap (PT 2026-09-25): **0.00%** (no realized moves; ADA fresh entry MTM 0). CLEAR (5% cap).
- Consecutive-loss cap: **1 loss** (NEAR 09-23). Streak = 1 of 7. CLEAR.
- Max drawdown: **6.86%** from peak $11,068.89. CLEAR (25% cap, 12.5% warn, 5.64pp headroom).
- Equity floor: **$10,309.52 > $7,500** (+$2,809.52 above). CLEAR.
- Exposure: **1.500% / 4% used** (ADA position). CLEAR.
- Cluster cap: 0/2 (ADA not in BTC-cluster). CLEAR.
- Universe/liquidity: ADA notional $10.35M > $2M floor. CLEAR.
- 5b cooldown: **no active cooldowns** (NEAR/USD expired 2026-09-24T14:00Z).
- **Regime 5a: PASS 13/15 positive, median +3.23%**.
- **5a-SBD: CLEAR** (both legs).
- MCP availability: Kraken ticker + indicators.py both healthy. CLEAR.
- **All Ring 3 kill switches CLEAR.**

## Ops notes

- Watchdog fired 8 findings — 2 heartbeat (routine-06/07 overdue >12d), 1 dirty-tree (4 carry-over 06-29 files), 5 stale-MTM (variants rack — expected, rack frozen since 07-10 scheduler outage).
- Same 4 uncommitted 06-29 carry-over files still in working tree (`docs/sentinel_10k_reset_spec_20260704.md`, `scripts/replay_cache_20260629/`, `scripts/replay_result_20260629.json`, `scripts/routine07_replay_20260629.py`) — not touched this wake.
- News scan skipped for ADA (informational-only per v0.2 strategy; does not veto). Sentiment: 5.7 bps Kraken spread — good depth.
- Routine-06 / routine-07 heartbeats still overdue (>12d) — deferred to Sat 2026-09-26 routine-04-harness resume.
- ONDO/USD (+23.95% 09-24 breakout, rank 14 addition) still not in indicators.py config — routed to routine-04-harness (Sat 2026-09-26) for reconciliation.
- Not last trading day of month (2026-09-25 vs 09-30) → no monthly archive this wake.
