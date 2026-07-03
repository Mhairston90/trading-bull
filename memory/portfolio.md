# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-07-03T04:11Z routine-03-eod (PT Thu 2026-07-02 21:11 ON-SCHEDULE M-F cron `0 21 * * 1-5`, PT date label 2026-07-02 per date-labeling guard, UTC wall-clock 2026-07-03T04:11Z). **0 OPEN / 0 CLOSE this wake** — SOL/USD long held, breakeven ratchet remains ARMED at $75.3538 (armed 2026-07-02T09:00Z overnight, up-only per v0.4). **Exit checks all PASS** on SOL/USD (last closed 1H bar 07-03T03:00Z): (i) **1H 20-EMA per `scripts/indicators.py` = $80.311** at close of 07-03T03:00Z, last close $80.64 = **$0.33 above EMA**; second-most-recent close $80.72 (02:00Z) also above EMA $80.273 → **Exit 1 two-bar confirmation NOT triggered**; (ii) lowest bar low since ratchet-arm at 07-02T09:00Z = $78.21 at 09:00Z bar itself, all subsequent lows well above active stop $75.3538 (min headroom **$2.86**); **Exit 2 stop-hit NOT triggered**; (iii) highest 1H close since ratchet-arm = **$82.30** at 11:00Z bar (still $0.10 short of 4R target $82.4019 close; intrabar $82.65 exceeded target by $0.248 but Exit-3 is close-only per v0.4) — **Exit 3 4R-target NOT triggered**. Post-arm 1H closes since 11:00Z: 81.32, 81.35, 80.44, 80.78, 80.48, 80.59, 80.96, 80.78, 80.94, 80.68, 80.57, 80.62, 80.64, 81.41, 80.72, 80.64 (last) — trend consolidated above 20-EMA in a $80–$81 band since drifting back from 4R zone. Equity MTM **$10,732.69** ($3,670.97 cash + 87.5709 SOL × $80.64 = $7,061.72) = **−$12.26 / −0.11% wake-over-wake** vs midday $10,744.95; **day-to-date PT 2026-07-02 = +$175.14 / +1.66%** vs prior EOD $10,557.55 (all unrealized SOL mark-up, 0 realized closes today). DD **1.32%** (widened 0.12pp from midday's 1.20%, still **sub-2% window since equity peak set 2026-06-13**; 11.18pp headroom to 12.5% warn). All Ring 3 kill switches CLEAR. **Entry scan run per routine-03 spec**: 9 non-open TECH-PASS candidates (BTC, ETH, HYPE, XRP, SUI, TAO, XDG, ADA, LINK), rule-8 winner BTC by 30d rank 1, **all 9 REJECT cash-insufficient** at 1.5%-risk sizing vs $3,670.97 cash — **7th consecutive cash-binding wake W24-W27** (P-W26-CASHFIT still pending user `[Y/N]`). Monthly-archive check: PT 2026-07-02 (Thu) is NOT last trading day of July (last = Fri 2026-07-31) → no archive.

> **Prior rebuilds:** 2026-07-02T20:00Z routine-02-midday (Thu 13:00 PT ON-SCHEDULE M-F, PT date 2026-07-02, 0/0, SOL held +2.99R unrealized, DD 1.20%); 2026-07-02T13:07Z routine-01-overnight (Thu 06:00 PT ON-SCHEDULE M-F, PT date 2026-07-02, 0/0, **MILESTONE: W22-H breakeven ratchet ARMED on SOL/USD** at bar 07-02T09:00Z close $79.40 = +2.30R, stop moved $73.5918 → $75.3538; 10 non-open TECH-PASS all cash-rejected, regime PASS 15/15 SBD CLEAR, DD 0.77%, +4R intrabar-touch/close-miss 1st instance at 11:00Z bar); 2026-07-02T04:11Z routine-03-eod (Wed 21:00 PT ON-SCHEDULE, PT date 2026-07-01, 0/0, SOL held +1.87R unrealized, 7 TECH-PASS all cash-rejected, DD 2.93%); 2026-07-01T20:00Z routine-02-midday (Wed 13:00 PT ON-SCHEDULE M-F, 0/0, SOL held +0.87R unrealized, DD 4.34%); 2026-07-01T15:52Z routine-01-overnight (Wed 06:00 PT slot ~2h52m late fire, 0/0, regime PASS 13/15 SBD CLEAR, SOL held +0.86R unrealized, universe refresh ONDO in / FARTCOIN out); 2026-07-01T04:12Z routine-03-eod (Tue 21:00 PT ON-SCHEDULE M-F, PT date 2026-06-30, 1 entry SOL/USD 87.5709 @ $75.3538 / 0 exits, rule-8 winner over HYPE/SUI/ADA/LTC, regime flipped back PASS 9/15 SBD CLEAR).

