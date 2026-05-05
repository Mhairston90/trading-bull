# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-05-05T05:00:00Z (routine-01-overnight EOD pass — BTC OPEN @ 80961.16, size 0.0299; LINK MTM held).

## Account

- Starting equity: **$10,000.00**
- Cash: **$4,853.46**  *(was $7,280.49; BTC notional $2,420.74 + entry comm $6.29 = $2,427.03 deducted)*
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
- Unrealized PnL: **+$31.07**
  - LINK: 257 × 9.56418 = $2,457.99 MTM; cost 257×9.4393 + comm $6.31 = $2,432.21 → +$25.78
  - BTC: 0.0299 × 80920.7 = $2,419.53 MTM; cost 0.0299×80961.16 + comm $6.29 = $2,427.03 → −$7.50 (slip + entry comm)
- Position values (MTM): **$4,877.52**
- Current equity (cash + positions MTM): **$9,730.98**
- Equity peak: **$10,027.55** (set 2026-04-24 midday)
- Drawdown from peak: **2.96%**

## Open positions

| Pair | Side | Size | Entry | Stop | Entry time | Stop dist | Risk USD | Risk % | Cluster |
|------|------|------|-------|------|------------|-----------|----------|--------|---------|
| LINK/USD | long | 257 | 9.4393 | 9.2018 | 2026-05-04T19:00Z | 0.2375 | $61.04 | 0.63% | yes (BTC-corr) |
| BTC/USD | long | 0.0299 | 80961.16 | 80124.19 | 2026-05-05T05:00Z | 836.97 | $25.02 | 0.26% | yes (BTC-corr) |

Portfolio risk-at-moment: **0.89%** (cap 4%).
Open positions: **2 / 8** (strategy v0.2 max-concurrent 4 → 2/4 used; cluster cap 2/2 — at limit).

## Active kill-switch state

- Daily realized: **0.00%** today 2026-05-04 (cap 5%) — no closes today
- Daily realized + unrealized: **+0.20%** today (cap 5%) — combined unrealized +$31.07 vs pre-entry equity ~$9,712.70 (LINK +$25.78, BTC −$7.50 fresh slip)
- Consecutive losing trading days: 04-24 L, 04-25 L, 04-26 flat, 04-27 L, 04-28 flat, 04-29 L, 04-30 flat, 05-01 flat, 05-02 flat, 05-03 flat, 05-04 open → not 7-in-a-row (cap 7)
- Max drawdown: 2.96% (cap 25%, warn 12.5%) — clear
- Equity floor: $9,730.98 > $7,500 floor — OK
- **All clear. Trading authorized.**

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | — | — | — | — |
| 30d | — | — | — | — |
| 90d | — | — | — | — |

(Populated once a 7-day window has closed.)
