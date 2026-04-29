# Variant v0.3 — vol-compression entry gate

**Spin-up date:** 2026-04-29
**Source idea:** IDEA-20260429-04 (Glassnode Insights W17 — RV/IV convergence regime gate)
**Hypothesis:** When 1H realized volatility (ATR) compresses meaningfully below its trailing 30-day mean, the market is range-bound and momentum entries underperform. Skipping new entries during compressed-vol regimes preserves capital for higher-conviction trend regimes.
**Diff vs main (currently v0.2):**
- Added: rule **5c** — volatility-compression gate (reject entries when 1H ATR(14) < 0.5 × mean ATR(14) over past 720 bars)
- Removed: none
- Modified: none

All other v0.2 rules (1, 2, 2a, 3, 4, 4a, 5, 5a, 5b, 6, 6a, 7, 8) are inherited verbatim.

## Mandate-compliance check

- [x] Spot only — variant adds an entry gate, does not introduce leverage/margin/perps/options
- [x] ≤ 8 positions — inherited from main (rule 6, cap of 4 active)
- [x] ≤ 1.5% per trade — inherited (sizing unchanged)
- [x] ≤ 4% portfolio — inherited (rule 7)
- [x] Universe from `memory/universe.md` — inherited
- [x] $10K start — synthetic, fresh from spin-up date
- [x] Paper-paper only — no real Kraken orders, no trade log writes outside `variants/v0.3-vol-compression/`
- [x] Inherits Ring-3 kill switches from `memory/guardrails.md`

All checks pass. Variant approved for spin-up.

## Promotion criteria

Standard from `variants/README.md`:
- ≥ 30 days live
- Beats main BULL on net return over rolling 30d
- Beats main BULL on profit factor over rolling 30d
- Max DD does not exceed main's DD by > 25%
- ≥ 10 trades in rolling 30d window

Earliest promotion-eligible date: **2026-05-29** (30 days after spin-up).

## Threshold rationale

The Glassnode source claim was "RV/IV gap < 2%". BULL has no implied-volatility data on Kraken spot — so v0.3 substitutes an RV-only proxy: current 1H ATR vs. its trailing 30-day mean.

**Threshold pick: 0.5×** — meaning "current ATR less than half the 30-day mean = compressed regime, skip entries." Reasoning:
- 0.5 is a deliberately conservative starting value. It will fire less often than the source's RV/IV claim would suggest, biasing toward false negatives (allowing some chop entries) rather than false positives (blocking trend entries).
- Routine #4 Saturday harness can sweep this threshold against historical bars (0.4, 0.5, 0.6, 0.7) once the variant has accumulated trade evidence.
- Lesson 2026-04-27 cascade option (c) was phrased as "1H ATR has compressed below recent average" without a specific number — picking 0.5 is BULL's first concrete instantiation of that lesson.

## What this variant explicitly does NOT do

- Does not change risk per trade, stop distance, or take-profit.
- Does not introduce mean-reversion or short-side trades — still long-only momentum.
- Does not modify the cluster cap (W18-A), liquidity floor (W18-B), one-per-wake (W18-C), RSI cap (W19-D 2a), regime-confirmation gate (W19-D 5a), or re-entry cooldown (W19-D 5b).
- Does not interact with main BULL's portfolio in any way.

## Expected behavior

- In choppy / low-vol weeks: variant skips most/all entries main BULL took. Variant equity flat; main equity may show small losses or gains depending on whether main's entries went to stop or target.
- In high-vol trending weeks: variant takes the same entries as main. Variant tracks main closely.
- Net effect over time (hypothesis): variant suffers fewer chop-driven small losses, captures comparable trend gains. Net return higher with similar or smaller drawdown.

## Source quotes

From Glassnode W17 2026 ("Trapped Below Market Mean"):
> "Realized and implied volatility are closely aligned, confirming a calmer market backdrop with limited directional conviction."
> "When realized volatility falls, it naturally pulls implied volatility lower... cheaper options reduce the urgency to hedge, leading to less hedging-driven price movement."

From `memory/lessons.md` 2026-04-27 cascade, option (c) deferred:
> "regime filter that pauses new momentum entries when 1H ATR has compressed below recent average (volatility-pop precursor)"
