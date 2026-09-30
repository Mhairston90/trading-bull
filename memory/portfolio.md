# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md`; the log remains the source of truth.
> **Last rebuild:** 2026-09-30T04:12Z routine-03-eod (PT 2026-09-29 21:12) — **ON-SCHEDULE authoritative EOD pass** (12-min drift vs cron `0 21 * * 1-5`). First on-schedule fire since 09-27. Supersedes the 17:28Z 09-29 off-schedule early EOD pass. Book flat, no MTM change from prior; regime read has RECOVERED to 5a PASS 12/15 (+0.37% median) — dramatic 9-pair swing in the 7h between the two 09-29 EOD passes. Still 0 tech-PASS candidates (regime PASS moot).

## Account

- Starting equity: **$10,000.00**
- Cash: **$10,263.72** (equity = cash since no open positions)
- Realized PnL: **+$263.72** ($264.60 lifetime − $0.88 SOL 09-27 close)
- Unrealized PnL: **$0.00** (flat)
- Current equity: **$10,263.72**
- Equity peak: **$11,068.89**
- Drawdown from peak: **7.27%**
- Since-inception return: **+2.64%**

## Open positions

_None._ Book is flat.

Portfolio risk-at-moment: **0.00%**.
Open positions: **0 / 8** (strategy cap 0/4; BTC cluster 0/2).

## Day summary — PT 2026-09-29 (on-schedule authoritative EOD, superseding 17:28Z off-schedule pass)

- **Day PnL**: **$0.00 / 0.00%** (equity unchanged; book flat since 09-27T15Z SOL close).
- **Trades opened**: **0**.
- **Trades closed**: **0**.
- **Win rate today**: N/A (no trades).
- **Missed slots since last on-schedule EOD (09-27T04:13Z)**: Mon 09-28 midday, Mon 09-28 EOD, Tue 09-29 overnight. Fired this day: routine-02-midday 17:30Z (off-sched, ~2.5h early), routine-03-eod 17:28Z (off-sched, ~10.5h early), routine-03-eod 04:12Z 09-30 (this wake, on-sched). Book stayed flat throughout; no exits missed.

## Rolling benchmark (marked to live-ticker 04:12Z 09-30)

- **BULL 30d** (08-30 → 09-29): **−1.64%** (equity $10,263.72 unchanged from prior EOD).
- **BULL 7d** (09-22 → 09-29): **−2.09%** (equity flat).
- **BTC-hold 30d** (~$79,500 → live $83,331): **+4.82%** (up +0.29pp from 17:28Z prior EOD — BTC recovered slightly).
- **BTC-hold 7d** (~$76,398 → live $83,331): **+9.07%** (up +0.30pp from prior).
- **BULL vs BTC-hold 30d**: **−6.46pp behind** BTC (**−0.29pp vs 17:28Z −6.17pp** — lost relative ground while flat as BTC recovered).
- **BULL vs BTC-hold 7d**: **−11.16pp behind** BTC (**−0.30pp vs 17:28Z −10.86pp** — same mechanism).
- **90d benchmark**: not-yet-computable (post-outage cross-window 74d gap; will resume after 10-15).

## Exit-rule replay — no positions to replay

Book has been flat since 09-27T15:00Z SOL close. No open positions across the 09-27 EOD → 09-30 EOD window; no exit rules to evaluate at this wake.

## Entry-scan (EOD 04:12Z 09-30, indicators.py bar-close authoritative) — regime PASS, ZERO tech-PASS

**Regime**: **12/15 positive 24h, median +0.37% → 5a PASS** — RECOVERED from prior 3 wakes of FAIL (3/15 −1.58% → 3/15 −0.82% → 3/15 −0.94% → **12/15 +0.37%**). 9-pair swing in 7h.

Positive pairs (12): BTC (+0.28), ETH (+0.27), SOL (+1.09), XRP (+0.29), SUI (+2.90), TAO (+0.02), XDG (+0.37), NEAR (+5.22), ADA (+0.44), FARTCOIN (+8.61), TRX (+0.50), AVAX (+8.33). Negatives (3): HYPE (−1.12), LINK (−3.25), LTC (−1.24).

**5a-SBD**: CLEAR by wide margin — both legs fail (12>1 positive; +0.37 > −1.0 floor).

**Full-pass technical check per indicators.py 04:12Z (rules 1+2+2a+3+4a)**: **0 pairs FULL PASS** — second consecutive zero-pass EOD wake (17:28Z was also zero).

| Pair | R1 (>EMA20) | R2 (RSI≥55) | R3 (4H>EMA50) | R4a | Verdict |
|---|---|---|---|---|---|
| BTC | FAIL −$237 | FAIL RSI 44.1 | FAIL −$193 | OK | R1+R2+R3 fail |
| ETH | FAIL −$12.43 | FAIL RSI 43.1 | FAIL −$2.04 | OK | R1+R2+R3 fail |
| SOL | FAIL −$0.024 (touch) | FAIL RSI 49.7 | PASS +$1.40 | OK | R1 near-miss, R2 fail |
| HYPE | FAIL −$0.69 | FAIL RSI 41.9 | FAIL −$4.03 | OK | technical reject |
| XRP | FAIL −$0.007 | FAIL RSI 46.2 | FAIL −$0.008 | OK | R1+R2+R3 fail |
| SUI | FAIL −$0.005 | FAIL RSI 46.9 | PASS +$0.051 | OK | R1+R2 fail |
| TAO | FAIL −$4.42 | FAIL RSI 42.4 | FAIL −$0.88 | OK | R1+R2+R3 fail |
| XDG | FAIL | FAIL RSI 43.5 | FAIL | OK | technical reject |
| NEAR | FAIL −$0.045 | FAIL RSI 47.6 | PASS +$0.22 | OK | R1+R2 fail |
| ADA | FAIL | FAIL RSI 43.7 | FAIL | OK | technical reject |
| LINK | FAIL −$0.33 | FAIL RSI 37.0 | PASS +$0.53 | OK | R1+R2 fail |
| LTC | FAIL | FAIL RSI 38.5 | FAIL | OK | technical reject |
| FARTCOIN | PASS +$0.0002 | FAIL RSI 51.5 | FAIL | FAIL $1.62M | R2+R3+R4a fail |
| TRX | PASS +$0.001 | PASS RSI 60.7 | FAIL −$0.0008 | FAIL $1.70M | R3+R4a fail — CLOSEST to full-pass |
| AVAX | FAIL −$0.008 | FAIL RSI 52.3 | PASS +$0.69 | OK | R1+R2 fail (RSI near-miss −2.7) |

