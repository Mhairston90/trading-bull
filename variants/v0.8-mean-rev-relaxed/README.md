# Variant v0.8 — mean-rev-relaxed (parameter sweep)

**Spin-up date:** 2026-05-12
**Variant category:** LAB-SWEEP
**Hypothesis:** v0.4's RSI<25 threshold is conservative ("conventional" RSI floor is 30). A relaxed threshold of 30 produces more entry signals — testing whether v0.4 is missing legitimate oversold bounces or whether the 25 floor is correctly filtering low-quality setups.

## Lineage

- **Parent variant:** v0.4-mean-reversion-sleeve
- **Parameter perturbed:** `rsi_oversold_threshold` (parent value 25, this variant **30**)
- **Perturbation direction:** higher (= more entries, lower per-trade conviction)
- **Sibling variants:** (none yet — only one sweep spawned this cycle; v0.4 could also be swept lower at 20 in a future round)
- **Hypothesis:** at RSI<30 vs RSI<25 — does the larger entry set still maintain positive expectancy, or does relaxing the floor admit too many false-positive oversold signals?

## Diff vs parent v0.4

- **Modified:** rule M2 threshold `RSI(14) < 25` → `RSI(14) < 30`
- All other rules inherited verbatim from v0.4 (4H 200-EMA filter, 1.5×ATR stop, 24h time stop, max 2 concurrent)

## Mandate-compliance check

Inherited from v0.4. All 8 checks pass.

## Promotion criteria

Standard. Earliest **2026-06-11**.

## Expected behavior vs parent

- Entry frequency: v0.8 produces ~3-5× more entries than v0.4 (RSI<30 events are ~3-5× more frequent than RSI<25 in historical Kraken data)
- Per-trade hit rate: expected to be lower (admitting weaker oversold setups)
- Net effect: ambiguous. Higher trade count × lower hit rate could produce similar, better, or worse net return depending on whether the marginal trades are profitable

Already today (2026-05-12 routine #7 wake), v0.4 noted that PENGU hit RSI 25.4 — just above the 25 threshold. v0.8 would have considered PENGU for entry that wake. The empirical question is whether those marginal entries are profitable.

## Honest caveats

- The 1H RSI < 30 threshold is the "standard" mean-reversion floor used in many published strategies. v0.4 deliberately chose the stricter 25; v0.8 reverts to the convention. If v0.8 wins, it implies v0.4 was overfitted in design; if v0.4 wins, it implies the convention is wrong for crypto-spot 1H.
- Trade count over 30d may still be small (the 4H 200-EMA filter is also restrictive).
- This sweep does NOT test the other v0.4 parameters (`stop_atr_multiplier`, `time_stop_bars`) — those are deferred for future autoloop rounds.
