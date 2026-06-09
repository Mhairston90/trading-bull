# Variant v0.8-mean-rev-relaxed — Synthetic Trade Log

> Paper-paper. Same schema as parent v0.4.

| Timestamp (UTC) | Action | Pair | Side | Size | Price | Stop | Target | R | Reason | Variant |
|-----------------|--------|------|------|------|-------|------|--------|---|--------|---------|

| 2026-06-05T04:00Z | OPEN | NEAR/USD | LONG | 1087.076038 | 2.1241 | 1.986115 | — | — | entry-rule-v0.8-meanrev (M1 4H>200EMA ✓, M2 RSI 26.9<30 ✓, M3 reversal candle ✓, M4 $26.8M ✓; stop 1.5×ATR 0.137985; mcp-outage gap replay 2026-06-09, user-directed) | v0.8-mean-rev-relaxed |
| 2026-06-05T08:00Z | CLOSE | NEAR/USD | LONG | 1087.076038 | 1.986115 | — | — | -1.00 | exit-stop-hit (X2 1.5×ATR, intra-bar; PnL -$150.00; mcp-outage gap replay 2026-06-09) | v0.8-mean-rev-relaxed |
