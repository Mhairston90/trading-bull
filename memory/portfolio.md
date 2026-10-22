# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md`; the log remains the source of truth.
> **Last rebuild:** 2026-10-22T04:12Z routine-03-eod (PT 2026-10-21 21:12 Wed — **off-cadence early ~3h48m before 00:00Z 10-22 slot**; 3rd routine fire this UTC day after 16:48Z gap-recovery overnight and 20:05Z on-cadence midday; label date = PT fire-time 2026-10-21 per EOD date-labeling guard). Portfolio unchanged: flat, Ring 3 TRIPPED (streak 7/7). **FULL PAUSE REMAINS IN EFFECT. USER `RESUME` STILL REQUIRED.** Ambient at fire: BTC $82,809.8, ETH $2,441.6, SOL $105.38, NEAR $5.1014, ADA $0.220447 — **0/5 sampled green 24h**, FULL REGIME FLIP from midday's 5/5 green within ~8 hours (midday→EOD breadth swing: BTC −2.03%, ETH −2.10%, SOL −2.59%, NEAR −3.81%, ADA −3.33% — mean −2.77%). Day PnL $0.00 (flat). Telegram EOD card sent per routine-03 NOTIFY mandatory daily rule.
>
> **Scheduler-gap note (carried):** no routine fires between 2026-10-12T20:41Z and 2026-10-21T16:47Z = ~9.5 days. Third major scheduler outage in ~5 weeks (09-20, 10-10, 10-21 recoveries). Flagged for next harness Sat memo as recurring-A watchdog evidence. No open positions = no PnL impact; cosmetic ops gap.
>
> **W22-G exit-interpretation audit note (carried forward from prior wake):** replay of the NEAR 10-06 bars shows the W22-G two-bar 20-EMA exit was satisfied at bar close **10-06T13:00Z** (close $5.1475 < EMA20 ~$5.163, confirming 10-06T12:00Z close $5.1673 < EMA20 ~$5.166). Had the W22-G exit been applied, fill ≈ $5.144923 (0.05pct slippage), net PnL ≈ −$106.13 / R ≈ −0.59 (vs. the logged stop-hit at 10-06T17:00Z fill $5.064802, net −$168.06 / R −1.01). Both are still the 7th consecutive loss; only magnitude differs. **Not amending the committed trade_log row** — stop-hit interpretation stands. Flagged for next routine-04-harness Sat memo review.

## Account

- Starting equity: **$10,000.00**
- Cash: **$9,518.79** (unchanged — no closes since prior wake)
- Realized PnL (since inception): **−$481.20** (unchanged)
- Unrealized PnL: **$0.00** (flat)
- Current equity: **$9,518.79**
- Equity peak: **$11,068.89** (unchanged)
- Drawdown from peak: **14.00%** — **BREACHES 12.5% warn by 1.50pp; still below 25% kill cap by 11.00pp**
- Since-inception return: **−4.81%**

## Open positions

**NONE — flat.** No positions since NEAR 10-06T17:00Z stop-hit (replay-logged 10-10).

Portfolio risk-at-moment: **0.00%** of equity.
Open positions: **0 / 8** (strategy cap 0/4; BTC-cluster 0/2).

## Day summary — PT 2026-10-21 Wed trading day (EOD close)

- **Day PnL (realized)**: $0.00 (no closes).
- **Trades opened today**: 0 (Ring 3 TRIPPED blocks all entries; routine-03 EOD scan also skipped per strategy §Entries no-kill-switch gate).
- **Trades closed today**: 0.
- **Win rate today**: n/a.
- **New equity**: $9,518.79 (unchanged).
- **Rolling 30d BULL**: −9.19% (sum of 7 losses −$963.02 / 30d-ago equity ~$10,481.81).
- **Rolling 30d BTC-hold**: −3.93% (BTC 09-22T00:00Z close $86,196.7 → now $82,809.8).
- **Delta BULL − BTC (30d)**: **−5.26pp** — BULL lagging BTC-hold.

## Active kill-switch state (routine-03-eod 2026-10-22T04:12Z — PT 2026-10-21 21:12 EOD)

