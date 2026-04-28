# BULL Strategy — v0.1 (W18 amended 2026-04-28)

> **Gated file.** BULL may propose edits only via weekly memo → Telegram `[Y/N]`. Never edit autonomously.
> **Version:** v0.1
> **Last approved:** 2026-04-28 (off-cycle W18 proposal — A: cluster cap, B: liquidity floor, C: one-per-wake)
> **Prior version:** v0-seed (2026-04-20 standup)
> **Next review:** routine #4, first Saturday post-application (2026-05-02)

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
4a. **(W18-B)** Pair has 24h notional volume >= **$2.0M USD** at time of entry-scan, measured from Kraken MCP `kraken_ticker`. Filters out thin-liquidity pairs whose 1H bars wick beyond 2×ATR stops (lesson 2026-04-24 TRX). Pairs currently affected: FARTCOIN, AVAX, LINK, PENGU, TRX (re-evaluated each entry-scan, not statically blocked).
5. No existing open position in this pair
6. Current open positions < 4 (v0 deliberately uses half the 8-position cap)
6a. **(W18-A)** Concurrent positions in the BTC-correlated cluster `{BTC, ETH, SOL, TAO, AVAX, SUI, LINK}` <= **2**. Empirically these pairs move together on 1H (cascade event 2026-04-27T05:00Z stopped 4/4 cluster positions in a single bar). Cap limits worst-case correlated tail loss to ~2R.
7. Portfolio risk-at-moment + this trade's risk <= 4%
8. **(W18-C)** Max **1** new entry per routine wake. If multiple pairs are eligible at the same wake, prefer the pair with **highest 30d notional rank** (i.e., XBT > ETH > SOL > TAO etc. per `memory/universe.md`). Remaining eligible entries re-evaluated at next wake; if no longer eligible (e.g., RSI dropped below 55), they are skipped — this is intentional, the rule is meant to prevent same-bar cluster fills.

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
