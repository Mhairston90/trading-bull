# Variant v0.8-mean-rev-relaxed — Synthetic Portfolio

> **Paper-paper account.** Synthetic $10K starting equity.
> **Category:** LAB-SWEEP (parameter sweep of v0.4, RSI threshold 25 → 30)
> **Last rebuild:** 2026-06-24T16:35Z (routine-07 wake 2026-06-24 PT — 0 entries across all 12 wakes in replay window; RSI 48-76 throughout, far above M2 RSI<30 threshold; 1 closed trade lifetime)

## Account

- Starting equity: **$10,000.00**
- Cash: **$9,850.00**
- Realized PnL: **-$150.00** (NEAR/USD -1.00R, closed 2026-06-05T08:00Z)
- Unrealized PnL: **$0.00**
- Current equity: **$9,850.00**
- Equity peak: **$10,000.00**
- Drawdown: **1.50%**

## Open positions

(none — NEAR/USD closed 2026-06-05T08:00Z exit-stop-hit)

Open positions: **0 / 2** (mean-reversion sized smaller than momentum, inherited from v0.4).

## Active kill-switch state

All clear at $9,850.00 equity. DD 1.50% well under caps.

## Rolling performance vs main v0.2 AND parent v0.4

| Window | v0.8 return | v0.4 (parent) return | v0.2 (main) return | Verdict |
|--------|-------------|----------------------|---------------------|---------|
| 7d  | — | — | — | not yet 7 days live |
| 30d | — | — | — | not yet 30 days live (earliest 2026-06-11) |

## Days live

- Spin-up: 2026-05-12
- As of last rebuild: **43 days**
- Promotion-eligible: **2026-06-11 (reached)** — 1 closed trade in rolling 30d (NEAR −1R) — below 10-trade minimum → NOT promotion-eligible; variant continues in LAB.

## Notes

