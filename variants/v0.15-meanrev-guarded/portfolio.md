# Variant v0.15-meanrev-guarded — Synthetic Portfolio

> **Paper-paper account.** Synthetic $10K starting equity.
> **Category:** LAB hypothesis (mean-reversion: RSI<30 floor + SBD knife-catch guard; A/B vs v0.8)
> **Last rebuild:** 2026-06-27T16:43Z (routine-07 wake 2026-06-27 PT — 09:43 PT OFF-SCHEDULE Saturday fire; 0 entries; SBD CLEAR all 3 wakes so guard inactive; M2 RSI<30 not met in 14/15-positive tape; 0 closed trades lifetime)

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
- As of last rebuild: **16 days**
- Promotion-eligible: 2026-07-09 (after the 2026-07-01 competition deadline — this variant is for learning, not the contest). 0 closed trades lifetime.

## Notes

Combines v0.8's relaxed RSI<30 with an SBD entry guard. The benchmark trade: v0.8's NEAR/USD 2026-06-05 entry (RSI 26.9, SBD wake, −1.00R in 4h) — v0.15 would have skipped it. Every future v0.8-vs-v0.15 divergence isolates the guard's value. Regime at spin-up: 2/15 positive, median ≈ −2.4% — not SBD (needs ≤1/15), but 5a-FAIL territory; mean-rev variants ignore 5a by design, so the guard is the only regime brake here.

### Routine #7 wake log

- **CORRECTION NOTE (2026-06-11 22:00 PT):** Prior entry labeled "2026-06-11 22:00 PT" was from the June 10 22:00 PT run (first sim wake, mislabeled). Mean-rev analysis unaffected by BTC close correction (M2 RSI<30 fails regardless). 0-entry conclusion unchanged.
- **2026-06-10 22:00 PT (MISLABELED as 2026-06-11 22:00 PT — first sim wake, stale)** — Wakes: OVERNIGHT (2026-06-10T13:00Z), EOD (2026-06-11T04:00Z), OVERNIGHT (2026-06-11T13:00Z), EOD (2026-06-12T04:00Z). SBD active at first 3 wakes → v0.15 guard blocks. EOD 2026-06-12T04:00Z: SBD CLEARED → guard inactive; M3 PASSES (15/15 ✓); M2 (RSI<30): BTC ~57.9 → FAIL. **0 entries.** Kill switches clear at $10,000. Days live: 3.
- **2026-06-11 22:00 PT (this wake)** — **EOD 2026-06-12T04:00Z (confirmed):** SBD CLEARED ✓ (guard inactive); M3 PASSES (15/15 green ✓); M2 (RSI < 30): BTC RSI 57.4 >> 30; no pair near oversold. **0 entries.** A/B vs v0.8: same outcome (both 0); guard was irrelevant this wake since SBD cleared before entry window. Next divergence requires RSI<30 during an SBD-active wake. Kill switches all clear at $10,000. Days live: **3**.
- **2026-06-12 22:00 PT (routine-07)** — replay window 2026-06-12T06:45Z → 2026-06-13T05:00Z (~22h). **OVERNIGHT + EOD:** SBD CLEAR (guard inactive). M2 (RSI < 30): universe RSI elevated 48-65. **0 entries.** A/B vs v0.8: identical outcome (both 0). Kill switches all clear at $10,000. Days live: **4**.
- **2026-06-13 22:00 PT (routine-07)** — replay window 2026-06-13T05:08Z → 2026-06-14T05:00Z (~23.87h). **OVERNIGHT + EOD:** SBD CLEARED throughout (15/15 positive at EOD) → SBD guard inactive. M3 PASSES. M2 (RSI < 30): universe RSI 48-76 — no pair near oversold. **0 entries.** A/B vs v0.8: identical outcome (both 0 — guard irrelevant when RSI far from threshold). Next meaningful A/B divergence requires RSI<30 during an active SBD wake. Kill switches all clear at $10,000. Days live: **5**.
- **2026-06-24 PT (routine-07 — gap replay via routine07_replay_20260623.py; fired ~09:35 PT off-schedule)** — Replay window: **2026-06-14T05:00Z → 2026-06-24T13:00Z** (10.5 days). **All 12 wakes assessed: 0 entries.** June 14–22 broad-rally tape: RSI 48-76+; M2 (RSI<30) failed at all wakes. The June 22 SBD wake (9/15+ positive → SBD borderline area) and June 24 SBD morning: v0.15 guard would have blocked even if RSI had approached the threshold, but RSI was still far above 30. **A/B vs v0.8: identical outcome — both 0 entries.** The SBD guard is not yet producing divergence data (would need RSI<30 in an SBD wake to diverge from v0.8). **OVERNIGHT 2026-06-24T13:00Z:** SBD active → v0.15 SBD guard blocks before M3/M2 checks. Kill switches all clear at $10,000. Days live: **15**.
- **2026-06-25 PT (routine-07, 2026-06-25T19:19Z — off-cron 12:19 PT)** — Watchdog ALL CLEAR. Kraken MCP OK. Replay window: 2026-06-24T16:35Z → 2026-06-25T19:19Z (~26.7h). Wakes evaluated: **EOD 2026-06-25T04:00Z**: SBD ACTIVE → SBD guard blocks entry before M3/M2 checked (same outcome as v0.8). **OVERNIGHT 2026-06-25T13:00Z**: SBD ACTIVE → SBD guard blocks. Universe RSI 38-55 during sell-off — RSI<30 not met anyway. A/B vs v0.8: identical 0-entry outcome (guard irrelevant when RSI>30). Kill switches all clear at $10,000. Days live: **16**.
- **2026-06-25 PT (routine-07, 2026-06-26T05:06Z — 22:05 PT on-schedule cron fire)** — Watchdog ALL CLEAR. Kraken MCP OK ($59,766.5 BTC). Replay window: 2026-06-25T19:19Z → 2026-06-26T05:06Z (~9.8h). MIDDAY 20:00Z: default skip. **EOD 2026-06-26T04:00Z**: SBD briefly CLEARED → guard inactive. M3 check: SOL/HYPE positive (M3 PASS); M2 (RSI<30): SOL ~54.4, HYPE ~53.7 >> 30 → M2 FAIL. Negative pairs M3 FAIL. TRX RSI ~30 but R4a notional FAIL. **0 entries.** A/B vs v0.8: identical 0-entry (guard was irrelevant; M2 was binding). Post-EOD: SBD re-activated → guard now active again. Kill switches all clear at $10,000. Days live: **16**.
- **2026-06-27 PT (routine-07, 2026-06-27T16:43Z — 09:43 PT OFF-SCHEDULE Saturday fire)** — Watchdog 1 finding (self-resolving). Kraken MCP OK (14/15 positive, median +1.60%, SBD CLEAR). Replay window: 2026-06-26T05:06Z → 2026-06-27T16:43Z (~35.6h). Wakes: OVERNIGHT Jun26 13:00Z (SBD state uncertain; R3 binding anyway → 0 entries; guard irrelevant), EOD Jun27 04:00Z (SBD CLEAR → guard inactive; M2 RSI<30 FAIL), OVERNIGHT Jun27 13:00Z (SBD CLEAR → guard inactive; M2 RSI<30: SOL 63.5, SUI 60.8, LTC 66.3 — all far above threshold). **0 entries all 3 wakes.** A/B vs v0.8: identical 0-entry (guard irrelevant in 14/15-positive SBD-CLEAR tape; M2 was binding). Guard would only produce divergence if RSI<30 occurred during an SBD wake. Kill switches all clear at $10,000. Days live: **18**.
