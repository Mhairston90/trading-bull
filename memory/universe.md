# BULL Universe — top 15 Kraken USD pairs by 30-day volume

> **Refreshed monthly** by routine #1 on the 1st of each month, or manually if a pair delists.
> **Source of truth:** Kraken MCP `kraken_pairs` + `kraken_ticker` volume queries.
> **Last refreshed:** 2026-04-20 (standup — ranked by **24h** notional as a proxy until routine #1 runs a real 30d aggregation).

## Current universe

| Rank | Pair | Kraken symbol | 24h notional (USD) | Notes |
|------|------|---------------|-------------------:|-------|
| 1 | BTC/USD | XXBTZUSD | $130.2M | — |
| 2 | ETH/USD | XETHZUSD | $37.2M | — |
| 3 | SOL/USD | SOLUSD | $30.0M | — |
| 4 | XRP/USD | XXRPZUSD | $18.8M | — |
| 5 | TAO/USD | TAOUSD | $6.80M | — |
| 6 | HYPE/USD | HYPEUSD | $5.86M | — |
| 7 | DOGE/USD | XDGUSD | $5.21M | Kraken symbol is XDG |
| 8 | SUI/USD | SUIUSD | $4.86M | — |
| 9 | LTC/USD | XLTCZUSD | $2.19M | — |
| 10 | ADA/USD | ADAUSD | $1.95M | — |
| 11 | FARTCOIN/USD | FARTCOINUSD | $1.52M | Meme — watch for volume decay |
| 12 | AVAX/USD | AVAXUSD | $1.21M | — |
| 13 | LINK/USD | LINKUSD | $1.17M | — |
| 14 | PENGU/USD | PENGUUSD | $1.07M | Meme — watch for volume decay |
| 15 | TRX/USD | TRXUSD | $1.04M | — |

## Near-miss (watch for next refresh)

- DOT/USD — $0.89M
- NEAR/USD — $0.73M
- UNI/USD — $0.73M

## Refresh rules

- Monthly on 1st (or next weekday if 1st is weekend)
- Query Kraken for all `*/USD` spot pairs
- Rank by 30-day notional USD volume (price × volume)
- Top 15 wins
- **If a pair in the current universe has an open position and falls out of top-15:**
  - Hold the existing position, let strategy exit rules close it
  - No new entries on the dropped pair until it re-enters top-15
- **If a pair delists mid-month:** trigger immediate universe refresh, flatten any open position on the delisted pair at market (paper), ALERT on Telegram.
