# Variant v0.15-meanrev-guarded — Synthetic Trade Log

> **Append-only.** Hypothetical paper-paper trades.
> **No real Kraken orders.**

## Schema

| Timestamp (UTC) | Action | Pair | Side | Size | Price | Stop | Target | R | Reason | Variant |
|-----------------|--------|------|------|------|-------|------|--------|---|--------|---------|

`Action` ∈ {OPEN, CLOSE}
`Reason` cites entry/exit rule (e.g. `entry-rule-v0.15-meanrev-guarded`, `exit-ema20-target`, `exit-stop-hit`, `exit-time-stop-24bar`)
`Variant` always `v0.15-meanrev-guarded`

## Trades

(empty — spun up 2026-06-09)
