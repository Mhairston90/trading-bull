# BULL Strategy — Variant v0.4-mean-reversion-sleeve

> **Variant strategy file. Self-contained — does NOT inherit from main `memory/strategy.md`.**
> **Status:** active LAB variant, spun up 2026-04-29
> **Diff vs main v0.2:** entirely different entry signal (oversold bounce in uptrend), tighter stops, time-stop, smaller position cap.
> **Subject to mandate:** all hard floors in `memory/guardrails.md` apply unmodified.

## Philosophy

Long-only mean-reversion. Look for 1H oversold conditions in structurally up-trending pairs, expect bounce back to 1H 20-EMA. Complement to (not replacement for) momentum.

## Universe

Read from `memory/universe.md`. Same as main.

## Entries (long-only mean-reversion)

Enter LONG when **all** of the following are true on a just-closed 1H candle:

**M1.** 4H close > 4H 200-EMA (long-term structural uptrend confirmed)
**M2.** 1H RSI(14) < 25 (oversold — high-conviction floor, not the conventional 30)
**M3.** 1H close > previous 1H low AND 1H close > 1H open (reversal candle showing buyer step-in)
**M4.** Pair has 24h notional volume >= $2.0M USD at entry-scan (W18-B liquidity floor)
**M5.** No existing open position in this pair (within this variant's portfolio)
**M6.** Current open positions in this variant < 2 (lower cap than v0.2's 4)
**M7.** Portfolio risk-at-moment + this trade's risk <= 4% (mandate floor)
**M8.** Max 1 new entry per routine wake (W18-C, inherited)

## Position sizing

- Risk per trade: 1.5% of current variant equity
- Stop distance: **1.5 × ATR(14) on 1H** (tighter than v0.2's 2×ATR — mean-reversion shouldn't bleed)
- Size = (equity × 0.015) / stop distance, rounded down to Kraken minimum lot

## Exits

Exit the position when **any** of the following is true:

**X1.** 1H close >= 1H 20-EMA (target — mean reached)
**X2.** Price hits the 1.5 × ATR(14) stop (set at entry, static)
**X3.** Position is still open 24 bars after entry (~24h time stop) — close at next 1H close at market

Exits checked at every 1H close. Stop check is intra-bar.

## Concept buckets (variant-internal)

- `momentum`: 0%
- `mean-reversion`: 100%
- `news-reactive`: 0%

(Variant declares its own buckets; main `memory/strategy.md` v0.2 unchanged at `momentum: 100%`.)

## Variant-specific tracking

- Synthetic equity, portfolio, and trade log live in `variants/v0.4-mean-reversion-sleeve/`
- Routine #7 (variant-paper) replays past 24h Kraken bars and applies these rules daily at 22:00 PT
- Performance reported on `memory/leaderboard.md`

## Promotion path

Eligible for promotion proposal at routine #4 Saturday when ALL hold (promotion criteria from `variants/README.md`):
- ≥ 30 days live (earliest: 2026-05-29)
- Beats main on net return rolling 30d
- Beats main on profit factor rolling 30d
- Max DD ≤ main's DD × 1.25
- ≥ 10 trades in rolling 30d

If promoted via Ring-2 `[Y]`, this could replace OR supplement main strategy depending on the proposed integration (a fully-different concept bucket might warrant adding-as-sleeve rather than replace; routine #4 to draft).