**Verdict**: **0 technical-PASS pairs**. TRX is closest to a full-pass this wake (R1+R2+R2a all clear, RSI 60.7 comfortable) but R4a locks it out at $1.70M < $2.0M notional AND R3 fails at 4H EMA50 −$0.0008. Regime PASS is moot without eligible tape candidates.

Notable: the 9-pair swing to positive did NOT translate to R1/R2 passes because the recovery is fresh (RSIs still in 37-52 band; only TRX has punched RSI ≥55). One more day of positive tape could bring 4-5 pairs into RSI territory.

Note: ONDO/USD still not in `scripts/indicators.py` config (6th consecutive wake). Routed to routine-04-harness Sat 10-03.

## Active kill-switch state (routine-03-eod 2026-09-30T04:12Z / PT 2026-09-29 21:12; on-schedule authoritative)

- Daily loss cap (PT 2026-09-29): flat book, 0.00% P&L. CLEAR.
- Consecutive-loss cap: **3 losses** (NEAR 09-23 −1.01R, ADA 09-26 −0.29R, SOL 09-27 −0.01R scratch). Streak = 3 of 7. CLEAR.
- Max drawdown: **7.27%** from peak $11,068.89 (unchanged; book flat, no MTM). CLEAR (25% cap, 12.5% warn, **5.23pp headroom to warn**).
- Equity floor: **$10,263.72 > $7,500** (+$2,763.72). CLEAR.
- Exposure: **0.00%** / 4% used (flat book). CLEAR.
- Cluster cap: **0/2 BTC-cluster**. CLEAR.
- Universe/liquidity: N/A (flat book).
- 5b cooldown: SOL 09-27T15Z cleared (**85h ago**); NEAR 09-23 (**205h ago**); ADA 09-26 (**141h ago**). All expired.
- **Regime 5a: PASS 12/15 positive, median +0.37%** — new entries permitted (moot; 0 tech PASS anyway).
- **5a-SBD: CLEAR** — both legs fail by wide margin.
- MCP availability: Kraken ticker + OHLCV + indicators.py + watchdog all healthy. `kraken_risk_flag` returned NO_DATA (daily_risk_flag.json not present — unchanged carry-over, non-blocking).
- **All Ring 3 kill switches CLEAR.**

## Ops notes

- **First on-schedule fire since 09-27** — this EOD landed at 04:12Z 09-30 (PT 2026-09-29 21:12) vs cron 21:00 PT = 12-minute drift only. Encouraging signal that Task Scheduler drift may have self-corrected. Prior 7 fires (09-27 → 09-29) were all off-schedule (5 day-mask, 2 within-day early). Routine-04-harness Sat 10-03 cron audit will confirm this is stable, not a one-off.
- **Missed slots since 09-28 overnight**: Mon 09-28 midday/EOD, Tue 09-29 overnight (all 3 slots). Book stayed flat throughout so no exits missed; entry-scans at those slots would have been blocked by regime 5a FAIL similarly.
- **Watchdog: 8 findings** (unchanged since 09-28 overnight — routine-06 heartbeat, routine-07 heartbeat, C dirty-tree 4 files, D stale-MTM ×5 variants). No new findings. Alerted per --telegram.
- **Regime whiplash 3/15 → 12/15 in 7h**: notable intraday recovery. The momentum unwind flagged at 17:28Z arrested and broadly reversed within the same PT session. If recurring, may argue for tighter regime-read cadence or 2-of-3 confirmation gate — single data point only, no memo candidate yet.
- **Cash-fit constraint no longer binding** — book is flat, all $10,263.72 available for next entry.
- **Wed 09-30 is last trading day of September** → tomorrow's EOD wake (04:00Z 10-01 in UTC) owes the monthly archive sweep of any rows dated < 08-31 (current trade_log has no 08-xx rows so archive will effectively be small — 07-xx rows from the SOL/ETH/ADA/BTC/HYPE sequence).

## Notes for next wake

- Book is flat; next scheduled fire is Wed 09-30 06:00 PT overnight (assuming Task Scheduler continues its recovered behavior from this wake).
- Regime has just flipped to PASS 12/15 — one more session of positive tape would likely start bringing pairs into RSI ≥55 territory (currently only TRX clears, but R3+R4a blocked). Watch NEAR (+5.22 24h, RSI 47.6), AVAX (+8.33 24h, RSI 52.3), SUI (+2.90 24h, RSI 46.9) as the R2-recovery candidates.
- W22-H ratchet pattern-of-4 remains outstanding for routine-04-harness Sat 10-03 memo (P-W25R-RATCHET-TIGHTEN).
- Wed 09-30 EOD = monthly archive sweep due (rows dated < 08-31 into `memory/archive/2026-09.md`).
