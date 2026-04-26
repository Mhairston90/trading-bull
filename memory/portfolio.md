# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-04-26T21:13:00Z (routine-01-overnight — 3 OPENs (ETH, BTC, SOL), 0 CLOSEs, 0 ACTIONABLE news, all kill switches clear).

## Account

- Starting equity: **$10,000.00**
- Cash: **$2,465.49**
- Realized PnL (all-time): **−$69.24**
  - BTC −$9.14 (exit-ema-cross 2026-04-24T04:00Z)
  - TRX −$26.69 (exit-stop-hit 2026-04-24T20:00Z)
  - LTC +$39.40 (exit-ema-cross 2026-04-25T17:00Z, +1.32R)
  - ADA −$38.77 (exit-ema-cross 2026-04-25T17:00Z, −1.21R)
  - AVAX −$34.04 (exit-ema-cross 2026-04-25T17:00Z, −0.99R)
- Unrealized PnL: **−$10.14** (entry slippage + commission drag on 3 fresh fills, partly offset by favorable post-fill drift)
- Position values (MTM @ live quote): **$7,455.13**
- Current equity (cash + positions MTM): **$9,920.62**
- Equity peak: **$10,027.55** (set 2026-04-24 midday)
- Drawdown from peak: **1.07%**

## Open positions

| Pair | Side | Size | Entry | Stop | MTM @ last | Unreal PnL (gross) | Risk-at-moment |
|------|------|-----:|------:|-----:|-----------:|-------------------:|---------------:|
| ETH/USD | long | 1.0499 | 2364.72 | 2345.10 | 2367.01 | +$2.40 | 0.21% |
| BTC/USD | long | 0.0317 | 78266.21 | 77803.14 | 78273.10 | +$0.22 | 0.15% |
| SOL/USD | long | 28.6 | 86.79 | 86.10 | 87.02 | +$6.58 | 0.20% |

Portfolio risk-at-moment: **0.56%** (cap 4%).
Open positions: **3 / 8** (strategy v0 max-concurrent 4).

## Active kill-switch state

- Daily realized: −$33.41 / −0.33% today (cap 5%)
- Consecutive losing days: tracking
- Max drawdown: 1.07% (cap 25%, warn 12.5%)
- Equity floor: $9,920.62 > $7,500 floor — OK
- **All clear. Trading authorized.**

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | — | — | — | — |
| 30d | — | — | — | — |
| 90d | — | — | — | — |

(Populated once a 7-day window has closed.)
