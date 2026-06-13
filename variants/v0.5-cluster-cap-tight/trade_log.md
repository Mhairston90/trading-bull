# Variant v0.5-cluster-cap-tight — Synthetic Trade Log

> **Append-only.** Hypothetical paper-paper trades.
> **No real Kraken orders.**

## Schema

| Timestamp (UTC) | Action | Pair | Side | Size | Price | Stop | Target | R | Reason | Variant |
|-----------------|--------|------|------|------|-------|------|--------|---|--------|---------|

`Action` ∈ {OPEN, CLOSE}
`Reason` cites entry/exit rule (e.g. `entry-rule-v0.5-momentum-cluster1`, `exit-stop-hit`, `exit-ema-cross`, `exit-target-4R`)
`Variant` always `v0.5-cluster-cap-tight`

## Trades

| 2026-05-30T13:00Z | OPEN | HYPE/USD | LONG | 77 | 68.06 | 66.13 | 75.80 | — | entry-rule-v0.5-momentum-OVERNIGHT | v0.5-cluster-cap-tight |
| 2026-05-31T11:00Z | CLOSE | HYPE/USD | LONG | 77 | 68.29 | — | — | +0.12 | exit-ema-cross (PnL +$17.71; mcp-outage gap replay 2026-06-09, user-directed; marginal call: close 68.29 vs EMA20 68.2922) | v0.5-cluster-cap-tight |
| 2026-06-12T04:00Z | OPEN | BTC/USD | LONG | 0.157932 | 63430.6 | 62647.6 | 66562.6 | — | entry-rule-v0.5-momentum-EOD (1H close 63430.6 > EMA20 ~63200 ✓; 1H RSI 57.4 ≥ 55 ✓; 4H close 63430.6 > 4H 50-EMA ~63013 ✓ marginal +$417; rule 4 BTC liq ✓; 5a 10/15 pos ✓; SBD CLEARED ✓; cluster 1/1 ✓; ATR 391.5, stop 2×ATR=783, size cash-capped 0.157932 BTC, risk $123.7/1.23%) | v0.5-cluster-cap-tight |
| 2026-06-12T06:45Z | CLOSE | BTC/USD | LONG | 0.157932 | 63430.6 | — | — | 0.00 | void-entry-correction (interactive: the wake's 4H 50-EMA ~$63,013 was a 60-bar-seed artifact; converged 720-bar 4H 50-EMA = $63,682.6 → rule 3 FAILS by $252. v0.5 shares main's rule 3 verbatim — this entry was a computation error, not a hypothesis divergence. Voided at entry price, $0 PnL, twin fidelity restored to main's correct deferral. Warm-up spec fixed in routines 01/03/07 same session.) | v0.5-cluster-cap-tight |
| 2026-06-13T04:00Z | OPEN | TAO/USD | LONG | 32.22 | 217.286 | 212.6226 | 235.9396 | — | entry-rule-v0.5-momentum-EOD (1H close 217.286 > EMA20 213.406 ✓ +$3.88; RSI 62.5 ≥ 55 ✓; 4H close 217.286 > 4H 50-EMA 214.065 ✓ HIGH-CONFIDENCE (720 bars) +$3.22; vol $3.04M ≥ $2M ✓; 5a 4/15 pos ✓; SBD CLEAR ✓; cluster 0/1 ✓ TAO in cluster; ATR 2.3317 2×ATR=4.6634; risk $150.27/1.50% of $10,017.71; sole passing pair at EOD; routine-07 2026-06-12 22:00 PT) | v0.5-cluster-cap-tight |
