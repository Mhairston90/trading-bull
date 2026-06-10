# Variant v0.15 — meanrev-guarded (relaxed RSI floor + SBD knife-catch guard)

**Spin-up date:** 2026-06-09
**Source idea:** internal / user-requested (interactive 2026-06-09), evidence from the same session's mcp-outage gap replay
**Hypothesis:** v0.8's relaxed RSI<30 floor finds real oversold-bounce trades that the parent's RSI<25 misses, but only if synchronized-breakdown days are excluded — oversold during a cascade is a knife, oversold in a functioning tape is a spring.
**Diff vs parent family (v0.4-mean-reversion-sleeve / v0.8-mean-rev-relaxed):**
- Added: **M-guard** — reject all entries while regime = SYNCHRONIZED_BREAKDOWN (≤1/15 universe pairs positive 24h AND median 24h ≤ −1.0%, same classifier as main 5a-SBD)
- Removed: nothing
- Modified: M2 RSI floor = **30** (v0.8's sweep value; parent uses 25)

## Lineage

- **Parent variant:** v0.4-mean-reversion-sleeve (rules) × v0.8-mean-rev-relaxed (RSI threshold)
- **Parameter perturbed:** none new — combines v0.8's `rsi_oversold_threshold` 30 with a new categorical rule (M-guard)
- **Sibling variants:** v0.8-mean-rev-relaxed (same RSI floor, NO guard — direct A/B on the guard), v0.9-mean-rev-tight, parent v0.4
- **Hypothesis:** does excluding SBD days flip the relaxed floor's expectancy positive?

## Evidence (gap replay 2026-06-09)

The rack's only mean-reversion signal in 41 days fired at the 2026-06-05T04:00Z wake: NEAR/USD RSI 26.9 with M1 pass. v0.8 (no guard) took it and was stopped out 4 hours later for −1.00R / −$150 — the wake's regime was **0/15 positive, median −6.15%, deep SBD**. v0.15 with the M-guard would have skipped exactly this trade while keeping the wider RSI net open for oversold signals in non-cascade tape. Direct A/B vs v0.8: identical rules except the guard, so every future divergence isolates the guard's value.

## Tuneable parameters

- `rsi_oversold_threshold` (this variant 30; range 20-35)
- `sbd_guard` (this variant ON; v0.8 OFF — the categorical A/B)

## Mandate-compliance check

- [x] Spot only
- [x] ≤ 8 positions (inherits mean-rev cap of 2)
- [x] ≤ 1.5% per trade
- [x] ≤ 4% portfolio
- [x] Universe from memory/universe.md
- [x] $10K start
- [x] Paper-paper only
- [x] Inherits Ring-3 kill switches

## Promotion criteria (from variants/README.md)

Standard: 30+ days live (eligible 2026-07-09), beats main on net return + profit factor, DD increase ≤ 25%, trade count ≥ 10 in rolling 30d window.

## Notes

Long-only mean reversion remains mandate-clean (buying oversold is a long). The M-guard is the defensive mirror of main's 5a-SBD lesson (2026-05-19 fragility audit): BULL cannot short a cascade, and now its mean-rev sleeve also declines to catch falling knives inside one. Expected behavior: very few trades (M1 4H>200-EMA is restrictive post-crash), but each one in a structurally safer context than v0.8's.
