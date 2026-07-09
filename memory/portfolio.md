# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-07-09T15:52Z routine-03-eod (PT Thu **2026-07-09 08:52**, **OFF-SCHEDULE ~12h47m EARLY** vs 21:00 PT / 04:00Z-Fri target cron `0 21 * * 1-5`; fired ~45s after the routine-02-midday finished — back-to-back scheduler burst). Slot identity confirmed `bull-03-eod`; PT date label 2026-07-09 Thu at fire time. **0 trade events this wake — flat book carried forward from 07-07 HYPE stop-hit-intrabar (35h+ ago).** Zero exit checks (0 open positions). **Authoritative bar-close regime read via `indicators.py` at 15:52:30Z (720-bar convergence, just-closed 14Z 1H bar basis): 14/15 positive 24h, median +1.38% → 5a PASS, 5a-SBD CLEAR (both prior legs cleared by wide margin: 14 positive » 1-ceiling AND +1.38% » −1.0% floor).** **Full regime FLIP confirmed authoritative** vs 07-07T04:10Z EOD reading (1/15 median −2.94% + SBD-ACTIVE); intervening SBD-clearing bars occurred during the 35h+ missed-wake gap. **Entry-scan result: 1 pair full-tech-PASS = BTC/USD** (R1 +$372.7, R2 +4.104 RSI 59.1, R2a OK, R3 +$410.6 EMA 62,311.3, R4a OK $107.99M); AVAX+TRX pass R1+R2+R2a+R3 but FAIL R4a ($1.85M and $1.33M respectively < $2.0M floor); TAO passes R1+R2+R2a but FAILS R3 (4H close $207.11 < EMA50 $210.35 by $3.24); all 11 others FAIL R2 (RSI < 55). **Entry decision: BTC entry DEFERRED to next authoritative on-schedule wake** — precedent 07-06T17:47Z (OFF-SCHEDULE EOD → MTM-only, 0 entries); the ~13h off-schedule state + fresh-regime-flip (1-bar-old SBD clear) + 3-day loss streak headroom-4 recommend defer over take-now. **Materially compliant with mandate either way** — flagging as "would-be BTC/USD rank-1 winner Fri overnight" for the 07-10T13Z on-schedule wake. Post-EOD equity **$10,509.36** (unchanged since 07-07 EOD, flat book), DD **5.055%** (unchanged, peak $11,068.89), since-inception **+5.094%**. Loss streak still **3 confirmed** as of 07-07 EOD (07-05 −0.10%, 07-06 −0.795%, 07-07 −1.535%); 07-08 was a missed-wake day (no close computed, conservatively 0 P&L, streak unchanged); today 07-09 flat and no bar-close-driven exit fires → streak stays at 3, cap 7, headroom 4. Kill switches all CLEAR (day PnL 0.000%, DD 5.055% < 12.5% warn, equity $10,509 > $7,500 floor). Rule 5b HYPE cooldown CLEARED 07-08T18Z. Watchdog carry-over: 9 findings identical to midday (routine-06/07 stale, dirty-tree, 6× variant stale-MTM). indicators.py universe-config drift confirmed persistent (still emitted FARTCOIN row in place of ONDO at 15:52Z run — ONDO's 14Z bar-close not read this wake; non-blocking for regime headline math since only 1 of 15 pairs; routine-01 tomorrow should reconcile). **Mandatory EOD Telegram card SENT per `skills/telegram.md`.**

