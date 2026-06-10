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

(empty — spun up 2026-06-09)
