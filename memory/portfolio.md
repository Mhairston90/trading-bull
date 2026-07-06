# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-07-06T10:30Z routine-01-overnight (PT Mon 2026-07-06 03:30, **~2h30m EARLY vs 06:00 PT cron `0 6 * * 1-5`**). **0 trade events this wake — 2nd consecutive flat-portfolio wake since ADA 07-05T10:00Z exit.** Pulled `kraken_multi_ticker` (15 universe pairs) + `scripts/indicators.py` (720-bar 1H+4H EMA/RSI/ATR authoritative table). **Entry scan result: 0 tech-PASS candidates** — all 15 pairs FAIL R1 (1H close < 20-EMA) AND R2 (RSI < 55) at 09:00Z bar close; R3 (4H > 50-EMA) PASS on all 14 evaluated pairs (trend structure intact). **Universe-wide 1H pullback, 4H trend still bullish.** RSI cluster 32-45 across board (deep sub-55, not marginal). Regime bar-close 5a PASS 12/15 positive median +0.50%, SBD CLEAR. **Live-tick regime diverges to 0/15 positive median -1.33%** — leading-edge SBD divergence per [[lesson 2026-06-17]] — informational only, not gating (portfolio flat). No exits to check. No stop-management events. No news scan (skipped: 0 tech-PASS). No sentiment pass (skipped: 0 tech-PASS). Universe unchanged (15 pairs; next refresh 2026-08-01). Watchdog 9 findings (1 net-new = routine-06 heartbeat crossed 200h threshold — known false-positive since #5 is Sun-only cadence; routine-07 8.7+ days silent; 4 uncommitted files; 6 variant stale-MTM). No universe refresh (not first-of-month). **Cash-fit is NOT the binding rejection this wake** — first such instance in ~9 wakes; technical rejection is universal. Portfolio remains all-cash $10,763.08 / DD 2.76%.

> **Prior rebuilds:** 2026-07-06T01:15Z routine-02-midday (PT Sun 2026-07-05 18:15 OFF-SCHEDULE Sun ~5h15m late, 1 CLOSE ADA missed-scheduler-replay of 07-05T10Z bar-close W22-G exit, realized −$110.94 / −0.68R, day −0.91%, DD widened 1.87%→2.76%); 2026-07-05T04:10Z routine-03-eod (PT Sat 2026-07-04 21:10 OFF-SCHEDULE Sat, 1 CLOSE ETH missed-scheduler-replay + 1 OPEN ADA rule-8-sole-TECH-PASS; equity peak $11,068.89 unchanged from midday; DD 1.87%; broke 9-wake cash-blockade streak by taking low-notional ADA); 2026-07-04T20:00Z routine-02-midday (PT Sat 13:00 OFF-SCHEDULE, 0/0, ETH held +1.4385R peak-close 21h post-entry, NEW EQUITY PEAK $11,068.89 via ETH MTM +$45.30/+0.41% vs overnight); 2026-07-04T17:00Z routine-01-overnight (PT Sat 10:00 OFF-SCHEDULE, 0/0, ETH held +1.148R 18h post-entry, 6 TECH-PASS all cash-rejected 9th consec incl. first LINK R4a PASS at rank 13, ADA R2a RSI 83.6 climactic reject, DD 0.00% new peak $11,023.59); 2026-07-04T04:10Z routine-03-eod (PT Fri 21:10 ON-SCHEDULE, PT date 2026-07-03, 0/0, ETH held -0.17R 5h post-entry, 8 TECH-PASS all cash-rejected 8th consec, day +0.93%, DD 0.49%).

## Account

- Starting equity: **$10,000.00**
- Cash: **$10,763.08** (unchanged; all-cash post-ADA-exit)
- Realized PnL (all-time): **+$763.04** (unchanged; no realized events this wake)
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
- Unrealized PnL (open positions): **$0.00 (flat)**
- Position values: **$0.00 (no open positions)**
- Current equity (cash + MTM): **$10,763.08** (all cash, unchanged)
- Equity peak: **$11,068.89** (unchanged from 07-04T20:00Z midday ETH-MTM peak; peak-day exceeds current equity by $305.81)
- Drawdown from peak: **2.763%** ($305.81 below peak; 9.74pp headroom to 12.5% warn cap)
- Since-inception return: **+7.63%** ($10,763.08 / $10,000 − 1)

## Open positions

*(none — portfolio flat)*

Portfolio risk-at-moment: **0.000%** (no open positions). Cap 4% → 4.00pp headroom.
Open positions: **0 / 8** (strategy v0.4 max-concurrent 4 → 0/4 used; BTC-cluster 0/2 used).
Breakeven ratchet (W22-H-partial): N/A (no open positions).

## Overnight snapshot — 2026-07-06 PT Mon 03:30 (fired 10:30Z 07-06, ~2h30m EARLY vs 06:00 PT cron)

