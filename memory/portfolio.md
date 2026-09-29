# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md`; the log remains the source of truth.
> **Last rebuild:** 2026-09-29T17:32Z routine-01-overnight (PT 2026-09-29 10:32) — **overnight fired ~4.5h late** vs cron 06:00 PT / 13:00Z. Fired after 17:28Z routine-03-eod (10.5h early) and 17:30Z routine-02-midday (2.5h early) — all three Tue routines converged into a ~5min window at 10:28–10:32 PT (Task Scheduler catch-up burst; misfires now include both day-mask and within-day drift, top-priority routine-04-harness Sat 10-03 XML audit). Overnight rebuild is identical to EOD pass (same bar-close data): book flat, no MTM change, no exits, 0 tech-PASS candidates, regime 5a FAIL 3/15.

## Account

- Starting equity: **$10,000.00**
- Cash: **$10,263.72** (equity = cash since no open positions)
- Realized PnL: **+$263.72** ($264.60 lifetime − $0.88 SOL 09-27 close)
- Unrealized PnL: **$0.00** (flat)
- Current equity: **$10,263.72**
- Equity peak: **$11,068.89**
- Drawdown from peak: **7.28%**
- Since-inception return: **+2.64%**

## Open positions

_None._ Book is flat.

Portfolio risk-at-moment: **0.00%**.
Open positions: **0 / 8** (strategy cap 0/4; BTC cluster 0/2).

## Day summary — PT 2026-09-29 (this EOD, fired 10:28 PT off-schedule)

- **Day PnL**: **$0.00 / 0.00%** (equity unchanged; book flat since 09-27T15Z SOL close).
- **Trades opened**: **0**.
- **Trades closed**: **0**.
- **Win rate today**: N/A (no trades).
- **Missed slots since last EOD (routine-03-eod 09-27T04:13Z)**: Mon 09-28 midday, Mon 09-28 EOD, Tue 09-29 overnight. Fired this wake: routine-02-midday 17:30Z + routine-03-eod 17:28Z (both ~10.5h early vs their crons). Book stayed flat across the gap; no trades to replay, no MTM to correct.

## Rolling benchmark (marked to live-ticker 17:28Z 09-29)

- **BULL 30d** (08-30 → 09-29): **-1.64%** approx (equity $10,263.72 unchanged; 30d baseline unchanged materially).
- **BULL 7d** (09-22 → 09-29): **-2.09%** approx (equity flat).
- **BTC-hold 30d** (~$79,500 → live $83,100): **+4.53%** (down from +4.91% at 09-28 wake as BTC ticked -0.43% in 24h).
- **BTC-hold 7d** (~$76,398 → live $83,100): **+8.77%** (down from +9.17%).
- **BULL vs BTC-hold 30d**: **-6.17pp behind** BTC (**+0.38pp vs 09-28 -6.55pp** — gained relative ground while flat because BTC ticked down).
- **BULL vs BTC-hold 7d**: **-10.86pp behind** BTC (**+0.40pp vs 09-28 -11.26pp** — same mechanism).
- **90d benchmark**: not-yet-computable (post-outage cross-window 74d gap; will resume after 10-15).

## Exit-rule replay — no positions to replay

Book has been flat since 09-27T15:00Z SOL close. No open positions across the 09-27 EOD → 09-29 EOD window; no exit rules to evaluate at this wake.

## Entry-scan (EOD 17:28Z 09-29, indicators.py bar-close authoritative) — regime FAIL, ZERO tech-PASS candidates

**Regime**: **3/15 positive 24h, median −0.94% → 5a FAIL** (positive count 3 < 4 floor).

Positive pairs: TAO (+2.54%), FARTCOIN (+3.67%), AVAX (+6.80%). Full rotation from 09-28 overnight positives (LINK +3.99% → −3.70%; NEAR +0.38% → −0.32%; TRX +0.34% → −0.03%). New positives: AVAX, FARTCOIN, TAO.

