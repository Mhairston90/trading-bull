# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-07-01T04:12Z routine-03-eod (PT Tue 2026-06-30 21:12 ON-SCHEDULE M-F cron `0 21 * * 1-5`). **1 OPEN / 0 EXIT** — regime flipped back **5a PASS 9/15 positive median +0.44%** (SBD CLEAR) from midday's 1/15 FAIL; **OPENED SOL/USD long 87.5709 @ $75.3538** (stop $73.5918, target $82.4019, 1.50% risk = $154.30, notional $6,598.80, entry commission $17.16, cash post-entry $3,670.97) — rule-8 winner (SOL 30d rank 3 > HYPE 4 > SUI 6 > ADA 10 > LTC 12 all TECH-PASS), SOL 5b cooldown lapsed at 04:00Z exactly 12min before fire; equity MTM $10,267.22 (day PnL −$19.71 / −0.19% = entry friction). DD 5.60%. All Ring 3 kill switches CLEAR.

> **Prior rebuilds:** 2026-06-30T20:00Z routine-02-midday (Tue 13:00 PT ON-SCHEDULE M-F, 0 entries / 0 exits, flat, regime FAIL 1/15 SBD ACTIVE); 2026-06-30T15:07Z routine-01-overnight (Tue 06:00 PT slot ~2h7m late fire, 0 entries / 0 exits, regime FAIL 0/15 SBD ACTIVE); 2026-06-30T10:30Z routine-03-eod (LATE FIRE Mon 21:00 PT slot — labeled PT 2026-06-29 Mon EOD — closed SOL/USD long +$74.48 / +0.49R net on Exit-1 two-bar EMA20 confirmation, ended day $10,286.93 / +0.91%); 2026-06-29T20:00Z routine-02-midday (held SOL +1.71R unrealized at tick $75.80, equity $10,458.97, DD 3.83%); 2026-06-29T04:11Z routine-03-eod (OPENED SOL/USD 82.3578 @ $72.6163, regime flipped back PASS 9/15 SBD CLEAR).

## Account

- Starting equity: **$10,000.00**
- Cash: **$3,670.97** (= $10,286.93 pre-entry cash − $6,598.80 SOL notional − $17.16 entry commission)
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
- Unrealized PnL (open positions): **−$2.63** (SOL 87.5709 × ($75.35 last close − $75.3538 fill) = −$0.33 MTM, plus $17.16 friction already booked as cash reduction; net position mark vs fill = −$0.33, but full trade round-trip drag is entry commission $17.16 → equity mark reflects both)
- Position values: **$6,598.47** (SOL 87.5709 × $75.35 = $6,598.47 MTM at last-closed 1H bar)
- Current equity (cash + MTM): **$10,267.22** (= $3,670.97 cash + $6,598.47 SOL MTM; note: pre-entry equity was $10,286.93, day PnL = −$19.71 = entry commission $17.16 + slippage $2.55 = −0.19%)
- Equity peak: **$10,875.85** (set 2026-06-13T09:00Z at TAO 4R close — unchanged)
- Drawdown from peak: **5.60%** ($608.63 below peak)
- Since-inception return: **+2.67%** ($10,267.22 / $10,000 − 1)

## Open positions

| Pair | Side | Size | Entry | Stop | Target | Notional | Risk-at-moment | Cluster | Entered |
|------|------|------|-------|------|--------|----------|----------------|---------|---------|
| SOL/USD | long | 87.5709 | $75.3538 | $73.5918 | $82.4019 | $6,598.80 | 1.50% ($154.30) | BTC-cluster (1/2) | 2026-07-01T04:00Z |

Portfolio risk-at-moment: **1.50%** of equity. Cap 4% → 2.50pp headroom.
Open positions: **1 / 8** (strategy v0.4 max-concurrent 4 → 1/4 used; BTC-cluster 1/2 used).
Breakeven ratchet (W22-H-partial): SOL R≈0 at wake, needs 1H close ≥ +2R = $75.3538 + 2×$1.76202 = **$78.878** to arm.

## EOD snapshot — 2026-06-30 PT Tue 21:00 PT

