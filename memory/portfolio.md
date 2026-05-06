# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-05-06T16:30:00Z (routine-01-overnight 5/6 wake — HYPE stopped out (-1.02R, -$58.18) at 15:00Z bar; opened LTC/USD; 4 OPEN positions; max-concurrent 4/4).

## Account

- Starting equity: **$10,000.00**
- Cash: **$13.17**
- Realized PnL (all-time): **−$345.44**
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
- Unrealized PnL: **+$173.63**
  - LINK: 257 × 10.02422 = $2,576.22 MTM; cost 257×9.4393 + comm $6.31 = $2,432.21 → **+$144.01**
  - BTC: 0.0299 × 81600.0 = $2,439.84 MTM; cost 0.0299×80961.16 + comm $6.29 = $2,427.03 → **+$12.81**
  - XRP: 1723 × 1.42743 = $2,459.46 MTM; cost 1723×1.40857 + comm $6.31 = $2,433.28 → **+$26.18**
  - LTC: 41 × 57.06 = $2,339.46 MTM; cost 41×57.14 + comm $6.09 = $2,348.83 → **−$9.37**
- Position values (MTM): **$9,814.98**
- Current equity (cash + positions MTM): **$9,828.15**
- Equity peak: **$10,027.55** (set 2026-04-24 midday)
- Drawdown from peak: **1.99%**

## Open positions

| Pair | Side | Size | Entry | Stop | Entry time | Stop dist | Risk USD | Risk % | Cluster |
|------|------|------|-------|------|------------|-----------|----------|--------|---------|
| LINK/USD | long | 257 | 9.4393 | 9.2018 | 2026-05-04T19:00Z | 0.2375 | $61.04 | 0.621% | yes (BTC-corr) |
| BTC/USD | long | 0.0299 | 80961.16 | 80124.19 | 2026-05-05T05:00Z | 836.97 | $25.02 | 0.255% | yes (BTC-corr) |
| XRP/USD | long | 1723 | 1.40857 | 1.39468 | 2026-05-05T17:00Z | 0.01389 | $23.93 | 0.244% | no |
| LTC/USD | long | 41 | 57.14 | 56.28 | 2026-05-06T15:00Z | 0.86 | $35.26 | 0.359% | no |

Portfolio risk-at-moment: **1.48%** (cap 4%).
Open positions: **4 / 8** (strategy v0.2 max-concurrent 4 → 4/4 used **AT LIMIT**; cluster cap 2/2 — at limit; non-cluster 2 = XRP + LTC).

## Active kill-switch state

- Daily realized: **−0.60%** today 2026-05-06 (cap 5%) — HYPE stop-out −$58.18 / starting equity baseline $9,712.74 (post-prior-realized)
- Daily realized + unrealized: combined approx +1.18% today (−$58.18 realized + $173.63 unrealized = $115.45 / $9,712.74) — well within 5% cap
- Consecutive losing trading days: 04-24 L, 04-25 L, 04-26 flat, 04-27 L, 04-28 flat, 04-29 L, 04-30 flat, 05-01 flat, 05-02 flat, 05-03 flat, 05-04 flat, 05-05 flat, 05-06 L (HYPE stop) → not 7-in-a-row (cap 7)
- Max drawdown: 1.99% (cap 25%, warn 12.5%) — clear
- Equity floor: $9,828.15 > $7,500 floor — OK
- **All clear. Trading authorized.**

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | — | — | — | — |
| 30d | — | — | — | — |
| 90d | — | — | — | — |

(Populated once a 7-day window has closed.)
