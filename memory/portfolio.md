# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-07-05T04:10Z routine-03-eod (PT Sat 2026-07-04 21:10, **OFF-SCHEDULE Sat fire** — cron `0 21 * * 1-5` is M-F but routine markdown has no day-gate; PT date label 2026-07-04 per date-labeling guard). **2 trade events this wake — 1 CLOSE (ETH exit-ema20-confirm missed-scheduler-replay) + 1 OPEN (ADA entry-rule-v0.4-momentum).** ETH position 26h old at time of exit trigger (opened 07-03T23:00Z, exited at 07-05T01:00Z bar-close by W22-G two-bar-below-EMA20 rule); the fire happened between routine-02-midday (20:00Z) and routine-03-eod wakes, so tagged missed-scheduler-replay. Kraken `kraken_multi_ticker` (16 pairs incl. ETH last $1,762.48 24h -0.91%; ADA last $0.190459 24h -0.81% via ticker but +7.46% per indicators.py close-to-close; regime deteriorated vs midday) + `kraken_ohlcv` (30× ETH 1H bars) + `scripts/indicators.py` full 15-pair authoritative table at 04:10Z. Watchdog 8 findings — 1× A routine-07 stale 179h (carry-over past 30h threshold), 1× C dirty-tree (4 uncommitted files carry-over from prior sessions), 6× D stale-MTM variants 179h (all carry-over); Telegram alert auto-sent by watchdog. **Post-close exit check on ETH/USD (bar-by-bar since midday 07-04T20:00Z)**: (i) **1H 20-EMA per indicators.py = $1,770.12** (arithmetic forward-march from midday's $1,769.27@19Z ≈ $1,770.38, converges within $0.26); bar-by-bar closes vs EMA — 20Z close $1,785.56 vs EMA $1,770.82 = +$14.74 above; 21Z $1,787.86 vs $1,772.44 = +$15.42; 22Z $1,782.88 vs $1,773.44 = +$9.44; 23Z $1,778.72 vs $1,773.94 = +$4.78; 07-05T00Z close **$1,770.50 vs EMA $1,773.61 = −$3.11 BELOW** (1st below-EMA close since entry, at 25h post-open); 01Z close **$1,765.01 vs EMA $1,772.79 = −$7.78 BELOW** (2nd consecutive → **EXIT 1 W22-G TRIGGERED at 01Z bar close**); 02Z $1,759.14 vs $1,771.49 = −$12.35 (post-exit, informational); 03Z $1,759.84 vs $1,770.12 (indicators.py) = −$10.28 (post-exit, informational); (ii) **stop-hit check** since entry: 28 post-entry bar lows (min $1,742.93 at 07-04T02Z unchanged; between-wake lows 07-05T00Z $1,768.64, 01Z $1,759.92 both above stop $1,728.5520 by $31.37+; 02Z low $1,755.98 post-exit informational) → **NOT triggered pre-exit**; (iii) **4R target check** ($1,870.5820 close basis): peak close $1,797.82 (07-04T17Z bar, +1.4385R close; unchanged from midday); peak intrabar $1,805.52 (07-04T17Z high, +1.7096R intrabar; unchanged) → **Exit 3 NOT triggered** at any point in life of trade, gap remained $72.76 close-basis at peak; (iv) **breakeven ratchet** arm level +2R close ≥ $1,813.7700: peak close +1.4385R at 07-04T17Z = $15.95 below arm level; peak intrabar +1.7096R at same bar = $8.25 below arm intrabar → **NEVER armed** during the trade's life (ratchet did not protect this position). **Exit fill mechanics**: 01Z close $1,765.01 × (1 − 0.0005) adverse slippage = fill $1,764.128; exit gross 5.7481 × $1,764.128 = $10,140.43; exit comm 0.26% = $26.37; cash back $10,114.06. Realized PnL vs entry ($10,099.185 notional + $26.258 entry comm = $10,125.443): **−$11.38 / −0.07R net** (gross price move +$41.21 flipped by round-trip $52.63 friction). All-time realized: $885.36 + (−$11.38) = **$873.98**. **Entry scan (W19-E) at 03Z bar close** (post-exit; cash now $10,874.02): **Regime** (indicators.py 04:10Z): **PASS 5/15 positive (BTC +0.22, ETH +0.43, XRP +0.03, ADA +7.46, TRX +0.13)** median −0.97% — right at 5a floor (≥4/15); **SBD CLEAR** (5 positives > 1 ceiling; median −0.97% > −1.0% floor by 0.03pp — narrow miss). **TECH-PASS pairs**: only **ADA/USD** (R1 +$0.001942 on EMA20 $0.188204, R2 RSI 59.2, R2a OK, R3 +$0.027 on 4H EMA50 $0.16315 = +16.5% above, R4a $16.25M ≥ $2M, 720 4H bars ≥ 200 for converged EMA); every other pair fails R1+R2 (RSI 33-49 across most, close below 20-EMA). ADA is isolated strength (+7.46% 24h vs median −0.97%) on the same-day BTC/ETH give-back tape. **Rule-8 winner: ADA (only TECH-PASS candidate; no tiebreak needed)**. **News**: SKIPPED for ADA (04:10Z Sat US Independence-Day weekend low-news window; W19-E default NEUTRAL tag; news does not veto in v0.2). **Sentiment**: not queried (does not veto). **Sizing** at post-exit equity $10,874.02 × 0.015 = $163.11 risk / $0.0066241 (2×ATR14) = **24,624 ADA**; notional 24,624 × $0.190146 = $4,681.76 (well under cash $10,874.02 → cash-fit YES, breaks the 9-consecutive-wake cash-blockade streak by taking a low-notional pair instead of BTC/ETH); entry comm $12.17; total entry cost $4,693.93; cash after entry $10,874.02 − $4,693.93 = **$6,180.09**. **Cluster (rule 6a)**: ADA is NOT in BTC-cluster {BTC,ETH,SOL,TAO,AVAX,SUI,LINK} → cluster 0/2 (down from 1/2 pre-ETH-exit; freed by exit). **Position cap (rule 6)**: 1/4 used (3 slots headroom). **Portfolio risk (rule 7)**: 1.500% (2.500pp headroom to 4% cap). **OPEN ADA/USD long 24,624 @ $0.190146 stop $0.183522 target $0.216642** — first non-cluster (non-BTC/non-ETH/non-SOL/non-TAO) entry since 2026-05-21 HYPE; first ADA/USD entry inception-to-date (ADA has been rank 6 in universe since 07-01 refresh, present in earlier refreshes; never fired an entry before because RSI floor + regime alignment rarely coincided). MTM at close-basis: cash $6,180.09 + ADA 24,624 × $0.190146 = **$10,861.85** (equity closed-bar basis, dropped by $12.17 entry comm from post-exit $10,874.02). At ticker-real-time (ADA $0.190459): $6,180.09 + $4,689.79 = $10,869.88. **Day PnL PT 2026-07-04** (Sat) vs prior EOD PT 2026-07-03 $10,832.24: **close-basis +$29.61 / +0.274%** (ticker-basis +$37.64 / +0.348%). **Wake-over-wake vs midday $11,068.89: −$207.04 / −1.87% close-basis** (ETH give-back from peak MTM). **DD from peak $11,068.89: 1.871% close-basis** (up from 0.000% at midday but still 10.63pp under 12.5% warn). **Loss streak: 0** (day positive). **All Ring 3 kill switches CLEAR.** Ratchet-arm-never-fired + Exit-1-EMA20-2-bar-caught-trend-break = **3rd instance of intrabar-touched-close-missed ratchet pattern** (after SOL 06-22 +1.51R close, SOL 06-29 +1.74R close, now ETH 07-04 +1.44R close). Triggers 06-29 lesson's "3rd instance → route to routine-04 memo" escalation path — 1 new lesson added this wake. **Monthly archive**: PT 2026-07-04 (Sat) is NOT last trading day of July (last = Fri 2026-07-31) → **no archive** (2026-06 rows queued for 2026-07-31 EOD sweep).

