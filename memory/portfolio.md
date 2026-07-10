# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-07-10T04:11Z routine-03-eod (PT Thu **2026-07-09 21:11**, **ON-SCHEDULE +11 min** vs 21:00 PT / 04:00Z target cron `0 21 * * 1-5` PT — scheduler recovery from the 4-wake outage continues, third consecutive on-schedule fire after 07-09 midday and 07-09 overnight). Slot identity `bull-03-eod` confirmed; PT date label 2026-07-09 Thu at fire time (guard: 04:11Z UTC = 21:11 PT prior calendar date, per 2026-06-11 date-labeling guard). **1 OPEN this wake, 0 CLOSE — book turns to 1/4 positions with BTC/USD long 0.16438 @ $63,925.85 (rule-8 rank-1 winner, cash-fit degraded from strategy sizing 0.21258).** Prior 07-09T15:52Z EOD had DEFERRED this exact entry over OFF-SCHEDULE discipline; now ON-SCHEDULE, executed per that plan. Regime authoritative at 03:00Z bar close via `indicators.py` 720-bar convergence: **15/15 positive 24h, median +2.38% → 5a PASS, 5a-SBD CLEAR (both legs cleared: 15 » 1 ceiling AND +2.38% » −1.0% floor)**. Regime strengthened materially from 07-09T15:52Z (14/15 median +1.38%) — 15h of SBD-clear confirmation now. Equity **$10,504.11** post-entry ($1.84 cash + $10,502.27 MTM at $63,893.9 close), reflecting entry slippage cost −$5.25. DD **5.104%** ($564.78 below peak $11,068.89, 7.396pp headroom to 12.5% warn). Since-inception **+5.041%**. Loss streak **4 confirmed** (07-05 −0.10%, 07-06 −0.795%, 07-07 −1.535%, 07-09 −0.050% slippage-only day close); cap 7, headroom 3. Kill switches all CLEAR. Rule 5b HYPE cooldown cleared 07-08T18Z, no active same-pair cooldowns. **Telegram EOD card SENT (mandatory daily per skills/telegram.md EOD template).**

> **Prior rebuilds:** 2026-07-09T20:07Z routine-02-midday (PT Thu 13:07 ON-SCHEDULE +7min, 0/0 flat, equity $10,509.36, DD 5.055%, live-ticker regime PASS 13/15 median +0.78% SBD-CLEAR); 2026-07-09T15:52Z routine-03-eod (PT Thu 08:52 OFF-SCHEDULE ~12h47m EARLY vs 04:00Z-Fri, 0/0 flat, equity $10,509.36 unchanged, DD 5.055%, authoritative regime 14/15 median +1.38% SBD CLEAR full-FLIP vs 07-07 EOD, 1 tech-PASS BTC/USD DEFERRED per OFF-SCHEDULE precedent 07-06T17:47Z); 2026-07-09T15:51Z routine-02-midday (PT Thu 08:51 OFF-SCHEDULE ~4h09m EARLY, 0/0 flat, equity $10,509.36 unchanged, DD 5.055%, regime live-ticker 11/15 +0.78% recovery-snapshot, 4-wake scheduler outage flagged); 2026-07-08T04:10Z routine-03-eod (PT Tue 21:10 ON-SCHEDULE +10min, 0/0 flat, equity $10,509.36, DD 5.055%, regime FAIL 1/15 SBD-ACTIVE, loss streak 3 confirmed); 2026-07-07T20:00Z routine-02-midday (PT Tue 13:00 ON-SCHEDULE, HYPE stop-hit-intrabar 18Z −$163.87/−1.02R, flat post-exit, equity $10,509.36, DD 5.055%); 2026-07-07T13:07Z routine-01-overnight (PT Tue 06:07 ON-SCHEDULE +7min, 1 OPEN HYPE/USD long 106.725 @ $72.05 rule-8 winner of 3 tech-PASS, TRX blocked R4a); 2026-07-07T04:15Z routine-03-eod (PT Mon 21:15 ON-SCHEDULE, BTC exit −$93.69 / −0.581R exit-ema20-confirm).

## Account