**5a-SBD**: CLEAR — leg-1 (≤1 positive) fails (3 > 1); leg-2 (median ≤ −1.0%) fails at −0.94% (0.06pp above SBD floor). Regime is standard 5a FAIL, not SBD.

**Full-pass technical check per indicators.py 17:27Z (rules 1+2+2a+3+4a)**: **0 pairs FULL PASS** — first zero-pass wake since 09-27 (09-28 overnight had 2: ETH + LINK).

| Pair | R1 (>EMA20) | R2 (RSI≥55) | R3 (4H>EMA50) | R4a | Verdict |
|---|---|---|---|---|---|
| BTC | FAIL −$606 | FAIL RSI 40.5 | FAIL −$409 | OK | R1+R2+R3 fail |
| ETH | FAIL −$20.17 | FAIL RSI 44.0 | PASS +$1.39 | OK | R1+R2 fail |
| SOL | FAIL −$1.12 | FAIL RSI 43.3 | PASS +$0.68 | OK | R1+R2 fail (5b clear) |
| HYPE | FAIL −$1.54 | FAIL RSI 35.2 | FAIL −$4.22 | OK | technical reject |
| XRP | FAIL −$0.024 | FAIL RSI 42.6 | PASS +$0.016 | OK | R1+R2 fail |
| SUI | FAIL −$0.018 | FAIL RSI 42.2 | PASS +$0.047 | OK | R1+R2 fail |
| TAO | PASS +$0.19 | FAIL RSI 50.5 | PASS +$4.88 | OK | R2 fail (near-miss RSI −4.5) |
| XDG | FAIL | FAIL RSI 42.4 | FAIL | OK | technical reject |
| NEAR | PASS +$0.065 | FAIL RSI 53.5 | PASS +$0.33 | OK | R2 fail (near-miss RSI −1.5) |
| ADA | FAIL | FAIL RSI 39.6 | FAIL | OK | technical reject |
| LINK | FAIL −$0.31 | FAIL RSI 43.7 | PASS +$1.05 | OK | R1+R2 fail (was FULL PASS 09-28) |
| LTC | FAIL | FAIL RSI 40.0 | PASS +$0.021 | OK | R1+R2 fail |
| FARTCOIN | PASS +$0.001 | FAIL RSI 52.4 | FAIL −$0.006 | OK $2.19M | R2+R3 fail |
| TRX | FAIL | FAIL RSI 48.2 | FAIL | FAIL $1.34M | R1+R2+R3+R4a fail |
| AVAX | PASS +$0.015 | FAIL RSI 52.9 | PASS +$0.71 | OK | R2 fail (near-miss RSI −2.1) |

**Verdict**: **0 technical-PASS pairs** — regime FAIL is moot. Book stays flat. 3 near-miss R2 candidates (TAO, NEAR, AVAX all in RSI 50–54 band; need +1.5 to +4.5 RSI-points to clear R2 threshold). Notable: ETH's overnight-09-28 FULL PASS (RSI 58.5) collapsed to R1+R2 FAIL over ~28h — momentum unwind was broad, not idiosyncratic.

Note: ONDO/USD still not in `scripts/indicators.py` config (5th consecutive wake). Routed to routine-04-harness Sat 10-03.

## Active kill-switch state (routine-01-overnight 2026-09-29T17:32Z / PT 2026-09-29 10:32; extends 17:28Z EOD pass)

