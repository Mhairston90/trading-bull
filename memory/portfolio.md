# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-07-06T17:40Z routine-01-overnight (PT Mon 2026-07-06 10:40, **~4h40m LATE vs 06:00 PT cron `0 6 * * 1-5`**). **1 OPEN this wake — BTC/USD long 0.16899 @ $63,679.4 rule-8 winner (rank 1) from 10 tech-PASS candidates, breaking prior wake's 0-tech-PASS pullback.** Pulled `kraken_multi_ticker` (15 universe pairs) + `scripts/indicators.py` (720-bar 1H+4H authoritative table) + `kraken_spread` for BTC. **Entry scan flip vs prior wake**: prior 10:30Z wake had 0/15 tech-PASS (universe-wide 1H pullback below 20-EMA), this 17:40Z wake has **10/15 tech-PASS** — BTC, ETH, SOL, HYPE, XRP, NEAR, TAO, LTC, AVAX, LINK all cleared R1+R2+R2a+R3+R4a. Rejects: SUI (R2 FAIL RSI 53.0), XDG (R2 FAIL RSI 50.9), ADA (R1 + R2 FAIL, RSI 48.4 recovering post-exit), TRX (R1 + R2 FAIL RSI 46.5), FARTCOIN not-in-universe (indicators.py legacy row) + ONDO missing from indicators.py output (data gap flagged, not blocking). **Regime bar-close 11/15 positive median +1.08% → 5a PASS, SBD CLEAR** (recovery from prior wake's 12/15 bar-close + live-tick 0/15 divergence — divergence resolved to broad recovery). **Rule-8 winner deterministic: BTC rank 1**. Cluster BTC-{BTC,ETH,SOL,TAO,AVAX,SUI,LINK} 0/2 pre-entry → 1/2 post-entry. **Cash-capped sizing**: risk-based size 0.169080 BTC ($10,766.87 pos value) exceeded cash $10,763.08 by $3.79 → capped to 0.16899 BTC ($10,757.35 pos value), actual risk $161.35 = **1.499% equity (under 1.5% cap)**. News scan skipped (informational-only per amended DO 4; 10 candidates lean-mode skip). Sentiment: BTC spread 1.4-3.5 bps (~0.005% of price) — extremely tight liquidity, no thin-tape concern. Watchdog 9 findings (unchanged from prior wake: 1× A routine-06 217h, 1× A routine-07 216h, 1× C dirty-tree 4 files, 6× D variant stale-MTM). No universe refresh (not first-of-month). Portfolio: 1 open (BTC $10,757.35), cash $5.73 residual, equity $10,763.08 (unchanged at wake baseline; MTM instantaneous match).

> **Prior rebuilds:** 2026-07-06T10:30Z routine-01-overnight (PT Mon 03:30 ~2h30m EARLY, 0/0 all-cash flat, 0 tech-PASS all 15 pairs FAIL R1 AND R2 universe-wide 1H pullback, R3 4H trend intact 14/14, regime 5a PASS 12/15 bar-close but live-tick 0/15 SBD divergence informational); 2026-07-06T01:15Z routine-02-midday (PT Sun 18:15 OFF-SCHEDULE ~5h15m late, 1 CLOSE ADA missed-scheduler-replay of 07-05T10Z bar-close W22-G exit, realized −$110.94 / −0.68R, day −0.91%, DD widened 1.87%→2.76%); 2026-07-05T04:10Z routine-03-eod (PT Sat 21:10 OFF-SCHEDULE Sat, 1 CLOSE ETH missed-scheduler-replay + 1 OPEN ADA rule-8-sole-TECH-PASS; equity peak $11,068.89 unchanged from midday; DD 1.87%; broke 9-wake cash-blockade streak by taking low-notional ADA); 2026-07-04T20:00Z routine-02-midday (PT Sat 13:00 OFF-SCHEDULE, 0/0, ETH held +1.4385R peak-close 21h post-entry, NEW EQUITY PEAK $11,068.89 via ETH MTM +$45.30/+0.41% vs overnight); 2026-07-04T17:00Z routine-01-overnight (PT Sat 10:00 OFF-SCHEDULE, 0/0, ETH held +1.148R 18h post-entry, 6 TECH-PASS all cash-rejected 9th consec incl. first LINK R4a PASS at rank 13, ADA R2a RSI 83.6 climactic reject, DD 0.00% new peak $11,023.59).

## Account