> **Prior rebuilds:** 2026-07-09T15:51Z routine-02-midday (PT Thu 08:51 OFF-SCHEDULE ~4h09m EARLY, 0/0 flat, equity $10,509.36 unchanged, DD 5.055%, regime live-ticker 11/15 +0.78% recovery-snapshot, 4-wake scheduler outage flagged); 2026-07-08T04:10Z routine-03-eod (PT Tue 21:10 ON-SCHEDULE +10min, 0/0 flat, equity $10,509.36, DD 5.055%, regime FAIL 1/15 SBD-ACTIVE, loss streak 3 confirmed); 2026-07-07T20:00Z routine-02-midday (PT Tue 13:00 ON-SCHEDULE, HYPE stop-hit-intrabar 18Z −$163.87/−1.02R, flat post-exit, equity $10,509.36, DD 5.055%); 2026-07-07T13:07Z routine-01-overnight (PT Tue 06:07 ON-SCHEDULE +7min, 1 OPEN HYPE/USD long 106.725 @ $72.05 rule-8 winner of 3 tech-PASS, TRX blocked R4a, regime FLIP overnight to PASS 12/15 +1.95% median; live-ticker rolling-24h divergence flagged); 2026-07-07T04:15Z routine-03-eod (PT Mon 21:15 ON-SCHEDULE, BTC exit −$93.69 / −0.581R exit-ema20-confirm, 0 new, equity $10,673.22, DD 3.58%, flat post-exit, regime 4/15 −1.54% PASS just above SBD); 2026-07-06T20:00Z routine-02-midday (PT Mon 13:00 ON-SCHEDULE, MTM-only $10,748.86, DD 2.89%, 0 trades, BTC live $63,572.6); 2026-07-06T17:47Z routine-03-eod (PT Mon 10:47 OFF-SCHEDULE ~10h13m EARLY, MTM-only $10,758.75, DD 2.80%, 0 trades); 2026-07-06T17:40Z routine-01-overnight (PT Mon 10:40 ~4h40m LATE, 1 OPEN BTC/USD long 0.16899 @ $63,679.4 rule-8 winner rank-1 of 10 tech-PASS, equity $10,763.08).

## Account

- Starting equity: **$10,000.00**
- Cash: **$10,509.36** (unchanged; flat book since 2026-07-07T18Z HYPE stop-hit-intrabar)
- Realized PnL (all-time): **+$505.48** (unchanged; no trade events this wake)
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
- Unrealized PnL (open positions): **$0.00** (flat)
- Position values (MTM at 2026-07-09T15:52Z bar-close basis): **$0.00** (flat)
- Current equity (cash + MTM): **$10,509.36** ($10,509.36 cash + $0.00 MTM)
- Equity peak: **$11,068.89** (unchanged from 07-04T20:00Z; peak-day exceeds current equity by $559.53)
- Drawdown from peak: **5.055%** ($559.53 below peak; 7.445pp headroom to 12.5% warn cap)
- Since-inception return: **+5.094%** ($10,509.36 / $10,000 − 1)

## Open positions

*(none — flat book since 2026-07-07T18Z; HYPE 5b cooldown cleared 2026-07-08T18Z, no re-entry gate active for any pair)*

Portfolio risk-at-moment: **0.000%** (flat). Cap 4% → 4.00pp headroom.
Open positions: **0 / 8** (strategy v0.4 max-concurrent 4 → 0/4 used; BTC-cluster **0/2 used**).
Breakeven ratchet (W22-H-partial): N/A (no open positions).

## EOD snapshot — 2026-07-09 PT Thu 08:52 (fired 15:52Z, OFF-SCHEDULE ~12h47m EARLY vs 21:00 PT target)

