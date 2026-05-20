# Variant v0.13-trend-confirm — Synthetic Portfolio

> **Paper-paper account.** Synthetic $10K starting equity.
> **Category:** LAB hypothesis (entry-quality filter: 2-bar EMA confirm + 4H RSI ≥ 50 vs main's single-bar entry)
> **Last rebuild:** 2026-05-20 (initial spin-up, interactive session)

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

Open positions: **0 / 4** (momentum cap inherited from v0.3 rule 6).

## Active kill-switch state

All clear at $10,000 equity.

## Rolling performance vs main v0.3

| Window | v0.13 return | v0.3 (main) return | Verdict |
|--------|--------------|---------------------|---------|
| 7d  | — | — | not yet 7 days live |
| 30d | — | — | not yet 30 days live (earliest 2026-06-19) |

## Days live

- Spin-up: 2026-05-20
- Promotion-eligible: 2026-06-19

## Notes

Hypothesis variant targeting the whipsaw −1R bucket — the dominant un-addressed loss source on main (9 of 17 closes are −1R stop-outs inside 21h of entry, ≈ −$386 of the ~−$700 in main's losses inception-to-date). Adds entry-quality filters: (a) requires two consecutive 1H closes above the 20-EMA (single-bar tag insufficient), and (b) requires 4H RSI(14) ≥ 50 at entry-scan (higher-timeframe trend confirmation). Strictly entry-restricting vs v0.3 — can only reject entries v0.3 would have taken, never admit new ones. Created interactively 2026-05-20 to accrue paper-paper evidence as the entry-quality counterpart to the v0.10/v0.11/v0.12 exit-quality variant cluster.
