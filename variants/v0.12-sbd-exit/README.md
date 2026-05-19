# Variant v0.12 — sbd-exit (hypothesis / instrumented twin)

**Spin-up date:** 2026-05-19
**Source idea:** Fragility audit 2026-05-19 (interactive session) → Ring-2 proposal 2026-W21-F, user-approved `[Y B]` (adopt live) **+** this variant. Origin lesson: `memory/lessons.md` 2026-05-19 "synchronized-breakdown defensive asymmetry."
**Variant category:** LAB (hypothesis)
**Relationship to main:** main BULL was simultaneously upgraded to **v0.3** with the same 5a-SBD / Exit 1-SBD rules. This variant is the **instrumented paper-paper twin**: it isolates the SBD change so its avoided-give-back can be measured cleanly against the **v0.2 pre-change baseline**, free of live-execution noise (MCP gaps, fill slippage, concurrent-routine races). It is NOT a competing hypothesis to v0.3 — it is v0.3's measurement harness.

**Hypothesis:** In a synchronized-breakdown regime (≤1/15 universe pairs positive 24h AND median 24h ≤ −1.0%), tightening the trend exit from 1H<20-EMA to 1H<9-EMA flattens open longs earlier and preserves unrealized R that v0.2 surrenders by riding the slower 20-EMA down (XRP 2026-05-14 archetype: ran ~+2.8R, exited −0.14R). Expected effect: less give-back in multi-day risk-off, at the cost of occasionally giving up a sharp V-reversal bounce. Net give-back-avoided vs. whipsaw-cost is exactly what this variant quantifies.

**Diff vs v0.2 baseline:**
- **Added** rule 5a-SBD: classify regime = SYNCHRONIZED_BREAKDOWN when (i) ≤1/15 pairs positive 24h AND (ii) median universe 24h % ≤ −1.0%. Strict subset of a 5a fail; reject-all-entries unchanged.
- **Added** Exit rule 1-SBD: while SBD active, trend exit = 1H close < 1H **9-EMA** (vs default 20-EMA). Reverts on SBD clear.
- Exit rules 2 (2×ATR static stop), 3 (4R target) and ALL entry rules / sizing / kill switches inherited verbatim from v0.2.
- This is exactly the v0.3 ruleset; the variant exists for isolated measurement + the avoided-give-back telemetry.

## Mandate-compliance check

- [x] **Spot only** — no leverage/margin/perps/options; SBD only tightens an exit (long-only preserved, no shorting)
- [x] **≤ 8 positions** — inherited from v0.2 (rule 6, active cap 4)
- [x] **≤ 1.5% per trade** — sizing inherited; a faster exit only *reduces* realized risk, never increases it
- [x] **≤ 4% portfolio** — inherited (rule 7)
- [x] **Universe** from `memory/universe.md` — inherited
- [x] **$10K start** — synthetic
- [x] **Paper-paper only** — no real Kraken orders
- [x] **Inherits Ring-3 kill switches** from `memory/guardrails.md`

All 8 checks pass. Strictly risk-reducing vs v0.2 — it can only flatten a long earlier, never widen exposure or short.

## Tuneable parameters (Phase 1 autoloop)

| Parameter | Current value | Sweep range | Notes |
|-----------|--------------:|-------------|-------|
| `sbd_breadth_max` | 1 | 0 – 3 | Max # of 15 pairs positive 24h to qualify as SBD. Lower = stricter/rarer. |
| `sbd_median_max` | -1.0 | -2.0 – -0.5 | Max median universe 24h % to qualify as SBD. More negative = deeper break required. |
| `sbd_exit_ema` | 9 | 5 – 15 | Fast EMA used for the tightened SBD trend exit. Lower = exits even faster, more whipsaw. |

## Promotion criteria

Standard from `variants/README.md`: 30+ days live, beats main on net return + profit factor, DD increase ≤ 25%, ≥ 10 trades in rolling 30d. Earliest promotion-eligible: **2026-06-18**. Note: since main is already v0.3 (= these rules), "promotion" here means the autoloop may instead sweep `sbd_*` params and propose a *tuned* SBD config via the normal Ring-2 channel.

## Honest caveats

- No backtest (TradingView harness unavailable per recent routine #4 logs) — this variant IS the evidence-gathering mechanism for the SBD change that was adopted live on thin (1-trade) evidence.
- SBD is a rare state; in calm/mixed tape this variant is byte-for-byte identical to v0.2, so early sample will be sparse until the next genuine synchronized risk-off.
- Whipsaw (giving up a V-reversal bounce) is a real, not hypothetical, cost — the dual breadth+depth gate reduces but does not eliminate it. The variant measures the net.
- Sibling exit-logic variants: v0.10-exit-confirm, v0.11-breakeven-2R.
