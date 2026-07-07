# BULL Trade Log

> **Append-only. Source of truth.** `portfolio.md` is rebuilt from this file each wake.
> Each entry = one trade event (open or close).
> Rows older than 30 days are moved to `memory/archive/YYYY-MM.md` by routine #3 on the last trading day of the month.
> **Last monthly archive:** 2026-06-30 (routine-03-eod) — moved 31 May-dated rows to `memory/archive/2026-06.md`.

## Schema

| Timestamp (UTC) | Event | Pair | Side | Size | Price | Stop | Target | R at exit | Realized PnL | Reason tag |
|-----------------|-------|------|------|------|-------|------|--------|-----------|--------------|------------|

## Entries

| 2026-06-13T04:00:00Z | OPEN | TAO/USD | long | 32.985 | 217.286 | 212.6226 | 235.9396 | — | — | entry-rule-v0.4-momentum |
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
| 2026-06-29T04:00:00Z | OPEN | SOL/USD | long | 82.3578 | 72.6163 | 70.7563 | 80.0563 | — | — | entry-rule-v0.4-momentum |
| 2026-06-30T04:00:00Z | CLOSE | SOL/USD | long | 82.3578 | 73.9030 | — | 80.0563 | +0.49 | +74.48 | exit-ema20-confirm-missed-scheduler-replay |
| 2026-07-01T04:00:00Z | OPEN | SOL/USD | long | 87.5709 | 75.3538 | 73.5918 | 82.4019 | — | — | entry-rule-v0.4-momentum |
| 2026-07-03T20:00:00Z | CLOSE | SOL/USD | long | 87.5709 | 82.5987 | — | 82.4019 | +3.88 | +598.56 | exit-4R-target-missed-scheduler-replay |
| 2026-07-03T23:00:00Z | OPEN | ETH/USD | long | 5.7481 | 1756.9580 | 1728.5520 | 1870.5820 | — | — | entry-rule-v0.4-momentum-rule8-fallback |
| 2026-07-05T01:00:00Z | CLOSE | ETH/USD | long | 5.7481 | 1764.128 | — | — | -0.07 | -11.38 | exit-ema20-confirm-missed-scheduler-replay |
| 2026-07-05T03:00:00Z | OPEN | ADA/USD | long | 24624 | 0.190146 | 0.183522 | 0.216642 | — | — | entry-rule-v0.4-momentum |
| 2026-07-05T10:00:00Z | CLOSE | ADA/USD | long | 24624 | 0.186604 | — | — | -0.68 | -110.94 | exit-ema20-confirm-missed-scheduler-replay |
| 2026-07-06T16:00:00Z | OPEN | BTC/USD | long | 0.16899 | 63679.4 | 62724.55 | 67498.80 | — | — | entry-rule-v0.4-momentum |
| 2026-07-07T03:00:00Z | CLOSE | BTC/USD | long | 0.16899 | 63125.0 | — | — | -0.58 | -93.69 | exit-ema20-confirm |
