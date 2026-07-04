# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-07-04T04:10Z routine-03-eod (PT Fri 2026-07-03 21:10, cron slot `bull-03-eod` ON-SCHEDULE M-F cron `0 21 * * 1-5`, PT date label 2026-07-03 per date-labeling guard). **0 trade events this wake.** ETH position 5h10m old at EOD check; 5 post-entry 1H bars closed (23Z/00Z/01Z/02Z/03Z closes: $1,757.04, $1,757.07, $1,746.67, $1,747.31, $1,752.28). Kraken `kraken_ohlcv` + `scripts/indicators.py` full 15-pair authoritative table at 04:10Z. Watchdog 8 findings (carry-over class: 1× A routine-07 155h stale, 1× C dirty-tree 3 uncommitted files, 6× D stale-MTM variants); Telegram auto-alert sent by watchdog. **Post-close exit check on ETH/USD (last closed 1H bar 07-04T03:00Z close $1,752.28)**: (i) **1H 20-EMA per indicators.py = $1,740.30** (R1 PASS +$11.98), last close $1,752.28 = $11.98 above EMA; second-most-recent close $1,747.31 (07-04T02:00Z) = $7.01 above EMA → **Exit 1 two-bar confirmation NOT triggered** (neither of last two closes below EMA); (ii) **stop-hit check** since 07-03T23:00Z entry: bar lows = $1,753.47, $1,754.42, $1,744.36, $1,742.93, $1,745.69 (all ≥ $1,742.93) vs stop $1,728.5520 → min headroom $14.38, **Exit 2 NOT triggered**; (iii) **4R target check** ($1,870.5820): highest post-entry 1H close $1,757.07 (bar 07-04T00:00Z), highest intrabar $1,762.00 same bar → **Exit 3 NOT triggered**, gap $113.51 on close basis; (iv) **breakeven ratchet** arm level +2R = $1,813.7700 close: peak close $1,757.07 = -0.165R (well below arm) → NOT armed. **Entry scan (W19-E analyst-role split)** per routine spec — **Technical (authoritative `scripts/indicators.py` at 04:10:19Z, 720 4H bars/pair)**: regime 5a **PASS 14/15 positive median +2.49%** (only FARTCOIN −3.35% negative), SBD **CLEAR** (14 positives ≫ 1 ceiling; median +2.49% ≫ −1.0% floor); TECH-PASS pairs (R1+R2+R2a+R3+R4a all PASS) = **BTC** (R1+$348.2, R2 RSI 63.7, R3 +$1,691, R4a $113.74M), **ETH** (R1+$11.98, R2 RSI 63.1, R3 +$104.3, R4a $38.37M — SKIP: rule 5 already open), **SOL** (R1+$0.7924, R2 RSI 64.4, R3 +$6.537, R4a $21.66M), **HYPE** (R1+$1.454, R2 RSI 68.3, R3 +$5.621, R4a $14.02M), **XRP** (R1+$0.01413, R2 RSI 67.0, R3 +$0.05694, R4a $29.32M), **SUI** (R1+$0.001424, R2 RSI 55.7, R3 +$0.04054, R4a $9.42M), **XDG** (R1+$0.0006376, R2 RSI 62.3, R3 +$0.002296, R4a $7.13M), **ADA** (R1+$0.002043, R2 RSI 61.8, R3 +$0.02022, R4a $14.51M), **LTC** (R1+$0.1443, R2 RSI 56.2, R3 +$1.358, R4a $3.12M). REJECT reasons: TAO R1+R2 FAIL (RSI 49.1) + R4a FAIL $1.97M, NEAR R1+R2 FAIL (RSI 50.8), LINK R4a FAIL $1.59M, FARTCOIN R1+R2 FAIL (RSI 40.4) + R4a FAIL $1.58M, TRX R2a FAIL RSI 82.0>80 cap + R4a FAIL $1.19M, AVAX R4a FAIL $1.96M. **News (informational)**: SKIPPED for all 8 non-open TECH-PASS candidates (04Z Sat early UTC morning, low news cycle) → default NEUTRAL tags. **Sentiment (informational)**: not queried per-candidate (rule-8 winner deterministic on 30d rank). **Decision — Rule 8**: TECH-PASS winner order by 30d notional rank (universe.md) = **BTC (1)** > **SOL (3)** > **HYPE (4)** > **XRP (5)** > **ADA (6)** > **SUI (8)** > **XDG (10)** > **LTC (11)**. Sizing per strategy v0.4 (risk = 1.5% × equity $10,832.24 = $162.48; size = risk / 2×ATR14): **BTC** stop-dist $620.48, size 0.2619, notional $16,386.34 + comm $42.60 = **$16,428.94 > cash $759.96 → REJECT cash-insufficient**; **SOL** stop-dist $1.3052, size 124.49, notional $10,289.05 + $26.75 = **$10,315.80 → REJECT cash-insufficient**; **HYPE** stop-dist $1.6623, size 97.75, notional $6,969.31 + $18.12 = **$6,987.43 → REJECT cash-insufficient**; **XRP** stop-dist $0.019019, size 8,543, notional $9,711.51 + $25.25 = **$9,736.76 → REJECT cash-insufficient**; **ADA** stop-dist $0.0050451, size 32,206, notional $5,698.96 + $14.82 = **$5,713.77 → REJECT cash-insufficient**; **SUI** stop-dist $0.01501, size 10,825, notional $8,222.69 + $21.38 = **$8,244.07 → REJECT cash-insufficient** (also cluster 2/2 with ETH but cash rejects first); **XDG** stop-dist $0.0012524, size 129,738, notional $10,027.21 + $26.07 = **$10,053.28 → REJECT cash-insufficient**; **LTC** stop-dist $0.72086, size 225.4, notional $9,989.84 + $25.97 = **$10,015.81 → REJECT cash-insufficient**. **All 8 rule-8 fallback candidates cash-rejected. 0 entries this wake.** This is the **8th cash-binding wake W24-W27** (06-27 EOD 3×, 06-30 midday 1×, 07-01 EOD 7×, 07-02 overnight 10×, 07-02 EOD 7×, 07-03 overnight 10× incl. ETH rule-8-fallback win, 07-03 EOD 8×) — pattern extremely well established, P-W26-CASHFIT proposal remains pending user `[Y/N]`; today's 8-candidate REJECT is further data point but no new lesson (existing 2026-06-17 W26 score-8 captures it).