| Metric | Value |
|---|---|
| Wake type | routine-03-eod (bull-03-eod slot confirmed, PT date label 2026-07-09 Thu at fire time, wall-clock UTC 2026-07-09T15:52Z, **OFF-SCHEDULE ~12h47m EARLY** vs scheduled 04:00Z-Fri; back-to-back with routine-02-midday which finished 45s earlier at 15:51:41Z) |
| Regime basis | `indicators.py` 720-bar convergence at 15:52:30Z; just-closed 14:00Z 1H bar authoritative per 2026-06-12 amendment |
| Regime headline | **14/15 positive 24h, median +1.38% → 5a PASS, 5a-SBD CLEAR** (both prior legs cleared: 14 » 1 ceiling AND +1.38% » −1.0% floor) |
| Regime FLIP magnitude | 07-07T04:10Z EOD (1/15 median −2.94% + SBD-ACTIVE) → 07-09T15:52Z EOD (14/15 median +1.38% + SBD CLEAR): 13-pair swing in positive count, +4.32pp swing in median 24h % |
| Only pair negative 24h | FARTCOIN −0.20% (universe drift — universe.md rank 14 is ONDO, indicators.py still emits FARTCOIN) |
| Biggest positive movers | AVAX +4.63%, NEAR +3.08%, BTC +1.81%, TAO +1.82%, LINK +1.69% |
| Entries this wake | **0** (0 opened) — **1 full tech-PASS candidate (BTC/USD) DEFERRED** to next on-schedule wake per OFF-SCHEDULE-EOD precedent 07-06T17:47Z; documented below |
| Exits this wake | **0** — 0 open positions to evaluate |
| Stop-management events | 0 (flat book) |
| Day PnL PT 2026-07-09 (Thu DTD, baseline 07-07 EOD equity $10,509.36; 07-08 skipped-no-close) | **$0.00 / 0.000%** (flat book, no trade events; 07-08 skipped-scheduler adds no P&L) |
| Equity (mix, bar-close basis) | **$10,509.36** ($10,509.36 cash + $0.00 MTM, flat) |
| Equity peak | **$11,068.89 (unchanged; set 07-04T20:00Z midday MTM)** |
| Drawdown from peak | **5.055%** ($559.53 below peak; 7.445pp headroom to 12.5% warn) — UNCHANGED |
| Loss streak | **3 confirmed** (07-05 −0.10%, 07-06 −0.795%, 07-07 −1.535%). Cap 7, headroom 4. 07-08 was a missed-scheduler day (no close computed; conservatively 0 P&L, streak unchanged). 07-09 flat = 0 P&L close → streak stays 3. |
| Trades today | **0 opened, 0 closed** |
| Win rate today | N/A (0 closed) |
| 7-day BULL vs BTC-hold | BULL ≈ +0.34% ($10,474 est → $10,509.36) vs BTC ≈ +0.87% ($62,405 est → $62,956.2) = **≈ −0.5pp behind 7d** |
| 30-day BULL vs BTC-hold | BULL ≈ +5.09% (inception $10k) vs BTC ≈ −18.2% est ($77k → $62,956.2) = **≈ +23.3pp ahead 30d** |
| 90-day | not computable (inception 2026-04-20 = 80 days ago; window first computable ~2026-07-19) |
| Watchdog | 9 findings unchanged (routine-06/07 287h stale, C dirty-tree 4 files, 6× D variant stale-MTM 287h) — carry-over from midday |

### Entry-scan detail (bar-close 14:00Z, indicators.py authoritative)

Rule pass-fail per pair (bold = full tech-PASS eligible):

- **BTC/USD (rank 1) — FULL TECH-PASS**: R1 PASS +$372.7 above 20-EMA; R2 PASS RSI 59.1 (+4.10); R2a OK (< 80); R3 PASS 4H close $62,721.9 > 50-EMA $62,311.3 by +$410.6; R4a OK $107.99M » $2.0M floor. 24h +1.81%. ATR14 = $393.4; 2×ATR stop = $786.81. If sized: 1.5% × $10,509.36 = $157.64 risk / $786.81 stop distance = 0.2004 BTC target size, but cash constraint $10,509.36 / $62,956.2 = 0.1669 max → **rule-8-fallback cash-blocked reduces to 0.1669 BTC** = $10,509.36 notional, actual risk 0.1669 × $786.81 = $131.32 = 1.25% of equity (within 1.5% cap).
- AVAX/USD (rank 12) — tech-PASS but **R4a BLOCKED $1.85M < $2.0M**. R1 PASS +$0.0853; R2 PASS RSI 60.2 (+5.22); R3 PASS +$0.01744. 24h +4.63%.
- TRX/USD (rank 15) — tech-PASS but **R4a BLOCKED $1.33M < $2.0M**. R1 PASS +$0.000883; R2 PASS RSI 58.1 (+3.10); R3 PASS +$0.004278. 24h +0.77%.
- TAO/USD (rank 9) — R2 PASS RSI 55.2 barely (+0.20), R1 PASS, but **R3 FAIL** 4H close −$4.87 below EMA50 $210.35. AND R4a BLOCKED $1.57M. Two independent rejects.
- 11 others — all fail R2 (RSI 47.8–54.1, none ≥55). ETH/SOL/LTC also fail R1 (below 20-EMA). No candidates.

