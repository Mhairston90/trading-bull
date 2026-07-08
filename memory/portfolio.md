# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-07-08T04:10Z routine-03-eod (PT Tue **2026-07-07 21:10**, ON-SCHEDULE cron `0 21 * * 1-5`, +10 min drift). Wake fired at 21:10 PT / 04:10Z Wed as scheduled — per date-labeling guard, EOD wake takes PT-date-at-fire-time = 2026-07-07. **0 trade events this wake — flat book from midday HYPE stop-hit-intrabar carry-forward.** No exit checks (0 open positions). Entry scan yielded **0 tech-PASS candidates across 15 universe pairs** — ALL pairs FAIL R1 (>EMA20). Regime **1/15 positive median −2.94% → 5a FAIL AND 5a-SBD ACTIVE** (both sub-state legs satisfied by wide margin: only TRX +0.22% positive; median −2.94% << −1.0% floor). Post-EOD equity **$10,509.36** (unchanged from midday close), DD **5.055%**, since-inception **+5.094%**. Loss streak now **3 confirmed** (07-05 −0.10%, 07-06 −0.795%, 07-07 −1.535% — cap 7, headroom 4). Watchdog carry-over (9 findings from earlier wakes — all unchanged: 2× A routine-06/07 stale, 1× C dirty-tree 4 files, 6× D variant stale-MTM). Kill switches all CLEAR. Rule 5b HYPE cooldown active until 2026-07-08T18:00Z (spans overnight 07-08T13Z + midday 07-08T20Z). indicators.py universe-config drift noted (still emits FARTCOIN in place of ONDO; non-blocking for regime headline math; routine-01 tomorrow to reconcile).

> **Prior rebuilds:** 2026-07-07T20:00Z routine-02-midday (PT Tue 13:00 ON-SCHEDULE, HYPE stop-hit-intrabar 18Z −$163.87/−1.02R, flat post-exit, equity $10,509.36, DD 5.055%); 2026-07-07T13:07Z routine-01-overnight (PT Tue 06:07 ON-SCHEDULE +7min, 1 OPEN HYPE/USD long 106.725 @ $72.05 rule-8 winner of 3 tech-PASS, TRX blocked R4a, regime FLIP overnight to PASS 12/15 +1.95% median; live-ticker rolling-24h divergence flagged); 2026-07-07T04:15Z routine-03-eod (PT Mon 21:15 ON-SCHEDULE, BTC exit −$93.69 / −0.581R exit-ema20-confirm, 0 new, equity $10,673.22, DD 3.58%, flat post-exit, regime 4/15 −1.54% PASS just above SBD); 2026-07-06T20:00Z routine-02-midday (PT Mon 13:00 ON-SCHEDULE, MTM-only $10,748.86, DD 2.89%, 0 trades, BTC live $63,572.6); 2026-07-06T17:47Z routine-03-eod (PT Mon 10:47 OFF-SCHEDULE ~10h13m EARLY, MTM-only $10,758.75, DD 2.80%, 0 trades); 2026-07-06T17:40Z routine-01-overnight (PT Mon 10:40 ~4h40m LATE, 1 OPEN BTC/USD long 0.16899 @ $63,679.4 rule-8 winner rank-1 of 10 tech-PASS, equity $10,763.08); 2026-07-06T10:30Z routine-01-overnight (PT Mon 03:30 EARLY, 0/0 flat, 0 tech-PASS).

## Account

- Starting equity: **$10,000.00**
- Cash: **$10,509.36** (unchanged from midday close; flat book)
- Realized PnL (all-time): **+$505.48** (unchanged from midday; no trade events this wake)
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
- Position values (MTM at 04:00Z close): **$0.00** (flat)
- Current equity (cash + MTM): **$10,509.36** ($10,509.36 cash + $0.00 MTM)
- Equity peak: **$11,068.89** (unchanged from 07-04T20:00Z; peak-day exceeds current equity by $559.53)
- Drawdown from peak: **5.055%** ($559.53 below peak; 7.445pp headroom to 12.5% warn cap)
- Since-inception return: **+5.094%** ($10,509.36 / $10,000 − 1)

## Open positions

*(none — flat, no HYPE re-entry allowed until 2026-07-08T18:00Z per 5b cooldown)*

Portfolio risk-at-moment: **0.000%** (flat). Cap 4% → 4.00pp headroom.
Open positions: **0 / 8** (strategy v0.4 max-concurrent 4 → 0/4 used; BTC-cluster **0/2 used**).
Breakeven ratchet (W22-H-partial): N/A (no open positions).

## EOD snapshot — 2026-07-07 PT Tue 21:10 (fired 04:10Z Wed, ON-SCHEDULE M-F cron `0 21 * * 1-5`, +10min drift)

