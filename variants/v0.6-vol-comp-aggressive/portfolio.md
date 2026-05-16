# Variant v0.6-vol-comp-aggressive — Synthetic Portfolio

> **Paper-paper account.** Synthetic $10K starting equity.
> **Category:** LAB-SWEEP (parameter sweep of v0.3, threshold 0.5 → 0.3)
> **Last rebuild:** 2026-05-17T05:00:00Z (routine-07 wake 2026-05-16 22:00 PT — first simulation wake; no trades, see notes)

## Account

- Starting equity: **$10,000.00**
- Cash: **$10,000.00**
- Realized PnL: **$0.00**
- Unrealized PnL: **$0.00**
- Current equity: **$10,000.00**
- Equity peak: **$10,000.00**
- Drawdown from peak: **0.00%**

## Open positions

(none)

Portfolio risk-at-moment: **0.00%** (cap 4%).
Open positions: **0 / 4**. Cluster: 0/2.

## Active kill-switch state

All clear at $10,000 equity.

## Rolling performance vs main v0.2 AND parent v0.3

| Window | v0.6 return | v0.3 (parent) return | v0.2 (main) return | Verdict |
|--------|-------------|----------------------|---------------------|---------|
| 7d  | — | — | — | not yet 7 days live |
| 30d | — | — | — | not yet 30 days live (earliest 2026-06-11) |

## Days live

- Spin-up: 2026-05-12
- Promotion-eligible: 2026-06-11
- Days vs parent v0.3 (spun 2026-04-29): parent is 13 days older

## Notes

Parameter sweep — `vol_compression_threshold = 0.3` (vs v0.3's 0.5). Tests whether v0.3's threshold is over-filtering. See README for full lineage.

### Routine #7 wake log

- **2026-05-16 22:00 PT (first sim wake since 05-12 spin-up)** — past-24h replay window = 2026-05-15 10:00 UTC → 2026-05-16 10:00 UTC. Wakes: OVERNIGHT (05-15 13:00Z), MIDDAY (05-15 20:00Z, default-skip), EOD (05-16 04:00Z). Inherits v0.3 rules incl. regime gate 5a (≥4/15 positive 24h). Broadly-red tape — all 15 pairs negative 24h, 0/15 positive at EOD; 5a rejected all entries at both eligible wakes before the loosened 0.3 vol-comp gate was reached. 0 entries, 0 open positions. All kill switches clear at $10,000 equity.
