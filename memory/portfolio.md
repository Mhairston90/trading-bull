# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md`; the log remains the source of truth.
> **Last rebuild:** 2026-09-25T20:00Z routine-02-midday — book still flat (no positions since 09-23T14Z NEAR CLOSE, no exits possible this wake); midday is position-management-only, no new entries evaluated. Live-ticker snapshot corroborates regime recovery persistence (13/15 positive, median +3.14%, SBD CLEAR).

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

## Day summary — PT 2026-09-25

- **Day PnL**: **$0.00 / 0.00%** (flat book, no trades this day).
- **Trades opened**: **0** (midday is position-management-only per routine spec — no entry scan).
- **Trades closed**: **0**.
- **Win rate today**: **N/A** (no trades).
- **Time-in-trade**: N/A.

## Rolling benchmark (07-10 last live equity → 09-25 midday)

- **BULL 30d** (08-26 → 09-25): **−1.64%** (essentially flat except 09-23 NEAR round-trip).
- **BULL 7d** (09-18 → 09-25): **−1.64%** (same window).
- **BTC-hold 30d** (approx 08-26 close ~$79.0k → 09-25 midday live ~$83.94k): **+6.26%**.
- **BTC-hold 7d** (09-18 close ~$76.4k → 09-25 midday live ~$83.94k): **+9.87%**.
- **BULL vs BTC-hold 30d**: **−7.90pp behind** BTC.
- **BULL vs BTC-hold 7d**: **−11.51pp behind** BTC.
- **90d benchmark**: not-yet-computable (post-outage cross-window with 74d gap; will resume at next EOD after 10-15).

## Midday scan — position management only (no entries evaluated)

**Regime read (live-ticker snapshot ~20:00Z, informational only — midday spec bars new entries regardless):**
- 13/15 positive 24h, median +3.14%. SBD CLEAR both legs.
- Recovery from EOD (11/15, +2.20%) has continued modestly higher (Δ +2 count, +0.94pp median in ~16h).
- Only LTC (−1.17%) and BTC (−0.52%) negative; ETH borderline +0.09%.
- Note: bar-close authoritative regime is not computed this wake (indicators.py not invoked in midday routine). Live-ticker regime is directional confirmation only.

**No exits to evaluate** (0 open positions). **No new entries** (midday routine forbids per spec).

## Active kill-switch state (midday 2026-09-25T20:00Z)

- Daily loss cap (PT 2026-09-25 fresh session): **0.00%** (flat book, no trades today). CLEAR.
- Consecutive-loss cap: **1 loss** (NEAR 09-23). Streak = 1 of 7. CLEAR.
- Max drawdown: **6.86%** from peak $11,068.89. CLEAR (25% cap, 12.5% warn, 5.64pp headroom).
- Equity floor: **$10,309.52 > $7,500** (+$2,809.52 above). CLEAR.
- Exposure: 0.000% / 4% used. CLEAR.
- Cluster cap: 0/2. CLEAR.
- Universe/liquidity: N/A (flat). CLEAR.
- 5b cooldown: **no active cooldowns** (NEAR/USD expired 2026-09-24T14:00Z; no other stop-outs in 24h window).
- **Regime 5a (live-ticker read):** PASS 13/15 positive, median +3.14%.
- **5a-SBD (live-ticker read):** CLEAR both legs.
- MCP availability: Kraken multi_ticker fetched successfully. CLEAR.
- **All Ring 3 kill switches CLEAR.** (5a/SBD are entry-scan gates and not relevant this wake since no entries.)

## Ops notes

- Same 4 uncommitted 06-29 carry-over files remain in working tree (`docs/sentinel_10k_reset_spec_20260704.md`, `scripts/replay_cache_20260629/`, `scripts/replay_result_20260629.json`, `scripts/routine07_replay_20260629.py`) — not touched this wake.
- Routine-06 / routine-07 heartbeats still overdue (>13d) — deferred to Sat 2026-09-26 routine-04-harness resume.
- Variant rack still frozen since 07-10 scheduler outage; awaits routine-04-harness resume.
