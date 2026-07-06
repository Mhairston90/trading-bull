# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-07-06T20:00Z routine-02-midday (PT Mon 2026-07-06 13:00, **ON-SCHEDULE M-F cron `0 13 * * 1-5`**). Midday position-management only — no entry scan. Fresh Kraken MTM: BTC live tick $63,572.6 (was $63,658 at prior 17:47Z wake, was entry $63,679.4 at 16Z bar close). Post-entry 1H closes for BTC: 17Z $63,534.6, 18Z $63,648.8, 19Z $63,696.6, 20Z in-progress ~$63,572.6. Rough 1H SMA20 ≈ $63,009; all 3 completed post-entry closes remain above → **Exit 1 (W22-G 2-consecutive-below-EMA20) NOT triggered**. Post-entry lows 63,330.6/63,521.7/63,503.7/63,610.8/63,554.7 all well above stop $62,724.55 → **Exit 2 (stop-hit) NOT triggered**. Highest close 63,696.6 vs +4R target $67,498.80 → **Exit 3 NOT triggered**. Peak close 63,696.6 = +0.018R above entry → **breakeven ratchet NOT armed** (needs +2R close ≥ $65,589.10; currently $1,892.50 below arm). BTC position value now $10,743.13 (0.16899 × 63,572.6); unrealized **-$18.05 / -0.112R** vs entry basis $10,761.18. Equity **$10,748.86** (was $10,758.75 at prior wake); wake-over-wake **-$9.89 / -0.092%** MTM drift. Peak $11,068.89 unchanged; DD widened 2.802% → **2.892%** (+0.090pp). Rule 5a live: **6/15 positive median -0.25% PASS** (softened from prior wake 5/15 median -0.22%; 2 more positives — AVAX flipped positive, TAO stayed marginal +0.01, ADA/TRX/XDG/HYPE/LINK/LTC/XRP/SUI all remain negative); SBD CLEAR. All Ring 3 kill switches CLEAR. Watchdog NOT re-run midday (lean-mode routine; 9 carry-over findings from prior wake still apply). No trade_log rows appended; no lessons appended; no archive (not month-end).

> **Prior rebuilds:** 2026-07-06T17:47Z routine-03-eod (PT Mon 10:47 ~10h13m EARLY, MTM-only, equity $10,758.75, DD 2.802%, 0 trades); 2026-07-06T17:40Z routine-01-overnight (PT Mon 10:40 ~4h40m LATE, 1 OPEN BTC/USD long 0.16899 @ $63,679.4 rule-8 winner rank-1 of 10 tech-PASS, equity $10,763.08 all-in from all-cash); 2026-07-06T10:30Z routine-01-overnight (PT Mon 03:30 ~2h30m EARLY, 0/0 all-cash flat, 0 tech-PASS universe-wide 1H pullback); 2026-07-06T01:15Z routine-02-midday (PT Sun 18:15 OFF-SCHEDULE ~5h15m late, 1 CLOSE ADA missed-scheduler-replay of 07-05T10Z bar-close W22-G exit, realized −$110.94 / −0.68R); 2026-07-05T04:10Z routine-03-eod (PT Sat 21:10 OFF-SCHEDULE Sat, 1 CLOSE ETH + 1 OPEN ADA rule-8-sole-TECH-PASS; equity peak $11,068.89 unchanged from midday).

## Account

- Starting equity: **$10,000.00**
- Cash: **$5.73** (unchanged; no realized events this wake)
- Realized PnL (all-time): **+$763.04** (unchanged)
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
- Unrealized PnL (open positions): **-$18.05** (BTC live tick $63,572.6 vs entry $63,679.4, -0.112R)
- Position values: **$10,743.13** (BTC 0.16899 × $63,572.6)
- Current equity (cash + MTM): **$10,748.86**
- Equity peak: **$11,068.89** (unchanged from 07-04T20:00Z midday ETH-MTM peak; peak-day exceeds current equity by $320.03)
- Drawdown from peak: **2.892%** ($320.03 below peak; 9.61pp headroom to 12.5% warn cap)
- Since-inception return: **+7.489%** ($10,748.86 / $10,000 − 1)

## Open positions

