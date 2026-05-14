# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-05-14T16:00Z (routine-01-overnight — opened XRP/USD long after 14/15 regime breadth recovered; 4H trend filter passed marginally on XRP only; BTC/ETH/SOL/TAO/HYPE all still rejected on 4H close < 50-EMA).

## Account

- Starting equity: **$10,000.00**
- Cash: **$935.19**
- Realized PnL (all-time): **+$258.10**
  - BTC −$9.14 (exit-ema-cross 2026-04-24T04:00Z)
  - TRX −$26.69 (exit-stop-hit 2026-04-24T20:00Z)
  - LTC +$39.40 (exit-ema-cross 2026-04-25T17:00Z, +1.32R)
  - ADA −$38.77 (exit-ema-cross 2026-04-25T17:00Z, −1.21R)
  - AVAX −$34.04 (exit-ema-cross 2026-04-25T17:00Z, −0.99R)
  - ETH −$34.68 (exit-stop-hit 2026-04-27T05:00Z, −1.06R)
  - BTC −$28.77 (exit-stop-hit 2026-04-27T05:00Z, −1.08R)
  - SOL −$33.82 (exit-stop-hit 2026-04-27T05:00Z, −1.06R)
  - TAO −$56.38 (exit-stop-hit 2026-04-27T05:00Z, −1.03R)
  - TAO −$64.37 (exit-stop-hit 2026-04-29T14:00Z, −1.02R)
  - HYPE −$58.18 (exit-stop-hit 2026-05-06T15:00Z, −1.02R)
  - BTC +$1.42 (exit-ema-cross 2026-05-06T19:00Z, +0.06R)
  - LTC −$48.58 (exit-stop-hit 2026-05-07T01:00Z, −1.03R)
  - XRP −$37.68 (exit-stop-hit 2026-05-07T14:00Z, −1.05R)
  - LINK +$103.03 (exit-ema-cross 2026-05-07T20:00Z, +1.69R)
  - SOL +$585.35 (exit-4R-target 2026-05-11T19:00Z, +4.03R)
- Unrealized PnL: **−$4.62** (XRP open; last price 1.46733 vs fill 1.46806; entry commission $24.18 deducted from cash)
- Position values (MTM): **$9,294.07** (XRP 6334 × 1.46733)
- Current equity (cash + positions MTM): **$10,229.26**
- Equity peak: **$10,258.06** (set 2026-05-11 midday at 4R take-profit on SOL)
- Drawdown from peak: **0.28%**

## Open positions

| Pair | Side | Size | Entry | Stop | Stop dist | R-risk | Last px | Unreal PnL | Unreal R |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| XRP/USD | long | 6334 | 1.46806 | 1.44377 | 0.02429 | $153.86 | 1.46733 | −$4.62 | −0.03 |

Portfolio risk-at-moment: **1.50%** of equity (cap 4%, XRP single position).
Open positions: **1 / 8** (strategy v0.2 max-concurrent 4 → 1/4 used; cluster {BTC,ETH,SOL,TAO,AVAX,SUI,LINK} 0/2; non-cluster 1 — XRP).

## Active kill-switch state

- Daily realized: **0.00%** today 2026-05-14 PT (no closes; only one OPEN) — well within 5% LOSS cap
- Consecutive losing trading days: ... 05-06 L, 05-07 W, 05-11 W, 05-12 flat, 05-13 flat → streak 0 (cap 7)
- Max drawdown: 0.28% (cap 25%, warn 12.5%) — clear, position just opened with normal slippage drag
- Equity floor: $10,229.26 > $7,500 floor — OK
- **All clear. Trading authorized.** XRP position freshly opened; monitor stop 1.44377 at 1H closes.

## Pending exit triggers

- **XRP/USD stop** at 1.44377 (2 × ATR(14) below 1.46806 entry; ATR ≈ 0.01215). Check at each 1H close.
- **XRP/USD 1H 20-EMA exit** when 1H close < 1H 20-EMA. EMA at entry-bar ≈ 1.4405; price currently ~$0.027 above EMA. Plenty of room.
- **XRP/USD 4R target** at 1.46806 + 4 × 0.02429 = **1.56522** (would yield ≈ +$615 / +4R).

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | — | — | — | — |
| 30d | — | — | — | — |
| 90d | — | — | — | — |

(Populated once a 7-day window has closed.)
