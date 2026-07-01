# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-07-01T15:52Z routine-01-overnight (PT Wed 2026-07-01 08:52 ON-SCHEDULE M-F cron `0 6 * * 1-5`, ~2h52m late fire vs 06:00 PT). **0 OPEN / 0 CLOSE this wake** — regime flipped strong bullish **5a PASS 13/15 positive median +2.45% (SBD CLEAR)** from overnight-Tue's 0/15 SBD ACTIVE, universe fully recovered. **SOL/USD held (entry $75.3538 → last close $76.87 = +0.86R unrealized / +$132.79 unrealized)** — no exit triggers hit. Entry scan: 3 tech-PASS pairs (SOL/SUI/ADA) but SOL already open, SUI & ADA both cash-insufficient at strategy-mandated sizing ($7,192 & $5,912 notional required vs $3,671 cash). Rule-8 fallback exhausted → **no entry this wake**. **First-of-month universe refresh executed** — ONDO in (rank 14), FARTCOIN out (dropped to 18 near-miss); universe committed separately. Equity MTM $10,402.80 (day PnL +$135.58 / +1.32% = unrealized SOL mark-up). DD 4.35% (down 1.25pp from prior wake). All Ring 3 kill switches CLEAR.

> **Prior rebuilds:** 2026-07-01T04:12Z routine-03-eod (Tue 21:00 PT ON-SCHEDULE M-F cron, PT date 2026-06-30, 1 entry SOL/USD 87.5709 @ $75.3538 / 0 exits, rule-8 winner over HYPE/SUI/ADA/LTC, regime flipped back PASS 9/15 SBD CLEAR); 2026-06-30T20:00Z routine-02-midday (Tue 13:00 PT ON-SCHEDULE M-F, 0/0, flat, regime FAIL 1/15 SBD ACTIVE); 2026-06-30T15:07Z routine-01-overnight (Tue 06:00 PT slot ~2h7m late fire, 0/0, regime FAIL 0/15 SBD ACTIVE); 2026-06-30T10:30Z routine-03-eod (LATE FIRE Mon 21:00 PT slot — labeled PT 2026-06-29 Mon EOD — closed SOL/USD long +$74.48 / +0.49R net on Exit-1 two-bar EMA20 confirmation, ended day $10,286.93 / +0.91%); 2026-06-29T20:00Z routine-02-midday (held SOL +1.71R unrealized at tick $75.80, equity $10,458.97, DD 3.83%); 2026-06-29T04:11Z routine-03-eod (OPENED SOL/USD 82.3578 @ $72.6163, regime flipped back PASS 9/15 SBD CLEAR).

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
- Unrealized PnL (open positions): **+$132.79** (SOL 87.5709 × ($76.87 − $75.3538) = 87.5709 × $1.5162 = +$132.79 gross; entry commission $17.16 already booked at open)
- Position values: **$6,731.83** (SOL 87.5709 × $76.87 last 1H close = $6,731.83 MTM)
- Current equity (cash + MTM): **$10,402.80** (= $3,670.97 cash + $6,731.83 SOL MTM; wake-over-wake PnL = +$135.58 from $10,267.22 prior rebuild)
- Equity peak: **$10,875.85** (set 2026-06-13T09:00Z at TAO 4R close — unchanged)
- Drawdown from peak: **4.35%** ($473.05 below peak; improved 1.25pp from 5.60% at prior wake)
- Since-inception return: **+4.03%** ($10,402.80 / $10,000 − 1)

## Open positions

| Pair | Side | Size | Entry | Stop | Target | Notional | Risk-at-moment | Cluster | Entered |
|------|------|------|-------|------|--------|----------|----------------|---------|---------|
| SOL/USD | long | 87.5709 | $75.3538 | $73.5918 | $82.4019 | $6,598.80 | 1.48% ($154.30 / $10,402.80) | BTC-cluster (1/2) | 2026-07-01T04:00Z |

Portfolio risk-at-moment: **1.48%** of equity. Cap 4% → 2.52pp headroom.
Open positions: **1 / 8** (strategy v0.4 max-concurrent 4 → 1/4 used; BTC-cluster 1/2 used).
Breakeven ratchet (W22-H-partial): SOL +0.86R at wake ($76.87 close), needs 1H close ≥ +2R = $78.878 to arm. **Not yet armed**; peak 1H close so far = $76.87. Gap to arm = $2.01.

## Overnight snapshot — 2026-07-01 PT Wed 06:00 PT (fired 08:52 PT, ~2h52m late)

| Metric | Value |
|---|---|
| Wake type | routine-01-overnight (Wed 06:00 PT ON-SCHEDULE M-F cron, PT date 2026-07-01) |
| Entries this wake | 0 (SOL R5 REJECT already-open; SUI/ADA REJECT cash-insufficient at strategy sizing) |
| Exits this wake | 0 (SOL above stop $73.59, above 20-EMA, not at target, ratchet not armed) |
| Day-to-date P&L (PT 2026-07-01) | **+$135.58 / +1.32%** (unrealized SOL mark-up, no realized closes) |
| Equity (cash + MTM) | **$10,402.80** ($3,670.97 cash + $6,731.83 SOL MTM) |
| Equity peak | $10,875.85 (unchanged; need +$473.05 to retake) |
| Drawdown from peak | **4.35%** (down from 5.60% at prior wake by 1.25pp = SOL mark-up) |
| Loss streak | 0 trading days (unchanged) |
| Trades today | 0 opened, 0 closed |
| Universe refresh | **YES** — first-of-month sweep executed, ONDO in / FARTCOIN out |

