# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-05-07T18:30:00Z (routine-01-overnight 5/7 morning wake — XRP stop-out at 14:00Z 5/7 (low 1.39121 < stop 1.39468), fill 1.39398, -1.05R / -$37.68; 0/15 regime gate blocks all entries; 1 OPEN position remaining (LINK)).

## Account

- Starting equity: **$10,000.00**
- Cash: **$7,137.46**
- Realized PnL (all-time): **−$430.28**
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
- Unrealized PnL: **+$116.19**
  - LINK: 257 × 9.91596 = $2,548.40 MTM; cost 257×9.4393 + comm $6.31 = $2,432.21 → **+$116.19**
- Position values (MTM): **$2,548.40**
- Current equity (cash + positions MTM): **$9,685.86**
- Equity peak: **$10,027.55** (set 2026-04-24 midday)
- Drawdown from peak: **3.41%**

## Open positions

| Pair | Side | Size | Entry | Stop | Entry time | Stop dist | Risk USD | Risk % | Cluster |
|------|------|------|-------|------|------------|-----------|----------|--------|---------|
| LINK/USD | long | 257 | 9.4393 | 9.2018 | 2026-05-04T19:00Z | 0.2375 | $61.04 | 0.630% | yes (BTC-corr) |

Portfolio risk-at-moment: **0.630%** (cap 4%).
Open positions: **1 / 8** (strategy v0.2 max-concurrent 4 → 1/4 used; cluster cap 1/2; non-cluster 0).

## Active kill-switch state

- Daily realized: **−0.39%** today 2026-05-07 PT (cap 5%) — XRP −$37.68 / starting equity baseline ~$9,704.39 → -0.39%
- Daily realized + unrealized: combined approx −0.20% today (−$37.68 realized + change in unrealized vs prior wake +$19.16) — well within 5% cap
- Consecutive losing trading days: 04-24 L, 04-25 L, 04-26 flat, 04-27 L, 04-28 flat, 04-29 L, 04-30 flat, 05-01 flat, 05-02 flat, 05-03 flat, 05-04 flat, 05-05 flat, 05-06 L, 05-07 L → 2-in-a-row (cap 7)
- Max drawdown: 3.41% (cap 25%, warn 12.5%) — clear
- Equity floor: $9,685.86 > $7,500 floor — OK
- **All clear. Trading authorized.**

## Pending exit triggers (informational; routine-01 closes only stop-outs per task body)

- **LINK/USD**: 1H close < 1H 20-EMA condition still active across multiple bars (close 9.92 at 18:00Z vs ~9.95 EMA). Will be re-evaluated by next routine-02 midday wake. Stop 9.2018 well below current 9.92; no imminent stop risk barring cascade.

(Per task body, routine-01-overnight only executes stop-out closures. EMA-cross exits accumulate until routine-02 midday catches them. This is the architected behavior.)

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | — | — | — | — |
| 30d | — | — | — | — |
| 90d | — | — | — | — |

(Populated once a 7-day window has closed.)
