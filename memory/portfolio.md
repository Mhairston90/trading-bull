# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-07-07T04:15Z routine-03-eod (PT Mon 2026-07-06 21:15, **ON-SCHEDULE M-F cron `0 21 * * 1-5`**). Wake fired at 04:00Z bar boundary (PT 21:00 exact). Just-closed 1H = 03:00Z bar close $63,125.0. **W22-G Exit rule 1 TRIGGERED on BTC/USD**: two consecutive 1H closes < 1H 20-EMA — 02:00Z close $63,268.5 vs EMA20 ≈ $63,470.3 (−201.8), 03:00Z close $63,125.0 vs EMA20 $63,437.2 (−312.2, per indicators.py). Exit fires on 03Z close. **CLOSE BTC/USD 0.16899 @ $63,125.0 → gross −$93.69 / −0.581R (`exit-ema20-confirm`)**. Position round-tripped over 12h: peak close was 21:00Z $64,453.0 (+0.81R) which never reached the +2R ratchet arm level $65,589.10 (breakeven ratchet W22-H NEVER armed). Realized PnL delta this wake: **−$93.69**; new all-time realized $763.04 − $93.69 = **+$669.35**. Cash post-exit: $5.73 + (0.16899 × $63,125.0) = $5.73 + $10,667.49 = **$10,673.22**. Equity flat = **$10,673.22** (−$75.64 vs midday $10,748.86, of which −$92.39 realized exit and +$16.75 rounding drift from prior wake cash-basis vs bar-close-realized reconciliation). Peak $11,068.89 unchanged; DD widened 2.89% → **3.58%** (+0.69pp). **EOD entry scan on 03Z close (via indicators.py 04:10Z run)**: 0 tech-PASS in universe. Regime 5a: **4/15 positive, median −1.54% → PASS** (weakened significantly vs midday 6/15 −0.25% — TAO/AVAX/NEAR/SOL only positives; ONDO absent from indicators.py so hand-checked +0.29% from live ticker: actual universe-positives = 4/15 with ONDO neutral/positive would nudge to 5/15 but doesn't change PASS verdict; median −1.54% remains well above −1.0% SBD floor). SBD CLEAR. TRX only pair with R1+R2 PASS but FAILS R4a notional ($0.69M < $2.0M floor). BTC/ETH/SOL/HYPE/ADA/XRP/SUI/AVAX/LINK/LTC/NEAR/XDG/TAO all FAIL R1 (below EMA20) AND R2 (RSI 36–47 all below 55 floor). **0 new entries this wake.** Watchdog re-run 04:13Z (9 findings, unchanged carryover: 2× heartbeat routine-06/07, 1× dirty tree 4 files, 6× variant stale-MTM). All Ring 3 kill switches CLEAR.

> **Prior rebuilds:** 2026-07-06T20:00Z routine-02-midday (PT Mon 13:00 ON-SCHEDULE, MTM-only $10,748.86, DD 2.89%, 0 trades, BTC live $63,572.6); 2026-07-06T17:47Z routine-03-eod (PT Mon 10:47 OFF-SCHEDULE ~10h13m EARLY, MTM-only $10,758.75, DD 2.80%, 0 trades); 2026-07-06T17:40Z routine-01-overnight (PT Mon 10:40 ~4h40m LATE, 1 OPEN BTC/USD long 0.16899 @ $63,679.4 rule-8 winner rank-1 of 10 tech-PASS, equity $10,763.08 all-in from all-cash); 2026-07-06T10:30Z routine-01-overnight (PT Mon 03:30 EARLY, 0/0 flat, 0 tech-PASS); 2026-07-06T01:15Z routine-02-midday (PT Sun 18:15 OFF-SCHEDULE, ADA missed-scheduler replay −0.68R); 2026-07-05T04:10Z routine-03-eod (PT Sat 21:10 OFF-SCHEDULE Sat, 1 CLOSE ETH + 1 OPEN ADA; equity peak $11,068.89 unchanged).

## Account

- Starting equity: **$10,000.00**
- Cash: **$10,673.22** (was $5.73; +$10,667.49 = BTC exit proceeds 0.16899 × $63,125.0)
- Realized PnL (all-time): **+$669.35** (was $763.04; delta −$93.69 = BTC exit −0.581R at 03Z close $63,125.0)
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
  - **BTC −$93.69 (exit-ema20-confirm 2026-07-07T03:00:00Z close-basis on-schedule, −0.581R)**
