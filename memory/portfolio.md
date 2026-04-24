# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-04-24T20:00:00Z (routine-02-midday — TRX stopped out intrabar).

## Account

- Starting equity: **$10,000.00**
- Cash: **$4,963.44** (= $2,483.57 + TRX close proceeds $2,479.87)
- Realized PnL (all-time): **−$26.69** (TRX stop-out)
- Unrealized PnL (mark-to-market):
  - LTC @ last 56.63: 45.2 × (56.63 − 55.27) = **+$61.47**
  - BTC @ last 77777.5: 0.0322 × (77777.5 − 77600.4) = **+$5.70**
  - Total unrealized: **+$67.17**
- Position values (mark-to-market):
  - LTC: 45.2 × 56.63 = **$2,559.68**
  - BTC: 0.0322 × 77777.5 = **$2,504.43**
  - Total: **$5,064.11**
- Current equity (cash + positions MTM): **$4,963.44 + $5,064.11 = $10,027.55**
- Equity peak: **$10,027.55** (new peak set 2026-04-24 midday)
- Drawdown from peak: **0.00%**

## Open positions

| Pair | Side | Size | Entry | Stop | Target (static) | Risk at open | R-at-stop | MTM |
|------|------|------|-------|------|-----------------|--------------|-----------|-----|
| LTC/USD | long | 45.2 | 55.27 | 54.61 | — (4R exit rule dynamic) | $29.83 (0.30%) | −1R | 56.63 |
| BTC/USD | long | 0.0322 | 77600.4 | 76454.3 | — (4R exit rule dynamic) | $36.90 (0.37%) | −1R | 77777.5 |

Portfolio risk-at-moment: $66.73 / $10,027.55 = **0.67%** (cap 4%).

## Active kill-switch state

- Daily loss: realized −0.27% + unrealized +0.67% = net +0.40% (cap 5%)
- Consecutive losing days: 0 (cap 7)
- Max drawdown: 0.00% (cap 25%)
- Equity floor: $10,027.55 > $7,500 floor — OK
- **All clear. Trading authorized.**

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | — | — | — | — |
| 30d | — | — | — | — |
| 90d | — | — | — | — |

(Populated once a 7-day window has closed.)
