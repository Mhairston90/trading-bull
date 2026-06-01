# BULL Universe — top 15 Kraken USD pairs by 30-day volume

> **Refreshed monthly** by routine #1 on the 1st of each month, or manually if a pair delists.
> **Source of truth:** Kraken MCP `kraken_pairs` + `kraken_ohlcv` 30d daily aggregation (sum of vwap × volume across 30 most-recent daily bars).
> **Last refreshed:** 2026-06-01 (routine-01-overnight first-of-month sweep — first true 30d aggregation, replacing the 2026-04-20 standup 24h-proxy snapshot).

## Current universe

| Rank | Pair | Kraken symbol | 30d notional (USD) | Notes |
|------|------|---------------|-------------------:|-------|
| 1 | BTC/USD | XXBTZUSD | ~$3,920M | — |
| 2 | ETH/USD | XETHZUSD | ~$1,100M | — |
| 3 | SOL/USD | SOLUSD | ~$573M | — |
| 4 | HYPE/USD | HYPEUSD | ~$535M | Promoted from rank 6 — late-May parabolic rally (41 → 72) drove volume +5x |
| 5 | XRP/USD | XXRPZUSD | ~$528M | — |
| 6 | SUI/USD | SUIUSD | ~$312M | Promoted from rank 8 — May 10 8-10 mini-runup boosted notional |
| 7 | TAO/USD | TAOUSD | ~$195M | — |
| 8 | DOGE/USD | XDGUSD | ~$180M | Kraken symbol is XDG |
| 9 | NEAR/USD | NEARUSD | ~$177M | **NEW** — replaces PENGU. 5/21-5/29 NEAR rallied 1.30 → 2.77 with 5-9M daily vol |
| 10 | ADA/USD | ADAUSD | ~$106M | — |
| 11 | LINK/USD | LINKUSD | ~$81M | — |
| 12 | LTC/USD | XLTCZUSD | ~$66M | — |
| 13 | FARTCOIN/USD | FARTCOINUSD | ~$48M | Meme — watch for volume decay |
| 14 | TRX/USD | TRXUSD | ~$48M | — |
| 15 | AVAX/USD | AVAXUSD | ~$42M | — |

## Near-miss (watch for next refresh)

- PENGU/USD — ~$38M (dropped this refresh; meme decay 0.011 → 0.0074 over 30d)
- DOT/USD — ~$22M
- UNI/USD — ~$20M

## Diff vs prior universe (2026-04-20 24h-proxy snapshot)

- **Added:** NEAR/USD (rank 9) — fresh entrant on May rally
- **Dropped:** PENGU/USD (was rank 14)
- **Promoted:** HYPE 6→4, SUI 8→6, DOGE 7→8 (relative ordering shifted)
- **Demoted:** ADA 10→10, LINK 13→11, LTC 9→12, FARTCOIN 11→13, TRX 15→14, AVAX 12→15
- All 14 incumbent pairs (ex-PENGU) retained. No open positions on PENGU → no holdover position handling needed.

## Refresh rules

- Monthly on 1st (or next weekday if 1st is weekend)
- Query Kraken for all `*/USD` spot pairs
- Rank by 30-day notional USD volume (sum of vwap × volume across 30 daily bars)
- Top 15 wins
- **If a pair in the current universe has an open position and falls out of top-15:**
  - Hold the existing position, let strategy exit rules close it
  - No new entries on the dropped pair until it re-enters top-15
- **If a pair delists mid-month:** trigger immediate universe refresh, flatten any open position on the delisted pair at market (paper), ALERT on Telegram.
