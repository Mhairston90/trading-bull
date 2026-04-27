# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-04-27T04:10:00Z (routine-01-overnight — 1 OPEN (TAO), 0 CLOSE, 0 ACTIONABLE news, all kill switches clear).

## Account

- Starting equity: **$10,000.00**
- Cash: **$5.73**
- Realized PnL (all-time): **−$69.24**
  - BTC −$9.14 (exit-ema-cross 2026-04-24T04:00Z)
  - TRX −$26.69 (exit-stop-hit 2026-04-24T20:00Z)
  - LTC +$39.40 (exit-ema-cross 2026-04-25T17:00Z, +1.32R)
  - ADA −$38.77 (exit-ema-cross 2026-04-25T17:00Z, −1.21R)
  - AVAX −$34.04 (exit-ema-cross 2026-04-25T17:00Z, −0.99R)
- Unrealized PnL: **+$57.87** (3 prior fills now in profit on overnight rally; TAO fresh entry has slight commission drag)
- Position values (MTM @ live quote): **$9,982.90**
- Current equity (cash + positions MTM): **$9,988.63**
- Equity peak: **$10,027.55** (set 2026-04-24 midday)
- Drawdown from peak: **0.39%**

## Open positions

| Pair | Side | Size | Entry | Stop | MTM @ last | Unreal PnL (gross) | Risk-at-moment |
|------|------|-----:|------:|-----:|-----------:|-------------------:|---------------:|
| ETH/USD | long | 1.0499 | 2364.72 | 2345.10 | 2393.14 | +$29.84 | 0.21% |
| BTC/USD | long | 0.0317 | 78266.21 | 77803.14 | 79094.60 | +$26.26 | 0.15% |
| SOL/USD | long | 28.6 | 86.79 | 86.10 | 87.72 | +$26.60 | 0.20% |
| TAO/USD | long | 9.6 | 255.56 | 251.12 | 255.62 | +$0.58 | 0.43% |

Portfolio risk-at-moment: **0.99%** (cap 4%).
Open positions: **4 / 8** (strategy v0 max-concurrent 4 — at cap).

## Active kill-switch state

- Daily realized: 0.00% today (cap 5%) — no closes this wake
- Consecutive losing days: tracking
- Max drawdown: 0.39% (cap 25%, warn 12.5%)
- Equity floor: $9,988.63 > $7,500 floor — OK
- **All clear. Trading authorized.**

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | — | — | — | — |
| 30d | — | — | — | — |
| 90d | — | — | — | — |

(Populated once a 7-day window has closed.)