> **Prior rebuilds:** 2026-07-04T20:00Z routine-02-midday (PT Sat 13:00 OFF-SCHEDULE Sat, 0/0, ETH held +1.4385R peak-close unrealized 21h post-entry, stop $14 headroom EMA $22 headroom, arm-level $16 above peak close, NEW EQUITY PEAK $11,068.89 via ETH MTM +$45.30/+0.41% vs overnight); 2026-07-04T17:00Z routine-01-overnight (PT Sat 10:00 OFF-SCHEDULE Sat, 0/0, ETH held +1.148R peak-close unrealized 18h post-entry, 6 TECH-PASS all cash-rejected 9th consec incl. first LINK R4a PASS at rank 13, ADA R2a RSI 83.6 climactic reject, DD 0.00% new peak $11,023.59); 2026-07-04T04:10Z routine-03-eod (PT Fri 21:10 ON-SCHEDULE M-F, PT date 2026-07-03, 0/0, ETH held -0.17R unrealized 5h post-entry, 8 TECH-PASS all cash-rejected 8th consec, +0.93% day from SOL 4R morning realization, DD 0.49%); 2026-07-03T23:15Z routine-02-midday (PT Fri 16:15, ~3h15m late; 0/0, ETH held -0.03R unrealized 43min post-entry, silent wake); 2026-07-03T23:01Z routine-01-overnight (PT Fri 16:01, ~10h late; 1 CLOSE SOL 4R +$598.56/+3.88R + 1 OPEN ETH rule-8-fallback @ $1,756.9580; equity peak set $10,885.39; 2nd 4R take-profit inception-to-date, 1st post-W22-H ratchet-arm proof-of-mechanism); 2026-07-03T04:11Z routine-03-eod (Thu 21:00 PT ON-SCHEDULE M-F, PT date 2026-07-02, 0/0, SOL held +2.92R unrealized, 9 TECH-PASS all cash-rejected 7th consec, DD 1.32%).

