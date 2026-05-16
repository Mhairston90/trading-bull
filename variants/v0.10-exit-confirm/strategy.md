# BULL Strategy — Variant v0.10-exit-confirm

> **Variant strategy file. Self-contained.**
> **Status:** active LAB (hypothesis) variant, spun up 2026-05-16
> **Lineage:** modification of main v0.2. Exit rule 1 requires `ema_exit_confirm_bars` = 2 consecutive 1H closes below the 20-EMA (vs main's single close).
> **Source:** lessons.md 2026-04-24 commission-drag (score 8).

## Philosophy

Same as v0.2 — minimal long-only momentum baseline, single `momentum` bucket. The only change tests whether a 2-bar exit-confirmation on the EMA-cross exit reduces whipsaw friction.

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

Identical to v0.2: risk per trade 1.5% of equity; stop distance 2 × ATR(14) on 1H; size = (equity × 0.015) / stop distance, rounded down to Kraken minimum lot.

## Exits

Exit the position when **any** of the following is true:

1. **(v0.10 MODIFIED)** **2 consecutive** 1H closes < 1H 20-EMA (`ema_exit_confirm_bars` = 2). A single 1H close below the EMA no longer triggers exit; the next 1H bar must also close below the EMA. If price reclaims the EMA on the confirming bar, the position is retained and the counter resets.
2. Price hits the 2 × ATR(14) stop (set at entry, static) — **unchanged from v0.2**
3. Unrealized PnL >= 4R (take profit) — **unchanged from v0.2**

Exits are checked at the close of each 1H candle. No intra-bar exits (stop rule 2 excepted, per v0.2 convention).

## Concept buckets declared

`momentum: 100%`, same as v0.2. Variant-internal — does not affect main allocation.

## Variant-specific tracking

Files in `variants/v0.10-exit-confirm/`. Compared to v0.2 (main) on `memory/leaderboard.md`.

## Promotion path

Standard. Earliest 2026-06-15. Ring-2 `[Y/N]` required for promotion to main.
