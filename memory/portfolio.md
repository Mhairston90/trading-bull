# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md`; the log remains the source of truth.
> **Last rebuild:** 2026-09-30T20:00Z routine-02-midday (PT 2026-09-30 13:00) — **ON-SCHEDULE fire** vs cron `0 13 * * 1-5`. **SOL/USD LONG STOPPED OUT** intrabar at 14:00Z (bar low $118.41 pierced stop $119.6039). Book flat.

## Account

- Starting equity: **$10,000.00**
- Cash: **$10,068.04** (prior $2,141.53 + close proceeds $7,947.17 − close commission $20.66)
- Realized PnL: **+$68.04** (prior $263.72 + −$195.68 SOL 09-30 stop)
- Unrealized PnL: **$0.00** (book flat)
- Current equity: **$10,068.04**
- Equity peak: **$11,068.89**
- Drawdown from peak: **9.04%**
- Since-inception return: **+0.68%**

## Open positions

*None. Book flat.*

Portfolio risk-at-moment: **0.00%** (0 open trades).
Open positions: **0 / 8** (strategy cap 0/4; BTC cluster 0/2).

## Day summary — PT 2026-09-30 (mid-session, routine-02-midday)

- **Day PnL**: **−$195.68 / −1.91%** (SOL/USD stop-out realized).
- **Trades opened**: **1** (SOL/USD long, 13:00Z bar close).
- **Trades closed**: **1** (SOL/USD long, 14:00Z intrabar stop).
- **Win rate today**: **0/1** (100% loss rate, single trade).

## Rolling benchmark (marked to live-ticker 20:00Z 09-30)

- **BULL 30d** (08-30 → 09-30 EOD basis): equity $10,068.04 → **~−3.55%** vs 08-30 baseline (widened from −1.50% due to SOL loss).
- **BULL 7d**: **~−3.98%**.
- **BTC-hold 30d**: BTC live ~$85,262 vs ~$79,500 base → **+7.25%** (assume roughly unchanged intraday).
- **BTC-hold 7d**: **+11.60%**.
- **BULL vs BTC-hold 30d**: **~−10.80pp** behind (widened from −8.75pp at 13:13Z overnight due to SOL loss).
- **BULL vs BTC-hold 7d**: **~−15.58pp** behind.
- **90d benchmark**: not-yet-computable (post-outage cross-window; will resume after 10-15).

## Exit rationale — SOL/USD 14:00Z stop hit

Entry bar (13:00Z) closed at 120.97 (below entry fill 121.9209 already at bar-close); next bar 14:00Z opened 120.99, ran to high 121.23, then reversed hard to low **$118.41** — 118 cents below the 2×ATR stop of $119.6039. Per routine-02-midday spec: "check static 2×ATR stop — if price has pierced it intrabar, close at stop price." Fill: $119.6039, exactly 1R loss gross. Bar closed at 118.78 confirming the breakdown was not a one-tick wick.

Post-exit context (informational, no re-entry consideration): 20:00Z live-ticker bid $117.51, below stop. Subsequent 1H bars (15:00Z–20:00Z) all closed 117.17–120.26, average ~$118.90 — chop below stop. 09-27 stop-out cooldown (5b) still 24h-window-open (from 15:00Z 09-27), and this 09-30 stop-out re-triggers cooldown for another 24h from 14:00Z 09-30 → SOL blocked for re-entry until 2026-10-01T14:00Z.

## Active kill-switch state (routine-02-midday 2026-09-30T20:00Z / PT 2026-09-30 13:00; on-schedule)

