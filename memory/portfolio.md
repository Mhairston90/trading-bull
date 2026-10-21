# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md`; the log remains the source of truth.
> **Last rebuild:** 2026-10-21T20:05Z routine-02-midday (PT 2026-10-21 13:05 Wed — **on-cadence** 13:00 PT midday slot; follows the 16:48Z off-cadence recovery fire ~3h17m prior and the 16:50Z off-cadence EOD ~3h15m prior as part of the same 9-day scheduler-gap recovery day). Portfolio unchanged: flat, Ring 3 TRIPPED (streak 7/7). **FULL PAUSE REMAINS IN EFFECT. USER `RESUME` STILL REQUIRED.** Ambient at fire: BTC $84,520.6, ETH $2,493.98, SOL $108.18, NEAR $5.3032, ADA $0.228031 — **5/5 sampled green 24h** (NEAR strongest +7.76%). Day PnL $0.00 (flat). No Telegram sent (no new Ring-3 trip, no exit, no new DD threshold crossing; DD still at 14.00% — already announced in prior wakes). Ambient drift from 16:48Z sample: BTC −0.14%, ETH −0.85%, SOL −0.28%, NEAR −0.26%, ADA −0.52% — mild intraday fade of the morning green but still fully positive 24h.
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

## Day summary — PT 2026-10-21 Wed trading day

- **Day PnL (realized)**: $0.00 (no closes).
- **Trades opened today**: 0 (routine-02-midday is not entry-authorized per spec; also Ring 3 TRIPPED).
- **Trades closed today**: 0.
- **Win rate today**: n/a.

## Active kill-switch state (routine-02-midday 2026-10-21T20:05Z — on-cadence)

- **Daily loss cap (PT 10-21 trading day)**: 0.00% realized vs PT-midnight equity $9,518.79. **CLEAR.**
- **Consecutive-loss cap**: **7 losses** (NEAR 09-23, ADA 09-26, SOL 09-27 scratch, SOL 09-30, ADA 10-01, SOL 10-02, NEAR 10-06). Streak **7/7**. **RING 3 TRIP — FULL PAUSE REMAINS. USER `RESUME` NEEDED BEFORE ANY NEW ENTRIES.**
- **Max drawdown**: **14.00% from peak $11,068.89**. BREACHES 12.5% warn by 1.50pp. **CLEAR of 25% kill cap** (11.00pp headroom).
- **Equity floor: $9,518.79 > $7,500** (+$2,018.79). **CLEAR.**
- **Exposure: 0.00% / 4%** used. **CLEAR** (flat).
- **Cluster cap: 0/2 BTC-cluster**. **CLEAR** (flat).
- **MCP availability**: Kraken multi_ticker healthy (returned 5 pairs). ue-scripts MCP failed (not needed for BULL ops).
- **Ring 3 state**: **TRIPPED on consecutive-loss cap (7/7).** No new entries by any routine until user `RESUME`.

## Ops notes

- **Entry authorization: SUSPENDED.** Ring 3 trip + routine-02 spec both block entries.
- **Scheduler gap:** 9d 23h since last fire. Routine-01 overnight did not fire 10-13 through 10-21 (9 missed fires). Routine-03 EOD missed 10-12 Mon-Fri. Routine-04 harness missed Sat 10-17. Routine-05 allocation missed Sun 10-18. Pattern-of-N (where N = count of scheduler-outage recoveries): now 3rd major outage in ~5 weeks (09-20 recovery, 10-10 recovery, 10-21 recovery).
- **Pending Ring-2 proposals** (all backlog, user action required):
  - P-W27-CASHFIT (routine-04-harness W25R)
  - P-W25R-SAMESESSION-STOP-GATE (options a/b/d from 10-01 ADA lesson, pattern-of-7 strengthened)
  - P-W25R-RATCHET-TIGHTEN (from 09-27 SOL W22-H lesson, score 8)
  - P-W25R-POSTOUTAGE-DEFER-HEURISTIC (from 09-23 lesson, score 6) — would have DEFERRED the 10-05 NEAR entry on gap-dead state (would also apply today if a RESUME came with the gap not yet closed)
- **Benchmark**: not re-computed this wake (lean midday). BTC spot $84,635 (recovered from $82,974 at 10-12 midday ≈ +2.0% over 9d). BULL now −4.81% since inception (unchanged — flat). Delta narrowed slightly as BTC also drifted; proper daily-anchored computation at next EOD.
- **Market tone shift:** 10-12 was full-sample red (0/5 green); today is full-sample green (5/5 green). Regime measurement deferred to overnight/EOD (not routine-02 scope).

## Lessons status

- Pattern-of-7 rule8-cashfit-class remains documented. No new trades = no new lesson evidence this wake.
- Lesson appending deferred to routine-01 or routine-04 (not this routine's job per spec).

## Notes for next wake

- **TRADING HALTED** until user `RESUME`. All routines fire for monitoring/MTM but reject any entry pre-check (per guardrails `kill_switch_tripped`).
- **Scheduler gap** needs user visibility: this is the 3rd major outage in ~5 weeks. Even if user `RESUME`s today, same gap-exposure dynamic could recur. Flagging for next harness-Sat memo.
- **User action required**:
  1. Resolve pending Ring-2 proposals with Y/N/D
  2. Investigate scheduler gap root cause
  3. Send `RESUME` only after at least some of the above are addressed
- **Next routine wakeup**: whichever cron fires next — routine-03-eod ~21:00 PT today (04:00Z 10-22) if scheduler healthy, otherwise next recovery wake.