- **Daily loss cap (PT 10-21 trading day)**: 0.00% realized vs PT-midnight equity $9,518.79. **CLEAR.**
- **Consecutive-loss cap**: **7 losses** (NEAR 09-23, ADA 09-26, SOL 09-27 scratch, SOL 09-30, ADA 10-01, SOL 10-02, NEAR 10-06). Streak **7/7**. **RING 3 TRIP — FULL PAUSE REMAINS. USER `RESUME` NEEDED BEFORE ANY NEW ENTRIES.**
- **Max drawdown**: **14.00% from peak $11,068.89**. BREACHES 12.5% warn by 1.50pp. **CLEAR of 25% kill cap** (11.00pp headroom).
- **Equity floor: $9,518.79 > $7,500** (+$2,018.79). **CLEAR.**
- **Exposure: 0.00% / 4%** used. **CLEAR** (flat).
- **Cluster cap: 0/2 BTC-cluster**. **CLEAR** (flat).
- **MCP availability**: Kraken multi_ticker healthy (5 pairs). Kraken 1d OHLCV healthy (35 bars for benchmark). ue-scripts MCP failed (not needed for BULL ops).
- **Ring 3 state**: **TRIPPED on consecutive-loss cap (7/7).** No new entries by any routine until user `RESUME`.

## Ops notes

- **Entry authorization: SUSPENDED.** Ring 3 trip blocks all entries. Routine-03 EOD scan also skipped per strategy §Entries no-kill-switch gate.
- **Scheduler status:** EOD slot fired ~3h48m **early** off-cadence (04:12Z vs expected ~05:00Z for 21:00 PT cron on standard time). Third routine fire this UTC day (16:48Z overnight-recovery, 20:05Z midday on-cadence, 04:12Z EOD early). Behaviorally benign — label date correct per PT fire-time (2026-10-21).
- **Pending Ring-2 proposals** (all backlog, user action required):
  - P-W27-CASHFIT (routine-04-harness W25R)
  - P-W25R-SAMESESSION-STOP-GATE (options a/b/d from 10-01 ADA lesson, pattern-of-7 strengthened)
  - P-W25R-RATCHET-TIGHTEN (from 09-27 SOL W22-H lesson, score 8)
  - P-W25R-POSTOUTAGE-DEFER-HEURISTIC (from 09-23 lesson, score 6) — would have DEFERRED the 10-05 NEAR entry on gap-dead state
- **Benchmark (EOD daily-anchored)**: BTC 30d change = $86,196.7 → $82,809.8 = **−3.93%**. BULL 30d = −$963.02 / ~$10,481.81 = **−9.19%**. Delta **−5.26pp**. BULL lagging BTC-hold over 30d (consistent with 7-loss streak). Since-inception BULL −4.81%; BTC spot has drifted enough that the BULL-vs-BTC gap narrowed modestly from midday framing.
- **Market tone shift (intraday 10-21 PT):** midday 5/5 green → EOD 0/5 red within ~8h; mean sampled drawdown −2.77%. **Near-miss regime-crystallization-within-15h instance #5** archetype — had Ring 3 been cleared pre-midday and an entry authorized, this fade would likely have put the position stop-pierce proximate. Reinforces P-W25R-POSTOUTAGE-DEFER-HEURISTIC + P-W25R-SAMESESSION-STOP-GATE urgency; routed to next harness Sat memo.

## Lessons status

- Pattern-of-7 rule8-cashfit-class remains documented. No new trades = no new lesson evidence this wake.
- EOD per routine spec can append up to 2 lessons; none appended this wake — a flat Ring-3-tripped day with no closes provides no within-trade evidence. The intraday breadth-flip (5/5→0/5) is ambient regime data, not a BULL trade lesson; routed to next harness Sat memo as further W25R evidence.

## Notes for next wake

- **TRADING HALTED** until user `RESUME`. All routines fire for monitoring/MTM but reject any entry pre-check (per guardrails `kill_switch_tripped`).
- **Scheduler status:** today's three fires (16:48Z overnight-recovery, 20:05Z midday on-cadence, 04:12Z EOD off-cadence early) indicate the scheduler is now responsive again after the 9.5d outage. Watch for any further gaps; still flagged for next harness-Sat memo.
- **User action required**:
  1. Resolve pending Ring-2 proposals with Y/N/D
  2. Investigate scheduler gap root cause
  3. Send `RESUME` only after at least some of the above are addressed
- **Next routine wakeup**: whichever cron fires next — routine-01-overnight ~05:00 PT 10-22 (12:00Z) if scheduler healthy, otherwise next recovery wake.
