# Variant v0.10-exit-confirm — Synthetic Trade Log

> Paper-paper. Same schema as main v0.2 trade_log.

| Timestamp (UTC) | Event | Pair | Side | Size | Price | Stop | Target | R at exit | Realized PnL | Reason tag |
|-----------------|-------|------|------|------|-------|------|--------|-----------|--------------|------------|

| 2026-05-30T13:00Z | OPEN | HYPE/USD | long | 77 | 68.06 | 66.13 | 75.80 | — | — | entry-rule-v0.2-momentum-OVERNIGHT |
| 2026-05-31T12:00Z | CLOSE | HYPE/USD | long | 77 | 67.72 | — | — | -0.18 | -26.18 | exit-ema20-confirm (2-bar; mcp-outage gap replay 2026-06-09, user-directed) |