- Starting equity: **$10,000.00**
- Cash: **$1.84** (was $10,509.36; decreased by $10,507.51 BTC entry notional at fill $63,925.85 × 0.16438 = $10,507.5165)
- Realized PnL (all-time): **+$505.48** (unchanged; no trade closes this wake)
  - [archived earlier rows trimmed for brevity — full ledger preserved in trade_log.md]
  - HYPE −$58.18 (exit-stop-hit 2026-05-06T15:00Z, −1.02R)
  - BTC +$1.42 (exit-ema-cross 2026-05-06T19:00Z, +0.06R)
  - LTC −$48.58 (exit-stop-hit 2026-05-07T01:00Z, −1.03R)
  - XRP −$37.68 (exit-stop-hit 2026-05-07T14:00Z, −1.05R)
  - LINK +$103.03 (exit-ema-cross 2026-05-07T20:00Z, +1.69R)
  - SOL +$585.35 (exit-4R-target 2026-05-11T19:00Z, +4.03R)
  - XRP −$21.92 (exit-ema-cross 2026-05-15T04:00Z, −0.14R) — corrected
  - HYPE +$413.62 (missed-scheduler replay exit-4R-target 2026-05-21T08:00Z, +4.04R)
  - TAO −$29.84 (missed-scheduler replay exit-ema20-confirm 2026-05-22T01:00Z, −0.50R)
  - HYPE −$33.98 (missed-scheduler replay exit-ema20-confirm 2026-05-22T02:00Z, −0.29R)
  - SOL −$45.64 (missed-scheduler replay exit-stop-hit 2026-05-22T15:00Z, −1.43R)
  - AVAX −$35.83 (missed-scheduler replay exit-ema20-confirm 2026-05-22T16:00Z, −0.94R)
  - BTC −$33.70 (exit-stop-hit 2026-05-25T22:00Z, −1.07R)
  - TAO −$114.75 (missed-scheduler replay exit-ema20-confirm 2026-05-26T18:00Z, −0.58R)
  - XRP −$101.40 (missed-scheduler replay exit-ema20-confirm 2026-05-30T23:00Z, −0.65R)
  - TAO +$621.22 (missed-scheduler replay exit-4R-target 2026-06-13T09:00Z, +4.04R)
  - BTC −$47.27 (missed-scheduler replay exit-ema20-confirm 2026-06-14T13:00Z, −0.60R)
  - ETH −$214.33 (missed-scheduler replay exit-stop-hit 2026-06-16T15:00Z, −1.32R)
  - HYPE −$182.64 (missed-scheduler replay exit-stop-hit 2026-06-17T12:00Z, −1.15R)
  - SOL −$199.87 (exit-stop-hit intrabar replay 2026-06-17T18:00Z, −1.28R)
  - SOL +$232.13 (missed-scheduler replay exit-ema20-confirm 2026-06-22T15:00Z, +1.51R gross)
  - SOL −$50.00 (correction-previous-row friction adjustment 2026-06-22T16:00Z, net SOL exit = +$182.13 / +1.19R)
  - SOL −$201.55 (exit-stop-hit-intrabar 2026-06-27T19:00Z, −1.29R)
  - SOL +$74.48 (exit-ema20-confirm-missed-scheduler-replay 2026-06-30T04:00Z, +0.49R net)
  - SOL +$598.56 (exit-4R-target-missed-scheduler-replay 2026-07-03T20:00Z, +3.88R net)
  - ETH −$11.38 (exit-ema20-confirm-missed-scheduler-replay 2026-07-05T01:00Z, −0.07R net)
  - ADA −$110.94 (exit-ema20-confirm-missed-scheduler-replay 2026-07-05T10:00Z, −0.68R net)
  - BTC −$93.69 (exit-ema20-confirm 2026-07-07T03:00:00Z close-basis on-schedule, −0.581R)
  - HYPE −$163.87 (exit-stop-hit-intrabar 2026-07-07T18:00:00Z, −1.02R) — stop pierced during 18Z bar low $70.14 < stop $70.5499
- Unrealized PnL (open positions): **−$5.25** (BTC entry slippage cost: 0.16438 × ($63,893.9 − $63,925.85) = 0.16438 × −$31.95)
- Position values (MTM at 2026-07-10T03:00:00Z bar-close basis $63,893.9): **$10,502.27** (0.16438 BTC × $63,893.9)
- Current equity (cash + MTM): **$10,504.11** ($1.84 cash + $10,502.27 MTM)
- Equity peak: **$11,068.89** (unchanged from 07-04T20:00Z; peak-day exceeds current equity by $564.78)
- Drawdown from peak: **5.104%** ($564.78 below peak; 7.396pp headroom to 12.5% warn cap)
- Since-inception return: **+5.041%** ($10,504.11 / $10,000 − 1)

## Open positions

