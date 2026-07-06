# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-07-06T01:15Z routine-02-midday (PT Sun 2026-07-05 18:15, **OFF-SCHEDULE Sun fire + ~5h15m late** — cron `0 13 * * 1-5` is M-F 13:00 PT, but routine markdown has no day-gate and scheduler fired late Sun evening; PT date label 2026-07-05 per date-labeling guard). **1 trade event this wake — CLOSE ADA/USD via missed-scheduler-replay** of W22-G Exit-1 (two consecutive 1H closes < 20-EMA) that fired at 07-05T10:00Z bar close. Pulled `kraken_multi_ticker` (15 universe pairs) + 60× 1H ADA bars via `kraken_ohlcv`. **Bar-by-bar exit check on ADA/USD since 03Z entry** (using portfolio-recorded seed EMA20 $0.188204 at 07-05T03Z, α=2/21 forward-march): 04Z close $0.190532 vs EMA $0.188426 = +$0.002106 ABOVE; 05Z $0.188916 vs $0.188473 = +$0.000443 ABOVE; 06Z $0.189764 vs $0.188596 = +$0.001168 ABOVE; 07Z $0.192895 vs $0.189005 = +$0.003890 ABOVE (peak close); 08Z $0.19155 vs $0.189247 = +$0.002303 ABOVE; **09Z $0.18764 vs $0.189094 = −$0.001454 BELOW** (1st below-EMA close since entry, at 6h post-open); **10Z $0.186697 vs $0.188866 = −$0.002169 BELOW** (2nd consecutive → **EXIT 1 W22-G TRIGGERED at 10Z bar close**). Subsequent bars informational only (post-exit): 11Z $0.186652 vs $0.188781 = −$0.002129 BELOW; 12Z $0.187617 vs $0.188670 = −$0.001053 BELOW; 13Z $0.188936 vs $0.188696 = +$0.000240 ABOVE; recovery bars 13Z-14Z 15Z-16Z drift back near EMA (13Z $0.188936, 14Z $0.18926, 15Z $0.188966, 16Z $0.189726, 17Z $0.190122, 18Z $0.189666, 19Z $0.188566, 20Z $0.188337, 21Z $0.190326, 22Z $0.19028, 23Z $0.189352, 00Z 07-06 $0.189906, 01Z partial $0.189494) — post-exit range consolidation, would have gyrated between +0.5R and −0.5R, no fresh exit re-fire, and no re-entry consideration in midday. **Stop-hit check since entry**: 22 post-entry bar lows through 07-06T00Z (spanning 07-05 04Z→07-06 00Z), min $0.185118 at 07-05T10:00Z bar low vs stop $0.183522 = $0.001596 / +0.86% headroom → **NOT triggered** (near-miss at exit-firing bar itself). **4R target check** ($0.216642 close basis): highest post-entry close $0.192895 (07-05T07Z, +0.415R close); highest intrabar $0.194841 (07-05T01Z, +0.708R intrabar) — wait that's pre-entry bar. Post-entry peak intrabar = $0.194107 (07-05T21Z bar high, informational post-exit). Pre-exit peak intrabar = $0.192222 (07-05T04Z) → Exit 3 gap $0.024420 close-basis at peak → **NEVER triggered**. **Breakeven ratchet arm level** +2R close ≥ $0.203394: peak close pre-exit $0.192895 = +0.415R close = $0.010499 below arm; peak intrabar pre-exit $0.194841 = +0.709R = $0.008553 below arm → **NEVER armed**. **Exit fill mechanics**: 10Z close $0.186697 × (1 − 0.0005) adverse slippage = fill $0.186604; exit gross 24,624 × $0.186604 = $4,594.94; exit comm 0.26% = $11.95; cash back $4,582.99. Realized PnL vs recorded entry cost $4,693.93 = **−$110.94 / −0.68R net** (gross price move −$87.22 amplified by round-trip $24.12 friction). All-time realized: $873.98 + (−$110.94) = **$763.04**. Cash post-exit: $6,180.09 + $4,582.99 = **$10,763.08** (all cash, flat portfolio). **Ratchet non-arm again**: this is the **4th consecutive intrabar-touched-close-missed-ratchet pattern** (after SOL 06-22 +1.51R close, SOL 06-29 +1.74R close, ETH 07-04 +1.44R close — now ADA 07-05 +0.42R close). ADA peaked at just +0.42R which is nowhere near the +2R arm — this instance is quite different from the prior 3 which all peaked ≥+1.4R just shy of the arm. **This ADA case is NOT a ratchet-arm-miss lesson** (too far from arm to matter); it is a **fast-fade pattern** — entered at $0.190146, peaked +0.42R within 4h, exited −0.68R within 7h. Regime was already narrow at entry (5/15 positive median −0.97%, closest to SBD activation since W25 per prior EOD note). Kraken-ticker snapshot at 01:15Z shows ADA 24h +0.07%, median across 15 universe pairs now around +0.4% (calmer than 03Z's −0.97%), regime softening back into normal range. **Midday routine — NO ENTRY SCAN** per routine spec (position management only; entries reserved for #1 Overnight and #3 EOD). Universe unchanged (15 pairs; next refresh 2026-08-01). Monthly archive: 07-05 is NOT last trading day of July → **no archive** (2026-06 rows still queued for 07-31 EOD sweep).

