# BULL Strategy — Variant v0.11-breakeven-2R

> **Variant strategy file. Self-contained.**
> **Status:** active LAB (hypothesis) variant, spun up 2026-05-16
> **Lineage:** modification of main v0.2. Adds a breakeven stop-ratchet at `breakeven_trigger_R` = 2.0R unrealized.
> **Source:** lessons.md 2026-05-15 profit-give-back (score 9).

## Philosophy

Same as v0.2 — minimal long-only momentum baseline, single `momentum` bucket. The only change adds profit-protection: once a trade is up ≥2R, its stop ratchets to breakeven so a matured winner cannot round-trip into a loss.

## Universe

Read from `memory/universe.md` (same as v0.2).

## Entries (long-only)

Identical to v0.2. Enter LONG when **all** are true on a just-closed 1H candle:

1. 1H close > 1H 20-EMA
2. 1H RSI(14) > 55
2a. 1H RSI(14) <= 80 (combined: 55 < RSI14 <= 80)
3. 4H close > 4H 50-EMA
4. Pair has >= 10 candles of history on both 1H and 4H
4a. Pair 24h notional volume >= $2.0M USD at entry-scan (Kraken `kraken_ticker`)
5. No existing open position in this pair
5a. Regime-confirmation gate: >= 4/15 universe pairs positive 24h, else reject all entries this wake
5b. Same-pair re-entry cooldown: no new position within 24h of an `exit-stop-hit` on that pair
6. Current open positions < 4
6a. Concurrent positions in BTC-correlated cluster {BTC, ETH, SOL, TAO, AVAX, SUI, LINK} <= 2
7. Portfolio risk-at-moment + this trade's risk <= 4%
8. Max 1 new entry per routine wake (tie-break: highest 30d notional rank)

## Position sizing

Identical to v0.2: risk per trade 1.5% of equity; initial stop distance 2 × ATR(14) on 1H; size = (equity × 0.015) / stop distance, rounded down to Kraken minimum lot.

## Stop management (v0.11 ADDED)

- At each 1H close, compute unrealized R = (current close − entry) / (entry − initial stop).
- **Once unrealized R ≥ `breakeven_trigger_R` (2.0) at any 1H close, move the stop to breakeven (= entry price).**
- The stop ratchets **up only** — never moved back down. Once at breakeven it remains at breakeven for the life of the trade (this variant does not trail further).
- All other risk parameters (1.5% per trade, initial 2×ATR placement) inherited verbatim from v0.2.

## Exits

Exit the position when **any** of the following is true:

1. 1H close < 1H 20-EMA — **unchanged from v0.2**
2. Price hits the stop. The stop is the original 2×ATR level until the breakeven ratchet fires (unrealized ≥ 2R), then it is the entry price. Checked at 1H close (intra-bar for the stop per v0.2 convention).
3. Unrealized PnL >= 4R (take profit) — **unchanged from v0.2**

## Concept buckets declared

`momentum: 100%`, same as v0.2. Variant-internal — does not affect main allocation.

## Variant-specific tracking

Files in `variants/v0.11-breakeven-2R/`. Compared to v0.2 (main) on `memory/leaderboard.md`. Sibling exit-logic variant: v0.10-exit-confirm.

## Promotion path

Standard. Earliest 2026-06-15. Ring-2 `[Y/N]` required for promotion to main.