> **Prior rebuilds:** 2026-07-03T23:15Z routine-02-midday (PT Fri 16:15, ~3h15m late vs nominal 20:00Z; same-wake window as overnight 23:01Z 14 min prior; 0/0, ETH held -0.03R unrealized 43min post-entry, stop 4.92 headroom, silent wake); 2026-07-03T23:01Z routine-01-overnight (PT Fri 16:01, ~10h late; 1 CLOSE SOL 4R +$598.56/+3.88R + 1 OPEN ETH rule-8-fallback @ $1,756.9580; equity peak set $10,885.39 clearing 06-13 TAO peak by +$9.54; 2nd 4R take-profit inception-to-date, 1st post-W22-H ratchet-arm proof-of-mechanism); 2026-07-03T04:11Z routine-03-eod (Thu 21:00 PT ON-SCHEDULE M-F, PT date 2026-07-02, 0/0, SOL held +2.92R unrealized, 9 TECH-PASS all cash-rejected 7th consec, DD 1.32%); 2026-07-02T20:00Z routine-02-midday (Thu 13:00 PT ON-SCHEDULE M-F, 0/0, SOL held +2.99R unrealized, DD 1.20%); 2026-07-02T13:07Z routine-01-overnight (Thu 06:00 PT ON-SCHEDULE M-F, 0/0, W22-H breakeven ratchet ARMED on SOL at 07-02T09:00Z close $79.40 = +2.30R, stop $73.5918→$75.3538, 10 TECH-PASS all cash-rejected, DD 0.77%, +4R intrabar-touch/close-miss 1st instance); 2026-07-02T04:11Z routine-03-eod (Wed 21:00 PT ON-SCHEDULE, 0/0, SOL held +1.87R unrealized, 7 TECH-PASS all cash-rejected, DD 2.93%); 2026-07-01T20:00Z routine-02-midday (Wed 13:00 PT ON-SCHEDULE M-F, 0/0, SOL held +0.87R unrealized, DD 4.34%).

