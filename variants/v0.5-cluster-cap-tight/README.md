# Variant v0.5 — cluster-cap-tight

**Spin-up date:** 2026-04-29
**Source idea:** internal — direct response to lesson 2026-04-27 cascade event (4 simultaneous correlated stops in 1 bar). Even with W18-A's cluster cap of 2, two correlated entries can still tail-loss together.
**Hypothesis:** A cluster cap of 1 (vs main's 2) on the BTC-correlated pair set further reduces tail risk during regime flips that cascade through correlated assets. Trade frequency drops modestly; per-cluster-event drawdown is halved.
**Diff vs main (currently v0.2):**
- **Modified** rule 6a: cluster cap reduced from `<= 2` to `<= 1` for BTC-correlated set {BTC, ETH, SOL, TAO, AVAX, SUI, LINK}
- All other rules (1, 2, 2a, 3, 4, 4a, 5, 5a, 5b, 6, 7, 8) inherited verbatim from v0.2

## Mandate-compliance check

- [x] Spot only — single rule parameter change, no instrument shift
- [x] ≤ 8 positions — inherited from main (rule 6, cap of 4 active)
- [x] ≤ 1.5% per trade — sizing inherited
- [x] ≤ 4% portfolio — inherited (rule 7); tighter cluster cap actually reduces realistic risk
- [x] Universe from `memory/universe.md` — inherited
- [x] $10K start — synthetic
- [x] Paper-paper only — no real Kraken orders
- [x] Inherits Ring-3 kill switches from `memory/guardrails.md`

All checks pass.

## Promotion criteria

Standard from `variants/README.md`. Earliest promotion-eligible: **2026-05-29**.

## Threshold rationale

The cascade event of 2026-04-27T05:00Z stopped 4 simultaneous cluster positions in one 1H bar. W18-A applied cluster cap = 2 to prevent that exact failure. But:
- 2 correlated entries × 1.06R average loss = 2.12R cluster-event loss (still ~$100 on $10K with 1.5% risk/trade)
- 1 correlated entry × 1.06R = 1.06R cluster-event loss (~$50)

The trade-off:
- **Cap 1 (this variant):** halves realistic worst-case cluster loss; misses ~half the cluster-trend opportunities
- **Cap 2 (main):** allows 2 cluster fills; one cascade event consumes 4× the tail loss

Whether the foregone upside in clean cluster rallies outweighs the saved tail loss is what this variant tests.

## What this variant explicitly does NOT do

- Does not change risk per trade, stop distance, exit rules, RSI bounds, regime gate, re-entry cooldown, liquidity floor, or one-per-wake
- Does not modify the cluster set itself (same 7 pairs as W18-A: BTC, ETH, SOL, TAO, AVAX, SUI, LINK)
- Does not affect non-cluster pairs (XRP, HYPE, XDG, LTC, ADA, FARTCOIN, PENGU, TRX trade independently per rule 6 cap of 4)

## Expected behavior

- In normal regime: variant takes ~1 fewer cluster trade per week vs main. Slightly lower trade count.
- In cluster-trend regime (e.g., broad market rally): variant captures only 1 of N cluster pairs that go up; main captures up to 2. Variant under-performs by the spread between the missed second cluster trade and what it could have been.
- In cluster-cascade regime (e.g., 2026-04-27): variant suffers 1-cluster stop instead of 2-cluster stop. Saves roughly 1R per cascade event.
- Net effect (hypothesis): better drawdown profile, modestly lower net return in trend regimes, comparable or better in cascade regimes.

## Source

From `memory/lessons.md` 2026-04-27 cross-asset cascade lesson:
> "v0 sizing assumes positions are independent for the 4% portfolio-risk cap. They are not — top-cap crypto pairs are highly correlated, especially in fast tape."

W18-A applied cluster cap = 2 as the first response. v0.5 tests whether tightening further is the better tradeoff.

## Honest caveats

- No backtest. Whether cap-1 is "too tight" depends on the frequency of cluster-trend regimes (where main outperforms) vs cluster-cascade regimes (where variant outperforms).
- Sample size will be low — cluster events themselves are infrequent. The 30-day window may not capture even one. Promotion likely requires longer-window evidence than other variants.
- Tightest defensible cap is "cluster cap = 0" (no concurrent cluster trades) — that's TOO tight to be useful and would essentially halve trade frequency on the cluster pairs. Skipping that as a separate variant.