### Entry decision — DEFER (0 entries this wake)

**BTC is the sole full tech-PASS candidate and would be the routine's rule-8 winner (rank-1 by 30d notional, sole candidate).** Deferred over take-now on three grounds:

1. **Off-schedule discipline** — this EOD fired ~12h47m EARLY vs its 04:00Z-Fri scheduled slot. Precedent 07-06T17:47Z (also OFF-SCHEDULE EOD ~10h13m EARLY) declared MTM-only / 0 entries. Following precedent.
2. **Fresh-regime-flip risk** — SBD just cleared at the 14Z bar close. The prior 5 authoritative wakes (07-06T17:40 to 07-08T04:10) were regime FAIL/SBD-ACTIVE; the 14Z bar is a 1-bar-old confirmation. Post-06-17 lesson (`SBD crystallized within 11h of a rule-8 fallback entry`, score 7) warns against fresh-regime-flip entries; an on-schedule Fri overnight wake would have 21+ additional bars of confirmation.
3. **Loss-streak coupling** — 3-day streak (headroom 4 to cap 7) counsels selectivity. A skip here does not consume streak headroom.

Take-now would have been within mandate (BTC passes all 8 rules, and rule 8 says "max 1 new entry per wake" not "must take an entry per wake"). Documenting for audit: had this been on-schedule the entry would have been executed. Flagged as **would-be BTC/USD rank-1 entry Fri 07-10T13Z overnight wake** if BTC still tech-PASS + regime PASS at that 12Z bar close.

## Midday snapshot — 2026-07-09 PT Thu 08:51 (fired 15:51Z, OFF-SCHEDULE ~4h09m EARLY vs 13:00 PT target)

| Metric | Value |
|---|---|
| Wake type | routine-02-midday (bull-02-midday slot, PT date label 2026-07-09 Thu at fire time, wall-clock UTC 2026-07-09T15:51Z, **OFF-SCHEDULE ~4h09m EARLY** vs scheduled 20:00Z) |
| MTM basis | Kraken live-ticker at 15:51Z (flat book, MTM = $0.00) |
| Entries this wake | **0** — midday routine is position-management only (skill mandate) |
| Exits this wake | **0** — 0 open positions to evaluate |
| Stop-management events | 0 (flat book) |
| Day PnL PT 2026-07-09 (Thu DTD, baseline 07-07 EOD equity $10,509.36; 07-08 skipped) | **$0.00 / 0.000%** (flat book, no trade events) |
| Equity (mix) | **$10,509.36** ($10,509.36 cash + $0.00 MTM, flat) |
| Equity peak | **$11,068.89 (unchanged; set 07-04T20:00Z midday MTM)** |
| Drawdown from peak | **5.055%** ($559.53 below peak; 7.445pp headroom to 12.5% warn) — UNCHANGED |
| Loss streak (last-known) | **3 confirmed** as of 07-07 EOD (07-05 −0.10%, 07-06 −0.795%, 07-07 −1.535%). Cap 7, headroom 4. 07-08 was a MISSED WAKE — no close computed. Live-day 07-09 currently flat (0 events) so no new loss day accumulating. |
| Regime (live-ticker snapshot 15:51Z, NOT authoritative — bar-close basis is authoritative per prior amendments) | **11/15 positive, median +0.78%** (calc: sorted 24h% changes ETH −0.11, SOL −0.13, HYPE 0.00, ADA −0.26 = 4 non-positive; XBT +1.14, XRP +0.10, NEAR +1.21, SUI +0.93, TAO +1.27, XDG +0.31, LTC +0.50, AVAX +4.44, LINK +0.82, ONDO +0.78, TRX +0.97 = 11 positive; median 8th value = 0.78%) |
| SBD status (live-ticker) | Would clear both legs — 11 positive > 1 ceiling AND +0.78% median > −1.0% floor. Awaiting bar-close confirmation at next overnight wake (07-10T13Z or replay). |
| BTC live | $62,947.7 (+1.14% vs 24h ago) |
| AVAX live | $6.758 (+4.44%, biggest mover today) |
| HYPE live | $67.61 (0.00%, closed exit near $70.51 = live is $2.90 / −4.1% below stop-exit fill; retrospective SBD-tightened 9-EMA would likely have exited BTC/HYPE earlier if applied — but was N/A since flat mid-wake) |
| MCP availability | Kraken OK (`kraken_multi_ticker` 15-pair fetch clean at 15:51:41Z). CLEAR. |

