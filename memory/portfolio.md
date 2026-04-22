# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-04-22T03:00:00Z (routine-02-midday — mark-to-market, no exits).

## Account

- Starting equity: **$10,000.00**
- Cash: **$4,988.80** (= $7,493.50 − $2,498.20 LTC notional − $6.50 entry commission @ 0.26%)
- Realized PnL (all-time): **$0.00**
- Unrealized PnL (mark-to-market):
  - TRX @ last 0.332272: 7531 × (0.332272 − 0.331943) = **+$2.48**
  - LTC @ last 55.88: 45.2 × (55.88 − 55.27) = **+$27.57**
  - Total unrealized: **+$30.05**
- Position values (mark-to-market):
  - TRX: 7531 × 0.332272 = **$2,502.34**
  - LTC: 45.2 × 55.88 = **$2,525.78**
  - Total: **$5,028.12**
- Current equity (cash + positions MTM): **$4,988.80 + $5,028.12 = $10,016.92**
- Equity peak: **$10,016.92** (new peak this wake)
- Drawdown from peak: **0.00%**

## Open positions

| Pair | Side | Size | Entry | Stop | Target (static) | Risk at open | R-at-stop | MTM |
|------|------|------|-------|------|-----------------|--------------|-----------|-----|
| TRX/USD | long | 7531 | 0.331943 | 0.330285 | — (4R exit rule dynamic) | $12.48 (0.12%) | −1R | 0.332272 |
| LTC/USD | long | 45.2 | 55.27 | 54.61 | — (4R exit rule dynamic) | $29.83 (0.30%) | −1R | 55.88 |

Portfolio risk-at-moment: $42.31 / $10,016.92 = **0.42%** (cap 4%).

## Active kill-switch state

- Daily loss: 0.00% (cap 5%) — position is net positive
- Consecutive losing days: 0 (cap 7)
- Max drawdown: 0.00% (cap 25%)
- Equity floor: $10,016.92 > $7,500 floor — OK
- **All clear. Trading authorized.**

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | — | — | — | — |
| 30d | — | — | — | — |
| 90d | — | — | — | — |

(Populated once a 7-day window has closed.)
