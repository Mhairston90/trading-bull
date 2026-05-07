# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-05-07T04:30:00Z (routine-01-overnight 5/6 PT-EOD wake — LTC stop-out at 01:00Z 5/7 (low 56.22 < stop 56.28), fill 56.25, -1.03R / -$48.58; 2 OPEN positions remaining).

## Account

- Starting equity: **$10,000.00**
- Cash: **$4,741.87**
- Realized PnL (all-time): **−$392.60**
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
- Unrealized PnL: **+$97.03**
  - LINK: 257 × 9.88429 = $2,540.26 MTM; cost 257×9.4393 + comm $6.31 = $2,432.21 → **+$108.05**
  - XRP: 1723 × 1.40584 = $2,422.26 MTM; cost 1723×1.40857 + comm $6.31 = $2,433.28 → **−$11.02**
- Position values (MTM): **$4,962.52**
- Current equity (cash + positions MTM): **$9,704.39**
- Equity peak: **$10,027.55** (set 2026-04-24 midday)
- Drawdown from peak: **3.22%**

## Open positions

| Pair | Side | Size | Entry | Stop | Entry time | Stop dist | Risk USD | Risk % | Cluster |
|------|------|------|-------|------|------------|-----------|----------|--------|---------|
| LINK/USD | long | 257 | 9.4393 | 9.2018 | 2026-05-04T19:00Z | 0.2375 | $61.04 | 0.629% | yes (BTC-corr) |
| XRP/USD | long | 1723 | 1.40857 | 1.39468 | 2026-05-05T17:00Z | 0.01389 | $23.93 | 0.247% | no |

Portfolio risk-at-moment: **0.876%** (cap 4%).
Open positions: **2 / 8** (strategy v0.2 max-concurrent 4 → 2/4 used; cluster cap 1/2; non-cluster 1 = XRP).

## Active kill-switch state

- Daily realized: **−1.08%** today 2026-05-06 PT (cap 5%) — HYPE −$58.18 + BTC +$1.42 + LTC −$48.58 = −$105.34 / starting equity baseline ~$9,712.74
- Daily realized + unrealized: combined approx −1.36% today (−$105.34 realized + change in unrealized vs prior wake) — well within 5% cap
- Consecutive losing trading days: 04-24 L, 04-25 L, 04-26 flat, 04-27 L, 04-28 flat, 04-29 L, 04-30 flat, 05-01 flat, 05-02 flat, 05-03 flat, 05-04 flat, 05-05 flat, 05-06 L → not 7-in-a-row (cap 7)
- Max drawdown: 3.22% (cap 25%, warn 12.5%) — clear
- Equity floor: $9,704.39 > $7,500 floor — OK
- **All clear. Trading authorized.**

## Pending exit triggers (informational; routine-01 closes only stop-outs per task body)

- **LINK/USD**: 1H close < 1H 20-EMA first triggered at 2026-05-07T00:00Z bar (close 9.93977 < EMA 9.973). Exit-ema-cross condition currently active across 4 subsequent bars. Will be executed by next routine-02 midday wake unless price reverses above EMA. Stop 9.2018 still well below current 9.88; no stop risk imminent.
- **XRP/USD**: 1H close < 1H 20-EMA first triggered at 2026-05-06T20:00Z bar (close 1.42448 < EMA 1.42714). Exit-ema-cross condition active for 8 consecutive bars. Will be executed by next routine-02 midday wake unless price reverses. Stop 1.39468 below current 1.40584; modest cushion.

(Per task body, routine-01-overnight only executes stop-out closures. EMA-cross exits accumulate until routine-02 midday catches them. This is the architected behavior.)

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | — | — | — | — |
| 30d | — | — | — | — |
| 90d | — | — | — | — |

(Populated once a 7-day window has closed.)
