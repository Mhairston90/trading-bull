# BULL Strategy — Variant v0.9-mean-rev-tight

> **Variant strategy file. Self-contained.**
> **Status:** active LAB-SWEEP variant, spun up 2026-05-16
> **Lineage:** parameter sweep of v0.4-mean-reversion-sleeve. `rsi_oversold_threshold` changed from 25 to **20**.

## Philosophy

Same as v0.4 — long-only mean-reversion on 1H oversold conditions in 4H-uptrending pairs. Sweep tests a stricter (deeper-capitulation) RSI threshold.

## Universe

Same as v0.4.

## Entries (long-only mean-reversion)

**M1.** 4H close > 4H 200-EMA (inherited)
**M2. (v0.9 SWEEP)** 1H RSI(14) **< 20** (vs parent v0.4's < 25). Deep-capitulation floor.
**M3.** 1H close > previous 1H low AND 1H close > 1H open (inherited)
**M4.** 24h notional volume >= $2.0M USD (inherited)
**M5.** No existing open position in this pair (inherited)
**M6.** Current open positions in this variant < 2 (inherited)
**M7.** Portfolio risk-at-moment + this trade's risk <= 4% (inherited)
**M8.** Max 1 new entry per routine wake (inherited)

## Position sizing

Inherited from v0.4: 1.5% risk/trade, 1.5×ATR(14) stop on 1H.

## Exits

Inherited from v0.4:
- X1. 1H close >= 1H 20-EMA (target)
- X2. 1.5×ATR stop
- X3. 24-bar time stop

## Concept buckets

`mean-reversion: 100%`, same as v0.4. Variant-internal — doesn't affect main.

## Variant-specific tracking

Files in `variants/v0.9-mean-rev-tight/`. Compared to v0.4 (parent) and v0.8 (sibling sweep) on leaderboard.

## Promotion path

Standard. Earliest 2026-06-15.
