# Variant v0.4-mean-reversion-sleeve — Synthetic Portfolio

> **Paper-paper account.** Synthetic $10K starting equity.
> **Last rebuild:** 2026-04-29T22:00:00Z (initial spin-up — no trades yet)

## Account

- Starting equity: **$10,000.00**
- Cash: **$10,000.00**
- Realized PnL (variant lifetime): **$0.00**
- Unrealized PnL: **$0.00** (no open positions)
- Position values (MTM): **$0.00**
- Current equity: **$10,000.00**
- Equity peak: **$10,000.00**
- Drawdown from peak: **0.00%**

## Open positions

(none)

Portfolio risk-at-moment: **0.00%** (cap 4%).
Open positions: **0 / 2** (variant max-concurrent 2 — mean-reversion sized smaller than momentum).

## Active kill-switch state

- Daily realized: **0.00%** (cap 5%)
- Consecutive losing trading days: 0 (cap 7)
- Max drawdown: 0.00% (cap 25%, warn 12.5%)
- Equity floor: $10,000 > $7,500 floor — OK
- **All clear.**

## Rolling performance vs main BULL v0.2

| Window | v0.4 return | v0.2 main return | Delta | BTC-hold | Result |
|--------|-------------|------------------|-------|----------|--------|
| 7d  | — | — | — | — | not yet 7 days live |
| 30d | — | — | — | — | not yet 30 days live (earliest 2026-05-29) |
| 90d | — | — | — | — | not yet 90 days live |

## Days live

- Spin-up: 2026-04-29
- As of last rebuild: **0 days**
- Promotion-eligible date: 2026-05-29

## Notes

Tests whether BULL's mandate-allowed-but-unused mean-reversion bucket adds edge uncorrelated to momentum. Looks for oversold bounces (RSI < 25) in pairs whose 4H trend is structurally bullish. Variant-internal bucket allocation is `mean-reversion: 100%`; main BULL bucket allocation in `memory/strategy.md` is unchanged at `momentum: 100%`.