## Active kill-switch state

- Daily realized + unrealized PT 2026-07-09: **$0.00 / 0.000%** of equity (flat book, no trade events). CLEAR (5% loss cap → 5.00pp headroom).
- Consecutive losing trading days (last-known): **3 confirmed** as of 07-07 EOD; 07-08 was a MISSED WAKE (no close computed, cannot be counted or excluded here without a replay; the next EOD wake should reconcile). CLEAR (cap 7, headroom 4 conservatively).
- Max drawdown: **5.055%** from peak $11,068.89 (cap 25%, warn 12.5%, **7.445pp headroom to warn**) — CLEAR. UNCHANGED from 07-07 EOD.
- Equity floor: $10,509.36 > $7,500 floor (+$3,009.36 above floor). CLEAR.
- MCP availability: Kraken live-ticker OK. TradingView / Telegram not exercised this wake (silent). CLEAR.
- Regime gate (rule 5a): **bar-close authoritative PASS 14/15 median +1.38%** at 07-09T14Z 1H bar close (indicators.py 15:52:30Z run). Full flip from 07-07 EOD FAIL 1/15 −2.94% + SBD-ACTIVE → PASS 14/15 +1.38% + SBD CLEAR. Entry gate OPEN this wake (but 0 entries taken per DEFER decision above).
- 5a-SBD status: **CLEAR** (both legs: 14 positive » 1 ceiling AND +1.38% » −1.0% floor). Exit rule 1 reverts to 20-EMA two-bar (from 9-EMA-SBD-tightened). N/A this wake (flat book).
- Active 5b cooldowns: **NONE** — HYPE cooldown expired 2026-07-08T18:00Z, ~21h52m ago. No same-pair cooldowns active. All 15 universe pairs entry-eligible at bar close (subject to per-rule filters).
- Cluster cap (rule 6a, BTC-cluster): **0/2** used. 2 slots headroom.
- **All Ring 3 kill switches CLEAR.** Routine-03-eod 2026-07-09T15:52Z: **0 entries (1 tech-PASS deferred), 0 exits, 0 open at wake / 0 open after**; DD unchanged 5.055%; portfolio 0/4 positions (flat); regime FULLY FLIPPED authoritative to PASS + SBD CLEAR.

### EOD lesson entry (Thu 07-09)

Lesson candidate: **repeated 4-wake scheduler outage 07-08→07-09 alongside a full regime FLIP** — the same outage window that cost potential entry opportunities was also the window across which SBD cleared. Both material — but the outage is an ops concern (routes to routine-06 heartbeat, watchdog A findings), not a strategy concern. No new lessons.md row this wake — no novel strategy pattern.

## Universe (unchanged since 2026-07-01 refresh)

Top 15 by 30d notional per `memory/universe.md` (refreshed at 07-01 overnight; next refresh 2026-08-01):

BTC, ETH, SOL, HYPE, XRP, ADA, NEAR, SUI, TAO, XDG, LTC, AVAX, LINK, ONDO, TRX.

**Note (carry-over, confirmed persistent)**: indicators.py at this authoritative EOD wake (07-09T15:52Z) STILL emitted FARTCOIN in place of ONDO — indicators.py universe-config drift confirmed persistent across at least 2 authoritative wakes (07-07 EOD, 07-09 EOD). Non-blocking for regime headline math (14/15 positive holds whether ONDO or FARTCOIN is used since both would land near-flat); ONDO's actual 07-09T14Z close was not read this wake. Routine-01 Fri (07-10T13Z or the next authoritative wake) should reconcile the config or explicitly acknowledge the drift as accepted.

