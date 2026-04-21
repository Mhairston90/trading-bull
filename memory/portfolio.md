# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-04-21T18:05:00Z (routine-01-overnight — opened TRX/USD long).

## Account

- Starting equity: **$10,000.00**
- Cash: **$7,493.50** (= $10,000 − $2,500 notional − $6.50 entry commission @ 0.26%)
- Realized PnL (all-time): **$0.00**
- Unrealized PnL (mark-to-market @ TRX last 0.332086): 7531 × (0.332086 − 0.331943) = **+$1.08**
- Position value (mark-to-market): 7531 × 0.332086 = **$2,500.94**
- Current equity (cash + position MTM): **$9,993.50 + $1.08 = $9,994.58** (net of one-side entry fee)
- Equity peak: **$10,000.00**
- Drawdown from peak: **0.05%**

## Open positions

| Pair | Side | Size | Entry | Stop | Target (static) | Risk at open | R-at-stop | MTM |
|------|------|------|-------|------|-----------------|--------------|-----------|-----|
| TRX/USD | long | 7531 | 0.331943 | 0.330285 | — (4R exit rule dynamic) | $12.49 (0.12%) | −1R | 0.332086 |

## Active kill-switch state

- Daily loss: 0.05% (cap 5%)
- Consecutive losing days: 0 (cap 7)
- Max drawdown: 0.05% (cap 25%)
- Equity floor: $9,994.58 > $7,500 floor — OK
- **All clear. Trading authorized.**

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | — | — | — | — |
| 30d | — | — | — | — |
| 90d | — | — | — | — |

(Populated once a 7-day window has closed.)
