# BULL Strategy — v0 seed (locked 2026-04-20)

> **Gated file.** BULL may propose edits only via weekly memo → Telegram `[Y/N]`. Never edit autonomously.
> **Version:** v0-seed
> **Last approved:** 2026-04-20 (standup)
> **Next review:** routine #4, first Saturday post-standup

## Philosophy

Minimal momentum baseline. Long-only. One concept bucket (`momentum`). Expected to evolve in week 1.

## Universe

Read from `memory/universe.md` (top 15 Kraken USD pairs, refreshed monthly).

## Entries (long-only)

Enter LONG when **all** of the following are true on a just-closed 1H candle:

1. 1H close > 1H 20-EMA
2. 1H RSI(14) > 55
3. 4H close > 4H 50-EMA
4. Pair has >= 10 candles of history on both 1H and 4H (no ultra-fresh listings)
5. No existing open position in this pair
6. Current open positions < 4 (v0 deliberately uses half the 8-position cap)
7. Portfolio risk-at-moment + this trade's risk <= 4%

## Position sizing

- Risk per trade: 1.5% of current equity
- Stop distance: 2 × ATR(14) on 1H
- Size = (equity × 0.015) / stop distance, rounded down to Kraken minimum lot

## Exits

Exit the position when **any** of the following is true:

1. 1H close < 1H 20-EMA
2. Price hits the 2 × ATR(14) stop (set at entry, static)
3. Unrealized PnL >= 4R (take profit)

Exits are checked at the close of each 1H candle. No intra-bar exits.

## Concept buckets declared

- `momentum`: 100%
- `mean-reversion`: 0%
- `news-reactive`: 0%

(These buckets are referenced by routine #5 allocation review. Shifts >20% between buckets are Ring 2 gated.)

## Known limitations of v0

- Long-only — misses downtrends
- Single entry signal — low diversity of edge
- No regime filter — will likely overtrade in chop
- No news awareness — mandate allows, v0 ignores

These are intentional. Routine #4 will propose upgrades with backtested evidence.
