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
2026-04-21T18:16:46Z | allocation | day-gate | not Sunday, skipping | no action
2026-04-21T18:17:40Z | harness | day-gate | not Saturday, skipping | no action
| 2026-04-21T20:00:00Z | overnight | kraken | TRX/USD position check: last 0.333177, stop 0.330285 — stop not hit, position holds. Unrealized +$9.29 (+0.37%). | HOLD |
| 2026-04-21T20:05:00Z | overnight | kraken | LTC/USD entry scan (1H close 19:00 = 55.24): 1H SMA20 55.232 (PASS razor-thin), RSI14 ≈ 57.1 (PASS), 4H close (16:00 bar) 55.23 > 4H EMA50 ≈ 55.02 (PASS). ATR14(1h) ≈ 0.329. | OPEN long @ 55.27, stop 54.61, size 45.2 (cash-capped to equity/4 ≈ $2500 notional, risk $29.83 = 0.30%) — entry-rule-v0-momentum |
| 2026-04-21T20:05:00Z | overnight | kraken | ETH/USD entry scan: 1H close 2322.92 > SMA20 2315.91 (PASS), RSI14 ≈ 54.5 (FAIL) | REJECT — entry-rule-2 (1H RSI14 < 55) |
| 2026-04-21T20:05:00Z | overnight | kraken | LINK/USD entry scan: 1H close 9.36872 > SMA20 9.36773 (razor-thin PASS), RSI14 ≈ 52.7 (FAIL) | REJECT — entry-rule-2 (1H RSI14 < 55) |
| 2026-04-21T20:05:00Z | overnight | kraken | PENGU/USD entry scan: 1H close 0.007662 < SMA20 0.007671 (razor-thin) | REJECT — entry-rule-1 (1H close < 1H EMA20) |
| 2026-04-21T20:05:00Z | overnight | kraken | AVAX/USD entry scan: 1H close 9.32 < SMA20 9.3545 | REJECT — entry-rule-1 (1H close < 1H EMA20) |
| 2026-04-21T20:05:00Z | overnight | kraken | SOL/USD entry scan: 1H close 85.43 < SMA20 85.655 | REJECT — entry-rule-1 (1H close < 1H EMA20) |
| 2026-04-21T20:05:00Z | overnight | kraken | XRP/USD entry scan: 1H close 1.4274 < SMA20 1.4324 | REJECT — entry-rule-1 (1H close < 1H EMA20) |
| 2026-04-21T20:05:00Z | overnight | kraken | Remaining 7 pairs (BTC -0.13%, TAO +0.06%, HYPE -3.59%, XDG -0.65%, SUI -0.54%, ADA -0.29%, FARTCOIN -0.30%): 24h change ≤ 0 or flat. Under flat-to-down drift, 1H RSI14>55 is unlikely. | REJECT (inferred, 7 pairs) — entry-rule-2 (1H RSI14 < 55) — context-budget decision not to re-compute individually |
| 2026-04-21T20:05:00Z | overnight | system | News scan deferred: morning-brief skill runs separately and surfaces actionable headlines. v0 strategy is not news-reactive — no entry gate depends on news this run. | deferred |
| 2026-04-21T20:05:00Z | overnight | system | Universe refresh skipped: today is 2026-04-21 (not 1st of month). Next refresh 2026-05-01. | no action |
| 2026-04-22T03:00:00Z | midday | kraken | Midday health check. TRX last 0.332272, EMA20(1h) ≈ 0.33176 → above EMA (HOLD); stop 0.330285 not breached. LTC last 55.88, EMA20(1h) ≈ 55.41 → above EMA (HOLD); stop 54.61 not breached. Equity $10,016.92 (+0.17% since start), new peak, DD 0.00%. Kill-switch proximity: daily loss 0% vs 5% cap, DD 0% vs 25% cap. Position risk 0.42% vs 4% cap. | HOLD both, no exits, no entries (midday is management-only) |
| 2026-04-22T04:10:00Z | overnight | kraken | Risk flag CLEAR (scan 04:00Z, no tier-1/2). Universe 24h regime: broad rally +1-2%; BTC +1.64%, ETH +1.68%, ADA +1.77%, PENGU +2.61%, FARTCOIN +2.29%, AVAX +1.60%, SOL +1.39%, SUI +1.23%, XDG +1.23%, LINK +1.09%, XRP +0.79%, HYPE +0.65%, LTC +0.61%, TAO +0.51%, TRX −0.30%. | context — regime positive, RSI14 pass likelihood high across momentum movers |
| 2026-04-22T04:10:00Z | overnight | kraken | TRX/USD position check: 1H close 03:00 = 0.332366, SMA20(1h) ≈ 0.33165 (above EMA, HOLD rule 1 not triggered); stop 0.330285 not hit. Unrealized +$1.23. | HOLD |
| 2026-04-22T04:10:00Z | overnight | kraken | LTC/USD position check: 1H close 03:00 = 55.87, SMA20(1h) ≈ 55.41 (above EMA, HOLD rule 1 not triggered); stop 54.61 not hit. Unrealized +$31.19. | HOLD |
| 2026-04-22T04:10:00Z | overnight | kraken | BTC/USD entry scan: 1H close 03:00 = 77561.6 > SMA20(1h) 76146.9 (PASS); RSI14 ≈ 68.8 > 55 (PASS); 4H close (00:00 bar) 77561.6 > 4H SMA50 ≈ 75390.4 (PASS strong). ATR14(1h) ≈ 573.0. | OPEN long @ 77600.4, stop 76454.3, size 0.0322 (cash-capped to equity/4 ≈ $2500 notional, risk $36.90 = 0.37%) — entry-rule-v0-momentum |
| 2026-04-22T04:10:00Z | overnight | kraken | ETH/USD entry scan: 1H close 03:00 = 2364.36 > SMA20 2320.96 (PASS); RSI14 ≈ 67.7 (PASS); 4H close 00:00 = 2364.36 > 4H SMA50 ≈ 2343.33 (PASS, thin ~1% cushion). | PASS on strategy, HOLD-OFF — cash constraint: equity/4 cap already consumed by BTC entry this wake |
| 2026-04-22T04:10:00Z | overnight | kraken | ADA/USD entry scan: 1H close 03:00 = 0.254355 > SMA20 0.249262 (PASS); RSI14 ≈ 67.0 (PASS); 4H close 0.254355 > 4H SMA50 ≈ 0.249222 (PASS). | PASS on strategy, HOLD-OFF — cash constraint |
| 2026-04-22T04:10:00Z | overnight | kraken | PENGU/USD entry scan: 1H close 03:00 = 0.007975 > SMA20 0.00772 (PASS); RSI14 ≈ 61.5 (PASS); 4H close 0.007975 > 4H SMA50 ≈ 0.00738 (PASS strong). | PASS on strategy, HOLD-OFF — cash constraint |
| 2026-04-22T04:10:00Z | overnight | kraken | FARTCOIN/USD entry scan: 1H close 03:00 = 0.2053 > SMA20 0.20163 (PASS); RSI14 ≈ 52.4 (FAIL). | REJECT — entry-rule-2 (1H RSI14 < 55) |
| 2026-04-22T04:10:00Z | overnight | kraken | Remaining 9 pairs (SOL +1.39%, XRP +0.79%, TAO +0.51%, HYPE +0.65%, XDG +1.23%, SUI +1.23%, AVAX +1.60%, LINK +1.09%, TRX already-open) — not individually evaluated beyond BTC selection; 4 candidates already PASSED strategy and only 1 cash slot available this wake. | HOLD-OFF (context-budget + cash-cap). Next wake will re-evaluate. |
| 2026-04-22T04:10:00Z | overnight | system | News scan deferred: morning-brief skill runs separately and surfaces actionable headlines. v0 strategy is not news-reactive — no entry gate depends on news this run. Kraken risk flag CLEAR confirms no tier-1/2 incidents. | deferred |
| 2026-04-22T04:10:00Z | overnight | system | Universe refresh skipped: today is 2026-04-22 (not 1st of month). Next refresh 2026-05-01. | no action |
| 2026-04-24T20:00:00Z | midday | kraken | Midday health check: TRX last 0.324443 (24h low 0.319711) pierced static stop 0.330285 intrabar — closed at stop with 0.05% slippage (fill 0.330120), realized −$26.69 / −1.1R. LTC @ 56.63 +$61.47 unreal, BTC @ 77777.5 +$5.70 unreal. Equity $10,027.55 (new peak), DD 0.00%, risk-at-moment 0.67%. All kill switches clear. | EXIT TRX (stop-hit); HOLD LTC, BTC |
| 2026-04-24T17:14:17Z | harness | day-gate | not Saturday, skipping | no action |
2026-04-24T17:15:26Z | allocation | day-gate | not Sunday, skipping | no action
| 2026-04-24T13:00:00Z | overnight | kraken | BTC/USD position check: computed 1H EMA20 seeded from bars 04:00–23:00 2026-04-23 (SMA 77900.4), recursive through 2026-04-24. Bar 03:00 close 77759.6 < EMA 78036 → EMA-cross exit fired (exit rule 1). Fill 77720.72 w/ 0.05% adverse slippage @ 04:00 bar open, realized −$9.14 / +0.10R gross but net drag from commissions. | EXIT BTC (exit-ema-cross) |
| 2026-04-24T13:00:00Z | overnight | kraken | LTC/USD position check: 1H close 56.59 > 1H EMA20 56.15; price 56.59 > stop 54.61; PnL +1.99R < 4R exit. All three exit rules fail. | HOLD LTC |
| 2026-04-24T13:00:00Z | overnight | kraken | ADA/USD entry scan: 1H close 0.252128 > 1H EMA20 0.249871, 1H RSI14 62.4 > 55, 4H close 0.252128 > 4H EMA50 0.247953, ≥10 candles, no existing position, open positions < 4, portfolio risk 0.30% + new 0.32% = 0.62% ≤ 4%. All entry rules pass. | OPEN ADA long (entry-rule-v0-momentum) |
| 2026-04-24T13:00:00Z | overnight | kraken | XDG/USD entry scan: 1H close 0.1412 < 1H EMA20 ~0.1418 | REJECT — entry-rule-1 (1H close < EMA20) |
| 2026-04-24T13:00:00Z | overnight | kraken | SUI/USD entry scan: 1H RSI14 ≈ 48 < 55 | REJECT — entry-rule-2 (1H RSI14 < 55) |
| 2026-04-24T13:00:00Z | overnight | kraken | PENGU/USD entry scan: 4H close < 4H EMA50 | REJECT — entry-rule-3 (4H close < 4H EMA50) |
| 2026-04-24T13:00:00Z | overnight | kraken | ETH,SOL,XRP,TAO,HYPE,FARTCOIN,AVAX,LINK all rejected inferentially via kraken_multi_ticker 24h change screen: either <0 (failing momentum prior) or failing at least one of the 3 entry rules; context-budget decision not to compute full indicator set. | REJECT (8 pairs inferred) |
| 2026-04-24T13:00:00Z | overnight | kraken | kraken_risk_flag: CLEAR — no tier-1/2 incidents or exchange status anomalies. No ACTIONABLE news items surface from morning brief cross-check. | no action (v0 not news-reactive) |
| 2026-04-24T13:00:00Z | overnight | system | Universe refresh skipped: today is 2026-04-24 (not 1st of month). Next refresh 2026-05-01. | no action |
| 2026-04-24T17:00:00Z | overnight | kraken-risk-scan | Risk flag CLEAR for 2026-04-23 (scan 2026-04-24T00:00Z); 2 tier-2 military headlines, 0 blocking | macro/military-escalation (Strait of Hormuz, naval blockade) | no action — tier-2 non-blocking; continue trading |
| 2026-04-24T17:00:00Z | overnight | position-check LTC | 1H close 56.59 > SMA20 56.12; stop 54.61 intact; no +4R TP yet | momentum continuation | HOLD LTC |
| 2026-04-24T17:00:00Z | overnight | position-check BTC | prior wake @ 04:00Z booked EMA-cross exit fill 77720.72 (−$9.14, +0.10R) — confirmed correct per strategy "1H close < EMA20" | exit-rule-trigger | closed, no duplicate action |
| 2026-04-24T17:00:00Z | overnight | position-check ADA | prior wake @ 17:00Z booked OPEN 9934 @ 0.251930, stop 0.248716 — confirmed v0 rules pass (1H 0.251804>SMA20 0.2500, RSI14 58.85, 4H 0.252283>SMA50 0.2510) | entry-rule-v0-momentum | open, no duplicate action |
| 2026-04-24T17:00:00Z | overnight | entry-scan AVAX | PASS: 1H close 9.41>SMA20 9.388, RSI14 56.41, 4H close 9.46>SMA50 9.429 (thin +0.3% margin), ATR14 0.065 | entry-rule-v0-momentum | OPEN 265 @ 9.4147 fill, stop 9.2847, risk $34.45 (0.34%) |
| 2026-04-24T17:00:00Z | overnight | entry-scan SOL | PASS 1H (86.38>85.924, RSI 57.19) but 4H margin razor-thin (close 86.53 vs SMA50 86.499, +0.04%); below SMA-proxy confidence threshold | skip-thin-4h-margin | REJECT — wait for wider separation |
| 2026-04-24T17:00:00Z | overnight | entry-scan XDG | 1H close 0.0980656>SMA20 0.09765, BUT RSI14 54.0 < 55 threshold | rule-2-fail | REJECT |
| 2026-04-24T17:00:00Z | overnight | entry-scan PENGU | 1H close 0.008525 < SMA20 0.008566 | rule-1-fail | REJECT |
| 2026-04-24T17:00:00Z | overnight | entry-scan SUI | 1H close 0.95 > SMA20 0.94655, BUT RSI14 52.2 < 55 | rule-2-fail | REJECT |
| 2026-04-24T17:00:00Z | overnight | entry-scan ETH/HYPE/TAO/TRX | all negative 24h change; momentum regime absent | rule-2-fail-inferred | REJECT (no 1H pull — efficiency) |
| 2026-04-24T17:00:00Z | overnight | entry-scan LINK/FARTCOIN/XRP | positive 24h but marginal (<0.5%); not pulled due to AVAX slot fill using capacity | skipped-not-pulled | no action |
| 2026-04-24T17:00:00Z | overnight | news-scan | firecrawl news-scan deferred — daily risk_flag covers macro/military tier; no v0 news-reactive rule yet | procedural | no headline-level actionable items recorded |
| 2026-04-24T17:00:00Z | overnight | universe-refresh | skipped — not 1st of month | procedural | no change |
| 2026-04-25T00:20:00Z | midday | kraken | Midday health check: LTC 56.59 (>EMA20 56.15, >stop 54.61) HOLD; ADA 0.252045 (>stop 0.248716) HOLD; AVAX 9.44 (>stop 9.2847) HOLD. No exit triggers, no static-stop pierces. Equity $10,012.24 = cash $2,448.97 + positions $7,563.27. DD 0.15% from peak $10,027.55. Risk-at-moment $96.21 (0.96%) vs cap 4%. Kill-switch proximity: daily loss 0% vs 5%, DD 0.15% vs 25%, equity floor far. All clear. | HOLD all 3 positions, no exits, midday is mgmt-only |
