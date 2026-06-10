# BULL Strategy — Variant v0.14-recovery-trend

> **Variant strategy file. Self-contained.**
> **Status:** active LAB (hypothesis) variant, spun up 2026-06-09 (interactive, user-requested)
> **Lineage:** modification of main v0.4. Entry rule 3 uses the 4H **20-EMA** (vs main's 50-EMA). All other rules — including W19-D gates, W21-F SBD, W22 exits/stop management — inherited verbatim.
> **Source:** mcp-outage gap replay 2026-06-09 — recovery wakes 06-07→06-09 had regime 8-14/15 positive but 0/15 pairs passing rule 3 under the 50-EMA.

## Philosophy

Same as v0.4 — long-only momentum. The single change tests whether a faster 4H trend filter converts confirmed regime recoveries into trades weeks before the 50-EMA catches down to post-crash prices, without giving up crash protection (5a/SBD gates unchanged).

## Universe

Read from `memory/universe.md` (top 15 Kraken USD pairs, refreshed monthly).

## Entries (long-only)

Enter LONG when **all** of the following are true on a just-closed 1H candle:

1. 1H close > 1H 20-EMA
2. 1H RSI(14) > 55
2a. 1H RSI(14) <= 80 (W19-D) — combined: **55 < RSI14 <= 80**
3. **(v0.14 MODIFIED)** 4H close > 4H **20-EMA** (main v0.4 uses the 50-EMA; this is the only rule change)
4. Pair has >= 10 candles of history on both 1H and 4H
4a. Pair has 24h notional volume >= $2.0M USD at entry-scan (W18-B)
5. No existing open position in this pair
5a. Regime-confirmation gate (W19-D): >= 4 of 15 universe pairs positive 24h, else reject all entries this wake
5a-SBD. (W21-F) Synchronized-breakdown sub-state: <= 1/15 positive AND median 24h <= -1.0% → SBD; triggers Exit rule 1-SBD; clears automatically
5b. Same-pair re-entry cooldown: 24h after an `exit-stop-hit` (W19-D)
6. Current open positions < 4
6a. BTC-correlated cluster {BTC, ETH, SOL, TAO, AVAX, SUI, LINK} <= 2 concurrent (W18-A)
7. Portfolio risk-at-moment + this trade's risk <= 4%
8. Max 1 new entry per routine wake; prefer highest 30d notional rank (W18-C)

## Position sizing

- Risk per trade: 1.5% of current variant equity
- Stop distance: 2 × ATR(14) on 1H
- Size = (equity × 0.015) / stop distance, rounded down to Kraken minimum lot

## Stop management (W22-H-partial, inherited)

- Once unrealized R ≥ 2.0 at any 1H close, move the stop to entry (breakeven). Ratchets up only; no further trailing.

## Exits (inherited from v0.4 unchanged)

1. (W22-G) Two consecutive 1H closes < 1H 20-EMA — fires on the second below-EMA close
1-SBD. (W21-F) While SBD active: two consecutive 1H closes < 1H **9-EMA**; reverts when SBD clears
2. Price hits the active stop (initial 2×ATR, or entry after breakeven ratchet)
3. Unrealized PnL ≥ 4R (take profit)

Exits checked at the close of each 1H candle. No intra-bar exits.

## Concept buckets declared

- `momentum`: 100%

## Variant-specific tracking

Files in `variants/v0.14-recovery-trend/`. Compared to main v0.4 on `memory/leaderboard.md`. The A/B question vs main: do early recovery entries (20-EMA passes, 50-EMA fails) net positive after dead-cat-bounce losers?
