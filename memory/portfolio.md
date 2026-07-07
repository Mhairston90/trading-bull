# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-07-07T13:07Z routine-01-overnight (PT Tue 06:07, **ON-SCHEDULE M-F cron `0 6 * * 1-5`**, +7 min drift). Wake fired 7 min after 06:00 PT cron; just-closed 1H = 12:00Z bar close. **Regime FLIP overnight**: indicators.py 720-bar 24h reports **12/15 positive, median +1.95% → 5a PASS with strong cushion** (vs prior EOD 4/15 −1.54%). SBD CLEAR. **3 tech-PASS candidates on 12Z close (indicators.py authoritative)**: HYPE/USD (R1+R2+R3+R4a PASS, RSI 60.4), TAO/USD (R1+R2+R3+R4a PASS, RSI 56.0), TRX/USD (R1+R2+R3 PASS but R4a FAIL $1.18M < $2.0M). **Rule 8 winner: HYPE/USD** (rank 4 > TAO rank 9; TRX out via R4a). **1 new OPEN**: HYPE/USD long 106.725 @ $72.05 (12Z close), stop $70.5499 (2×ATR 1.5001), 4R target $78.0504, risk $160.10 = 1.500% equity. Cash post-entry $10,673.22 − $7,689.53 = **$2,983.69**. Portfolio risk-at-moment 1.500% (from 0%). Cluster 6a status: HYPE **not** in BTC-cluster {BTC,ETH,SOL,TAO,AVAX,SUI,LINK}, so cluster stays **0/2** used — TAO entry (if it appeared later same wake) would be same-wake blocked by rule 8 max-1-entry regardless. Positions 1/4 used. **Notable data divergence flagged**: indicators.py bar-close-basis 24h shows 12/15 positive median +1.95%, but live ticker rolling-24h at 13:09Z shows only 2/15 positive (HYPE +1.69, TRX +0.34), median ≈ −1.51% — the 07-06T12Z→07-07T12Z window captures a large 07-06 midday dip as baseline and the 07-07 overnight-to-morning recovery from that low, whereas rolling-24h anchors 24h ago at 13:09Z 07-06 which was higher. Per 2026-06-12 amendment indicators.py is authoritative for rule 5a; the divergence does not change entry-eligibility verdict but IS logged in research_log as a signal-quality caution. Watchdog 13:07:05Z re-ran (9 findings, unchanged carryover): 2× A heartbeat routine-06/07 (236h), 1× C dirty-tree 4 files, 6× D variant stale-MTM 236h. All Ring 3 kill switches CLEAR.

> **Prior rebuilds:** 2026-07-07T04:15Z routine-03-eod (PT Mon 21:15 ON-SCHEDULE, BTC exit −$93.69 / −0.581R exit-ema20-confirm, 0 new, equity $10,673.22, DD 3.58%, flat post-exit, regime 4/15 −1.54% PASS just above SBD); 2026-07-06T20:00Z routine-02-midday (PT Mon 13:00 ON-SCHEDULE, MTM-only $10,748.86, DD 2.89%, 0 trades, BTC live $63,572.6); 2026-07-06T17:47Z routine-03-eod (PT Mon 10:47 OFF-SCHEDULE ~10h13m EARLY, MTM-only $10,758.75, DD 2.80%, 0 trades); 2026-07-06T17:40Z routine-01-overnight (PT Mon 10:40 ~4h40m LATE, 1 OPEN BTC/USD long 0.16899 @ $63,679.4 rule-8 winner rank-1 of 10 tech-PASS, equity $10,763.08); 2026-07-06T10:30Z routine-01-overnight (PT Mon 03:30 EARLY, 0/0 flat, 0 tech-PASS); 2026-07-06T01:15Z routine-02-midday (PT Sun 18:15 OFF-SCHEDULE, ADA missed-scheduler replay −0.68R); 2026-07-05T04:10Z routine-03-eod (PT Sat 21:10 OFF-SCHEDULE Sat, 1 CLOSE ETH + 1 OPEN ADA; equity peak $11,068.89 unchanged).

## Account

