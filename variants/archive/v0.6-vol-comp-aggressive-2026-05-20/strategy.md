# BULL Strategy — Variant v0.6-vol-comp-aggressive

> **Variant strategy file. Self-contained.**
> **Status:** active LAB-SWEEP variant, spun up 2026-05-12
> **Lineage:** parameter sweep of v0.3-vol-compression. `vol_compression_threshold` changed from 0.5 to **0.3**. All other rules identical to v0.3.
> **Subject to mandate:** all hard floors in `memory/guardrails.md` apply unmodified.

## Philosophy

Same as v0.3: long-only momentum baseline with a vol-compression entry gate. This sweep variant tests a more lenient threshold (0.3 vs v0.3's 0.5) — only block entries during *extreme* compression rather than during *any* below-average ATR.

## Universe

Read from `memory/universe.md`. Same as parent.

## Entries (long-only)

Enter LONG when **all** of the following are true on a just-closed 1H candle:

1. 1H close > 1H 20-EMA
2. 1H RSI(14) > 55
2a. 1H RSI(14) <= 80 (W19-D)
3. 4H close > 4H 50-EMA
4. Pair has >= 10 candles of history on both 1H and 4H
4a. Pair has 24h notional volume >= $2.0M USD (W18-B)
5. No existing open position in this pair (within this variant's portfolio)
5a. Regime-confirmation gate: ≥ 4 of 15 universe pairs positive 24h (W19-D)
5b. Same-pair re-entry cooldown: 24h (W19-D)
**5c. (v0.6 SWEEP)** Volatility-compression gate: compute current 1H ATR(14) and mean 1H ATR(14) over past 720 bars. If `current_ATR / mean_ATR < 0.3` → reject. **Threshold 0.3** (vs parent v0.3's 0.5). Source: Phase 1 autoloop parameter sweep, lower-bound perturbation. Tests whether v0.3's threshold is over-filtering normal-vol regimes.
6. Current open positions < 4
6a. Concurrent positions in BTC-correlated cluster {BTC, ETH, SOL, TAO, AVAX, SUI, LINK} <= 2
7. Portfolio risk-at-moment + this trade's risk <= 4%
8. Max 1 new entry per routine wake (W18-C)

## Position sizing, exits, concept buckets

Identical to v0.3 (which inherited from v0.2). 1.5% risk per trade, 2×ATR stop, 4R target, 1H EMA-cross exit, `momentum: 100%`.

## Variant-specific tracking

- Synthetic equity/portfolio/trade-log live in `variants/v0.6-vol-comp-aggressive/`
- Routine #7 daily replays
- Performance compared to v0.3 (parent) and v0.7 (sibling sweep) on `memory/leaderboard.md`

## Promotion path

Standard. Earliest 2026-06-11.
