# Variant v0.3-vol-compression — Synthetic Trade Log

> **Append-only.** Hypothetical paper-paper trades. Same schema as main `memory/trade_log.md` but flagged as variant trades.
> **No real Kraken orders are placed from this file.**
> **Source of truth** for variant performance — `portfolio.md` is rebuilt from this on every routine #7 wake.

## Schema

| Timestamp (UTC) | Action | Pair | Side | Size | Price | Stop | Target | R | Reason | Variant |
|-----------------|--------|------|------|------|-------|------|--------|---|--------|---------|

`Action` ∈ {OPEN, CLOSE}
`R` is left blank on OPEN, filled on CLOSE
`Reason` cites the entry rule that triggered (e.g., `entry-rule-v0.3-momentum-volcomp`) or exit rule (`exit-stop-hit`, `exit-ema-cross`, `exit-target-4R`)
`Variant` always `v0.3-vol-compression` for rows in this file

## Trades

(empty — variant spun up 2026-04-29; first routine #7 simulation wake will populate)
