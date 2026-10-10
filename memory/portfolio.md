# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md`; the log remains the source of truth.
> **Last rebuild:** 2026-10-10T06:54Z routine-01-overnight (PT 2026-10-09 23:54 Fri — 18h past the 06:00 PT target; fire-slot was today's overnight run). Portfolio state unchanged from midday 10-09 replay: flat, Ring 3 TRIPPED (streak 7/7). **FULL PAUSE REMAINS IN EFFECT. USER `RESUME` REQUIRED.** Date-label guard: PT calendar date at fire time = **2026-10-09**. Prior wakes this cycle: midday replay 06:30Z + two day-gate skips (routine-04-harness Fri 10-09 not-Sat, routine-05-allocation Fri 10-09 not-Sun).
>
> **W22-G exit-interpretation audit note (preserved from the pre-commit routine-03/overnight working copy; re-stated here by this overnight wake):** replay of the NEAR 10-06 bars shows the W22-G two-bar 20-EMA exit was satisfied at bar close **10-06T13:00Z** (close $5.1475 < EMA20 ~$5.163, confirming 10-06T12:00Z close $5.1673 < EMA20 ~$5.166). Had the W22-G exit been applied at that point, fill would have been $5.144923 (0.05pct slippage), net PnL ≈ −$106.13 / R ≈ −0.59 (vs. the midday-replay-logged stop-hit at 10-06T17:00Z fill $5.064802, net −$168.06 / R −1.01). The two differ by ≈$62 realized and 0.42R. Per strategy v0.4 Exit priority, rule 1 (two-bar EMA20 close confirmation) fires chronologically before rule 2 (stop) when the EMA condition is satisfied first. **Not amending the committed trade_log row** — stop-hit interpretation stands as logged by midday 10-09 (commit `f4288e9`); flagging the discrepancy for next routine-04-harness Sat memo review. Both interpretations are the 7th consecutive loss and both trip Ring 3; only magnitude differs.

## Account

- Starting equity: **$10,000.00**
- Cash: **$9,518.79** ($5,603.78 prior + NEAR exit proceeds $3,925.22 − close commission $10.21)
- Realized PnL (since inception): **−$481.20** (prior −$313.14 + NEAR 10-06 −$168.06)
- Unrealized PnL: **$0.00** (flat)
- Current equity: **$9,518.79**
- Equity peak: **$11,068.89** (unchanged)
- Drawdown from peak: **14.00%** — **BREACHES 12.5% warn by 1.50pp; still below 25% kill cap by 11.00pp**
- Since-inception return: **−4.81%**

## Open positions

**NONE — flat.** NEAR 10-06 position closed at stop-hit intrabar replay.

Portfolio risk-at-moment: **0.00%** of equity.
Open positions: **0 / 8** (strategy cap 0/4; BTC-cluster 0/2).

## Day summary — PT 2026-10-09 Thu trading day (midday replay)

- **Day PnL (realized)**: NEAR −$168.06 attributed to original 10-06 close date, not 10-09. **No same-day closes attributable to 10-09 trading day.** Day-anchored PnL vs PT-midnight equity ≈ $0.00 for 10-09 window (the −$168.06 was realized on 10-06 UTC = PT 10-06 Tue).
- **Trades opened today**: 0 (routine-02-midday is not entry-authorized per spec).
- **Trades closed today (replay-attributed)**: 1 (NEAR @ 10-06T17:00Z stop fill, recovered this wake).
- **Win rate today (closed only)**: 0% (1 loss).

## NEAR exit mechanics — 2026-10-06T17:00:00Z (replay-detected this wake)

- **Trigger**: intrabar stop-hit. 1H bar 10-06 17:00Z low $5.0258 pierced 2×ATR stop $5.067336 by $0.0415.
- **Fill**: $5.067336 × 0.9995 slippage = **$5.064802**.
- **Gross PnL**: (5.064802 − 5.254826) × 775 = **−$147.27**.
- **Commissions**: open $10.59 (already paid at entry) + close $10.21 = **$20.80**.
- **Net PnL**: **−$168.06** (R = −1.0135 → **−1.01R**).
- **Hold time**: 13h (entry 10-06T04:00Z → stop 10-06T17:00Z).
- **W22-H breakeven ratchet**: never armed. Max close post-entry $5.5048 (10-08 06:00Z). +2R trigger would have required close ≥ $5.629806 — missed by $0.1250.
- **Peak price reached**: $5.5948 high (10-08 07:00Z) = $0.4100 shy of 4R target $6.004786.
- **Post-stop price action**: continued down to $4.4404 low (10-09 00:00Z), −$0.63 below stop. Market-wide liquidation cascade 10-08 15:00Z (NEAR −7.4% hourly on $1.6M-trade pukebar) coincided with likely SBD regime. Price has since recovered to $5.18 by 10-10 06:00Z but trade already closed at stop.

## Replay context — this wake

- **Routine 02 midday** fired after a 101h gap from last routine-03-eod 10-05. First opportunity to detect the 10-06T17:00Z stop-hit was 10-06 overnight (routine-01) which did not fire; then 10-06 midday (routine-02) which did not fire; etc.
- Watchdog flags from prior wake (routines 01/02/03 all dead) were accurate predictors; this wake confirms the gap caused a 4-day open-position exposure that extended through a market-wide liquidation (NEAR $4.44 low on 10-09, well below stop).
- **No MTM-based opportunity loss** was created by the delay: stop would have been hit at same intrabar price regardless of routine timing. The delayed exit timestamp is cosmetic — fill price is the stop level per routine spec.

## Active kill-switch state (routine-02-midday replay 2026-10-10T06:30Z)

- **Daily loss cap (PT 10-09 trading day)**: 0.00% realized vs PT-midnight equity (the −$168.06 realized attributes to 10-06 trading day, not 10-09). **CLEAR by day-anchored measure; but see 7-day cumulative below.**
- **Consecutive-loss cap**: **7 losses** (NEAR 09-23, ADA 09-26, SOL 09-27 scratch, SOL 09-30, ADA 10-01, SOL 10-02, NEAR 10-06). Streak **7/7**. **RING 3 TRIP — FULL PAUSE REQUIRED. USER `RESUME` NEEDED BEFORE ANY NEW ENTRIES.**
- **Max drawdown**: **14.00% from peak $11,068.89**. BREACHES 12.5% warn by 1.50pp. **CLEAR of 25% kill cap** (11.00pp headroom).
- **Equity floor: $9,518.79 > $7,500** (+$2,018.79). **CLEAR** (2018pp headroom).
- **Exposure: 0.00% / 4%** used. **CLEAR** (position flat).
- **Cluster cap: 0/2 BTC-cluster**. **CLEAR** (flat).
- **MCP availability**: Kraken ticker + OHLCV healthy via kraken MCP. ue-scripts and yt-analysis MCPs failed (not needed for BULL ops).
- **Ring 3 state**: **TRIPPED on consecutive-loss cap (7/7).** Also warn-breached on drawdown but not kill-cap. All open positions already flat (NEAR exit this wake was the only open position).

## Ops notes

- **Entry authorization: SUSPENDED.** Routine-02-midday is already not entry-authorized by spec, but regardless — Ring 3 kill switch is now TRIPPED. No new entries by any routine until user replies `RESUME` to Telegram ALERT.
- **Pattern-of-7 rule8-cashfit-class** (06-17 SOL fallback, 07-10 BTC +0.23R, 09-30 SOL −1.00R, 10-01 ADA −1.02R, 10-02 SOL −1.03R, 10-06 NEAR −1.01R). 6 of 7 instances are losses. Cumulative P&L across 6 losing instances ≈ −$857. The only winner (07-10 BTC +0.23R) is 83d old and arguably from a different regime.
- **NEAR 2x-stop in 14 days**: 09-23 (−$172) and 10-06 (−$168). Same pair, same rule-8 trigger class, both under elevated-regime risk. P-W25R-SAMESESSION-STOP-GATE (score 9 lesson from 10-01 ADA, which cited NEAR 09-23 archetype) remains Ring-2 unapproved; 10-06 NEAR materially strengthens the evidence base for that proposal.
- **Pending Ring-2 proposals** (all still backlog, all would have blocked the 10-05 NEAR entry):
  - P-W27-CASHFIT (routine-04-harness W25R)
  - P-W25R-SAMESESSION-STOP-GATE (options a/b/d from 10-01 ADA lesson, score 9) — **NEAR 10-06 is 2nd confirming data point this month**
  - P-W25R-RATCHET-TIGHTEN (from 09-27 SOL W22-H lesson, score 8)
  - P-W25R-POSTOUTAGE-DEFER-HEURISTIC (from 09-23 lesson, score 6) — **would have DEFERRED the 10-05 NEAR entry on gap-dead state**
- **Scheduler diagnosis**: no routine fires between 10-05T04:13Z EOD and 10-10T06:30Z this wake = ~122h gap. Routine-01 overnight did not fire 10-06/10-07/10-08/10-09. Routine-02 midday did not fire 10-06/10-07/10-08/10-09. Routine-03 EOD did not fire 10-06/10-07/10-08. This is the longest contiguous routine outage since 09-20 scheduler-recovery. Root cause unknown — possibly OS sleep or scheduler service hiccup; needs investigation at next harness.
- **Drawdown trajectory**: 12.60% (10-05 EOD) → 14.00% (now, post-NEAR-stop) = +1.40pp from the single stop-out. If NEAR had been exited at 10-09 00:00Z low ($4.4404) instead of the 10-06 stop, drawdown would be ~17.3% — the W22 2×ATR stop capped the loss at −1R even under a 15%-further-down continuation.
- **Benchmark**: not re-computed this wake (replay-focused). BTC spot $82,720 per multi-ticker, down from $85,493 at 10-05 EOD = −3.2% BTC over 4-5 days. BULL now −4.81% since inception vs BTC-hold estimated −3-4% approximate same period; delta likely slightly widened but needs proper daily-anchored computation at next EOD.

## Lessons status

- Pattern-of-7 rule8-cashfit-class now explicitly a HIGH-PRIORITY lesson target. Consecutive-loss streak hitting 7/7 is a Ring 3 trip — this is NOT a routine learning event but a mandate-level safety event.
- NEAR 10-05 entry under exact 4-floor regime materialized as predicted stop-out — companion to [[lesson-2026-09-23-same-session-stop-after-regime-crystallization]] and [[lesson-2026-10-01-pattern-of-4]]. Will be formalized at next routine-04-harness as pattern-of-5 confirmation (NEAR 09-23, ADA 10-01, SOL 10-02 same-day entries, SOL 09-30 same-day, NEAR 10-06 2d-after-entry — the 2d hold on NEAR extends the archetype slightly).
- Lesson appending deferred to routine-01 or routine-04 (not this routine's job per spec).

## Notes for next wake

- **TRADING HALTED** until user `RESUME`. All routines should still fire for monitoring/MTM but reject any entry pre-check (per guardrails `kill_switch_tripped`).
- **Scheduler investigation required**: 4-day gap in routine fires caused delayed-exit cosmetic timing but did NOT affect realized PnL (stop fill is deterministic). Still, the gap needs resolution before trading resumes — otherwise even a RESUME would risk the same gap-exposure dynamic recurring.
- **User action required**:
  1. Review this NEAR stop-out and the pattern-of-7 cashfit-class evidence
  2. Resolve pending Ring-2 proposals (SAMESESSION-STOP-GATE, CASHFIT, POSTOUTAGE-DEFER, RATCHET-TIGHTEN) with Y/N/D
  3. Investigate scheduler gap root cause
  4. Send `RESUME` only after at least some of the above are addressed — ideally with explicit strategy-v0.4 change approved
- **Next routine wakeup**: routine-01-overnight would next fire ~04:00 PT 10-10 (= 11:00Z 10-10). Will MTM (no positions) and verify kill-switch state still TRIPPED. No entry scanning until RESUME.
