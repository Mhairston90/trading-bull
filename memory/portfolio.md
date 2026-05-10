# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-05-10T20:00:00Z (routine-02-midday — SOL/USD long held, MTM @ 96.44; new equity peak $10,115.60).

## Account

- Starting equity: **$10,000.00**
- Cash: **$677.98**
- Realized PnL (all-time): **−$327.25**
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
- Unrealized PnL: **+$466.22 gross / +$441.68 net of est. exit commission** (SOL position, MTM at 96.44 spot)
- Position values (MTM): **$9,437.62** (97.86 × 96.44)
- Current equity (cash + positions MTM): **$10,115.60**
- Equity peak: **$10,115.60** (set 2026-05-10 midday — new peak, prior $10,027.55 from 2026-04-24)
- Drawdown from peak: **0.00%**

## Open positions

| Pair | Side | Size | Entry | Stop | Cost basis (gross) | Entry comm | Cluster | Unrealized R |
|------|------|-----:|------:|-----:|-------------------:|-----------:|---------|-------------:|
| SOL/USD | long | 97.86 | 91.6758 | 90.1932 | $8,971.40 | $23.33 | yes | +3.21R (MTM 96.44) |

Portfolio risk-at-moment: **1.43%** (cap 4%) — single SOL position, stop distance 1.4826 × 97.86 = $145.10 = 1.43% of equity $10,115.60.
Open positions: **1 / 8** (strategy v0.2 max-concurrent 4 → 1/4 used; cluster {BTC,ETH,SOL,TAO,AVAX,SUI,LINK} 1/2; non-cluster 0).

## Active kill-switch state

- Daily realized: **$0.00** today 2026-05-10 PT (no closes) — well within 5% cap
- Daily realized + unrealized: SOL position deeply green; daily change since prior wake snapshot is positive — within 5% loss cap
- Consecutive losing trading days: 04-24 L, 04-25 L, 04-26 flat, 04-27 L, 04-28 flat, 04-29 L, 04-30..05-05 flat, 05-06 L, 05-07 W → reset to 0 (cap 7)
- Max drawdown: 0.00% (cap 25%, warn 12.5%) — clear, new peak today
- Equity floor: $10,115.60 > $7,500 floor — OK
- **All clear. Trading authorized.**

## Pending exit triggers

- **SOL/USD** (long 97.86 @ 91.6758): static stop 90.1932 (2×ATR below entry); next exit checks at 21:00Z, 22:00Z, 23:00Z 1H closes — EMA-cross (1H close < 1H 20-EMA ≈ 94.40 and rising), stop hit, or 4R take-profit at 97.6062. Currently +3.21R unrealized; 4R target ~$1.17 above spot. EMA-cross deferred to next 1H close per architecture.

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | — | — | — | — |
| 30d | — | — | — | — |
| 90d | — | — | — | — |

(Populated once a 7-day window has closed.)