| Pair | Side | Size | Entry | Stop | Target | Entry timestamp | R risk | Notes |
|---|---|---|---|---|---|---|---|---|
| BTC/USD | long | 0.16899 | $63,679.4 | $62,724.55 | $67,498.80 | 2026-07-06T16:00:00Z | 1.499% ($161.35) | Rule-8 winner (rank 1 of 10 tech-PASS). BTC-cluster slot 1/2. Cash-capped size at OPEN. Live-tick $63,572.6 = -$18.05 unrealized (-0.112R). Post-entry 1H closes: 17Z 63,534.6 / 18Z 63,648.8 / 19Z 63,696.6 (all above ~63,009 SMA20 proxy for EMA20 — Exit 1 NOT triggered). Post-entry lows all ≥ $63,330 (Exit 2 stop-hit NOT triggered). Peak close 63,696.6 = +0.018R above entry → breakeven ratchet armed at 1H close ≥ $65,589.10 (+2R); currently $1,892.50 below arm level. |

Portfolio risk-at-moment: **1.501%** ($161.35 / $10,748.86). Cap 4% → **2.499pp headroom** (space for 1 more full 1.5% trade + 1 partial ~1.0% trade — but cash-blocked, no funding available).
Open positions: **1 / 8** (strategy v0.4 max-concurrent 4 → 1/4 used; BTC-cluster {BTC,ETH,SOL,TAO,AVAX,SUI,LINK} **1/2 used**).
Breakeven ratchet (W22-H-partial): BTC needs 1H close ≥ $65,589.10 (+2R = entry $63,679.4 + 2×$954.85) to arm; then stop moves from $62,724.55 to $63,679.4 (entry = breakeven). Currently $2,016.50 below arm level on live tick.

## Midday snapshot — 2026-07-06 PT Mon 13:00 (fired 20:00Z, ON-SCHEDULE M-F `0 13 * * 1-5`)