| Metric | Value |
|---|---|
| Wake type | routine-03-eod (bull-03-eod slot, PT date label 2026-07-07 Tue at fire time, wall-clock UTC 2026-07-08T04:10Z, ON-SCHEDULE) |
| Entries this wake | **0** (0 tech-PASS candidates AND regime 5a FAIL AND SBD ACTIVE — multi-reject) |
| Exits this wake | **0** (no open positions to check) |
| Stop-management events | 0 (flat book) |
| Day PnL PT 2026-07-07 (Tue DTD, baseline 07-06 EOD equity $10,673.22) | **−$163.86 / −1.535%** (fully realized via HYPE stop-hit-intrabar 18Z) |
| Equity (mix) | **$10,509.36** ($10,509.36 cash + $0.00 MTM, flat) |
| Equity peak | **$11,068.89 (unchanged; set 07-04T20:00Z midday MTM)** |
| Drawdown from peak | **5.055%** ($559.53 below peak; 7.445pp headroom to 12.5% warn) |
| Loss streak | **3 confirmed** (07-05 close −0.10%, 07-06 close −0.795%, 07-07 close **−1.535%** — cap 7, headroom 4) |
| Trades today | **1 opened (HYPE 07-07T12Z routine-01), 1 closed (HYPE 07-07T18Z routine-02 stop-hit-intrabar)** |
| Win rate today | **0%** (0 winners / 1 closed) |
| Regime (indicators.py bar-close basis 07-07T03Z→07-08T03Z window) | **1/15 positive, median −2.94% → 5a FAIL AND 5a-SBD ACTIVE** |
| Only pair positive 24h | TRX +0.22% (blocked by R4a $1.08M < $2.0M) |
| Worst movers | AVAX −5.95%, ADA −5.84%, FARTCOIN −9.61% (indicators.py config drift — universe.md swapped to ONDO at 07-01) |
| 7-day BULL vs BTC-hold | BULL ≈ +0.90% vs BTC ≈ +2.04% ($61,447 → $62,703) = **≈ −1.14pp behind 7d** |
| 30-day BULL vs BTC-hold | BULL ≈ +5.09% vs BTC ≈ −18.6% est ($77k → $62,703) = **+23.7pp BULL well ahead 30d** |
| 90-day | not computable (inception 2026-04-20 = 79 days ago; window first computable ~2026-07-19) |

## Active kill-switch state

- Daily realized + unrealized PT 2026-07-07: **−$163.86 / −1.535%** of equity — CLEAR (5% loss cap → 3.465pp headroom).
- Consecutive losing trading days: **3 confirmed** (07-05 −0.10% close-basis, 07-06 −0.795% close-basis, 07-07 **−1.535% close-basis**). CLEAR (cap 7, headroom 4).
- Max drawdown: **5.055%** from peak $11,068.89 (cap 25%, warn 12.5%, **7.445pp headroom to warn**) — CLEAR.
- Equity floor: $10,509.36 > $7,500 floor (+$3,009.36 above floor). CLEAR.
- MCP availability: Kraken OK (`indicators.py` 720-bar convergence run for 15 pairs completed cleanly). CLEAR.
- Regime gate (rule 5a): **FAIL 1/15 positive, median −2.94%** (bar-close basis; authoritative). Blocks new entries.
- **5a-SBD sub-state: ACTIVE** (both legs satisfied: 1 positive ≤ 1-positive ceiling AND median −2.94% ≤ −1.0% floor). Exit rule 1-SBD (9-EMA two-bar) would apply if any positions were open; N/A this wake (flat book). Zero avoided-give-back credited this wake.
- Active 5b cooldowns: **HYPE/USD** — no HYPE re-entry until **2026-07-08T18:00Z** (spans overnight 07-08T13Z + midday 07-08T20:00Z; HYPE off-limits for both wakes; clears before 07-08T21Z EOD).
- Cluster cap (rule 6a, BTC-cluster): **0/2** used. 2 slots headroom.
- **All Ring 3 kill switches CLEAR.** Routine-03-eod 2026-07-08T04:10Z: **0 entries, 0 exits, 0 open at wake / 0 open after**; DD unchanged 5.055%; portfolio 0/4 positions (flat); regime deteriorated PASS 12/15 → FAIL 1/15 AND SBD ACTIVE over 15h.

## Universe (unchanged since 2026-07-01 refresh)

Top 15 by 30d notional per `memory/universe.md` (refreshed at 07-01 overnight; next refresh 2026-08-01):

BTC, ETH, SOL, HYPE, XRP, ADA, NEAR, SUI, TAO, XDG, LTC, AVAX, LINK, ONDO, TRX.

**Note**: indicators.py this wake still emitted FARTCOIN in place of ONDO — indicators.py universe-config drift. Non-blocking for regime headline math (both are single-pair rows within the 15-pair aggregate); ONDO's actual 07-08T03Z close was not read this wake. Routine-01 tomorrow to reconcile the config.

## Pending exit triggers

*(none — portfolio flat)*

Next scheduled wake: routine-01-overnight Wed 2026-07-08 06:00 PT = 13:00Z Wed (ON-SCHEDULE cron `0 6 * * 1-5`, ~9h out from now). Cash reserve **$10,509.36** (100% cash). Rule-7 portfolio-risk headroom **4.00pp / 4.0%**. Cluster 0/2 unchanged, position cap 0/4 (4 slots headroom). Rule 5b HYPE cooldown active until 2026-07-08T18:00Z (blocks overnight 13Z + midday 20Z HYPE re-entries; clears before 07-08T21Z EOD). Watching for: (a) whether SBD clears through the overnight — requires either ≥2 positive pairs OR median > −1.0% at the 07-08T12Z just-closed bar (currently 1/15 positive median −2.94%, needs ~2pp median lift; historical precedent: 06-17→06-18 SBD activation persisted 8 wakes before clearing); (b) whether any single pair recovers R1 (>EMA20) — currently ALL 15 pairs fail R1, first pair to recover would become the leading candidate; (c) whether the indicators.py universe-config drift (FARTCOIN vs ONDO) resolves autonomously or needs a code touch (out of routine scope this wake).

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | ≈ +0.90% (equity 06-30 est ~$10,415 → $10,509.36) | ≈ +2.04% ($61,447 → $62,703) | ≈ −1.14pp | BULL behind 7d |
| 30d | ≈ +5.09% (inception $10k 2026-04-20; $10,509.36 flat) | ≈ −18.6% est (BTC 30d ago ~$77k → $62,703) | ≈ +23.7pp | BULL well ahead |
| 90d | — | — | — | not computable (BULL inception 79 days ago; window first computable ~2026-07-19) |

(BTC bar-close 03:00Z 07-08 = $62,703.1 per indicators.py. Portfolio flat.)
