# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-04-22T04:10:00Z (routine-01-overnight — 1 new entry: BTC/USD).

## Account

- Starting equity: **$10,000.00**
- Cash: **$2,483.57** (= $4,988.80 − $2,498.73 BTC notional − $6.50 entry commission @ 0.26%)
- Realized PnL (all-time): **$0.00**
- Unrealized PnL (mark-to-market):
  - TRX @ last 0.332107: 7531 × (0.332107 − 0.331943) = **+$1.23**
  - LTC @ last 55.96: 45.2 × (55.96 − 55.27) = **+$31.19**
  - BTC @ last 77600.0: 0.0322 × (77600.0 − 77600.4) = **−$0.01**
  - Total unrealized: **+$32.41**
- Position values (mark-to-market):
  - TRX: 7531 × 0.332107 = **$2,501.10**
  - LTC: 45.2 × 55.96 = **$2,529.39**
  - BTC: 0.0322 × 77600.0 = **$2,498.72**
  - Total: **$7,529.21**
- Current equity (cash + positions MTM): **$2,483.57 + $7,529.21 = $10,012.78**
- Equity peak: **$10,016.92** (set 2026-04-22 midday)
- Drawdown from peak: **0.04%**

## Open positions

| Pair | Side | Size | Entry | Stop | Target (static) | Risk at open | R-at-stop | MTM |
|------|------|------|-------|------|-----------------|--------------|-----------|-----|
| TRX/USD | long | 7531 | 0.331943 | 0.330285 | — (4R exit rule dynamic) | $12.49 (0.12%) | −1R | 0.332107 |
| LTC/USD | long | 45.2 | 55.27 | 54.61 | — (4R exit rule dynamic) | $29.83 (0.30%) | −1R | 55.96 |
| BTC/USD | long | 0.0322 | 77600.4 | 76454.3 | — (4R exit rule dynamic) | $36.90 (0.37%) | −1R | 77600.0 |

Portfolio risk-at-moment: $79.22 / $10,012.78 = **0.79%** (cap 4%).

## Active kill-switch state

- Daily loss: 0.00% (cap 5%) — position is net positive
- Consecutive losing days: 0 (cap 7)
- Max drawdown: 0.04% (cap 25%)
- Equity floor: $10,012.78 > $7,500 floor — OK
- **All clear. Trading authorized.**

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | — | — | — | — |
| 30d | — | — | — | — |
| 90d | — | — | — | — |

(Populated once a 7-day window has closed.)
