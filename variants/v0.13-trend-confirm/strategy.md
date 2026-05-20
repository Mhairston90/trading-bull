# BULL Strategy — Variant v0.13-trend-confirm

> **Variant strategy file. Self-contained.**
> **Status:** active LAB (hypothesis) variant, spun up 2026-05-20
> **Lineage:** modification of main v0.3 (W21-F base). Tightens entry rule 1 to 2 consecutive 1H closes > 20-EMA, adds 4H RSI ≥ 50 confirmation. All other rules verbatim.
> **Source:** trade_log whipsaw analysis 2026-05-20 (interactive session).

## Philosophy

Same as v0.3 — minimal long-only momentum baseline, single `momentum` bucket. The only change tightens entry quality: a single 1H close above the 20-EMA is too noisy as an entry trigger (9 of 17 main closes are −1R whipsaws inside 21h of entry). Two consecutive 1H closes above the 20-EMA, with 4H RSI confirming the higher-timeframe trend, filters those bars out.

## Universe

Read from `memory/universe.md` (same as v0.3).

## Entries (long-only)

Enter LONG when **all** of the following are true on a just-closed 1H candle:

1. **(v0.13 modified)** **The just-closed 1H AND the prior 1H both close > 1H 20-EMA.** (v0.3 required only the just-closed bar above; v0.13 requires two consecutive closes above to demonstrate persistence rather than a single-bar tag.)
2. 1H RSI(14) > 55
2a. 1H RSI(14) ≤ 80 (combined: 55 < RSI14 ≤ 80) — unchanged
3. 4H close > 4H 50-EMA — unchanged
3a. **(v0.13 added)** **4H RSI(14) ≥ 50** at entry-scan. Cross-timeframe trend-confirmation; rejects entries where the 4H is still in net mean-reverting territory despite a 4H close above the 50-EMA.
4. Pair has ≥ 10 candles of history on both 1H and 4H — unchanged
4a. Pair 24h notional volume ≥ $2.0M USD — unchanged
5. No existing open position in this pair — unchanged
5a. Regime-confirmation gate (≥ 4/15 universe pairs positive 24h, else reject all entries this wake) — unchanged
5a-SBD. Synchronized-breakdown sub-state (≤ 1/15 positive AND median ≤ −1.0%) — unchanged
5b. Same-pair re-entry cooldown (no new position within 24h of an `exit-stop-hit` on that pair) — unchanged
6. Current open positions < 4 — unchanged
6a. Concurrent positions in BTC-correlated cluster {BTC, ETH, SOL, TAO, AVAX, SUI, LINK} ≤ 2 — unchanged
7. Portfolio risk-at-moment + this trade's risk ≤ 4% — unchanged
8. Max 1 new entry per routine wake (tie-break: highest 30d notional rank) — unchanged

## Position sizing

Identical to v0.3: risk per trade 1.5% of equity; initial stop distance 2 × ATR(14) on 1H; size = (equity × 0.015) / stop distance, rounded down to Kraken minimum lot.

## Exits

Identical to v0.3 (inherits W21-F amendments verbatim):

1. 1H close < 1H 20-EMA
1-SBD. While regime = SYNCHRONIZED_BREAKDOWN per rule 5a-SBD, exit rule 1 tightens to: 1H close < 1H 9-EMA
2. Price hits the 2 × ATR(14) stop (set at entry, static)
3. Unrealized PnL ≥ 4R (take profit)

Exits checked at the close of each 1H candle. No intra-bar exits.

## Concept buckets declared

`momentum: 100%`, same as v0.3. Variant-internal — does not affect main allocation.

## Variant-specific tracking

Files in `variants/v0.13-trend-confirm/`. Compared to v0.3 (main) on `memory/leaderboard.md`. Sibling **entry-quality** variant (none yet); siblings on the **exit-quality** axis: v0.10-exit-confirm, v0.11-breakeven-2R, v0.12-sbd-exit.

## Promotion path

Standard. Earliest 2026-06-19. Ring-2 `[Y/N]` required for promotion to main.