- **Daily loss cap (PT 2026-09-30): −$195.68 realized, −1.91% P&L. CLEAR** (well under 5% cap; 3.09pp headroom).
- **Consecutive-loss cap: 4 losses** (NEAR 09-23, ADA 09-26, SOL 09-27 scratch, SOL 09-30 stop). Streak = **4 of 7**. CLEAR (3-loss headroom).
- **Max drawdown: 9.04%** from peak $11,068.89 (widened from 7.13% at overnight due to SOL loss). CLEAR (25% cap, 12.5% warn threshold, **3.46pp headroom to warn**).
- **Equity floor: $10,068.04 > $7,500** (+$2,568.04). CLEAR.
- **Exposure: 0.00% / 4%** used. CLEAR.
- **Cluster cap: 0/2 BTC-cluster** (SOL closed). CLEAR.
- **Universe/liquidity**: n/a (no open positions).
- **5b cooldown state**: SOL blocked until 2026-10-01T14:00Z (24h from stop-out). NEAR 09-23 (**217h ago** — expired). ADA 09-26 (**154h ago** — expired). Other 12 pairs: no active cooldown.
- **Regime 5a**: not re-evaluated this wake (midday routine is position-management-only per spec; regime check is Overnight/EOD job). Prior overnight reading 8/15 +0.44% PASS still stands.
- **MCP availability**: Kraken ticker + OHLCV healthy this wake.
- **All Ring 3 kill switches CLEAR.**

## Ops notes

- **Third on-schedule fire in a row** (04:12Z EOD, 13:13Z overnight, 20:00Z this midday). Task Scheduler drift appears reliably self-corrected; awaiting routine-04-harness Sat 10-03 XML audit for confirmation.
- **SOL stop-out was intrabar 14:00Z, ~1h after 13:00Z entry.** The entry-bar (13:00Z) had already closed below fill (close 120.97 < fill 121.9209), which is a soft warning of failed follow-through — but strategy rules don't trigger on entry-bar close (need two consecutive 1H closes < EMA20 for W22-G exit; not applicable one bar in). Next-bar low pierced stop before EMA-based exit could fire. This is a textbook "buy the top" outcome.
- **Cash-fit pattern watch**: at $10,068 equity with SOL now near $117-118, SOL would fit at ~$7,760 notional (66×117.5). BTC/ETH remain infeasible at current prices. Rule-8 cash-fit fallback continues to favor SOL/XRP/ADA/XDG-tier size names when BTC/ETH pass tech.
- **12 tech-PASS candidates at overnight scan (excluding SOL now blocked by 5b)**: ETH, XRP, SUI, TAO, XDG, NEAR, ADA, LINK, LTC, AVAX still available if their signals persist to next EOD wake. Overnight rule-8 tie-break already ordered these BTC>ETH>SOL>XRP>ADA>NEAR>SUI>TAO>XDG>LTC>AVAX>LINK.
- **W22-H breakeven ratchet never fired** on this SOL trade — trade never reached +2R (max unrealized +0.5R at 12:00-13:00Z transition). Ratchet pattern-of-4 count unchanged for routine-04-harness memo.
- **No mid-routine news scan performed** — midday routine spec is position-management-only.

## Notes for next wake

- **Book flat**. Next routine: routine-03-eod tonight ~21:00 PT / 04:00Z 10-01 will handle the day-close entry-scan and Sep monthly archive.
- **Monthly archive obligation**: routine-03-eod tonight owes the Sep archive sweep of any rows dated < 09-01 (rows 15–43 in current trade_log are 06-xx and 07-xx and one 09-23 row — the 07-xx rows are now >60 days old and belong in 2026-07 archive; the 06-xx rows belong in 2026-06 archive; the 09-23+ rows stay in trade_log until they age past 30 days). Actually 30d cutoff is 09-01 for tonight — most 07-xx rows and all 06-xx rows should archive.
- **5b cooldowns for next wake**: SOL blocked until 10-01T14:00Z.
- **Consecutive-loss streak now 4/7** — one more losing trade takes us to 5/7 (2 away from full-pause kill switch). Routine-03-eod should note this in the Telegram card.
- **Drawdown 9.04%** — 3.46pp headroom to 12.5% warn threshold. Not yet warn-worthy but tighter than yesterday.
