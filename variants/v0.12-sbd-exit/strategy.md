# BULL Strategy — Variant v0.12-sbd-exit

> **Variant strategy file. Self-contained.**
> **Status:** active LAB (hypothesis / instrumented twin), spun up 2026-05-19
> **Lineage:** v0.2 + 5a-SBD + Exit 1-SBD (== main v0.3). Exists to isolate/measure the SBD change vs the v0.2 baseline.
> **Source:** fragility audit 2026-05-19; Ring-2 proposal 2026-W21-F (approved `[Y B]` + variant).

## Philosophy

Same as v0.2 — minimal long-only momentum baseline, single `momentum` bucket. The only change adds a synchronized-breakdown regime classifier that tightens the trend exit while the breakdown persists, so open longs give back less unrealized R in multi-day risk-off. No shorting — long-only mandate fully preserved.

## Universe

Read from `memory/universe.md` (same as v0.2).

## Entries (long-only)

Identical to v0.2 (rules 1, 2, 2a, 3, 4, 4a, 5, 5a, 5b, 6, 6a, 7, 8). Plus:

5a-SBD. Synchronized-breakdown sub-state: classify regime = SYNCHRONIZED_BREAKDOWN when **both** (i) ≤ 1 of 15 universe pairs positive on 24h % change, **and** (ii) median 24h % change across the 15 universe pairs ≤ −1.0%. Strict subset of a 5a failure — reject-all-new-entries (rule 5a) still applies unchanged. SBD additionally triggers Exit rule 1-SBD. Re-evaluated every wake; clears when (i) or (ii) is no longer true.

## Position sizing

Identical to v0.2: risk per trade 1.5% of equity; stop distance 2 × ATR(14) on 1H; size = (equity × 0.015) / stop distance, rounded down to Kraken minimum lot.

## Exits

Exit the position when **any** of the following is true:

1. 1H close < 1H 20-EMA — default.
1-SBD. While regime = SYNCHRONIZED_BREAKDOWN, Exit rule 1 tightens to: **1H close < 1H 9-EMA**. Reverts to 20-EMA automatically when SBD clears. Strictly risk-reducing — flattens earlier only.
2. Price hits the 2 × ATR(14) stop (set at entry, static) — unchanged by SBD.
3. Unrealized PnL ≥ 4R (take profit) — unchanged by SBD.

Exits checked at the close of each 1H candle. No intra-bar exits (per v0.2 convention).

## Concept buckets declared

`momentum: 100%`, same as v0.2. Variant-internal — does not affect main allocation.

## Variant-specific tracking

Files in `variants/v0.12-sbd-exit/`. Compared to v0.2 (baseline) and main v0.3 on `memory/leaderboard.md`. Each SBD-active wake logs estimated avoided-give-back (9-EMA exit unrealized R vs modeled 20-EMA exit). Sibling exit-logic variants: v0.10-exit-confirm, v0.11-breakeven-2R.

## Promotion path

Standard. Earliest 2026-06-18. Since main is already v0.3 with these rules, promotion route is autoloop `sbd_*` parameter sweep → Ring-2 `[Y/N]` for a tuned config.
