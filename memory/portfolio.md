# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-07-07T20:00Z routine-02-midday (PT Tue 13:00, **ON-SCHEDULE M-F cron `0 13 * * 1-5`**, +0 min drift). Wake fired at 13:00 PT / 20:00Z as scheduled. **1 exit this wake — HYPE/USD stop pierced intrabar during 18:00Z 1H bar (bar low $70.14 < stop $70.5499); closed at stop − 0.05% slippage = $70.5146 for −$163.87 / −1.02R (`exit-stop-hit-intrabar` reason tag, per SOL 2026-06-27T19:00Z precedent).** HYPE entry was at 07-07T12:00Z close $72.05 (rule-8 winner); stop $70.5499 (2×ATR $1.5001); held 6 bars (12Z→18Z). The 18Z bar traded 71.61 open → 71.86 high → **70.14 low (stop pierced)** → 70.19 close. Post-exit portfolio is **flat 0/4 positions**. Cash post-exit = pre-entry cash $10,673.22 − trade P&L $163.87 = **$10,509.36** (equivalent: $2,983.69 pre-exit cash + $7,525.67 HYPE proceeds = $10,509.36). All-time realized PnL: $669.35 − $163.87 = **+$505.48**. **NO new entries per routine spec — midday is position-management only; entry responsibility belongs to routines #1 (overnight) and #3 (EOD).** Kill switches all CLEAR. **Rule 5b (24h cooldown for HYPE re-entry) now active until 2026-07-08T18:00Z** — HYPE off-limits for entry-scans in tonight's EOD and tomorrow's overnight wake until that timestamp passes. Watchdog carry-over (9 findings from 13:07Z overnight wake — 2× A heartbeat routine-06/07 stale, 1× C dirty-tree 4 files, 6× D variant stale-MTM). All Ring 3 kill switches CLEAR.

> **Prior rebuilds:** 2026-07-07T13:07Z routine-01-overnight (PT Tue 06:07 ON-SCHEDULE +7min, 1 OPEN HYPE/USD long 106.725 @ $72.05 rule-8 winner of 3 tech-PASS, TRX blocked R4a, regime FLIP overnight to PASS 12/15 +1.95% median; live-ticker rolling-24h divergence flagged); 2026-07-07T04:15Z routine-03-eod (PT Mon 21:15 ON-SCHEDULE, BTC exit −$93.69 / −0.581R exit-ema20-confirm, 0 new, equity $10,673.22, DD 3.58%, flat post-exit, regime 4/15 −1.54% PASS just above SBD); 2026-07-06T20:00Z routine-02-midday (PT Mon 13:00 ON-SCHEDULE, MTM-only $10,748.86, DD 2.89%, 0 trades, BTC live $63,572.6); 2026-07-06T17:47Z routine-03-eod (PT Mon 10:47 OFF-SCHEDULE ~10h13m EARLY, MTM-only $10,758.75, DD 2.80%, 0 trades); 2026-07-06T17:40Z routine-01-overnight (PT Mon 10:40 ~4h40m LATE, 1 OPEN BTC/USD long 0.16899 @ $63,679.4 rule-8 winner rank-1 of 10 tech-PASS, equity $10,763.08); 2026-07-06T10:30Z routine-01-overnight (PT Mon 03:30 EARLY, 0/0 flat, 0 tech-PASS); 2026-07-06T01:15Z routine-02-midday (PT Sun 18:15 OFF-SCHEDULE, ADA missed-scheduler replay −0.68R).

## Account

- Starting equity: **$10,000.00**
- Cash: **$10,509.36** (was $2,983.69; +$7,525.67 = HYPE exit proceeds 106.725 × $70.5146)
- Realized PnL (all-time): **+$505.48** (was +$669.35; HYPE −$163.87 stop-hit-intrabar 07-07T18Z)
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
- Position values (MTM at 20:00Z): **$0.00** (flat)
- Current equity (cash + MTM): **$10,509.36** ($10,509.36 cash + $0.00 MTM)
- Equity peak: **$11,068.89** (unchanged from 07-04T20:00Z; peak-day exceeds current equity by $559.53)
- Drawdown from peak: **5.055%** ($559.53 below peak; 7.445pp headroom to 12.5% warn cap)
- Since-inception return: **+5.094%** ($10,509.36 / $10,000 − 1)

