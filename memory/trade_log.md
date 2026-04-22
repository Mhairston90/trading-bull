# BULL Trade Log

> **Append-only. Source of truth.** `portfolio.md` is rebuilt from this file each wake.
> Each entry = one trade event (open or close).
> Rows older than 30 days are moved to `memory/archive/YYYY-MM.md` by routine #3 on the last trading day of the month.

## Schema

| Timestamp (UTC) | Event | Pair | Side | Size | Price | Stop | Target | R at exit | Realized PnL | Reason tag |
|-----------------|-------|------|------|------|-------|------|--------|-----------|--------------|------------|

## Entries

| 2026-04-21T18:00:00Z | OPEN | TRX/USD | long | 7531 | 0.331943 | 0.330285 | — | — | — | entry-rule-v0-momentum |
| 2026-04-21T20:00:00Z | OPEN | LTC/USD | long | 45.2 | 55.27 | 54.61 | — | — | — | entry-rule-v0-momentum |
| 2026-04-22T04:05:00Z | OPEN | BTC/USD | long | 0.0322 | 77600.4 | 76454.3 | — | — | — | entry-rule-v0-momentum |