Parameter sweep — RSI oversold threshold 30 (vs v0.4's 25). Tests whether v0.4 is over-filtering oversold candidates. Today's 2026-05-12 OVERNIGHT wake noted PENGU/USD hit RSI 25.4 — just above v0.4's threshold. v0.8 would have considered PENGU that wake (but other rules including M1 4H>200-EMA still apply).

### Routine #7 wake log

- **2026-05-16 22:00 PT (first sim wake since 05-12 spin-up)** — past-24h replay window = 2026-05-15 10:00 UTC → 2026-05-16 10:00 UTC. Wakes: OVERNIGHT (05-15 13:00Z), MIDDAY (05-15 20:00Z, default-skip), EOD (05-16 04:00Z). Inherits v0.4 rules. M3 (reversal candle: 1H close > open) failed for all 15 universe pairs at BOTH eligible wakes — synchronized red crash bar 05-15 13:00Z, red universe-wide again at 05-16 04:00Z. M3 blocks before the relaxed RSI<30 floor (M2) is evaluated. 0 entries, 0 open positions. All kill switches clear at $10,000 equity.
- **2026-05-29 22:00 PT** — past-24h replay window 2026-05-29 05:00 UTC → 2026-05-30 05:00 UTC. Kraken MCP OK (BTC/USD $73,183). Wakes evaluated: OVERNIGHT (13:00 UTC), MIDDAY (default-skip), EOD (04:00 UTC). At OVERNIGHT: M3 failed universe-wide (1H bar at 13:00 UTC red for all sampled pairs). At EOD: M3 passed BTC/SOL/HYPE/TAO/ADA; M2 (RSI < 30) failed for all — computed RSI BTC≈55, SOL≈59, HYPE≈75, TAO≈50, ADA≈58, none near oversold. 0 entries. No open positions. All kill switches clear at $10,000 synthetic equity.
- **2026-05-30 22:00 PT** — replay window 2026-05-30T05:00Z → 2026-05-31T05:00Z. Kraken MCP OK. OVERNIGHT: M3 checked — HYPE 13:00Z bar red (68.34→68.06); BTC/SOL/TAO green but M2 (RSI < 30) fails — BTC RSI ~62, SOL RSI ~55, TAO RSI ~59. EOD: M3 passed for BTC/SOL/TAO/HYPE; M2 (RSI < 30): BTC RSI ~70, HYPE RSI ~60, TAO RSI ~62, SOL RSI ~65 — all far above the relaxed 30 threshold. 0 entries. Kill switches clear at $10,000. Days live: **19**.
- **2026-06-09 interactive (user-directed mcp-outage gap replay)** — 9 missed routine-07 wakes recovered from Kraken public REST bars. **FIRST TRADE for this variant — and the only missed entry in the entire rack during the outage: NEAR/USD long 1087.076038 @ 2.1241 at the 2026-06-05T04:00Z EOD wake** (M1 ✓ 4H close > 4H 200-EMA — NEAR's late-May rally kept it above its long EMA while everything else crashed below; M2 ✓ RSI 26.9 < 30 — crash-day oversold; M3 ✓ reversal candle close 2.1241 > prev low 2.1129 and > open 2.1224; M4 ✓ $26.8M vol). Stop 1.986115 (1.5×ATR 0.137985). **CLOSED 2026-06-05T08:00Z @ 1.986115 exit-stop-hit, −1.00R, −$150.00** — the 06-05 crash leg (universe median −6.15% that wake) ran straight through the reversal candle in 4 hours. **Sweep datum vs parent/siblings: parent v0.4 (RSI<25) and v0.9 (RSI<20) did NOT take this trade (RSI 26.9 above neither threshold)** — first divergence evidence in the sweep, and it favors the tighter thresholds: the relaxed floor bought a knife-catch in a synchronized breakdown. Equity $9,850.00, book flat. Audit: `scripts/mcp_outage_replay_20260609.py`.
- **CORRECTION NOTE (2026-06-11 22:00 PT):** Prior entry labeled "2026-06-11 22:00 PT" was from the June 10 22:00 PT run. Mean-rev analysis unaffected by BTC close correction (M2 RSI<30 fails regardless: RSI 57.4 >> 30). 0-entry conclusion unchanged.
- **2026-06-10 22:00 PT (MISLABELED as 2026-06-11 22:00 PT — stale)** — Wakes: OVERNIGHT (2026-06-10T13:00Z), EOD (2026-06-11T04:00Z), OVERNIGHT (2026-06-11T13:00Z), EOD (2026-06-12T04:00Z). SBD active at all 3 prior-wakes → M3 FAIL or M2 FAIL. EOD 2026-06-12T04:00Z: SBD CLEARED, M3 PASSES, M2 (RSI<30) BTC RSI ~57.9 FAIL. **0 entries.** Kill switches clear at $9,850. Days live: 31.
- **2026-06-11 22:00 PT (this wake)** — **EOD 2026-06-12T04:00Z (confirmed):** SBD CLEARED ✓; M3 PASSES (15/15 green ✓); M2 (RSI < 30): BTC 1H RSI 57.4 >> 30; NEAR RSI elevated in bounce; no pair near oversold. M2 failure is the binding constraint. **0 entries.** A/B vs sibling v0.9/v0.4: all mean-rev variants uniformly 0-entry in broad-positive tape; next divergence will occur at a deeply oversold wake (RSI 20-30 range). Kill switches all clear at $9,850. Days live: **31**.
- **2026-06-12 22:00 PT (routine-07)** — replay window 2026-06-12T06:45Z → 2026-06-13T05:00Z (~22h). **OVERNIGHT 2026-06-12T13:00Z:** M2 (RSI < 30): no pair near oversold. 0 entries. **EOD 2026-06-13T04:00Z:** 4/15 positive, SBD CLEAR. M3 PASSES. M2 (RSI < 30): TAO 1H RSI 62.5 >> 30; universe-wide RSI elevated. **0 entries.** Kill switches all clear at $9,850. Days live: **32**.
- **2026-06-13 22:00 PT (routine-07)** — replay window 2026-06-13T05:08Z → 2026-06-14T05:00Z (~23.87h). **OVERNIGHT + EOD:** M3 PASSES (green bars across regime). M2 (RSI < 30): universe RSI 48-76 range across 15/15 positive tape — no pair approaching oversold at the 30 threshold; TAO RSI ~76, BTC RSI ~55 both well above 30. **0 entries.** A/B vs siblings v0.4 (RSI<25) and v0.9 (RSI<20): all mean-rev variants uniformly 0-entry in broad-rallying tape. Next divergence requires RSI<30 pull-back, likely in a reversal or ranging wake. Kill switches all clear at $9,850. Days live: **33**.
- **2026-06-24 PT (routine-07 — gap replay via routine07_replay_20260623.py; fired ~09:35 PT off-schedule)** — Replay window: **2026-06-14T05:00Z → 2026-06-24T13:00Z** (10.5 days). **All 12 wakes assessed: 0 entries.** June 14–22 broad-rally tape: universe RSI 48-76+ range throughout; M2 (RSI<30 relaxed threshold) failed at every wake. No pull-back below RSI 30 even at intraday lows. A/B vs v0.4 (RSI<25) and v0.9 (RSI<20): all three mean-rev variants uniformly 0-entry. **OVERNIGHT 2026-06-24T13:00Z:** SBD active, red bars → M3 FAIL → 0 entries. Kill switches all clear at $9,850. Days live: **43**.
