# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-05-04T20:00:00Z (routine-02-midday — LINK MTM @ 9.38328; no exits, no entries).

## Account

- Starting equity: **$10,000.00**
- Cash: **$7,280.49**  *(unchanged since LINK open 19:00Z; no exits this wake)*
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
- Unrealized PnL: **−$20.71**  *(LINK MTM 257×9.38328 = $2,411.50; cost 257×9.4393 + comm $6.31 = $2,432.21)*
- Position values (MTM): **$2,411.50**
- Current equity (cash + positions MTM): **$9,691.99**
- Equity peak: **$10,027.55** (set 2026-04-24 midday)
- Drawdown from peak: **3.35%**

## Open positions

| Pair | Side | Size | Entry | Stop | Entry time | Stop dist | Risk USD | Risk % | Cluster |
|------|------|------|-------|------|------------|-----------|----------|--------|---------|
| LINK/USD | long | 257 | 9.4393 | 9.2018 | 2026-05-04T19:00Z | 0.2375 | $61.04 | 0.63% | yes (BTC-corr) |

Portfolio risk-at-moment: **0.63%** (cap 4%).
Open positions: **1 / 8** (strategy v0.2 max-concurrent 4 → 1/4 used; cluster cap 1/2).

## Active kill-switch state

- Daily realized: **0.00%** today 2026-05-04 (cap 5%) — no closes today
- Daily realized + unrealized: **−0.21%** today (cap 5%) — LINK unrealized −$20.71 vs pre-entry equity $9,712.70
- Consecutive losing trading days: 04-24 L, 04-25 L, 04-26 flat, 04-27 L, 04-28 flat, 04-29 L, 04-30 flat, 05-01 flat, 05-02 flat, 05-03 flat, 05-04 open → not 7-in-a-row (cap 7)
- Max drawdown: 3.35% (cap 25%, warn 12.5%) — clear
- Equity floor: $9,691.99 > $7,500 floor — OK
- **All clear. Trading authorized.**

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | — | — | — | — |
| 30d | — | — | — | — |
| 90d | — | — | — | — |

(Populated once a 7-day window has closed.)
