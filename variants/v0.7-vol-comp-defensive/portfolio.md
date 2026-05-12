# Variant v0.7-vol-comp-defensive — Synthetic Portfolio

> **Paper-paper account.** Synthetic $10K starting equity.
> **Category:** LAB-SWEEP (parameter sweep of v0.3, threshold 0.5 → 0.7)
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

Open positions: **0 / 4**. Cluster: 0/2.

## Active kill-switch state

All clear at $10,000 equity.

## Rolling performance vs main v0.2 AND parent v0.3

| Window | v0.7 return | v0.3 (parent) return | v0.2 (main) return | Verdict |
|--------|-------------|----------------------|---------------------|---------|
| 7d  | — | — | — | not yet 7 days live |
| 30d | — | — | — | not yet 30 days live (earliest 2026-06-11) |

## Days live

- Spin-up: 2026-05-12
- Promotion-eligible: 2026-06-11

## Notes

Parameter sweep — `vol_compression_threshold = 0.7` (vs v0.3's 0.5). Tests whether v0.3 is under-filtering. May produce few trades if regime stays in mild compression.
