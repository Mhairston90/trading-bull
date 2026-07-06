# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-07-06T17:47Z routine-03-eod (PT Mon 2026-07-06 10:47, **OFF-SCHEDULE ~10h13m EARLY vs 21:00 PT cron `0 21 * * 1-5`**; fired ~7 min after routine-01-overnight 17:40Z). Same 16-17Z just-closed 1H candle. No new open or close events (BTC entered at 16Z bar-close is same-bar as this check — exits not eligible; cash $5.73 residual blocks any new entry). MTM-only refresh: BTC live tick bid/ask mid ~$63,658 (was entry $63,679.4) → BTC pos value $10,753.02 (was $10,757.35), unrealized **-$4.33 / -0.040%**. Equity **$10,758.75** (was $10,763.08 at wake). Peak $11,068.89 unchanged; DD widened 2.763% → **2.802%** (+0.039pp on the -$4.33 tick). Rule 5a live: **5/15 positive median -0.22% PASS**; SBD CLEAR. **6 pairs flipped positive→negative live-tick vs 17:40Z bar-close (HYPE, XRP, TAO, LTC, AVAX, LINK)** — likely instrument (live-tick 24h roll vs bar-close snap) rather than 7-minute real rotation. All Ring 3 kill switches CLEAR. Watchdog 9 findings unchanged from prior wake (Telegram sent 17:48:03Z). No trade_log rows appended; no lessons appended; no archive (not month-end).

> **Prior rebuilds:** 2026-07-06T17:40Z routine-01-overnight (PT Mon 10:40 ~4h40m LATE vs 06:00 PT cron, 1 OPEN BTC/USD long 0.16899 @ $63,679.4 rule-8 winner rank-1 of 10 tech-PASS, equity $10,763.08 all-in from all-cash); 2026-07-06T10:30Z routine-01-overnight (PT Mon 03:30 ~2h30m EARLY, 0/0 all-cash flat, 0 tech-PASS universe-wide 1H pullback, regime bar-close 12/15 PASS but live-tick 0/15 SBD divergence informational); 2026-07-06T01:15Z routine-02-midday (PT Sun 18:15 OFF-SCHEDULE ~5h15m late, 1 CLOSE ADA missed-scheduler-replay of 07-05T10Z bar-close W22-G exit, realized −$110.94 / −0.68R, day −0.91%, DD widened 1.87%→2.76%); 2026-07-05T04:10Z routine-03-eod (PT Sat 21:10 OFF-SCHEDULE Sat, 1 CLOSE ETH missed-scheduler-replay + 1 OPEN ADA rule-8-sole-TECH-PASS; equity peak $11,068.89 unchanged from midday); 2026-07-04T20:00Z routine-02-midday (PT Sat 13:00 OFF-SCHEDULE, 0/0, ETH held +1.4385R peak-close 21h post-entry, NEW EQUITY PEAK $11,068.89 via ETH MTM +$45.30/+0.41% vs overnight).

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
- Unrealized PnL (open positions): **-$4.33** (BTC live tick $63,658 vs entry $63,679.4)
- Position values: **$10,753.02** (BTC 0.16899 × $63,658)
- Current equity (cash + MTM): **$10,758.75**
- Equity peak: **$11,068.89** (unchanged from 07-04T20:00Z midday ETH-MTM peak; peak-day exceeds current equity by $310.14)
- Drawdown from peak: **2.802%** ($310.14 below peak; 9.70pp headroom to 12.5% warn cap)
- Since-inception return: **+7.588%** ($10,758.75 / $10,000 − 1)

## Open positions

| Pair | Side | Size | Entry | Stop | Target | Entry timestamp | R risk | Notes |
|---|---|---|---|---|---|---|---|---|
| BTC/USD | long | 0.16899 | $63,679.4 | $62,724.55 | $67,498.80 | 2026-07-06T16:00:00Z | 1.499% ($161.35) | Rule-8 winner (rank 1 of 10 tech-PASS). BTC-cluster slot 1/2. Cash-capped size at OPEN. Live-tick $63,658 = -$4.33 unrealized (~-0.027R). Breakeven ratchet armed at 1H close ≥ $65,589.10 (+2R). First post-entry 1H bar close is 17-18Z at 18:00Z (~13 min post-EOD-wake). |