- Starting equity: **$10,000.00**
- Cash: **$5.73** (was $10,763.08; deployed $10,757.35 to BTC entry, $5.73 residual)
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
- Unrealized PnL (open positions): **$0.00** (BTC entered at close, MTM = entry)
- Position values: **$10,757.35** (BTC 0.16899 × $63,679.4)
- Current equity (cash + MTM): **$10,763.08** (all-in; $5.73 cash + $10,757.35 BTC pos)
- Equity peak: **$11,068.89** (unchanged from 07-04T20:00Z midday ETH-MTM peak; peak-day exceeds current equity by $305.81)
- Drawdown from peak: **2.763%** ($305.81 below peak; 9.74pp headroom to 12.5% warn cap)
- Since-inception return: **+7.63%** ($10,763.08 / $10,000 − 1)

## Open positions

| Pair | Side | Size | Entry | Stop | Target | Entry timestamp | R risk | Notes |
|---|---|---|---|---|---|---|---|---|
| BTC/USD | long | 0.16899 | $63,679.4 | $62,724.55 | $67,498.80 | 2026-07-06T16:00:00Z | 1.499% ($161.35) | Rule-8 winner (rank 1 of 10 tech-PASS). BTC-cluster slot 1/2. Cash-capped size (risk-based 0.169080 exceeded cash by $3.79). Live-tick $63,687.1 = +$1.30 unrealized. Breakeven ratchet armed at 1H close ≥ $65,589.10 (+2R). |

Portfolio risk-at-moment: **1.499%** ($161.35 / $10,763.08). Cap 4% → **2.501pp headroom** (space for 1 more full 1.5% trade + 1 partial ~1.0% trade).
Open positions: **1 / 8** (strategy v0.4 max-concurrent 4 → 1/4 used; BTC-cluster {BTC,ETH,SOL,TAO,AVAX,SUI,LINK} **1/2 used**).
Breakeven ratchet (W22-H-partial): BTC needs 1H close ≥ $65,589.10 (+2R) to arm; then stop moves from $62,724.55 to $63,679.4 (entry = breakeven).

## Overnight snapshot — 2026-07-06 PT Mon 10:40 (fired 17:40Z 07-06, ~4h40m LATE vs 06:00 PT cron)

| Metric | Value |
|---|---|
| Wake type | routine-01-overnight (bull-01-overnight slot, PT date label 2026-07-06, wall-clock UTC 2026-07-06T17:40Z, ~4h40m LATE vs `0 6 * * 1-5` cron 06:00 PT = 13:00Z) |
| Entries this wake | **1** — BTC/USD long 0.16899 @ $63,679.4 (rule-8 rank-1 winner of 10 tech-PASS) |
| Exits this wake | **0** (no positions at wake start; new BTC not exit-eligible same wake) |
| Stop-management events | 0 |
| Wake-over-wake P&L | **$0.00 / 0.00%** vs prior 10:30Z all-cash flat (entry was at close so instantaneous MTM = entry) |
| Day PnL PT 2026-07-06 (Mon DTD) | **$0.00 / 0.00%** (no realized events; MTM change from BTC entry-to-live-tick +$1.30 = +0.012%) |
| Equity (mix) | **$10,763.08** ($5.73 cash + $10,757.35 BTC MTM) |
| Equity peak | **$11,068.89 (unchanged; set 07-04T20:00Z midday MTM)** |
| Drawdown from peak | **2.763%** ($305.81 below peak; 9.74pp to 12.5% warn) |
| Loss streak | **1 trading day** (07-05 negative; 07-04 positive close-basis) |
| Trades today | **1 opened (BTC 17:40Z wake), 0 closed** |
| 7-day BULL vs BTC-hold | BULL ≈ +3.34% (equity 06-29 est ~$10,415 → $10,763.08) vs BTC ≈ +3.7% ($60,437 → $62,814) = **−0.4pp BULL behind 7d** (BTC ticker steady; BULL flat since prior wake) |
| 30-day BULL vs BTC-hold | BULL ≈ +7.63% (inception $10k) vs BTC ≈ −17.4% est ($77k → $62.8k) = **+25.0pp BULL well ahead 30d** |
| 90-day | not computable (inception 2026-04-20 = 77 days ago; window first computable ~2026-07-19) |

## Active kill-switch state