## Account

- Starting equity: **$10,000.00**
- Cash: **$6,180.09** (post-exit $10,874.02, post-entry $6,180.09; delta from prior wake $759.96 = +$5,420.13 net cash change from ETH exit ($10,114.06 cash back) − ADA entry ($4,693.93 out))
- Realized PnL (all-time): **+$873.98** (was $885.36; ETH exit −$11.38 today; running realized ledger below)
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
- Unrealized PnL (open positions): **$0.00 gross at fill (24,624 × ($0.190146 − $0.190146) = $0)**; at ticker-last $0.190459: +$7.71 gross MTM
- Position values: **$4,681.76 close-basis** (ADA 24,624 × $0.190146; $4,689.47 at ticker last $0.190459)
- Current equity (cash + MTM): **$10,861.85 close-basis** (= $6,180.09 cash + $4,681.76 ADA MTM at close); at ticker-real-time: **$10,869.56** (= $6,180.09 + $4,689.47)
- Equity peak: **$11,068.89** (unchanged from midday 07-04T20:00Z; peak-day close-basis exceeds today's EOD close by $207.04)
- Drawdown from peak: **1.871% close-basis** ($207.04 below peak; 10.63pp headroom to 12.5% warn cap)
- Since-inception return: **+8.62% close-basis** ($10,861.85 / $10,000 − 1)

## Open positions

| Pair | Side | Size | Entry | Stop | Target | Notional | Risk-at-moment | Cluster | Entered |
|------|------|------|-------|------|--------|----------|----------------|---------|---------|
| ADA/USD | long | 24624 | $0.190146 | $0.183522 | $0.216642 | $4,681.76 | ~$163.11 / 1.500% | non-cluster | 2026-07-05T03:00Z |

Portfolio risk-at-moment: **~1.500%** of equity (single ADA position). Cap 4% → 2.500pp headroom.
Open positions: **1 / 8** (strategy v0.4 max-concurrent 4 → 1/4 used; BTC-cluster 0/2 used; ADA is non-cluster).
Breakeven ratchet (W22-H-partial): NOT armed on ADA (fresh entry; needs 1H close ≥ +2R = close ≥ $0.216642 to arm; currently at entry).
**Peak-defense level (informational)**: to preserve $11,068.89 equity peak on future MTM marks, ADA would need to rise to close ≥ (($11,068.89 − $6,180.09) / 24,624) = $0.198526 (+4.4% from entry).

## EOD snapshot — 2026-07-04 PT Sat 21:10 (fired 04:10Z 07-05, OFF-SCHEDULE Sat)

| Metric | Value |
|---|---|
| Wake type | routine-03-eod (bull-03-eod slot, PT date label 2026-07-04, wall-clock UTC 2026-07-05T04:10Z, OFF-SCHEDULE Sat — cron M-F, no day-gate in markdown) |
| Entries this wake | **1 — ADA/USD long 24,624 @ $0.190146** (entry-rule-v0.4-momentum, sole TECH-PASS candidate; rule-8 winner by exclusion; breaks 9-wake cash-blockade streak by taking a low-notional pair) |
| Exits this wake | **1 — ETH/USD long CLOSE @ $1,764.128 (missed-scheduler-replay of 07-05T01:00Z bar-close W22-G exit)**; realized −$11.38 / −0.07R net |
| Stop-management events | 0 (W22-H ratchet never armed on ETH — peak close +1.4385R vs +2R arm; ADA fresh entry, ratchet arm level +2R close $0.216642 = target) |
| Wake-over-wake P&L | **−$207.04 / −1.87% close-basis** vs midday $11,068.89 (ETH give-back from MTM peak; net-of-exit cash was $10,874.02 pre-entry) |
| Day PnL PT 2026-07-04 | **+$29.61 / +0.274% close-basis** vs prior EOD $10,832.24 (ETH round-tripped through the wake giving back the +2.19% MTM gain, but ADA fresh entry net-of-comm kept day positive) |
| Equity (cash + MTM close-basis) | **$10,861.85** ($6,180.09 cash + $4,681.76 ADA MTM at entry close) |
| Equity peak | **$11,068.89 (unchanged; set 07-04T20:00Z midday MTM)** |
| Drawdown from peak | **1.871% close-basis** ($207.04 below peak; 10.63pp to 12.5% warn) |
| Loss streak | **0 trading days** (today positive; ETH −$11.38 realized was offset by ADA entry — day PT +$29.61 net; strict "trading day" definition uses realized+unrealized so +0.274% clear-positive) |
| Trades today | **1 opened (ADA), 1 closed (ETH)** — first 2-event wake since 07-03T23:00Z overnight (SOL close + ETH open) |
| 7-day BULL vs BTC-hold | BULL ≈ +4.30% (equity 06-27 ~$10,415 → $10,861.85) vs BTC ≈ +3.78% ($60,437 → $62,721.4 via ticker) = **+0.52pp BULL ahead 7d** (narrowed from midday +2.26pp as BTC rebounded modestly while ETH gave back MTM) |
| 30-day BULL vs BTC-hold | BULL ≈ +8.62% (inception $10k) vs BTC ≈ −18.5% est = **+27.1pp BULL well ahead 30d** |
| 90-day | not computable (inception 2026-04-20 = 76 days ago; window first computable ~2026-07-19) |

## Active kill-switch state

- Daily realized + unrealized PT 2026-07-04: **+$29.61 / +0.274%** of equity (vs prior EOD $10,832.24) — CLEAR (positive; 5.00% loss cap → 5.27pp headroom).
- Consecutive losing trading days: **0** (positive close-basis today). CLEAR (cap 7).
- Max drawdown: **1.871%** from peak $11,068.89 (cap 25%, warn 12.5%, **10.63pp headroom to warn**) — CLEAR.
- Equity floor: $10,861.85 > $7,500 floor (+$3,361.85 above floor). CLEAR.
- MCP availability: Kraken OK (`kraken_multi_ticker` + `kraken_ohlcv` returned data; `scripts/indicators.py` executed on 720 4H bars). CLEAR.
- Regime gate (rule 5a): **PASS 5/15 positive median −0.97%** at 04:10Z — right at 5a floor (≥4/15). Narrow-miss on SBD (SBD needs ≤1 AND ≤−1.0%; regime is 5 positives median −0.97%, so 0.03pp above the SBD median floor and 4 pairs above the SBD count ceiling). CLEAR but weakening.
- Regime sub-state (rule 5a-SBD): **CLEAR** (5 positives > 1 ceiling; median −0.97% > −1.0% floor by 0.03pp — narrow miss, closest to SBD activation since W25).
- Active 5b cooldowns: **ETH/USD until 2026-07-06T01:00Z** (ETH exit 07-05T01:00Z was EMA-confirm exit not stop-hit → **5b does NOT apply** per rule wording "within 24h of a stop-out (exit-stop-hit) on that pair"; ETH re-entry hypothetically OK immediately, though practically ETH won't pass R1+R2 for a while).
- Cluster cap (rule 6a, BTC-cluster): **0/2** used (ETH exited; ADA is non-cluster). Full headroom left = 2 slots.
- **All Ring 3 kill switches CLEAR.** Routine-03-eod 2026-07-05T04:10Z: **1 entry, 1 exit, 1 open at wake / 1 open after** (ETH→ADA rotation); **DD widened 0.000% → 1.871% close-basis** (peak $11,068.89 unchanged, ETH MTM gave back to exit).

## Universe (unchanged since 2026-07-01 refresh)

Top 15 by 30d notional per `memory/universe.md` (refreshed at 07-01 overnight; next refresh 2026-08-01):

BTC, ETH, SOL, HYPE, XRP, ADA, NEAR, SUI, TAO, XDG, LTC, AVAX, LINK, ONDO, TRX.

## Pending exit triggers

**ADA/USD long — active exits monitored at each 1H close:**
- Exit 1 (W22-G): two consecutive 1H closes < 20-EMA. Current 20-EMA at last closed bar (03Z) = $0.188204; current close $0.190146 is $0.001942 above. Trigger requires 2 consecutive closes < ~$0.188.
- Exit 1-SBD (only if regime flips to SBD): two consecutive 1H closes < 9-EMA. Currently inactive (regime PASS 5/15; SBD narrow-miss at −0.97% median could flip to SBD if median falls another 0.03pp).
- Exit 2 (stop-hit): **initial 2×ATR stop $0.183522**. Post-open no bars yet (entered at 03Z close).
- Exit 3 (take-profit): 4R = $0.216642. Distance from entry $0.026496 (+13.9% notional).
- Breakeven ratchet arm level: +2R close ≥ $0.203394 (currently $0.013248 above entry, +7.0% notional).

Next scheduled wake: routine-01-overnight Sun 2026-07-05 06:00 PT = 07-05T13:00Z. Cluster 0/2 used; position cap 1/4, 3 more slots. Cash $6,180.09 unblocks many low-to-mid-notional pairs (SOL/HYPE/XRP/SUI/XDG/LTC/ADA-already-open would all fit under 1.5%-risk sizing at current volatilities).

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | ≈ +4.30% (equity 06-27 EOD ~$10,415 → today $10,861.85 close-basis) | ≈ +3.78% ($60,437 → $62,721.4 ticker) | ≈ +0.52pp | BULL ahead 7d (narrowed from midday +2.26pp) |
| 30d | ≈ +8.62% (inception $10k 2026-04-20; close-basis $10,861.85) | ≈ −18.5% est (BTC 30d ago ~$77k → today ~$62.7k) | ≈ +27.1pp | BULL well ahead |
| 90d | — | — | — | not computable (BULL inception 75 days ago; window first computable ~2026-07-19) |

(BTC last closed 1H = $62,710.1 per indicators.py; ticker $62,721.4.)
