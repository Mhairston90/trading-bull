# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-07-09T20:07Z routine-02-midday (PT Thu **2026-07-09 13:07**, **ON-SCHEDULE +7 min** vs 13:00 PT / 20:00Z target cron `0 13 * * 1-5` — scheduler back on-schedule after 4-wake outage, confirming recovery indicated by the back-to-back midday+EOD burst 45s apart at 15:51+15:52Z earlier today). Slot identity `bull-02-midday`; PT date label 2026-07-09 Thu at fire time. **0 trade events this wake — flat book (0 open positions) carried forward from 07-07T18Z HYPE stop-hit-intrabar (~50h ago).** Position-management routine — 0 MTM computations needed, 0 exit checks needed, 0 entries per midday spec. **Live-ticker regime snapshot at 20:07Z (Kraken `kraken_multi_ticker` 15-pair, NOT authoritative — bar-close authoritative per 2026-06-12 amendment): 13/15 positive 24h, median +0.78% → 5a PASS, 5a-SBD CLEAR (both legs cleared: 13 positive » 1-ceiling AND +0.78% » −1.0% floor).** BTC $63,144.3 (+1.46%); only negatives ADA −0.86%, HYPE −0.81%. Consistent with EOD 15:52Z authoritative bar-close read (14/15 median +1.38%) — regime PASS + SBD CLEAR persisting ~4h+ into next 1H bar window. Equity **$10,509.36** unchanged (flat book, no MTM to compute), DD **5.055%** unchanged (peak $11,068.89), since-inception **+5.094%**. Loss streak **3 confirmed** as of 07-07 EOD; 07-08 skipped-scheduler (0 P&L); 07-09 flat and no exit fires → streak stays 3, cap 7, headroom 4. Kill switches all CLEAR. Rule 5b HYPE cooldown CLEARED 07-08T18Z, no active same-pair cooldowns. Rule 5a-BTC DEFERRED entry from 15:52Z EOD still standing — reserved for next authoritative overnight wake (07-10T13:00Z Fri, cron `0 6 * * 1-5`). **Silent — no Telegram (0 exits, no kill-switch trip, DD 5.055% < 12.5% warn).**

> **Prior rebuilds:** 2026-07-09T15:52Z routine-03-eod (PT Thu 08:52 OFF-SCHEDULE ~12h47m EARLY vs 04:00Z-Fri, 0 trade events flat book, equity $10,509.36 unchanged, DD 5.055%, authoritative regime 14/15 median +1.38% SBD CLEAR full-FLIP vs 07-07 EOD, 1 tech-PASS BTC/USD DEFERRED per OFF-SCHEDULE precedent 07-06T17:47Z); 2026-07-09T15:51Z routine-02-midday (PT Thu 08:51 OFF-SCHEDULE ~4h09m EARLY, 0/0 flat, equity $10,509.36 unchanged, DD 5.055%, regime live-ticker 11/15 +0.78% recovery-snapshot, 4-wake scheduler outage flagged); 2026-07-08T04:10Z routine-03-eod (PT Tue 21:10 ON-SCHEDULE +10min, 0/0 flat, equity $10,509.36, DD 5.055%, regime FAIL 1/15 SBD-ACTIVE, loss streak 3 confirmed); 2026-07-07T20:00Z routine-02-midday (PT Tue 13:00 ON-SCHEDULE, HYPE stop-hit-intrabar 18Z −$163.87/−1.02R, flat post-exit, equity $10,509.36, DD 5.055%); 2026-07-07T13:07Z routine-01-overnight (PT Tue 06:07 ON-SCHEDULE +7min, 1 OPEN HYPE/USD long 106.725 @ $72.05 rule-8 winner of 3 tech-PASS, TRX blocked R4a); 2026-07-07T04:15Z routine-03-eod (PT Mon 21:15 ON-SCHEDULE, BTC exit −$93.69 / −0.581R exit-ema20-confirm); 2026-07-06T20:00Z routine-02-midday (PT Mon 13:00 ON-SCHEDULE, MTM-only $10,748.86, DD 2.89%, 0 trades).

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
- Position values (MTM at 2026-07-09T20:07Z live-ticker basis): **$0.00** (flat)
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

## Midday snapshot — 2026-07-09 PT Thu 13:07 (fired 20:07Z, ON-SCHEDULE +7 min vs 13:00 PT target)

