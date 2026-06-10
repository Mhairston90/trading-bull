# Variant v0.15-meanrev-guarded — Synthetic Portfolio

> **Paper-paper account.** Synthetic $10K starting equity.
> **Category:** LAB hypothesis (mean-reversion: RSI<30 floor + SBD knife-catch guard; A/B vs v0.8)
> **Last rebuild:** 2026-06-09 (spin-up — interactive, user-requested)

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

Open positions: **0 / 2** (mean-reversion cap inherited from v0.4-mr M6).

## Active kill-switch state

All clear at $10,000 equity.

## Rolling performance vs v0.8 (no-guard A/B) and parent v0.4-mr

| Window | v0.15 return | v0.8 return | v0.4-mr return | Verdict |
|--------|--------------|-------------|-----------------|---------|
| 7d  | — | — | — | not yet 7 days live |
| 30d | — | — | — | not yet 30 days live (earliest 2026-07-09) |

## Days live

- Spin-up: 2026-06-09
- Promotion-eligible: 2026-07-09 (after the 2026-07-01 competition deadline — this variant is for learning, not the contest)

## Notes

Combines v0.8's relaxed RSI<30 with an SBD entry guard. The benchmark trade: v0.8's NEAR/USD 2026-06-05 entry (RSI 26.9, SBD wake, −1.00R in 4h) — v0.15 would have skipped it. Every future v0.8-vs-v0.15 divergence isolates the guard's value. Regime at spin-up: 2/15 positive, median ≈ −2.4% — not SBD (needs ≤1/15), but 5a-FAIL territory; mean-rev variants ignore 5a by design, so the guard is the only regime brake here.

### Routine #7 wake log

(none yet — first sim wake expected 2026-06-09 22:00 PT)
