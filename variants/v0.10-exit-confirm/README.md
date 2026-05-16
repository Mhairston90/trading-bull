# Variant v0.10 — exit-confirm (hypothesis)

**Spin-up date:** 2026-05-16
**Source idea:** internal — `memory/lessons.md` 2026-04-24 "Commission drag dominates short-lived EMA-cross exits" (score **8** as of 2026-W20). Lesson recommendation (a): "require an exit-confirmation bar (e.g., 2 closes below EMA)."
**Variant category:** LAB (hypothesis)
**Hypothesis:** v0.2's exit rule 1 fires on a *single* 1H close below the 20-EMA. On shallow mean-reversions the price often reclaims the EMA within 1–2 bars, so the strategy pays a full ~0.5%+ round-trip commission/slippage tax for a whipsaw. Requiring **2 consecutive** 1H closes below the 20-EMA before exiting should filter single-bar noise dips, cut whipsaw exits, and let winners run past transient pullbacks — improving net-of-friction expectancy.

**Diff vs main (currently v0.2):**
- **Modified** exit rule 1: `1H close < 1H 20-EMA` → `2 consecutive 1H closes < 1H 20-EMA`
- Exit rules 2 (2×ATR static stop) and 3 (4R take-profit) inherited verbatim — unchanged
- All entry rules (1, 2, 2a, 3, 4, 4a, 5, 5a, 5b, 6, 6a, 7, 8), sizing, kill switches inherited verbatim from v0.2

## Why this variant exists now (instead of a Ring-2 proposal)

The commission-drag lesson is score 8 with 3 instances (2026-04-24 BTC, 2026-05-06 BTC, 2026-05-15 XRP — the last on the largest-notional position to date, ~$57 friction ≈ 0.37R). It is the clearest single-rule improvement candidate BULL has. A Ring-2 strategy-edit proposal requires backtest evidence (guardrails logging obligation), but TradingView Desktop is not installed on this machine (`tv_launch` finds no binary; 2nd consecutive harness blocked). Rather than defer indefinitely, this variant converts the blocked proposal into an autonomous paper-paper evidence track that accrues via routine #7 without needing TradingView. When 30d evidence exists (or TV becomes available for a 180d backtest), routine #4 can draft the Ring-2 proposal with real numbers.

## Mandate-compliance check

- [x] **Spot only** — no leverage/margin/perps/options; single exit-rule modification
- [x] **≤ 8 positions** — inherited from v0.2 (rule 6, active cap 4)
- [x] **≤ 1.5% per trade** — sizing inherited verbatim
- [x] **≤ 4% portfolio** — inherited (rule 7); a slower exit slightly extends hold time but does not change per-trade or portfolio risk caps
- [x] **Universe** from `memory/universe.md` — inherited
- [x] **$10K start** — synthetic
- [x] **Paper-paper only** — no real Kraken orders
- [x] **Inherits Ring-3 kill switches** from `memory/guardrails.md`

All 8 checks pass.

## Tuneable parameters (Phase 1 autoloop)

| Parameter | Current value | Sweep range | Notes |
|-----------|--------------:|-------------|-------|
| `ema_exit_confirm_bars` | 2 | 1 – 3 | Exit rule 1 — consecutive 1H closes below 20-EMA required to exit. 1 = v0.2 main behavior (degenerate baseline); 3 = very slow. Future autoloop may sweep to 3. |

## Promotion criteria

Standard from `variants/README.md`: 30+ days live, beats main on net return + profit factor, DD increase ≤ 25%, ≥ 10 trades in rolling 30d. Earliest promotion-eligible: **2026-06-15**.

## Expected behavior vs main

- **Whipsaw EMA-cross exits** (BTC 04-24 +0.10R gross / −0.21R net, BTC 05-06 +0.06R net): v0.10 would hold through the single-bar dip; if price reclaims the EMA the trade continues instead of paying round-trip friction for ~nothing.
- **Genuine trend reversals:** v0.10 exits one 1H bar later than main → gives back ~1 bar of adverse move (a real but bounded cost; the static 2×ATR stop still caps downside).
- **Take-profit / stop-out trades** (e.g. SOL +4.03R, XRP −1.03R): unaffected — rules 2 and 3 are unchanged; only the EMA-cross exit path differs.
- Net effect (hypothesis): fewer low-quality EMA-cross exits, modestly longer average hold, better net-of-commission expectancy on the momentum bucket. Risk: in fast reversals the extra bar widens some losers.

## Honest caveats

- No backtest yet (TV unavailable) — this variant IS the evidence-gathering mechanism. Do not promote on hypothesis alone.
- Routine #7 paper-paper sample may be small in the current broadly-red regime (entries gated by v0.2's regime filter); the EMA-exit path only differs on trades that actually open and then approach the EMA.
- A 2-bar confirmation is a single point on the curve; `ema_exit_confirm_bars` is declared tuneable so a future autoloop round can sweep 1/2/3 once the parent has ≥14d live.
- Does NOT address the friction tax on stop-out trades (XRP-type tight-stop large-notional losses) — that is a *sizing*-side concern, a separate future variant (friction-aware position sizing), not this exit-side test.