| Metric | Value |
|---|---|
| Wake type | routine-02-midday (bull-02-midday slot, PT date label 2026-07-09 Thu, wall-clock UTC 2026-07-09T20:07Z, **ON-SCHEDULE +7 min** vs scheduled 20:00Z) |
| MTM basis | Kraken live-ticker at 20:07Z (flat book, MTM = $0.00) |
| Entries this wake | **0** — midday routine is position-management only (skill mandate) |
| Exits this wake | **0** — 0 open positions to evaluate |
| Stop-management events | 0 (flat book) |
| Day PnL PT 2026-07-09 (Thu DTD, baseline 07-07 EOD equity $10,509.36; 07-08 skipped) | **$0.00 / 0.000%** (flat book, no trade events) |
| Equity (mix) | **$10,509.36** ($10,509.36 cash + $0.00 MTM, flat) |
| Equity peak | **$11,068.89 (unchanged; set 07-04T20:00Z midday MTM)** |
| Drawdown from peak | **5.055%** ($559.53 below peak; 7.445pp headroom to 12.5% warn) — UNCHANGED |
| Loss streak (last-known) | **3 confirmed** as of 07-07 EOD (07-05 −0.10%, 07-06 −0.795%, 07-07 −1.535%). Cap 7, headroom 4. 07-08 was skipped-scheduler (no close computed, 0 P&L). 07-09 flat book → no new loss day. |
| Regime (live-ticker snapshot 20:07Z, NOT authoritative — bar-close basis is authoritative) | **13/15 positive, median +0.78%** (calc: sorted 24h% changes ADA −0.86, HYPE −0.81 = 2 negative; ETH +0.18, SOL +0.31, XRP +0.54, ONDO +0.61, LTC +0.66, XDG +0.78, SUI +0.96, TRX +1.05, NEAR +1.28, BTC +1.46, LINK +1.51, TAO +1.66, AVAX +3.37 = 13 positive; median 8th value = +0.78%) |
| SBD status (live-ticker) | CLEAR both legs — 13 positive » 1 ceiling AND +0.78% median » −1.0% floor. Consistent with 15:52Z EOD authoritative read (14/15 median +1.38%) — persisting. |
| BTC live | $63,144.3 (+1.46% vs 24h ago) — up $196.6 vs live 15:51Z snapshot ($62,947.7). Held above 20-EMA ~$62,772 (~15:52Z indicator level); would-be BTC rank-1 rule-8 winner still tracking. |
| AVAX live | $6.689 (+3.37%, biggest mover today; still R4a-blocked 24h volume $2.57M borderline — closer to $2M floor now than mid-morning $1.85M reading) |
| HYPE live | $67.06 (−0.81%, below 07-07T18Z stop-fill $70.51; 5b cooldown expired 07-08T18Z, no re-entry gate) |
| MCP availability | Kraken OK (`kraken_multi_ticker` 15-pair fetch clean at 20:07Z). CLEAR. |

## Active kill-switch state

- Daily realized + unrealized PT 2026-07-09: **$0.00 / 0.000%** of equity (flat book, no trade events). CLEAR (5% loss cap → 5.00pp headroom).
- Consecutive losing trading days (last-known): **3 confirmed** as of 07-07 EOD; 07-08 was a MISSED WAKE (no close computed, cannot be counted or excluded here without a replay; the next EOD wake should reconcile). CLEAR (cap 7, headroom 4 conservatively).
- Max drawdown: **5.055%** from peak $11,068.89 (cap 25%, warn 12.5%, **7.445pp headroom to warn**) — CLEAR. UNCHANGED from 07-07 EOD.
- Equity floor: $10,509.36 > $7,500 floor (+$3,009.36 above floor). CLEAR.
- MCP availability: Kraken live-ticker OK. TradingView / Telegram not exercised this wake (silent). CLEAR.
- Regime gate (rule 5a): **bar-close authoritative PASS 14/15 median +1.38%** at 07-09T14Z (last authoritative read). Live-ticker at 20:07Z confirms persistence (13/15 median +0.78%). Entry gate open — but midday routine per spec takes no entries regardless.
- 5a-SBD status: **CLEAR** (both legs: live-ticker 13 positive » 1 ceiling AND +0.78% » −1.0% floor). Exit rule 1 remains 20-EMA two-bar. N/A this wake (flat book).
- Active 5b cooldowns: **NONE** — HYPE cooldown expired 2026-07-08T18:00Z. No same-pair cooldowns active.
- Cluster cap (rule 6a, BTC-cluster): **0/2** used. 2 slots headroom.
- **All Ring 3 kill switches CLEAR.** Routine-02-midday 2026-07-09T20:07Z: **0 entries (midday spec = no entries), 0 exits, 0 open at wake / 0 open after**; DD unchanged 5.055%; portfolio 0/4 positions (flat); regime PASS + SBD CLEAR persisting.

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

Next scheduled wake: routine-01-overnight Fri 2026-07-10 06:00 PT = 13:00Z Fri (cron `0 6 * * 1-5`, ~17h out from this fire). Cash reserve **$10,509.36** (100% cash). Rule-7 portfolio-risk headroom **4.00pp / 4.0%**. Cluster 0/2 unchanged, position cap 0/4 (4 slots headroom). No 5b cooldowns active. Watching for: (a) scheduler on-schedule fire at Fri 13:00Z (this midday's clean +7min ON-SCHEDULE fire confirms recovery from 4-wake outage — next Fri overnight should also fire cleanly); (b) whether BTC/USD retains full tech-PASS at 07-10T12Z bar close and executes as the rank-1 rule-8 winner (deferred at 15:52Z EOD, still tracking above key levels at 20:07Z); (c) SBD-CLEAR persistence — now ~6h+ old, additional bars strengthen confidence; (d) indicators.py universe-config drift (FARTCOIN vs ONDO) reconciliation.

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | ≈ +0.34% (equity 07-02 est ~$10,474 → $10,509.36) | ≈ +1.19% ($62,401 est 24h→ $63,144.3 live) | ≈ −0.85pp | BULL slightly behind 7d |
| 30d | ≈ +5.09% (inception $10k 2026-04-20; $10,509.36 flat) | ≈ −18.0% est (BTC 30d ago ~$77k → $63,144.3 live) | ≈ +23.1pp | BULL well ahead |
| 90d | — | — | — | not computable (BULL inception 80 days ago; window first computable ~2026-07-19) |

(BTC live-ticker 2026-07-09T20:07Z = $63,144.3. Portfolio flat.)
