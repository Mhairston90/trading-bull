# Variant v0.7 — vol-comp-defensive (parameter sweep)

**Spin-up date:** 2026-05-12
**Variant category:** LAB-SWEEP (parameter-sweep variant)
**Hypothesis:** v0.3's vol-compression threshold of 0.5× may be too lenient (still admitting too many chop-regime entries). A higher threshold of 0.7× would block more entries during mild-compression regimes — testing whether v0.3 is under-filtering.

## Lineage

- **Parent variant:** v0.3-vol-compression
- **Parameter perturbed:** `vol_compression_threshold` (parent value 0.5, this variant **0.7**)
- **Perturbation direction:** higher (= more blocks = more defensive trading)
- **Sibling variants:** v0.6-vol-comp-aggressive (parent's lower-threshold sweep at 0.3)
- **Hypothesis:** does raising threshold from 0.5 to 0.7 improve win rate / profit factor at the cost of trade count, or does the additional filtering miss legitimate entries?

## Diff vs parent v0.3

- **Modified:** rule 5c threshold `0.5` → `0.7`
- All other rules inherited verbatim

## Mandate-compliance check

Inherited from v0.3. All 8 checks pass.

## Promotion criteria

Standard. Earliest **2026-06-11**.

## Expected behavior vs parent

In mild-compression regimes (ATR between 0.5× and 0.7× of mean):
- **v0.3 (parent, 0.5×):** allows entries
- **v0.7 (this variant, 0.7×):** rejects entries

If v0.7 outperforms v0.3, the autoloop should propose raising v0.3 toward 0.7. If it underperforms, v0.3's 0.5 is closer to optimum.

Together with v0.6 (0.3), this sweep brackets the parameter space {0.3, 0.5, 0.7}. After 30 days the ranking tells us which direction to sweep further.

## Honest caveats

- Higher threshold means fewer entries, so v0.7's trade count over 30 days may be too low for statistical significance. May need 60+ days before the ranking is meaningful.
- If v0.7 produces zero trades in the rolling 30d window, it auto-fails the 10-trades-minimum promotion criterion. That's a meaningful result too — it means 0.7 is too restrictive for current regime.