- Starting equity: **$10,000.00**
- Cash: **$2,983.69** (was $10,673.22; −$7,689.53 = HYPE entry cost 106.725 × $72.05)
- Realized PnL (all-time): **+$669.35** (unchanged — no realized events this wake)
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
- Unrealized PnL (open positions): **−$29.88** (HYPE MTM: (71.77 live tick − 72.05 entry) × 106.725 = −$29.88 = −0.187R)
- Position values (MTM at 13:09Z live tick): **$7,659.65** (HYPE 106.725 × $71.77)
- Current equity (cash + MTM): **$10,643.34** ($2,983.69 cash + $7,659.65 MTM)
- Equity peak: **$11,068.89** (unchanged from 07-04T20:00Z; peak-day exceeds current equity by $425.55)
- Drawdown from peak: **3.846%** ($425.55 below peak; 8.65pp headroom to 12.5% warn cap)
- Since-inception return: **+6.433%** ($10,643.34 / $10,000 − 1)

## Open positions

| Pair | Side | Size | Entry | Stop | Target | Entry timestamp | R risk | Notes |
|---|---|---|---|---|---|---|---|---|
| HYPE/USD | long | 106.725 | 72.05 | 70.5499 | 78.0504 | 2026-07-07T12:00:00Z | 1.500% ($160.10) | Rule-8 winner rank 4 among 3 tech-PASS (HYPE, TAO, TRX-blocked-R4a). Not in BTC-cluster (cluster 0/2 unchanged). 2×ATR stop dist $1.5001. Live 13:09Z bid/ask $71.79/$71.81 (spread 1.4-4.2 bps, tight). W22-H breakeven ratchet arm level: 1H close ≥ 72.05 + 2×1.5001 = $75.0502. |

Portfolio risk-at-moment: **1.500%** ($160.10 / $10,673.22 basis). Cap 4% → **2.500pp headroom** available for future entries.
Open positions: **1 / 8** (strategy v0.4 max-concurrent 4 → 1/4 used; BTC-cluster **0/2 used** since HYPE not in cluster).
Breakeven ratchet (W22-H-partial): HYPE not yet armed (current close vs. +2R arm level $75.0502 = −$3.00 below arm, +4.16% of entry away).

## Overnight snapshot — 2026-07-07 PT Tue 06:07 (fired 13:07Z, ON-SCHEDULE M-F `0 6 * * 1-5`, +7 min drift)

| Metric | Value |
|---|---|
| Wake type | routine-01-overnight (bull-01-overnight slot, PT date label 2026-07-07 Tue, wall-clock UTC 2026-07-07T13:07Z, ON-SCHEDULE) |
| Entries this wake | **1** (HYPE/USD long 106.725 @ $72.05, rule-8 winner rank 4 of 3 tech-PASS; TRX blocked R4a) |
| Exits this wake | **0** (portfolio was flat at wake — no exit-management needed) |
| Stop-management events | 0 (HYPE brand-new entry, no arm/ratchet events yet) |
| Wake-over-wake P&L (04:15Z→13:07Z, ~8h55m) | **−$29.88 / −0.280%** (unrealized MTM only; no realized events; HYPE dropped $0.28 from 12Z close $72.05 to 13:09Z live $71.77) |
| Day PnL PT 2026-07-07 (Tue DTD, baseline 07-06 EOD equity $10,673.22) | **−$29.88 / −0.280%** (unrealized only; no realized events today yet) |
| Equity (mix) | **$10,643.34** ($2,983.69 cash + $7,659.65 MTM) |
| Equity peak | **$11,068.89 (unchanged; set 07-04T20:00Z midday MTM)** |
| Drawdown from peak | **3.846%** ($425.55 below peak; 8.65pp headroom to 12.5% warn) |
| Loss streak | **2 trading days** (07-05 close −0.10%, 07-06 close −0.795%; 07-07 in progress, currently −0.28% unrealized) |
| Trades today | **1 opened (HYPE 07-07T12Z routine-01), 0 closed** |
| 7-day BULL vs BTC-hold | BULL ≈ +2.19% (equity 06-30 est ~$10,415 → $10,643.34) vs BTC ≈ +2.97% ($61,447 → $63,273.7 live) = **≈ −0.78pp BULL slightly behind 7d** |
| 30-day BULL vs BTC-hold | BULL ≈ +6.43% (inception $10k → $10,643.34) vs BTC ≈ −17.8% est ($77k → $63.3k live) = **+24.2pp BULL well ahead 30d** |
| 90-day | not computable (inception 2026-04-20 = 78 days ago; window first computable ~2026-07-19) |

## Active kill-switch state

