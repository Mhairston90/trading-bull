# Variant v0.5-cluster-cap-tight — Synthetic Portfolio

> **Paper-paper account.** Synthetic $10K starting equity.
> **Last rebuild:** 2026-05-17T05:00:00Z (routine-07 wake 2026-05-16 22:00 PT — no trades; see notes)

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
Open positions: **0 / 8** (variant max-concurrent 4 → 0/4 used; cluster cap 0/**1**).

## Active kill-switch state

- Daily realized: **0.00%** (cap 5%)
- Consecutive losing trading days: 0 (cap 7)
- Max drawdown: 0.00% (cap 25%, warn 12.5%)
- Equity floor: $10,000 > $7,500 floor — OK
- **All clear.**

## Rolling performance vs main BULL v0.2

| Window | v0.5 return | v0.2 main return | Delta | BTC-hold | Result |
|--------|-------------|------------------|-------|----------|--------|
| 7d  | — | — | — | — | not yet 7 days live |
| 30d | — | — | — | — | not yet 30 days live (earliest 2026-05-29) |
| 90d | — | — | — | — | not yet 90 days live |

## Days live

- Spin-up: 2026-04-29
- As of last rebuild: **17 days**
- Promotion-eligible date: 2026-05-29

## Notes

Tests whether tightening cluster cap from 2 to 1 (rule 6a) reduces cascade-event tail loss enough to justify foregone trend capture in cluster rallies. Single-rule parameter change vs v0.2.

### Routine #7 wake log

- **2026-05-12 22:00 PT** — past-24h replay window = 2026-05-11 16:00 UTC → 2026-05-12 16:00 UTC. Same entry-eval as v0.3 minus the vol-compression gate. At EOD-prior (positive 6/15) no pair passed rules 1+2+3 jointly. At OVERNIGHT positive 0/15 → 5a rejected all entries. MIDDAY had 6 candidates {BTC, SOL, XRP, DOGE, SUI, FARTCOIN} but variants honor main's no-midday-entry default. Result: 0 entries, 0 open positions. All kill switches clear at $10,000 equity.
- **2026-05-16 22:00 PT (this wake)** — past-24h replay window = 2026-05-15 10:00 UTC → 2026-05-16 10:00 UTC. Wakes evaluated: OVERNIGHT (2026-05-15 13:00 UTC), MIDDAY (2026-05-15 20:00 UTC, default-skip), EOD (2026-05-16 04:00 UTC). Broadly-red tape — all 15 pairs negative 24h; 05-15 13:00Z synchronized crash bar. Rule 5a (≥4/15 positive) rejected all entries at both eligible wakes (0/15 at EOD); cluster-cap 6a never reached. Result: 0 entries, 0 open positions. All kill switches clear at $10,000 equity.