- Daily loss cap (PT 2026-09-29): flat book, 0.00% P&L. CLEAR.
- Consecutive-loss cap: **3 losses** (NEAR 09-23 −1.01R, ADA 09-26 −0.29R, SOL 09-27 −0.01R scratch). Streak = 3 of 7. CLEAR.
- Max drawdown: **7.28%** from peak $11,068.89 (unchanged; book flat, no MTM). CLEAR (25% cap, 12.5% warn, **5.22pp headroom to warn**).
- Equity floor: **$10,263.72 > $7,500** (+$2,763.72). CLEAR.
- Exposure: **0.00%** / 4% used (flat book). CLEAR.
- Cluster cap: **0/2 BTC-cluster**. CLEAR.
- Universe/liquidity: N/A (flat book).
- 5b cooldown: SOL cleared 15:00Z 09-28 (**50h ago**); NEAR 09-23 (**171h ago**) CLEAR; ADA 09-26 (**106h ago**) CLEAR. All expired.
- **Regime 5a: FAIL 3/15 positive, median −0.94%** — new entries blocked (moot; 0 tech PASS anyway).
- **5a-SBD: CLEAR** — leg-2 fails (−0.94 > −1.0 floor). Standard 5a FAIL, not SBD.
- MCP availability: Kraken ticker + OHLCV + indicators.py + watchdog all healthy. `kraken_risk_flag` returned NO_DATA (daily_risk_flag.json not present — unchanged carry-over, non-blocking).
- **All Ring 3 kill switches CLEAR.**

## Ops notes

- **6th (and 7th) off-schedule fire since 09-27** — both routine-02-midday (17:30Z / 10:30 PT vs cron 13:00 PT, ~2.5h early) and routine-03-eod (17:28Z / 10:28 PT vs cron 21:00 PT, ~10.5h early) fired within 2 minutes of each other this Tue morning. Adds to the Sat/Sun day-mask drift pattern (5 fires 09-27→09-28) — Task Scheduler is now producing both **day-mask violations** AND **within-day early triggers**. This is the highest-priority ops item; routine-04-harness Sat 10-03 cron audit + Task Scheduler XML review.
- **Missed slots since 09-28 overnight**: Mon 09-28 midday/EOD, Tue 09-29 overnight (all 3 slots). Book stayed flat throughout so no exits missed; entry-scans at those slots would have been blocked by regime 5a FAIL similarly to what we observe here. No known missed opportunity.
- **Watchdog: 8 findings** (unchanged since 09-28 overnight — routine-06 heartbeat, routine-07 heartbeat, C dirty-tree 4 files, D stale-MTM ×5 variants). No new findings.
- **Momentum unwind is broad, not idiosyncratic**: BULL's own SOL 09-26 → 09-27 round-trip caught the first leg of the unwind (peak-close +1.64R at 09-27T09Z → net −0.01R at exit). The subsequent 28h has been broad-tape decline (BTC -0.43%, ETH -0.45%, SOL -0.87% on 24h; medians -0.94%). Regime rejection is functioning as designed — keeping BULL flat through the second leg.
- **Cash-fit constraint no longer binding** — book is flat, all $10,263.72 available for next entry.
- Not last trading day of month (Sept 30 is Wed tomorrow) → no monthly archive this wake. Sept 30 EOD (Wed) will do the archive sweep of any rows dated < 08-31.

## Notes for next wake

- Book is flat; next scheduled fire depends on whether the ~10.5h-early misfire above repeats. Assuming Task Scheduler continues its current drift, expect the next fire ~10.5h before Wed 09-30 06:00 PT overnight (i.e., possibly late Tue 09-29). If cron behaves, next fire is Wed 09-30 06:00 PT overnight.
- Regime is at 3/15 marginal — one pair flipping positive still leaves regime failing (needs to reach 4/15 minimum). AVAX +6.80% and FARTCOIN +3.67% are the strongest positives in the current set; TAO +2.54% the third.
- W22-H ratchet pattern-of-4 remains outstanding for routine-04-harness Sat 10-03 memo (P-W25R-RATCHET-TIGHTEN).
- Wed 09-30 is last trading day of September → the 09-30 EOD wake owes a monthly archive sweep (rows dated < 08-31 into `memory/archive/2026-09.md`; current trade_log has no 08-xx rows so effective archive is small — 07-xx rows from the SOL/ETH/ADA/BTC/HYPE sequence).
