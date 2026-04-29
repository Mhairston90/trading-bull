# BULL Strategy — Variant v0.3-vol-compression

> **Variant strategy file. Self-contained — does NOT inherit from main `memory/strategy.md`.**
> **Status:** active LAB variant, spun up 2026-04-29
> **Diff vs main v0.2:** adds rule 5c (volatility-compression gate). All other rules unchanged.
> **Subject to mandate:** all hard floors in `memory/guardrails.md` apply unmodified.

## Philosophy

Same as main v0.2: long-only momentum baseline on 1H/4H Kraken spot. Adds a regime gate to skip entries during compressed-volatility periods that historically produce range-bound chop.

## Universe

Read from `memory/universe.md` (top 15 Kraken USD pairs, refreshed monthly). Same as main.

## Entries (long-only)

Enter LONG when **all** of the following are true on a just-closed 1H candle:

1. 1H close > 1H 20-EMA
2. 1H RSI(14) > 55
2a. 1H RSI(14) <= 80 at entry-scan close. Combined: entry requires 55 < RSI14 <= 80.
3. 4H close > 4H 50-EMA
4. Pair has >= 10 candles of history on both 1H and 4H (no ultra-fresh listings)
4a. Pair has 24h notional volume >= $2.0M USD at time of entry-scan, measured from Kraken MCP `kraken_ticker`.
5. No existing open position in this pair (within this variant's portfolio)
5a. Regime-confirmation gate: at entry-scan time, count universe pairs with positive 24h % change. If < 4 of 15 are positive, reject all new entries this wake.
5b. Same-pair re-entry cooldown: do not open a new position in a pair within 24h of a stop-out (`exit-stop-hit`) on that pair (within this variant's portfolio).
**5c. (v0.3 NEW) Volatility-compression gate:** at entry-scan time, compute current 1H ATR(14) and mean 1H ATR(14) over past **720 bars** (~30 days). If `current_ATR / mean_ATR < 0.5`, reject all new entries this wake. Hypothesis: low ATR vs. trailing mean precedes range-bound chop where momentum strategies underperform. Source: IDEA-20260429-04 (Glassnode RV/IV claim) + lesson 2026-04-27 cascade option (c). Threshold 0.5 is initial pick subject to routine #4 backtest sweep.
6. Current open positions < 4 (variant uses same half-cap as main v0.2)
6a. Concurrent positions in the BTC-correlated cluster {BTC, ETH, SOL, TAO, AVAX, SUI, LINK} <= 2.
7. Portfolio risk-at-moment + this trade's risk <= 4% (within this variant's portfolio)
8. Max 1 new entry per routine wake. If multiple pairs are eligible at the same wake, prefer the highest-ranked pair by 30d notional rank.

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

Exits are checked at the close of each 1H candle. No intra-bar exits. Same as main v0.2.

## Concept buckets

- `momentum`: 100%
- `mean-reversion`: 0%
- `news-reactive`: 0%

Same as main. Variant tests an entry filter, not a bucket reallocation.

## Variant-specific tracking

- Synthetic equity, portfolio, and trade log live in `variants/v0.3-vol-compression/`
- Routine #7 (variant-paper) replays past 24h Kraken bars and applies these rules daily at 22:00 PT
- Performance reported on `memory/leaderboard.md` alongside main v0.2

## Promotion path

Variant is eligible for promotion proposal at routine #4 Saturday when ALL hold:
- ≥ 30 days live (earliest: 2026-05-29)
- Beats main on net return over rolling 30d
- Beats main on profit factor over rolling 30d
- Max DD does not exceed main's DD by > 25%
- ≥ 10 trades in rolling 30d window

If promoted via Ring-2 `[Y]`, this strategy.md replaces `memory/strategy.md` with version bump.