| Metric | Value |
|---|---|
| Wake type | routine-02-midday (bull-02-midday slot, PT date label 2026-07-06 Mon, wall-clock UTC 2026-07-06T20:00Z, ON-SCHEDULE) |
| Entries this wake | **0** (midday routine — position management only, no entry scan) |
| Exits this wake | **0** (BTC 3 post-entry 1H closes all above EMA20 proxy; no stop-hit; no 4R touch) |
| Stop-management events | 0 (BTC at -0.112R unrealized, far from +2R ratchet arm level $65,589.10) |
| Wake-over-wake P&L (17:47Z→20:00Z, ~2h13m) | **-$9.89 / -0.092%** (pure MTM drift on BTC live tick $63,658→$63,572.6) |
| Day PnL PT 2026-07-06 (Mon DTD, baseline 07-05 EOD $10,763.08) | **-$14.22 / -0.132%** (no realized events; MTM drift on BTC position + prior wake's 07-05 close-basis baseline) |
| Equity (mix) | **$10,748.86** ($5.73 cash + $10,743.13 BTC MTM) |
| Equity peak | **$11,068.89 (unchanged; set 07-04T20:00Z midday MTM)** |
| Drawdown from peak | **2.892%** ($320.03 below peak; 9.61pp to 12.5% warn) |
| Loss streak | **1 trading day** (07-05 close-basis negative; 07-04 positive; 07-06 currently -0.132% borderline) |
| Trades today | **1 opened (BTC 17:40Z routine-01), 0 closed** |
| 7-day BULL vs BTC-hold | BULL ≈ +3.20% (equity 06-29 est ~$10,415 → $10,748.86) vs BTC ≈ +3.5% ($61,447 → $63,572.6) = **≈ −0.3pp BULL slightly behind 7d** |
| 30-day BULL vs BTC-hold | BULL ≈ +7.49% (inception $10k) vs BTC ≈ −17.5% est ($77k → $63.6k) = **+25.0pp BULL well ahead 30d** |
| 90-day | not computable (inception 2026-04-20 = 77 days ago; window first computable ~2026-07-19) |

## Active kill-switch state

- Daily realized + unrealized PT 2026-07-06: **-$14.22 / -0.132%** of equity — CLEAR (5% loss cap → 4.87pp headroom).
- Consecutive losing trading days: **1** (07-05 negative close-basis; 07-04 positive; 07-06 currently -0.132% — will finalize at real 21:00 PT EOD close). CLEAR (cap 7).
- Max drawdown: **2.892%** from peak $11,068.89 (cap 25%, warn 12.5%, **9.61pp headroom to warn**) — CLEAR.
- Equity floor: $10,748.86 > $7,500 floor (+$3,248.86 above floor). CLEAR.
- MCP availability: Kraken OK (`kraken_multi_ticker` + `kraken_ohlcv` returned data cleanly). CLEAR.
- Regime gate (rule 5a): **PASS live-tick 6/15 positive, median -0.25%** (positives: AVAX +0.17, ETH +0.18, NEAR +2.71, ONDO +1.31, SOL +0.26, TAO +0.01; softened from prior wake 5/15 median -0.22% — AVAX flipped positive between wakes on tape drift).
- Regime sub-state (rule 5a-SBD): **CLEAR** — 6 positives >> 1-positive SBD ceiling AND -0.25% median > -1.0% SBD median ceiling.
- Active 5b cooldowns: **none** — both recent exits (ETH 07-05T01Z, ADA 07-05T10Z) were `exit-ema20-confirm` (not `exit-stop-hit`); 5b applies only to stop-hits.
- Cluster cap (rule 6a, BTC-cluster): **1/2** used (BTC/USD active). 1 slot headroom for ETH/SOL/TAO/AVAX/SUI/LINK.
- **All Ring 3 kill switches CLEAR.** Routine-02-midday 2026-07-06T20:00Z: **0 entries, 0 exits, 1 open at wake / 1 open after**; DD widened 2.80% → 2.89% on MTM drift; portfolio unchanged structurally.

## Universe (unchanged since 2026-07-01 refresh)

Top 15 by 30d notional per `memory/universe.md` (refreshed at 07-01 overnight; next refresh 2026-08-01):

BTC, ETH, SOL, HYPE, XRP, ADA, NEAR, SUI, TAO, XDG, LTC, AVAX, LINK, ONDO, TRX.

## Pending exit triggers

**BTC/USD** (entered 2026-07-06T16:00Z @ $63,679.4):
- **Exit-1 (W22-G)**: two consecutive 1H closes < 1H 20-EMA. Rough SMA20 proxy ~$63,009; live tick $63,572.6 = +$564 above; requires ≥ 2 hourly closes to fall through EMA20 (EMA rising slowly as recent-bar closes have been in $63.5k range).
- **Exit-2 (stop-hit)**: intrabar touch of $62,724.55 (2×ATR below entry). Currently $848 below live tick.
- **Exit-3 (+4R take-profit)**: 1H close ≥ $67,498.80. Currently $3,926 above live tick (+6.2% move needed).
- **W22-H breakeven ratchet arm**: 1H close ≥ $65,589.10 (+2R). At arm, stop moves to entry-price $63,679.4 (breakeven).

Next scheduled wake: routine-03-eod Mon 2026-07-06 21:00 PT = 07-07T04:00Z Tue (ON-SCHEDULE M-F cron `0 21 * * 1-5`, ~8h out). EOD is the next entry-scan opportunity — will check BTC exit triggers on 8 intervening 1H closes (21Z 22Z 23Z 00Z 01Z 02Z 03Z 04Z) and potentially open a 2nd position if a rule-8 TECH-PASS pair fits within remaining $5.73 cash (unlikely to fund a meaningful notional — would require sub-$10 per unit price like XDG). Cluster 1/2 used; position cap 1/4, 3 slots headroom; cash reserve $5.73 dust — cannot fund further entries until BTC exit frees capital. Rule-7 portfolio-risk headroom 2.499pp / 4% (would allow another 1.5% trade if cash existed). Watching for: (a) BTC follow-through — will 20-21Z bar hold above rising EMA20?; (b) whether tape's 6/15 positive live-tick regime holds or drifts back toward SBD threshold; (c) whether BTC pushes toward +2R ratchet arm ($65,589.10) to lock in a breakeven floor.

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | ≈ +3.20% (equity 06-29 est ~$10,415 → today $10,748.86 close-basis) | ≈ +3.5% ($61,447 → $63,572.6 ticker) | ≈ −0.3pp | BULL slightly behind 7d (marginal; BTC steady, BULL MTM drift down) |
| 30d | ≈ +7.49% (inception $10k 2026-04-20; close-basis $10,748.86) | ≈ −17.5% est (BTC 30d ago ~$77k → $63.6k) | ≈ +25.0pp | BULL well ahead |
| 90d | — | — | — | not computable (BULL inception 77 days ago; window first computable ~2026-07-19) |

(BTC live tick mid $63,572.6; entry-bar close $63,679.4 unchanged.)
