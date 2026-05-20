# Variant v0.6 — vol-comp-aggressive (parameter sweep)

**Spin-up date:** 2026-05-12
**Variant category:** LAB-SWEEP (parameter-sweep variant, not new hypothesis)
**Hypothesis:** v0.3's vol-compression threshold of 0.5× may be too aggressive (blocking too many entries during normal-vol regimes). A lower threshold of 0.3× would block only extreme compression — testing whether v0.3 is over-filtering.

## Lineage

- **Parent variant:** v0.3-vol-compression
- **Parameter perturbed:** `vol_compression_threshold` (parent value 0.5, this variant **0.3**)
- **Perturbation direction:** lower (= fewer blocks = more aggressive trading)
- **Sibling variants:** v0.7-vol-comp-defensive (parent's higher-threshold sweep at 0.7)
- **Hypothesis:** does lowering the threshold from 0.5 to 0.3 on v0.3's parent improve net return / profit factor / trade frequency, or is the lower threshold simply admitting more chop-driven losers?

## Diff vs parent v0.3

- **Modified:** rule 5c threshold `0.5` → `0.3`
- All other rules inherited verbatim from v0.3 strategy.md

## Mandate-compliance check

Inherited from v0.3 (which passed all 8 checks). Single-parameter change doesn't introduce new mandate concerns:
- [x] Spot only
- [x] ≤ 8 positions
- [x] ≤ 1.5% per trade
- [x] ≤ 4% portfolio
- [x] Universe from `memory/universe.md`
- [x] $10K start
- [x] Paper-paper only
- [x] Inherits Ring-3 kill switches

All checks pass.

## Promotion criteria

Standard from `variants/README.md`. Earliest promotion-eligible: **2026-06-11** (30 days after spin-up).

## Expected behavior vs parent

In normal-vol regimes (where ATR is between 0.3× and 0.5× of mean):
- **v0.3 (parent, 0.5×):** rejects entries — assumes regime is "compressed"
- **v0.6 (this variant, 0.3×):** allows entries — assumes regime is "normal enough"

The Phase 1 question: which call is right?
- If v0.6 outperforms v0.3 on net return AND profit factor → 0.5 was over-filtering, the autoloop should propose tightening v0.3 toward 0.3
- If v0.6 underperforms v0.3 → 0.5 was correctly filtering chop, the lower threshold admits losing trades
- If both about equal → the threshold doesn't matter in this regime; routine #4 retires whichever has lower trade count

## Honest caveats

- Sample size will be small over 30 days. Sweep results are *directional*, not definitive.
- Threshold 0.3 is the lower bound of the sweep range. If 0.6 outperforms 0.3 outperforms 0.5, the autoloop should spawn 0.2 next round to find the local optimum.
- This variant does NOT compete with v0.3 directly for the "winner takes the parent's slot" — both run independently. Promotion to main remains Ring-2 gated for either.
