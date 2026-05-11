# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-05-11T13:00:00Z (routine-01-overnight — SOL/USD long held, MTM @ 95.10; broad-tape pullback wake, 0/15 universe pairs positive 24h, regime gate blocks all new entries).

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
- Unrealized PnL: **+$335.09 gross / +$310.90 net of est. exit commission** (SOL position, MTM at 95.10 spot)
- Position values (MTM): **$9,306.49** (97.86 × 95.10)
- Current equity (cash + positions MTM): **$9,984.47**
- Equity peak: **$10,115.60** (set 2026-05-10 midday)
- Drawdown from peak: **1.30%**

## Open positions

| Pair | Side | Size | Entry | Stop | Cost basis (gross) | Entry comm | Cluster | Unrealized R |
|------|------|-----:|------:|-----:|-------------------:|-----------:|---------|-------------:|
| SOL/USD | long | 97.86 | 91.6758 | 90.1932 | $8,971.40 | $23.33 | yes | +2.31R (MTM 95.10) |

Portfolio risk-at-moment: **1.45%** (cap 4%) — single SOL position, stop distance 1.4826 × 97.86 = $145.10 = 1.45% of equity $9,984.47.
Open positions: **1 / 8** (strategy v0.2 max-concurrent 4 → 1/4 used; cluster {BTC,ETH,SOL,TAO,AVAX,SUI,LINK} 1/2; non-cluster 0).

## Active kill-switch state

- Daily realized: **$0.00** today 2026-05-11 PT (no closes) — well within 5% cap
- Daily realized + unrealized change from prior wake: SOL MTM fell from 96.44 → 95.10 (~−$131 unrealized swing); intraday pullback only, still net +$310.90 on position. Well within 5% loss cap.
- Consecutive losing trading days: 04-24 L, 04-25 L, 04-26 flat, 04-27 L, 04-28 flat, 04-29 L, 04-30..05-05 flat, 05-06 L, 05-07 W → reset to 0 (cap 7)
- Max drawdown: 1.30% (cap 25%, warn 12.5%) — clear
- Equity floor: $9,984.47 > $7,500 floor — OK
- **All clear. Trading authorized (but regime gate blocks new entries this wake: 0/15 universe positive 24h, need ≥4).**

## Pending exit triggers

- **SOL/USD** (long 97.86 @ 91.6758): static stop 90.1932 (2×ATR below entry). Spot 95.09–95.10. Next exit checks at 1H closes via routine-02 midday and routine-03 EOD — EMA-cross (1H 20-EMA tracking ~95.13 at the 2026-05-11 08:00Z close; tape has tightened toward the EMA but no confirmed cross-down yet), stop hit (intact), or 4R take-profit at 97.6062. Currently +2.31R unrealized; 4R target ~$2.51 above spot. EMA-cross/4R deferred to next 1H-close routine per architecture.

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | — | — | — | — |
| 30d | — | — | — | — |
| 90d | — | — | — | — |

(Populated once a 7-day window has closed.)
