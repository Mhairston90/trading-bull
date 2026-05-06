# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-05-06T04:11:00Z (routine-01-overnight 5/6 wake — opened HYPE/USD; 4 OPEN positions; max-concurrent 4/4).

## Account

- Starting equity: **$10,000.00**
- Cash: **$28.26**
- Realized PnL (all-time): **−$287.26**
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
- Unrealized PnL: **+$121.91**
  - LINK: 257 × 9.87593 = $2,538.11 MTM; cost 257×9.4393 + comm $6.31 = $2,432.21 → **+$105.90**
  - BTC: 0.0299 × 81543.1 = $2,438.14 MTM; cost 0.0299×80961.16 + comm $6.29 = $2,427.03 → **+$11.11**
  - XRP: 1723 × 1.4215 = $2,449.24 MTM; cost 1723×1.40857 + comm $6.31 = $2,433.28 → **+$15.96**
  - HYPE: 54 × 44.09 = $2,380.86 MTM; cost 54×44.18 + comm $6.20 = $2,391.92 → **−$11.06**
- Position values (MTM): **$9,806.35**
- Current equity (cash + positions MTM): **$9,834.61**
- Equity peak: **$10,027.55** (set 2026-04-24 midday)
- Drawdown from peak: **1.92%**

## Open positions

| Pair | Side | Size | Entry | Stop | Entry time | Stop dist | Risk USD | Risk % | Cluster |
|------|------|------|-------|------|------------|-----------|----------|--------|---------|
| LINK/USD | long | 257 | 9.4393 | 9.2018 | 2026-05-04T19:00Z | 0.2375 | $61.04 | 0.622% | yes (BTC-corr) |
| BTC/USD | long | 0.0299 | 80961.16 | 80124.19 | 2026-05-05T05:00Z | 836.97 | $25.02 | 0.255% | yes (BTC-corr) |
| XRP/USD | long | 1723 | 1.40857 | 1.39468 | 2026-05-05T17:00Z | 0.01389 | $23.93 | 0.244% | no |
| HYPE/USD | long | 54 | 44.18 | 43.35 | 2026-05-06T04:00Z | 0.83 | $44.82 | 0.457% | no |

Portfolio risk-at-moment: **1.58%** (cap 4%).
Open positions: **4 / 8** (strategy v0.2 max-concurrent 4 → 4/4 used **AT LIMIT**; cluster cap 2/2 — at limit; non-cluster 2 = XRP + HYPE).

## Active kill-switch state

- Daily realized: **0.00%** today 2026-05-06 (cap 5%) — no closes today
- Daily realized + unrealized: **+1.26%** today (cap 5%) — combined unrealized +$121.91 vs starting equity baseline $9,712.74 (post-realized)
- Consecutive losing trading days: 04-24 L, 04-25 L, 04-26 flat, 04-27 L, 04-28 flat, 04-29 L, 04-30 flat, 05-01 flat, 05-02 flat, 05-03 flat, 05-04 flat, 05-05 flat (no closes), 05-06 open → not 7-in-a-row (cap 7)
- Max drawdown: 1.92% (cap 25%, warn 12.5%) — clear
- Equity floor: $9,834.61 > $7,500 floor — OK
- **All clear. Trading authorized.**

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | — | — | — | — |
| 30d | — | — | — | — |
| 90d | — | — | — | — |

(Populated once a 7-day window has closed.)
