# Variant v0.11 — breakeven-2R (hypothesis)

**Spin-up date:** 2026-05-16
**Source idea:** internal — `memory/lessons.md` 2026-05-15 "Winner round-tripped from ~+3R unrealized to a scratch loss (XRP)" (score **9** as of 2026-W20). Lesson recommendation (a): "move-stop-to-breakeven once unrealized ≥ 2R."
**Variant category:** LAB (hypothesis)
**Hypothesis:** v0.2's static 2×ATR stop never moves, and the only profit-protection is a far 4R fixed target (hit just 1 of 17 closed trades inception-to-date) plus a slow 20-EMA trailing exit. A winner can run to +2–3R unrealized and round-trip all the way back to a scratch/small loss (XRP 2026-05-14: ran ~+2.8R close / ~+3.16R high, exited −0.14R). Ratcheting the stop to breakeven once unrealized ≥ 2R caps that give-back: a trade that reaches +2R can no longer become a loser. Expected effect: materially higher win rate and lower variance on the winners that don't reach 4R, at the cost of being stopped flat on some trades that dip to breakeven then resume.

**Diff vs main (currently v0.2):**
- **Added** stop-management rule: once unrealized PnL ≥ **2R** at any 1H close, move the static stop from the original 2×ATR level up to **breakeven (entry price)**. The stop only ratchets up, never down; once at breakeven it stays at breakeven (this variant does not trail further — that is a separate future variant).
- Exit rules 1 (EMA-cross), 2 (static stop — now breakeven-ratcheted), 3 (4R target) otherwise inherited verbatim from v0.2
- All entry rules, sizing, kill switches inherited verbatim from v0.2

## Mandate-compliance check

- [x] **Spot only** — no leverage/margin/perps/options; a stop-management addition
- [x] **≤ 8 positions** — inherited from v0.2 (rule 6, active cap 4)
- [x] **≤ 1.5% per trade** — sizing inherited; moving the stop to breakeven only *reduces* realized risk, never increases it
- [x] **≤ 4% portfolio** — inherited (rule 7); breakeven ratchet lowers portfolio-risk-at-moment as winners mature
- [x] **Universe** from `memory/universe.md` — inherited
- [x] **$10K start** — synthetic
- [x] **Paper-paper only** — no real Kraken orders
- [x] **Inherits Ring-3 kill switches** from `memory/guardrails.md`

All 8 checks pass. (This variant is strictly risk-reducing vs v0.2 — it can only move a stop tighter, never wider.)

## Tuneable parameters (Phase 1 autoloop)

| Parameter | Current value | Sweep range | Notes |
|-----------|--------------:|-------------|-------|
| `breakeven_trigger_R` | 2.0 | 1.0 – 3.0 | Unrealized-R threshold at which the stop ratchets to breakeven. Lower = protects sooner but stopped flat more often on noise; higher = lets more profit accrue but exposes more give-back. |

## Promotion criteria

Standard from `variants/README.md`: 30+ days live, beats main on net return + profit factor, DD increase ≤ 25%, ≥ 10 trades in rolling 30d. Earliest promotion-eligible: **2026-06-15**.

## Why a variant instead of a Ring-2 proposal now

The profit-give-back lesson is score 9 — the highest-value open exit-logic gap (the 4R target is reached only 1/17 trades, so nearly every winner is exposed to full round-trip; XRP alone surrendered ~3R / ~$460). A Ring-2 strategy-edit proposal requires backtest evidence (guardrails logging obligation); TradingView Desktop is not installed (`tv_launch` finds no binary; 2nd consecutive harness blocked). This variant converts the blocked proposal into a paper-paper evidence track that accrues via routine #7 with no TV dependency. Pairs with v0.10-exit-confirm (commission-drag lesson) — together they form the combined exit-logic Ring-2 proposal both lessons call for, once 30d evidence exists or TV returns for a 180d backtest.

## Expected behavior vs main

- **Winners that reach ≥2R then reverse** (XRP 2026-05-14 archetype): v0.11 exits at breakeven (≈ scratch, minus friction) instead of riding the 20-EMA down to a loss — converts a −0.14R into ≈ 0R (still pays round-trip friction).
- **Winners that reach ≥2R and continue** (SOL 2026-05-08 archetype, +4.03R): unaffected — stop at breakeven is never threatened; 4R target still captures the move identically.
- **Trades that dip to breakeven after hitting 2R then resume up:** v0.11 is stopped flat and misses the continuation — the main cost of this rule. Frequency of this vs. the give-back it prevents is exactly what the variant measures.
- **Trades that never reach 2R:** identical to main (rule never activates).
- Net effect (hypothesis): higher win rate, lower drawdown, lower variance; net return ambiguous (depends on how often 2R-then-resume happens vs 2R-then-roundtrip).

## Honest caveats

- No backtest yet (TV unavailable) — this variant IS the evidence-gathering mechanism. Do not promote on hypothesis alone.
- Single-point trigger (2R); `breakeven_trigger_R` declared tuneable so a future autoloop round can sweep 1R/2R/3R once the parent has ≥14d live.
- Does NOT trail beyond breakeven — a fuller trailing-stop mechanism (lesson recommendation b) is a separate future variant; this isolates the breakeven-ratchet effect cleanly.
- In the current broadly-red regime (0/15 universe pairs positive 2026-05-16) v0.2 entries are regime-gated, so early sample may be thin until regime turns.