> **Prior rebuilds:** 2026-07-05T04:10Z routine-03-eod (PT Sat 2026-07-04 21:10 OFF-SCHEDULE Sat, 1 CLOSE ETH missed-scheduler-replay + 1 OPEN ADA rule-8-sole-TECH-PASS; equity peak $11,068.89 unchanged from midday; DD 1.87%; broke 9-wake cash-blockade streak by taking low-notional ADA); 2026-07-04T20:00Z routine-02-midday (PT Sat 13:00 OFF-SCHEDULE, 0/0, ETH held +1.4385R peak-close 21h post-entry, NEW EQUITY PEAK $11,068.89 via ETH MTM +$45.30/+0.41% vs overnight); 2026-07-04T17:00Z routine-01-overnight (PT Sat 10:00 OFF-SCHEDULE, 0/0, ETH held +1.148R 18h post-entry, 6 TECH-PASS all cash-rejected 9th consec incl. first LINK R4a PASS at rank 13, ADA R2a RSI 83.6 climactic reject, DD 0.00% new peak $11,023.59); 2026-07-04T04:10Z routine-03-eod (PT Fri 21:10 ON-SCHEDULE, PT date 2026-07-03, 0/0, ETH held -0.17R 5h post-entry, 8 TECH-PASS all cash-rejected 8th consec, day +0.93%, DD 0.49%); 2026-07-03T23:15Z routine-02-midday (PT Fri 16:15, ~3h15m late, 0/0, ETH held -0.03R 43min post-entry, silent wake); 2026-07-03T23:01Z routine-01-overnight (PT Fri 16:01, ~10h late; 1 CLOSE SOL 4R +$598.56/+3.88R + 1 OPEN ETH rule-8-fallback @ $1,756.9580; equity peak set $10,885.39; 2nd 4R take-profit inception-to-date, 1st post-W22-H ratchet-arm proof-of-mechanism).

## Account

- Starting equity: **$10,000.00**
- Cash: **$10,763.08** (post-exit $10,763.08 all-cash; delta from prior wake $4,582.99 = ADA exit cash back)
- Realized PnL (all-time): **+$763.04** (was $873.98; ADA exit −$110.94 today; running realized ledger below)
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
- Current equity (cash + MTM): **$10,763.08** (all cash)
- Equity peak: **$11,068.89** (unchanged from 07-04T20:00Z midday ETH-MTM peak; peak-day exceeds current equity by $305.81)
- Drawdown from peak: **2.763%** ($305.81 below peak; 9.74pp headroom to 12.5% warn cap)
- Since-inception return: **+7.63%** ($10,763.08 / $10,000 − 1)

## Open positions

*(none — portfolio is flat after ADA exit)*

Portfolio risk-at-moment: **0.000%** (no open positions). Cap 4% → 4.00pp headroom.
Open positions: **0 / 8** (strategy v0.4 max-concurrent 4 → 0/4 used; BTC-cluster 0/2 used).
Breakeven ratchet (W22-H-partial): N/A (no open positions).

## Midday snapshot — 2026-07-05 PT Sun 18:15 (fired 01:15Z 07-06, OFF-SCHEDULE Sun ~5h15m late)

| Metric | Value |
|---|---|
| Wake type | routine-02-midday (bull-02-midday slot, PT date label 2026-07-05, wall-clock UTC 2026-07-06T01:15Z, OFF-SCHEDULE Sun — cron M-F 13:00 PT, no day-gate in markdown, ~5h15m late) |
| Entries this wake | **0** (midday NO ENTRY SCAN per routine spec) |
| Exits this wake | **1 — ADA/USD long CLOSE @ $0.186604 (missed-scheduler-replay of 07-05T10:00Z bar-close W22-G exit)**; realized −$110.94 / −0.68R net |
| Stop-management events | 0 (W22-H ratchet never armed on ADA — peak close +0.42R vs +2R arm; too far from arm to be relevant) |
| Wake-over-wake P&L | **−$98.77 / −0.91%** vs prior EOD $10,861.85 (ADA give-back from +0.42R peak to −0.68R exit within 7h; +0.7R round-trip) |
| Day PnL PT 2026-07-05 (Sun) | **−$98.77 / −0.909%** (single ADA exit −$110.94 partially offset by intraday MTM drift; strict close-basis) |
| Equity (all cash) | **$10,763.08** |
| Equity peak | **$11,068.89 (unchanged; set 07-04T20:00Z midday MTM)** |
| Drawdown from peak | **2.763%** ($305.81 below peak; 9.74pp to 12.5% warn) |
| Loss streak | **1 trading day** (today negative; 07-04 was +0.274% positive, before that 07-03 was +0.93%) |
| Trades today | **0 opened, 1 closed** (ADA missed-scheduler-replay) |
| 7-day BULL vs BTC-hold | BULL ≈ +3.34% (equity 06-28 est ~$10,415 → $10,763.08) vs BTC ≈ +5.43% ($60,437 → $63,718 ticker) = **−2.09pp BULL behind 7d** (rolled from +0.52pp ahead as ADA loss + BTC continued rise) |
| 30-day BULL vs BTC-hold | BULL ≈ +7.63% (inception $10k) vs BTC ≈ −17% est (BTC 30d ago ~$77k → $63.7k) = **+24.6pp BULL well ahead 30d** |
| 90-day | not computable (inception 2026-04-20 = 77 days ago; window first computable ~2026-07-19) |

