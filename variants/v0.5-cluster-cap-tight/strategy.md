# BULL Strategy — Variant v0.5-cluster-cap-tight

> **Variant strategy file. Self-contained.**
> **Status:** active LAB variant, spun up 2026-04-29
> **Diff vs main v0.2:** rule 6a cluster cap reduced from `<= 2` to `<= 1`. All other rules unchanged.
> **Subject to mandate:** all hard floors in `memory/guardrails.md` apply unmodified.

## Philosophy

Same as main v0.2: long-only momentum baseline. Tightens cluster cap to test whether further tail-risk reduction beats main's marginally-higher trend capture.

## Universe

Read from `memory/universe.md`. Same as main.

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
6. Current open positions < 4
**6a. (v0.5 MODIFIED)** Concurrent positions in the BTC-correlated cluster `{BTC, ETH, SOL, TAO, AVAX, SUI, LINK}` <= **1** (vs main's 2). Tightens W18-A cap further; rationale per variant README — tail-risk reduction at cost of foregone trend capture in cluster rallies.
7. Portfolio risk-at-moment + this trade's risk <= 4%
8. Max 1 new entry per routine wake (W18-C)

## Position sizing

- Risk per trade: 1.5% of current variant equity
- Stop distance: 2 × ATR(14) on 1H
- Size = (equity × 0.015) / stop distance, rounded down to Kraken minimum lot

Same as main v0.2.

## Exits

Exit the position when **any** of the following is true:

1. 1H close < 1H 20-EMA
2. Price hits the 2 × ATR(14) stop (set at entry, static)
3. Unrealized PnL >= 4R (take profit)

Same as main v0.2.

## Concept buckets

- `momentum`: 100%
- `mean-reversion`: 0%
- `news-reactive`: 0%

Same as main.

## Variant-specific tracking

- Synthetic equity, portfolio, and trade log live in `variants/v0.5-cluster-cap-tight/`
- Routine #7 (variant-paper) replays past 24h Kraken bars daily at 22:00 PT
- Performance reported on `memory/leaderboard.md`

## Promotion path

Eligible at routine #4 Saturday when standard criteria pass. Earliest: 2026-05-29. May require longer evidence window than other variants since cluster events are infrequent.
