# Variant v0.12-sbd-exit — Synthetic Trade Log

> Paper-paper. Same schema as main v0.2/v0.3 trade_log.
>
> **LEADERBOARD-SOURCED — FORWARD PAPER-PAPER ONLY.** The external Strategy
> Leaderboard reads this file (registry `BULL v0.12-SBD (twin)`).
>
> **GAP-RECOVERY BACKFILL (2026-05-29, user-authorized).** Routine #7 (the variant
> simulator) did not run from 2026-05-16 to 2026-05-29 (13-day scheduler gap) and
> its old spec only replayed a trailing 24h with no backfill, so the trades this
> twin would have made after its 2026-05-19 spin-up were never recorded. The user
> directed that trades the twin's rules would have taken on/after spin-up SHOULD
> count. The rows below are those trades, recovered as follows:
>   • ENTRIES — identical to main BULL v0's actual entries on/after 2026-05-19
>     (this variant's entry rules ARE v0.2, unchanged; the SBD change only tightens
>     the exit), so the twin would have entered exactly these.
>   • EXITS — main BULL v0's actual realized exits (20-EMA / stop / 4R). The SBD
>     9-EMA tightening is strictly risk-reducing, so the twin's true result is
>     >= what is shown here (this backfill is conservative).
>   • SIZING — the twin's own $10,000 account at 1.5% risk/trade (independent of
>     main BULL's equity), sized off realized equity at each entry.
> Going forward, routine #7's lookback was hardened to replay since last rebuild,
> so this manual recovery should not be needed again.

| Timestamp (UTC) | Event | Pair | Side | Size | Price | Stop | Target | R at exit | Realized PnL | Reason tag |
|-----------------|-------|------|------|------|-------|------|--------|-----------|--------------|------------|
| 2026-05-20T13:00Z | OPEN | HYPE/USD | long | 75.052537 | 50.01499 | 48.01639 | — | — | — | entry-v0.2-momentum (backfill: routine-07 gap-recovery) |
| 2026-05-21T04:00Z | OPEN | TAO/USD | long | 24.142421 | 277.83675 | 271.62362 | — | — | — | entry-v0.2-momentum (backfill: routine-07 gap-recovery) |
| 2026-05-21T08:00Z | CLOSE | HYPE/USD | long | 75.052537 | 58.38080 | — | — | +4.04 | +606.00 | exit-4R-target (backfill) |
| 2026-05-21T13:00Z | OPEN | HYPE/USD | long | 62.190445 | 57.74886 | 55.19075 | — | — | — | entry-v0.2-momentum (backfill: routine-07 gap-recovery) |
| 2026-05-22T01:00Z | CLOSE | TAO/USD | long | 24.142421 | 276.14136 | — | — | -0.50 | -75.00 | exit-ema20-confirm (backfill) |
| 2026-05-22T02:00Z | CLOSE | HYPE/USD | long | 62.190445 | 57.31133 | — | — | -0.29 | -46.14 | exit-ema20-confirm (backfill) |
| 2026-05-22T04:00Z | OPEN | AVAX/USD | long | 1142.722942 | 9.50475 | 9.36712 | — | — | — | entry-v0.2-momentum (backfill: routine-07 gap-recovery) |
| 2026-05-22T13:00Z | OPEN | SOL/USD | long | 148.727099 | 87.70383 | 86.64637 | — | — | — | entry-v0.2-momentum (backfill: routine-07 gap-recovery) |
| 2026-05-22T15:00Z | CLOSE | SOL/USD | long | 148.727099 | 86.64637 | — | — | -1.43 | -224.90 | exit-stop-hit (backfill) |
| 2026-05-22T16:00Z | CLOSE | AVAX/USD | long | 1142.722942 | 9.42529 | — | — | -0.94 | -147.84 | exit-ema20-confirm (backfill) |
| 2026-05-25T15:00Z | OPEN | BTC/USD | long | 0.272760 | 77678.12000 | 77122.02000 | — | — | — | entry-v0.2-momentum (backfill: routine-07 gap-recovery) |
| 2026-05-25T22:00Z | CLOSE | BTC/USD | long | 0.272760 | 77083.46000 | — | — | -1.07 | -162.30 | exit-stop-hit (backfill) |
| 2026-05-26T12:00Z | OPEN | TAO/USD | long | 14.513854 | 286.40410 | 276.12100 | — | — | — | entry-v0.2-momentum (backfill: routine-07 gap-recovery) |
| 2026-05-26T18:00Z | CLOSE | TAO/USD | long | 14.513854 | 280.40233 | — | — | -0.58 | -86.56 | exit-ema20-confirm (backfill) |