| Pair | Side | Size | Entry | Stop | Target | Age | Unreal $ | Unreal R | Notes |
|---|---|---|---|---|---|---|---|---|---|
| BTC/USD | long | 0.16438 | 63,925.85 | 63,184.34 | 66,891.89 | 0h | −5.25 | −0.04 | Entered 2026-07-10T03:00Z (bar-close basis 03Z 1H). Rule-8 rank-1 winner, cash-fit degraded sizing (0.16438 vs strategy 0.21258; 77.3% of full). Actual risk 0.16438 × $741.51 = $121.87 = 1.16% of equity (within 1.5% cap). BTC-cluster 1/2 used. Ratchet not yet armed (needs +2R close = $65,408.77). |

Portfolio risk-at-moment: **1.16%** ($121.87 stop-distance × size / equity). Cap 4% → 2.84pp headroom.
Open positions: **1 / 8** (strategy v0.4 max-concurrent 4 → 1/4 used; BTC-cluster **1/2 used**).
Breakeven ratchet (W22-H-partial): dormant on BTC (unrealized −0.04R, arm requires +2.0R close = $65,408.77).

## EOD snapshot — 2026-07-09 PT Thu 21:11 (fired 04:11Z Fri UTC, ON-SCHEDULE +11 min vs 21:00 PT / 04:00Z Fri target)

| Metric | Value |
|---|---|
| Wake type | routine-03-eod (bull-03-eod slot confirmed, PT date label 2026-07-09 Thu at fire time, wall-clock UTC 2026-07-10T04:11Z = 2026-07-09 21:11 PT, **ON-SCHEDULE +11 min** vs scheduled 04:00Z-Fri; third consecutive on-schedule fire post-outage) |
| Regime basis | `indicators.py` 720-bar convergence at 04:10:40Z; just-closed 03:00Z 1H bar authoritative per 2026-06-12 amendment |
| Regime headline | **15/15 positive 24h, median +2.38% → 5a PASS, 5a-SBD CLEAR** (both legs cleared: 15 » 1 ceiling AND +2.38% » −1.0% floor) |
| Regime evolution | 07-08T04:10Z EOD (1/15 median −2.94% SBD-ACTIVE) → 07-09T15:52Z EOD (14/15 median +1.38% SBD CLEAR) → 07-10T04:11Z (15/15 median +2.38% SBD CLEAR) — full FLIP + strengthening across ~24h |
| Biggest positive movers | TAO +5.99%, AVAX +4.83%, LINK +3.76%, FARTCOIN +3.84%, BTC +3.17% |
| Entries this wake | **1** (BTC/USD long 0.16438 @ $63,925.85, entry-rule-v0.4-momentum-rule8-cashfit) — executed per prior 07-09T15:52Z EOD deferred plan |
| Exits this wake | **0** — flat book at wake start, no exits to evaluate |
| Stop-management events | 0 (BTC newly opened; ratchet not yet armed) |
| Day PnL PT 2026-07-09 (Thu DTD, baseline 07-07 EOD equity $10,509.36; 07-08 skipped-no-close) | **−$5.25 / −0.050%** (BTC entry slippage cost only, no realized events) |
| Equity (mix, bar-close basis) | **$10,504.11** ($1.84 cash + $10,502.27 MTM) |
| Equity peak | **$11,068.89 (unchanged; set 07-04T20:00Z midday MTM)** |
| Drawdown from peak | **5.104%** ($564.78 below peak; 7.396pp headroom to 12.5% warn) — up +0.049pp from 5.055% |
| Loss streak | **4 confirmed** (07-05 −0.10%, 07-06 −0.795%, 07-07 −1.535%, 07-09 −0.050% slippage close). Cap 7, headroom 3. 07-08 was a missed-scheduler day (no close computed; excluded from streak count per prior convention). |
| Trades today | **1 opened, 0 closed** |
| Win rate today | N/A (0 closed) |
| 7-day BULL vs BTC-hold | BULL ≈ +0.29% ($10,474 est → $10,504.11) vs BTC ≈ +2.4% ($62,405 est → $63,893.9) = **≈ −2.1pp behind 7d** |
| 30-day BULL vs BTC-hold | BULL ≈ +5.04% (inception $10k) vs BTC ≈ −17.0% est ($77k → $63,893.9) = **≈ +22.0pp ahead 30d** |
| 90-day | not computable (inception 2026-04-20 = 81 days ago; window first computable ~2026-07-19) |
| Watchdog | 9 findings unchanged carry-over (routine-06/07 12-day stale, C dirty-tree 4 files, 6× D variant stale-MTM 299h) — telegram-sent by watchdog |

