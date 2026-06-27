# Variant v0.9-mean-rev-tight — Synthetic Portfolio

> **Paper-paper account.** Synthetic $10K starting equity.
> **Category:** LAB-SWEEP (parameter sweep of v0.4, RSI threshold 25 → 20)
> **Last rebuild:** 2026-06-27T16:43Z (routine-07 wake 2026-06-27 PT — 09:43 PT OFF-SCHEDULE Saturday fire; 0 entries; RSI<20 not approached in 14/15-positive tape; 0 closed trades lifetime)

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

| Window | v0.9 return | v0.4 (parent) return | v0.2 (main) return | Verdict |
|--------|-------------|----------------------|---------------------|---------|
| 7d  | — | — | — | not yet 7 days live |
| 30d | — | — | — | not yet 30 days live (earliest 2026-06-15) |

## Days live

- Spin-up: 2026-05-16
- As of last rebuild: **40 days**
- Promotion-eligible: 2026-06-15 (reached) — 0 closed trades lifetime (need ≥10 in rolling 30d) → NOT promotion-eligible; variant continues in LAB.

## Notes

Parameter sweep — RSI oversold threshold 20 (vs v0.4's 25, v0.8's 30). Brackets the parent on the strict side; forms a 3-point expectancy curve (20/25/30) with sibling v0.8. Spawned by routine #4 Phase-1 autoloop 2026-05-16 (v0.4 ≥14d live, lower-direction perturbation untested, rack had open slots).

### Routine #7 wake log

