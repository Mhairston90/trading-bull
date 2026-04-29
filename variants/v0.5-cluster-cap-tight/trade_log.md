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

(empty — variant spun up 2026-04-29)