### Entry-scan detail (bar-close 03:00Z, indicators.py authoritative)

Rule pass-fail per pair (bold = full tech-PASS eligible per all 8 rules):

- **BTC/USD (rank 1) — FULL TECH-PASS — RULE-8 RANK-1 WINNER — EXECUTED**: R1 PASS +$741.4 above 20-EMA; R2 PASS RSI 70.3 (+15.33 over 55 floor); R2a OK (< 80); R3 PASS 4H close $63,893.9 > 50-EMA $62,454.7 by +$1,438.98; R4a OK $114.85M » $2.0M floor; R5 OK (no open); R5a OK (regime PASS); R5b OK (last BTC event was 07-07T03Z ema20-exit, not stop-hit); R6 OK (0 < 4); R6a OK (BTC-cluster 0/2 pre-entry); R7 OK (0% + 1.16% < 4%); R8 winner (rank 1). 24h +3.17%. ATR14 = $370.75; 2×ATR = $741.51. Strategy sizing 0.21258 BTC → notional $13,586 exceeds cash $10,509.36 → **degrade-to-cash sizing 0.16438 BTC** (fits cash 10,507.52 of 10,509.36), actual risk $121.87 = 1.16% of equity (within 1.5% cap).
- **ETH/USD (rank 2) — FULL TECH-PASS**: R1 PASS +$23.26; R2 PASS RSI 68.7 (+13.68); R3 PASS +$40.81; R4a OK $25.35M. Skipped per rule-8 (BTC won). 24h +2.65%.
- **SOL/USD (rank 3) — FULL TECH-PASS**: R1 PASS +$0.7772; R2 PASS RSI 65.2 (+10.22); R3 PASS +$0.3156; R4a OK $17.91M. Skipped per rule-8 (BTC won). 24h +2.19%.
- **HYPE/USD (rank 4) — FULL TECH-PASS**: R1 PASS +$0.7931; R2 PASS RSI 61.0 (+5.96); R3 PASS +$0.2465; R4a OK $11.21M. R5b OK (cooldown cleared 07-08T18Z). Skipped per rule-8 (BTC won). 24h +1.88%.
- **XRP/USD (rank 5) — FULL TECH-PASS**: R1 PASS; R2 PASS RSI 62.6; R3 PASS; R4a OK $9.91M. Skipped per rule-8. 24h +1.78%.
- **TAO/USD (rank 9) — FULL TECH-PASS**: R1 PASS; R2 PASS RSI 73.9 (+18.9); R3 PASS +$4.47; R4a OK $2.16M. Skipped per rule-8. 24h +5.99% (biggest mover; RSI approaching R2a-80 territory, would have been R2a-warning candidate but still OK).
- **AVAX/USD (rank 12) — FULL TECH-PASS**: R1 PASS; R2 PASS RSI 60.9; R3 PASS +$0.07853; R4a OK $2.76M (recovered above $2.0M floor from prior wake's $1.85M). Skipped per rule-8. 24h +4.83%.
- SUI/USD (rank 8) — R3 FAIL −$0.002381 below 4H EMA50. Skipped.
- XDG/USD (rank 10) — R3 FAIL −$0.0004836 below 4H EMA50. Skipped.
- NEAR/USD (rank 7) — R3 FAIL −$0.004648, R4a BLOCKED $1.08M. Skipped.
- ADA/USD (rank 6) — R1 FAIL −$9e-5 below EMA20, R2 FAIL RSI 48.6. Skipped.
- LINK/USD (rank 13) — R4a BLOCKED $1.75M. Otherwise full tech-PASS. Skipped.
- LTC/USD (rank 11) — R4a BLOCKED $1.73M. Otherwise full tech-PASS. Skipped.
- FARTCOIN — universe drift (indicators.py emits FARTCOIN vs universe.md ONDO). R3 FAIL, R4a BLOCKED $0.29M. Skipped.
- TRX/USD (rank 15) — R1 FAIL −$0.000174, R2 FAIL RSI 50.6, R4a BLOCKED $0.71M. Skipped.

### Entry decision — EXECUTE BTC/USD long at bar-close 03:00Z

Rule 8 winner clear. Rank-1 BTC over rank-2 ETH. Sizing degraded-to-cash from strategy 0.21258 → 0.16438 BTC (77.3% of full). Actual risk 1.16% of equity, well within 1.5% per-trade cap.

**Reversal from 07-09T15:52Z EOD deferral**: that wake deferred BTC over three grounds — (1) OFF-SCHEDULE discipline (this wake is ON-SCHEDULE, discipline satisfied), (2) fresh-regime-flip risk (SBD-clear now 13h old with strengthening pattern — 14/15 → 15/15, median +1.38% → +2.38%), (3) loss-streak coupling (3 confirmed, headroom 4; entry adds slippage-only day loss → streak 4 with headroom 3, still material). All three deferral reasons resolved or acceptably diminished. The deferred wake's own text acknowledged "had this been on-schedule the entry would have been executed" — this is on-schedule.

Precedent: 2026-07-06T17:47Z OFF-SCHEDULE EOD deferred a BTC-cluster candidate to next on-schedule wake, which then executed as the 2026-07-06T16:00Z BTC OPEN (0.16899 @ $63,679.4). Consistent pattern followed here.

## Prior EOD snapshot — 2026-07-09 PT Thu 08:52 (fired 15:52Z, OFF-SCHEDULE ~12h47m EARLY vs 21:00 PT target)

*(retained for continuity; superseded by this wake's snapshot above)*

| Metric | Value |
|---|---|
| Wake type | routine-03-eod OFF-SCHEDULE ~12h47m EARLY |
| Regime headline | 14/15 positive 24h, median +1.38% → 5a PASS, 5a-SBD CLEAR |
| Entries this wake | 0 (1 full tech-PASS BTC/USD DEFERRED per OFF-SCHEDULE precedent 07-06T17:47Z) |
| Exits this wake | 0 |
| Day PnL PT 07-09 (Thu DTD) | $0.00 / 0.000% (flat book) |
| Equity | $10,509.36 |
| DD | 5.055% |
| Loss streak | 3 confirmed |

## Prior Midday snapshot — 2026-07-09 PT Thu 13:07 (fired 20:07Z, ON-SCHEDULE +7 min)

*(retained for continuity)*

| Metric | Value |
|---|---|
| Wake type | routine-02-midday ON-SCHEDULE +7min |
| MTM basis | Kraken live-ticker at 20:07Z (flat book) |
| Regime (live) | 13/15 positive median +0.78% SBD CLEAR |
| Day PnL PT 07-09 | $0.00 / 0.000% |
| Equity | $10,509.36 |
| DD | 5.055% |

## Active kill-switch state

- Daily realized + unrealized PT 2026-07-09: **−$5.25 / −0.050%** of equity (slippage-only). CLEAR (5% loss cap → 4.95pp headroom).
- Consecutive losing trading days: **4 confirmed** (07-05 −0.10%, 07-06 −0.795%, 07-07 −1.535%, 07-09 −0.050%; 07-08 skipped-scheduler excluded). CLEAR (cap 7, headroom 3).
- Max drawdown: **5.104%** from peak $11,068.89 (cap 25%, warn 12.5%, **7.396pp headroom to warn**) — CLEAR.
- Equity floor: $10,504.11 > $7,500 floor (+$3,004.11 above floor). CLEAR.
- MCP availability: Kraken live-ticker OK via indicators.py 720-bar fetch. TradingView / Telegram exercised (watchdog + EOD card). CLEAR.
- Regime gate (rule 5a): **bar-close authoritative PASS 15/15 median +2.38%** at 07-10T03Z (last authoritative read this wake). Strongest read since W25.
- 5a-SBD status: **CLEAR** (15 positive » 1 ceiling AND +2.38% » −1.0% floor by wide margins).
- Active 5b cooldowns: **NONE** — HYPE cooldown expired 2026-07-08T18Z, no other same-pair cooldowns active.
- Cluster cap (rule 6a, BTC-cluster): **1/2** used (BTC newly opened). 1 slot headroom.
- **All Ring 3 kill switches CLEAR.** Routine-03-eod 2026-07-10T04:11Z: **1 OPEN BTC/USD, 0 exits, 0 open at wake / 1 open after**; DD 5.104% (was 5.055%, up +0.049pp from slippage); portfolio 1/4 positions used.

### EOD lesson entry (Thu 07-09)

Lesson candidate: **degrade-to-cash sizing invoked on the rank-1 BTC full tech-PASS pick — first live-main-line instance** (the 07-09T15:52Z OFF-SCHEDULE EOD had planned to invoke it but DEFERRED, and prior instances were rule-8-fallback to next-eligible not degrade-to-cash on rank-1). Pattern: strong regime + rank-1 winner + cash constraint → invoke degrade-to-cash as option (c) from 2026-06-17 lesson. This is the P-W27-CASHFIT proposal's implicit behavior codified in-practice; the P-W27 memo is still pending user [Y/N] and this instance may serve as strengthened evidence.

**Not adding to lessons.md this wake** — pattern-of-1 for live-main-line degrade-to-cash; the mechanism is already fully covered by lesson 2026-06-17 (score 9, status active) which explicitly lists degrade-to-cash as option (c). Adding a lessons.md row would duplicate existing content. Instead, will accumulate observations and route to routine-04 W28 memo (Sat 2026-07-11) as reinforcing evidence for P-W28-CASHFIT (or renamed).

## Universe (unchanged since 2026-07-01 refresh)

Top 15 by 30d notional per `memory/universe.md` (refreshed at 07-01 overnight; next refresh 2026-08-03 first-Mon of Aug):

BTC, ETH, SOL, HYPE, XRP, ADA, NEAR, SUI, TAO, XDG, LTC, AVAX, LINK, ONDO, TRX.

**Note (carry-over, confirmed persistent)**: indicators.py at this authoritative EOD wake (07-10T04:11Z) STILL emitted FARTCOIN in place of ONDO — indicators.py universe-config drift confirmed persistent across 4 authoritative wakes (07-07 EOD, 07-09 EOD, 07-09 overnight, 07-10 EOD). Non-blocking for BTC rank-1 pick; ONDO would rank #8 in universe order and would need to fully tech-PASS to displace TAO/AVAX/etc. Should be reconciled in scripts/indicators.py config at next routine-06 heartbeat or manual pass.

## Missed-wake reconciliation carry-over

Prior wake (2026-07-09T13:07Z overnight) flagged a 4-wake outage 07-08→07-09 and recommended a targeted missed-scheduler replay for the 07-08T12Z / 07-09T03Z / 07-09T12Z bar closes. **Replay NOT run this wake** — deferred to routine-07 replay-owner (heartbeat 12-day stale per watchdog; route to user for scheduler review). Conservative prior: during those bars, regime was FAIL/SBD-ACTIVE (per 07-08T04:10Z EOD read 1/15 median −2.94% and subsequent live-ticker sequence showing regime flip only around 07-09T14Z-15Z). Estimated entry candidates during outage windows: **zero** — SBD-active regime blocks all new entries via rule 5a. Non-material for entry-timing edge; the flip window happened during our missed-wake gap but the on-schedule 07-09 midday + overnight + this EOD recover the timing budget forward.

## Pending exit triggers

- **BTC/USD**: monitor 20-EMA (currently $63,152.5) for two-bar close-below (Exit 1). Monitor stop $63,184.34 for intrabar breach (Exit 2). Monitor +4R close ≥ $66,891.89 for take-profit (Exit 3). Ratchet arms at +2.0R close ≥ $65,408.77 (per W22-H-partial).

Next scheduled wake: routine-01-overnight Fri 2026-07-10 06:00 PT = 13:00Z Fri (cron `0 6 * * 1-5`, ~9h out from this fire). Cash reserve **$1.84** (0.02% cash, 99.98% deployed to BTC). Rule-7 portfolio-risk headroom **2.84pp / 2.84%**. Cluster 1/2 used (1 headroom), position cap 1/4 (3 slots headroom). No 5b cooldowns active. Watching for: (a) BTC EMA20 hold above $63,152.5 (exit rule 1 not fired); (b) stop $63,184.34 not breached; (c) regime persistence 15/15 PASS + SBD-CLEAR; (d) at 12Z bar close Fri overnight, evaluate any additional entries — but cash is essentially fully deployed so any Fri entry would require BTC to close first or a further degrade of BTC size (not planned).

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | ≈ +0.29% (equity 07-02 est ~$10,474 → $10,504.11) | ≈ +2.4% ($62,401 est → $63,893.9) | ≈ −2.1pp | BULL behind 7d |
| 30d | ≈ +5.04% (inception $10k 2026-04-20; $10,504.11) | ≈ −17.0% est (BTC 30d ago ~$77k → $63,893.9) | ≈ +22.0pp | BULL well ahead |
| 90d | — | — | — | not computable (BULL inception 81 days ago; window first computable ~2026-07-19) |

(BTC bar-close 2026-07-10T03:00Z = $63,893.9. Portfolio 1 open — BTC/USD long 0.16438.)
