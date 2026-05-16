# Variant v0.11-breakeven-2R — Synthetic Portfolio

> **Paper-paper account.** Synthetic $10K starting equity.
> **Category:** LAB hypothesis (breakeven stop-ratchet at 2R unrealized vs main's static stop)
> **Last rebuild:** 2026-05-16T18:00:00Z (initial spin-up)

## Account

- Starting equity: **$10,000.00**
- Cash: **$10,000.00**
- Realized PnL: **$0.00**
- Unrealized PnL: **$0.00**
- Current equity: **$10,000.00**
- Equity peak: **$10,000.00**
- Drawdown: **0.00%**

## Open positions

(none)

Open positions: **0 / 4** (momentum cap inherited from v0.2 rule 6).

## Active kill-switch state

All clear at $10,000 equity.

## Rolling performance vs main v0.2

| Window | v0.11 return | v0.2 (main) return | Verdict |
|--------|--------------|---------------------|---------|
| 7d  | — | — | not yet 7 days live |
| 30d | — | — | not yet 30 days live (earliest 2026-06-15) |

## Days live

- Spin-up: 2026-05-16
- Promotion-eligible: 2026-06-15

## Notes

Hypothesis variant targeting the profit-give-back lesson (2026-05-15, score 9). Adds a breakeven stop-ratchet: once a trade is up ≥2R, the stop moves to entry so a matured winner cannot round-trip into a loss (XRP 2026-05-14 archetype: ran ~+2.8R, exited −0.14R). Stop ratchets up only; no further trailing. Strictly risk-reducing vs v0.2. Created by routine #4 2026-05-16 to accrue paper-paper evidence while TradingView (needed for the 180d backtest behind a Ring-2 proposal) is unavailable. Sibling exit-logic variant: v0.10-exit-confirm.
