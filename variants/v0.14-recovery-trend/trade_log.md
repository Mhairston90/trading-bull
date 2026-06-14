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
| 2026-06-13T09:00Z | CLOSE | TAO/USD | LONG | 32.17 | 237.3015 | — | — | +4.29 | exit-4R-target (08:00Z bar close 237.3015 ≥ 4R target 235.9396; PnL: 32.17 × $20.0155 = +$643.90; 4R fires before EMA exit check; routine-07 2026-06-13 22:00 PT) | v0.14-recovery-trend |
| 2026-06-13T13:00Z | OPEN | BTC/USD | LONG | 0.1660 | 64100.0 | 63677.02 | 65791.92 | — | entry-rule-v0.14-momentum-OVERNIGHT (12:00Z bar close 64100.0; R1: 64100 > EMA20 ~63850 ✓; R2: RSI ~58 ≥ 55 ✓; R3-20: 4H close > 4H 20-EMA ~62652 ✓ clear +$1448; no vol-comp (v0.14 does not inherit); cluster 0/2→1/2 ✓; ATR 211.49, 2×ATR=422.98; cash-binding 0.1660 BTC, risk $70.21/0.66% of $10,645.15; routine-07 2026-06-13 22:00 PT) | v0.14-recovery-trend |
| 2026-06-13T18:00Z | CLOSE | BTC/USD | LONG | 0.1660 | 63944.3 | — | — | -0.37 | exit-ema20-2bar-W22G (2nd consecutive 1H close below EMA20: 16:00Z close 63988.5 [1st], 17:00Z close 63944.3 [2nd]; stop 63677.02 not hit; 4R 65791.92 not reached; PnL: 0.1660 × ($63,944.3 − $64,100.0) = −$25.85/−0.37R; routine-07 2026-06-13 22:00 PT) | v0.14-recovery-trend |
| 2026-06-14T04:00Z | OPEN | BTC/USD | LONG | 0.1651 | 64320.2 | 63897.22 | 66012.12 | — | entry-rule-v0.14-momentum-EOD (indicators.py 04:00Z bar: BTC close 64320.2; R1 ✓; RSI 56.8 ≥ 55 ✓; R3-20: 4H close > 4H 20-EMA ~63382.3 ✓ +$937.9 (indicators R3-20 PASS); R4a ✓; 5a 15/15 pos ✓; SBD CLEAR ✓; no vol-comp; cluster 0/2→1/2 ✓; ATR 211.49, 2×ATR=422.98; stop=64320.2−422.98=63897.22; target=64320.2+1691.92=66012.12; cash-binding 0.1651 BTC, risk $69.77/0.66% of $10,619.30; routine-07 2026-06-13 22:00 PT) | v0.14-recovery-trend |
