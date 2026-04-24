# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-04-24T20:10:00Z (routine-02-midday — MTM refresh at 20:06Z; no exits, no entries by design).

## Account

- Starting equity: **$10,000.00**
- Cash: **$2,448.97** (unchanged)
- Realized PnL (all-time): **−$35.83** (−$26.69 TRX + −$9.14 BTC)
- Unrealized PnL (mark-to-market, ticker @ 20:06Z):
  - LTC @ 56.72: 45.2 × (56.72 − 55.27) = **+$65.54**
  - ADA @ 0.251958: 9934 × (0.251958 − 0.251930) = **+$0.28**
  - AVAX @ 9.44: 265 × (9.44 − 9.4147) = **+$6.70**
  - Total unrealized: **+$72.52**
- Position values (mark-to-market):
  - LTC: 45.2 × 56.72 = **$2,563.74**
  - ADA: 9934 × 0.251958 = **$2,502.95**
  - AVAX: 265 × 9.44 = **$2,501.60**
  - Total: **$7,568.29**
- Current equity (cash + positions MTM): **$2,448.97 + $7,568.29 = $10,017.26**
- Equity peak: **$10,027.55** (set 2026-04-24 midday)
- Drawdown from peak: **0.10%**

## Open positions

| Pair | Side | Size | Entry | Stop | Target (static) | Risk at open | R-at-stop | MTM |
|------|------|------|-------|------|-----------------|--------------|-----------|-----|
| LTC/USD | long | 45.2 | 55.27 | 54.61 | — (4R exit rule dynamic) | $29.83 (0.30%) | −1R | 56.72 |
| ADA/USD | long | 9934 | 0.251930 | 0.248716 | — (4R exit rule dynamic) | $31.93 (0.32%) | −1R | 0.251958 |
| AVAX/USD | long | 265 | 9.4147 | 9.2847 | — (4R exit rule dynamic) | $34.45 (0.34%) | −1R | 9.44 |

Portfolio risk-at-moment: $29.83 + $31.93 + $34.45 = $96.21 / $10,017.26 = **0.96%** (cap 4%).

## Active kill-switch state

- Daily loss: realized −0.36% + unrealized +0.72% = net +0.37% (cap 5%)
- Consecutive losing days: 0 (cap 7)
- Max drawdown: 0.10% (cap 25%, warn 12.5%)
- Equity floor: $10,017.26 > $7,500 floor — OK
- **All clear. Trading authorized.**

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | — | — | — | — |
| 30d | — | — | — | — |
| 90d | — | — | — | — |

(Populated once a 7-day window has closed.)
