# BULL Universe — top 15 Kraken USD pairs by 30-day volume

> **Refreshed monthly** by routine #1 on the 1st of each month, or manually if a pair delists.
> **Source of truth:** Kraken public REST OHLC (1440-min bars) — 30-day sum of vwap × volume, 30 most-recent daily bars per pair.
> **Last refreshed:** 2026-07-01 (routine-01-overnight first-of-month sweep — second true 30d aggregation).

## Current universe

| Rank | Pair | Kraken symbol | 30d notional (USD) | Notes |
|------|------|---------------|-------------------:|-------|
| 1 | BTC/USD | XXBTZUSD | ~$5,120M | — |
| 2 | ETH/USD | XETHZUSD | ~$1,435M | — |
| 3 | SOL/USD | SOLUSD | ~$795M | — |
| 4 | HYPE/USD | HYPEUSD | ~$726M | — |
| 5 | XRP/USD | XXRPZUSD | ~$711M | — |
| 6 | ADA/USD | ADAUSD | ~$249M | ▲ from rank 10 — late-June rally + volume expansion |
| 7 | NEAR/USD | NEARUSD | ~$210M | ▲ from rank 9 — continued volume growth |
| 8 | SUI/USD | SUIUSD | ~$180M | ▼ from rank 6 — cooling after May run-up |
| 9 | TAO/USD | TAOUSD | ~$158M | ▼ from rank 7 |
| 10 | DOGE/USD | XDGUSD | ~$157M | ▼ from rank 8. Kraken symbol is XDG |
| 11 | LTC/USD | XLTCZUSD | ~$75M | ▲ from rank 12 |
| 12 | AVAX/USD | AVAXUSD | ~$70M | ▲ from rank 15 |
| 13 | LINK/USD | LINKUSD | ~$68M | ▼ from rank 11 |
| 14 | ONDO/USD | ONDOUSD | ~$51M | **NEW** — replaces FARTCOIN. Sustained June volume $1-2M/day |
| 15 | TRX/USD | TRXUSD | ~$46M | ▼ from rank 14 |

## Near-miss (watch for next refresh)

- TON/USD — ~$38M
- UNI/USD — ~$33M
- FARTCOIN/USD — ~$27M (dropped this refresh; meme volume decayed vs May peak)
- DOT/USD — ~$21M
- PENGU/USD — ~$20M (still on decay trajectory)

## Diff vs prior universe (2026-06-01 refresh)

- **Added:** ONDO/USD (rank 14) — first appearance; consistent $1-2M/day notional
- **Dropped:** FARTCOIN/USD (was rank 13) — meme volume decay, now $27M near-miss watch
- **Promoted:** ADA 10→6, NEAR 9→7, LTC 12→11, AVAX 15→12
- **Demoted:** SUI 6→8, TAO 7→9, XDG 8→10, LINK 11→13, TRX 14→15
- **Unchanged:** BTC 1, ETH 2, SOL 3, HYPE 4, XRP 5
- No open positions on FARTCOIN → no holdover position handling needed.
- 14 of 15 pairs retained (only FARTCOIN churned).

## Refresh rules

- Monthly on 1st (or next weekday if 1st is weekend)
- Query Kraken for all `*/USD` spot pairs (this refresh: 26-pair candidate slate covering incumbent 15 + near-miss watchlist + momentum names ONDO/TON/APT/WIF/POPCAT/JUP/TIA/SEI)
- Rank by 30-day notional USD volume (sum of vwap × volume across 30 daily bars)
- Top 15 wins
- **If a pair in the current universe has an open position and falls out of top-15:**
  - Hold the existing position, let strategy exit rules close it
  - No new entries on the dropped pair until it re-enters top-15
- **If a pair delists mid-month:** trigger immediate universe refresh, flatten any open position on the delisted pair at market (paper), ALERT on Telegram.
