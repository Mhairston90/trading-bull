# BULL Lessons

> **Capped at ~50 entries.** Weekly routine #4 prunes lowest-scored lessons.
> Each lesson: one observation + evidence + implication for strategy.

## Schema

Each lesson is a section:

```
### <date> — <short title>

**Observation:** <what BULL saw in the data>
**Evidence:** <pointer to trade_log entries, dates, pairs>
**Implication:** <what this suggests about strategy>
**Score:** <1–10, routine #4 assigns and updates>
**Status:** active | superseded | pruned
```

## Lessons

### 2026-04-24 — Low-liquidity wick blew through 2×ATR stop (TRX)

**Observation:** TRX/USD 2026-04-24 intraday low was 0.319711 vs static stop 0.330285 — wick reached ~3.2% below stop. Final 1H close was higher than the wick but the static stop was filled at 0.330120 (with our slippage model).
**Evidence:** trade_log.md row CLOSE TRX/USD 2026-04-24T20:00:00Z (−$26.69 / −1.1R). 24h low 0.319711. Universe note flags TRX as $1.04M/24h notional (rank 15 = thinnest in our universe).
**Implication:** The 2×ATR static stop is sensitive to single-bar wicks on the thinnest pairs in the universe (rank 12+: FARTCOIN, AVAX/LINK borderline, PENGU, TRX). Routine #4 should evaluate (a) widening to 2.5–3×ATR for sub-$2M/24h pairs, or (b) using a closing-bar stop check (no intrabar) on those pairs, or (c) excluding sub-$2M pairs from v0 entries entirely.
**Score:** _(routine #4 will assign)_
**Status:** **superseded** — addressed by W18-B liquidity floor (pairs < $2M/24h excluded from new entries), applied to `strategy.md` 2026-04-28. Implementation chose option (c) — full exclusion below threshold.

### 2026-04-27 — Cross-asset cascade stops out all 4 positions in one 1H bar

**Observation:** ETH, BTC, SOL, TAO all opened the prior wake (21:00Z 04/26 for ETH/BTC/SOL, 04:05Z 04/27 for TAO) on momentum entries with all v0 rules passing. In the very next overlapping 1H bar after entry at 05:00Z 2026-04-27, all four hit their 2×ATR stops intra-bar simultaneously. ETH -2.66% intra-bar, BTC -1.68%, SOL -1.95%, TAO -1.97%. No tier-1/2 risk-flag trigger; classifier called markets "calm". Realized −$153.65 (-1.54% of equity).
**Evidence:** trade_log.md rows OPEN ETH/BTC/SOL 2026-04-26T21:05:00Z, OPEN TAO 2026-04-27T04:05:00Z, all four CLOSEs 2026-04-27T05:00:00Z exit-stop-hit. Strategy v0 max-concurrent 4 → 100% of capacity stopped together. Each individual trade -1.03 to -1.08R; combined -4.23R in single bar.
**Implication:** v0 sizing assumes positions are independent for the 4% portfolio-risk cap. They are not — top-cap crypto pairs are highly correlated, especially in fast tape. When the strategy fills its 4-slot cap with simultaneously-eligible momentum entries, "portfolio risk-at-moment" understates true tail risk by roughly the correlation factor (~0.7-0.9 across BTC/ETH/SOL on 1H). Routine #4 should evaluate (a) a portfolio-correlation cap that throttles concurrent BTC-correlated entries, (b) staggered entries across 4H instead of all-on-the-same-1H-close, or (c) a regime filter that pauses new momentum entries when 1H ATR has compressed below recent average (volatility-pop precursor). Also consider that filling all 4 slots in one 1H wake from a single regime-flip signal is a recipe for this exact failure mode.
**Score:** _(routine #4 will assign)_
**Status:** **superseded** — addressed by W18-A (BTC-cluster correlation cap: max 2 concurrent in {BTC,ETH,SOL,TAO,AVAX,SUI,LINK}) AND W18-C (one entry per wake), both applied to `strategy.md` 2026-04-28. Implementation chose options (a) and (b) from this lesson's recommendations. Volatility-compression filter (option c) deferred to next routine #4 with backtest evidence.

### 2026-04-24 — Commission drag dominates short-lived EMA-cross exits (BTC)

**Observation:** BTC/USD entered 2026-04-22T04:05Z @ 77600.4, exited 2026-04-24T04:00Z @ 77720.72 on EMA cross. Gross PnL = +$5.39 (price moved +$120 in our favor) but two-side commission (~$13.01 at 0.26% per side) flipped it to net −$9.14.
**Evidence:** trade_log.md rows OPEN BTC/USD 2026-04-22T04:05:00Z and CLOSE BTC/USD 2026-04-24T04:00:00Z (R +0.10 gross, −0.21R net after commissions). Trade lifetime ~48h.
**Implication:** v0 EMA-cross exit can fire on small mean reversions where the price barely retraced past the EMA. Net-of-commission breakeven on a $2,500 BTC notional requires ~$13 / 0.0322 = $404 of price movement (~0.52%). Routine #4 should consider (a) requiring an exit-confirmation bar (e.g., 2 closes below EMA), (b) replacing 1-EMA exit with a slower trailing stop, or (c) raising the entry RSI threshold so we only enter trades with stronger expected runs.
**Score:** _(routine #4 will assign)_
**Status:** active
