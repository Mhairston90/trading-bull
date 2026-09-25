# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md`; the log remains the source of truth.
> **Last rebuild:** 2026-09-24T04:12:21Z routine-03-eod — book still flat (no positions since 09-23T14Z NEAR CLOSE, no exits this wake); EOD entry scan produced 1 rule-8-winner (SOL) but was **DEFERRED as Ring-1 judgment** on live-ticker-vs-bar-close divergence matching the 2026-07-07 HYPE archetype + fresh 2026-09-23 same-session-stop lesson escalation. Strategy v0.4 unchanged.

## Account

- Starting equity: **$10,000.00**
- Cash: **$10,309.52** (flat book)
- Realized PnL: **+$309.52**
- Unrealized PnL: **$0.00** (no open positions)
- Current equity: **$10,309.52**
- Equity peak: **$11,068.89**
- Drawdown from peak: **6.86%**
- Since-inception return: **+3.10%**

## Open positions

None. Book flat.

Portfolio risk-at-moment: **0.000%**
Open positions: **0 / 8** (strategy cap 0/4; BTC cluster 0/2).

## Day summary — PT 2026-09-24

- **Day PnL**: **$0.00 / 0.00%** (flat book, no trades this day).
- **Trades opened**: **0** (SOL rule-8-winner DEFERRED — see EOD scan section below).
- **Trades closed**: **0**.
- **Win rate today**: **N/A** (no trades).
- **Time-in-trade**: N/A.

## Rolling benchmark (07-10 last live equity → 09-24 EOD)

- **BULL 30d** (08-25 → 09-24): **−1.64%** (essentially flat except 09-23 NEAR round-trip).
- **BULL 7d** (09-17 → 09-24): **−1.64%** (same window).
- **BTC-hold 30d** (approx 08-25 close ~$79.0k → 09-24 EOD ~$84.05k live): **+6.39%**.
- **BTC-hold 7d** (09-17 close ~$76.4k → 09-24 EOD ~$84.05k live): **+10.02%**.
- **BULL vs BTC-hold 30d**: **−8.03pp behind** BTC.
- **BULL vs BTC-hold 7d**: **−11.66pp behind** BTC.
- **90d benchmark**: not-yet-computable (post-outage cross-window with 74d gap; will resume at next EOD after 10-15).

## EOD entry scan — 0 executions (rule-8 winner SOL DEFERRED)

**Regime (indicators.py 03Z bar-close authoritative): 11/15 positive, median +2.20% → 5a PASS, SBD CLEAR** (leg-1: 11 > 1-ceiling; leg-2: +2.20% > −1.0% floor). Regime PASSes by margin +7 above 4-floor.

**Eligible (R1..R8 PASS deterministically): 4 pairs.**
- SOL/USD (RSI 55.6, R4a $52.03M) — rank 3 → **rule-8 winner**
- ADA/USD (RSI 55.4, R4a $6.83M) — rank 6
- LTC/USD (RSI 57.0, R4a $41.37M) — rank 11
- LINK/USD (RSI 65.8, R4a $13.52M) — rank 13

**SOL sizing preview (not executed):** equity $10,309.52 × 0.015 = $154.6428 risk; 2×ATR $2.1739; size = 71.1370 SOL; entry (bar close $116.85 × 1.0005 slip) = $116.9084; stop = $114.7345; target = $125.6040 (+4R). Notional $8,314.51 fits cash.

**DEFER decision — Ring-1 judgment, strategy v0.4 unchanged.** Rationale:
- **Live-ticker vs bar-close divergence flag matches 2026-07-07 HYPE archetype** (bar-close 11/15 +2.20% vs live 2/15 ~−0.48%; ~−2.7pp median divergence + pair-count polarity mismatch 11→2). 07-07 HYPE stopped out 6h post-entry under structurally identical pre-flagged divergence.
- **Fresh 09-23 same-session-stop pattern-of-3 escalation** (lesson score 8) — NEAR 09-23 stopped 60min post-entry; routine-04 W25-restart memo (Sat 09-26, 2 days away) will evaluate P-W25R-SAMESESSION-STOP-GATE.
- **Under both proposed backlog gate rules, SOL would be blocked** (P-W25R-b two-wake regime-confirmation; P-W28-d live-ticker divergence gate).
- **SOL R2 borderline** at RSI 55.6 = +0.63 above 55-floor (smallest margin of 4 eligible pairs).
- **Preservation-of-capital dominates** given the pre-flagged leading signal — 2-day wait for routine-04-harness memo carries asymmetric downside protection vs upside opportunity cost.

**No same-pair 5b cooldowns active** (NEAR expired 14:00Z earlier today; no other stop-outs in 24h window).

## Active kill-switch state (EOD 04:12Z)

- Daily loss cap (PT 2026-09-24 fresh session): **0.00%** (flat book, no trades today). CLEAR.
- Consecutive-loss cap: **1 loss** (NEAR 09-23). Streak = 1 of 7. CLEAR.
- Max drawdown: **6.86%** from peak $11,068.89. CLEAR (25% cap, 12.5% warn, 5.64pp headroom).
- Equity floor: **$10,309.52 > $7,500** (+$2,809.52 above). CLEAR.
- Exposure: 0.000% / 4% used. CLEAR.
- Cluster cap: 0/2. CLEAR.
- Universe/liquidity: N/A (flat). CLEAR.
- 5b cooldown: **no active cooldowns** (NEAR/USD expired 2026-09-24T14:00Z).
- **Regime 5a: PASS 11/15 positive median +2.20%** (softer than midday's 14/15 but comfortably above 4-floor by 7).
- **5a-SBD: CLEAR** both legs.
- MCP availability: Kraken multi-ticker + OHLCV both fetched successfully. CLEAR.
- **All Ring 3 kill switches CLEAR.** (5a/SBD are entry-scan gates, not Ring-3 kills.)

## Ops notes (from watchdog EOD 04:12Z --telegram)

- 2× A heartbeat: routine-06 (>12d), routine-07 (>12d) still overdue. Routine-03 heartbeat broken by this wake's commit.
- 1× C dirty-tree: same 4 uncommitted 06-29 carry-over files (`docs/sentinel_10k_reset_spec_20260704.md`, `scripts/replay_cache_20260629/`, `scripts/replay_result_20260629.json`, `scripts/routine07_replay_20260629.py`). Not touched this wake.
- 5× D stale-MTM: variants v0.3/v0.5/v0.7/v0.13/v0.14 rebuild >30h ago. Variant rack effectively frozen since 07-10 scheduler outage; awaits routine-04-harness resume Sat 2026-09-26.
- Watchdog Telegram sent per --telegram flag (separate ops channel).