- **2026-05-16 22:00 PT (first sim wake; spun up earlier today)** — past-24h replay window = 2026-05-15 10:00 UTC → 2026-05-16 10:00 UTC. Wakes: OVERNIGHT (05-15 13:00Z), MIDDAY (05-15 20:00Z, default-skip), EOD (05-16 04:00Z). Inherits v0.4 rules. M3 (reversal candle: 1H close > open) failed for all 15 universe pairs at BOTH eligible wakes — synchronized red crash bar 05-15 13:00Z, red universe-wide again at 05-16 04:00Z. M3 blocks before the strict RSI<20 floor (M2) is evaluated (and RSI<20 is rarer still). 0 entries, 0 open positions. All kill switches clear at $10,000 equity.
- **2026-05-29 22:00 PT** — past-24h replay window 2026-05-29 05:00 UTC → 2026-05-30 05:00 UTC. Kraken MCP OK (BTC/USD $73,183). Wakes evaluated: OVERNIGHT (13:00 UTC), MIDDAY (default-skip), EOD (04:00 UTC). At OVERNIGHT: M3 failed universe-wide (1H bar at 13:00 UTC red for all sampled pairs). At EOD: M3 passed BTC/SOL/HYPE/TAO/ADA; M2 (RSI < 20 — strict threshold) failed for all — computed RSI BTC≈55, SOL≈59, HYPE≈75, TAO≈50, ADA≈58, far from deeply oversold. 0 entries. No open positions. All kill switches clear at $10,000 synthetic equity.
- **2026-05-30 22:00 PT** — replay window 2026-05-30T05:00Z → 2026-05-31T05:00Z. Kraken MCP OK. OVERNIGHT and EOD: M3 passed for several pairs at EOD; M2 (RSI < 20 — strict threshold) failed all — market in broad recovery, RSI values ranging 55-80 across monitored pairs. 0 entries. Kill switches clear at $10,000. Days live: **15**.
- **2026-06-10 22:00 PT** *(partial-run — header/days updated but wake-log not written; retroactively captured here)* — 7-day cap replay 2026-06-04T05:00Z → 2026-06-11T05:00Z (prior rebuild 2026-05-31T05:00Z). Crash wakes: SBD active → 5a FAIL; M3 also failed (red bars). Recovery wakes 06-07→06-09: 5a PASS; M3 green for some pairs; M2 (RSI < 20 ultra-strict): recovering RSI 55-75 — far from deeply oversold. Post-recovery 06-09T13:00Z → tonight: SBD active → 5a FAIL. **0 entries.** Book flat. Kill switches clear at $10,000.
- **CORRECTION NOTE (2026-06-11 22:00 PT):** Prior entry labeled "2026-06-11 22:00 PT" was from the June 10 22:00 PT run. Mean-rev analysis unaffected by BTC close correction (M2 RSI<20 fails regardless: RSI 57.4 >> 20). 0-entry conclusion unchanged.
- **2026-06-10 22:00 PT (MISLABELED as 2026-06-11 22:00 PT — stale)** — **OVERNIGHT 2026-06-11T13:00Z:** SBD active; M2 (RSI<20) far from triggered. **EOD 2026-06-12T04:00Z:** SBD CLEARED, M3 PASSES (15/15 ✓), M2 (RSI<20): BTC ~57.9 → FAIL. **0 entries.** Kill switches clear at $10,000. Days live: 27.
- **2026-06-11 22:00 PT (this wake)** — **EOD 2026-06-12T04:00Z (confirmed):** SBD CLEARED ✓; M3 PASSES (15/15 green ✓); M2 (RSI < 20 ultra-strict): BTC RSI 57.4 — nowhere near 20. **0 entries.** Ultra-strict RSI<20 threshold makes entries extremely rare; no pair remotely oversold in broad-positive tape. Kill switches clear at $10,000. Days live: **27**.
- **2026-06-12 22:00 PT (routine-07)** — replay window 2026-06-12T06:45Z → 2026-06-13T05:00Z (~22h). **OVERNIGHT + EOD:** M2 (RSI < 20 ultra-strict): no pair anywhere near 20. **0 entries.** Kill switches all clear at $10,000. Days live: **28**.
- **2026-06-13 22:00 PT (routine-07)** — replay window 2026-06-13T05:08Z → 2026-06-14T05:00Z (~23.87h). **OVERNIGHT + EOD:** 15/15 positive at EOD, SBD CLEAR. M3 PASSES. M2 (RSI < 20 ultra-strict): universe RSI 48-76, nowhere near 20. **0 entries.** Ultra-strict threshold; next entry requires a sharp crash-level sell-off. Kill switches all clear at $10,000. Days live: **29**.
- **2026-06-24 PT (routine-07 — gap replay via routine07_replay_20260623.py; fired ~09:35 PT off-schedule)** — Replay window: **2026-06-14T05:00Z → 2026-06-24T13:00Z** (10.5 days). **All 12 wakes assessed: 0 entries.** RSI<20 ultra-strict threshold not remotely approached at any wake in the 10-day rally window. The June 24 SBD morning decline (RSI falling from highs): even with the sell-off, estimated universe RSI still in 35-55 range — well above the <20 floor. A/B vs siblings: all 3 mean-rev variants uniformly inactive. **OVERNIGHT 2026-06-24T13:00Z:** SBD, red bars → M3 FAIL. Kill switches all clear at $10,000. Days live: **39**.
- **2026-06-25 PT (routine-07, 2026-06-25T19:19Z — off-cron 12:19 PT)** — Watchdog ALL CLEAR. Kraken MCP OK. Replay window: 2026-06-24T16:35Z → 2026-06-25T19:19Z (~26.7h). Wakes evaluated: **EOD 2026-06-25T04:00Z**: 0/15 positive, SBD ACTIVE, M3 FAIL → 0 entries. **OVERNIGHT 2026-06-25T13:00Z**: BTC crashed −4.9%, SBD 5th consecutive wake, M3 FAIL → 0 entries. RSI<20 ultra-strict: universe RSI 38-55 during sell-off — nowhere near 20. Book flat. Kill switches all clear at $10,000. Days live: **40**.
- **2026-06-25 PT (routine-07, 2026-06-26T05:06Z — 22:05 PT on-schedule cron fire)** — Watchdog ALL CLEAR. Kraken MCP OK ($59,766.5 BTC). Replay window: 2026-06-25T19:19Z → 2026-06-26T05:06Z (~9.8h). MIDDAY 20:00Z: default skip. **EOD 2026-06-26T04:00Z**: 2/15 positive (SOL, HYPE), SBD briefly CLEARED. M2 (RSI<20 ultra-strict): SOL RSI ~54.4, HYPE ~53.7 — nowhere near 20; negative pairs M3 FAIL. Deepest reading: TRX RSI ~29.6 at 05:00Z bar (still >>20). **0 entries.** A/B vs v0.8/v0.4: identical 0-entry outcome. Kill switches all clear at $10,000. Days live: **40**.
- **2026-06-27 PT (routine-07, 2026-06-27T16:43Z — 09:43 PT OFF-SCHEDULE Saturday fire)** — Watchdog 1 finding (self-resolving). Kraken MCP OK (14/15 positive, median +1.60%, SBD CLEAR). Replay window: 2026-06-26T05:06Z → 2026-06-27T16:43Z (~35.6h). Wakes: all 3 fail M2 (RSI<20 ultra-strict). OVERNIGHT Jun27 13:00Z: SOL RSI 63.5, LTC 66.3 — far above threshold. **0 entries all 3 wakes.** Kill switches all clear at $10,000. Days live: **42**.