| Metric | Value |
|---|---|
| Wake type | routine-03-eod (Tue 21:00 PT ON-SCHEDULE M-F cron, PT date 2026-06-30) |
| Entries this wake | **1** (SOL/USD long 87.5709 @ $75.3538, rule-8 winner over HYPE/SUI/ADA/LTC) |
| Exits this wake | 0 (flat at wake; no positions to evaluate before entry) |
| Day-to-date P&L (PT 2026-06-30) | **−$19.71 / −0.19%** (entry friction only, no realized closes today) |
| Equity (cash + MTM) | **$10,267.22** ($3,670.97 cash + $6,598.47 SOL MTM) |
| Equity peak | $10,875.85 (unchanged; need +$608.63 to retake) |
| Drawdown from peak | **5.60%** (up from 5.41% midday by 0.19pp = entry friction) |
| Loss streak | 0 trading days (unchanged; Mon's +$74.48 winner reset prior streak) |
| Trades today | 1 opened, 0 closed |

## Active kill-switch state

- Daily realized + unrealized PT 2026-06-30: **−$19.71 / −0.19%** of equity — CLEAR (5.00% loss cap → 4.81pp headroom).
- Consecutive losing trading days: **0** (cap 7, full 7-day headroom). CLEAR.
- Max drawdown: **5.60%** from peak $10,875.85 (cap 25%, warn 12.5%, **6.90pp to warn**) — CLEAR.
- Equity floor: $10,267.22 > $7,500 floor — CLEAR.
- MCP availability: Kraken OK (`kraken_multi_ticker` + `kraken_ohlcv` returned all pairs; `indicators.py` 720 4H bars/pair). CLEAR.
- Regime gate (rule 5a): **PASS** (9/15 positive — SOL, ETH, XRP, SUI, ADA, LTC, FARTCOIN, AVAX, HYPE-if-marginal; median +0.44%) — new entries permitted.
- Regime sub-state (rule 5a-SBD): **CLEAR** (positives 9 > 1 OR median +0.44% > −1.0%). Both SBD gates failed → SBD off.
- Active 5b cooldowns: **none** (SOL/USD 24h cooldown lapsed 2026-07-01T04:00Z exactly).
- Cluster cap (rule 6a, BTC-cluster): **1/2** used (SOL). Full headroom left = 1 more slot.
- **All Ring 3 kill switches CLEAR.** Routine-03-eod 2026-07-01T04:12Z: **1 entry, 0 exits, flat at wake / 1 open after**.

## Universe refresh — 2026-06-01 (first true 30d aggregation)

| Rank | Pair | Change vs prior |
|------|------|-----------------|
| 1 | BTC | — |
| 2 | ETH | — |
| 3 | SOL | — |
| 4 | HYPE | ▲ from 6 |
| 5 | XRP | ▼ from 4 |
| 6 | SUI | ▲ from 8 |
| 7 | TAO | ▼ from 5 |
| 8 | XDG (DOGE) | — |
| 9 | NEAR | **NEW** (was off-list near-miss) |
| 10 | ADA | — |
| 11 | LINK | ▲ from 13 |
| 12 | LTC | ▼ from 9 |
| 13 | FARTCOIN | ▼ from 11 |
| 14 | TRX | ▲ from 15 |
| 15 | AVAX | ▼ from 12 |

- **PENGU dropped** (was rank 14) → moves to near-miss watch list (~$38M 30d notional).
- **Near-miss watch:** PENGU $38M, DOT $22M, UNI $20M.

## Pending exit triggers

**SOL/USD long** — exit conditions checked at each 1H close:
- Exit 1 (W22-G): two consecutive 1H closes < 20-EMA ($73.777 per indicators R1 +$1.573 from close $75.35). Trigger: 2 consecutive closes < ~$73.78.
- Exit 1-SBD (only if regime flips back to SBD): two consecutive 1H closes < 9-EMA. Currently inactive (regime PASS).
- Exit 2 (stop-hit): active stop $73.5918 (2×ATR14). Ratchet inactive until +2R close ≥ $78.878.
- Exit 3 (take-profit): 4R = $82.4019.

Next entry-eligible scan: routine-01-overnight Wed 2026-07-01 06:00 PT (= 13:00Z Wed). Cluster 1/2 used, so 1 more cluster slot available; position cap 1/4, so 3 more slots. Gated by regime and per-pair TECH-PASS. No 5b cooldowns active.

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | ≈ −1.4% (equity 06-24 ~$10,414 → today $10,267 MTM) | ≈ −4.7% est (BTC 06-24 ~$62.0k → today $59.1k) | ≈ +3.3% est | BULL ahead 7d |
| 30d | ≈ +2.67% (inception $10k 2026-04-20; MTM $10,267.22) | ≈ −23% est (BTC 30d ago ~$77k → today $59.1k) | ≈ +26% est | BULL well ahead |
| 90d | — | — | — | not computable (BULL inception 2026-04-20 = 72 days ago; window first computable ~2026-07-19) |

(BTC tick read $59,100 this wake per indicators.py.)