Portfolio risk-at-moment: **1.500%** ($161.35 / $10,758.75). Cap 4% → **2.500pp headroom** (space for 1 more full 1.5% trade + 1 partial ~1.0% trade — but cash-blocked, no funding available).
Open positions: **1 / 8** (strategy v0.4 max-concurrent 4 → 1/4 used; BTC-cluster {BTC,ETH,SOL,TAO,AVAX,SUI,LINK} **1/2 used**).
Breakeven ratchet (W22-H-partial): BTC needs 1H close ≥ $65,589.10 (+2R = entry $63,679.4 + 2×$954.85) to arm; then stop moves from $62,724.55 to $63,679.4 (entry = breakeven). Currently $1,931.10 below arm level.

## EOD snapshot — 2026-07-06 PT Mon 10:47 (fired 17:47Z, ~10h13m EARLY vs 21:00 PT cron; **off-schedule EARLY**, ~7 min after routine-01-overnight 17:40Z)

| Metric | Value |
|---|---|
| Wake type | routine-03-eod (bull-03-eod slot, PT date label 2026-07-06 Mon, wall-clock UTC 2026-07-06T17:47Z, ~10h13m EARLY vs `0 21 * * 1-5` cron 21:00 PT = 07-07T04:00Z) |
| Entries this wake | **0** (cash $5.73 dust; BTC already opened at prior 17:40Z wake same-bar close) |
| Exits this wake | **0** (BTC entered at 16Z bar close — same bar as this check; exits not eligible until 17-18Z bar closes at 18:00Z) |
| Stop-management events | 0 (BTC at -$4.33 unrealized, far from +2R ratchet arm level $65,589.10) |
| Wake-over-wake P&L (17:40Z→17:47Z, ~7 min) | **-$4.33 / -0.040%** (pure MTM drift on live BTC tick) |
| Day PnL PT 2026-07-06 (Mon DTD) | **-$4.33 / -0.040%** (no realized events; only MTM drift on the freshly-opened BTC position) |
| Equity (mix) | **$10,758.75** ($5.73 cash + $10,753.02 BTC MTM) |
| Equity peak | **$11,068.89 (unchanged; set 07-04T20:00Z midday MTM)** |
| Drawdown from peak | **2.802%** ($310.14 below peak; 9.70pp to 12.5% warn) |
| Loss streak | **1 trading day** (07-05 close-basis negative; 07-04 positive; 07-06 currently -$4.33 borderline) |
| Trades today | **1 opened (BTC 17:40Z routine-01), 0 closed** |
| 7-day BULL vs BTC-hold | BULL ≈ +3.30% (equity 06-29 est ~$10,415 → $10,758.75) vs BTC ≈ +3.7% ($60,437 → $62,660 ticker) = **−0.4pp BULL behind 7d** (BTC roughly flat since 17:40Z; BULL small MTM drift down) |
| 30-day BULL vs BTC-hold | BULL ≈ +7.59% (inception $10k) vs BTC ≈ −17.4% est ($77k → $62.7k) = **+25.0pp BULL well ahead 30d** |
| 90-day | not computable (inception 2026-04-20 = 77 days ago; window first computable ~2026-07-19) |

## Active kill-switch state

