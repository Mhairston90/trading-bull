# Variant v0.4 — mean-reversion sleeve

**Spin-up date:** 2026-04-29
**Source idea:** internal — concept-bucket diversification + competitor structural observation (Codex declares a `mean_revert` sleeve, BULL declared 0% mean-reversion in v0.2; this variant tests whether BULL's mandate-allowed-but-unused bucket has edge)
**Hypothesis:** Oversold pullbacks within structurally up-trending pairs mean-revert reliably enough that a small mean-reversion sleeve adds uncorrelated returns to BULL's pure momentum bucket. Concept: when 4H is bullish (close > 4H 200-EMA) but 1H is briefly oversold (RSI < 25 + reversal candle), the 1H pullback often retraces back toward the 1H 20-EMA within hours.
**Diff vs main (currently v0.2):**
- **Replaced** the entire entry signal — this variant looks for oversold bounces, not breakout momentum
- New entry rules (numbered M1-M5 to distinguish from v0.2's momentum rules):
  - M1: 4H close > 4H 200-EMA (long-term structural uptrend)
  - M2: 1H RSI(14) < 25 (oversold)
  - M3: 1H close > previous 1H low AND 1H close > 1H open (reversal candle, not free-fall)
  - M4: Pair has 24h notional volume >= $2.0M USD (W18-B liquidity floor inherited)
  - M5: No existing open position in this pair within this variant's portfolio
- **Modified** exit rules:
  - Take profit at 1H close >= 1H 20-EMA (mean reached)
  - Static stop at 1.5×ATR(14) on 1H below entry (tighter than v0.2's 2×ATR — mean-reversion shouldn't bleed)
  - **Time stop:** if position is still open 24 bars (~24h) after entry without target hit, close at next 1H close at market
- **Modified** position cap: max 2 concurrent mean-reversion positions (lower than v0.2's 4 momentum cap — mean-reversion has lower hit rate, smaller exposure)
- **Modified** concept buckets (variant-internal only):
  - `momentum`: 0%
  - `mean-reversion`: 100%
  - `news-reactive`: 0%
  (Variant declares its own buckets; main `memory/strategy.md` unchanged.)

## Mandate-compliance check

- [x] Spot only — long-only mean-reversion, no shorts/leverage/perps/options
- [x] ≤ 8 positions — variant max-concurrent 2 < 8
- [x] ≤ 1.5% per trade — sizing inherited
- [x] ≤ 4% portfolio — variant max 2 positions × 1.5% = 3% max simultaneous risk
- [x] Universe from `memory/universe.md` — same 15 pairs
- [x] $10K start — synthetic, fresh from spin-up date
- [x] Paper-paper only — no real Kraken orders
- [x] Inherits Ring-3 kill switches from `memory/guardrails.md`

All checks pass.

## Promotion criteria

Standard from `variants/README.md`. Earliest promotion-eligible: **2026-05-29**.

## Threshold rationale

- **RSI 25 floor:** stronger than the conventional 30. Picks high-conviction oversold only, accepting fewer signals for higher per-trade expectancy.
- **4H 200-EMA filter:** strict structural uptrend. Avoids "catching falling knives" in actual downtrends — mean-reversion in a downtrend is just slow-bleeding.
- **24-bar time stop:** mean-reversion is supposed to happen quickly. If it hasn't reverted in 24h the thesis is wrong; cut and move on.
- **1.5×ATR stop (vs 2×ATR for momentum):** smaller stop → smaller losers when wrong, and mean-reversion shouldn't drift far from entry before the bounce.

## What this variant explicitly does NOT do

- Does not enter on momentum signals — different concept entirely
- Does not pyramid or scale in
- Does not modify v0.2 main strategy
- Does not interact with v0.3-vol-compression or v0.5-cluster-cap-tight portfolios

## Expected behavior

- In choppy markets with periodic 1H washouts: variant takes the bounces, profits when 1H reverts to mean
- In strong trends: very few entries (RSI rarely hits 25 in trends)
- In persistent downtrends: filtered out by M1 (4H below 200-EMA), no entries
- Net effect (hypothesis): uncorrelated to v0.2's momentum results — should perform best when v0.2 underperforms (chop) and vice versa

## Source quote

From Robot Wealth's "To Trend or Not To Trend? (Wrong question)":
> "An edge requires a why... A leveraged token rebalanced... A wealth manager rebalanced... three mean-reverting patterns, each with a different 'why'."

The "why" for THIS variant: in liquid crypto, RSI<25 + 4H uptrend = retail panic-selling into structural-buyer support, which mean-reverts as the panic-selling exhausts. Not a perfect "why" (no specific identified flow), but defensible.

## Honest caveats

- No backtest. Threshold (RSI 25, 1.5×ATR, 24h time stop) is judgment, not optimized.
- Mean-reversion variants in crypto are notorious for "death by a thousand cuts" if the market regime shifts. Time stop is the main defense.
- Lower hit rate than momentum strategies typically — accept smaller trade count.
