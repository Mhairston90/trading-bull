# BULL Strategy — Variant v0.15-meanrev-guarded

> **Variant strategy file. Self-contained.**
> **Status:** active LAB (hypothesis) variant, spun up 2026-06-09 (interactive, user-requested)
> **Lineage:** v0.4-mean-reversion-sleeve rules with v0.8's relaxed RSI floor (30) plus a new SBD entry guard. Direct A/B sibling of v0.8 (only diff: the guard).
> **Source:** gap replay 2026-06-09 — v0.8's NEAR/USD −1.00R knife-catch entered at a 0/15-positive, median −6.15% SBD wake.

## Philosophy

Long-only mean reversion on 1H oversold conditions in 4H-uptrending pairs — but never inside a synchronized breakdown. Oversold in a functioning tape is a spring; oversold in a cascade is a knife.

## Universe

Read from `memory/universe.md`. Same as main.

## Entries (long-only mean-reversion)

**M1.** 4H close > 4H 200-EMA (long-term structural uptrend confirmed; inherited)
**M2.** 1H RSI(14) < **30** (v0.8's relaxed floor; parent v0.4 uses 25)
**M3.** 1H close > previous 1H low AND 1H close > 1H open (reversal candle; inherited)
**M4.** 24h notional volume >= $2.0M USD at entry-scan (inherited)
**M5.** No existing open position in this pair (inherited)
**M6.** Current open positions in this variant < 2 (inherited)
**M7.** Portfolio risk-at-moment + this trade's risk <= 4% (inherited)
**M8.** Max 1 new entry per routine wake (inherited)
**M-guard. (v0.15 NEW)** Reject all entries while regime = SYNCHRONIZED_BREAKDOWN: **<= 1 of 15** universe pairs positive on 24h % change AND median 24h % change **<= -1.0%** (same classifier as main rule 5a-SBD). Re-evaluated at every wake; clears automatically. Rationale: the only mean-rev signal in 41 days (NEAR 2026-06-05) fired in deep SBD and lost −1R in 4 hours; cascades produce serially-correlated downside that defeats single-bar reversal evidence.

## Position sizing

Inherited from v0.4: 1.5% risk/trade, 1.5×ATR(14) stop on 1H. Size = (equity × 0.015) / stop distance.

## Exits

Inherited from v0.4:
- X1. 1H close >= 1H 20-EMA (target)
- X2. 1.5×ATR stop (intra-bar, at stop price, per v0.2 convention)
- X3. 24-bar time stop

## Concept buckets declared

`mean-reversion: 100%`. Variant-internal — doesn't affect main's allocation.

## Variant-specific tracking

Files in `variants/v0.15-meanrev-guarded/`. Compared on `memory/leaderboard.md` to v0.8 (the no-guard A/B), v0.4 (parent), and v0.9. Every trade v0.8 takes that v0.15 skips (or vice versa) is a clean guard datum.
