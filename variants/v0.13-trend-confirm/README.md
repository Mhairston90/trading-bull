# Variant v0.13 — trend-confirm (hypothesis)

**Spin-up date:** 2026-05-20
**Source idea:** internal — `memory/trade_log.md` whipsaw analysis 2026-05-20 (interactive session). 9 of 17 closed trades on main (v0.2/v0.3) are −1R stop-outs within 1–21h of entry; this is the dominant un-attacked loss bucket after the W18-A cluster cascade was closed.
**Variant category:** LAB (hypothesis)

**Hypothesis:** v0.3's entry rule 1 (single 1H close > 20-EMA) plus RSI(14) > 55 fires on the **first bar** of any uptick, including failed bounces that immediately reverse. Tightening entry to require **two consecutive 1H closes > 20-EMA** plus a **4H RSI ≥ 50 confirmation** filters out the lowest-quality entries — bars where the higher timeframe is still leaning down despite a single positive 1H reading. Expected effect: ~30–40% fewer entries, concentrated in the −1R whipsaw bucket; remaining entries have higher base-rate expectancy because they fire only after trend persistence has been demonstrated.

**Diff vs main (currently v0.3):**
- **Modified** entry rule 1: `1H close > 1H 20-EMA` → **`2 consecutive 1H closes > 1H 20-EMA`** at entry-scan (i.e., both the just-closed bar AND the prior bar's close are above the 20-EMA).
- **Added** entry rule 3a: at entry-scan, **4H RSI(14) ≥ 50**. Cross-timeframe trend confirmation; rejects entries where the 4H is still in net mean-reverting territory.
- All other entry rules (2, 2a, 3, 4, 4a, 5, 5a, 5a-SBD, 5b, 6, 6a, 7, 8), sizing, exits (1, 1-SBD, 2, 3), kill switches inherited verbatim from v0.3.

## Mandate-compliance check

- [x] **Spot only** — entry-quality filter; no leverage/margin/perps/options
- [x] **≤ 8 positions** — inherited from v0.3 (rule 6, active cap 4)
- [x] **≤ 1.5% per trade** — sizing inherited; entry filter does not change per-trade risk
- [x] **≤ 4% portfolio** — inherited (rule 7); fewer entries lowers portfolio-risk-at-moment ceiling
- [x] **Universe** from `memory/universe.md` — inherited
- [x] **$10K start** — synthetic
- [x] **Paper-paper only** — no real Kraken orders
- [x] **Inherits Ring-3 kill switches** from `memory/guardrails.md`

All 8 checks pass. (This variant is **strictly entry-restricting** vs v0.3 — it can only reject entries, never admit ones v0.3 would have rejected.)

## Tuneable parameters (Phase 1 autoloop)

| Parameter | Current value | Sweep range | Notes |
|-----------|--------------:|-------------|-------|
| `bars_above_ema` | 2 | 1 – 3 | Number of consecutive 1H closes above 20-EMA required at entry-scan. 1 = current v0.3; 3 = stricter, fewer entries. |
| `h4_rsi_floor` | 50 | 45 – 60 | 4H RSI(14) minimum at entry-scan. 45 = barely-above-mid; 60 = strongly trending. |

## Promotion criteria

Standard from `variants/README.md`: 30+ days live, beats main on net return + profit factor, DD increase ≤ 25%, ≥ 10 trades in rolling 30d. Earliest promotion-eligible: **2026-06-19**.

## Why a variant instead of a Ring-2 proposal now

The whipsaw −1R bucket is the dominant un-addressed loss source (9 of 17 closes = 53% of trades, ~−$386 of the ~−$700 in losses). But the fix is **entry-restricting**, which carries the opposite risk profile of v0.10/v0.11 (those are strictly risk-reducing on exits). An entry filter that's too tight may eliminate the next +4R SOL-style winner along with the whipsaws. That trade-off needs paper-paper evidence, not direct adoption — exactly the use case the variant rack exists for.

## Expected behavior vs main

- **Whipsaw bars (1H closes > EMA then immediately reverses next bar):** v0.13 rejects — won't enter. Avoids the −1R stop-out entirely.
- **Trend continuations (1H closes > EMA two bars in a row, 4H RSI confirms):** v0.13 enters on the second bar's close, ~1 bar later than v0.3. Foregoes 1H of entry-price advantage but enters into demonstrated persistence.
- **Strong-trend entries** (SOL 2026-05-08 archetype, +4.03R): both bars before entry already above EMA, 4H RSI was 65+. v0.13 enters at the same bar as v0.3 or 1 bar later. Effect on the eventual +4R outcome: minimal.
- **Climactic-RSI entries** already capped by v0.3 rule 2a (RSI ≤ 80) — v0.13 inherits, no new behavior here.
- **Net effect (hypothesis):** materially lower trade count, materially higher win rate, lower drawdown. Net return ambiguous — depends on whether the filtered-out trades were genuinely net-negative or merely high-variance.

## Honest caveats

- No backtest yet (TV Desktop validation track is separate, and the morning brief shows broadly-red regime persists 2026-05-19 — only 1/15 pairs positive — so synthetic trades will be sparse early).
- The 4H RSI ≥ 50 floor is reasoned, not optimized. Declared tuneable; routine #4 may sweep.
- "Two consecutive closes" is a common technical filter but has no specific BULL-lesson source — this is theory-driven (filter low-quality momentum entries) rather than evidence-driven the way v0.11 was. Stated honestly so promotion requires harder evidence than v0.11.
- Does NOT address the give-back failure mode (that is v0.11). Does NOT address commission drag (v0.10). The three exit/entry-logic variants are independent.

## Sibling exit-logic variants

- v0.10-exit-confirm (2-bar EMA exit confirmation)
- v0.11-breakeven-2R (stop ratchets to breakeven at +2R unrealized)
- v0.12-sbd-exit (9-EMA exit during synchronized-breakdown regime)

v0.13 is the **entry-quality** counterpart to those three exit-quality variants. If v0.13 + (v0.10 or v0.11) both demonstrate edge over 30 days, the combined Ring-2 proposal can package entry + exit upgrades together.