- Daily realized + unrealized PT 2026-07-07: **−$29.88 / −0.280%** of equity — CLEAR (5% loss cap → 4.72pp headroom).
- Consecutive losing trading days: **2** (07-05 −0.10% close-basis, 07-06 −0.795% close-basis). CLEAR (cap 7).
- Max drawdown: **3.846%** from peak $11,068.89 (cap 25%, warn 12.5%, **8.65pp headroom to warn**) — CLEAR.
- Equity floor: $10,643.34 > $7,500 floor (+$3,143.34 above floor). CLEAR.
- MCP availability: Kraken OK (`kraken_multi_ticker` 15 pairs + `kraken_spread` HYPE/TAO returned data; indicators.py 720-bar EMA/RSI/ATR converged). CLEAR.
- Regime gate (rule 5a per indicators.py, authoritative): **PASS 12/15 positive, median +1.95%** (bar-close basis 07-06T12Z→07-07T12Z window). Live-ticker rolling-24h divergence noted (2/15 positive, median ≈ −1.51%) — see research_log for full note. Does not change verdict.
- Regime sub-state (rule 5a-SBD): **CLEAR** — 12 positives >> 1-positive SBD ceiling AND +1.95% median >> −1.0% SBD median ceiling.
- Active 5b cooldowns: **none** — BTC exit yesterday was `exit-ema20-confirm` (not stop-hit); 5b applies only to stop-hits.
- Cluster cap (rule 6a, BTC-cluster): **0/2** used (HYPE not in cluster). 2 slots headroom for BTC/ETH/SOL/TAO/AVAX/SUI/LINK.
- **All Ring 3 kill switches CLEAR.** Routine-01-overnight 2026-07-07T13:07Z: **1 entry, 0 exit, 0 open at wake / 1 open after**; DD widened 3.58% → 3.85% on HYPE unrealized drift; portfolio 1/4 positions.

## Universe (unchanged since 2026-07-01 refresh)

Top 15 by 30d notional per `memory/universe.md` (refreshed at 07-01 overnight; next refresh 2026-08-01):

BTC, ETH, SOL, HYPE, XRP, ADA, NEAR, SUI, TAO, XDG, LTC, AVAX, LINK, ONDO, TRX.

## Pending exit triggers

- **HYPE/USD**: exit-1 (2 consec closes < 20-EMA), exit-2 (price ≤ $70.5499 stop), exit-3 (unrealized ≥ +4R at 1H close = $78.0504+). W22-H ratchet arm at 1H close ≥ $75.0502. Next exit-check wake: routine-02-midday Tue 13:00 PT = 20:00Z (~6h53m out).

Next scheduled wake: routine-02-midday Tue 2026-07-07 13:00 PT = 20:00Z (ON-SCHEDULE M-F cron `0 13 * * 1-5`, ~6h53m out from now). Cash reserve **$2,983.69** (28% of equity — 1 more full-sized 1.5%-risk entry possible with headroom). Rule-7 portfolio-risk headroom **2.500pp / 2.5%**. Cluster 0/2 unchanged, position cap 1/4 (3 slots headroom). Watching for: (a) whether HYPE holds above 20-EMA (currently entry $72.05, EMA20 ~$71.045 at 12Z close, live tick $71.77 = +$0.725 above EMA20) or produces a 2-bar close-below flip; (b) whether regime holds up — the indicators.py→ticker divergence signals a fragile session where the mid-day 07-06 dip skewed the bar-close-basis 24h; if the day continues to drift down, the next indicators.py run may deteriorate quickly; (c) TAO as a secondary rule-8 candidate if HYPE fails and TAO holds tech-PASS (TAO IS in BTC-cluster so cluster gates matter for it — with HYPE not in cluster, TAO could still enter, would take cluster to 1/2).

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | ≈ +2.19% (equity 06-30 est ~$10,415 → $10,643.34 MTM) | ≈ +2.97% ($61,447 → $63,273.7 live) | ≈ −0.78pp | BULL slightly behind 7d |
| 30d | ≈ +6.43% (inception $10k 2026-04-20; $10,643.34 MTM) | ≈ −17.8% est (BTC 30d ago ~$77k → $63.3k live) | ≈ +24.2pp | BULL well ahead |
| 90d | — | — | — | not computable (BULL inception 78 days ago; window first computable ~2026-07-19) |

(BTC 12Z close $63,416.7; live tick 13:09Z $63,273.7. HYPE 12Z close $72.05; live tick 13:09Z $71.77.)
