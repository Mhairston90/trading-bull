# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-06-27T21:30Z routine-02-midday (PT Sat 2026-06-27 14:30 — OFF-SCHEDULE Saturday fire vs M-F cron `0 13 * * 1-5`; routine markdown has no day-gate so executed normally). **1 EXIT: SOL/USD stop-out intrabar at 2026-06-27T19:00Z** (19:00Z bar low $70.82 pierced stop $71.3184; closed at stop with 0.05% slippage = $71.2827, net −$201.55 / −1.29R). Portfolio now FLAT. Regime gate still 5a PASS (per overnight read 14/15 positive); SBD CLEAR. Equity $10,212.32 (DD widened to 6.10% from 4.54%). All Ring 3 kill switches CLEAR. Daily PnL −1.93% well below 5% cap. Loss-streak day 1 (today's −$201.55 vs prior flat day).

> **Prior rebuilds:** 2026-06-27T16:45Z routine-01-overnight (OPEN SOL/USD 110.1608 @ $72.7364, 14/15 positive median +1.60% PASS); 2026-06-26T20:00Z routine-02-midday (flat, 12/15 positive median +1.05%, SBD CLEAR); 2026-06-26T15:53Z routine-01-overnight (flat, 11/15 positive median +1.21%, regime flipped to PASS but R3 binding 0/15).

## Account

- Starting equity: **$10,000.00**
- Cash: **$10,212.32** (post-close: $2,380.18 + $7,832.14 exit proceeds — exit notional $7,852.56 less $20.42 exit commission)
- Realized PnL (all-time): **+$212.32** (was +$413.87; −$201.55 SOL stop-out this wake)
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
  - **SOL −$201.55 (exit-stop-hit-intrabar 2026-06-27T19:00Z, −1.29R)** — this wake
- Unrealized PnL (open positions): **$0** — FLAT
- Position values: **$0**
- Current equity (cash + MTM): **$10,212.32**
- Equity peak: **$10,875.85** (set 2026-06-13T09:00Z at TAO 4R close — unchanged)
- Drawdown from peak: **6.10%** ($663.53 below peak; widened from 4.54% by today's stop-out)
- Since-inception return: **+2.12%** ($10,212.32 / $10,000 − 1)

## Open positions

(none — portfolio flat after SOL stop-out)

Portfolio risk-at-moment: **0.00%** of equity. Cap 4% → full 4pp headroom.
Open positions: **0 / 8** (strategy v0.4 max-concurrent 4 → 0/4 used; BTC-cluster 0/2 used).
Breakeven ratchet (W22-H-partial): N/A — no open positions.

## Midday snapshot — 2026-06-27 PT (Sat, OFF-SCHEDULE — M-F cron fired Sat)

| Metric | Value |
|---|---|
| Wake type | routine-02-midday (OFF-SCHEDULE Saturday — routine has no day-gate, executed) |
| Open positions MTM | $0 (flat after SOL stop-out) |
| Exits this wake | **1 (SOL/USD stop-out intrabar at 2026-06-27T19:00Z, −1.29R / −$201.55)** |
| Entries this wake | 0 (midday is position management only) |
| Equity (cash + MTM) | **$10,212.32** |
| Equity peak | $10,875.85 (unchanged; need +$663.53 to retake) |
| Drawdown from peak | **6.10%** |
| Loss streak | 1 trading day (today's −$201.55) |
| Day-to-date realized PnL (2026-06-27 PT) | **−$201.55 / −1.93%** |

## Active kill-switch state

- Daily realized + unrealized 2026-06-27 PT: **−$201.55 / −1.93%** of equity — CLEAR (cap 5%, 3.07pp headroom).
- Consecutive losing trading days: **1** (cap 7, 6 days headroom). CLEAR.
- Max drawdown: **6.10%** from peak $10,875.85 (cap 25%, warn 12.5%, 6.40pp to warn) — CLEAR.
- Equity floor: $10,212.32 > $7,500 floor — CLEAR.
- MCP availability: Kraken OK (`kraken_ohlcv` returned 50 1H SOL bars cleanly; `kraken_multi_ticker` rejected `SOLUSD` symbol, accepted `SOL/USD` form — convention noted). CLEAR.
- Regime gate (rule 5a): **PASS** (per overnight read 14/15 positive median +1.60%). Midday is position management only — regime not re-scored this wake.
- Regime sub-state (rule 5a-SBD): **CLEAR** (per overnight).
- Active 5b cooldowns: **SOL/USD — 24h cooldown active until 2026-06-28T19:00Z** (just stopped out this wake).
- Cluster cap (rule 6a, BTC-cluster): **0/2** used. Full headroom.
- Watchdog: not re-run this wake (midday lean budget); routine-07 staleness carry-over from earlier (routine-04 territory).
- **All Ring 3 kill switches CLEAR.** Routine-02-midday 2026-06-27T21:30Z (OFF-schedule Saturday fire): **1 exit, 0 entries**.

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

(none — flat)

Next entry-eligible scan: routine-03-eod (PT Sat 2026-06-27 ~21:00 = Sun 04:00Z). SOL/USD specifically blocked by 5b re-entry cooldown until 2026-06-28T19:00Z.

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | ≈ −2.0% (today's −$201.55 SOL stop reverses prior week's +$182 SOL winner; net 7d slightly negative) | ≈ −6.6% (BTC ~$65k → $60.74k) | ≈ +4.6% | BULL ahead 7d |
| 30d | ≈ +2.12% (inception $10k 2026-04-20; equity $10,212.32 mark) | ≈ −22.2% (BTC 30d ago ~$78k → today $60.74k) | ≈ +24.3% | BULL well ahead |
| 90d | — | — | — | not computable (BULL inception 2026-04-20 = 68 days ago; window first computable ~2026-07-19) |

(7d/30d figures approximate. SOL stop today erases the recent +$182 SOL win plus more — net SOL P&L across 2026-06-20 → 06-27 cycle: +$182 − $201 = −$19. Two consecutive same-pair stops within a week — pattern worth flagging in lessons if it repeats next cycle.)
