# Variant v0.14-recovery-trend — Synthetic Portfolio

> **Paper-paper account.** Synthetic $10K starting equity.
> **Category:** LAB hypothesis (entry rule 3: 4H 20-EMA trend filter vs main's 50-EMA)
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

Open positions: **0 / 4** (momentum cap inherited from v0.4 rule 6).

## Active kill-switch state

All clear at $10,000 equity.

## Rolling performance vs main v0.4

| Window | v0.14 return | main (v0.4) return | Verdict |
|--------|--------------|---------------------|---------|
| 7d  | — | — | not yet 7 days live |
| 30d | — | — | not yet 30 days live (earliest 2026-07-09) |

## Days live

- Spin-up: 2026-06-09
- Promotion-eligible: 2026-07-09 (after the 2026-07-01 competition deadline — this variant is for learning, not the contest)

## Notes

Tests whether replacing the 4H 50-EMA trend filter with a 20-EMA converts confirmed regime recoveries into trades. Evidence at spin-up: during 06-07→06-09 recovery wakes (8-14/15 positive), 0 pairs passed the 50-EMA filter while 1→14 pairs per wake passed the 20-EMA version. Counterfactual first trade (BTC @ 63,078, 06-08T04:00Z) would likely be a small loser in the current rollover — the dead-cat-bounce risk is acknowledged at spin-up. Regime at spin-up: 2/15 positive, median ≈ −2.4% (5a FAIL) — variant starts blocked, same as main.

### Routine #7 wake log

(none yet — first sim wake expected 2026-06-09 22:00 PT)
