# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md`; the log remains the source of truth.
> **Last rebuild:** 2026-09-24T04:15:00Z routine-03-eod (PT date 2026-09-23) — book still flat (no new entries this wake — full 5a FAIL + SBD ACTIVE); EOD MTM formality-only since flat.

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

## Day summary — PT 2026-09-23

- **Day PnL**: **−$172.30 / −1.64%** (start-of-day equity $10,481.82).
- **Trades opened**: **1** (NEAR/USD 13:00Z, rule-8 winner @ $4.72836).
- **Trades closed**: **1** (NEAR/USD 14:00Z, stop-hit-intrabar @ $4.45393, −1.01R, −$172.30 net).
- **Win rate today**: **0/1** (0%).
- **Time-in-trade**: 1H (single-bar stop-out).

## Rolling benchmark (07-10 last live equity → 09-23 EOD)

- **BULL 30d** (08-24 → 09-23): **−1.64%** (book flat 08-24 → 09-23T13Z; today's NEAR round-trip is the only P&L).
- **BULL 7d** (09-16 → 09-23): **−1.64%** (same — flat until today).
- **BTC-hold 30d** (08-24 close $78,966.10 → 09-24 close $83,819.30): **+6.15%**.
- **BTC-hold 7d** (09-17 close $76,354.80 → 09-24 close $83,819.30): **+9.78%**.
- **BULL vs BTC-hold 30d**: **−7.79pp behind** BTC.
- **BULL vs BTC-hold 7d**: **−11.42pp behind** BTC.
- **90d benchmark**: not-yet-computable (post-outage cross-window with 74d gap; will resume at next EOD after 10-15).

## EOD entry scan — 0 executions (regime FAIL + SBD ACTIVE)

- Regime (indicators.py 03Z bar-close authoritative): **1/15 positive, median −6.18% → 5a FAIL AND SBD ACTIVE** (both legs tripped; positive-count 1 ≤ 1-ceiling; median −6.18% ≤ −1.0% floor by 5.18pp).
- Only 2 pairs pass R1+R2 filters: **LTC/USD** (RSI 73.8, R3 PASS, R4a OK $19.43M) and **TRX/USD** (RSI 60.6, R3 PASS, R4a FAIL $1.39M).
- Both **BLOCKED by rule 5a** (mandatory reject-all-new-entries under regime FAIL). TRX additionally blocked by R4a liquidity floor.
- **NEAR/USD 5b cooldown ACTIVE** until 2026-09-24T14:00:00Z (24h from 14:00Z stop-out).
- **Reversal from 09-23T13Z overnight-wake regime read**: 4/15 median −0.86% → 1/15 median −6.18% (−5.32pp median deterioration + 3-pair drop-out in 15h). SBD leg-1 tripped (4 → 1 positive-count crossed the ≤1 ceiling); SBD leg-2 tripped (median −0.86% crossed the −1.0% floor and continued to −6.18%).

## Active kill-switch state (EOD 04:15Z)

- Daily loss cap (PT 2026-09-23): **−1.64%** ($−172.30 / $10,481.82 start-of-day). CLEAR (5% cap, 3.36pp headroom).
- Consecutive-loss cap: **1 loss** (NEAR today). Streak = 1 of 7. CLEAR.
- Max drawdown: **6.86%** from peak $11,068.89. CLEAR (25% cap, 12.5% warn, 5.64pp headroom).
- Equity floor: **$10,309.52 > $7,500** (+$2,809.52 above). CLEAR.
- Exposure: 0.000% / 4% used. CLEAR.
- Cluster cap: 0/2. CLEAR.
- Universe/liquidity: N/A (flat). CLEAR.
- 5b cooldown: **NEAR/USD active until 2026-09-24T14:00Z**.
- **Regime 5a**: **FAIL** 1/15 positive median −6.18% (entry-scan reject-all).
- **5a-SBD**: **ACTIVE** (both legs tripped by wide margins; Exit rule 1 tightens to 9-EMA 2-bar for any hypothetical future open position — n/a right now, book flat).
- MCP availability: Kraken REST + MCP + indicators.py + watchdog + Telegram OK. CLEAR.
- **All Ring 3 kill switches CLEAR.** (5a/SBD are entry-scan gates, not Ring-3 kills.)

## Ops notes (from watchdog)

- 3× A heartbeat: routine-03/06/07 last commit >12d (routine-03 pre-outage — this wake breaks the 03 heartbeat if commit lands).
- 1× C dirty-tree: 4 uncommitted files carry-over from 06-29 (`docs/sentinel_10k_reset_spec_20260704.md`, `scripts/replay_cache_20260629/`, `scripts/replay_result_20260629.json`, `scripts/routine07_replay_20260629.py`). Not touched this wake.
- 5× D stale-MTM: variants v0.3/v0.5/v0.7/v0.13/v0.14 rebuild >30h ago (1354–2123h). Variant rack effectively frozen since 07-10 scheduler outage; awaits routine-04-harness resume.
