# Variant v0.14-recovery-trend — Synthetic Trade Log

> **Append-only.** Hypothetical paper-paper trades.
> **No real Kraken orders.**

## Schema

| Timestamp (UTC) | Action | Pair | Side | Size | Price | Stop | Target | R | Reason | Variant |
|-----------------|--------|------|------|------|-------|------|--------|---|--------|---------|

`Action` ∈ {OPEN, CLOSE}
`Reason` cites entry/exit rule (e.g. `entry-rule-v0.14-momentum-recovery`, `exit-stop-hit`, `exit-ema20-confirm`, `exit-4R-target`)
`Variant` always `v0.14-recovery-trend`

## Trades

| 2026-06-12T04:00Z | OPEN | BTC/USD | LONG | 0.157653 | 63430.6 | 62647.6 | 66562.6 | — | entry-rule-v0.14-momentum-EOD (1H close 63430.6 > EMA20 ~63200 ✓; 1H RSI 57.4 ≥ 55 ✓; **rule 3: 4H 63430.6 > 4H 20-EMA ~62409 ✓ clear +$1021**; 5a 10/15 pos ✓; SBD CLEARED ✓; cluster 0/4→1/4 ✓; ATR 391.5, stop 783, size cash-capped 0.157653 BTC, risk $123.4/1.23%) | v0.14-recovery-trend |
| 2026-06-12T22:00Z | CLOSE | BTC/USD | LONG | 0.157653 | 63438.5 | — | — | +0.01 | exit-ema20-confirm (two consecutive 1H closes < 1H 20-EMA: bar opening 20:00Z close 63423.1 < EMA ~63497.6 [1st]; bar opening 21:00Z close 63438.5 < EMA ~63491.7 [2nd]; exit fires at 22:00Z bar close 63438.5. Stop 62647.6 never threatened — min low 62765.3 on 06:00Z bar. 4R target 66562.6 not reached — max close 63943.4. No breakeven ratchet — 2R level 64997 never reached. PnL: 0.157653 × 7.9 = +$1.25 / +0.01R.) | v0.14-recovery-trend |
| 2026-06-13T04:00Z | OPEN | TAO/USD | LONG | 32.17 | 217.286 | 212.6226 | 235.9396 | — | entry-rule-v0.14-momentum-EOD (1H close 217.286 > EMA20 213.406 ✓ +$3.88; RSI 62.5 ≥ 55 ✓; R3-20: 4H close 217.286 > 4H 20-EMA ~211.3 ✓ +$5.99; vol $3.04M ✓; 5a 4/15 pos ✓; SBD CLEAR ✓; cluster 0/2→1/2 ✓; ATR 2.3317 2×ATR=4.6634; risk $150.02/1.50% of $10,001.25; post-BTC-exit same-bar re-entry to TAO — sole pair passing all rules at EOD; routine-07 2026-06-12 22:00 PT) | v0.14-recovery-trend |