- Daily realized + unrealized PT 2026-07-06: **-$4.33 / -0.040%** of equity — CLEAR (5% loss cap → 4.96pp headroom).
- Consecutive losing trading days: **1** (07-05 negative close-basis; 07-04 positive; 07-06 currently -0.040% — will finalize at real 21:00 PT close). CLEAR (cap 7).
- Max drawdown: **2.802%** from peak $11,068.89 (cap 25%, warn 12.5%, **9.70pp headroom to warn**) — CLEAR.
- Equity floor: $10,758.75 > $7,500 floor (+$3,258.75 above floor). CLEAR.
- MCP availability: Kraken OK (`kraken_multi_ticker` + `kraken_spread` returned data cleanly). CLEAR.
- Regime gate (rule 5a): **PASS live-tick 5/15 positive, median -0.22%** — softened from prior wake bar-close 11/15 / +1.08% on live-tick 24h roll; 1-positive cushion above 4/15 floor.
- Regime sub-state (rule 5a-SBD): **CLEAR** — 5 positives >> 1-positive SBD ceiling AND -0.22% median > -1.0% SBD median ceiling.
- Active 5b cooldowns: **none** — both recent exits (ETH 07-05T01Z, ADA 07-05T10Z) were `exit-ema20-confirm` (not `exit-stop-hit`); 5b applies only to stop-hits.
- Cluster cap (rule 6a, BTC-cluster): **1/2** used (BTC/USD active). 1 slot headroom for ETH/SOL/TAO/AVAX/SUI/LINK.
- **All Ring 3 kill switches CLEAR.** Routine-03-eod 2026-07-06T17:47Z (off-schedule EARLY): **0 entries, 0 exits, 1 open at wake / 1 open after**; DD widened 2.76% → 2.80% on MTM drift; portfolio unchanged structurally.

## Universe (unchanged since 2026-07-01 refresh)

Top 15 by 30d notional per `memory/universe.md` (refreshed at 07-01 overnight; next refresh 2026-08-01):

BTC, ETH, SOL, HYPE, XRP, ADA, NEAR, SUI, TAO, XDG, LTC, AVAX, LINK, ONDO, TRX.

## Pending exit triggers

**BTC/USD** (entered 2026-07-06T16:00Z @ $63,679.4):
- **Exit-1 (W22-G)**: two consecutive 1H closes < 1H 20-EMA. Current EMA20 ~$62,814 (live tick $63,658 = +$844 above); requires ≥ 2 hourly closes to fall through EMA20 (moving up as BTC trades in-range).
- **Exit-2 (stop-hit)**: intrabar touch of $62,724.55 (2×ATR below entry). Currently $934 below live tick.
- **Exit-3 (+4R take-profit)**: 1H close ≥ $67,498.80. Currently $3,841 above live tick (+6.0% move needed).
- **W22-H breakeven ratchet arm**: 1H close ≥ $65,589.10 (+2R). At arm, stop moves entry-price $63,679.4 (breakeven).

Next scheduled wake: routine-02-midday Mon 2026-07-06 13:00 PT = 07-06T20:00Z (ON-SCHEDULE M-F cron `0 13 * * 1-5`, ~2h13m out). Midday is position-management-only — will check BTC exit triggers on 3 intervening 1H closes (18:00Z, 19:00Z, 20:00Z bars). **Next entry-scan opportunity: routine-03-eod Mon 2026-07-06 21:00 PT = 07-07T04:00Z Tue** (the CORRECT scheduled EOD; this wake was ~10h early). Cluster 1/2 used; position cap 1/4, 3 slots headroom; cash reserve $5.73 dust — cannot fund further entries until BTC exit frees capital. Rule-7 portfolio-risk headroom 2.500pp / 4% (would allow another 1.5% trade if cash existed). Watching for: (a) BTC follow-through — does 17-18Z bar close hold above $62,814 EMA20?; (b) whether regime live-tick softening (5/15 positive here vs 11/15 bar-close 7 min prior) reflects true rotation or just live-tick-vs-bar-close instrument noise; (c) whether ETH (up 24h) or SOL (near-flat 24h) test the cluster cap slot.

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | ≈ +3.30% (equity 06-29 est ~$10,415 → today $10,758.75 close-basis) | ≈ +3.7% ($60,437 → $62,660 ticker) | ≈ −0.4pp | BULL slightly behind 7d (marginal; BTC steady, BULL small MTM drift down since 17:40Z) |
| 30d | ≈ +7.59% (inception $10k 2026-04-20; close-basis $10,758.75) | ≈ −17.4% est (BTC 30d ago ~$77k → $62.7k) | ≈ +25.0pp | BULL well ahead |
| 90d | — | — | — | not computable (BULL inception 77 days ago; window first computable ~2026-07-19) |

(BTC live tick mid $63,658; entry-bar close $63,679.4 unchanged.)