## Active kill-switch state

- Daily realized + unrealized PT 2026-07-05: **−$98.77 / −0.909%** of equity (vs prior EOD $10,861.85) — CLEAR (well below 5% cap; 4.09pp headroom).
- Consecutive losing trading days: **1** (07-05 negative close-basis; 07-04 positive). CLEAR (cap 7).
- Max drawdown: **2.763%** from peak $11,068.89 (cap 25%, warn 12.5%, **9.74pp headroom to warn**) — CLEAR.
- Equity floor: $10,763.08 > $7,500 floor (+$3,263.08 above floor). CLEAR.
- MCP availability: Kraken OK (`kraken_multi_ticker` + `kraken_ohlcv` returned data cleanly). CLEAR.
- Regime gate (rule 5a): **not re-scored this wake** (midday is position management only; last authoritative read 07-05T04:10Z EOD = 5/15 positive median −0.97%, narrow-miss on SBD; informational ticker snapshot at 01:15Z shows ADA +0.07, BTC +0.20, ETH +0.32, HYPE +1.25, LINK +0.79, NEAR +0.81, ONDO +0.38, SOL +0.54, SUI +0.05, TAO +1.18, XRP +0.07, XDG +0.17, LTC +0.07 positive; AVAX -0.06, TRX -0.08 negative → 13/15 positive on ticker, up substantially from 5/15 on indicators.py close-to-close 21h ago — regime softening back to normal range).
- Regime sub-state (rule 5a-SBD): **CLEAR** (ticker snapshot suggests regime materially improved from 07-05T04:10Z narrow-miss; positions being flat means no defensive exit consideration anyway).
- Active 5b cooldowns: **ADA/USD until 2026-07-06T10:00Z NOT active** (ADA exit was EMA-confirm not stop-hit → **5b does NOT apply** per rule wording "within 24h of a stop-out (exit-stop-hit) on that pair"). **ETH/USD 5b also not active** (07-05T01Z exit was also ema-confirm not stop-hit).
- Cluster cap (rule 6a, BTC-cluster): **0/2** used (no positions). Full headroom.
- **All Ring 3 kill switches CLEAR.** Routine-02-midday 2026-07-06T01:15Z: **1 exit, 0 open at wake / 0 open after** (ADA closed, portfolio now flat); **DD widened 1.87% → 2.76% close-basis** (peak $11,068.89 unchanged, ADA loss booked).

## Universe (unchanged since 2026-07-01 refresh)

Top 15 by 30d notional per `memory/universe.md` (refreshed at 07-01 overnight; next refresh 2026-08-01):

BTC, ETH, SOL, HYPE, XRP, ADA, NEAR, SUI, TAO, XDG, LTC, AVAX, LINK, ONDO, TRX.

## Pending exit triggers

*(none — portfolio is flat)*

Next scheduled wake: routine-01-overnight Mon 2026-07-06 06:00 PT = 07-06T13:00Z (ON-SCHEDULE M-F cron `0 6 * * 1-5`). Cluster 0/2 used; position cap 0/4, 4 slots headroom. Cash $10,763.08 is a full non-blocked reserve — Rule-8 winner at overnight will fit any pair including BTC (would need ~$16-22k for full BTC position, which now depends on stop distance). **First flat-portfolio wake since 2026-07-01T04:00Z overnight** (SOL entered at that wake); prior all-cash duration was ~11h. Flat state permits regime re-scoring at overnight with fresh authoritative indicators.py table.

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | ≈ +3.34% (equity 06-28 est ~$10,415 → today $10,763.08 close-basis) | ≈ +5.43% ($60,437 → $63,718 ticker) | ≈ −2.09pp | BULL behind 7d (rolled negative from +0.52pp ahead at prior EOD; ADA loss + BTC steady rise) |
| 30d | ≈ +7.63% (inception $10k 2026-04-20; close-basis $10,763.08) | ≈ −17% est (BTC 30d ago ~$77k → $63.7k) | ≈ +24.6pp | BULL well ahead |
| 90d | — | — | — | not computable (BULL inception 76 days ago; window first computable ~2026-07-19) |

(BTC ticker $63,718.4.)
