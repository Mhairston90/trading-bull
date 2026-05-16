# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-05-16T20:00Z (routine-02-midday — XRP/USD stop pierced intrabar on 2026-05-15T13:00Z 1H bar (low 1.4292 < stop 1.44377); missed by intervening routines (last MTM was EOD 2026-05-14; 05-15 overnight/EOD did not run/commit). Closed at stop price w/ 0.05% adverse slippage. Now flat.)

## Account

- Starting equity: **$10,000.00**
- Cash: **$10,051.73**
- Realized PnL (all-time): **+$51.73**
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
  - XRP −$206.37 (exit-stop-hit 2026-05-15T13:00Z, −1.03R)
- Unrealized PnL: **$0.00** (flat — no open positions)
- Position values (MTM): **$0.00**
- Current equity (cash + positions MTM): **$10,051.73**
- Equity peak: **$10,258.06** (set 2026-05-11 midday at 4R take-profit on SOL)
- Drawdown from peak: **2.01%**

## Open positions

| Pair | Side | Size | Entry | Stop | Stop dist | R-risk | Last px | Unreal PnL | Unreal R |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| — | — | — | — | — | — | — | — | — | — |

Portfolio risk-at-moment: **0.00%** of equity (cap 4%, flat).
Open positions: **0 / 8** (strategy v0.2 max-concurrent 4 → 0/4 used; cluster {BTC,ETH,SOL,TAO,AVAX,SUI,LINK} 0/2).

## Active kill-switch state

- Daily realized: **0.00%** today 2026-05-16 PT (no closes today). The XRP stop-out booked 2026-05-15T13:00Z = −$206.37 ≈ −2.01% of equity for that day — within 5% LOSS cap.
- Consecutive losing trading days: 05-07 W, 05-11 W, 05-12 flat, 05-13 flat, 05-14 flat (open only), **05-15 L** (XRP −1.03R) → streak **1** (cap 7)
- Max drawdown: 2.01% (cap 25%, warn 12.5%) — clear
- Equity floor: $10,051.73 > $7,500 floor — OK
- **All clear. Trading authorized.** No open positions; XRP/USD long closed at stop 1.44305 (price pierced 1.44377 intrabar on 2026-05-15T13:00Z bar, low 1.4292). XRP last px 1.39814 — well below stop, confirming the exit was correct.

## Pending exit triggers

- None — portfolio is flat.

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | — | — | — | — |
| 30d | — | — | — | — |
| 90d | — | — | — | — |

(Populated once a 7-day window has closed.)
