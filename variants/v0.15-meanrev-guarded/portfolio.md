# Variant v0.15-meanrev-guarded — Synthetic Portfolio

> **Paper-paper account.** Synthetic $10K starting equity.
> **Category:** LAB hypothesis (mean-reversion: RSI<30 floor + SBD knife-catch guard; A/B vs v0.8)
> **Last rebuild:** 2026-06-12T05:00Z (routine-07 wake 2026-06-11 22:00 PT — 0 trades; first sim wake; 48h replay)

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
- As of last rebuild: **3 days**
- Promotion-eligible: 2026-07-09 (after the 2026-07-01 competition deadline — this variant is for learning, not the contest)

## Notes

Combines v0.8's relaxed RSI<30 with an SBD entry guard. The benchmark trade: v0.8's NEAR/USD 2026-06-05 entry (RSI 26.9, SBD wake, −1.00R in 4h) — v0.15 would have skipped it. Every future v0.8-vs-v0.15 divergence isolates the guard's value. Regime at spin-up: 2/15 positive, median ≈ −2.4% — not SBD (needs ≤1/15), but 5a-FAIL territory; mean-rev variants ignore 5a by design, so the guard is the only regime brake here.

### Routine #7 wake log

- **2026-06-11 22:00 PT (first sim wake)** — replay window 2026-06-10T05:00Z → 2026-06-12T05:00Z (48h from 2026-06-09 spin-up). Kraken MCP OK (BTC/USD $62,563; 4H OHLCV unavailable). Wakes: OVERNIGHT (2026-06-10T13:00Z), EOD (2026-06-11T04:00Z), OVERNIGHT (2026-06-11T13:00Z), EOD (2026-06-12T04:00Z). **OVERNIGHT 2026-06-10T13:00Z:** SBD active → v0.15 SBD entry guard blocks mean-rev entries during SBD (by design). 0 entries. **EOD 2026-06-11T04:00Z:** SBD active → guard blocks. 0 entries. **OVERNIGHT 2026-06-11T13:00Z:** SBD active → guard blocks. 0 entries. **EOD 2026-06-12T04:00Z:** SBD CLEARED ✓ (guard inactive). M3 PASSES (15/15 green ✓). M2 (RSI < 30): BTC 1H RSI ~57.9 — far above 30 threshold. Full 15/15 positive tape → no pair near oversold. **0 entries.** A/B vs v0.8: same outcome this wake (both 0 entries); SBD-guard divergence was only relevant at the 3 SBD-active wakes, where v0.8 would have logged 0 entries anyway (NEAR RSI ≈36–45 > 30 → M2 FAIL). First A/B divergence will occur when RSI < 30 during SBD. Exit replay no-op (book flat). Kill switches all clear at $10,000. Days live: **3**.
