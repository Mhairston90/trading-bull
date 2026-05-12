# Variant v0.8-mean-rev-relaxed — Synthetic Portfolio

> **Paper-paper account.** Synthetic $10K starting equity.
> **Category:** LAB-SWEEP (parameter sweep of v0.4, RSI threshold 25 → 30)
> **Last rebuild:** 2026-05-12T22:00:00Z (initial spin-up)

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

Open positions: **0 / 2** (mean-reversion sized smaller than momentum, inherited from v0.4).

## Active kill-switch state

All clear at $10,000 equity.

## Rolling performance vs main v0.2 AND parent v0.4

| Window | v0.8 return | v0.4 (parent) return | v0.2 (main) return | Verdict |
|--------|-------------|----------------------|---------------------|---------|
| 7d  | — | — | — | not yet 7 days live |
| 30d | — | — | — | not yet 30 days live (earliest 2026-06-11) |

## Days live

- Spin-up: 2026-05-12
- Promotion-eligible: 2026-06-11

## Notes

Parameter sweep — RSI oversold threshold 30 (vs v0.4's 25). Tests whether v0.4 is over-filtering oversold candidates. Today's 2026-05-12 OVERNIGHT wake noted PENGU/USD hit RSI 25.4 — just above v0.4's threshold. v0.8 would have considered PENGU that wake (but other rules including M1 4H>200-EMA still apply).
