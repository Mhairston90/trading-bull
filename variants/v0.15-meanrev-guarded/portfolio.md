# Variant v0.15-meanrev-guarded — Synthetic Portfolio

> **Paper-paper account.** Synthetic $10K starting equity.
> **Category:** LAB hypothesis (mean-reversion: RSI<30 floor + SBD knife-catch guard; A/B vs v0.8)
> **Last rebuild:** 2026-06-14T05:00Z (routine-07 wake 2026-06-13 22:00 PT — 0 entries; RSI far above mean-rev thresholds; 15/15 positive EOD)

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
- As of last rebuild: **5 days**
- Promotion-eligible: 2026-07-09 (after the 2026-07-01 competition deadline — this variant is for learning, not the contest)

## Notes

Combines v0.8's relaxed RSI<30 with an SBD entry guard. The benchmark trade: v0.8's NEAR/USD 2026-06-05 entry (RSI 26.9, SBD wake, −1.00R in 4h) — v0.15 would have skipped it. Every future v0.8-vs-v0.15 divergence isolates the guard's value. Regime at spin-up: 2/15 positive, median ≈ −2.4% — not SBD (needs ≤1/15), but 5a-FAIL territory; mean-rev variants ignore 5a by design, so the guard is the only regime brake here.

### Routine #7 wake log

- **CORRECTION NOTE (2026-06-11 22:00 PT):** Prior entry labeled "2026-06-11 22:00 PT" was from the June 10 22:00 PT run (first sim wake, mislabeled). Mean-rev analysis unaffected by BTC close correction (M2 RSI<30 fails regardless). 0-entry conclusion unchanged.
- **2026-06-10 22:00 PT (MISLABELED as 2026-06-11 22:00 PT — first sim wake, stale)** — Wakes: OVERNIGHT (2026-06-10T13:00Z), EOD (2026-06-11T04:00Z), OVERNIGHT (2026-06-11T13:00Z), EOD (2026-06-12T04:00Z). SBD active at first 3 wakes → v0.15 guard blocks. EOD 2026-06-12T04:00Z: SBD CLEARED → guard inactive; M3 PASSES (15/15 ✓); M2 (RSI<30): BTC ~57.9 → FAIL. **0 entries.** Kill switches clear at $10,000. Days live: 3.
- **2026-06-11 22:00 PT (this wake)** — **EOD 2026-06-12T04:00Z (confirmed):** SBD CLEARED ✓ (guard inactive); M3 PASSES (15/15 green ✓); M2 (RSI < 30): BTC RSI 57.4 >> 30; no pair near oversold. **0 entries.** A/B vs v0.8: same outcome (both 0); guard was irrelevant this wake since SBD cleared before entry window. Next divergence requires RSI<30 during an SBD-active wake. Kill switches all clear at $10,000. Days live: **3**.
- **2026-06-12 22:00 PT (routine-07)** — replay window 2026-06-12T06:45Z → 2026-06-13T05:00Z (~22h). **OVERNIGHT + EOD:** SBD CLEAR (guard inactive). M2 (RSI < 30): universe RSI elevated 48-65. **0 entries.** A/B vs v0.8: identical outcome (both 0). Kill switches all clear at $10,000. Days live: **4**.
- **2026-06-13 22:00 PT (routine-07)** — replay window 2026-06-13T05:08Z → 2026-06-14T05:00Z (~23.87h). **OVERNIGHT + EOD:** SBD CLEARED throughout (15/15 positive at EOD) → SBD guard inactive. M3 PASSES. M2 (RSI < 30): universe RSI 48-76 — no pair near oversold. **0 entries.** A/B vs v0.8: identical outcome (both 0 — guard irrelevant when RSI far from threshold). Next meaningful A/B divergence requires RSI<30 during an active SBD wake. Kill switches all clear at $10,000. Days live: **5**.
