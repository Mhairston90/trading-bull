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
| 2026-05-06T19:00:00Z | CLOSE | BTC/USD | long | 0.0299 | 81430.76 | — | — | +0.06 | +1.42 | exit-ema-cross |
| 2026-05-07T01:00:00Z | CLOSE | LTC/USD | long | 41 | 56.25 | — | — | -1.03 | -48.58 | exit-stop-hit |
| 2026-05-07T14:00:00Z | CLOSE | XRP/USD | long | 1723 | 1.39398 | — | — | -1.05 | -37.68 | exit-stop-hit |
| 2026-05-07T20:00:00Z | CLOSE | LINK/USD | long | 257 | 9.890452 | — | — | +1.69 | +103.03 | exit-ema-cross |
| 2026-05-08T17:00:00Z | OPEN | SOL/USD | long | 97.86 | 91.6758 | 90.1932 | — | — | — | entry-rule-v0-momentum |
| 2026-05-11T19:00:00Z | CLOSE | SOL/USD | long | 97.86 | 98.1509 | — | 97.6062 | +4.03 | +585.35 | exit-4R-target |
| 2026-05-14T16:00:00Z | OPEN | XRP/USD | long | 6334 | 1.46806 | 1.44377 | — | — | — | entry-rule-v0-momentum |
| 2026-05-15T13:00:00Z | CLOSE | XRP/USD | long | 6334 | 1.44305 | — | — | -1.03 | -206.37 | exit-stop-hit |
| 2026-05-15T04:00:00Z | CLOSE | XRP/USD | long | 6334 | 1.47224 | — | — | -0.14 | -21.92 | correction-previous-row |
| 2026-05-20T13:00:00Z | OPEN | HYPE/USD | long | 51.165356 | 50.01499 | 48.01639 | 58.00942 | — | — | routine-01-overnight-missed-scheduler-entry |
| 2026-05-21T04:00:00Z | OPEN | TAO/USD | long | 9.515117 | 277.83675 | 271.62362 | 302.68925 | — | — | routine-03-eod-missed-scheduler-entry |
| 2026-05-21T08:00:00Z | CLOSE | HYPE/USD | long | 51.165356 | 58.38080 | — | — | +4.04 | +413.62 | exit-4R-target-missed-scheduler-replay |
| 2026-05-21T13:00:00Z | OPEN | HYPE/USD | long | 46.123284 | 57.74886 | 55.19075 | 67.98128 | — | — | routine-01-overnight-missed-scheduler-entry |
| 2026-05-22T01:00:00Z | CLOSE | TAO/USD | long | 9.515117 | 276.14136 | — | — | -0.50 | -29.84 | exit-ema20-confirm-missed-scheduler-replay |
| 2026-05-22T02:00:00Z | CLOSE | HYPE/USD | long | 46.123284 | 57.31133 | — | — | -0.29 | -33.98 | exit-ema20-confirm-missed-scheduler-replay |
| 2026-05-22T04:00:00Z | OPEN | AVAX/USD | long | 278.438254 | 9.50475 | 9.36712 | 10.05526 | — | — | routine-03-eod-missed-scheduler-entry |
| 2026-05-22T13:00:00Z | OPEN | SOL/USD | long | 30.207436 | 87.70383 | 86.64637 | 91.93366 | — | — | routine-01-overnight-missed-scheduler-entry |
| 2026-05-22T15:00:00Z | CLOSE | SOL/USD | long | 30.207436 | 86.64637 | — | — | -1.43 | -45.64 | exit-stop-hit-missed-scheduler-replay |
| 2026-05-22T16:00:00Z | CLOSE | AVAX/USD | long | 278.438254 | 9.42529 | — | — | -0.94 | -35.83 | exit-ema20-confirm-missed-scheduler-replay |
| 2026-05-25T15:00:00Z | OPEN | BTC/USD | long | 0.0338 | 77678.12 | 77122.02 | 79902.52 | — | — | entry-rule-v0-momentum |
| 2026-05-25T22:00:00Z | CLOSE | BTC/USD | long | 0.0338 | 77083.46 | — | — | -1.07 | -33.70 | exit-stop-hit |
| 2026-05-26T12:00:00Z | OPEN | TAO/USD | long | 15.273800 | 286.40410 | 276.12100 | 327.53650 | — | — | entry-rule-v0-momentum |
