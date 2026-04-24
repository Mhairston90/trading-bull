# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-04-24T13:00:00Z (routine-01-overnight — BTC EMA-cross exit, ADA entry; TRX close already booked by midday).

## Account

- Starting equity: **$10,000.00**
- Cash: **$4,950.36**
  - Opening 2026-04-24: $2,483.57
  - +BTC close proceeds @ 04:00: +$2,496.10
  - −ADA open outflow @ 17:00: −$2,509.18
  - +TRX close proceeds @ 20:00: +$2,479.87
- Realized PnL (all-time): **−$35.83** (−$26.69 TRX + −$9.14 BTC)
- Unrealized PnL (mark-to-market):
  - LTC @ last 56.63: 45.2 × (56.63 − 55.27) = **+$61.47**
  - ADA @ last 0.252128: 9934 × (0.252128 − 0.251930) = **+$1.97**
  - Total unrealized: **+$63.44**
- Position values (mark-to-market):
  - LTC: 45.2 × 56.63 = **$2,559.68**
  - ADA: 9934 × 0.252128 = **$2,504.64**
  - Total: **$5,064.32**
- Current equity (cash + positions MTM): **$4,950.36 + $5,064.32 = $10,014.68**
- Equity peak: **$10,027.55** (set 2026-04-24 midday)
- Drawdown from peak: **0.13%**

## Open positions

| Pair | Side | Size | Entry | Stop | Target (static) | Risk at open | R-at-stop | MTM |
|------|------|------|-------|------|-----------------|--------------|-----------|-----|
| LTC/USD | long | 45.2 | 55.27 | 54.61 | — (4R exit rule dynamic) | $29.83 (0.30%) | −1R | 56.63 |
| ADA/USD | long | 9934 | 0.251930 | 0.248716 | — (4R exit rule dynamic) | $31.93 (0.32%) | −1R | 0.252128 |

Portfolio risk-at-moment: $61.76 / $10,014.68 = **0.62%** (cap 4%).

## Active kill-switch state

- Daily loss: realized −0.36% + unrealized +0.63% = net +0.28% (cap 5%)
- Consecutive losing days: 0 (cap 7)
- Max drawdown: 0.13% (cap 25%)
- Equity floor: $10,014.68 > $7,500 floor — OK
- **All clear. Trading authorized.**

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | — | — | — | — |
| 30d | — | — | — | — |
| 90d | — | — | — | — |

(Populated once a 7-day window has closed.)
