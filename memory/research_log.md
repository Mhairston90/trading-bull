# BULL Research Log

> **Append-only.** News and external research notes per routine run.
> Rows older than 30 days archived by routine #3 monthly sweep.

## Schema

| Timestamp (UTC) | Routine | Source | Summary | Action taken |
|-----------------|---------|--------|---------|--------------|

## Entries

| 2026-04-21T03:26:55Z | overnight | system | Kraken MCP not available in session (no kraken_* tools registered); routine cannot fetch OHLCV or ticker data | SKIPPED per guardrails Ring 3 MCP-failure rule; will retry next routine |
| 2026-04-21T03:30:00Z | overnight | kraken | HYPE/USD entry scan: 1H close 41.09 below 1H EMA20 41.13; 4H close 41.09 above 4H EMA50 ~43.0 (failing) | REJECT — entry-rule-1 (1H close < EMA20) |
| 2026-04-21T03:30:00Z | overnight | kraken | AVAX/USD entry scan: 1H close 9.31 > EMA20 9.28, RSI14 58.0 > 55, but 4H close 9.31 < 4H EMA50 9.34 | REJECT — entry-rule-3 (4H close < 4H EMA50) |
| 2026-04-21T03:30:00Z | overnight | kraken | SOL/USD entry scan: 1H close 85.50 > EMA20 85.47 (razor-thin), RSI14 ≈ 51.3 < 55 | REJECT — entry-rule-2 (1H RSI14 < 55) |
| 2026-04-21T03:30:00Z | overnight | kraken | TAO/USD entry scan: 4H close 244.78 < 4H EMA50 250.16 | REJECT — entry-rule-3 (4H close < 4H EMA50) |
| 2026-04-21T03:30:00Z | overnight | kraken | XRP/USD entry scan: 1H close 1.4247 < EMA20 1.4251 (razor-thin); 4H close 1.4247 > 4H EMA50 1.4008 | REJECT — entry-rule-1 (1H close < EMA20) |
| 2026-04-21T03:30:00Z | overnight | kraken | BTC,ETH,DOGE,SUI,LTC,ADA,FARTCOIN,LINK,PENGU,TRX all have 24h change ≤ 0 (-0.04% to -1.73%); market regime: Apr 13–17 rally then Apr 18–19 selloff, now flat-to-down consolidation; 1H RSI14 > 55 mathematically implausible under this regime | REJECT (inferred, 10 pairs) — entry-rule-2 (1H RSI14 < 55) — context-budget decision not to compute indicators for each |
| 2026-04-21T03:30:00Z | overnight | system | News scan (CoinDesk / TheBlock via Firecrawl) deferred this run to conserve context budget; no ACTIONABLE items flagged | deferred — morning brief routine runs shortly after |
| 2026-04-21T03:30:00Z | overnight | system | Universe refresh skipped: today is 2026-04-20 (not 1st of month) | no action |
| 2026-04-21T18:05:00Z | overnight | kraken | TRX/USD entry scan (1H close 17:00 = 0.331777): 1H EMA20 ≈ 0.329847 (PASS), 1H RSI14 ≈ 76.4 (PASS), 4H close (12:00 bar) 0.330345 > 4H EMA50 ≈ 0.3264 (PASS). ATR14(1h) ≈ 0.000829. | OPEN long @ 0.331943, stop 0.330285, size 7531 (cash-capped to equity/4 = $2500 notional, risk $12.49 = 0.12%) — entry-rule-v0-momentum |
| 2026-04-21T18:05:00Z | overnight | kraken | LINK/USD entry scan: 1H close 17:00 = 9.35124, 20 recent-bar SMA ≈ 9.363 (EMA20 similar or higher) | REJECT — entry-rule-1 (1H close < 1H EMA20) |
| 2026-04-21T18:05:00Z | overnight | kraken | PENGU/USD entry scan: 1H close 17:00 = 0.007627, 20-bar SMA 0.007660 | REJECT — entry-rule-1 (1H close < 1H EMA20) |
| 2026-04-21T18:05:00Z | overnight | kraken | AVAX/USD entry scan: 1H close 17:00 = 9.33, 20-bar SMA 9.3355 | REJECT — entry-rule-1 (1H close < 1H EMA20, razor-thin) |
| 2026-04-21T18:05:00Z | overnight | kraken | Remaining 10 pairs (BTC -0.42%, ETH -0.55%, SOL -0.12%, XRP -0.03%, TAO -0.5%, HYPE -2.92%, XDG -1.06%, SUI -0.73%, LTC +0.04%, ADA -0.84%, FARTCOIN -0.79%): 24h change ≤ 0 or razor-thin; market regime still mixed. Under negative-drift regime, 1H RSI14>55 is mathematically unlikely. | REJECT (inferred, 11 pairs) — entry-rule-2 (1H RSI14 < 55) — context-budget decision not to re-compute individually |
| 2026-04-21T18:05:00Z | overnight | system | News scan deferred: morning-brief skill runs separately and surfaces actionable headlines. v0 strategy is not news-reactive — no entry gate depends on news this run. | deferred |
| 2026-04-21T18:05:00Z | overnight | system | Universe refresh skipped: today is 2026-04-21 (not 1st of month). Next refresh 2026-05-01. | no action |