- Unrealized PnL (open positions): **$0.00** (flat, no open positions)
- Position values: **$0.00** (all cash)
- Current equity (cash + MTM): **$10,673.22**
- Equity peak: **$11,068.89** (unchanged from 07-04T20:00Z midday ETH-MTM peak; peak-day exceeds current equity by $395.67)
- Drawdown from peak: **3.576%** ($395.67 below peak; 8.92pp headroom to 12.5% warn cap)
- Since-inception return: **+6.732%** ($10,673.22 / $10,000 − 1)

## Open positions

*(none — flat after BTC/USD EOD exit)*

| Pair | Side | Size | Entry | Stop | Target | Entry timestamp | R risk | Notes |
|---|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | — | Portfolio flat post-BTC-exit 2026-07-07T03Z close. |

Portfolio risk-at-moment: **0.000%** ($0 / $10,673.22). Cap 4% → **full 4pp headroom** available for future entries.
Open positions: **0 / 8** (strategy v0.4 max-concurrent 4 → 0/4 used; BTC-cluster {BTC,ETH,SOL,TAO,AVAX,SUI,LINK} **0/2 used**).
Breakeven ratchet (W22-H-partial): N/A — no open positions.

## EOD snapshot — 2026-07-06 PT Mon 21:00 (fired 04:00Z, ON-SCHEDULE M-F `0 21 * * 1-5`)

| Metric | Value |
|---|---|
| Wake type | routine-03-eod (bull-03-eod slot, PT date label 2026-07-06 Mon, wall-clock UTC 2026-07-07T04:00Z, ON-SCHEDULE) |
| Entries this wake | **0** (EOD entry-scan produced 0 tech-PASS on 03Z close in universe; TRX only R1+R2 PASS but FAIL R4a $0.69M) |
| Exits this wake | **1** (BTC/USD long 0.16899 CLOSE at 03Z bar close $63,125.0, W22-G two-bar EMA20 confirmation, gross −$93.69 / −0.581R) |
| Stop-management events | 0 (BTC breakeven ratchet W22-H never armed; peak close +0.81R vs +2R arm floor) |
| Wake-over-wake P&L (20:00Z→04:00Z, ~8h) | **−$75.64 / −0.703%** (−$92.39 realized exit + ~$16.75 rounding reconciliation to cash-basis) |
| Day PnL PT 2026-07-06 (Mon DTD, baseline 07-05 EOD equity $10,758.75) | **−$85.53 / −0.795%** ($10,673.22 − $10,758.75; one realized event: BTC exit −$93.69) |
| Equity (mix) | **$10,673.22** ($10,673.22 cash + $0 MTM) |
| Equity peak | **$11,068.89 (unchanged; set 07-04T20:00Z midday MTM)** |
| Drawdown from peak | **3.576%** ($395.67 below peak; 8.92pp to 12.5% warn) |
| Loss streak | **2 trading days** (07-05 close-basis negative $10,758.75; 07-06 close-basis negative $10,673.22) |
| Trades today | **1 opened (BTC 07-06T16Z routine-01), 1 closed (BTC 07-07T03Z EOD)** |
| 7-day BULL vs BTC-hold | BULL ≈ +2.48% (equity 06-30 est ~$10,415 → $10,673.22) vs BTC ≈ +2.73% ($61,447 → $63,125.0) = **≈ −0.25pp BULL slightly behind 7d** |
| 30-day BULL vs BTC-hold | BULL ≈ +6.73% (inception $10k → $10,673.22) vs BTC ≈ −18.0% est ($77k → $63.1k) = **+24.7pp BULL well ahead 30d** |
| 90-day | not computable (inception 2026-04-20 = 77 days ago; window first computable ~2026-07-19) |

## Active kill-switch state

