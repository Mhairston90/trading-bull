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
