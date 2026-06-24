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
| 2026-06-13T09:00Z | CLOSE | TAO/USD | LONG | 32.17 | 237.3015 | — | — | +4.29 | exit-4R-target (08:00Z bar close 237.3015 ≥ 4R target 235.9396; entry 217.286, ATR 2.3317, R=$4.6634; PnL: 32.17 × $20.0155 = +$643.90; stop 212.6226 never threatened; routine-07 2026-06-13 22:00 PT) | v0.3-vol-compression |
| 2026-06-13T13:00Z | OPEN | BTC/USD | LONG | 0.1660 | 64100.0 | 63677.02 | 65791.92 | — | entry-rule-v0.3-momentum-volcomp-OVERNIGHT (12:00Z bar close 64100.0; R1: 64100 > EMA20 ~63850 ✓; R2: RSI ~58 ≥ 55 ✓; R3: 4H close > 4H 50-EMA ~63762 +$338 ✓; R4a liquidity ✓; 5a pos ✓; vol-comp 5c: BTC ATR ~$211 vs 0.5×mean ~$206 — shut at 0.5 threshold → ALLOWED ✓; cluster 1/2 (TAO exited; BTC enters) ✓; ATR 211.49, 2×ATR=422.98; stop=64100−422.98=63677.02; target=64100+1691.92=65791.92; cash-binding 0.1660 BTC, risk $70.21/0.66% of $10,643.90; rule 8 BTC rank-1; routine-07 2026-06-13 22:00 PT) | v0.3-vol-compression |
| 2026-06-13T17:00Z | CLOSE | BTC/USD | LONG | 0.1660 | 63988.5 | — | — | -0.26 | exit-ema-cross-1bar (16:00Z bar close 63988.5 < 1H EMA20 ~64003 — single-bar v0.3 exit rule; stop 63677.02 not hit (lowest low 63893.2 on 16:00Z bar); 4R target 65791.92 not reached (highest close ~64561 at 01:00Z bar); PnL: 0.1660 × ($63,988.5 − $64,100.0) = −$18.51/−0.26R; routine-07 2026-06-13 22:00 PT) | v0.3-vol-compression |
| 2026-06-14T04:00Z | OPEN | SOL/USD | LONG | 155 | 68.49 | 67.560 | 72.210 | — | entry-rule-v0.3-momentum-volcomp-EOD (indicators.py 04:00Z bar: SOL close 68.49 > EMA20 68.325 ✓ +$0.165; RSI 56.1 ≥ 55 ✓; 4H 50-EMA PASS ✓; vol $12.85M ✓; 5a 15/15 pos ✓; SBD CLEAR ✓; vol-comp 5c: BTC blocked OPEN/OPEN at 0.5 threshold; SOL volcomp_05=shut → ALLOWED ✓; cluster 0/2→1/2 ✓; ATR 0.465, 2×ATR=0.930; stop=68.49−0.930=67.560; target=68.49+3.720=72.210; risk: 155×$0.930=$144.15/1.36% of $10,625.39; cash-binding 155 SOL; rule 8 BTC/HYPE blocked → SOL rank-3 wins; routine-07 2026-06-13 22:00 PT) | v0.3-vol-compression |
| 2026-06-14T06:00Z | CLOSE | SOL/USD | LONG | 155 | 68.24 | — | — | -0.27 | exit-ema20-1bar (05:00Z bar close 68.24 < 1H EMA20 ~68.35; single-bar v0.3 exit rule fires; stop 67.560 not hit; 4R target 72.210 not reached; PnL: 155×($68.24−$68.49) = −$38.75/−0.27R; gap replay 2026-06-14T05:00Z→2026-06-24T13:00Z via routine07_replay_20260623.py; routine-07 2026-06-24 PT) | v0.3-vol-compression |
