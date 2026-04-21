# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-04-21T20:05:00Z (routine-01-overnight — opened LTC/USD long).

## Account

- Starting equity: **$10,000.00**
- Cash: **$4,988.80** (= $7,493.50 − $2,498.20 LTC notional − $6.50 entry commission @ 0.26%)
- Realized PnL (all-time): **$0.00**
- Unrealized PnL (mark-to-market):
  - TRX @ last 0.333177: 7531 × (0.333177 − 0.331943) = **+$9.29**
  - LTC @ last 55.24: 45.2 × (55.24 − 55.27) = **−$1.36**
  - Total unrealized: **+$7.93**
- Position values (mark-to-market):
  - TRX: 7531 × 0.333177 = **$2,509.14**
  - LTC: 45.2 × 55.24 = **$2,496.85**
  - Total: **$5,005.99**
- Current equity (cash + positions MTM): **$4,988.80 + $5,005.99 = $9,994.79**
- Equity peak: **$10,000.00**
- Drawdown from peak: **0.05%**

## Open positions

| Pair | Side | Size | Entry | Stop | Target (static) | Risk at open | R-at-stop | MTM |
|------|------|------|-------|------|-----------------|--------------|-----------|-----|
| TRX/USD | long | 7531 | 0.331943 | 0.330285 | — (4R exit rule dynamic) | $12.48 (0.12%) | −1R | 0.333177 |
| LTC/USD | long | 45.2 | 55.27 | 54.61 | — (4R exit rule dynamic) | $29.83 (0.30%) | −1R | 55.24 |

Portfolio risk-at-moment: $42.31 / $9,994.79 = **0.42%** (cap 4%).

## Active kill-switch state

- Daily loss: 0.05% (cap 5%)
- Consecutive losing days: 0 (cap 7)
- Max drawdown: 0.05% (cap 25%)
- Equity floor: $9,994.79 > $7,500 floor — OK
- **All clear. Trading authorized.**

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | — | — | — | — |
| 30d | — | — | — | — |
| 90d | — | — | — | — |

(Populated once a 7-day window has closed.)
