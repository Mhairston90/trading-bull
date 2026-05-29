# Variant v0.9-mean-rev-tight — Synthetic Portfolio

> **Paper-paper account.** Synthetic $10K starting equity.
> **Category:** LAB-SWEEP (parameter sweep of v0.4, RSI threshold 25 → 20)
> **Last rebuild:** 2026-05-30T05:00:00Z (routine-07 wake 2026-05-29 22:00 PT — no trades; see notes)

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
- Promotion-eligible: 2026-06-15

## Notes

Parameter sweep — RSI oversold threshold 20 (vs v0.4's 25, v0.8's 30). Brackets the parent on the strict side; forms a 3-point expectancy curve (20/25/30) with sibling v0.8. Spawned by routine #4 Phase-1 autoloop 2026-05-16 (v0.4 ≥14d live, lower-direction perturbation untested, rack had open slots).

### Routine #7 wake log

- **2026-05-16 22:00 PT (first sim wake; spun up earlier today)** — past-24h replay window = 2026-05-15 10:00 UTC → 2026-05-16 10:00 UTC. Wakes: OVERNIGHT (05-15 13:00Z), MIDDAY (05-15 20:00Z, default-skip), EOD (05-16 04:00Z). Inherits v0.4 rules. M3 (reversal candle: 1H close > open) failed for all 15 universe pairs at BOTH eligible wakes — synchronized red crash bar 05-15 13:00Z, red universe-wide again at 05-16 04:00Z. M3 blocks before the strict RSI<20 floor (M2) is evaluated (and RSI<20 is rarer still). 0 entries, 0 open positions. All kill switches clear at $10,000 equity.
- **2026-05-29 22:00 PT** — past-24h replay window 2026-05-29 05:00 UTC → 2026-05-30 05:00 UTC. Kraken MCP OK (BTC/USD $73,183). Wakes evaluated: OVERNIGHT (13:00 UTC), MIDDAY (default-skip), EOD (04:00 UTC). At OVERNIGHT: M3 failed universe-wide (1H bar at 13:00 UTC red for all sampled pairs). At EOD: M3 passed BTC/SOL/HYPE/TAO/ADA; M2 (RSI < 20 — strict threshold) failed for all — computed RSI BTC≈55, SOL≈59, HYPE≈75, TAO≈50, ADA≈58, far from deeply oversold. 0 entries. No open positions. All kill switches clear at $10,000 synthetic equity.
