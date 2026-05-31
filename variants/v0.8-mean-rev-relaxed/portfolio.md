# Variant v0.8-mean-rev-relaxed — Synthetic Portfolio

> **Paper-paper account.** Synthetic $10K starting equity.
> **Category:** LAB-SWEEP (parameter sweep of v0.4, RSI threshold 25 → 30)
> **Last rebuild:** 2026-05-31T05:00:00Z (routine-07 wake 2026-05-30 22:00 PT — no trades; see notes)

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

### Routine #7 wake log

- **2026-05-16 22:00 PT (first sim wake since 05-12 spin-up)** — past-24h replay window = 2026-05-15 10:00 UTC → 2026-05-16 10:00 UTC. Wakes: OVERNIGHT (05-15 13:00Z), MIDDAY (05-15 20:00Z, default-skip), EOD (05-16 04:00Z). Inherits v0.4 rules. M3 (reversal candle: 1H close > open) failed for all 15 universe pairs at BOTH eligible wakes — synchronized red crash bar 05-15 13:00Z, red universe-wide again at 05-16 04:00Z. M3 blocks before the relaxed RSI<30 floor (M2) is evaluated. 0 entries, 0 open positions. All kill switches clear at $10,000 equity.
- **2026-05-29 22:00 PT** — past-24h replay window 2026-05-29 05:00 UTC → 2026-05-30 05:00 UTC. Kraken MCP OK (BTC/USD $73,183). Wakes evaluated: OVERNIGHT (13:00 UTC), MIDDAY (default-skip), EOD (04:00 UTC). At OVERNIGHT: M3 failed universe-wide (1H bar at 13:00 UTC red for all sampled pairs). At EOD: M3 passed BTC/SOL/HYPE/TAO/ADA; M2 (RSI < 30) failed for all — computed RSI BTC≈55, SOL≈59, HYPE≈75, TAO≈50, ADA≈58, none near oversold. 0 entries. No open positions. All kill switches clear at $10,000 synthetic equity.
- **2026-05-30 22:00 PT** — replay window 2026-05-30T05:00Z → 2026-05-31T05:00Z. Kraken MCP OK. OVERNIGHT: M3 checked — HYPE 13:00Z bar red (68.34→68.06); BTC/SOL/TAO green but M2 (RSI < 30) fails — BTC RSI ~62, SOL RSI ~55, TAO RSI ~59. EOD: M3 passed for BTC/SOL/TAO/HYPE; M2 (RSI < 30): BTC RSI ~70, HYPE RSI ~60, TAO RSI ~62, SOL RSI ~65 — all far above the relaxed 30 threshold. 0 entries. Kill switches clear at $10,000. Days live: **19**.
