# Variant v0.14 — recovery-trend (faster 4H trend filter)

**Spin-up date:** 2026-06-09
**Source idea:** internal / user-requested ("did you want to add any strategies yourself" — interactive 2026-06-09), evidence from the same session's mcp-outage gap replay
**Hypothesis:** after a synchronized crash, the 4H 50-EMA lags price by weeks and leaves main structurally unable to trade the recovery; a 4H 20-EMA trend filter re-admits entries days earlier without abandoning the trend requirement entirely.
**Diff vs main (currently v0.4):**
- Added: nothing
- Removed: nothing
- Modified: entry rule 3 — `4H close > 4H 20-EMA` (main: 4H 50-EMA). Everything else verbatim, including the 5a/SBD regime gates, which remain the crash protection.

## Evidence (gap replay 2026-06-09, `scripts/mcp_outage_replay_20260609.py` + cached bars)

During the 06-07 → 06-09 recovery (regime 8-14/15 positive, RSIs 55-67), **every single pair at every wake failed rule 3** under the 50-EMA — main and all momentum variants were blind in a confirmed-positive regime. Recomputed with a 20-EMA:

| Wake | 50-EMA passers | 20-EMA passers |
|------|----------------|----------------|
| 06-07T04:00Z | 0 | 1 (SUI) |
| 06-07T13:00Z | 0 | 6 (BTC, XRP, SUI, TAO, LINK, TRX) |
| 06-08T04:00Z | 0 | 11 |
| 06-08T13:00Z | 0 | 14 |
| 06-09T04:00Z | 0 | 5 |

With all other v0.4 rules applied, v0.14 would have entered BTC @ 63,078 at the 06-08T04:00Z wake (RSI 60.3). As of spin-up BTC is ~61,800 — that counterfactual first trade is likely a small loser, which is precisely the dead-cat-bounce false-positive risk this A/B measures against the recovery-capture upside. The 2026-05-30 HYPE recovery entry (+8.44% day) was only catchable by main because HYPE idiosyncratically held above its 50-EMA; most post-crash recoveries won't have such a pair.

## Tuneable parameters

- `trend_ema_period_4h` (this variant 20; main 50; reasonable sweep range 10-50)

## Mandate-compliance check

- [x] Spot only
- [x] ≤ 8 positions (inherits v0.4 cap of 4)
- [x] ≤ 1.5% per trade
- [x] ≤ 4% portfolio
- [x] Universe from memory/universe.md
- [x] $10K start
- [x] Paper-paper only
- [x] Inherits Ring-3 kill switches

## Promotion criteria (from variants/README.md)

Standard: 30+ days live (eligible 2026-07-09), beats main on net return + profit factor, DD increase ≤ 25%, trade count ≥ 10 in rolling 30d window.

## Notes

The risk asymmetry is deliberate: the 5a regime gate (≥4/15 positive) and SBD classifier remain unchanged, so this variant cannot enter during a crash — it can only enter recoveries earlier. The question is whether early recoveries it catches pay for the bounces that fail. Expected behavior: trades far more often than main in post-crash regimes, identically in established trends (where price is above both EMAs).
