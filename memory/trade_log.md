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
| 2026-04-24T04:00:00Z | CLOSE | BTC/USD | long | 0.0322 | 77720.72 | — | — | +0.10 | -9.14 | exit-ema-cross |
| 2026-04-24T17:00:00Z | OPEN | ADA/USD | long | 9934 | 0.251930 | 0.248716 | — | — | — | entry-rule-v0-momentum |
| 2026-04-24T20:00:00Z | CLOSE | TRX/USD | long | 7531 | 0.330120 | — | — | -1.1 | -26.69 | exit-stop-hit |
| 2026-04-24T17:00:00Z | OPEN | AVAX/USD | long | 265 | 9.4147 | 9.2847 | — | — | — | entry-rule-v0-momentum |
| 2026-04-25T17:00:00Z | CLOSE | LTC/USD | long | 45.2 | 56.432 | — | — | +1.32 | +39.40 | exit-ema-cross |
| 2026-04-25T17:00:00Z | CLOSE | ADA/USD | long | 9934 | 0.249331 | — | — | -1.21 | -38.77 | exit-ema-cross |
| 2026-04-25T17:00:00Z | CLOSE | AVAX/USD | long | 265 | 9.335 | — | — | -0.99 | -34.04 | exit-ema-cross |
| 2026-04-26T21:05:00Z | OPEN | ETH/USD | long | 1.0499 | 2364.72 | 2345.10 | — | — | — | entry-rule-v0-momentum |
| 2026-04-26T21:05:00Z | OPEN | BTC/USD | long | 0.0317 | 78266.21 | 77803.14 | — | — | — | entry-rule-v0-momentum |
| 2026-04-26T21:05:00Z | OPEN | SOL/USD | long | 28.6 | 86.79 | 86.10 | — | — | — | entry-rule-v0-momentum |
| 2026-04-27T04:05:00Z | OPEN | TAO/USD | long | 9.6 | 255.56 | 251.12 | — | — | — | entry-rule-v0-momentum |
| 2026-04-27T05:00:00Z | CLOSE | ETH/USD | long | 1.0499 | 2343.93 | — | — | -1.06 | -34.68 | exit-stop-hit |
| 2026-04-27T05:00:00Z | CLOSE | BTC/USD | long | 0.0317 | 77764.24 | — | — | -1.08 | -28.77 | exit-stop-hit |
| 2026-04-27T05:00:00Z | CLOSE | SOL/USD | long | 28.6 | 86.057 | — | — | -1.06 | -33.82 | exit-stop-hit |
| 2026-04-27T05:00:00Z | CLOSE | TAO/USD | long | 9.6 | 251.004 | — | — | -1.03 | -56.38 | exit-stop-hit |
| 2026-04-28T17:00:00Z | OPEN | TAO/USD | long | 9.4 | 260.12 | 254.74 | — | — | — | entry-rule-v0-momentum |
| 2026-04-29T14:00:00Z | CLOSE | TAO/USD | long | 9.4 | 254.61 | — | — | -1.02 | -64.37 | exit-stop-hit |
| 2026-05-04T19:00:00Z | OPEN | LINK/USD | long | 257 | 9.4393 | 9.2018 | — | — | — | entry-rule-v0-momentum |
| 2026-05-05T05:00:00Z | OPEN | BTC/USD | long | 0.0299 | 80961.16 | 80124.19 | — | — | — | entry-rule-v0-momentum |
| 2026-05-05T17:00:00Z | OPEN | XRP/USD | long | 1723 | 1.40857 | 1.39468 | — | — | — | entry-rule-v0-momentum |
| 2026-05-06T04:00:00Z | OPEN | HYPE/USD | long | 54 | 44.18 | 43.35 | — | — | — | entry-rule-v0-momentum |
| 2026-05-06T15:00:00Z | CLOSE | HYPE/USD | long | 54 | 43.33 | — | — | -1.02 | -58.18 | exit-stop-hit |
| 2026-05-06T15:00:00Z | OPEN | LTC/USD | long | 41 | 57.14 | 56.28 | — | — | — | entry-rule-v0-momentum |
