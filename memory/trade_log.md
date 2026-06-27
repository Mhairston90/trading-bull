# BULL Trade Log

> **Append-only. Source of truth.** `portfolio.md` is rebuilt from this file each wake.
> Each entry = one trade event (open or close).
> Rows older than 30 days are moved to `memory/archive/YYYY-MM.md` by routine #3 on the last trading day of the month.

## Schema

| Timestamp (UTC) | Event | Pair | Side | Size | Price | Stop | Target | R at exit | Realized PnL | Reason tag |
|-----------------|-------|------|------|------|-------|------|--------|-----------|--------------|------------|

## Entries

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
| 2026-06-13T04:00:00Z | OPEN | TAO/USD | long | 32.985 | 217.286 | 212.6226 | 235.9396 | — | — | entry-rule-v0.4-momentum |
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
| 2026-05-26T18:00:00Z | CLOSE | TAO/USD | long | 15.273800 | 280.40233 | — | — | -0.58 | -114.75 | exit-ema20-confirm-missed-scheduler-replay |
| 2026-05-30T04:00:00Z | OPEN | XRP/USD | long | 5769.659 | 1.34870 | 1.32178 | 1.45638 | — | — | entry-rule-v0.4-momentum |
| 2026-05-30T23:00:00Z | CLOSE | XRP/USD | long | 5769.659 | 1.33811 | — | — | -0.65 | -101.40 | exit-ema20-confirm-missed-scheduler-replay |
| 2026-06-13T09:00:00Z | CLOSE | TAO/USD | long | 32.985 | 237.3015 | — | — | +4.04 | +621.22 | exit-4R-target-missed-scheduler-replay |
| 2026-06-13T15:00:00Z | OPEN | BTC/USD | long | 0.168 | 64188.10 | 63720.62 | 66058.02 | — | — | entry-rule-v0.4-momentum |
| 2026-06-14T13:00:00Z | CLOSE | BTC/USD | long | 0.168 | 64240.66 | — | — | -0.60 | -47.27 | exit-ema20-confirm-missed-scheduler-replay |
| 2026-06-16T12:00:00Z | OPEN | ETH/USD | long | 5.1162 | 1797.88 | 1766.13 | 1924.87 | — | — | entry-rule-v0.4-momentum |
| 2026-06-16T15:00:00Z | CLOSE | ETH/USD | long | 5.1162 | 1765.25 | — | — | -1.32 | -214.33 | exit-stop-hit-missed-scheduler-replay |
| 2026-06-17T04:00:00Z | OPEN | HYPE/USD | long | 56.342770 | 74.4972 | 71.6714 | 85.8004 | — | — | entry-rule-v0.4-momentum |
| 2026-06-17T12:00:00Z | CLOSE | HYPE/USD | long | 56.342770 | 71.6356 | — | — | -1.15 | -182.64 | exit-stop-hit-missed-scheduler-replay |
| 2026-06-17T17:00:00Z | OPEN | SOL/USD | long | 104.454002 | 73.7268 | 72.2288 | 79.7189 | — | — | entry-rule-v0.4-momentum-rule8-fallback |
| 2026-06-17T18:00:00Z | CLOSE | SOL/USD | long | 104.454002 | 72.1927 | — | — | -1.28 | -199.87 | exit-stop-hit |
| 2026-06-20T13:00:00Z | OPEN | SOL/USD | long | 121.5347 | 71.17 | 69.9072 | 76.2212 | — | — | entry-rule-v0.4-momentum |
| 2026-06-22T15:00:00Z | CLOSE | SOL/USD | long | 121.5347 | 73.08 | — | — | +1.51 | +232.13 | exit-ema20-confirm-missed-scheduler-replay |
| 2026-06-22T16:00:00Z | CLOSE | SOL/USD | long | 121.5347 | 73.0435 | — | — | +1.19 | +182.13 | correction-previous-row |
| 2026-06-27T16:00:00Z | OPEN | SOL/USD | long | 110.1608 | 72.7364 | 71.3184 | 78.4084 | — | — | entry-rule-v0.4-momentum |
| 2026-06-27T19:00:00Z | CLOSE | SOL/USD | long | 110.1608 | 71.2827 | — | — | -1.29 | -201.55 | exit-stop-hit-intrabar |
