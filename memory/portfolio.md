# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-05-07T20:00:00Z (routine-02-midday 5/7 — LINK ema-cross exit at 19:00Z close 9.8954 (fill 9.890452), +1.69R / +$103.03; 0 open positions; flat).

## Account

- Starting equity: **$10,000.00**
- Cash: **$9,672.70**
- Realized PnL (all-time): **−$327.25**
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
- Unrealized PnL: **$0.00**
- Position values (MTM): **$0.00**
- Current equity (cash + positions MTM): **$9,672.70**
- Equity peak: **$10,027.55** (set 2026-04-24 midday)
- Drawdown from peak: **3.54%**

## Open positions

(none — flat)

Portfolio risk-at-moment: **0.00%** (cap 4%).
Open positions: **0 / 8** (strategy v0.2 max-concurrent 4 → 0/4 used; cluster 0/2; non-cluster 0).

## Active kill-switch state

- Daily realized: **+$65.35** today 2026-05-07 PT (XRP −$37.68 + LINK +$103.03) → +0.67% on day-start equity ~$9,704.39 (cap 5%)
- Daily realized + unrealized: +0.67% today — well within 5% cap
- Consecutive losing trading days: 04-24 L, 04-25 L, 04-26 flat, 04-27 L, 04-28 flat, 04-29 L, 04-30..05-05 flat, 05-06 L, 05-07 W (LINK +1.69R outweighs XRP −1.05R) → reset to 0 (cap 7)
- Max drawdown: 3.54% (cap 25%, warn 12.5%) — clear
- Equity floor: $9,672.70 > $7,500 floor — OK
- **All clear. Trading authorized.**

## Pending exit triggers

(none — flat)

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | — | — | — | — |
| 30d | — | — | — | — |
| 90d | — | — | — | — |

(Populated once a 7-day window has closed.)
