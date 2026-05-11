# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-05-11T20:00:00Z (routine-02-midday — SOL/USD 4R take-profit closed at 19:00Z 1H candle close, fill 98.1509, +4.03R, +$585.35 realized; portfolio flat).

## Account

- Starting equity: **$10,000.00**
- Cash: **$10,258.06**
- Realized PnL (all-time): **+$258.10**
  - BTC −$9.14 (exit-ema-cross 2026-04-24T04:00Z)
  - TRX −$26.69 (exit-stop-hit 2026-04-24T20:00Z)
  - LTC +$39.40 (exit-ema-cross 2026-04-25T17:00Z, +1.32R)
  - ADA −$38.77 (exit-ema-cross 2026-04-25T17:00Z, −1.21R)
  - AVAX −$34.04 (exit-ema-cross 2026-04-25T17:00Z, −0.99R)
  - ETH −$34.68 (exit-stop-hit 2026-04-27T05:00Z, −1.06R)
  - BTC −$28.77 (exit-stop-hit 2026-04-27T05:00Z, −1.08R)
  - SOL −$33.82 (exit-stop-hit 2026-04-27T05:00Z, −1.06R)
  - TAO −$56.38 (exit-stop-hit 2026-04-27T05:00Z, −1.03R)
  - TAO −$64.37 (exit-stop-hit 2026-04-29T14:00Z, −1.02R)
  - HYPE −$58.18 (exit-stop-hit 2026-05-06T15:00Z, −1.02R)
  - BTC +$1.42 (exit-ema-cross 2026-05-06T19:00Z, +0.06R)
  - LTC −$48.58 (exit-stop-hit 2026-05-07T01:00Z, −1.03R)
  - XRP −$37.68 (exit-stop-hit 2026-05-07T14:00Z, −1.05R)
  - LINK +$103.03 (exit-ema-cross 2026-05-07T20:00Z, +1.69R)
  - SOL +$585.35 (exit-4R-target 2026-05-11T19:00Z, +4.03R)
- Unrealized PnL: **$0.00** (no open positions)
- Position values (MTM): **$0.00**
- Current equity (cash + positions MTM): **$10,258.06**
- Equity peak: **$10,258.06** (set 2026-05-11 midday at 4R take-profit on SOL)
- Drawdown from peak: **0.00%**

## Open positions

(none)

Portfolio risk-at-moment: **0.00%** (cap 4%).
Open positions: **0 / 8** (strategy v0.2 max-concurrent 4 → 0/4 used; cluster {BTC,ETH,SOL,TAO,AVAX,SUI,LINK} 0/2; non-cluster 0).

## Active kill-switch state

- Daily realized: **+$585.35 (+5.86% of pre-trade equity $9,672.71 since 4/21 start; +5.71% of fresh equity $10,258.06)** today 2026-05-11 PT — a gain, well within the 5% LOSS cap (kill switch is loss-side only)
- Consecutive losing trading days: ... 05-06 L, 05-07 W, 05-11 W → streak reset to 0 (cap 7)
- Max drawdown: 0.00% (cap 25%, warn 12.5%) — clear, new peak set
- Equity floor: $10,258.06 > $7,500 floor — OK
- **All clear. Trading authorized.** (No entries this wake — midday is position-management only per routine-02 mandate.)

## Pending exit triggers

(none — flat)

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | — | — | — | — |
| 30d | — | — | — | — |
| 90d | — | — | — | — |

(Populated once a 7-day window has closed.)
