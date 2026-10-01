# BULL Trade Log

> **Append-only. Source of truth.** `portfolio.md` is rebuilt from this file each wake.
> Each entry = one trade event (open or close).
> Rows older than 30 days are moved to `memory/archive/YYYY-MM.md` by routine #3 on the last trading day of the month.
> **Last monthly archive:** 2026-10-01 (routine-03-eod catch-up sweep) — moved 29 June+July-dated rows to `memory/archive/2026-10.md` (Jul/Aug/Sep EOD archive cycles missed due to scheduler outage 07-10 → 09-20 and the Sep 30 EOD missed-fire).

## Schema

| Timestamp (UTC) | Event | Pair | Side | Size | Price | Stop | Target | R at exit | Realized PnL | Reason tag |
|-----------------|-------|------|------|------|-------|------|--------|-----------|--------------|------------|

## Entries

| 2026-09-23T13:00:00Z | OPEN | NEAR/USD | long | 577.6 | 4.72836 | 4.45616 | 5.81716 | — | — | entry-rule-v0.4-momentum-rule8-winner |
| 2026-09-23T14:00:00Z | CLOSE | NEAR/USD | long | 577.6 | 4.45393 | — | — | -1.01 | -172.30 | exit-stop-hit-intrabar |
| 2026-09-26T04:00:00Z | OPEN | ADA/USD | long | 19263 | 0.256346 | 0.248318 | 0.288458 | — | — | entry-rule-v0.4-momentum-rule8-winner |
| 2026-09-26T06:00:00Z | CLOSE | ADA/USD | long | 19263 | 0.254014 | — | — | -0.29 | -44.92 | exit-ema20-2bar-recovery-missed-scheduler-replay (05:00Z close 0.254976 < EMA20 0.255259 and 06:00Z close 0.254014 < EMA20 0.255140, both below by ≥$0.00028 on converged 1H EMA20; routine-02-midday did not run Sat off-schedule so exit was recovered at routine-01-overnight replay) |
| 2026-09-26T12:00:00Z | OPEN | SOL/USD | long | 75.09 | 121.07 | 119.0198 | 129.2708 | — | — | entry-rule-v0.4-momentum-rule8-winner |
| 2026-09-27T15:00:00Z | CLOSE | SOL/USD | long | 75.09 | 121.6894 | — | — | -0.01 | -0.88 | exit-ema20-confirm-missed-scheduler-replay (14:00Z close 121.68 and 15:00Z close 121.75 both below converged 1H EMA20 ~122.20 / ~122.16 — W22-G two-bar confirmation; retroactive replay — Sun 09-27 routines 02-midday and 03-eod did not fire off-schedule so exit was recovered at routine-03-eod off-schedule Sun replay 21:12 PT / 04:13Z 09-28; gross +$46.51 / +0.30R flipped to net −$0.88 / −0.01R by 0.05% slippage + 0.26% round-trip commission $47.39) |
| 2026-09-30T13:00:00Z | OPEN | SOL/USD | long | 66.4462 | 121.9209 | 119.6039 | 131.1889 | — | — | entry-rule-v0.4-momentum-rule8-cashfit (rank-3 pick after BTC/ETH skipped cash-fit — BTC notional $13,498 > $10,264 cash, ETH notional $11,851 > $10,264 cash; SOL notional $8,101 fits. Full-pass tech per indicators.py 13:13Z: R1 +$2.57, R2 RSI 65.8, R2a OK, R3 +$1.69, R4a $65.1M. Regime 5a PASS 8/15 +0.44% median. Cluster 0→1/2. 5b cleared (SOL 09-27T15Z stop-out was 70h ago > 24h). Fill = 121.86 × 1.0005 slippage = 121.9209; stop 121.9209 − 2×ATR(1.1585) = 119.6039; target 4R = 131.1889; size = 153.9558 / 2.317 = 66.4462) |
| 2026-09-30T14:00:00Z | CLOSE | SOL/USD | long | 66.4462 | 119.6039 | — | — | -1.00 | -195.68 | exit-stop-hit-intrabar (14:00Z 1H bar low $118.41 pierced 2×ATR stop $119.6039; routine-02-midday closes at stop price per routine spec. Gross PnL = (119.6039 − 121.9209) × 66.4462 = −$153.96; commissions open $21.06 + close $20.66 = $41.72; net −$195.68. Held 1h. SOL live bid at midday-scan 20:00Z = $117.51 (well below stop), confirming price rejected the entry-bar breakout. Trade was rank-3 cash-fit pick when BTC/ETH would not fit; single-bar failure suggests entry-bar $122.79 high was the local top before −4.10% reversal within same 15:00Z bar.) |
| 2026-10-01T07:00:00Z | OPEN | ADA/USD | long | 22838 | 0.253472 | 0.246859 | 0.279923 | — | — | entry-rule-v0.4-momentum-rule8-cashfit (rank-6 pick after BTC/ETH skipped cash-fit — BTC notional $15,310 > $10,068 cash, ETH notional $13,481 > $10,068 cash; SOL rank-3 fail R2 RSI 53.0; HYPE rank-4 fail R3; XRP rank-5 fail R2+R3; ADA rank-6 fits. Full-pass tech per indicators.py 07:13Z: R1 +$0.004783, R2 RSI 62.4, R2a OK, R3 +$0.005598, R4a $6.92M. Regime 5a PASS 14/15 +1.30% median (strongest in weeks). Cluster 0→0/2 (ADA not in BTC-cluster). 5b cleared (ADA 09-26T06Z stop-out was 121h ago > 24h). Fill = 0.253345 × 1.0005 slippage = 0.253472; stop 0.253472 − 2×ATR(0.0033063) = 0.246859; target 4R = 0.279923; size = 151.0206 / 0.0066126 = 22,838 ADA. EOD-fire delayed ~3h13m: Wed 09-30 21:00 PT cron fired at Thu 10-01 00:13 PT / 07:13Z. Candle 07:00Z is just-closed bar for this fire.) |