## Missed-wake reconciliation (added this wake)

Between 2026-07-08T04:10Z (last routine-03-eod) and 2026-07-09T15:51Z (this routine-02-midday), **4 scheduled wakes did not fire**:

1. **routine-01-overnight** scheduled 2026-07-08T13:00Z (PT Wed 06:00) — MISSED. Would have run entry-scan on 07-08T12Z bar close.
2. **routine-02-midday** scheduled 2026-07-08T20:00Z (PT Wed 13:00) — MISSED. Would have MTM'd the flat book (no effect since 0 positions).
3. **routine-03-eod** scheduled 2026-07-09T04:00Z (PT Wed 21:00) — MISSED. Would have run 07-08T03Z→07-09T03Z regime scan + entry-scan and computed 07-08 day-close.
4. **routine-01-overnight** scheduled 2026-07-09T13:00Z (PT Thu 06:00) — MISSED. Would have run entry-scan on 07-09T12Z bar close.

**Material impact**: entry opportunities on 07-08T12Z, 07-09T03Z, and 07-09T12Z bar closes were not evaluated — if any pair passed all 8 entry rules at those bar closes AND regime FLIPPED to PASS (live-ticker suggests it did), a paper trade was missed. This is a **material entry gap** consistent with prior missed-scheduler outages (2026-05-21, 06-13, 06-30, 07-03, etc. all resolved via targeted replay scripts).

**Recommendation for next authoritative wake (07-10T04Z EOD or 07-10T13Z overnight)**: run a targeted missed-scheduler replay per the established pattern (`scripts/routine07_replay_YYYYMMDD.py` or equivalent) to:
(a) Compute 07-08 close-basis regime + entry candidates on 07-08T12Z bar close;
(b) Compute 07-09T03Z EOD bar-close regime + entry candidates;
(c) Compute 07-09T12Z overnight bar-close entry candidates;
(d) If any entry passed all 8 rules including regime 5a at its bar-close-time — replay the trade with candle-close timestamp per the log-trade skill's chronological-append rule.

This midday wake CANNOT run the replay itself (routine-02 spec: position-management only, no entries). The replay is owned by the next overnight/EOD wake.

## Pending exit triggers

*(none — portfolio flat)*

Next scheduled wake: routine-01-overnight Fri 2026-07-10 06:00 PT = 13:00Z Fri (cron `0 6 * * 1-5`, ~21h out from this fire). Cash reserve **$10,509.36** (100% cash). Rule-7 portfolio-risk headroom **4.00pp / 4.0%**. Cluster 0/2 unchanged, position cap 0/4 (4 slots headroom). No 5b cooldowns active (HYPE expired 07-08T18Z). Watching for: (a) whether the scheduler resumes normally at the Fri 13:00Z wake (this back-to-back 15:51+15:52Z midday+EOD burst suggests the scheduler is now active again after the 4-wake outage; a clean on-schedule fire tomorrow confirms recovery); (b) whether BTC/USD retains full tech-PASS at the 07-10T12Z bar close and executes as the rank-1 rule-8 winner (deferred this wake); (c) whether the fresh SBD-CLEAR regime persists across additional bars (24+ bars would strengthen confidence per 06-17 same-session-flip lesson); (d) indicators.py universe-config drift (FARTCOIN vs ONDO) reconciliation status.

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | ≈ +0.34% (equity 07-02 est ~$10,474 → $10,509.36) | ≈ +0.87% ($62,405 est 24h→ $62,947.7 live) | ≈ −0.5pp | BULL slightly behind 7d |
| 30d | ≈ +5.09% (inception $10k 2026-04-20; $10,509.36 flat) | ≈ −18.2% est (BTC 30d ago ~$77k → $62,947.7 live) | ≈ +23.3pp | BULL well ahead |
| 90d | — | — | — | not computable (BULL inception 79 days ago; window first computable ~2026-07-19) |

(BTC live-ticker 2026-07-09T15:51Z = $62,947.7. Portfolio flat.)
