# BULL Universe — top 15 Kraken USD pairs by 30-day volume

> **Refreshed monthly** by routine #1 on the 1st of each month, or manually if a pair delists.
> **Source of truth:** Kraken MCP `kraken_pairs` + `kraken_ticker` volume queries.
> **Last refreshed:** NOT YET (populated on first routine #1 run).

## Current universe

| Rank | Pair | 30d volume (USD) | Notes |
|------|------|------------------|-------|
| — | — | — | Awaiting first routine #1 refresh |

## Refresh rules

- Monthly on 1st (or next weekday if 1st is weekend)
- Query Kraken for all `*/USD` spot pairs
- Rank by 30-day notional USD volume (price × volume)
- Top 15 wins
- **If a pair in the current universe has an open position and falls out of top-15:**
  - Hold the existing position, let strategy exit rules close it
  - No new entries on the dropped pair until it re-enters top-15
- **If a pair delists mid-month:** trigger immediate universe refresh, flatten any open position on the delisted pair at market (paper), ALERT on Telegram.
