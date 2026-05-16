# Variant v0.9 — mean-rev-tight (parameter sweep)

**Spin-up date:** 2026-05-16
**Variant category:** LAB-SWEEP
**Hypothesis:** v0.4's RSI<25 oversold floor may still be too permissive for crypto-spot 1H tape. A stricter floor of 20 admits only deep-capitulation bounces — testing whether the marginal 20–25 RSI entries v0.4 takes are net-positive or net-negative expectancy.

## Lineage

- **Parent variant:** v0.4-mean-reversion-sleeve
- **Parameter perturbed:** `rsi_oversold_threshold` (parent value 25, this variant **20**)
- **Perturbation direction:** lower (= fewer entries, higher per-trade conviction)
- **Sibling variants:** v0.8-mean-rev-relaxed (same parent, RSI 25 → **30**, higher direction). v0.9 and v0.8 bracket the parent on both sides — the three-point sweep (20 / 25 / 30) lets routine #4 read the expectancy curve across the RSI floor.
- **Hypothesis:** at RSI<20 vs RSI<25 — does tightening the floor improve per-trade expectancy enough to offset the lower trade count, or does it starve the variant of trades?

## Diff vs parent v0.4

- **Modified:** rule M2 threshold `RSI(14) < 25` → `RSI(14) < 20`
- All other rules inherited verbatim from v0.4 (4H 200-EMA filter, 1.5×ATR stop, 24h time stop, max 2 concurrent)

## Mandate-compliance check

Inherited from v0.4 (mandate-passing parent; single-parameter perturbation, stricter direction only reduces trade frequency). All 8 checks pass.

- [x] Spot only
- [x] ≤ 8 positions
- [x] ≤ 1.5% per trade
- [x] ≤ 4% portfolio
- [x] Universe from `memory/universe.md`
- [x] $10K start
- [x] Paper-paper only
- [x] Inherits Ring-3 kill switches

## Promotion criteria

Standard from `variants/README.md`. Earliest promotion-eligible: **2026-06-15** (30 days from spin-up).

## Expected behavior vs parent

- Entry frequency: v0.9 produces materially fewer entries than v0.4 (RSI<20 events are rare on 1H — deep capitulation only). Trade count over 30d may be very low; promotion likely needs longer-window evidence.
- Per-trade hit rate: expected higher (only the deepest oversold setups, strongest mean-reversion snap-back).
- Net effect: ambiguous — higher conviction × far fewer trades. The sweep's value is the expectancy curve it forms with v0.8 (30) and v0.4 (25), not v0.9 in isolation.

## Honest caveats

- RSI<20 on 1H is uncommon; 30-day sample may contain 0–2 trades. Statistical power is weak in isolation — interpret only alongside v0.4 and v0.8.
- Does NOT test the other v0.4 parameters (`stop_atr_multiplier`, `time_stop_bars`) — deferred to future autoloop rounds.
- In the current broadly-red regime (0/15 universe pairs positive 2026-05-16), the 4H 200-EMA filter (M1) will block most pairs regardless of RSI floor; early trade count likely zero until regime turns.