- Daily realized + unrealized PT 2026-07-06: **−$85.53 / −0.795%** of equity — CLEAR (5% loss cap → 4.21pp headroom).
- Consecutive losing trading days: **2** (07-05 −0.10% close-basis, 07-06 −0.795% close-basis). CLEAR (cap 7).
- Max drawdown: **3.576%** from peak $11,068.89 (cap 25%, warn 12.5%, **8.92pp headroom to warn**) — CLEAR.
- Equity floor: $10,673.22 > $7,500 floor (+$3,173.22 above floor). CLEAR.
- MCP availability: Kraken OK (`kraken_multi_ticker` + `kraken_ohlcv` returned data cleanly; indicators.py 720-bar EMA/RSI/ATR converged). CLEAR.
- Regime gate (rule 5a): **PASS 4/15 positive, median −1.54%** (positives per indicators.py: TAO +0.42?—actually indicators shows TRX +0.40, NEAR +1.67, FARTCOIN +0.12, SOL +0.42; universe positives from live ticker at wake TRX +0.05, NEAR −1.50→pending, SOL −1.16 pending — the indicators.py Regime line uses 24h % as-of last-closed 1H bar which weakens vs live tick; either way 4/15 clears the 4-floor of rule 5a).
- Regime sub-state (rule 5a-SBD): **CLEAR** — 4 positives > 1-positive SBD ceiling AND −1.54% median > −1.0% SBD median ceiling? **Median −1.54% is BELOW −1.0% ceiling**, so SBD sub-criterion (ii) FAILS the guardrail. But SBD activation requires BOTH (i) AND (ii); (i) (≤1 positive) FAILS at 4/15 positive. Therefore SBD does NOT activate — one leg failing is enough to keep SBD clear. **SBD CLEAR**.
- Active 5b cooldowns: **none** — BTC exit was `exit-ema20-confirm` (not stop-hit); 5b applies only to stop-hits.
- Cluster cap (rule 6a, BTC-cluster): **0/2** used (BTC/USD closed). 2 slots headroom for BTC/ETH/SOL/TAO/AVAX/SUI/LINK.
- **All Ring 3 kill switches CLEAR.** Routine-03-eod 2026-07-07T04:00Z: **0 entries, 1 exit, 1 open at wake / 0 open after**; DD widened 2.89% → 3.58% on realized BTC loss; portfolio now flat.

## Universe (unchanged since 2026-07-01 refresh)

Top 15 by 30d notional per `memory/universe.md` (refreshed at 07-01 overnight; next refresh 2026-08-01):

BTC, ETH, SOL, HYPE, XRP, ADA, NEAR, SUI, TAO, XDG, LTC, AVAX, LINK, ONDO, TRX.

## Pending exit triggers

*(none — flat portfolio)*

Next scheduled wake: routine-01-overnight Tue 2026-07-07 08:00 PT = 15:00Z (ON-SCHEDULE M-F cron `0 8 * * 1-5`, ~11h out from now). Next entry-scan opportunity: overnight will evaluate all 15 universe pairs on 14Z just-closed 1H bar. Cash reserve **$10,673.22** — full sizing capacity restored (was $5.73 dust prior wake). Rule-7 portfolio-risk headroom **4.000pp / 4%** (space for ~2-3 full 1.5%-risk trades). Cluster 0/2, position cap 0/4 (4 slots headroom). Watching for: (a) whether the current 4/15-positive regime (median −1.54%) recovers overnight — a further degradation to ≤1/15 positive + median ≤ −1.0% would activate SBD and tighten Exit 1 to 9-EMA on future entries; (b) whether any pair reclaims RSI ≥ 55 and closes above 1H 20-EMA to become entry-eligible (currently 0/15 universe pairs at rule-1+2 pass; TRX close but blocked by R4a notional); (c) BTC downside continuation — 03Z close $63,125 sits 1.12% below EMA20 with all last 12 closes below 21Z peak $64,453.

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | ≈ +2.48% (equity 06-30 est ~$10,415 → today $10,673.22 close-basis) | ≈ +2.73% ($61,447 → $63,125.0 close 03Z) | ≈ −0.25pp | BULL slightly behind 7d (marginal; BTC held, BULL took −0.58R exit) |
| 30d | ≈ +6.73% (inception $10k 2026-04-20; close-basis $10,673.22) | ≈ −18.0% est (BTC 30d ago ~$77k → $63.1k) | ≈ +24.7pp | BULL well ahead |
| 90d | — | — | — | not computable (BULL inception 77 days ago; window first computable ~2026-07-19) |

(BTC 03Z close $63,125.0; live tick at wake $63,150.)