| Metric | Value |
|---|---|
| Wake type | routine-01-overnight (bull-01-overnight slot, PT date label 2026-07-06, wall-clock UTC 2026-07-06T10:30Z, ~2h30m EARLY vs `0 6 * * 1-5` cron) |
| Entries this wake | **0** (0 tech-PASS; all 15 pairs FAIL R1 AND R2 on 09:00Z bar close) |
| Exits this wake | **0** (portfolio flat at wake, no positions to check) |
| Stop-management events | 0 |
| Wake-over-wake P&L | **$0.00 / 0.00%** vs prior midday $10,763.08 (both all-cash flat) |
| Day PnL PT 2026-07-06 (Mon DTD) | **$0.00 / 0.00%** (no trades, no MTM change from flat state) |
| Equity (all cash) | **$10,763.08** |
| Equity peak | **$11,068.89 (unchanged; set 07-04T20:00Z midday MTM)** |
| Drawdown from peak | **2.763%** ($305.81 below peak; 9.74pp to 12.5% warn) |
| Loss streak | **1 trading day** (07-05 negative; 07-04 was positive close-basis) |
| Trades today | **0 opened, 0 closed** |
| 7-day BULL vs BTC-hold | BULL ≈ +3.34% (equity 06-29 est ~$10,415 → $10,763.08) vs BTC ≈ +3.9% ($60,437 → $62,814.4 ticker) = **−0.56pp BULL behind 7d** (widened from −2.09pp behind at midday as BTC-hold basis rolled forward) |
| 30-day BULL vs BTC-hold | BULL ≈ +7.63% (inception $10k) vs BTC ≈ −17.5% est ($77k → $62.8k) = **+25.1pp BULL well ahead 30d** |
| 90-day | not computable (inception 2026-04-20 = 77 days ago; window first computable ~2026-07-19) |

## Active kill-switch state

- Daily realized + unrealized PT 2026-07-06: **$0.00 / 0.00%** of equity — CLEAR (5% loss cap → full 5pp headroom).
- Consecutive losing trading days: **1** (07-05 negative close-basis; 07-04 positive). CLEAR (cap 7).
- Max drawdown: **2.763%** from peak $11,068.89 (cap 25%, warn 12.5%, **9.74pp headroom to warn**) — CLEAR.
- Equity floor: $10,763.08 > $7,500 floor (+$3,263.08 above floor). CLEAR.
- MCP availability: Kraken OK (`kraken_multi_ticker` returned data cleanly; `scripts/indicators.py` fetched 720-bar 1H+4H tables converged). CLEAR.
- Regime gate (rule 5a): **PASS bar-close 12/15 positive, median +0.50%** — well above 4/15 floor. Live-tick diverges to 0/15 positive median -1.33% (would be SBD-active on live-tick basis but that is informational only per amended DO step 3; authoritative gating uses indicators.py bar-close).
- Regime sub-state (rule 5a-SBD, bar-close authoritative): **CLEAR** — 12 positives >> 1-positive SBD ceiling AND +0.50% median > -1.0% SBD median ceiling.
- Regime sub-state (rule 5a-SBD, live-tick informational): would activate on live-tick (0/15 positive AND median -1.33% ≤ -1.0%) — [[lesson 2026-06-17 SBD leading-edge]] pattern. Not gating today because (a) authoritative read is bar-close, (b) portfolio flat so no defensive tightening needed, (c) all pairs already tech-FAIL so entry gate moot.
- Active 5b cooldowns: **none** — both recent exits (ETH 07-05T01Z, ADA 07-05T10Z) were `exit-ema20-confirm` (not `exit-stop-hit`) so 5b does not apply per rule wording.
- Cluster cap (rule 6a, BTC-cluster): **0/2** used (no positions). Full headroom.
- **All Ring 3 kill switches CLEAR.** Routine-01-overnight 2026-07-06T10:30Z: **0 entries, 0 exits, 0 open at wake / 0 open after** (portfolio unchanged flat); **DD unchanged 2.76% close-basis** (equity flat, peak flat).

## Universe (unchanged since 2026-07-01 refresh)

Top 15 by 30d notional per `memory/universe.md` (refreshed at 07-01 overnight; next refresh 2026-08-01):

BTC, ETH, SOL, HYPE, XRP, ADA, NEAR, SUI, TAO, XDG, LTC, AVAX, LINK, ONDO, TRX.

## Pending exit triggers

*(none — portfolio flat)*

Next scheduled wake: routine-02-midday Mon 2026-07-06 13:00 PT = 07-06T20:00Z (ON-SCHEDULE M-F cron `0 13 * * 1-5`). Midday is position-management-only (no entry scan). **Next entry-scan opportunity: routine-03-eod Mon 2026-07-06 21:00 PT = 07-07T04:00Z Tue** (ON-SCHEDULE cron `0 21 * * 1-5`). Cluster 0/2 used; position cap 0/4, 4 slots headroom. Cash $10,763.08 is a full non-blocked reserve — Rule-8 winner at EOD will fit any pair including BTC if BTC recovers to R1+R2 PASS. For any pair to become eligible, 1H closes need to rally back above 20-EMA AND RSI needs to cross ≥55 — from current RSI 32-45 range, a ~1-3% recovery move on 1H would be typical. Watching for: (a) whether the live-tick 24h SBD divergence resolves to bar-close activation (would tighten defensive posture if positions existed), (b) whether 4H trend structure (R3) holds through the next 4H bar close (~12:00Z 07-06), (c) which pair recovers 1H momentum first (BTC/ETH lead-lag question).

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | ≈ +3.34% (equity 06-29 est ~$10,415 → today $10,763.08 close-basis) | ≈ +3.9% ($60,437 → $62,814.4 ticker) | ≈ −0.56pp | BULL behind 7d (widened from −2.09pp at midday as BTC-hold basis rolls forward; ADA loss + BTC steady) |
| 30d | ≈ +7.63% (inception $10k 2026-04-20; close-basis $10,763.08) | ≈ −17.5% est (BTC 30d ago ~$77k → $62.8k) | ≈ +25.1pp | BULL well ahead |
| 90d | — | — | — | not computable (BULL inception 77 days ago; window first computable ~2026-07-19) |

(BTC ticker $62,814.4.)
