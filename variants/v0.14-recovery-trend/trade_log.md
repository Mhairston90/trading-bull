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