- Daily realized + unrealized PT 2026-07-06: **$0.00 / 0.00%** of equity — CLEAR (5% loss cap → full 5pp headroom).
- Consecutive losing trading days: **1** (07-05 negative close-basis; 07-04 positive). CLEAR (cap 7).
- Max drawdown: **2.763%** from peak $11,068.89 (cap 25%, warn 12.5%, **9.74pp headroom to warn**) — CLEAR.
- Equity floor: $10,763.08 > $7,500 floor (+$3,263.08 above floor). CLEAR.
- MCP availability: Kraken OK (`kraken_multi_ticker` + `kraken_spread` returned data cleanly; `scripts/indicators.py` fetched 720-bar 1H+4H tables converged). CLEAR.
- Regime gate (rule 5a): **PASS bar-close 11/15 positive, median +1.08%** — recovery from prior wake's 12/15 bar-close but 0/15 live-tick divergence. Full 7-positive cushion above 4/15 floor.
- Regime sub-state (rule 5a-SBD): **CLEAR** — 11 positives >> 1-positive SBD ceiling AND +1.08% median > -1.0% SBD median ceiling.
- Active 5b cooldowns: **none** — both recent exits (ETH 07-05T01Z, ADA 07-05T10Z) were `exit-ema20-confirm` (not `exit-stop-hit`); 5b applies only to stop-hits.
- Cluster cap (rule 6a, BTC-cluster): **1/2** used (BTC/USD active). 1 slot headroom for ETH/SOL/TAO/AVAX/SUI/LINK.
- **All Ring 3 kill switches CLEAR.** Routine-01-overnight 2026-07-06T17:40Z: **1 entry (BTC), 0 exits, 0 open at wake / 1 open after**; DD unchanged 2.76%; portfolio deployed from all-cash to 99.95% invested in BTC.

## Universe (unchanged since 2026-07-01 refresh)

Top 15 by 30d notional per `memory/universe.md` (refreshed at 07-01 overnight; next refresh 2026-08-01):

BTC, ETH, SOL, HYPE, XRP, ADA, NEAR, SUI, TAO, XDG, LTC, AVAX, LINK, ONDO, TRX.

## Pending exit triggers

**BTC/USD** (entered 2026-07-06T16:00Z @ $63,679.4):
- **Exit-1 (W22-G)**: two consecutive 1H closes < 1H 20-EMA. Current EMA20 ~$62,814 (1H close $63,679.4 = +$865 above); requires ≥ 2 hourly closes to fall through EMA20 (moving up as BTC rises).
- **Exit-2 (stop-hit)**: intrabar touch of $62,724.55 (2×ATR below entry). Currently $955 below live tick.
- **Exit-3 (+4R take-profit)**: 1H close ≥ $67,498.80. Currently $3,819 above entry (+6.0% move needed).
- **W22-H breakeven ratchet arm**: 1H close ≥ $65,589.10 (+2R). At arm, stop moves entry-price $63,679.4 (breakeven).

Next scheduled wake: routine-02-midday Mon 2026-07-06 13:00 PT = 07-06T20:00Z (ON-SCHEDULE M-F cron `0 13 * * 1-5`). Midday is position-management-only (no entry scan) — will check BTC exit triggers on 4 additional 1H closes between now and then (18:00Z, 19:00Z, 20:00Z bars). **Next entry-scan opportunity: routine-03-eod Mon 2026-07-06 21:00 PT = 07-07T04:00Z Tue**. Cluster 1/2 used; position cap 1/4, 3 slots headroom; cash reserve $5.73 dust — cannot fund further entries until BTC exit frees capital. Rule-7 portfolio-risk headroom 2.501pp / 4% (would allow another 1.5% trade if cash existed). Watching for: (a) BTC follow-through — does 1H trend continue up into the 4R target zone, or fade back through EMA20?; (b) whether ETH/SOL rally alongside BTC to test the cluster cap (would be blocked by 1/2→2/2 rule 6a at next scan); (c) whether the tech-PASS breadth (10/15 now) holds through 20:00Z midday check.

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | ≈ +3.34% (equity 06-29 est ~$10,415 → today $10,763.08 close-basis) | ≈ +3.7% ($60,437 → $62,814.4 ticker) | ≈ −0.4pp | BULL slightly behind 7d (marginal; BTC steady, BULL flat since ADA exit) |
| 30d | ≈ +7.63% (inception $10k 2026-04-20; close-basis $10,763.08) | ≈ −17.4% est (BTC 30d ago ~$77k → $62.8k) | ≈ +25.0pp | BULL well ahead |
| 90d | — | — | — | not computable (BULL inception 77 days ago; window first computable ~2026-07-19) |

(BTC ticker $63,687.1 live; indicators.py bar-close $63,679.4.)
