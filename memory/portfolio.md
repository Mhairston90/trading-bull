# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-05-06T20:00:00Z (routine-02-midday 5/6 wake — BTC exited via exit-ema-cross at 19:00Z close (+0.06R, +$1.42); 3 OPEN positions remaining).

## Account

- Starting equity: **$10,000.00**
- Cash: **$2,441.62**
- Realized PnL (all-time): **−$344.02**
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
- Unrealized PnL: **+$163.71**
  - LINK: 257 × 10.03964 = $2,580.19 MTM; cost 257×9.4393 + comm $6.31 = $2,432.21 → **+$147.98**
  - XRP: 1723 × 1.42786 = $2,460.20 MTM; cost 1723×1.40857 + comm $6.31 = $2,433.28 → **+$26.92**
  - LTC: 41 × 57.04 = $2,338.64 MTM; cost 41×57.14 + comm $6.09 = $2,348.83 → **−$10.19**
- Position values (MTM): **$7,379.03**
- Current equity (cash + positions MTM): **$9,820.65**
- Equity peak: **$10,027.55** (set 2026-04-24 midday)
- Drawdown from peak: **2.06%**

## Open positions

| Pair | Side | Size | Entry | Stop | Entry time | Stop dist | Risk USD | Risk % | Cluster |
|------|------|------|-------|------|------------|-----------|----------|--------|---------|
| LINK/USD | long | 257 | 9.4393 | 9.2018 | 2026-05-04T19:00Z | 0.2375 | $61.04 | 0.621% | yes (BTC-corr) |
| XRP/USD | long | 1723 | 1.40857 | 1.39468 | 2026-05-05T17:00Z | 0.01389 | $23.93 | 0.244% | no |
| LTC/USD | long | 41 | 57.14 | 56.28 | 2026-05-06T15:00Z | 0.86 | $35.26 | 0.359% | no |

Portfolio risk-at-moment: **1.22%** (cap 4%).
Open positions: **3 / 8** (strategy v0.2 max-concurrent 4 → 3/4 used; cluster cap 1/2; non-cluster 2 = XRP + LTC).

## Active kill-switch state

- Daily realized: **−0.58%** today 2026-05-06 (cap 5%) — HYPE −$58.18 + BTC +$1.42 = −$56.76 / starting equity baseline $9,712.74 (post-prior-realized)
- Daily realized + unrealized: combined approx +1.10% today (−$56.76 realized + $163.71 unrealized = $106.95 / $9,712.74) — well within 5% cap
- Consecutive losing trading days: 04-24 L, 04-25 L, 04-26 flat, 04-27 L, 04-28 flat, 04-29 L, 04-30 flat, 05-01 flat, 05-02 flat, 05-03 flat, 05-04 flat, 05-05 flat, 05-06 L (HYPE stop − net of BTC +0.06R) → not 7-in-a-row (cap 7)
- Max drawdown: 2.06% (cap 25%, warn 12.5%) — clear
- Equity floor: $9,820.65 > $7,500 floor — OK
- **All clear. Trading authorized.**

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | — | — | — | — |
| 30d | — | — | — | — |
| 90d | — | — | — | — |

(Populated once a 7-day window has closed.)
