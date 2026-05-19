# BULL_Aggro_Ignition — Design Spec

> Status: DESIGN APPROVED 2026-05-19 (interactive brainstorm, user "looks good").
> Author: BULL agent. Origin: contest fragility audit 2026-05-19 — the only edge
> that paid in the BULL-vs-Codex window was convex positive-skew (synchronized
> breakdown). This strategy systematizes that.
> Scope note: standalone strategy, NOT bound by BULL's locked spot/caps mandate.
> Pine lives in the `/BULL_*` namespace per project rule. Leaderboard hygiene
> rule (forward-only) applies exactly as for `variants/v0.12-sbd-exit`.

## 1. Problem & goal

The whole-stable contest vs Codex (deadline **2026-06-06**) is decided by
convex moves. BULL is long-only/spot by mandate and structurally misses the
short side of volatility breakdowns — the single biggest paid edge in the
window. Goal: a **separate, aggressive crypto day-trading strategy** that
captures volatility-ignition convexity on **both** sides (long thrust-ups,
short thrust-downs), as an additive sleeve to Claude's stable — **only if it
earns it out-of-sample**. If it cannot clear the bar, the honest outcome is to
report failure, not ship a curve-fit (consistent with the session's honesty
standard; see memory `feedback-perf-analysis-framing`).

## 2. Edge thesis

Most crypto return arrives in rare, violent volatility-expansion bursts. An
"ignition bar" = a single bar whose **range and volume both spike far above
recent norms**, in a decisive direction, with momentum-zscore confirmation.
Enter in the ignition direction, ride with a volatility (chandelier) trail,
cut losers fast at an ATR stop. Positive-skew payoff: low win rate acceptable
if winners are large relative to losers.

## 3. Strategy rules (v1 baseline — to be tuned in validation)

- **Timeframe:** 30m and 60m intraday (both tested; pick by evidence).
- **Universe:** SOL, DOGE, AVAX, LINK (high-beta) + BTC, ETH (anchor). Kraken.
- **Ignition detection (per bar):**
  - `rngRatio = (high-low) / SMA(high-low, lookback)`
  - `volRatio = volume / SMA(volume, lookback)`
  - `cPos = (close-low)/(high-low)` (strong-close fraction)
  - `rocZ = zscore(ROC(close, rocLen), rocZLen)`
  - `ignition = rngRatio >= rangeMult AND volRatio >= volMult`
  - `bullIgnite = ignition AND close>open AND cPos>=closePos AND rocZ>=+rocZMin`
  - `bearIgnite = ignition AND close<open AND cPos<=1-closePos AND rocZ<=-rocZMin`
- **Entry:** market on close of the ignition bar (`process_orders_on_close`),
  one position at a time (`pyramiding=0`), long or short.
- **Exit (any):** (a) initial ATR stop = entry ∓ `stopMult*ATR`; (b) chandelier
  trail = extreme-since-entry ∓ `chandMult*ATR`, ratchets only in favor;
  (c) time stop after `maxBars`.
- **Sizing:** 1x, no leverage. Full-equity per position
  (`percent_of_equity`), **sizing-correctness is a v1 bug to fix** (probe
  showed contracts far below equity/price — investigate `percent_of_equity`
  vs explicit `qty` before any tuning).
- **Frictions (backtest realism):** 0.26%/side commission + slippage ≥ 2 ticks.

## 4. Risk model

1x spot-style, no margin/liquidation. "Aggressive" = signal selectivity +
full-size deployment + asymmetric hold (let winners run, kill losers fast),
NOT leverage. Rationale: in an 18-day window leverage's liquidation tail can
end the game; convexity already supplies the upside. Codex Aggro's uncapped
margin is the cautionary precedent.

## 5. Scope, namespace, leaderboard hygiene

- Pine script name: `BULL_Aggro_Ignition_v1` (and tuned successors), `/BULL_*`
  namespace ONLY. No scripts touched outside that namespace.
- NOT inside BULL's `strategy.md`; not bound by BULL's spot/1.5%/4%/15-pair caps.
- **Leaderboard hygiene (LOCKED):** backtest/reconstructed P&L NEVER goes on the
  Strategy Leaderboard. Backtests live in TradingView + a `backtest_notes.md`
  style file. A leaderboard registry entry is added ONLY when/if the strategy
  goes to forward paper, with an honest `live_start_iso`, exactly as done for
  `variants/v0.12-sbd-exit`. Three-layer guard pattern reused.

## 6. Validation / backtest campaign (the real work)

Sequenced, evidence-gated:
1. **Fix v1 mechanics:** position sizing; confirm short-side fires; sanity-check
   on SOL 60m (trade count, that both directions trigger).
2. **In-sample tune (SOL only):** sweep `rangeMult`, `volMult`, `rocZMin`,
   `chandMult`, `stopMult`, `maxBars`. Record the surface; pick a *robust*
   region, not the single best cell.
3. **Out-of-sample robustness:** apply the SOL-chosen params unchanged to DOGE,
   AVAX, LINK, BTC, ETH. Edge must generalize — no per-symbol refit.
4. **Head-to-head:** vs approach C (cross-sectional momentum rotation,
   BTC-relative-strength, Codex-Apex-style) on the same symbols/window.
5. **Window check:** full available history + an explicit slice over the contest
   window (2026-05-04 →) to see what it would have contributed.
6. **Decision:** ship to forward paper only if §7 criteria pass; else document
   the failure in `backtest_notes.md` and stop.

## 7. Success criteria (acceptance bar)

- Net positive AND profit factor **> 1.3** out-of-sample (steps 3–4),
- positive expectancy across **≥ 4 of 6** symbols (not one-symbol-carried),
- max strategy drawdown bounded (< buy-hold DD on the same window),
- trade sample large enough to be non-noise (target ≥ 30 closed trades
  aggregate OOS),
- beats approach C on risk-adjusted return, OR is clearly complementary.

If these do not all hold: **report failure, do not ship.**

## 8. Non-goals

- No leverage/margin/perps/options.
- No leaderboard exposure of backtest numbers.
- Not a BULL `strategy.md` change (separate sleeve; BULL mandate untouched).
- No per-symbol parameter overfitting.
- Not a high-frequency scalper (commission-bled) — convex, lower-frequency.

## 9. Open risks

- Ignition entries are late by construction (enter after the expansion bar) →
  slippage/whipsaw on exhaustion bars; mitigated by fast ATR stop, measured in
  backtest, not assumed away.
- Strict thresholds → sparse sample in 18 days; the strategy is a slow-burn
  optionality sleeve, not a contest silver bullet. Framed honestly to user.
- Curve-fit risk on the SOL in-sample tune → the OOS gate (step 3) is the guard.
