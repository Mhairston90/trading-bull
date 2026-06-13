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

| 2026-06-13T04:00Z | OPEN | TAO/USD | LONG | 32.17 | 217.286 | 212.6226 | 235.9396 | — | entry-rule-v0.3-momentum-volcomp-EOD (1H close 217.286 > EMA20 213.406 ✓ +$3.88; RSI 62.5 ≥ 55 ✓; 4H close 217.286 > 4H 50-EMA 214.065 ✓ HIGH-CONF +$3.22; vol $3.04M ≥ $2M ✓; vol-comp gate 5c: TAO ATR 2.4062 vs 0.5×mean — SHUT (not triggered) → entry ALLOWED; 5a 4/15 pos ✓; SBD CLEAR ✓; cluster 0/2→1/2 ✓; ATR 2.3317 2×ATR=4.6634; risk $150.00/1.50% of $10,000; first hypothetical trade for v0.3 — 45d to first entry; sole pair passing all rules at EOD; routine-07 2026-06-12 22:00 PT) | v0.3-vol-compression |