## Account

- Starting equity: **$10,000.00**
- Cash: **$759.96** (unchanged from overnight post-SOL exit +$7,214.42 net, post-ETH entry −$10,125.43)
- Realized PnL (all-time): **+$885.36** (unchanged; last realized was SOL 4R exit at overnight wake)
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
- Unrealized PnL (open positions): **−$26.89** (ETH 5.7481 × ($1,752.28 − $1,756.9580) = −$26.89 gross MTM; overnight entry commission $26.26 already booked at open)
- Position values: **$10,072.28** (ETH 5.7481 × $1,752.28 last-closed 1H 07-04T03:00Z = $10,072.28 MTM)
- Current equity (cash + MTM): **$10,832.24** (= $759.96 cash + $10,072.28 ETH MTM; wake-over-wake PnL = −$21.75 from midday $10,853.99 driven by ETH close drift $1,756.07 midday-tick → $1,752.28 EOD-close)
- Equity peak: **$10,885.39** (unchanged; set 2026-07-03T20:00Z post-SOL-exit all-cash mark)
- Drawdown from peak: **0.488%** ($53.15 below peak; widened from midday's 0.29% by $21.75)
- Since-inception return: **+8.32%** ($10,832.24 / $10,000 − 1)

## Open positions

| Pair | Side | Size | Entry | Stop | Target | Notional | Risk-at-moment | Cluster | Entered |
|------|------|------|-------|------|--------|----------|----------------|---------|---------|
| ETH/USD | long | 5.7481 | $1,756.9580 | $1,728.5520 | $1,870.5820 | $10,072.28 | ~$163.28 / 1.51% | BTC-cluster (1/2) | 2026-07-03T23:00Z |

Portfolio risk-at-moment: **~1.51%** of equity (single ETH position; unchanged from midday within rounding). Cap 4% → 2.49pp headroom.
Open positions: **1 / 8** (strategy v0.4 max-concurrent 4 → 1/4 used; BTC-cluster 1/2 used).
Breakeven ratchet (W22-H-partial): NOT armed on ETH (unrealized R = −0.165R, far from +2R threshold). Would arm on any 1H close ≥ $1,756.9580 + 2 × $28.406 = $1,813.7700.

## EOD snapshot — 2026-07-03 PT Fri 21:10 PT (fired 04:10Z 07-04, ON-SCHEDULE M-F cron `0 21 * * 1-5`)

| Metric | Value |
|---|---|
| Wake type | routine-03-eod (bull-03-eod slot, PT date 2026-07-03, wall-clock UTC 2026-07-04T04:10Z, ON-SCHEDULE) |
| Entries this wake | 0 (all 8 rule-8 fallback candidates cash-rejected; 8th consecutive cash-binding wake) |
| Exits this wake | 0 (ETH: stop $14.38 headroom, EMA $11.98 close-to-EMA headroom on last close, 4R target $113.51 above) |
| Stop-management events | 0 (ratchet arm level $1,813.77 is $61.49 above current close; unrealized R = −0.165R) |
| Day-to-date P&L (PT 2026-07-03) | **+$99.55 / +0.93%** vs prior EOD $10,732.69 (SOL 4R realization booked at 20:00Z bar dominates; ETH MTM slippage to $1,752.28 close pared some of the gain from midday's +1.13%) |
| Wake-over-wake P&L | **−$21.75 / −0.20%** vs midday $10,853.99 (ETH mark from $1,756.07 → $1,752.28 × 5.7481 = −$21.75 MTM drift over 5h) |
| Equity (cash + MTM) | **$10,832.24** ($759.96 cash + $10,072.28 ETH MTM) |
| Equity peak | **$10,885.39** (unchanged) |
| Drawdown from peak | **0.488%** (widened from midday 0.29%, still 12.01pp to 12.5% warn) |
| Loss streak | 0 trading days (today +0.93%, positive) |
| Trades today | 1 opened (ETH), 1 closed (SOL 4R) — unchanged from overnight |

## Active kill-switch state

- Daily realized + unrealized PT 2026-07-03: **+$99.55 / +0.93%** of equity — CLEAR (positive; 5.00% loss cap → 5.93pp headroom to loss cap).
- Consecutive losing trading days: **0** (cap 7, full 7-day headroom). CLEAR.
- Max drawdown: **0.488%** from peak $10,885.39 (cap 25%, warn 12.5%, **12.01pp to warn**) — CLEAR.
- Equity floor: $10,832.24 > $7,500 floor — CLEAR.
- MCP availability: Kraken OK (`kraken_multi_ticker` + `kraken_ohlcv` returned data this wake, `scripts/indicators.py` produced full 15-pair table). CLEAR.
- Regime gate (rule 5a): **PASS** 14/15 positive median +2.49% per `scripts/indicators.py` (authoritative). Multi-ticker source shows divergence again (~8/15 positive median lower) — P-W27-REGIME-SOURCE proposal remains queued for routine-04 W27 Sat 2026-07-04.
- Regime sub-state (rule 5a-SBD): **CLEAR** (14 positives ≫ 1; median +2.49% ≫ −1.0%).
- Active 5b cooldowns: **none** (SOL exit was 4R take-profit, not stop-hit; last stop-out 2026-06-27T19:00Z SOL cooldown lapsed 2026-06-28T19:00Z).
- Cluster cap (rule 6a, BTC-cluster): **1/2** used (ETH). Full headroom left = 1 more slot.
- **All Ring 3 kill switches CLEAR.** Routine-03-eod 2026-07-04T04:10Z: **0 entries, 0 exits, 1 open at wake / 1 open after** (unchanged).

## Universe (unchanged since 2026-07-01 refresh)

Top 15 by 30d notional per `memory/universe.md` (refreshed at 07-01 overnight; next refresh 2026-08-01):

BTC, ETH, SOL, HYPE, XRP, ADA, NEAR, SUI, TAO, XDG, LTC, AVAX, LINK, ONDO, TRX.

## Pending exit triggers

**ETH/USD long — active exits monitored at each 1H close:**
- Exit 1 (W22-G): two consecutive 1H closes < 20-EMA ($1,740.30 per indicators.py). Current 1H close $1,752.28 is $11.98 above; trigger requires 2 consecutive closes < ~$1,740.
- Exit 1-SBD (only if regime flips to SBD): two consecutive 1H closes < 9-EMA. Currently inactive (regime PASS 14/15 at EOD).
- Exit 2 (stop-hit): **initial 2×ATR stop $1,728.5520**. Post-open lowest low $1,742.93 (07-04T02:00Z bar). Headroom from current close $1,752.28 = $23.73.
- Exit 3 (take-profit): 4R = $1,870.5820. Distance from current close $118.30 (+6.75% notional).
- Breakeven ratchet arm level: +2R close ≥ $1,813.7700 (currently $61.49 below).

Next scheduled wake: routine-01-overnight Sat 2026-07-04 06:00 PT = 07-04T13:00Z (**OFF-SCHEDULE Saturday fire** — cron M-F but routine markdown has no day-gate → executes; noted in prior weekend fires). Cluster 1/2 used; position cap 1/4, 3 more slots. Gated by regime + per-pair TECH-PASS + cash-fit (cash $759.96 very tight; all low-notional pairs still exceed under 1.5%-risk sizing).

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | ≈ +4.02% (equity 06-26 EOD $10,413.87 → today $10,832.24 MTM) | ≈ +3.57% est (BTC 06-26 ~$60,449 → today $62,574.9 close-basis) | ≈ +0.45pp | BULL ahead 7d |
| 30d | ≈ +8.32% (inception $10k 2026-04-20; MTM $10,832.24) | ≈ −19% est (BTC 30d ago ~$77k → today $62.6k) | ≈ +27.3pp | BULL well ahead |
| 90d | — | — | — | not computable (BULL inception 2026-04-20 = 74 days ago; window first computable ~2026-07-19) |

(BTC last closed 1H $62,574.9 via `scripts/indicators.py`; multi-ticker last tick $62,604.7, 24h +0.11%.)