## Open positions

*(none — flat post-HYPE stop-hit-intrabar 07-07T18Z)*

Portfolio risk-at-moment: **0.000%** (flat). Cap 4% → 4.00pp headroom.
Open positions: **0 / 8** (strategy v0.4 max-concurrent 4 → 0/4 used; BTC-cluster **0/2 used**).
Breakeven ratchet (W22-H-partial): N/A (no open positions).

## Midday snapshot — 2026-07-07 PT Tue 13:00 (fired 20:00Z, ON-SCHEDULE M-F `0 13 * * 1-5`)

| Metric | Value |
|---|---|
| Wake type | routine-02-midday (bull-02-midday slot, PT date label 2026-07-07 Tue, wall-clock UTC 2026-07-07T20:00Z, ON-SCHEDULE) |
| Entries this wake | **0** (midday is position-management only per routine spec) |
| Exits this wake | **1** (HYPE/USD stop-hit-intrabar 07-07T18Z close $70.5146, −$163.87 / −1.02R) |
| Stop-management events | 0 (no open positions to manage post-exit) |
| Wake-over-wake P&L (13:07Z→20:00Z, ~6h53m) | **−$133.98 / −1.258%** (equity $10,643.34 → $10,509.36; delta = −$29.88 prior MTM drift closed out + additional −$104.10 realized drop from live tick $71.77 to stop-fill $70.5146) |
| Day PnL PT 2026-07-07 (Tue DTD, baseline 07-06 EOD equity $10,673.22) | **−$163.86 / −1.535%** (fully realized via HYPE stop-out) |
| Equity (mix) | **$10,509.36** ($10,509.36 cash + $0.00 MTM, flat) |
| Equity peak | **$11,068.89 (unchanged; set 07-04T20:00Z midday MTM)** |
| Drawdown from peak | **5.055%** ($559.53 below peak; 7.445pp headroom to 12.5% warn) |
| Loss streak | **2 confirmed prior trading days** (07-05 close −0.10%, 07-06 close −0.795%; 07-07 in progress at −1.535% would be 3rd if it closes here — kill switch at 7, still 4 headroom) |
| Trades today | **1 opened (HYPE 07-07T12Z routine-01), 1 closed (HYPE 07-07T18Z routine-02 stop-hit-intrabar)** |
| Round-trip HYPE | Entry $72.05 → held 6 bars 12Z-18Z → stop pierced 18Z bar low $70.14 → exit $70.5146 = net −$1.5354/unit × 106.725 = −$163.87 = −1.02R |
| 7-day BULL vs BTC-hold | BULL ≈ +0.90% (equity 06-30 est ~$10,415 → $10,509.36) vs BTC ≈ +3.74% ($61,447 → $63,742.5 live) = **≈ −2.84pp BULL behind 7d** |
| 30-day BULL vs BTC-hold | BULL ≈ +5.09% (inception $10k → $10,509.36) vs BTC ≈ −17.2% est ($77k → $63.7k live) = **+22.3pp BULL well ahead 30d** |
| 90-day | not computable (inception 2026-04-20 = 78 days ago; window first computable ~2026-07-19) |

## Active kill-switch state

