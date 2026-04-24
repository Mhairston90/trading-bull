# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-04-25T00:20:00Z (routine-02-midday — fresh MTM, no exits).

## Account

- Starting equity: **$10,000.00**
- Cash: **$2,448.97** (unchanged from prior wake — no exits, no entries midday)
- Realized PnL (all-time): **−$35.83** (−$26.69 TRX + −$9.14 BTC)
- Unrealized PnL (mark-to-market, live ticker @ 00:20Z):
  - LTC @ 56.59: 45.2 × (56.59 − 55.27) = **+$59.66**
  - ADA @ 0.252045: 9934 × (0.252045 − 0.251930) = **+$1.14**
  - AVAX @ 9.44: 265 × (9.44 − 9.4147) = **+$6.70**
  - Total unrealized: **+$67.50**
- Position values (mark-to-market):
  - LTC: 45.2 × 56.59 = **$2,557.87**
  - ADA: 9934 × 0.252045 = **$2,503.81**
  - AVAX: 265 × 9.44 = **$2,501.60**
  - Total: **$7,563.28**
- Current equity (cash + positions MTM): **$2,448.97 + $7,563.28 = $10,012.25**
- Equity peak: **$10,027.55** (set 2026-04-24 midday)
- Drawdown from peak: **0.15%**

## Open positions

| Pair | Side | Size | Entry | Stop | Target (static) | Risk at open | R-at-stop | MTM |
|------|------|------|-------|------|-----------------|--------------|-----------|-----|
| LTC/USD | long | 45.2 | 55.27 | 54.61 | — (4R exit rule dynamic) | $29.83 (0.30%) | −1R | 56.59 |
| ADA/USD | long | 9934 | 0.251930 | 0.248716 | — (4R exit rule dynamic) | $31.93 (0.32%) | −1R | 0.252045 |
| AVAX/USD | long | 265 | 9.4147 | 9.2847 | — (4R exit rule dynamic) | $34.45 (0.34%) | −1R | 9.44 |

Portfolio risk-at-moment: $29.83 + $31.93 + $34.45 = $96.21 / $10,012.25 = **0.96%** (cap 4%).

## Active kill-switch state

- Daily loss: realized −0.36% + unrealized +0.67% = net +0.31% (cap 5%)
- Consecutive losing days: 0 (cap 7)
- Max drawdown: 0.15% (cap 25%)
- Equity floor: $10,012.25 > $7,500 floor — OK
- **All clear. Trading authorized.**

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | — | — | — | — |
| 30d | — | — | — | — |
| 90d | — | — | — | — |

(Populated once a 7-day window has closed.)