## Account

- Starting equity: **$10,000.00**
- Cash: **$3,670.97** (unchanged; no trade events this wake)
- Realized PnL (all-time): **+$286.80** (unchanged; no closes this wake)
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
- Unrealized PnL (open positions): **+$462.90** (SOL 87.5709 × ($80.64 − $75.3538) = 87.5709 × $5.2862 = +$462.90 gross; entry commission $17.16 already booked at open)
- Position values: **$7,061.72** (SOL 87.5709 × $80.64 last 1H close 07-03T03:00Z = $7,061.72 MTM)
- Current equity (cash + MTM): **$10,732.69** (= $3,670.97 cash + $7,061.72 SOL MTM; wake-over-wake PnL = −$12.26 from $10,744.95 prior midday rebuild)
- Equity peak: **$10,875.85** (set 2026-06-13T09:00Z at TAO 4R close — unchanged)
- Drawdown from peak: **1.32%** ($143.16 below peak; widened 0.12pp from midday's 1.20%; still best sub-2% window since peak-set on 2026-06-13)
- Since-inception return: **+7.33%** ($10,732.69 / $10,000 − 1)

## Open positions

| Pair | Side | Size | Entry | Stop (RATCHETED) | Target | Notional | Risk-at-moment | Cluster | Entered |
|------|------|------|-------|------------------|--------|----------|----------------|---------|---------|
| SOL/USD | long | 87.5709 | $75.3538 | **$75.3538** (breakeven, ratchet armed 2026-07-02T09:00Z) | $82.4019 | $7,061.72 | **~$0.00 / 0.00%** | BTC-cluster (1/2) | 2026-07-01T04:00Z |

Portfolio risk-at-moment: **~0.00%** of equity (post-ratchet breakeven stop). Cap 4% → full headroom.
Open positions: **1 / 8** (strategy v0.4 max-concurrent 4 → 1/4 used; BTC-cluster 1/2 used).
Breakeven ratchet (W22-H-partial): **ARMED at 2026-07-02T09:00Z** (bar close $79.40 = +2.30R > +2R threshold $78.878 by $0.522). Active stop moved from $73.5918 → $75.3538. Post-arm peak 1H close = $82.30 at bar 07-02T11:00Z (short of +4R take-profit close threshold $82.4019 by $0.10; intrabar high $82.65 exceeded target by $0.248 but Exit-3 is 1H-close-only). Post-arm 1H closes since 11:00Z: 81.32, 81.35, 80.44, 80.78, 80.48, 80.59, 80.96, 80.78, 80.94, 80.68, 80.57, 80.62, 80.64, 81.41, 80.72, 80.64 (last close). Latest close $80.64 = +2.92R gross. Ratchet is up-only per strategy v0.4; remains at $75.3538 for life of trade.

## EOD snapshot — 2026-07-02 PT Thu 21:11 PT (fired 04:11Z on-cron)

| Metric | Value |
|---|---|
| Wake type | routine-03-eod (Thu 21:00 PT ON-SCHEDULE M-F cron, PT date 2026-07-02, wall-clock UTC 2026-07-03T04:11Z) |
| Entries this wake | **0** (9 non-open TECH-PASS candidates all REJECT cash-insufficient at 1.5%-risk sizing vs $3,670.97 cash) |
| Exits this wake | **0** (SOL 20-EMA gap +$0.33, stop headroom $5.29 from latest close $80.64, +4R target close missed by $1.76 on latest close, prior 11:00Z close missed by $0.10) |
| Stop-management events | 0 (ratchet already armed by routine-01 overnight 07-02T09:00Z; up-only, no further move) |
| Day-to-date P&L (PT 2026-07-02) | **+$175.14 / +1.66%** vs prior EOD $10,557.55 (all unrealized SOL mark-up, no realized closes) |
| Wake-over-wake P&L | **−$12.26 / −0.11%** (SOL 03:00Z close $80.64 vs midday-mark 19:00Z close $80.78 = −$0.14 × 87.5709 = −$12.26 MTM) |
| Equity (cash + MTM) | **$10,732.69** ($3,670.97 cash + $7,061.72 SOL MTM) |
| Equity peak | $10,875.85 (unchanged; need +$143.16 to retake) |
| Drawdown from peak | **1.32%** (widened 0.12pp from midday's 1.20%; still comfortably clear of 12.5% warn — **11.18pp headroom**) |
| Loss streak | 0 trading days (unchanged) |
| Trades today | 0 opened, 0 closed |

## Active kill-switch state

- Daily realized + unrealized PT 2026-07-02: **+$175.14 / +1.66%** of equity — CLEAR (positive; 5.00% loss cap → 6.66pp headroom to loss cap).
- Consecutive losing trading days: **0** (cap 7, full 7-day headroom). CLEAR.
- Max drawdown: **1.32%** from peak $10,875.85 (cap 25%, warn 12.5%, **11.18pp to warn**) — CLEAR.
- Equity floor: $10,732.69 > $7,500 floor — CLEAR.
- MCP availability: Kraken OK (`kraken_multi_ticker` + `kraken_ohlcv` + `scripts/indicators.py` returned data this wake). CLEAR.
- Regime gate (rule 5a): **PASS 14/15 positive median +2.17%** (only LTC −0.12% negative; per `scripts/indicators.py` authoritative close-to-close, 04:11:39Z).
- Regime sub-state (rule 5a-SBD): **CLEAR** (14 positives ≫ 1 ceiling; median +2.17% ≫ −1.0% floor).
- Active 5b cooldowns: **none**.
- Cluster cap (rule 6a, BTC-cluster): **1/2** used (SOL). Full headroom left = 1 more slot (irrelevant this wake — all cash-rejected).
- **All Ring 3 kill switches CLEAR.** Routine-03-eod 2026-07-03T04:11Z: **0 entries, 0 exits, 1 open at wake / 1 open after**.

## Universe (unchanged since 2026-07-01 refresh)

Top 15 by 30d notional per `memory/universe.md` (refreshed at 07-01 overnight; next refresh 2026-08-01):

BTC, ETH, SOL, HYPE, XRP, ADA, NEAR, SUI, TAO, XDG, LTC, AVAX, LINK, ONDO, TRX.

## Pending exit triggers

**SOL/USD long — post-ratchet state:** exit conditions checked at each 1H close.
- Exit 1 (W22-G): two consecutive 1H closes < 20-EMA ($80.311 at last close 07-03T03:00Z). Currently 1H close $80.64 is $0.33 above; trigger requires 2 consecutive closes < ~$80.31. **Gap narrowing** — midday gap was $1.06, now $0.33 (compressed 0.73 over 8h as EMA continues to advance while closes consolidate in $80–$81 band).
- Exit 1-SBD (only if regime flips back to SBD): two consecutive 1H closes < 9-EMA. Currently inactive (regime PASS 14/15 per `scripts/indicators.py`).
- Exit 2 (stop-hit): **active stop $75.3538 (breakeven, post-ratchet)**. Ratchet armed 07-02T09:00Z; up-only, will not trail higher. Post-arm lowest low $78.21 at 09:00Z bar; recent lows range $80.23–$80.83. Min headroom $2.86 (at 09:00Z bar), current headroom $5.29 vs latest close.
- Exit 3 (take-profit): 4R = $82.4019. Missed by $0.10 on close 07-02T11:00Z at $82.30 despite intrabar $82.65 (+$0.248 over target). Post-11:00Z closes drifted back to $80.64 → 4R gap now $1.76 on close basis.

Next entry-eligible scan: routine-01-overnight Fri 2026-07-03 06:00 PT (= 13:00Z Fri). Cluster 1/2 used, so 1 more cluster slot available; position cap 1/4, so 3 more slots. Gated by regime (currently PASS) and per-pair TECH-PASS. **Cash-fit constraint remains dominant** — 9 TECH-PASS at this wake all cash-blocked at $3,670.97 vs 1.5%-risk sizing; P-W26-CASHFIT pending user Y/N (weekly memo W26).

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | ≈ +3.06% (equity 06-26 EOD $10,413.87 → today $10,732.69 MTM) | ≈ +1.37% est (BTC 06-26 ~$60,449.20 → today $61,275.9) | ≈ +1.69pp | BULL ahead 7d |
| 30d | ≈ +7.33% (inception $10k 2026-04-20; MTM $10,732.69) | ≈ −20% est (BTC 30d ago ~$77k → today $61.3k) | ≈ +27pp | BULL well ahead |
| 90d | — | — | — | not computable (BULL inception 2026-04-20 = 74 days ago; window first computable ~2026-07-19) |

(BTC last tick $61,275.9 via `kraken_multi_ticker`, 24h −0.34%.)
