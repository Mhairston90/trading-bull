# Variant v0.4-mean-reversion-sleeve — Synthetic Trade Log

> **Append-only.** Hypothetical paper-paper trades.
> **No real Kraken orders.** Source of truth for variant performance.

## Schema

| Timestamp (UTC) | Action | Pair | Side | Size | Price | Stop | Target | R | Reason | Variant |
|-----------------|--------|------|------|------|-------|------|--------|---|--------|---------|

`Action` ∈ {OPEN, CLOSE}
`Reason` cites the entry/exit rule (e.g. `entry-rule-v0.4-mean-revert`, `exit-target-1h-ema`, `exit-stop-1.5atr`, `exit-time-stop-24h`)
`Variant` always `v0.4-mean-reversion-sleeve` for rows in this file

## Trades

(empty — variant spun up 2026-04-29)