## Active kill-switch state

- Daily realized + unrealized PT 2026-07-01: **+$135.58 / +1.32%** of equity — CLEAR (positive; 5.00% loss cap → 6.32pp headroom to loss cap).
- Consecutive losing trading days: **0** (cap 7, full 7-day headroom). CLEAR.
- Max drawdown: **4.35%** from peak $10,875.85 (cap 25%, warn 12.5%, **8.15pp to warn**) — CLEAR.
- Equity floor: $10,402.80 > $7,500 floor — CLEAR.
- MCP availability: Kraken OK (`kraken_multi_ticker` + `kraken_ohlcv` returned all pairs; `indicators.py` 720 4H bars/pair; Kraken REST universe-refresh returned 26/26 candidates). CLEAR.
- Regime gate (rule 5a): **PASS** (13/15 positive per indicators.py — ADA/AVAX/SOL/FARTCOIN/BTC/ETH/XRP/SUI/LINK/NEAR/XDG/LTC/TRX; only HYPE/TAO negative; median +2.45%) — new entries permitted.
- Regime sub-state (rule 5a-SBD): **CLEAR** (positives 13 > 1 AND median +2.45% > −1.0%). Both SBD gates failed → SBD off. 4th regime flip in 40h (Sun EOD SBD ACTIVE → Mon 06-29 EOD SBD CLEAR → Tue 06-30 EOD SBD CLEAR → Tue overnight 06-30T15:07Z SBD ACTIVE → Wed 07-01T04:12Z EOD SBD CLEAR → today SBD CLEAR).
- Active 5b cooldowns: **none** (SOL/USD 24h cooldown from 2026-06-27 lapsed 06-28; recent 2026-07-01T04:00Z SOL open is the current position, not a stop-out).
- Cluster cap (rule 6a, BTC-cluster): **1/2** used (SOL). Full headroom left = 1 more slot.
- **All Ring 3 kill switches CLEAR.** Routine-01-overnight 2026-07-01T15:52Z: **0 entries, 0 exits, 1 open at wake / 1 open after**.

## Universe refresh — 2026-07-01 (second true 30d aggregation)

Top 15 by 30d notional (Kraken public REST OHLC 1440-min bars × 30, vwap × volume):

| Rank | Pair | 30d notional | Change vs 2026-06-01 |
|------|------|-------------:|-----------------|
| 1 | BTC | $5,120M | — |
| 2 | ETH | $1,435M | — |
| 3 | SOL | $795M | — |
| 4 | HYPE | $726M | — |
| 5 | XRP | $711M | — |
| 6 | ADA | $249M | ▲ from 10 |
| 7 | NEAR | $210M | ▲ from 9 |
| 8 | SUI | $180M | ▼ from 6 |
| 9 | TAO | $158M | ▼ from 7 |
| 10 | XDG | $157M | ▼ from 8 |
| 11 | LTC | $75M | ▲ from 12 |
| 12 | AVAX | $70M | ▲ from 15 |
| 13 | LINK | $68M | ▼ from 11 |
| 14 | ONDO | $51M | **NEW** (replaces FARTCOIN) |
| 15 | TRX | $46M | ▼ from 14 |

- **FARTCOIN dropped** (was rank 13) → moves to near-miss watch (~$27M 30d notional).
- **Near-miss watch:** TON $38M, UNI $33M, FARTCOIN $27M, DOT $21M, PENGU $20M.

## Pending exit triggers

**SOL/USD long** — exit conditions checked at each 1H close:
- Exit 1 (W22-G): two consecutive 1H closes < 20-EMA ($74.806 per indicators R1 close $76.87 − 2.064 margin). Currently 1H close $76.87 well above; trigger requires 2 consecutive closes < ~$74.81.
- Exit 1-SBD (only if regime flips back to SBD): two consecutive 1H closes < 9-EMA. Currently inactive (regime PASS).
- Exit 2 (stop-hit): active stop $73.5918 (2×ATR14 at entry). Ratchet inactive until +2R close ≥ $78.878.
- Exit 3 (take-profit): 4R = $82.4019.

Next entry-eligible scan: routine-02-midday Wed 2026-07-01 13:00 PT (= 20:00Z Wed). Cluster 1/2 used, so 1 more cluster slot available; position cap 1/4, so 3 more slots. Gated by regime and per-pair TECH-PASS. **Cash-fit constraint dominates:** any BTC/ETH sizing exceeds cash; SUI/ADA also cash-insufficient; likely no entry until SOL closes (freeing cash) unless a low-vol pair passes tech at a stop distance ≥ ~2.7% of price.

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | ≈ −0.1% (equity 06-24 ~$10,414 → today $10,402.80 MTM) | ≈ −1.7% est (BTC 06-24 ~$61.1k → today $60.1k) | ≈ +1.6% est | BULL ahead 7d |
| 30d | ≈ +4.03% (inception $10k 2026-04-20; MTM $10,402.80) | ≈ −22% est (BTC 30d ago ~$77k → today $60.1k) | ≈ +26% est | BULL well ahead |
| 90d | — | — | — | not computable (BULL inception 2026-04-20 = 73 days ago; window first computable ~2026-07-19) |

(BTC tick read $60,074.8 live (multi-ticker) / $59,464.9 last 1H close (indicators.py) this wake.)