- Daily realized + unrealized PT 2026-07-07: **−$163.86 / −1.535%** of equity — CLEAR (5% loss cap → 3.465pp headroom).
- Consecutive losing trading days: **2 confirmed** (07-05 −0.10% close-basis, 07-06 −0.795% close-basis); 07-07 in progress at −1.535% (unrealized-into-realized). CLEAR (cap 7, headroom 4).
- Max drawdown: **5.055%** from peak $11,068.89 (cap 25%, warn 12.5%, **7.445pp headroom to warn**) — CLEAR.
- Equity floor: $10,509.36 > $7,500 floor (+$3,009.36 above floor). CLEAR.
- MCP availability: Kraken OK (`kraken_multi_ticker` 15 pairs + `kraken_ticker` HYPE + `kraken_ohlcv` HYPE 12 bars 1H all returned data). CLEAR.
- Regime gate (rule 5a): flat, N/A this wake — will be re-evaluated by routine-03-eod at 04:00Z tomorrow. Live-ticker snapshot at 20:00Z: 1/15 positive (TRX +0.54), median ≈ −1.24% → if this holds through EOD indicators.py run, next wake could enter SBD sub-state territory (SBD triggers when ≤1 positive AND median ≤ −1.0%; current live snap satisfies both, but bar-close basis is what counts, and the 07-07T12Z→07-08T12Z window is different).
- Active 5b cooldowns: **HYPE/USD** — stop-hit at 07-07T18:00Z means no HYPE re-entry until **2026-07-08T18:00Z** (spans routine-03-eod 07-07T04Z-late-Tue and routine-01-overnight 07-08T13Z; HYPE off-limits both wakes).
- Cluster cap (rule 6a, BTC-cluster): **0/2** used. 2 slots headroom.
- **All Ring 3 kill switches CLEAR.** Routine-02-midday 2026-07-07T20:00Z: **0 entries, 1 exit (HYPE stop-hit-intrabar), 1 open at wake / 0 open after**; DD widened 3.85% → 5.06% on HYPE stop-out; portfolio 0/4 positions (flat).

## Universe (unchanged since 2026-07-01 refresh)

Top 15 by 30d notional per `memory/universe.md` (refreshed at 07-01 overnight; next refresh 2026-08-01):

BTC, ETH, SOL, HYPE, XRP, ADA, NEAR, SUI, TAO, XDG, LTC, AVAX, LINK, ONDO, TRX.

## Pending exit triggers

*(none — portfolio flat)*

Next scheduled wake: routine-03-eod Tue 2026-07-07 21:00 PT = 04:00Z Wed (ON-SCHEDULE cron `0 21 * * *`, ~8h out from now). Cash reserve **$10,509.36** (100% cash). Rule-7 portfolio-risk headroom **4.00pp / 4.0%**. Cluster 0/2 unchanged, position cap 0/4 (4 slots headroom). Rule 5b HYPE cooldown active until 2026-07-08T18:00Z. Watching for: (a) regime deterioration through the EOD close — live-ticker 20:00Z shows 1/15 positive median −1.24%, if bar-close-basis at 07-08T04Z (07-07T04Z→07-08T03Z window) mirrors this, regime 5a fails outright AND 5a-SBD sub-state may activate; (b) BTC still moderately weak at $63,742.5 (live) vs 07-07T04Z close $62,981 = +$761/+1.2% over the last ~16h — modest recovery but not decisive; (c) HYPE cooldown means the previous rule-8 winner (rank 4) drops out of eligibility for the next two wakes — TAO (rank 9, BTC-cluster) becomes the leading rule-8 fallback candidate if it re-passes; NEAR (rank 7), XRP (rank 5), ADA (rank 6) all held rule-4a $2M+ liquidity historically.

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | ≈ +0.90% (equity 06-30 est ~$10,415 → $10,509.36) | ≈ +3.74% ($61,447 → $63,742.5 live) | ≈ −2.84pp | BULL behind 7d |
| 30d | ≈ +5.09% (inception $10k 2026-04-20; $10,509.36 flat) | ≈ −17.2% est (BTC 30d ago ~$77k → $63.7k live) | ≈ +22.3pp | BULL well ahead |
| 90d | — | — | — | not computable (BULL inception 78 days ago; window first computable ~2026-07-19) |

(BTC live tick 20:00Z $63,742.5. HYPE last tick 20:00Z $70.20, closed out at stop-fill $70.5146.)
