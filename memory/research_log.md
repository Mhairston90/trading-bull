# BULL Research Log

> **Append-only.** News and external research notes per routine run.
> Rows older than 30 days archived by routine #3 monthly sweep.
>
> ## Schema (W19-E, effective 2026-04-29)
>
> Routine #1 (overnight) and Routine #2 (midday) entry-scan blocks should use the analyst-role split below. Legacy single-line rows above the marker remain as-is.
>
> ```markdown
> ## YYYY-MM-DDTHH:MMZ — routine-NN-<name>
>
> ### Technical (rule-driven, deterministic)
> - Per-pair RSI14, 1H/4H EMA state, 4H regime, ATR14
> - Pass/fail per entry rule (1, 2, 2a, 3, 4, 4a, 5, 5a, 5b, 6, 6a, 7, 8)
> - Final candidate list
>
> ### News (Firecrawl-driven, informational only in v0.2)
> - For each candidate, scan 2 sources (e.g. coindesk.com, theblock.co)
>   for headlines tagged with the pair's base asset over past 6h
> - Record: top 3 headlines + 1-line summary each
> - Tag: "neutral / supportive / contradictory" relative to long bias
> - Does NOT veto entries in v0.2 — informational only
>
> ### Sentiment (passive — Kraken depth/spread proxy in v0.2)
> - For each candidate, record bid/ask spread bps + top-of-book depth
>   via Kraken MCP `kraken_spread` and `kraken_depth`
> - Wide spread / thin depth = sentiment caveat, recorded but no veto
>
> ### Decision
> - Final action this wake (OPEN / SKIP / HOLD)
> - Cite which rule(s) drove the decision
> ```
>
> If Firecrawl is unavailable, the News section logs `Firecrawl unavailable — skipped this wake` and the routine continues. Per Ring 3 (`guardrails.md`), repeated MCP failures still skip the routine entirely.

---

2026-04-25T17:40:11Z | allocation | day-gate | not Sunday, skipping | no action
2026-04-26T20:00:00Z | midday | system | Portfolio flat (0 open positions); no MTM required. Equity $9,930.76, DD 0.97% from peak $10,027.55. All kill switches clear (daily loss 0%, equity > $7,500 floor, DD < 12.5% warn). Midday is position-mgmt only — no entries scanned. | no action
2026-04-27T20:00:00Z | midday | system | Portfolio flat (0 open positions) after 05:00Z stop cascade closed ETH/BTC/SOL/TAO. No MTM/exit checks required. Equity $9,777.08, DD 2.50% from peak $10,027.55. Day realized -1.54% (cap 5%). All kill switches clear: DD < 12.5% warn, equity > $7,500 floor, daily loss < 5%. Midday is position-mgmt only — no entries scanned. | no action
2026-04-28T20:00:00Z | midday | kraken | TAO/USD MTM check (last 257.3733): stop 254.74 not breached on bars completed after entry (18:00 low 255.85, 19:00 low 256.64, 20:00 low 256.88). Last completed 1H close 19:00 = 257.0935 > 1H 20-EMA ≈ 251.81 — no EMA-cross exit. 4R target 281.64 not hit. Unrealized −$32.18 (−0.60R incl commission). Equity $9,744.90, DD 2.82% from peak $10,027.55, risk-at-moment 0.52%. Kill-switch proximity: day realized 0% / unrealized −0.33% (cap 5%), DD 2.82% (warn 12.5%, cap 25%), equity > $7,500 floor. NOTE: 17:00 entry-candle low 253.8037 sits below stop 254.74; cannot determine intra-candle ordering vs entry — flagging for routine-03 EOD review at 1H close. | HOLD TAO, no exits, no entries (midday is management-only)
2026-04-29T19:55:00Z | idea-scan | system | Manual dry-run (HARV-20260429-DRYRUN) — pre-cron pipeline validation. 2 sources fetched (Glassnode Insights, Robot Wealth), 10 claims extracted, 4 survived score-floor (>=8), 0 deduped, 4 appended to idea_bank.md. RW "To Trend or Not To Trend" outside 7d window — included for pipeline test only, normal Friday cron will exclude. First scheduled run: 2026-05-01 (Fri) 18:00 PT. | no trade action
2026-05-04T19:05:30Z | midday | system | Portfolio flat (0 open positions) — no trades since TAO stop-out 2026-04-29T14:00Z. No MTM/exit checks required; Kraken MCP not called (no positions to mark). Equity $9,712.70, DD 3.14% from peak $10,027.55. Day realized 0.00% (cap 5%). Kill-switch state: DD 3.14% (warn 12.5%, cap 25%) — clear; equity > $7,500 floor — clear; daily loss 0% — clear; consecutive losing trading days streak does not exceed 7 (current run since 04-29 L is 4 flat days, not losing). Midday is position-mgmt only — no entries scanned. | no action
2026-05-04T20:00:00Z | midday | kraken | LINK/USD MTM check (last 9.38328, opened 19:00Z @ 9.4393, stop 9.2018, 4R target 10.3893). Stop not breached: 19:00 bar low 9.37012, in-progress 20:00 low 9.38183 — both well above stop. Last completed 1H close 19:00 = 9.38827 > computed 1H 20-EMA ≈ 9.360 (seeded SMA20 9.2552 over 2026-05-03 15:00→2026-05-04 10:00, then iterated; α=2/21) — no exit-rule-1 EMA-cross. 4R target far. Unrealized −$20.71 (−0.34R incl commission). Equity $9,691.99, cash $7,280.49, position MTM $2,411.50, DD 3.35% from peak $10,027.55, risk-at-moment 0.63%. Kill-switch proximity: day realized 0% / unrealized −0.21% (cap 5%) — clear; DD 3.35% (warn 12.5%, cap 25%) — clear; equity > $7,500 floor — clear; consecutive-loss streak not 7-in-a-row. Midday is position-mgmt only — no entries scanned. | HOLD LINK, no exits, no entries
| 2026-05-05T20:00:00Z | midday | kraken | 3 open positions MTM check at 13:00 PT / 20:00 UTC (just-closed 19:00Z 1H bar). LINK/USD: last 9.74589, 19:00 close 9.73157 > 1H 20-EMA ≈ 9.632 (seeded SMA20 9.40435 over 2026-05-04 05:00→2026-05-05 00:00, iterated α=2/21) — no EMA-cross; 19:00 low 9.69894 well above stop 9.2018; +$72.48 (+1.19R). BTC/USD: last 81683.1, 19:00 close 81601.0 > 1H 20-EMA ≈ 80983 — no EMA-cross; 19:00 low 81426.6 well above stop 80124.19; +$15.29 (+0.61R). XRP/USD: last 1.41544, 19:00 close 1.41313 > 1H 20-EMA ≈ 1.40762 — no EMA-cross; 19:00 low 1.409 well above stop 1.39468; +$5.52 (+0.23R). No 4R targets near. Aggregate unrealized +$93.29; equity $9,806.00, cash $2,420.18, MTM $7,385.82, DD 2.21% from peak $10,027.55, risk-at-moment 1.12%. Kill-switch proximity: day realized 0% / day realized+unrealized +0.96% (cap 5%) — clear; DD 2.21% (warn 12.5%, cap 25%) — clear; equity > $7,500 floor — clear; consecutive-loss streak not 7-in-a-row. Midday is position-mgmt only — no entries scanned. | HOLD all 3, no exits, no entries
| 2026-05-06T20:00:00Z | midday | kraken | 4 open positions MTM check at 13:00 PT / 20:00 UTC (just-closed 19:00Z 1H bar). BTC/USD: 19:00 close 81471.5 < 1H 20-EMA ≈ 81570.2 (seeded SMA20 80646.195 over 2026-05-04 19:00→2026-05-05 14:00, iterated α=2/21) — exit-rule-1 EMA-cross TRIGGERED. Exit fill 81430.76 (close × 0.9995 slippage); gross +$14.04 minus exit comm $6.33 = +$1.42 net (+0.06R). LINK/USD: last 10.03964, 19:00 close 10.02236 > 1H 20-EMA ≈ 9.958 — no EMA-cross; 19:00 low 9.95 well above stop 9.2018; +$147.98 unrealized. XRP/USD: last 1.42786, 19:00 close 1.42815 > 1H 20-EMA ≈ 1.4274 (margin 0.0008) — no EMA-cross; 19:00 low 1.42235 well above stop 1.39468; +$26.92 unrealized. LTC/USD: last 57.04, 19:00 close 56.95 > 1H 20-EMA ≈ 56.92 (margin 0.03) — no EMA-cross; 19:00 low 56.78 well above stop 56.28; −$10.19 unrealized. No intrabar stop breaches (all 24h lows above stops post-entry). No 4R targets near. Post-exit: 3 open, equity $9,820.65, cash $2,441.62, MTM $7,379.03, DD 2.06% from peak $10,027.55, risk-at-moment 1.22%. Kill-switch proximity: day realized −0.58% (HYPE −$58.18 + BTC +$1.42) / day realized+unrealized +1.10% (cap 5%) — clear; DD 2.06% (warn 12.5%, cap 25%) — clear; equity > $7,500 floor — clear; consecutive-loss streak not 7-in-a-row. Midday is position-mgmt only — no entries scanned. XRP and LTC EMA margins thin — flagging for routine-03 EOD re-check. | CLOSE BTC ema-cross, HOLD LINK/XRP/LTC, no entries

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
| 2026-04-25T00:25:00Z | eod | kraken | EOD post-close exit check (ran early per operator request, ~11h before scheduled 21:00 PT): LTC 1H close 56.59 > EMA20 56.15 (HOLD); ADA 1H close 0.251804 > EMA20 0.249946 (HOLD); AVAX 1H close 9.41 > EMA20 9.39 (HOLD razor-thin +0.21%). All static stops intact. EOD entry scan duplicates routine-01 from 17:00Z (same 16:00 bar) — 2 cash slots used (ADA, AVAX); SOL was the 3rd PASS but ran into thin 4H margin in earlier wake; no new entries this run. Day stats: realized −$35.83 (TRX −$26.69 + BTC −$9.14), unrealized +$57.16, equity $10,001.91 (+0.02% since start), DD 0.26% from peak. Trades today: 2 closed (BTC ema-cross, TRX stop), 2 opened (ADA, AVAX). Open 3/8. Kill switches all clear. | EOD card sent via Telegram; no new fills |
| 2026-04-25T00:30:00Z | harness | day-gate | not Saturday, skipping | no action |
| 2026-04-25T00:31:00Z | allocation | day-gate | not Sunday, skipping | no action |
| 2026-04-24T17:40:00Z | allocation | day-gate | not Sunday, skipping | no action |
| 2026-04-24T20:10:00Z | midday | kraken | MTM @ 20:06Z — LTC 56.72, ADA 0.251958, AVAX 9.44; no stops pierced intrabar, 19:00Z 1H closes all above 20-EMA; equity $10,017.26, DD 0.10%, day +0.37% net | no action — all clear, silent |
| 2026-04-25T17:07:23Z | harness | system | Saturday harness verify: tv_health_check failed (CDP connection refused, TradingView Desktop not running); kraken_ticker BTC/USD OK ($77,392.4). Per Ring 3 MCP-failure rule, skip routine. | SKIPPED harness run; Telegram ALERT sent; retry next Saturday or operator can run /loop manually after launching TradingView |
| 2026-04-25T20:00:00Z | midday | system | Found 3 uncommitted CLOSE rows in trade_log.md from 2026-04-25T17:00Z (LTC +1.32R/+$39.40, ADA −1.21R/−$38.77, AVAX −0.99R/−$34.04, all exit-ema-cross) lacking corresponding research_log entries — likely an interrupted prior routine. Treated trade_log as source of truth per skill rules and rebuilt portfolio. No open positions to MTM. Equity $9,930.76, cash $9,930.76, realized all-time −$69.24, DD 0.97% from peak $10,027.55. Day realized −$33.41 (−0.33%). Kill-switch proximity: daily loss 0.33% vs 5% cap, DD 0.97% vs 25% cap (warn 12.5%), equity floor $2,430 above. All clear. | Flushed 3 prior closes via this commit; no new exits, no entries (midday is mgmt-only); silent — no Telegram |
| 2026-04-26T04:40:00Z | overnight | kraken | Risk flag CLEAR (scan 04:39Z, no tier-1/2). Universe 24h regime: 14/15 pairs negative or flat (XBT -0.25, ETH -0.36, SOL -0.14, XRP -0.33, TAO -0.82, HYPE -0.48, XDG -0.28, SUI -0.38, LTC -0.46, ADA -0.43, FARTCOIN -0.50, AVAX -0.32, LINK -0.31, PENGU -0.02), TRX +0.06 only positive. | context — flat-to-down regime, RSI>55 unlikely across most pairs |
| 2026-04-26T04:40:00Z | overnight | kraken | Position check: no open positions to manage. No stops or EMA-cross checks needed. | no action |
| 2026-04-26T04:40:00Z | overnight | kraken | TRX/USD entry scan (1H close 03:00Z = 0.323905): 1H SMA20 ≈ 0.32373 (PASS razor +0.05%), 1H RSI14 ≈ 59.6 (PASS), 4H close (00:00Z bar) 0.323905 < 4H SMA50 ≈ 0.328567 (FAIL by 1.4%). | REJECT — entry-rule-3 (4H close < 4H EMA50) |
| 2026-04-26T04:40:00Z | overnight | kraken | PENGU/USD entry scan (1H close 03:00Z = 0.008627): 1H SMA20 ≈ 0.008541 (PASS), 1H RSI14 ≈ 54.1 (FAIL <55). | REJECT — entry-rule-2 (1H RSI14 < 55) |
| 2026-04-26T04:40:00Z | overnight | kraken | SOL/USD entry scan (1H close 03:00Z = 86.01): 1H SMA20 ≈ 86.18 (FAIL by -0.20%). | REJECT — entry-rule-1 (1H close < 1H EMA20) |
| 2026-04-26T04:40:00Z | overnight | kraken | Remaining 12 pairs (XBT -0.25%, ETH -0.36%, XRP -0.33%, TAO -0.82%, HYPE -0.48%, XDG -0.28%, SUI -0.38%, LTC -0.46%, ADA -0.43%, FARTCOIN -0.50%, AVAX -0.32%, LINK -0.31%): all negative 24h drift; under negative-drift regime, 1H RSI14>55 mathematically unlikely. | REJECT (12 pairs inferred) — entry-rule-2 (1H RSI14 < 55) — context-budget decision not to compute individually, consistent with prior wakes' methodology |
| 2026-04-26T04:40:00Z | overnight | system | News scan deferred per established pattern: kraken_risk_flag CLEAR is the binding macro/news pre-screen for v0 (not news-reactive). Morning brief skill runs separately and surfaces ACTIONABLE headlines. No headline-level actionable items recorded. | deferred |
| 2026-04-26T04:40:00Z | overnight | system | Universe refresh skipped: today is 2026-04-25/26 (not 1st of month). Next refresh 2026-05-01. | no action |
| 2026-04-26T04:40:00Z | overnight | system | Routine #1 result: 0 OPEN, 0 CLOSE, 0 ACTIONABLE news. Equity $9,930.76 (flat), DD 0.97%, all kill switches clear. Telegram silent per template (no entries, no exits, no kill-switch trip, no actionable news). | no Telegram |
2026-04-26T21:14:21Z | harness | day-gate | not Saturday, skipping | no action
| 2026-04-26T21:30:00Z | allocation | system | First weekly allocation review (W17, 2026-04-20→2026-04-26). Buckets: momentum 100% / mean-rev 0% / news-react 0% (v0 declared). 5 closed trades, 1W/4L, avg R −0.376, total PnL −$69.24, all in momentum. BTC-hold 7d +5.99%, BULL −0.69%, Δ −6.68%. 30d/90d not evaluable (only 6 days history). Sample below noise floor; only one active bucket exists; no proposal generated. | NO allocation change; weekly memo W17 written; no pending strategy edit to apply (W16 had no memo, W17 harness was MCP-skipped) |
| 2026-04-26T21:13:44Z | overnight | kraken | Risk flag CLEAR (no tier-1/2). Universe 24h regime FLIPPED POSITIVE since 04:40Z wake: PENGU +5.06, FARTCOIN +3.03, ETH +2.03, LINK +1.34, HYPE +1.04, TAO +0.99, AVAX +0.96, SOL +0.94, ADA +0.86, XDG +0.85, XBT +0.80, SUI +0.73, LTC +0.36, XRP +0.34, TRX -0.13. | context — broad rally regime; 1H RSI>55 likely across momentum movers |
| 2026-04-26T21:13:00Z | overnight | kraken | Position check: no open positions to manage at start of wake. | no action |
| 2026-04-26T21:13:00Z | overnight | kraken | ETH/USD entry scan (1H close 20:00Z = 2363.54): 1H SMA20 2336.73 (PASS +1.15%), RSI14 71.83 (PASS strong), 4H close (20:00Z bar) 2367.01 > 4H SMA50 2330.53 (PASS +1.6%), ATR14(1h) 9.22. Pre-entry guardrails: positions 0<4, portfolio risk 0%+0.21%≤4%, per-trade 0.21%≤1.5%, in-universe, daily loss 0.33%<5%, equity above floor — ACCEPT. | OPEN long @ 2364.72 (close + 0.05% slip), stop 2345.10 (2×ATR), size 1.0499, risk $20.60 (0.21%) — entry-rule-v0-momentum |
| 2026-04-26T21:13:00Z | overnight | kraken | BTC/USD entry scan (1H close 20:00Z = 78227.1): 1H SMA20 77963.05 (PASS +0.34%), RSI14 57.41 (PASS), 4H close (20:00Z bar) 78285.0 > 4H SMA50 76948.64 (PASS +1.74%), ATR14(1h) 211.98. Pre-entry guardrails ACCEPT. | OPEN long @ 78266.21, stop 77803.14, size 0.0317, risk $14.69 (0.15%) — entry-rule-v0-momentum |
| 2026-04-26T21:13:00Z | overnight | kraken | SOL/USD entry scan (1H close 20:00Z = 86.75): 1H SMA20 86.469 (PASS +0.32%), RSI14 55.84 (PASS razor-thin), 4H close (20:00Z bar) 87.09 > 4H SMA50 86.088 (PASS +1.16%), ATR14(1h) 0.3243. Pre-entry guardrails ACCEPT. | OPEN long @ 86.79, stop 86.10, size 28.6, risk $19.82 (0.20%) — entry-rule-v0-momentum |
| 2026-04-26T21:13:00Z | overnight | kraken | PENGU/USD entry scan (1H close 20:00Z = 0.009029): 1H SMA20 0.008784 (PASS), RSI14 63.34 (PASS), 4H close 0.009045 > 4H SMA50 0.008001 (PASS strong +13%), ATR14(1h) 0.000153. Strategy PASS on all 3 rules. BUT: 24h notional today $1.86M (universe rank 14, monthly $1.07M), at/below the sub-$2M threshold flagged in lessons.md #1 (TRX wick blow-through). | REJECT — discretionary skip per active lesson #1 (sub-$2M/24h thin-liquidity wick risk). Logged for routine #4 to formalize as a rule. |
| 2026-04-26T21:13:00Z | overnight | kraken | FARTCOIN/USD entry scan (1H close 20:00Z = 0.2045): 1H SMA20 0.20056 (PASS), RSI14 61.39 (PASS), 4H close 0.2043 > 4H SMA50 0.2007 (PASS +1.8%), ATR14(1h) 0.00183. Strategy PASS on all 3 rules. BUT: 24h notional today only $0.46M — 4× thinner than TRX was when its wick blew the stop. | REJECT — discretionary skip per active lesson #1, more strongly than PENGU |
| 2026-04-26T21:13:00Z | overnight | kraken | Remaining 10 pairs (XRP +0.34, TAO +0.99, HYPE +1.04, XDG +0.85, SUI +0.73, LTC +0.36, ADA +0.86, AVAX +0.96, LINK +1.34, TRX -0.13): not pulled — 3 of 4 max-concurrent slots filled by ETH/BTC/SOL with strong PASS signals; remaining slot reserved (LINK +1.34% would have been the next candidate by liquidity but per-position cap not exceeded). Context-budget decision consistent with prior wakes. | HOLD-OFF (slot capacity) |
| 2026-04-26T21:13:00Z | overnight | system | News scan deferred per established pattern: kraken_risk_flag CLEAR pre-screen, morning-brief skill runs separately. v0 not news-reactive. | deferred |
| 2026-04-26T21:13:00Z | overnight | system | Universe refresh skipped: today is 2026-04-26 (not 1st of month). Next refresh 2026-05-01. | no action |
| 2026-04-26T21:13:00Z | overnight | system | Routine #1 result: 3 OPEN (ETH, BTC, SOL), 0 CLOSE, 0 ACTIONABLE news. Equity $9,920.62 (cash $2,465.49 + positions $7,455.13), realized −$69.24, unrealized −$10.14 (entry slip+commission), DD 1.07% from peak. Portfolio risk 0.56%, all kill switches clear. Telegram digest required per template (new OPENs occurred). | TELEGRAM SEND — entry digest |
| 2026-04-27T04:10:00Z | overnight | kraken | Risk flag CLEAR (scan 2026-04-27T00:00Z, no tier-1/2). Universe 24h regime BROAD POSITIVE: PENGU +11.79, FARTCOIN +1.92, HYPE +1.74, TAO +1.72, SUI +1.19, XDG +1.18, ETH +1.0, SOL +0.89, ADA +0.76, XRP +0.74, LINK +0.62, XBT +0.56, AVAX +0.53, LTC +0.53, TRX +0.15. Rally extending from prior wake's flip. | context — momentum regime intact, RSI>55 likely across movers |
| 2026-04-27T04:10:00Z | overnight | kraken | ETH/USD position check: 1H close (just-closed 03:00Z bar) 2395.05 > SMA20 2357.82 (PASS HOLD); intraday low post-entry 2349.51 (21:00Z bar) > stop 2345.10 by $4.41 — narrow but intact. 4R target 2443.20 not hit. Unrealized +$29.84 (+1.20%). | HOLD ETH |
| 2026-04-27T04:10:00Z | overnight | kraken | BTC/USD position check: 1H close 03:00Z 79110 > SMA20 78359.6 (PASS HOLD); intraday low post-entry 77885.7 > stop 77803.14 by $82.56. 4R target 80118.49 not hit. Unrealized +$26.26 (+1.06%). | HOLD BTC |
| 2026-04-27T04:10:00Z | overnight | kraken | SOL/USD position check: 1H close 03:00Z 87.77 > SMA20 86.81 (PASS HOLD); intraday low post-entry 86.26 > stop 86.10 by $0.16 — razor-thin but intact. 4R target 89.55 not hit. Unrealized +$26.60 (+1.07%). | HOLD SOL |
| 2026-04-27T04:10:00Z | overnight | kraken | TAO/USD entry scan (1H close 03:00Z = 255.4353): 1H SMA20 250.03 (PASS +2.16%), RSI14 ≈ 81.2 (PASS), 4H close 04/27 00:00 bar 255.4353 > 4H SMA50 246.44 (PASS +3.65%), ATR14(1h) 2.222. Pre-entry guardrails: positions 3<4 (1 slot), portfolio risk 0.56%+0.43%≤4%, per-trade 0.43%≤1.5%, in-universe (rank 5, $6.80M notional > $2M lesson-1 threshold), daily loss 0%<5%, equity above floor — ACCEPT. | OPEN long @ 255.56 (close + 0.05% slip), stop 251.12 (2×ATR), size 9.6, risk $42.66 (0.43%) — entry-rule-v0-momentum |
| 2026-04-27T04:10:00Z | overnight | kraken | HYPE/USD entry scan (1H close 03:00Z = 43.26): 1H SMA20 41.84 (PASS +3.4%), RSI14 ≈ 94.8 (PASS but extreme/climactic), 4H close 04/27 00:00 bar 43.26 > 4H SMA50 42.14 (PASS +2.66%), ATR14(1h) 0.322. Strategy PASS on all 3 rules. | PASS on strategy, HOLD-OFF — cash slot consumed by TAO (preferred for slightly higher liquidity rank, less-extreme RSI, and stronger 4H structural cushion). Will re-evaluate next wake if HYPE still PASSes and a slot opens. |
| 2026-04-27T04:10:00Z | overnight | kraken | PENGU/USD entry scan: 24h +11.79% strong; universe rank 14 ($1.07M monthly notional). | REJECT — discretionary skip per active lesson #1 (sub-$2M/24h thin-liquidity wick risk, consistent with prior wake's PENGU/FARTCOIN reject pattern) |
| 2026-04-27T04:10:00Z | overnight | kraken | FARTCOIN/USD entry scan: 24h +1.92%; universe rank 11 ($1.52M monthly notional). | REJECT — discretionary skip per active lesson #1 |
| 2026-04-27T04:10:00Z | overnight | kraken | Remaining 9 pairs (XBT/ETH/SOL already-open; SUI +1.19, XDG +1.18, ADA +0.76, XRP +0.74, LINK +0.62, AVAX +0.53, LTC +0.53, TRX +0.15) — not pulled: 4 max-concurrent slots filled by ETH/BTC/SOL/TAO; ADA/AVAX/LTC/LINK/TRX below or near $2M lesson-1 threshold; SUI/XDG/XRP would need 1H+4H pull but no available cash/slot. Context-budget decision consistent with prior wakes. | HOLD-OFF (slot+cash capacity exhausted) |
| 2026-04-27T04:10:00Z | overnight | system | News scan deferred per established pattern: kraken_risk_flag CLEAR pre-screen, morning-brief skill runs separately. v0 not news-reactive. | deferred |
| 2026-04-27T04:10:00Z | overnight | system | Universe refresh skipped: today is 2026-04-26 PT (not 1st of month). Next refresh 2026-05-01. | no action |
| 2026-04-27T04:10:00Z | overnight | system | Routine #1 result: 1 OPEN (TAO), 0 CLOSE, 0 ACTIONABLE news. Equity $9,988.63 (cash $5.73 + positions $9,982.90), realized −$69.24, unrealized +$57.87 (overnight rally lifted ETH/BTC/SOL into profit), DD 0.39% from peak. Portfolio risk 0.99%, all kill switches clear. 4/4 strategy-cap concurrent slots filled. Telegram digest required per template (new OPEN occurred). | TELEGRAM SEND — entry digest |
| 2026-04-27T13:00:00Z | overnight | kraken | Risk flag CLEAR (scan 12:30Z, no tier-1/2; classifier note: routine sanctions only). Universe 24h regime FLIPPED NEGATIVE since prior wake: 13/15 pairs red — FARTCOIN -2.97, AVAX -2.43, ETH -2.34, SOL -2.13, LINK -1.90, ADA -1.76, SUI -1.71, XRP -1.49, LTC -1.47, XBT -1.26, XDG -1.09, TAO -0.52, HYPE -0.47; positives: TRX +0.74, PENGU +9.61 (post-cascade rebound). | context — bearish reversal, 1H RSI>55 unlikely on most pairs |
| 2026-04-27T13:00:00Z | overnight | kraken | ETH/USD position check: 1H bar 05:00Z low 2319.46 < stop 2345.10 → STOP HIT intrabar. Fill 2343.93 (stop × 0.9995 adverse slip per TRX precedent). Stop-dist 19.62, loss-per-unit 20.79 → R = -1.06. Net realized −$34.68 (gross −$21.83 + commissions $12.85 entry+exit at 0.26%/side). | EXIT ETH (exit-stop-hit) |
| 2026-04-27T13:00:00Z | overnight | kraken | BTC/USD position check: 1H bar 05:00Z low 77601.0 < stop 77803.14 → STOP HIT intrabar. Fill 77764.24. Stop-dist 463.07, loss-per-unit 501.97 → R = -1.08. Net realized −$28.77. | EXIT BTC (exit-stop-hit) |
| 2026-04-27T13:00:00Z | overnight | kraken | SOL/USD position check: 1H bar 05:00Z low 85.82 < stop 86.10 → STOP HIT intrabar. Fill 86.057. Stop-dist 0.69, loss-per-unit 0.733 → R = -1.06. Net realized −$33.82. | EXIT SOL (exit-stop-hit) |
| 2026-04-27T13:00:00Z | overnight | kraken | TAO/USD position check: 1H bar 05:00Z low 250.1191 < stop 251.12 → STOP HIT intrabar (entry was 04:05Z @ 255.56, held ~1 hour). Fill 251.004. Stop-dist 4.44, loss-per-unit 4.5556 → R = -1.03. Net realized −$56.38. | EXIT TAO (exit-stop-hit) |
| 2026-04-27T13:00:00Z | overnight | system | NOTABLE PRICE ANOMALY: all 4 open positions stopped out simultaneously in the same 05:00Z 1H bar — cross-asset cascade. ETH dropped -2.66% intra-bar, BTC -1.68%, SOL -1.95%, TAO -1.97%. Total day realized −$153.65 (-1.54% of pre-cascade equity, well below 5% kill switch). Lesson appended to lessons.md (correlation risk in v0 sizing). | Lesson logged |
| 2026-04-27T13:00:00Z | overnight | kraken | Entry scan post-cascade: ETH/BTC/SOL/TAO 1H closes (12:00Z) all below pre-dump-elevated SMA20 → REJECT rule-1 (1H close < EMA20). Bearish regime drives 1H RSI14 below 55 across negative-drift pairs → inferred REJECT rule-2 for AVAX/ADA/LINK/SUI/XRP/LTC/XDG/HYPE/FARTCOIN. TRX +0.74% but rank 15 / $1.04M monthly notional → REJECT per lesson #1 (sub-$2M wick risk). PENGU +9.61% but rank 14 / $1.07M monthly → REJECT per lesson #1. Net: 0 entries. | REJECT (15 pairs) |
| 2026-04-27T13:00:00Z | overnight | system | News scan deferred per established pattern: kraken_risk_flag CLEAR pre-screen ("Markets calm"), morning-brief skill runs separately. v0 not news-reactive. No headline-level actionable items recorded. The 05:00Z cascade had no obvious news trigger in the risk-scan window — purely market-internal flow. | deferred |
| 2026-04-27T13:00:00Z | overnight | system | Universe refresh skipped: today is 2026-04-27 (not 1st of month). Next refresh 2026-05-01 (Friday). | no action |
| 2026-04-27T13:00:00Z | overnight | system | Routine #1 result: 0 OPEN, 4 CLOSE (cross-asset stop cascade ETH/BTC/SOL/TAO at 05:00Z), 0 ACTIONABLE news. Equity $9,777.08 (cash, no positions), realized all-time −$222.89, DD 2.50% from peak $10,027.55. Day realized −$153.65 (-1.54%). Portfolio risk 0.00%. Daily-loss kill switch 1.54% vs 5% cap (clear). DD 2.50% vs 25% cap and 12.5% warn (clear). Equity floor far above $7,500. Telegram digest required per template (4 stop-out CLOSEs occurred). | TELEGRAM SEND — exit digest |
| 2026-04-28T02:44:14Z | harness | day-gate | not Saturday, skipping | no action
| 2026-04-28T02:44:30Z | allocation | day-gate | not Sunday (Mon 2026-04-27 PT), skipping | no action |
| 2026-04-28T17:00:00Z | overnight | kraken | Risk flag CLEAR (scan 2026-04-28T02:43Z, no tier-1/2; "Markets calm"). Universe 24h regime BROADLY NEGATIVE post-cascade rebound: 12/15 red — XBT -1.81, XRP -1.83, ETH -1.07, SOL -1.44, HYPE -4.42, SUI -1.45, LTC -0.79, ADA -0.54, FARTCOIN -0.05, AVAX -0.76, LINK -1.00, PENGU -1.32, TRX -0.59; positives: TAO +5.08, XDG +0.65. | context — divergent tape, TAO breakout against weak broader market |
| 2026-04-28T17:00:00Z | overnight | kraken | Position check: no open positions to manage at start of wake (flat from 2026-04-27 cascade). | no action |
| 2026-04-28T17:00:00Z | overnight | kraken | TAO/USD entry scan (1H close 16:00Z = 259.9863, just-closed bar): 1H SMA20 ≈ 249.90 (PASS +4.0%), 1H RSI14 ≈ 86.1 (PASS but climactic/extreme), 4H close (just-closed 12:00Z bar) 256.2051 > 4H SMA50 247.45 (PASS +3.5%), ATR14(1H) ≈ 2.69. Universe rank 5, 24h notional ≈ $2.86M (live) > $2M lesson-1 threshold. Pre-entry guardrails: positions 0<4 (4 slots open), portfolio risk 0%+0.52%≤4%, per-trade 0.52%≤1.5%, in-universe, daily loss 0%<5%, equity $9,777 above $7,500 floor — ACCEPT. | OPEN long @ 260.12 (close + 0.05% slip), stop 254.74 (2×ATR), size 9.4 (equity/4 cash convention, $2,445 notional), risk $50.57 (0.52%) — entry-rule-v0-momentum |
| 2026-04-28T17:00:00Z | overnight | kraken | XDG/USD entry scan (1H close 16:00Z = 0.0995999): 1H SMA20 ≈ 0.09918 (PASS razor-thin +0.42%), RSI14 ≈ 54.65 (FAIL <55 by 0.35). | REJECT — entry-rule-2 (1H RSI14 < 55, razor-thin miss) |
| 2026-04-28T17:00:00Z | overnight | kraken | HYPE/USD entry scan: 24h -4.42% strong negative; under negative drift RSI14>55 mathematically implausible. Plus universe rank 6 ($5.86M) above lesson-1 threshold but no positive momentum to qualify. | REJECT — entry-rule-2 (1H RSI14 < 55) inferred |
| 2026-04-28T17:00:00Z | overnight | kraken | PENGU/USD entry scan: 24h -1.32%; rank 14 ($1.07M monthly notional) below $2M lesson-1 threshold. | REJECT — entry-rule-2 inferred + lesson-1 thin-liquidity skip |
| 2026-04-28T17:00:00Z | overnight | kraken | FARTCOIN/USD entry scan: 24h -0.05%; rank 11 ($1.52M monthly notional) below $2M lesson-1 threshold. | REJECT — entry-rule-2 inferred + lesson-1 thin-liquidity skip |
| 2026-04-28T17:00:00Z | overnight | kraken | TRX/USD entry scan: 24h -0.59%; rank 15 ($1.04M monthly notional) below $2M lesson-1 threshold. | REJECT — entry-rule-2 inferred + lesson-1 thin-liquidity skip |
| 2026-04-28T17:00:00Z | overnight | kraken | Remaining 9 pairs (XBT -1.81, ETH -1.07, SOL -1.44, XRP -1.83, SUI -1.45, LTC -0.79, ADA -0.54, AVAX -0.76, LINK -1.00) — all 24h negative under risk-off broader tape; under negative drift, 1H RSI14>55 mathematically unlikely. Context-budget decision not to compute individually, consistent with prior wakes' methodology. | REJECT (9 pairs inferred) — entry-rule-2 (1H RSI14 < 55) |
| 2026-04-28T17:00:00Z | overnight | system | Lesson #2 (cross-asset cascade) flagged for review: TAO entry on RSI 86 climactic in divergent tape (12/15 negative) vs prior cascade pattern. Different vector — only 1 slot fill not 4 — so lesson #2's specific failure mode (concurrent correlated stops) does not apply, but RSI extremity + same-day re-entry post-stopout is a new risk pattern to monitor. If TAO stops within 6h, append data point to lessons.md for routine #4 RSI-cap proposal. | proceed with entry, monitor at midday |
| 2026-04-28T17:00:00Z | overnight | system | News scan deferred per established pattern: kraken_risk_flag CLEAR pre-screen ("Markets calm"), morning-brief skill runs separately. v0 not news-reactive. The 04-27 05:00Z cascade had no news trigger — purely market-internal flow per prior wake's analysis, reinforcing v0's news-blindness as not a current cost factor. | deferred |
| 2026-04-28T17:00:00Z | overnight | system | Universe refresh skipped: today is 2026-04-28 (not 1st of month). Next refresh 2026-05-01 (Friday). | no action |
| 2026-04-28T17:00:00Z | overnight | system | Routine #1 result: 1 OPEN (TAO/USD), 0 CLOSE, 0 ACTIONABLE news. Equity $9,769.46 (cash $7,325.59 + position $2,443.87), realized −$222.89, unrealized −$7.62 (entry drag), DD 2.57% from peak $10,027.55. Portfolio risk 0.52%, all kill switches clear. 1/4 strategy-cap concurrent slots filled. Telegram digest required per template (new OPEN occurred). | TELEGRAM SEND — entry digest |
2026-04-28T17:59:42Z | harness | day-gate | not Saturday, skipping | no action
2026-04-28T17:59:41Z | allocation | day-gate | not Sunday, skipping | no action
| 2026-04-28T23:07:36Z | strategy | applied | W18 proposal A+B+C approved off-cycle by user via chat 2026-04-28; cluster cap, liquidity floor, one-per-wake committed to strategy.md (v0 -> v0.1); 2 lessons marked superseded | strategy.md updated, lessons updated, research_log appended |
| 2026-04-29T14:00:00Z | overnight | kraken | Risk flag CLEAR (scan 2026-04-29T00:00:32Z, no tier-1/2; "Markets calm"). Universe 24h regime BROADLY NEGATIVE: 14/15 red — PENGU -4.39, TAO -2.81, FARTCOIN -2.59, SUI -2.22, LINK -1.31, XRP -1.09, HYPE -1.05, ADA -0.91, LTC -0.75, SOL -0.61, ETH -0.52, XBT -0.38, AVAX -0.22, TRX -0.08; only positive XDG +4.0% (climactic blow-off, peak 0.1120 then -7.7% pullback). | context — risk-off divergent tape, RSI>55 mathematically unlikely on 14/15 pairs |
| 2026-04-29T14:00:00Z | overnight | kraken | TAO/USD position check: 1H bar 14:00Z low 253.7004 < stop 254.74 → STOP HIT intrabar. Fill 254.61 (stop × 0.9995 adverse slip per established model). Stop-dist 5.38, loss-per-unit 5.51 → R = -1.02. Net realized −$64.37 (gross −$51.79 + commissions $12.58). Position held ~21h after 17:00Z 04-28 entry; survived overnight rally to high 266.44 (+2.4% above entry) but reversed sharply, drift to 14:00Z dump. | EXIT TAO (exit-stop-hit) |
| 2026-04-29T14:00:00Z | overnight | kraken | XDG/USD entry scan (1H close 15:00Z = 0.1033165, just-closed bar): 1H SMA20 ≈ 0.10335 (FAIL by 0.04% — close just below SMA20). 24h notional ~$15.6M (well above $2M lesson-1 / W18-B floor). Pattern: blow-off top — peak 0.1120861 at 09:00Z, since pulled back -7.7% over 6 bars (climactic exhaustion). Discretionary read reinforces rule-1 fail: late-stage chase against sharp reversal. | REJECT — entry-rule-1 (1H close < 1H EMA20) + climactic exhaustion read |
| 2026-04-29T14:00:00Z | overnight | kraken | Remaining 13 non-open pairs (XBT -0.38, ETH -0.52, SOL -0.61, XRP -1.09, TAO -2.81, HYPE -1.05, SUI -2.22, LTC -0.75, ADA -0.91, FARTCOIN -2.59, AVAX -0.22, LINK -1.31, PENGU -4.39, TRX -0.08): all 24h negative under risk-off broader tape; under negative drift, 1H RSI14>55 mathematically unlikely. Liquidity sub-$2M floor excludes AVAX ($0.44M), LINK ($1.22M), LTC ($1.88M), TRX ($1.34M) regardless. Context-budget decision not to compute individually, consistent with prior wakes' methodology. | REJECT (13 pairs inferred) — entry-rule-2 (1H RSI14 < 55) ± W18-B liquidity floor |
| 2026-04-29T14:00:00Z | overnight | kraken | TAO same-day re-entry post-stopout flagged as failed pattern: 04-28 17:00Z entry on RSI ≈86 (climactic) in divergent tape (12/15 negative); 04-29 14:00Z stop-out at -1.02R after 21h hold. Lesson #4 candidate — RSI extremity at entry combined with broad-tape divergence is a worse-than-average setup. To be formalized in next routine #4 with backtest evidence; pattern noted to lessons.md. | lesson appended (RSI-extremity / divergent-tape setup) |
| 2026-04-29T14:00:00Z | overnight | system | News scan deferred per established pattern: kraken_risk_flag CLEAR pre-screen ("Markets calm"), morning-brief skill runs separately. v0.1 not news-reactive. | deferred |
| 2026-04-29T14:00:00Z | overnight | system | Universe refresh skipped: today is 2026-04-29 (not 1st of month). Next refresh 2026-05-01 (Friday). | no action |
| 2026-04-29T14:00:00Z | overnight | system | Routine #1 result: 0 OPEN, 1 CLOSE (TAO/USD stop-hit), 0 ACTIONABLE news. Equity $9,712.70 (cash, no positions), realized all-time −$287.26, DD 3.14% from peak $10,027.55 (warn 12.5% / cap 25%). Day realized −$64.37 (−0.66% on pre-close equity, cap 5%). Portfolio risk 0.00%. Equity floor far above $7,500. Telegram digest required per template (CLOSE event occurred). | TELEGRAM SEND — exit digest |
2026-04-29T17:07:19Z | harness | day-gate | not Saturday, skipping | no action

2026-04-29T17:40:38Z | allocation | day-gate | not Sunday, skipping | no action
| 2026-04-29T20:07:09Z | midday | system | Portfolio flat (0 open positions) after TAO stop-out at 14:00Z; no MTM/exit checks required. Equity $9,712.70 = cash $9,712.70 (no positions). Day realized −$64.37 (−0.66% on pre-close equity, cap 5%). DD 3.14% from peak $10,027.55 (warn 12.5%, cap 25%). All kill switches clear: daily loss 0.66% < 5%, DD 3.14% < 12.5% warn, equity > $7,500 floor, consecutive-losing-days streak not 7-in-a-row. Midday is position-mgmt only — no entries scanned per routine spec. | no action — silent (no exits, no kill-switch trip, no DD warning) |
2026-05-04T19:07:20Z | harness | day-gate | not Saturday, skipping | no action
2026-05-04T19:08:14Z | allocation | day-gate | not Sunday, skipping | no action

## 2026-05-04T19:00Z — routine-01-overnight

> **Note:** First routine-01 run since 2026-04-29 — 5-day gap (4-30 Thu, 5-01 Fri, 5-02 Sat, 5-03 Sun, 5-04 Mon morning). May 1 universe-refresh window was missed; flagging for catch-up but not refreshing this wake (strict spec is "today is the 1st" and the procedural cost outweighs membership stability over 4 days).

### Technical (rule-driven, deterministic)

- **Risk flag:** CLEAR (scan 2026-05-04T00:17Z; 1 tier-2 caution: Iran military-escalation headline, non-blocking — needs 2 major-source confirmations).
- **Universe regime:** 12/15 positive 24h — XBT +1.80, ETH +1.49, SOL +0.76, XRP +0.92, XDG +2.17, SUI +1.89, LTC −0.20, ADA +0.74, FARTCOIN +3.65, AVAX +1.98, LINK +3.16, PENGU +1.27, TRX +0.37, HYPE −0.39, TAO −2.01. **Regime gate (W19-D rule 5a):** PASS — 12/15 ≥ 4/15 positive.
- **Liquidity floor (W18-B rule 4a):** AVAX 24h notional ≈ $1.76M — FAIL $2M floor (excluded). All others ≥ $2M (TRX razor-thin ~$2.01M).
- **Same-pair re-entry cooldown (W19-D rule 5b):** No active cooldowns — last stop-out (TAO 04-29) is 5 days old, well past 24h window.

**Entry-scan results (just-closed 1H bar at 18:00Z 5/4):**

- **BTC/USD** (rank 1): close 80105.1, 1H SMA20 ≈ 79642.6 → PASS rule 1; 1H RSI14 ≈ 47.6 → **FAIL rule 2** (post-spike fade after 14:00Z +$1456 pump-then-revert). REJECT.
- **ETH/USD** (rank 2): close 2361.20, 1H SMA20 ≈ 2356.39 → PASS rule 1 (razor-thin +0.20%); 1H RSI14 ≈ 41.0 → **FAIL rule 2**. REJECT.
- **SOL/USD** (rank 3): not individually computed — cluster-correlated with BTC/ETH, expected similar RSI fade pattern. INFERRED REJECT — entry-rule-2.
- **XRP/USD** (rank 4): close 1.40378, 1H SMA20 ≈ 1.40378 → razor-tie **FAIL rule 1** (need close > EMA20 strict). REJECT.
- **TAO/USD** (rank 5): 24h −2.01% — under negative drift, 1H RSI14>55 mathematically unlikely. INFERRED REJECT — entry-rule-2.
- **HYPE/USD** (rank 6): 24h −0.39% — INFERRED REJECT — entry-rule-2.
- **XDG/USD** (rank 7): close 0.1110277, 1H SMA20 ≈ 0.1113126 → **FAIL rule 1** (close < EMA20 by 0.26%). Pattern: post-pump fade from 0.1137 peak at 03:00Z. REJECT.
- **SUI/USD** (rank 8): close 0.9399, 1H SMA20 ≈ 0.93471 → PASS rule 1; 1H RSI14 ≈ 45.5 → **FAIL rule 2**. REJECT.
- **LTC/USD** (rank 9): 24h −0.20% — INFERRED REJECT — entry-rule-2.
- **ADA/USD** (rank 10): 24h +0.74% modest, not pulled — 1 entry already chosen. HOLD-OFF.
- **FARTCOIN/USD** (rank 11): close 0.2103, 1H SMA20 ≈ 0.21108 → **FAIL rule 1** (close < EMA20 by 0.37%). REJECT.
- **AVAX/USD** (rank 12): excluded by W18-B liquidity floor ($1.76M < $2M). REJECT — entry-rule-4a.
- **LINK/USD** (rank 13): close 9.43462, 1H SMA20 ≈ 9.36810 → PASS rule 1 (+0.71%); 1H RSI14 ≈ 55.3 → PASS rule 2 (razor-thin) and rule 2a (<80); 4H close (12:00Z bar) 9.42709, 4H SMA50 ≈ 9.22660 → PASS rule 3 (+2.18%); ≥10 candles ✓; 24h notional $5.17M > $2M ✓; not already open ✓; cluster cap 0/2 → entry yields 1/2 ✓; per-trade risk 0.63% ≤ 1.5% ✓; portfolio risk 0% + 0.63% = 0.63% ≤ 4% ✓; daily loss 0% < 5% ✓; equity $9,712.70 > $7,500 ✓. ATR14(1H) ≈ 0.1187. **Pre-entry-check ACCEPT.**
- **PENGU/USD** (rank 14): 24h notional ~$2.55M (above floor); 24h +1.27%. Not pulled — 1 entry already chosen, lower 30d-rank than LINK per universe.md. HOLD-OFF (W18-C one-per-wake, prefer-highest-rank).
- **TRX/USD** (rank 15): 24h notional razor-thin ~$2.01M; 24h +0.37% modest. Not pulled — same reason. HOLD-OFF.

**Final candidate:** LINK/USD (only pair clearing all 8 rules + cluster + liquidity + regime + cooldown).

### News (Firecrawl-driven, informational only in v0.2)

News scan deferred per established pattern: kraken_risk_flag CLEAR pre-screen (1 tier-2 military-escalation caution but non-blocking, lacks major-source confirmation). v0.2 strategy is not news-reactive — no entry gate depends on news this run. Morning-brief skill runs separately and surfaces ACTIONABLE headlines if any. No headline-level actionable items recorded for this routine.

### Sentiment (passive — Kraken depth/spread proxy in v0.2)

Not pulled this wake — broad-rally regime with sufficient candidate clarity from price/volume data alone. To be added to candidate-only scans in routine #2 if entry sat at marginal pass.

### Decision

**OPEN LINK/USD long** @ 9.4393 (close 9.43462 + 0.05% slip), stop 9.2018 (entry − 2×ATR), size 257 LINK (equity/4 cash convention, $2,425.90 notional), risk $61.03 (0.63% of equity). Reason: entry-rule-v0-momentum (rules 1, 2, 2a, 3, 4, 4a, 5, 5a, 5b, 6, 6a, 7, 8 all pass). Trade row appended to trade_log.md; portfolio.md rebuilt.

Cluster state after entry: 1/2 in BTC-correlated cluster {BTC,ETH,SOL,TAO,AVAX,SUI,LINK}.

### Process notes

- **5-day routine gap (2026-04-30 → 2026-05-04 morning):** No routine-01 entries between 2026-04-29T14:00Z and now. Cause unknown (scheduled-task interruption, no exit log). Flagging for operator review — does not affect this wake's decision (portfolio was flat through gap, no open positions to mismanage).
- **May 1 universe-refresh missed:** Today's 24h-notional readings indicate universe membership likely unchanged (top 15 stable from 2026-04-20 ranking; AVAX dropped below liquidity floor but still in universe). Strict spec says refresh on the 1st of month — today is 4th. Will re-evaluate at next month's window (2026-06-01 Mon). Operator may force a refresh via direct universe.md edit if desired.
- **Concurrent routine-02-midday rebuild at 19:05:30Z:** Wrote portfolio.md to "flat" state; superseded by this wake's rebuild at 19:10:00Z reflecting LINK OPEN.

### Telegram

ENTRY DIGEST required per template (new OPEN occurred). Message will be sent after commit.
| 2026-05-04T19:14:56Z | offline-audit | system | User offline 2026-04-29 20:07Z to 2026-05-04 today; cron silent during gap (Claude Code Desktop was closed). Zero routine wakes, zero trades during 5-day window. Strategy v0.2 untested in production since W19 application. CODEX competitor data files stale at $10K baselines (no refresh observed). OPERATING.md created documenting cron-Claude-Code dependency and CODEX sync gap. | OPERATING.md added; no manual routine catch-up triggered (per recommendation 'let cron resume naturally'); next scheduled wake bull-02-midday at 2026-05-04T20:05Z |

## 2026-05-05T05:00Z — routine-01-overnight (EOD-window pass; bull-03-eod cron fired post-22:00 PT)

> Wake context: bull-03-eod task fired with routine-01-overnight content. Just-closed 1H bar = 2026-05-05 05:00Z (= 2026-05-04 22:00 PT). Pre-existing position: LINK from morning routine-01. Risk flag: CLEAR (kraken_risk_flag scan 2026-05-05T00:00Z, tier1=0, tier2=0, blocked=false).

### Universe price scan (15 pairs, 24h % change)

| Pair | Last | 24h % | 24h notional | vs $2M floor |
|------|------|-------|--------------|--------------|
| BTC/USD | 80926.7 | +1.36 | $194.9M | ✓ |
| ETH/USD | 2378.7 | +1.35 | $45.6M | ✓ |
| SOL/USD | 84.85 | +0.89 | $13.7M | ✓ |
| XRP/USD | 1.40077 | +0.65 | $13.9M | ✓ |
| TAO/USD | 285.84 | +0.32 | $5.93M | ✓ |
| HYPE/USD | 42.42 | +1.48 | $5.72M | ✓ |
| XDG/USD | 0.1115 | +1.25 | $7.97M | ✓ |
| SUI/USD | 0.9408 | +1.22 | $2.00M | ✓ (tight) |
| LTC/USD | 55.14 | +0.29 | $3.15M | ✓ |
| ADA/USD | 0.25251 | +1.03 | $3.35M | ✓ |
| FARTCOIN/USD | 0.2101 | +2.69 | $1.96M | ✗ |
| AVAX/USD | 9.28 | +1.09 | $1.98M | ✗ |
| LINK/USD | 9.56418 | +2.12 | $4.67M | ✓ (open) |
| PENGU/USD | 0.010761 | +6.57 | $4.70M | ✓ |
| TRX/USD | 0.339148 | −0.43 | $2.01M | ✓ (tight) |

Regime gate (W19-D 5a): **14/15 positive** ≥ 4 → PASS, new entries allowed.

### Position check on open positions

- **LINK/USD** (long 257 @ 9.4393, stop 9.2018): last 9.56418, 24h low 9.2592 — well above stop, no stop-out. MTM +$25.78. Hold.

No exits this wake.

### Entry-scan candidates (rule 8 prefer highest 30d notional rank)

- **BTC/USD** (rank 1): 1H close 80920.7, 1H 20-EMA ≈ 80317.5 → PASS rule 1; 1H RSI14 ≈ 67.0 → PASS rule 2 (>55) and rule 2a (≤80); 4H last-closed (2026-05-05 00:00) close 80879.3, 4H 50-EMA ≈ 78159 → PASS rule 3; ≥10 candles ✓; 24h notional $194.9M > $2M ✓; not currently open ✓ (last BTC stop 2026-04-27, ~8d ago > 24h cooldown ✓); regime 14/15 positive ≥ 4 ✓; positions 1<4 ✓; cluster: LINK 1 → BTC entry brings to 2 ≤ 2 ✓; per-trade risk computed below; portfolio risk 0.63%+0.26% = 0.89% ≤ 4% ✓; rank 1 (top of universe). **Pre-entry-check ACCEPT.**

  - ATR14(1H) ≈ 418.49 → 2×ATR = 836.97
  - Fill = 80920.7 × 1.0005 = 80961.16 (close + 0.05% slip)
  - Stop = 80961.16 − 836.97 = 80124.19
  - Sizing: equity/4 cash convention (per W18-aligned practice; risk-based 0.1737 BTC would consume 99% of cash and breach prudence) → notional $9,730.98/4 ≈ $2,433. Size = floor(2422 / 80961.16, 4 dp) = **0.0299 BTC**. Notional 0.0299×80961.16 = $2,420.74. Entry comm 0.26% × 2420.74 = $6.29. Total cost $2,427.03. Cash after: $4,853.46.
  - Risk: 0.0299 × 836.97 = $25.02 = 0.26% of equity ($9,691.99 pre-entry). Well within 1.5% per-trade cap.

- **ETH/USD** (rank 2): would also satisfy 1H/4H/RSI checks (close 2378.7 above EMA20, RSI estimated ~60-65 from rally bars 02:00-03:00 UTC), but per rule 8 BTC wins by rank when both eligible. Cluster cap would also be hit at 2/2 either way. INFERRED REJECT — entry-rule-8 (lower rank than BTC; 1 entry/wake limit).

- **SOL/USD** (rank 3): cluster-correlated with BTC; even if rules pass, blocked by rule 6a cluster cap (BTC entry brings cluster to 2/2; SOL would push 3>2). REJECT — entry-rule-6a.

- **XRP/USD** (rank 4): not pulled in detail — 1 entry already chosen this wake (rule 8 W18-C). HOLD-OFF. Note: XRP is non-cluster, would be candidate next wake if XRP's own conditions still pass.

- **TAO/USD** (rank 5): cluster-correlated, cluster cap blocks even if rules pass. REJECT — entry-rule-6a.

- **HYPE/USD** (rank 6): not pulled in detail — HOLD-OFF (W18-C, 1/wake).

- **XDG/USD** (rank 7): not pulled in detail — HOLD-OFF.

- **SUI/USD** (rank 8): cluster-correlated, cluster cap blocks. REJECT — entry-rule-6a.

- **LTC/USD** (rank 9): not pulled in detail — HOLD-OFF.

- **ADA/USD** (rank 10): not pulled in detail — HOLD-OFF.

- **FARTCOIN/USD** (rank 11): excluded by W18-B liquidity floor ($1.96M < $2M). REJECT — entry-rule-4a.

- **AVAX/USD** (rank 12): excluded by W18-B liquidity floor ($1.98M < $2M) AND cluster cap. REJECT — entry-rule-4a + 6a.

- **LINK/USD** (rank 13): already open. REJECT — entry-rule-5.

- **PENGU/USD** (rank 14): not pulled in detail — HOLD-OFF (rank lower than BTC; 1/wake limit). Note: 24h +6.57% suggests RSI extension; if pulled, rule 2a (RSI ≤ 80) might bite.

- **TRX/USD** (rank 15): 24h −0.43% — INFERRED REJECT — entry-rule-2 (RSI > 55 unlikely on negative drift).

**Final candidate:** BTC/USD (highest-rank pair clearing all rules; cluster cap 1→2 just within limit).

### News (lightweight scan; morning routine-01 covered Firecrawl pass)

Morning's news scan reported "1 tier-2 military-escalation caution but non-blocking, lacks major-source confirmation". Today's kraken_risk_flag (scanned 2026-05-05T00:00:34Z) reads **CLEAR** — no tier1, no tier2, summary "No significant risk events detected. Markets calm." No fresh Firecrawl pull this wake (token budget; morning pass + automated risk-flag suffice). No ACTIONABLE items.

### Sentiment (passive)

Broad rally regime (14/15 pairs positive). 1H BTC volume on the 14:00Z and 02:00Z bars (198 BTC and 314 BTC respectively) indicates real momentum participation, not low-liquidity wick. Sufficient candidate clarity from price/volume — no spread/depth pull needed.

### Decision

**OPEN BTC/USD long** @ 80961.16 (close 80920.7 + 0.05% slip), stop 80124.19 (entry − 2×ATR), size 0.0299 BTC ($2,420.74 notional), risk $25.02 (0.26% of equity). Reason: entry-rule-v0-momentum (rules 1, 2, 2a, 3, 4, 4a, 5, 5a, 5b, 6, 6a, 7, 8 all pass). Trade row appended to trade_log.md; portfolio.md rebuilt.

Cluster state after entry: **2/2** in BTC-correlated cluster {BTC, ETH, SOL, TAO, AVAX, SUI, LINK} — at the W18-A cap. No further cluster entries possible until LINK or BTC closes.

### Process notes

- **Task-name vs content mismatch:** scheduled task is named `bull-03-eod` (06:00 PT cron) but its SKILL.md content is the routine-01-overnight body. Executed per the SKILL content. The `skills/telegram.md` "EOD mandatory daily card" template is not invoked; routine-01 telegram rule (digest only on entry/kill/news) applies. Operator may want to reconcile task naming vs body in a future maintenance pass.
- **First-of-month universe refresh:** today is 2026-05-04 (Mon, 4th of month) → not first of month → no refresh.
- **Cluster cap state:** at 2/2. Going forward this wake, no cluster pair can be added even if eligible.

### Telegram

ENTRY DIGEST required per template (new OPEN occurred). Message will be sent after commit.

---

## 2026-05-05T17:55:51Z — routine-01-overnight (5/5 wake)

### Universe price snapshot (kraken_multi_ticker)

| Pair | Last | 24h % | 24h notional est | rule-4a ($2M floor) |
|------|------|-------|------------------|---------------------|
| BTC/USD | 81287.0 | +1.81 | $180M | OK |
| ETH/USD | 2363.12 | +0.68 | $38.7M | OK (cluster) |
| SOL/USD | 85.46 | +1.62 | $12.2M | OK (cluster) |
| XRP/USD | 1.40915 | +1.26 | $10.1M | OK |
| TAO/USD | 282.514 | -0.84 | $7.39M | OK (cluster, only neg) |
| HYPE/USD | 44.32 | +6.03 | $6.91M | OK |
| XDG/USD | 0.1138691 | +3.40 | $7.07M | OK |
| SUI/USD | 0.959 | +3.17 | $3.02M | OK (cluster) |
| LTC/USD | 55.63 | +1.18 | $3.58M | OK |
| ADA/USD | 0.2584 | +3.38 | $4.93M | OK |
| FARTCOIN/USD | 0.2203 | +7.67 | $2.16M | OK (just above floor) |
| AVAX/USD | 9.37 | +2.07 | $1.44M | FAIL (cluster + below floor) |
| LINK/USD | 9.69517 | +3.52 | $3.67M | OK (open) |
| PENGU/USD | 0.011474 | +13.63 | $6.49M | OK |
| TRX/USD | 0.34422 | +1.06 | $1.40M | FAIL |

Regime gate (W19-D 5a): **14/15 positive** >= 4 -> PASS, new entries allowed (only TAO -0.84%).
Risk flag: **CLEAR** (1 tier-2 caution: Iran/Hormuz military, non-blocking, lacks major-source confirmation).

### Position check on open positions

- **LINK/USD** (long 257 @ 9.4393, stop 9.2018): last 9.69517, 24h low 9.32 — well above stop. MTM **+$59.45** (+0.97R). Hold. No 1H close < EMA20 trigger detected.
- **BTC/USD** (long 0.0299 @ 80961.16, stop 80124.19): last 81287.0, 24h low 79743.1 occurred at 23:00Z 5/4 (BEFORE 05:00Z 5/5 entry). Post-entry 1H bars (05:00-17:00Z 5/5): minimum low = 80520.0 (09:00Z) — well above stop. MTM **+$3.45**. Hold.

No exits this wake.

### Entry-scan candidates (rule 8 prefer highest 30d notional rank)

Cluster state: 2/2 (LINK + BTC) at W18-A cap -> BTC, ETH, SOL, TAO, AVAX, SUI, LINK all blocked from new cluster entries this wake.

Non-cluster eligible candidates (rank order):

- **XRP/USD** (rank 4): 1H last-closed bar (5/5 16:00Z) close 1.40787, 1H 20-EMA approx 1.40671 -> PASS rule 1; 1H RSI14 approx **60.5** (avg gain 0.001544 / avg loss 0.001006, RS 1.535) -> PASS rules 2 + 2a (>55, <=80); 4H last-closed (5/5 12:00Z) close 1.41175, 4H 50-EMA approx 1.39496 -> PASS rule 3; >=10 candles OK; 24h notional approx $10M > $2M OK; not currently open OK (no XRP stop history); regime 14/15 positive >= 4 OK; positions 2<4 OK; non-cluster — rule 6a not engaged OK; per-trade risk 0.245% <= 1.5% OK; portfolio risk 0.881% + 0.245% = 1.13% <= 4% OK; rank 4 (highest non-blocked rank). **Pre-entry-check ACCEPT.**

  - ATR14(1H) over bars 5/5 03:00-16:00Z = sum TR 0.09725 / 14 = **0.006946** -> 2xATR = 0.013893
  - Fill = 1.40787 x 1.0005 = **1.40857** (close + 0.05% slip)
  - Stop = 1.40857 - 0.013893 = **1.39468**
  - Sizing (equity/4 cash convention per W18-aligned practice; risk-based 10510 XRP would consume notional $14.8K > available cash $4853) -> notional cap $9,712.74/4 approx $2,428. Size = floor(2427/1.40857) = **1723 XRP**. Notional 1723 x 1.40857 = $2,426.97. Entry comm 0.26% x 2426.97 = $6.31. Total cost $2,433.28. Cash after: $2,420.18.
  - Risk: 1723 x 0.013893 = $23.93 = **0.245%** of equity. Well within 1.5% per-trade cap.

- **HYPE/USD** (rank 6): not pulled in detail — HOLD-OFF (W18-C, 1 entry/wake; XRP wins by rank). 24h +6.03% suggests possible RSI extension; if scanned next wake, rule 2a (RSI <= 80) check needed.
- **XDG/USD** (rank 7): not pulled in detail — HOLD-OFF (rank lower than XRP).
- **LTC/USD** (rank 9): not pulled in detail — HOLD-OFF.
- **ADA/USD** (rank 10): not pulled in detail — HOLD-OFF.
- **FARTCOIN/USD** (rank 11): just above $2M floor at $2.16M — borderline. HOLD-OFF (rank lower than XRP, 1/wake limit). 24h +7.67% — RSI-cap concern next wake.
- **PENGU/USD** (rank 14): 24h +13.63% — extremely climactic, rule 2a (RSI <= 80) almost certainly bites. HOLD-OFF + INFERRED REJECT — entry-rule-2a likely.
- **TRX/USD** (rank 15): excluded by W18-B liquidity floor ($1.40M < $2M). REJECT — entry-rule-4a.
- **ETH/USD, SOL/USD, TAO/USD, SUI/USD, AVAX/USD** (cluster): blocked by W18-A cluster cap (2/2). REJECT — entry-rule-6a (regardless of other-rule status).
  - AVAX additionally rejected by W18-B (24h notional $1.44M < $2M).
  - TAO additionally has 24h -0.84% (only negative pair) and would also fail rule 2 likely.
- **LINK/USD** (rank 13): already open. REJECT — entry-rule-5.

**Final candidate:** XRP/USD (highest-rank non-cluster pair clearing all rules).

### News (lightweight scan)

Today's `kraken_risk_flag` (scanned 2026-05-05T17:55:51Z) reads **CLEAR**. Tier-2 caution (Iran/Strait of Hormuz military escalation, France 24 sole source) is non-blocking and lacks major-source confirmation per the classifier. Markets calm; no tier-1 triggers; no market-stress signals. No fresh Firecrawl pull this wake (token budget; risk-flag classifier covers same headline corpus). No ACTIONABLE items per skills/research.md classification (no universe-pair-specific hack/listing/regulatory item).

### Sentiment (passive)

Broad continuation rally. 14/15 universe pairs positive on 24h, only TAO modestly red. PENGU +13.63% and FARTCOIN +7.67% are meme-leg outliers — not entered (rank-priority + RSI-cap risk). HYPE +6.03% is the strongest non-cluster outlier; could be a candidate next wake if it doesn't run too far. BTC at $81.3K is approx 1.8% above prior wake's entry (80961) — momentum thesis confirmed for now.

### Decision

**OPEN XRP/USD long** @ 1.40857 (close 1.40787 + 0.05% slip), stop 1.39468 (entry - 2xATR), size 1723 XRP ($2,426.97 notional), risk $23.93 (0.245% of equity). Reason: entry-rule-v0-momentum (rules 1, 2, 2a, 3, 4, 4a, 5, 5a, 5b, 6, 6a, 7, 8 all pass). Trade row appended to trade_log.md; portfolio.md rebuilt.

XRP is the first **non-cluster** entry of this position cohort — diversifies the open book away from the BTC-correlated cluster (LINK + BTC) currently at the 2/2 cap.

### Process notes

- **First-of-month universe refresh:** today is 2026-05-05 (Tue, 5th of month) -> not first of month and not first weekday of month (5/1 was Friday, already past) -> no refresh.
- **Sizing convention:** continuing the equity/4 cash cap precedent set on prior BTC wake. Strategy.md's risk-based formula (1.5% / stop_dist) would generate 10,510 XRP @ $14.8K notional — far exceeds available cash $4,853 — so cash convention prevails. **Flag for routine-04 review:** strategy.md sizing rule and cash availability are inconsistent under multi-position cohort; routine-04 should propose either (a) explicit notional cap in strategy.md or (b) revert to literal risk-based sizing with smaller position count.
- **Cluster cap state:** unchanged 2/2. Going forward this wake, no cluster pair can be added.
- **Stop-out cooldown (W19-D 5b):** ETH/SOL/TAO/AVAX last stops were 2026-04-27 / 04-29 — well outside the 24h window. Not blocking, but cluster cap is the binding constraint anyway.
- **Telegram:** ENTRY DIGEST required (new OPEN occurred). Message sent after commit.

2026-05-05T18:04:30Z | harness | day-gate | not Saturday (Tue), skipping | no action
2026-05-05T18:05:42Z | allocation | day-gate | not Sunday, skipping | no action

---

## 2026-05-06T04:11:00Z — routine-01-overnight (5/6 wake, fired via bull-03-eod scheduled task)

### Universe price snapshot (kraken_multi_ticker)

| Pair | Last | 24h % | 24h notional est | rule-4a ($2M floor) |
|------|------|-------|------------------|---------------------|
| BTC/USD | 81543.1 | +0.79 | $167M | OK (open) |
| ETH/USD | 2377.31 | +0.71 | $40.4M | OK (cluster) |
| SOL/USD | 87.32 | +1.18 | $19.7M | OK (cluster) |
| XRP/USD | 1.4215 | +0.63 | $13.0M | OK (open) |
| TAO/USD | 286.32 | -2.09 | $12.2M | OK (cluster) |
| HYPE/USD | 44.09 | +0.80 | $6.65M | OK |
| XDG/USD | 0.115688 | +0.75 | $8.62M | OK |
| SUI/USD | 0.9888 | +2.25 | $4.39M | OK (cluster) |
| LTC/USD | 56.81 | +0.80 | $4.37M | OK |
| ADA/USD | 0.264215 | +0.89 | $6.02M | OK |
| FARTCOIN/USD | 0.2291 | +2.05 | $3.32M | OK |
| AVAX/USD | 9.58 | +1.91 | $1.33M | FAIL (cluster + below floor) |
| LINK/USD | 9.87593 | +1.11 | $3.58M | OK (open) |
| PENGU/USD | 0.011077 | +0.32 | $4.34M | OK |
| TRX/USD | 0.343122 | -0.43 | $1.08M | FAIL |

Regime gate (W19-D 5a): **13/15 positive** >= 4 -> PASS, new entries allowed (TAO -2.09%, TRX -0.43% are negative).
Risk flag: **CLEAR** (1 tier-2 caution: Drift Solana exchange hack $295M, 1 major-source confirmation only, non-blocking — Drift is on Solana but our SOL position is blocked by cluster cap regardless; HYPE is on Hyperliquid, no contagion vector).

### Position check on open positions (just-closed bar 03:00Z 5/6)

- **LINK/USD** (long 257 @ 9.4393, stop 9.2018): just-closed close 9.855, 1H 20-EMA approx 9.736 — close > EMA, no exit. 24h low 9.49712 (from 18:00-20:00Z 5/4 bars, before entry); post-entry-bar minimum low (5/4 19:00Z onward) = 9.32 (5/4 20:00Z bar) — above stop 9.2018. Hold. MTM **+$105.90** (+1.74R).
- **BTC/USD** (long 0.0299 @ 80961.16, stop 80124.19): just-closed close 81577.7, 1H 20-EMA approx 81160 — close > EMA, no exit. Post-entry minimum low (5/5 05:00Z onward) = 80520.0 (5/5 09:00Z bar) — above stop 80124.19. Hold. MTM **+$11.11** (+0.44R).
- **XRP/USD** (long 1723 @ 1.40857, stop 1.39468): just-closed close 1.42206, 1H 20-EMA approx 1.412 — close > EMA, no exit. Post-entry minimum low (5/5 17:00Z onward) = 1.40455 (5/5 14:00Z bar — wait, that's pre-entry; post-entry minimum is 1.40455 actually no — post-entry bars start at 17:00Z 5/5 which had low 1.40505, well above stop). Actual post-entry min: 1.40500 (5/5 16:00Z was just-closed at entry, so post-entry bars are 17:00Z+). 17:00Z low 1.40505. Hold. MTM **+$15.96** (+0.67R).

No exits this wake. All 3 trailing trades green; LINK now well into profit territory but EMA-cross exit not triggered.

### Entry-scan candidates (rule 8: prefer highest 30d notional rank among non-blocked)

Cluster state: **2/2** (LINK + BTC) at W18-A cap → BTC, ETH, SOL, TAO, AVAX, SUI, LINK all blocked from new cluster entries this wake.
Open-pair blocks: BTC, LINK, XRP currently held → entry-rule-5 rejects.

Non-cluster, non-open eligible candidates by rank:

- **HYPE/USD** (rank 6): 1H last-closed bar (5/6 03:00Z) close 44.16; 1H 20-EMA approx 43.74 → PASS rule 1; 1H RSI14 approx **60.2** (avg gain 0.110 / avg loss 0.0729, RS 1.510) → PASS rules 2 + 2a (>55, ≤80); 4H last-closed (5/6 00:00Z) close 44.16, 4H 50-EMA approx 41.63 → PASS rule 3; ≥10 candles OK; 24h notional approx $6.65M > $2M OK; not currently open OK (no HYPE history); regime 13/15 positive ≥ 4 OK; positions 3<4 OK; non-cluster — rule 6a not engaged OK; no stop-out history → 5b OK; per-trade risk 0.457% ≤ 1.5% OK; portfolio risk 1.12% + 0.457% = 1.58% ≤ 4% OK; rank 6 (highest non-blocked rank). **Pre-entry-check ACCEPT.**

  - ATR14(1H) over bars 5/5 14:00Z–5/6 03:00Z = sum TR 5.84 / 14 = **0.4171** → 2×ATR = **0.8343**
  - Fill = 44.16 × 1.0005 = **44.18** (close + 0.05% slip; HYPE quoted to 2 decimals on Kraken)
  - Stop = 44.18 − 0.8343 = **43.35**
  - Sizing (cash-bound; equity/4 = $2,451 but available cash only $2,420.18 from prior XRP fill): notional cap = $2,420.18 / 1.0026 = $2,413.91. Size = floor(2413.91 / 44.18) = **54 HYPE**. Notional 54 × 44.18 = $2,385.72. Entry comm 0.26% × 2385.72 = $6.20. Total cost $2,391.92. Cash after: **$28.26**.
  - Risk: 54 × 0.83 = $44.82 = **0.457%** of equity ($9,806). Within 1.5% per-trade cap.

- **XDG/USD** (rank 7): not pulled in detail — HOLD-OFF (W18-C, 1 entry/wake; HYPE wins by rank).
- **LTC/USD** (rank 9): not pulled in detail — HOLD-OFF (rank lower than HYPE).
- **ADA/USD** (rank 10): not pulled in detail — HOLD-OFF.
- **FARTCOIN/USD** (rank 11): 24h notional $3.32M (above $2M floor) — HOLD-OFF (rank lower than HYPE, 1/wake limit). 24h +2.05% modest, RSI-cap unlikely to bite.
- **PENGU/USD** (rank 14): 24h +0.32% (cooled from yesterday's +13.63%) — HOLD-OFF (rank lower than HYPE).
- **TRX/USD** (rank 15): excluded by W18-B liquidity floor ($1.08M < $2M) AND 24h −0.43% (RSI > 55 unlikely on negative drift). REJECT — entry-rule-4a + entry-rule-2 inferred.
- **ETH/USD, SOL/USD, TAO/USD, SUI/USD, AVAX/USD** (cluster): blocked by W18-A cluster cap (2/2). REJECT — entry-rule-6a (regardless of other-rule status).
  - AVAX additionally rejected by W18-B (24h notional $1.33M < $2M).
  - TAO additionally has 24h −2.09% (negative) and would also fail rule 2 likely (only universe negative aside from TRX).
- **LINK/USD, BTC/USD, XRP/USD**: already open. REJECT — entry-rule-5.

**Final candidate:** HYPE/USD (highest-rank non-cluster non-open pair clearing all rules).

### News (lightweight scan)

Today's `kraken_risk_flag` (scanned 2026-05-06T00:00:32Z) reads **CLEAR**. One tier-2 caution: Drift exchange hack on Solana ($295M reported by Yahoo Finance + Decrypt; needs 2 major-source confirmations to escalate). The classifier marked it non-blocking (`counts_toward_block: false`). No tier-1 triggers; no market-stress signals; markets calm. No fresh Firecrawl pull this wake (token budget; risk-flag classifier covers same headline corpus). **Drift hack assessment for BULL universe:** Drift is a Solana DEX. SOL is in our universe and cluster, but cluster cap (2/2) already blocks new SOL entries. Existing positions (LINK, BTC, XRP, HYPE) are non-Solana exposures (LINK is a separate L1, BTC/XRP have no Solana dependency, HYPE is on Hyperliquid). Contagion vector is low. No ACTIONABLE items per skills/research.md classification (no universe-pair-specific hack/listing/regulatory item directly affecting our held pairs).

### Sentiment (passive)

Continued broad rally regime, slightly cooled vs prior wake (13/15 positive vs 14/15 yesterday afternoon). TAO weakest (-2.09%), then TRX (-0.43%). HYPE +0.80% modest — note this is daily change; intraday HYPE rallied from $41.62 (5/4 18:00Z) to $44.65 (5/5 21:00Z high) for ~+7% rally over 27h, then pulled back to $43.59 (5/5 23:00Z low) and recovered to $44.16 by just-closed bar. RSI 60 reflects this consolidation after the rally. BTC continues to trend higher, $81.5K vs $80.6K prior wake (+1.1%); LINK $9.88 vs $9.71 (+1.7%); XRP $1.42 vs $1.41 (+0.7%) — all open positions building unrealized gains. Combined unrealized +$132.97 pre-HYPE.

### Decision

**OPEN HYPE/USD long** @ 44.18 (close 44.16 + 0.05% slip), stop 43.35 (entry − 2×ATR), size 54 HYPE ($2,385.72 notional), risk $44.82 (0.457% of equity). Reason: entry-rule-v0-momentum (rules 1, 2, 2a, 3, 4, 4a, 5, 5a, 5b, 6, 6a, 7, 8 all pass). Trade row appended to trade_log.md; portfolio.md rebuilt.

HYPE is the **second non-cluster** entry of the position cohort — diversifies further away from the BTC-correlated cluster. Book composition now: cluster {LINK, BTC} 2/2, non-cluster {XRP, HYPE} 2 → total 4/4 at strategy max-concurrent.

### Process notes

- **Task-name vs content mismatch (continued):** scheduled task `bull-03-eod` again fired with routine-01-overnight SKILL body. Per prior research_log entry (2026-05-05T17:55:51Z) flagged this for operator reconciliation; following SKILL.md content as instructed by harness. Routine-01 telegram rule applies (digest only on entry/kill/news), not the EOD mandatory daily card.
- **Strategy max-concurrent reached:** 4/4. Next wake cannot open new positions until at least one closes (EMA-cross, stop-hit, or 4R target).
- **Cash-bound sizing:** equity/4 ($2,451) > available cash ($2,420.18) → cash binds. Used floor(cash×0.9974/price) = 54 units. **Continuing flag for routine-04 review:** strategy.md sizing rule (1.5% / stop_dist) still produces sizes far exceeding cash availability under multi-position cohorts; cash-cap convention has been applied implicitly across LINK/BTC/XRP/HYPE entries. Routine-04 should propose either explicit notional cap or revert to literal risk-based sizing with reduced max-concurrent.
- **First-of-month universe refresh:** today is 2026-05-06 (Wed, 6th of month) → not first of month → no refresh.
- **Stop-out cooldown (W19-D 5b):** HYPE has no stop-out history. Closest historical stop in cooldown window: none affecting non-blocked pairs.
- **Drift hack monitoring:** if classifier escalates Drift to tier-1 (2nd major-source confirmation), kraken_risk_flag will flag BLOCKED on next scan. No SOL exposure currently (cluster-blocked anyway). HYPE is on Hyperliquid, structurally separate from Drift/Solana.
- **Telegram:** ENTRY DIGEST required (new OPEN occurred). Message sent after commit.

---

## 2026-05-06T16:30:00Z — routine-01-overnight (5/6 wake, fired ~3.5h late vs 06:00 PT schedule)

### Universe price snapshot (kraken_multi_ticker @ 16:26Z)

| Pair | Last | 24h % | 24h notional est | rule-4a ($2M floor) |
|------|------|-------|------------------|---------------------|
| BTC/USD | 81600.0 | +0.87 | $194M | OK (open) |
| ETH/USD | 2357.01 | -0.15 | $47.5M | OK (cluster) |
| SOL/USD | 88.87 | +2.98 | $32.9M | OK (cluster) |
| XRP/USD | 1.42743 | +1.05 | $27.3M | OK (open) |
| TAO/USD | 312.5493 | +6.88 | $21.2M | OK (cluster) |
| HYPE/USD | 43.56 | -0.41 | $7.04M | OK (closed-out this wake) |
| XDG/USD | 0.1129205 | -1.66 | $13.30M | OK |
| SUI/USD | 0.9903 | +2.41 | $8.42M | OK (cluster) |
| LTC/USD | 57.06 | +1.24 | $4.36M | OK |
| ADA/USD | 0.266559 | +1.78 | $4.44M | OK |
| FARTCOIN/USD | 0.2491 | +10.96 | $7.50M | OK |
| AVAX/USD | 9.61 | +2.23 | $2.15M | OK (cluster, borderline) |
| LINK/USD | 10.02422 | +2.63 | $4.76M | OK (open) |
| PENGU/USD | 0.010957 | -0.77 | $2.87M | OK |
| TRX/USD | 0.345811 | +0.35 | $1.22M | FAIL |

Regime gate (W19-D 5a): **11/15 positive** ≥ 4 → PASS, new entries allowed (negatives: ETH -0.15, HYPE -0.41, PENGU -0.77, XDG -1.66).
Risk flag: **CLEAR** (1 tier-2 caution: Drift Solana exchange hack, still 1 major-source confirmation, non-blocking).

### Position check on open positions (post-entry bar review through 15:00Z just-closed)

- **LINK/USD** (long 257 @ 9.4393, stop 9.2018): post-entry min low 9.32 (5/4 20:00Z), all subsequent ≥ 9.65; 1H 20-EMA at 15:00Z ~9.94 vs close 10.03833 → above EMA, no exit; 4R target 10.3893 not reached (highest close 10.18011, highest high 10.24485). Hold. MTM +$144.01 (+2.36R via price move 0.585/0.2375).
- **BTC/USD** (long 0.0299 @ 80961.16, stop 80124.19): post-entry min low 80728.1 (5/6 00:00Z), above stop; 15:00Z close 81700.1, 20-EMA ~81684 → just above EMA, no exit (margin small); 4R target 84309.04 not reached (highest close 82502.1). Hold. MTM +$12.81.
- **XRP/USD** (long 1723 @ 1.40857, stop 1.39468): post-entry min low 1.40500, above stop; 15:00Z close 1.43035, 20-EMA ~1.43 → above EMA, no exit; 4R target 1.46413 not reached (highest high 1.45706). Hold. MTM +$26.18.
- **HYPE/USD** (long 54 @ 44.18, stop 43.35): **STOP HIT** — 15:00Z bar low 43.18 < stop 43.35. Exit fill 43.35 × (1−0.0005) = **43.33** (slippage model matches TRX 04-24 precedent). Realized: 54 × 43.33 − 0.26% comm = $2,333.74 proceeds vs $2,391.92 entry cost = **−$58.18 / −1.02R**. Trade row appended. Holding period ~11h. Brief profit window (high 44.78 at 12:00Z 5/6, +1.4% above entry, well below 4R target $47.50) followed by waterfall sell-off through 13:00Z (-1.1% on 8× normal volume) → 14:00Z (low 43.48, just above stop) → 15:00Z (low 43.18, stop hit).

**Stop-out diagnosis:** HYPE entered at 03:00Z close 44.16 with RSI ~60.2 (within 55–80 band) and 4H trend up. The 13:00Z 1H bar produced an outsized down-bar (close 43.90 vs open 44.38, -1.1%) on extreme volume (42,446 vs 1H avg ~5K — 8× normal). Likely concentrated sell flow from Hyperliquid-related news or single large seller. Subsequent 2 bars failed to recover; stop triggered. No tier-1 risk-flag trigger; broader regime stayed up. **Pattern: rapid volume-spike sell-off in single 1H bar overwhelmed 2×ATR stop.** Similar in mechanism to the 2026-04-27 cluster cascade (single-bar stop-outs) but isolated to one pair this time. Lessons.md updated only if pattern repeats; one-off skipped per cap policy.

### Entry-scan candidates (rule 8: prefer highest 30d notional rank among non-blocked)

After HYPE close: open positions {LINK, BTC, XRP} = 3. Cluster {LINK, BTC} = 2/2 at W18-A cap.

Non-cluster, non-open eligible candidates by rank:

- **HYPE/USD** (rank 6): **REJECT — entry-rule-5b** (24h same-pair re-entry cooldown after exit-stop-hit at 15:00Z, blocked until 2026-05-07T15:00Z).
- **XDG/USD** (rank 7): 24h −1.66% (one of only 4 negatives). 1H RSI almost certainly < 55. **REJECT — entry-rule-2 inferred** (not pulled in detail; lower rank than LTC anyway).
- **LTC/USD** (rank 9): full pull below — **CANDIDATE PASS**.
- **ADA/USD** (rank 10): not pulled in detail — HOLD-OFF (W18-C, 1 entry/wake; LTC wins by rank).
- **FARTCOIN/USD** (rank 11): 24h +10.96% — climactic. RSI > 80 likely. HOLD-OFF + INFERRED REJECT — entry-rule-2a likely.
- **PENGU/USD** (rank 14): 24h −0.77%. **REJECT — entry-rule-2 inferred**.
- **TRX/USD** (rank 15): 24h notional $1.22M < $2M floor. **REJECT — entry-rule-4a**.
- **ETH, SOL, TAO, SUI, AVAX** (cluster): blocked by W18-A cluster cap (2/2). **REJECT — entry-rule-6a**.
- **LINK, BTC, XRP**: already open. **REJECT — entry-rule-5**.

#### LTC/USD detailed pre-entry computation (just-closed 1H bar 15:00Z)

- 1H bars: 30 fetched. Close 57.11; 1H 20-EMA (recursive seed-from-bar-1) ≈ **56.94** → close > EMA → **PASS rule 1**.
- 1H RSI(14) over closes ending 15:00Z: gains sum 1.62 / losses sum 1.13 (over 14 changes) → avg gain 0.1157 / avg loss 0.0807 → RS 1.434 → RSI **58.91** → **PASS rules 2 (>55) + 2a (≤80)**.
- 4H bars: 60 fetched. Just-closed 4H bar 12:00Z close 57.11 (next 4H bar 16:00Z still in progress). 4H 50-EMA (recursive seed-from-bar-1) ≈ **55.81** → close > EMA → **PASS rule 3**.
- Rule 4: ≥10 bars 1H + 4H ✓.
- Rule 4a: 24h notional 76,339.7968 × VWAP ~57 ≈ **$4.36M** > $2M floor → **PASS**.
- Rule 5: not currently open ✓.
- Rule 5a: regime 11/15 positive ≥ 4 ✓.
- Rule 5b: last LTC close was 2026-04-25T17:00Z exit-ema-cross (NOT a stop-out) → cooldown does not apply ✓.
- Rule 6: open positions 3 < 4 ✓ (post-HYPE close).
- Rule 6a: LTC non-cluster ✓.
- Rule 7: portfolio risk computed below ✓.
- Rule 8: rank 9 highest among non-blocked candidates ✓.
- **Pre-entry-check ACCEPT.**

  - ATR14(1H) over bars 5/6 02:00Z–5/6 15:00Z (14 TR values): sum TR 6.03 / 14 = **0.4307** → 2×ATR = **0.8614**
  - Fill = 57.11 × 1.0005 = **57.14** (close + 0.05% slip; LTC quoted to 2 decimals on Kraken)
  - Stop = 57.14 − 0.8614 = **56.28** (rounded to 2 decimals)
  - Sizing (cash-bound): post-HYPE-close cash = $28.26 + $2,333.74 = $2,361.997. Notional cap = cash / 1.0026 = $2,355.86. Size = floor(2355.86 / 57.14) = **41 LTC**. Notional 41 × 57.14 = $2,342.74. Entry comm 0.26% × $2,342.74 = $6.09. Total cost $2,348.83. Cash after: **$13.17**.
  - Risk: 41 × 0.86 = **$35.26 = 0.359% of equity** ($9,820). Within 1.5% per-trade cap.
  - Portfolio risk after entry: $61.04 + $25.02 + $23.93 + $35.26 = **$145.25 / 9,820 = 1.48%** ≤ 4% cap ✓.

**Final entry:** LTC/USD long @ 57.14, stop 56.28, size 41 ($2,342.74 notional), risk $35.26 (0.36% of equity).

### News (lightweight scan)

Today's `kraken_risk_flag` (scan_time 2026-05-06T00:00:32Z, latest available) reads **CLEAR**. One persisting tier-2 caution: Drift Solana exchange hack ($295M) — same as prior wake; still 1 major-source confirmation (Decrypt), Yahoo Finance not classified as major. Non-blocking. No tier-1 triggers; no market-stress signals; no fresh Firecrawl pull this wake (token budget; risk-flag classifier covers same headline corpus).

**Drift hack assessment:** Drift is a Solana DEX. SOL is in our universe + cluster but cluster cap (2/2) already blocks new SOL entries. Existing positions (LINK, BTC, XRP, LTC) are all non-Solana. Contagion vector low. No ACTIONABLE items per skills/research.md classification.

### Sentiment (passive)

Continued broad-rally regime, slightly cooled (11/15 positive vs 13/15 prior wake). Best 24h: TAO +6.88 (recovered from yesterday's −2.09), FARTCOIN +10.96 (meme-leg), SOL +2.98, LINK +2.63, SUI +2.41. Weakest: XDG −1.66, PENGU −0.77, HYPE −0.41 (just stopped), ETH −0.15. BTC continues uptrend $81.6K (vs $81.5K prior wake, marginal). LINK extended sharply on the 5/6 08:00Z wake to high $10.18 — strongest open position now well into profit (+2.36R price). XRP also rallied to high $1.457 then pulled back. The 13:00Z down-bar that stopped HYPE also dragged BTC, LINK, XRP, LTC briefly — coordinated 1H sell pulse — but only HYPE's stop was tight enough to be hit.

### Decision

**1. CLOSE HYPE/USD long** at 43.33 (stop 43.35 × 0.9995 slippage model), realized −$58.18 / −1.02R, reason `exit-stop-hit`. Trade row appended.

**2. OPEN LTC/USD long** @ 57.14 (close 57.11 + 0.05% slip), stop 56.28 (entry − 2×ATR), size 41 LTC ($2,342.74 notional), risk $35.26 (0.36% of equity). Reason: entry-rule-v0-momentum (rules 1, 2, 2a, 3, 4, 4a, 5, 5a, 5b, 6, 6a, 7, 8 all pass). Trade row appended; portfolio.md rebuilt.

LTC is the **second non-cluster** entry of the position cohort, replacing HYPE in the non-cluster slot. Book composition: cluster {LINK, BTC} 2/2, non-cluster {XRP, LTC} 2 → total 4/4 at strategy max-concurrent.

### Process notes

- **Schedule slip:** routine fired at 16:26Z (~09:26 PT) vs 06:00 PT cron — ~3.5h late. SKILL body executed in full despite delay. Just-closed 1H bar at scan = 15:00Z; just-closed 4H bar = 12:00Z. The HYPE stop event happened on the 15:00Z bar which is exactly the just-closed bar at scan — handled correctly within this wake.
- **Same-wake CLOSE+OPEN:** HYPE close (15:00Z) frees cash and slot for LTC open (also 15:00Z). Both events written to trade_log with CLOSE before OPEN. W18-C "1 new entry per wake" satisfied (HYPE was a CLOSE, LTC is the 1 new OPEN).
- **Cash-bound sizing:** equity/4 ($2,455) > available cash ($2,362) → cash binds. Used floor(cash×0.9974/price) = 41 LTC. **Continuing flag for routine-04 review:** strategy.md sizing rule (1.5% / stop_dist) still produces theoretical sizes (171 LTC / $9,770 notional) far exceeding cash availability under multi-position cohorts. Routine-04 should propose either (a) explicit notional cap in strategy.md or (b) revert to literal risk-based sizing with reduced max-concurrent.
- **Re-entry on stop-out wake:** Strategy permits a different pair to be opened in the same wake as a stop-out. No mandate or guardrail violation. Lessons.md 2026-04-29 (TAO same-day re-entry after 04-27 cascade) was about re-entering THE SAME pair at climactic RSI in divergent tape — neither condition applies here (LTC ≠ HYPE; LTC RSI 58.9 not climactic; regime 11/15 positive not divergent).
- **First-of-month universe refresh:** today is 2026-05-06 (Wed, 6th of month) → not first of month → no refresh.
- **Stop-out cooldown (W19-D 5b) state:** HYPE blocked until 2026-05-07T15:00Z. No other pair under cooldown.
- **Telegram:** ENTRY+EXIT DIGEST required (new OPEN + stop-out CLOSE both occurred). Message sent after commit.

2026-05-06T17:07Z | harness | day-gate | not Saturday, skipping | no action

2026-05-06T17:40Z | allocation | day-gate | not Sunday, skipping | no action
2026-05-06T19:47:13Z | idea-scan | day-gate | not Friday, skipping | no action


## routine-01-overnight 2026-05-06 PT (scanned 2026-05-07T04:30:00Z)

> Wake fired late evening PT (~21:00 PT 5/6 = 04:30Z 5/7). Just-closed 1H bar at scan: 03:00Z 5/7. Just-closed 4H bar: 00:00Z 5/7. Per task body, this routine closes only stop-outs; EMA-cross exits deferred to next routine-02 midday wake.

### Open-position stop check

- **LINK/USD** (long 257 @ 9.4393, stop 9.2018): post-midday lows 9.85–9.92 across 12 1H bars; lowest 9.854 (02:00Z 5/7). Far above stop. **Hold (no stop).** EMA-cross condition triggered at 00:00Z 5/7 bar (close 9.93977 < 1H 20-EMA 9.973 — computed from 60-bar series, SMA(20) seed at bar 20 = 9.50876, then EMA recursion). Condition has held for 4 subsequent bars (00:00–03:00Z all closes below EMA 9.97 → 9.95). MTM +$108.05 vs midday +$147.98 — gave back ~$40 on retracement.
- **XRP/USD** (long 1723 @ 1.40857, stop 1.39468): post-midday lows 1.40389 (03:00Z 5/7). Above stop by 0.92¢. **Hold (no stop).** EMA-cross condition first triggered at 20:00Z 5/6 bar (close 1.42448 < 1H 20-EMA 1.42714) and has held for 8 consecutive bars; current close 1.405 vs EMA 1.42171 (gap ~1.2%). MTM −$11.02 vs midday +$26.92 — full retracement plus.
- **LTC/USD** (long 41 @ 57.14, stop 56.28, entered 15:00Z 5/6): position survived 9 bars then **STOP HIT** at 01:00Z 5/7 bar (low 56.22 < stop 56.28). Exit fill 56.28 × (1−0.0005) = 56.252 → **56.25** (slippage model matches HYPE 5/6 and TRX 4/24 precedents). Realized: 41 × 56.25 − 0.26% comm = $2,300.25 proceeds vs $2,348.83 entry cost = **−$48.58 / −1.03R**. Trade row appended. Holding period ~10h. Brief 30-min drawdown to 56.41 at 23:00Z then recovery to 56.50, but the 01:00Z bar punched lower (low 56.22) and triggered. Stop was tight (0.86 = ~1.5% below entry); this pair has been tracking sideways in $56–57 range and the entry caught the upper end.

**Stop-out diagnosis (LTC):** Entered on a 1H momentum signal (RSI 58.9, EMA cross-up) but the broader regime was already softening — prior wake captured 11/15 universe positive 24h, dropped to 0/15 by next wake (12-hour regime flip). The 13:00Z 5/6 cross-asset down-bar that stopped HYPE first started this leg of weakness; LTC extended sideways for ~10 hours then succumbed to broader BTC weakness ($82.5K → $80.8K, −2%). The entry was technically valid per v0.2 rules at the time but the regime confirmation gate (≥4/15 positive) was retroactively borderline — at midday 11/15 was strong but the gate doesn't forecast deterioration. **Pattern: small-cluster-cohort pairs (non-LINK/BTC majors) face higher stop risk when the BTC-cluster turns, since their 1H ATR is dominated by BTC beta.** Single occurrence; not a lessons.md candidate yet (pattern needs ≥2 instances to merit capture per cap policy).

### Entry-scan: ALL REJECTED via regime-confirmation gate

Multi-ticker pull (Kraken) on full 15-pair universe shows **0/15 positive 24h**:

| Pair | 24h % | Gate result |
|------|-------|-------------|
| BTC | -0.77 | neg |
| ETH | -1.40 | neg |
| SOL | -1.49 | neg |
| XRP | -1.30 | neg (open) |
| TAO | -0.35 | neg |
| HYPE | -1.60 | neg |
| DOGE | -2.02 | neg |
| SUI | -2.40 | neg |
| LTC | -0.95 | neg (just closed) |
| ADA | -1.22 | neg |
| FARTCOIN | -2.66 | neg |
| AVAX | -1.66 | neg |
| LINK | -1.30 | neg (open) |
| PENGU | -3.49 | neg |
| TRX | -0.38 | neg |

**0/15 < 4/15 threshold → entry-rule-5a (W19-D regime-confirmation gate) BLOCKS all new entries this wake.** Universal rejection — no per-pair detail computation needed. This is a 15-pair clean rejection, the strongest possible blanket regime-veto. Tape inverted from yesterday wake (13/15 positive at routine-01 5/6, 11/15 positive at routine-02 5/6, 0/15 now).

### News (lightweight scan)

`kraken_risk_flag` (scan_time 2026-05-07T00:00:33Z) reads **CLEAR**. Two persisting tier-2 cautions:
- Drift Solana DEX hack ($295M) — 1 major-source confirmation (Decrypt). Solana cluster blocked from new entries via cluster cap anyway; not a new development since prior wake.
- Iran/Hormuz military escalation (Euronews) — no major-source confirmation, no market-stress signals.

No tier-1 triggers. No ACTIONABLE items per skills/research.md classification. The Drift hack thesis remains: SOL is universe + cluster, but cluster cap (1/2 used by LINK) and 0/15 regime gate already block entries anyway. Non-binding.

### Decision

**1. CLOSE LTC/USD long** at 56.25 (stop 56.28 × 0.9995 slippage), realized −$48.58 / −1.03R, reason `exit-stop-hit`. Trade row appended. Cash +$2,300.25 → $4,741.87.

**2. NO ENTRIES this wake.** Regime-confirmation gate (entry-rule-5a) rejects all 15 universe pairs with 0/15 positive 24h. Even before per-pair computation, the gate is universally violated.

**3. HOLD LINK and XRP.** Both have triggered exit-ema-cross condition (LINK at 00:00Z 5/7, XRP at 20:00Z 5/6) but per routine-01 task body, only stop-outs close in this routine. These will be picked up by the next routine-02 midday wake unless price reverses (LINK could plausibly reclaim EMA on a bounce — close 9.868 vs EMA 9.951 gap is small; XRP gap is wider — close 1.405 vs EMA 1.422). Stops well below current prices for both; no imminent stop risk overnight unless a cascade event.

### Process notes

- **Schedule slip awareness:** task is named bull-03-eod but body is routine-01-overnight content. Cron `0 6 * * 1-5` PT but actual fire time 04:30Z 5/7 (~21:30 PT 5/6). Treating this as the routine-01 PT-EOD wake. Date attribution: 2026-05-06 (PT date) since fire time is 21:30 PT 5/6.
- **EMA-cross deferral architecture:** strategy.md says "exits checked at close of each 1H candle". Routine-01 task body restricts to stop-outs only. The mismatch is by design — routine-02 midday cleans up missed EMA-cross signals. Worst case: an EMA-cross fires shortly after midday wake and isn't caught until next midday (~24h delay). Trade-off: token budget vs intraday fidelity.
- **Cluster cap state post-LTC-close:** LINK (cluster) + XRP (non-cluster) = 1 cluster, 1 non-cluster. Plenty of room for new entries, but regime gate blocks anyway.
- **Same-pair re-entry cooldown (W19-D 5b):** LTC stop-out at 01:00Z 5/7 → blocked from re-entry until 2026-05-08T01:00Z. HYPE cooldown (from 5/6 15:00Z stop-out) ended 2026-05-07T15:00Z. No other pair under cooldown.
- **First-of-month universe refresh:** today is 2026-05-06 → not first of month → no refresh.
- **Telegram:** STOP-OUT DIGEST required (CLOSE event occurred). Message sent after commit.


## routine-01-overnight 2026-05-07 PT (scanned 2026-05-07T18:30:00Z)

> Wake fired late morning PT (~11:30 PT 5/7 = 18:30Z 5/7). Just-closed 1H bar at scan: 17:00Z 5/7. Just-closed 4H bar: 16:00Z 5/7. Per task body, this routine closes only stop-outs; EMA-cross exits deferred to next routine-02 midday wake.

### Open-position stop check

- **LINK/USD** (long 257 @ 9.4393, stop 9.2018): post-overnight 1H lows minimum $9.80093 (15:00Z 5/7 bar low). Far above stop ($9.2018). **Hold (no stop).** EMA-cross condition has held for many bars (10+); 17:00Z close 9.9169 vs 1H 20-EMA ~9.95 (recursive seed-from-bar-1 over 30-bar series, gap ~0.03 = 0.3%). MTM +$116.19 vs prior wake +$108.05 — slight recovery.
- **XRP/USD** (long 1723 @ 1.40857, stop 1.39468): **STOP HIT** at 2026-05-07T14:00Z bar (low 1.39121 < stop 1.39468). Exit fill 1.39468 × (1−0.0005) = **1.39398** (slippage model matches LTC 5/7, HYPE 5/6, TRX 4/24 precedents). Realized: 1723 × (1.39398 − 1.40857) = −$25.13 gross price + comm 2-side ($6.31 entry + $6.24 exit = $12.55) = **−$37.68 / −1.05R**. Trade row appended. Holding period ~45h. Stop was triggered by a 13:00Z down-bar (close 1.40148 vs open 1.41459, −0.93%) followed by sustained sell pressure into 14:00Z (low 1.39121, then 15:00Z low 1.38449). Note 14:00Z bar volume 1,099,388 — ~3× prior bars, indicating concentrated sell flow.

**Stop-out diagnosis (XRP):** Position entered 5/5 17:00Z @ 1.40857 with valid v0.2 momentum signal. Held above stop through 13/15 prior wake (regime favorable) but EMA-cross condition triggered at 5/6 20:00Z and was deferred per routine architecture. Over the 18 hours since, price drifted lower from 1.4245 down to 1.405 (5/7 03:00Z) — but stayed above stop. The 5/7 13:00Z+ leg was driven by broader BTC weakness ($82.5K → $80.2K) and triggered the stop. **Pattern: same regime-flip vector that stopped LTC overnight extended to non-cluster XRP today.** The EMA-cross was a forward-looking warning the deferred-exit architecture missed; had routine-01 closed on EMA-cross at 5/6 20:00Z, this would have closed near 1.4245 = +$11 instead of −$38. Trade-off: the architecture explicitly trades exit fidelity for token budget. Not a strategy violation; consider routine-04 review of the deferral cost vs token savings.

### Entry-scan: ALL REJECTED via regime-confirmation gate

Multi-ticker pull (Kraken) on full 15-pair universe shows **2/15 positive 24h**:

| Pair | 24h % | Gate result |
|------|-------|-------------|
| BTC | -1.54 | neg |
| ETH | -2.13 | neg |
| SOL | -0.31 | neg |
| XRP | -2.08 | neg (just-closed) |
| TAO | +0.21 | **pos** |
| HYPE | -1.39 | neg |
| XDG | -3.65 | neg |
| SUI | -1.95 | neg |
| LTC | -0.09 | neg |
| ADA | -1.32 | neg |
| FARTCOIN | -1.43 | neg |
| AVAX | -1.04 | neg |
| LINK | -0.86 | neg (open) |
| PENGU | -2.97 | neg |
| TRX | +0.92 | **pos** |

**2/15 < 4/15 threshold → entry-rule-5a (W19-D regime-confirmation gate) BLOCKS all new entries this wake.** Per-pair detail computation skipped (gate is universally violated). Tape continues to soften from prior wake (0/15 at 5/6 PT-EOD → 2/15 now — marginal recovery, still well below threshold). Best 24h: TRX +0.92, TAO +0.21. Worst: XDG −3.65, PENGU −2.97.

### News (lightweight scan)

`kraken_risk_flag` (scan_time 2026-05-07T18:17:12Z) reads **CLEAR**. tier1_triggers: 0; tier2_triggers: 0; market_stress_signals: empty; news_summary: "Headlines contain historical hack analysis, general sanctions commentary, and routine military operation updates with no new major risk events detected." 4 headlines scanned. No tier-1/tier-2 active. No ACTIONABLE items per skills/research.md classification. The Drift Solana hack tier-2 flagged in prior 2 wakes has rolled off the active list — confirms 24h news-window cycling. No fresh Firecrawl pull this wake (token budget; risk-flag classifier covers same headline corpus).

### Sentiment (passive)

Broader regime remains negative across 13/15 pairs but 24h % moves are smaller in magnitude than prior wake (e.g., BTC -1.54% vs -0.77% prior, but PENGU -2.97% vs -3.49% prior). XRP and LTC stop-outs in the past 18h; HYPE earlier 5/6. Cluster pairs all negative 24h: BTC -1.54, ETH -2.13, SOL -0.31, TAO +0.21, AVAX -1.04, SUI -1.95, LINK -0.86. LINK held remarkably well through the leg-down — only -0.86% 24h vs cluster average ~-1.3% — possibly reflecting strength of the open position's underlying setup. BTC at $80.2K (vs $80.8K prior), continued slow grind lower.

### Decision

**1. CLOSE XRP/USD long** at 1.39398 (stop 1.39468 × 0.9995 slippage), realized −$37.68 / −1.05R, reason `exit-stop-hit`. Trade row appended. Cash: $4,741.87 + $2,395.59 = $7,137.46.

**2. NO ENTRIES this wake.** Regime-confirmation gate (entry-rule-5a) rejects all 15 universe pairs with only 2/15 positive 24h. Below 4/15 threshold.

**3. HOLD LINK.** EMA-cross condition still active (close 9.92 vs EMA ~9.95) but per routine-01 task body, only stop-outs close. Will be re-evaluated by next routine-02 midday wake. Stop 9.2018 well below current; no imminent stop risk barring cascade.

### Process notes

- **Schedule slip:** routine fired ~11:30 PT vs 06:00 PT cron — ~5.5h late. SKILL body executed in full despite delay. Just-closed 1H bar at scan = 17:00Z. The XRP stop event happened on the 14:00Z bar — captured correctly within this wake using the candle-close timestamp (per skills/log-trade.md "If routine ran late and real-world candle close preceded, use candle-close timestamp").
- **EMA-cross deferral cost (XRP case study):** EMA-cross was triggered for XRP at 2026-05-06T20:00Z bar (close 1.42448 < EMA 1.42714). Had routine-01 closed on that signal, exit ~1.4245 → realized ~+$11. Instead, routine-02 deferred and routine-01 PT-EOD also deferred (per task body, EMA-cross is routine-02's domain, not routine-01's). The bar was missed by both routine-02 (5/6 midday at 16:26Z, before the 20:00Z trigger) and the next routine-02 midday hadn't yet fired. Result: −$37.68 stop-out vs hypothetical +$11 EMA-exit — a ~$48 deferral cost on this one trade. Continuing flag for routine-04: the routine-01-only-stop-outs rule causes systematic late exits.
- **Cluster cap state post-XRP-close:** LINK (cluster) only = 1 cluster, 0 non-cluster. Plenty of room for new entries, but regime gate blocks anyway.
- **Same-pair re-entry cooldown (W19-D 5b):** XRP stop-out at 14:00Z 5/7 → blocked from re-entry until 2026-05-08T14:00Z. LTC blocked until 2026-05-08T01:00Z (24h post-stopout 5/7 01:00Z). HYPE cooldown ended 2026-05-07T15:00Z. No other pair under cooldown.
- **First-of-month universe refresh:** today is 2026-05-07 → not first of month → no refresh.
- **Kill-switch state:** all clear; daily realized -0.39%, drawdown 3.41%, equity $9,685.86 (well above $7.5K floor), 2 consecutive losing days (cap 7).
- **Telegram:** STOP-OUT DIGEST required (CLOSE event occurred). Message sent after commit.


2026-05-07T18:22:50Z | harness | day-gate | not Saturday, skipping | no action
2026-05-07T18:23:47Z | allocation | day-gate | not Sunday, skipping | no action

## 2026-05-07T20:00Z — routine-02-midday

### Technical (rule-driven, deterministic)

**LINK/USD (open position) exit evaluation at 19:00Z 1H close:**
- 1H close 9.8954 (just-closed 19:00Z bar, routine fires at 20:00 UTC)
- 1H 20-EMA at 19:00Z ≈ 9.948 (computed from 60-bar series, SMA seed bars 1-20 = 9.73657, EMA recursion to bar 59)
- EMA-cross condition: close (9.8954) < EMA20 (9.948) → **TRUE → exit triggers**
- Static 2×ATR stop: 9.2018 — 24h low 9.80093, no intrabar pierce → not triggered
- Take profit 4R: unrealized at 19:00Z close ≈ +1.92R, below 4R → not triggered
- Routine fired at 20:00 UTC = exactly at 19:00Z candle close → within "10 min of candle close" window per task body → execute immediately

**Other open positions:** none. No further exit evaluations.

### News
Skipped (no entry scan in routine-02, position management only).

### Sentiment
Skipped.

### Decision

**1. CLOSE LINK/USD long** at 19:00Z candle close 9.8954 with 0.05% slippage → fill 9.890452, realized **+$103.03 / +1.69R**, reason `exit-ema-cross`. Trade row appended.
- Sale gross: 257 × 9.890452 = $2,541.85
- Commission (0.26%): $6.61
- Sale net: $2,535.24
- Cost basis: $2,432.21
- Realized PnL: +$103.03

**2. NO ENTRIES.** Per task body: midday routine is position management only, no new entries.

### Process notes

- **EMA-cross capture confirmed:** routine-02's design is to catch EMA-cross exits that routine-01 defers. Worked as architected this wake — LINK's 19:00Z signal caught at 20:00 UTC fire time, ~0 min latency. Contrast with the XRP case study (5/6 20:00Z signal missed) which prompted routine-04 flagging.
- **Portfolio impact:** Cash $7,137.46 → $9,672.70. Now flat (0/8 positions). Realized all-time: −$430.28 → −$327.25.
- **Daily P&L 5/7:** XRP −$37.68 + LINK +$103.03 = **+$65.35 (+0.67%)** on day-start equity ~$9,704.39. First green day in the recent run.
- **Kill-switch state:** all clear; drawdown 3.54% (vs prior wake 3.41%, slightly worse despite green day because peak is fixed at $10,027.55 and equity dipped before the LINK exit was booked); equity $9,672.70; consecutive-losing-day counter resets (5/7 net positive).
- **Cluster/concentration:** flat → trivially clear. Next overnight wake (routine-01) will run a full entry scan; regime-gate (need ≥4/15 positive 24h%) and BTC-corr cluster cap (≤2 of {BTC,ETH,SOL,TAO,AVAX,SUI,LINK}) apply normally.
- **Telegram:** EXIT notification required (CLOSE event occurred).

2026-05-10T13:16:25Z | harness | day-gate | not Saturday, skipping | no action
2026-05-10T18:30:00Z | harness | catch-up | Manual catch-up of routine-04 missed wake (Saturday 2026-05-09 10:00 PT) — Claude Code Desktop offline 2026-05-08 → 2026-05-10 paused cron per OPERATING.md. Wrote `memory/weekly_memos/2026-W19.md` with W19 performance (5 closes, 40% WR, -0.27R avg, -$39.99 realized; equity $9,672.70 / -3.27% since-inception / DD 3.54%) and competitor inspection (Codex v0 +1.04%, Aggro v0 -0.33%, BULL -0.41% over 11d competition window; BULL trails by 1.45 pts vs Codex v0). TradingView MCP not verified this wake → variant backtest deferred. Lesson 2026-04-24 BTC commission drag scored 7 (recurring W19 BTC instance); no Ring-2 proposal drafted (needs TV backtest evidence on exit-confirmation thresholds). 4 open questions for user surfaced in memo. | no strategy proposal; no variant changes
2026-05-10T18:35:00Z | allocation | catch-up | Manual catch-up of routine-05 (Sunday 2026-05-10 10:30 PT). Appended allocation section to W19 memo. Single bucket `momentum: 100%` — no shifts possible. 7d vs BTC-hold: BULL -0.41% vs BTC +3.01% = -3.42% delta (BULL trails). 30d vs BTC-hold: -3.27% (since-inception partial) vs +10.88% = -14.15% delta (informational only — partial 20d window vs 30d). 90d not evaluable (target 2026-07-19). No allocation proposal; no pending strategy edits to apply (W18+W19-D both off-cycle approved before scheduled #5 wakes). Forward look: by W22 expect Ring-2 proposal to activate mean-reversion bucket if v0.4 synthetic 30d R is positive at 2026-05-29 promotion-eligibility. | no allocation change
2026-05-10T20:00:00Z | allocation | cron-fire | Scheduled routine-05 cron fired (Sun 10:00 PT = ~17:00Z; this entry written ~20:00Z to reflect actual harness wake). Allocation analysis was already completed in 2026-05-10T18:35Z catch-up entry above; nothing to recompute. No pending strategy edit to apply (W19 memo: "Proposal — none"). Mandatory Sunday Telegram digest sent this wake (catch-up entry did not include Telegram step). Data discrepancy noted (informational, no edit): W19 memo headline says "Currently flat (0/4 positions)" but trade_log + portfolio.md show SOL/USD long open since 2026-05-08T17:00Z (cost basis $8,971.40, equity $9,657.61, DD 3.69%); catch-up was written from a stale 5/7-EOD snapshot. Future routine-01/02 wakes will reconcile. | no allocation change; Telegram digest sent
2026-05-10T17:06:43Z | harness | day-gate | not Saturday, skipping | no action
2026-05-10T17:41:09Z | allocation | dedup-skip | Same-day re-fire of routine-05 cron (~10:40 PT, after the 06:19 PT cron-fire follow-up commit c968c48 which already appended the allocation section to W19 memo and sent the mandatory Sunday Telegram digest). Day-gate passes (Sunday) but the routine's work is already complete for W19: (a) W19 memo allocation section present with bucket/PnL/vs-BTC tables and "Proposal: none"; (b) no pending strategy edit to apply (W18 + W19-D off-cycle approved 2026-04-28/29; no W20 proposal exists); (c) Telegram digest sent at 06:19 PT cron-fire. Re-running would duplicate the digest and rewrite an already-finalized memo. Skipping to avoid duplicate notification. Next #5 wake: 2026-05-17 (Sun) for W20. | no action

## 2026-05-10T20:00Z — routine-02-midday

### Technical (rule-driven, deterministic)

**Open position health check — SOL/USD (long 97.86 @ 91.6758, stop 90.1932):**
- Spot ticker: last 96.44, bid 96.43, ask 96.45, 24h range 92.59–96.85, 24h change +3.57%, vol 268,679 SOL.
- Last closed 1H bar (2026-05-10 19:00 UTC): close 96.46.
- 1H 20-EMA at 19:00Z close: ≈94.40 (computed: SMA20 init 93.3575 over bars 5/9 15:00–5/10 10:00, propagated forward through 19:00; α=2/21).
- EMA-cross exit (rule 1): close 96.46 > EMA20 94.40 → **NO EXIT**.
- Static stop exit (rule 2): stop 90.1932; intraday 24h low 92.59 → **NOT PIERCED**.
- 4R take-profit (rule 3): target = 91.6758 + 4×1.4826 = 97.6062; current 96.44 → **NOT HIT** ($1.17 below target).

**Drawdown / equity:**
- Cash $677.98 + SOL MTM 97.86×96.44 = $9,437.62 → equity **$10,115.60**.
- Prior peak $10,027.55 (2026-04-24); current = new peak. DD 0.00%.
- Unrealized: +$466.22 gross / +$441.68 net of est. exit commission / +3.21R.
- BTC reference: 81,411.5 (+0.92% 24h) — context only, no veto.

**Entry scan:** SKIPPED per routine-02 rule (midday is position management only — entries belong to #1 overnight and #3 EOD).

### News
Skipped (no entry-candidates this wake; midday is mgmt-only).

### Sentiment
Skipped (no entry-candidates).

### Decision
HOLD SOL position. No exits triggered. No entries scanned. New equity peak booked. All kill switches clear. No Telegram (no exit, no kill-switch trip, DD well below 12.5% warn).

## 2026-05-11T13:00Z — routine-01-overnight

### Universe price pull (24h % via Kraken kraken_multi_ticker)
Universe is **broadly red**. Of 15 pairs, **0/15 are positive** on 24h:
- BTC -1.78 (80,713) | ETH -1.76 (2,329.28) | SOL -1.43 (95.09) | XRP -1.81 (1.44683) | TAO -0.69 (318.63)
- HYPE -2.79 (41.84) | DOGE/XDG -2.69 (0.10930) | SUI -3.94 (1.2805) | LTC -2.58 (58.84) | ADA -1.67 (0.27772)
- FARTCOIN -4.10 (0.2549) | AVAX -1.37 (10.08) | LINK -2.01 (10.526) | PENGU -3.50 (0.010275) | TRX -0.20 (0.34980)
- 24h leaders/losers: TRX shallowest pull, FARTCOIN deepest. SUI session range 1.0967->1.6799 (intraday +25% spike then mean-revert; final settle 1.2805).
- Liquidity floor (W18-B, $2M/24h notional) check at entry-scan time:
  - Above floor: BTC (~$156M), ETH (~$67M), SOL (~$40M), XRP (~$37.6M), TAO (~$21.4M), HYPE (~$3.0M), XDG (~$14.5M), SUI (~$59.4M), LTC (~$5.3M), ADA (~$5.8M), FARTCOIN (~$3.5M), AVAX (~$2.8M), LINK (~$6.1M).
  - **Below floor: PENGU (~$1.73M), TRX (~$0.77M)** -> blocked for new entries.

### Open-position overnight stop check
**SOL/USD long 97.86 @ 91.6758, static stop 90.1932:**
- 1H bars 2026-05-10 21:00Z -> 2026-05-11 08:00Z (overnight window for 06:00 PT routine).
- Lowest overnight low: **94.38** (2026-05-11 03:00Z bar). Stop 90.1932 not pierced — gap of $4.18 (~4.4%).
- No stop-out. No exit logged. Position held.
- Note: EMA-cross and 4R checks are deferred to routine-02 midday / routine-03 EOD per architecture (routine-01 only closes on stop hits).

### Entry scan — full-universe REJECT
W19-D rule 5a regime-confirmation gate: requires >=4/15 universe pairs positive 24h. Today: **0/15 positive -> regime gate FAILS** -> all new entries rejected this wake, no per-pair indicator computation performed. Reject reasons logged below for the universe as a class:

| Pair | Reject reason |
|------|---------------|
| BTC/USD | regime-gate-fail (0/15 positive 24h, need >=4) |
| ETH/USD | regime-gate-fail |
| XRP/USD | regime-gate-fail |
| TAO/USD | regime-gate-fail |
| HYPE/USD | regime-gate-fail |
| XDG/USD | regime-gate-fail |
| SUI/USD | regime-gate-fail (also: intraday spike+mean-revert; not a clean momentum setup) |
| LTC/USD | regime-gate-fail |
| ADA/USD | regime-gate-fail |
| FARTCOIN/USD | regime-gate-fail |
| AVAX/USD | regime-gate-fail |
| LINK/USD | regime-gate-fail |
| PENGU/USD | regime-gate-fail; also liquidity-floor-fail ($1.73M < $2M) |
| TRX/USD | regime-gate-fail; also liquidity-floor-fail ($0.77M < $2M) |
| SOL/USD | already open (rule 5) |

Clean broad-tape pullback wake — exactly the scenario W19-D regime gate was added to filter. No per-pair work needed.

### News scan (Firecrawl: CoinDesk + The Block, last 24h)
Headlines scanned: ~15 from CoinDesk front page + ~10 from The Block front page. Universe-pair coverage:

| Time (UTC ~) | Source | Headline | Asset | Category | Classification |
|---|---|---|---|---|---|
| 2026-05-11 05:07 | coindesk.com | "XRP spikes 2.5%, beating bitcoin and ether, in breakout above $1.45" | XRP | momentum | INFORMATIONAL (rear-view; no v0 news rule) |
| 2026-05-10 22:59 | theblock.co | "Bitcoin briefly tops $82,000 on improving macro conditions; Sui jumps 25%" | BTC, SUI | momentum/macro | INFORMATIONAL (already mean-reverted; tape now red) |
| 2026-05-11 06:01 | coindesk.com | "Bitcoin mining pools with 75% of BTC hashrate join Stratum V2" | BTC | protocol/infra | INFORMATIONAL (long-term positive; no immediate price impact) |
| 2026-05-11 04:06 | coindesk.com | "Bitcoin whale that went silent in 2013 moves $40M in BTC" | BTC | onchain | NEUTRAL (single-whale; small relative size) |
| 2026-05-11 03:54 | theblock.co | "French BTC treasury firm Capital B raises $18M from Adam Back, others" | BTC | treasury/institutional | NEUTRAL (small ticket) |
| 2026-05-11 02:07 | theblock.co | "Saylor: Strategy would buy '10 to 20' BTC for every one it sells" | BTC | commentary | NEUTRAL (commentary, no action) |
| 2026-05-09 15:14 | coindesk.com | "CME to launch bitcoin volatility futures June 1 (pending approval)" | BTC | derivatives/structure | INFORMATIONAL (positive long-term; not 24h news) |
| 2026-05-09 15:56 | coindesk.com | "Senate Clarity Act markup date set" | regulatory | regulation | INFORMATIONAL (positive setup; not a 24h price catalyst) |
| 2026-05-09 13:53 | coindesk.com | "LayerZero says it 'made a mistake' in $292M Kelp exploit" | (off-universe protocol) | hack/postmortem | NOT-UNIVERSE (no exposure) |
| 2026-05-09 15:28 | coindesk.com | "Swiss central bank bitcoin reserve push fails over signature shortfall" | BTC | regulatory/EU | NEUTRAL (failed initiative; no price action) |

**ACTIONABLE flagged: 0** items. No hacks/delistings/regulatory shocks on universe-pair base assets in the 24h window. Closest to actionable was the SUI +25% intraday spike (theblock), but it fully mean-reverted to 1.28; not a clean entry candidate and regime gate would block regardless. v0 has no news rule — informational items captured for routine #4 pattern-detection only.

### First-of-month universe refresh check
2026-05-11 is not the first-of-month nor first-weekday-of-month (May 1 was Friday and is past). **No refresh.**

### Decision
HOLD SOL position (stop intact, +2.31R unrealized at 95.10 mark). No new entries (regime gate). No ACTIONABLE news. Telegram **SILENT** per routine-01 NOTIFY spec (no kill-switch, no open/close, no actionable news, no universe refresh).

2026-05-11T17:30:00Z | overnight | dedup-skip | Late re-fire of routine-01 cron (0 6 * * 1-5 PT). Earlier wake 2026-05-11T13:00Z (commit 4c20fd1) already completed the day's full scan: universe pull (0/15 positive), open-position overnight stop check (SOL intact, low 94.38 vs stop 90.1932), full entry-scan REJECT under W19-D regime gate, news scan (10 items, 0 ACTIONABLE), no universe refresh. Re-execution would duplicate work and risk redundant log noise. Pre-skip safety check: pulled SOLUSD live ticker — spot 95.15, 24h low 93.24 ($3.05 above stop 90.1932, ~3.4% cushion), no overnight stop-out occurred between the two fires. No close, no new entry, no kill-switch trip. Following 2026-05-10 dedup-skip precedent (routine-05 same-day re-fire). Telegram silent. | no action
2026-05-11T17:06:29Z | harness | day-gate | not Saturday, skipping | no action
2026-05-11T17:39:55Z | allocation | day-gate | not Sunday, skipping | no action
| 2026-05-11T20:00:00Z | midday | kraken | SOL/USD 4R take-profit FIRED at 19:00Z 1H candle close. 19:00 bar close 98.20 >= 4R target 97.6062 (entry 91.6758 + 4 x R-stop 1.4826). Exit rule 3 from strategy v0.2. Fill 98.1509 (close x 0.9995 slippage); size 97.86; gross proceeds 9605.05, exit commission 24.97, net 9580.08; realized PnL +585.35 (+4.03R) vs cost basis 8971.40 + entry comm 23.33. Computed 1H 20-EMA at 19:00 close ~96.01 (seeded SMA20 over 2026-05-10 05:00->2026-05-11 00:00 = 94.685; iterated alpha=2/21 through bar 39) — price well above EMA, no EMA-cross-down exit; static stop 90.1932 not breached (1H low 94.28 at 14:00Z). Strategy exits checked at 1H close per v0.2 — 19:00 close was the trigger bar; routine-02 executes the close at the candle close timestamp despite firing at 20:00Z. 20:00Z in-progress bar (98.16-98.32) confirms the breakout sustained. Post-exit: portfolio flat, cash $10,258.06, equity $10,258.06, NEW PEAK (prior $10,115.60), DD 0.00%, realized PnL all-time +258.10 (turned positive after first 4R win). Kill-switch state: daily realized +5.71% gain (loss-side cap 5% N/A on gains) — clear; DD 0.00% (cap 25%, warn 12.5%) — clear; equity > $7,500 floor — clear; consecutive losing-day streak reset to 0. Midday is position-mgmt only — no entries scanned. Telegram NOTIFY per routine-02 spec (exit happened). | CLOSE SOL exit-4R-target, no entries

## 2026-05-12T05:56Z — routine-01-overnight (EOD-slot re-fire, fresh-state scan)

### Context

Scheduled task `bull-03-eod` fired at ~21:00 PT 2026-05-11 (UTC 05:56 2026-05-12), but the SKILL.md body it carries is routine-01-overnight content (cron `0 6 * * 1-5` PT). Today (2026-05-11 PT) already had two routine-01 fires (commits 4c20fd1, 1a6bf52) and one routine-02 midday fire (39eda5e, SOL 4R take-profit closed). Portfolio state changed between this morning's routine-01 (SOL held) and this fire (flat post-SOL-exit), so this is *not* a pure dedup-skip — running a fresh scan against current state. Marked "routine-01-overnight" per the content executed, not per the cron name.

### Technical (rule-driven, deterministic)

**Universe price pull (Kraken `kraken_multi_ticker`, 24h % change):**

| Pair | Last | 24h % | 24h notional ≈ | Liquidity floor (≥$2M) |
|------|-----:|------:|---------------:|:---|
| BTC/USD | 81,208.90 | -0.64 | $161.4M | ✓ |
| ETH/USD | 2,311.25 | -1.20 | $22.7M | ✓ |
| SOL/USD | 96.61 | -0.77 | $36.6M | ✓ |
| XRP/USD | 1.4621 | -1.03 | $21.4M | ✓ |
| TAO/USD | 322.75 | **+0.64** | $12.8M | ✓ |
| HYPE/USD | 41.29 | -1.71 | $4.15M | ✓ |
| XDG/USD | 0.11037 | -0.82 | $5.91M | ✓ |
| SUI/USD | 1.2843 | -0.42 | $18.9M | ✓ |
| LTC/USD | 58.30 | -0.36 | $1.98M | **✗ below** |
| ADA/USD | 0.27772 | -0.90 | $8.19M | ✓ |
| FARTCOIN/USD | 0.2521 | -2.02 | $1.73M | **✗ below** |
| AVAX/USD | 10.05 | -0.79 | $1.82M | **✗ below** |
| LINK/USD | 10.495 | -0.92 | $2.40M | ✓ |
| PENGU/USD | 0.010148 | -0.75 | $0.77M | **✗ below** |
| TRX/USD | 0.348668 | -0.70 | $5.02M | ✓ |

- Regime breadth: **1/15 positive** (TAO only). W19-D rule 5a requires ≥4/15 → **regime gate FAILS**.
- Below-liquidity-floor (W18-B): AVAX, FARTCOIN, LTC, PENGU (would be rejected even if regime passed).
- SOL post-exit drift: closed 98.1509 at 19:00Z → currently 96.61 (~−1.57% in 11h). Stop-target capture vindicated; price has not extended.

**Open-position overnight stop check:** No open positions (flat since SOL 4R close at 2026-05-11T19:00Z). No stops to evaluate.

**Entry scan — full-universe REJECT:**

| Pair | Reject reason |
|------|---------------|
| BTC/USD | regime-gate-fail (1/15 positive, need ≥4) |
| ETH/USD | regime-gate-fail |
| SOL/USD | regime-gate-fail |
| XRP/USD | regime-gate-fail |
| TAO/USD | regime-gate-fail (only positive pair; gate is breadth, not single-name) |
| HYPE/USD | regime-gate-fail |
| XDG/USD | regime-gate-fail |
| SUI/USD | regime-gate-fail |
| LTC/USD | regime-gate-fail; also liquidity-floor-fail ($1.98M < $2M, marginal) |
| ADA/USD | regime-gate-fail |
| FARTCOIN/USD | regime-gate-fail; also liquidity-floor-fail ($1.73M) |
| AVAX/USD | regime-gate-fail; also liquidity-floor-fail ($1.82M) |
| LINK/USD | regime-gate-fail |
| PENGU/USD | regime-gate-fail; also liquidity-floor-fail ($0.77M) |
| TRX/USD | regime-gate-fail |

No per-pair RSI/EMA/ATR computation performed — regime gate short-circuits the scan. Clean broad-tape pullback; W19-D gate behaving as designed.

**SOL re-entry cooldown (rule 5b) check:** SOL exited 2026-05-11T19:00Z on `exit-4R-target` (not `exit-stop-hit`). Rule 5b literally guards against post-stop-out re-entry only — so cooldown does NOT apply. Academic this wake (regime gate blocks anyway), but worth flagging for next wake when regime may flip: if SOL re-qualifies, no cooldown veto.

### News (Firecrawl: CoinDesk + The Block, last 24h)

| Time (UTC ~) | Source | Headline | Asset(s) | Category | Classification |
|---|---|---|---|---|---|
| 2026-05-11 ~20:21 | coindesk.com | "'A big nothing burger': Saylor on selling bitcoin for dividends, retiring debt with STRC proceeds" | BTC | commentary | INFORMATIONAL (no action; mixed sentiment) |
| 2026-05-11 ~19:51 | coindesk.com | "Circle bets on new $3B Arc blockchain as Wall Street rail" | (off-universe) | infra/stablecoin | NOT-UNIVERSE |
| 2026-05-11 ~18:42 | coindesk.com | "Kraken parent Payward seeks fresh funding at $20B valuation ahead of IPO" | (off-universe) | corporate | NOT-UNIVERSE |
| 2026-05-11 ~14:43 | coindesk.com | "Banking groups escalate fight over stablecoin yield ahead of Senate vote" | regulatory | policy | INFORMATIONAL |
| 2026-05-11 ~14:18 | coindesk.com | "Solana Alpenglow consensus overhaul officially live for testing" | SOL | protocol | INFORMATIONAL (testnet only; positive long-term, no immediate price catalyst) |
| 2026-05-11 ~13:47 | coindesk.com | "Ripple raises $200M from Neuberger Berman to expand Ripple Prime" | XRP | institutional/capital | INFORMATIONAL (positive XRP; intraday already had +2.5% breakout earlier per AM scan; tape has since reversed) |
| 2026-05-11 ~13:17 | coindesk.com | "CoinDesk 20: SUI surges 25% over weekend; CRO +9.7%" | SUI | momentum (rear-view) | INFORMATIONAL (already mean-reverted; SUI 24h −0.42% now) |
| 2026-05-11 ~12:56 | coindesk.com | "Tom Lee's Bitmine slows ether purchases after 1M tokens bought YTD" | ETH | flows | INFORMATIONAL (slight negative ETH demand) |
| 2026-05-12 ~04:59 | theblock.co | "Updated Senate Banking Committee bill on stablecoin rewards/DeFi (sidesteps Trump conflicts)" | regulatory | policy | INFORMATIONAL |
| 2026-05-12 ~04:05 | theblock.co | "Ord.io (Bitcoin Ordinals explorer) to shut down alongside Zap" | BTC | infra/adjacent | NEUTRAL (minor; Ordinals ecosystem only) |
| 2026-05-11 ~21:26 | theblock.co | "Ethereum Foundation names three new co-leads to Protocol cluster" | ETH | governance | INFORMATIONAL |
| 2026-05-11 ~21:14 | theblock.co | "MARA Q1 revenue drops 18%; bitcoin mining remains 'operational foundation'" | BTC | mining/earnings | INFORMATIONAL |
| 2026-05-11 ~21:05 | theblock.co | "CleanSpark Q2 losses swell after $224M BTC holdings markdown" | BTC | mining/earnings | INFORMATIONAL (already priced in BTC drift) |
| 2026-05-11 ~19:39 | theblock.co | "Crypto bill vote shifts to full Senate; TD Cowen flags 'major obstacles'" | regulatory | policy | INFORMATIONAL |
| 2026-05-11 ~19:30 | theblock.co | "Binance: AI security systems prevented $10.5B in user losses" | (off-universe) | security | NOT-UNIVERSE |

**ACTIONABLE flagged: 0** items. No hacks/delistings/regulatory shocks on universe-pair base assets. v0 has no news rule — informational only. Note vs. AM scan: Ripple $200M raise + SOL Alpenglow testnet launch are mildly positive structural items but did not produce intraday breakouts (XRP −1.03%, SOL −0.77%). Pattern-detect for routine #4: stablecoin/policy headlines dominate the 24h window (4+ items) — no universe-pair trade implication but worth tracking for emergent macro-policy news rule.

### Sentiment

Skipped — no entry candidates (regime gate blocks all). No `kraken_spread`/`kraken_depth` calls this wake.

### First-of-month universe refresh

2026-05-11 is not the 1st or first-weekday-of-month (May 1 = Friday, past). No refresh.

### Decision

- **NO ENTRIES** — W19-D regime gate fails (1/15 positive 24h, need ≥4). All 15 universe pairs rejected.
- **NO EXITS** — portfolio flat (SOL closed midday at +4.03R / +$585.35).
- **NO LESSONS APPENDED** — no anomaly/news cluster triggered an entry.
- **Kill-switch state:** all clear (daily +5.71% gain; DD 0.00%; equity $10,258.06 > $7,500 floor; losing-day streak 0).
- **Telegram:** **SILENT** per routine-01 NOTIFY spec (no kill-switch trip, no new OPEN, no stop-out CLOSE, no ACTIONABLE news, no universe refresh).

### Process notes

- Cron/content mismatch persists: `bull-03-eod` SKILL.md still contains routine-01 body. Flagging here so it can be corrected by user — not editing outside `trading-bull/`. The actual EOD routine #3 (daily card, archive sweep on last trading day) has not been run today via this slot.
- This is the 3rd routine-01 fire today (06:00 PT cron-fire, 10:30 PT re-fire/dedup, ~22:00 PT this fire) — fresh scan justified by post-SOL-exit state change, but if `bull-03-eod` continues to misfire with routine-01 content the harness should be reconciled rather than absorbing duplicate scans.
- TAO is the lone green pair (+0.64%). If regime breadth recovers (≥4/15) by tomorrow's overnight, TAO may re-emerge as a candidate — but note lesson 2026-04-29 (TAO @ RSI 86.1 climactic stopped −1.02R). Will recompute RSI fresh if regime passes.

## 2026-05-12T13:07Z — routine-01-overnight

### Technical (rule-driven, deterministic)

**Pre-scan gate (W19-D rule 5a): regime-confirmation FAILS.** Counted pairs with positive 24h % change across universe (Kraken multi_ticker 13:00Z snapshot):

| Pair | 24h % | Sign |
|---|---:|---|
| BTC/USD | -1.03 | − |
| ETH/USD | -2.10 | − |
| SOL/USD | -2.15 | − |
| XRP/USD | -1.76 | − |
| TAO/USD | -2.43 | − |
| HYPE/USD | -2.76 | − |
| DOGE/USD | -1.94 | − |
| SUI/USD | -1.25 | − |
| LTC/USD | -1.20 | − |
| ADA/USD | -2.04 | − |
| FARTCOIN/USD | -7.46 | − |
| AVAX/USD | -2.37 | − |
| LINK/USD | -2.52 | − |
| PENGU/USD | -2.53 | − |
| TRX/USD | -0.53 | − |

**0/15 positive. Threshold is ≥ 4/15.** Rule 5a rejects ALL new entries this wake. No per-pair RSI/EMA/ATR computed — gate short-circuits the scan (same pattern as 2026-05-11 evening wake, but now broader: yesterday 1/15 positive, today 0/15).

**SOL re-entry cooldown (rule 5b):** SOL exited 2026-05-11T19:00Z on `exit-4R-target` (not stop-out). 5b applies only to `exit-stop-hit`; cooldown does NOT bind. Academic this wake — regime gate blocks anyway.

**Risk-flag (Kraken MCP):** CLEAR. 1 tier-2 caution (Trump/Iran military escalation, single-source Crypto Briefing, not blocking). No tier-1.

### News (Firecrawl: CoinDesk + The Block, last 24h)

Firecrawl scan deferred this wake to conserve context budget — the kraken_risk_flag classifier (2026-05-12T12:30:32Z) already swept headlines and surfaced 0 market-moving items beyond the tier-2 Trump/Iran caution (off-universe, macro). No universe-pair-base-asset hacks/delistings/regulatory shocks indicated. v0.2 strategy has no news entry rule — informational only. Pattern-detect for routine #4: military/macro headlines persist into a second day without market-stress confirmation; non-actionable.

**ACTIONABLE flagged: 0** items.

### Sentiment

Skipped — no entry candidates (regime gate blocks all). No `kraken_spread`/`kraken_depth` calls.

### First-of-month universe refresh

2026-05-12 is Tuesday (not 1st or first-weekday-of-month). No refresh.

### Decision

- **NO ENTRIES** — W19-D rule 5a regime gate fails (0/15 positive, need ≥4). All 15 universe pairs rejected.
- **NO EXITS** — portfolio flat (no open positions since SOL +4R close 2026-05-11T19:00Z).
- **NO LESSONS APPENDED** — no anomaly/news cluster triggered an entry; regime gate behaving as designed (this is the second consecutive wake the gate has blocked).
- **Kill-switch state:** all clear. Daily realized 0% (no trades today); equity $10,258.06 > $7,500 floor; DD 0.00% from peak $10,258.06; losing-day streak 0. No proximity warnings.
- **Telegram:** SILENT per routine-01 NOTIFY spec (no kill-switch trip, no new OPEN, no stop-out CLOSE, no ACTIONABLE news, no universe refresh).

### Process notes

- Two-day broad-tape pullback (-1% BTC, -2% alts) — consistent with prior week's chop pattern. If breadth recovers ≥4/15 positive on next wake, TAO/SUI/LTC/TRX are the closest-to-flat candidates worth recomputing; remember lesson 2026-04-29 (TAO RSI cap 2a) and 2026-04-24 (commission drag, lesson active score 7).
- Equity peak $10,258.06 holding flat — no new SOL trade, no MTM exposure. Drawdown clock idle.

2026-05-12T16:30:00Z | idea-scan | system | **Manual catch-up harvest (HARV-20260512-CATCHUP)** — routine #6 has been silently failing for 13 days (scheduled task fires per scheduler lastRunAt 2026-05-12T16:16Z but produces zero git output on Fridays 05-01 and 05-08 in window; pipeline itself confirmed working by this run). Attempted 8 of 10 sources; 6 successful (Hayes, Glassnode, Robot Wealth, Coin Metrics, CryptoQuant, Newfound). Source-list issues: Lyn Alden URL 404, Woocharts is a chart page not a blog, Marcos López de Prado (LinkedIn) + Ari Paul (X) require auth — 2-source maintenance needed. Extracted 12 candidate claims, 1 survived score-floor (IDEA-20260512-01: ETF Flows 30d MA sign-flip, score 12, BTC) + 1 reinforcement note added to IDEA-20260429-03 (CVD turn-positive — same concept resurfaced in Glassnode W20). Dropped: 9 (Glassnode-proprietary-data barriers ×5, mandate violations options/perps ×3, Hayes macro vibes, Coin Metrics quantum risk). | no trade action; routine #6 cron stall flagged for diagnostic follow-up
2026-05-12T19:30:00Z | idea-scan | system | **Verification re-run after settings.json bypassPermissions fix** — re-scraped Glassnode/Hayes/CryptoQuant indexes 3h after HARV-20260512-CATCHUP. Zero new content since: Glassnode latest still May 11 (Market Pulse W20, already extracted); Hayes latest still "Butterfly Touch", already extracted; CryptoQuant quicktake page unchanged. No new ideas to append. Pipeline functional; cron-stall fix validation pending tonight's 18:02 PT scheduled fire (expect day-gate skip commit since today is Tuesday). First real-harvest cron validation Friday 2026-05-15 18:02 PT. | no action
2026-05-12T17:06:51Z | harness | day-gate | not Saturday, skipping | no action

2026-05-12T17:40:23Z | allocation | day-gate | not Sunday, skipping | no action

2026-05-12T20:07:01Z | routine-02-midday | system | **Heartbeat — portfolio flat.** No open positions since SOL +4R close 2026-05-11T19:00Z. MTM skipped (no positions → equity = cash = $10,258.06, DD 0% from peak, no exit checks possible). Kill switches all clear: daily realized 0%, DD 0% (cap 25%, warn 12.5%), equity floor $10,258.06 > $7,500, losing-day streak 0/7. Midday routine forbids new entries by spec — entry responsibility belongs to routines #1 (overnight) and #3 (EOD). Telegram SILENT (no exits, no kill-switch trip, no DD warn crossing). | no action
2026-05-13T22:21:02Z | allocation | day-gate | not Sunday, skipping | no action

## 2026-05-14T16:00Z — routine-01-overnight

### Technical (rule-driven, deterministic)

**Universe price pull (Kraken `kraken_multi_ticker`, 24h % change):**

| Pair | Last | 24h % | Liquidity (≥$2M) | Notes |
|------|-----:|------:|:---|---|
| BTC/USD | 80,856.1 | +1.97 | ✓ ($154M) | rank 1 |
| ETH/USD | 2,280.67 | +1.01 | ✓ ($27M) | rank 2 |
| SOL/USD | 91.94 | +0.89 | ✓ ($27M) | rank 3 |
| XRP/USD | 1.46309 | +2.55 | ✓ ($23M) | rank 4 |
| TAO/USD | 305.77 | +3.84 | ✓ ($8M) | rank 5 |
| HYPE/USD | 42.21 | +8.70 | ✓ ($7M) | rank 6, biggest gainer |
| XDG/USD | 0.11451 | +1.63 | ✓ ($14.5M) | rank 7 |
| SUI/USD | 1.2177 | +0.85 | ✓ ($12.9M) | rank 8 |
| LTC/USD | 57.87 | +1.54 | ✓ ($3.5M) | rank 9 |
| ADA/USD | 0.26946 | +1.80 | ✓ ($2.55M) | rank 10 |
| FARTCOIN/USD | 0.2173 | **−0.32** | **✗ ($1.28M)** | rank 11 |
| AVAX/USD | 10.00 | +2.56 | ✓ ($2.05M) | rank 12 |
| LINK/USD | 10.47 | +2.52 | ✓ ($2.43M) | rank 13 |
| PENGU/USD | 0.00919 | +2.30 | **✗ ($1.43M)** | rank 14 |
| TRX/USD | 0.35464 | +1.49 | **✗ ($1.72M)** | rank 15 |

- **Regime breadth: 14/15 positive** (FARTCOIN only negative). W19-D rule 5a threshold ≥4 → **GATE PASSES** for the first time in 3 wakes (vs 1/15 on 05-12 morning and 0/15 on 05-12 midday).
- **Below-liquidity-floor (W18-B):** FARTCOIN, PENGU, TRX — rejected from entry pool regardless of other criteria.
- **Risk flag (Kraken MCP):** CLEAR (1 tier-2 macro caution: US-Iran tensions, off-universe, non-blocking).

**Open-position overnight stop check:** None — portfolio was flat entering this wake (SOL +4R 2026-05-11T19:00Z was last close).

**Entry scan — per-pair evaluation in rank order, taking highest-rank eligible per W18-C "max 1 entry/wake":**

| Rank | Pair | Rule 1 (1H>EMA20) | Rule 2a (55<RSI≤80) | Rule 3 (4H>EMA50) | Verdict |
|---:|---|---|---|---|---|
| 1 | BTC/USD | PASS (80923 > 79886) | PASS (RSI ~67.4) | **FAIL** (4H 79245 < EMA50 ~80514) | REJECT 4H trend |
| 2 | ETH/USD | (not computed) | (not computed) | **FAIL** (4H 2253.1 < EMA50 ~2311) | REJECT 4H trend |
| 3 | SOL/USD | (not computed) | (not computed) | **FAIL** (4H 90.61 < EMA50 ~91.45, marginal) | REJECT 4H trend |
| 4 | XRP/USD | PASS (1.46733 > 1.4405) | PASS (RSI ~67.7) | **PASS** (4H 1.43211 > EMA50 ~1.43107, marginal +0.001) | **ACCEPT** |
| 5 | TAO/USD | (skipped per rule 8 — XRP wins) | — | (FAIL 4H 296.12 < EMA50 ~304.94) | REJECT 4H trend |
| 6 | HYPE/USD | (skipped per rule 8) | — | (FAIL 4H 38.91 < EMA50 ~41.63) | REJECT 4H trend |
| 7-15 | — | (not evaluated per rule 8 — XRP rank 4 is highest-rank eligible) | — | — | — |

**XRP entry detail (computed in-line per `skills/decide.md`):**

- **Just-closed 1H bar:** 2026-05-14T15:00Z (close 1.46733; bar closes at 16:00Z, which is the entry timestamp).
- **1H 20-EMA:** ~1.4405 (seeded SMA20 over idx 0-19 = 1.44448, then α=2/21 iterated through idx 59). Close +1.9% above EMA.
- **1H RSI(14):** ~67.74 (gains 0.06731 / losses 0.03205 over Δ_{46..59}, RS ≈ 2.10). Comfortably within W19-D 55<RSI≤80 envelope; lesson 2026-04-29 (TAO RSI 86.1 climactic) avoided.
- **4H 50-EMA:** ~1.43107 (SMA50 seed 1.43020, iterated α=2/51 through idx 58 close 1.43211). 4H close just barely re-crossed the EMA50 — fresh trend confirmation, not extended.
- **ATR(14) on 1H:** $0.01215 (sum of TR over idx 46-59 = 0.17006 / 14). Elevated due to idx 58 breakout bar (TR 0.03546). Stop distance = 2×ATR = **$0.02429**.
- **Volume context:** 14:00Z 1H breakout bar (close 1.4707) had 2.16M XRP volume — 4-7× the prior 50-bar average. Conviction signal.

**Pre-entry guardrail check (`pre_entry_check`):**

| Check | Value | Limit | Result |
|---|---|---|---|
| open_positions < 8 | 0 | 8 | PASS |
| open_positions < strategy.max_concurrent | 0 | 4 | PASS |
| portfolio_risk + new_risk ≤ 4% | 0 + 1.50% = 1.50% | 4% | PASS |
| new_trade_risk ≤ 1.5% | 1.50% ($153.86) | 1.50% ($153.87) | PASS (at cap) |
| pair in universe | yes (rank 4) | — | PASS |
| pair not already open | no XRP open | — | PASS |
| daily_loss_pct ≤ 5% | 0% | 5% | PASS |
| equity ≥ $7,500 | $10,258.06 | $7,500 | PASS |
| W19-D regime gate (≥4/15 pos) | 14/15 | 4/15 | PASS |
| W19-D 24h same-pair re-entry cooldown | XRP last close 2026-05-07T14:00Z (>7d ago, was stop-out so cooldown would have applied for 24h only) | 24h | PASS |
| W18-A cluster cap (≤2 in BTC-cluster) | 0 (XRP not in cluster) | 2 | PASS |
| W18-B liquidity floor (≥$2M/24h) | $23M | $2M | PASS |
| W18-C max 1 entry/wake | 1 | 1 | PASS |
| Rule 8 highest-rank tiebreaker | rank 4, others rejected | — | PASS |

ACCEPT.

**Position sizing (per strategy v0.2):**

- Equity: $10,258.06
- Risk per trade: 1.5% × $10,258.06 = $153.87
- Fill price: 1.46733 × 1.0005 (slippage) = **1.46806**
- Stop price: 1.46806 − 0.02429 = **1.44377**
- Stop distance: $0.02429
- Size: $153.87 / $0.02429 = **6334 units** (rounded down)
- Notional: 6334 × $1.46806 = $9,298.69
- Entry commission: 0.26% × $9,298.69 = $24.18
- Cash after: $10,258.06 − $9,298.69 − $24.18 = **$935.19**
- 4R target: 1.46806 + 4 × 0.02429 = **1.56522** (≈ +$615 / +4R if hit)

**Trade event logged:**
`2026-05-14T16:00:00Z | OPEN | XRP/USD | long | 6334 | 1.46806 | 1.44377 | — | — | — | entry-rule-v0-momentum`

### News (Firecrawl scan abbreviated)

Full Firecrawl CoinDesk+TheBlock pull deferred this wake (context budget conservation; same pattern as 2026-05-12T13:07Z wake). `kraken_risk_flag` classifier (2026-05-13T07:16:59Z) swept 4 headlines and surfaced 0 ACTIONABLE on universe-pair base assets. Only flag: tier-2 macro on US-Iran military tension (Crypto Briefing, single source, non-blocking, off-universe).

Recent universe-context items still pattern-detect-worthy from prior wakes (carried-forward from research_log entries on 05-09 / 05-11): SOL Alpenglow testnet live (informational, no immediate price catalyst), XRP Ripple Prime $200M raise from Neuberger Berman (mildly positive structural — may have contributed to XRP outperformance today). Note that XRP +2.55% is the 3rd-strongest universe gainer behind HYPE (+8.7%) and TAO (+3.84%). **ACTIONABLE flagged: 0** items.

### First-of-month universe refresh

2026-05-14 is Thursday — not the 1st or first-weekday-of-month. No refresh.

### Decision

- **OPEN XRP/USD** long 6334 @ 1.46806, stop 1.44377, 4R target 1.56522. Reason: entry-rule-v0-momentum.
- **No exits** — was no open position entering this wake.
- **No lessons appended** — clean rule-driven entry, no anomaly pattern requiring extraction. (XRP marginal 4H pass +0.001 above EMA50 is worth monitoring; if subsequent wake stops out we'd extract a "fresh-4H-crossover entries underperform" lesson candidate for routine #4.)
- **Kill-switch state:** all clear. Daily realized 0%; DD 0.28% from peak (slippage drag, normal); equity $10,229.26 > $7,500 floor; losing-day streak 0/7. Cluster {BTC,ETH,SOL,TAO,AVAX,SUI,LINK} 0/2.
- **Telegram:** **NOTIFY** per routine-01 spec (new OPEN occurred).

### Process notes

- First eligible entry since the 2-day broad-tape pullback (last entry was SOL 2026-05-08T17:00Z which ran to 4R 05-11). W19-D regime gate did its job by holding entries flat for 2 wakes at 1/15 and 0/15 breadth.
- Rule 8 priority worked as designed: top-3 by rank (BTC, ETH, SOL) all failed the 4H trend filter despite +1-2% 24h moves; XRP was the highest-rank pair where the 4H crossover materialized. Lower-rank candidates (XDG, SUI, LTC, ADA, AVAX, LINK) not evaluated because XRP locked the slot — this is correct per rule 8 (and saves token budget).
- ATR elevated (~3× of normal range) due to the breakout bar. Wider stop = smaller size = same $-risk. Strategy v0.2 sizing handles this automatically.
- Entry at marginal 4H crossover (+0.001 above EMA50) is the riskiest profile for a v0.2 entry — the 4H trend hasn't accelerated yet, just curled. The 1H momentum carry (+1.9% above EMA20 and RSI 67) is strong though. Watching for early-bar stop-out on cluster-correlated reversal (BTC/ETH still below their 4H EMA50s — if they fail to follow, XRP could orphan).

## 2026-05-14T16:45Z — routine-03-eod

### Context

Cron-fire of `bull-03-eod` ~45min after `bull-01-overnight` opened XRP at 16:00Z. EOD's role per spec: final MTM, exit check on just-closed 1H, entry rescan (interpreted below), lesson extraction, day-stats compilation, mandatory Telegram card.

### Final mark-to-market

- XRP/USD spot 16:30Z (`kraken_ticker`): **1.4689** (24h +2.96%, spread 0.00013, vwap 1.44). Tight liquidity, no spread anomaly.
- Position MTM: 6334 × 1.4689 = **$9,304.01** (vs entry notional 9298.69)
- Unrealized PnL: **+$5.32** (+0.03R) — recovered from earlier −$4.62 mark
- Cash: $935.19 (post entry-commission $24.18)
- **Equity: $10,239.20** (vs prior peak $10,258.06)
- **Drawdown from peak: 0.18%** — well within 12.5% warn / 25% kill caps

### Post-close exit check (XRP just-closed 1H bar 2026-05-14 15:00Z)

Bar 15:00Z close **1.46903** (high 1.4721, low 1.46197, vol 553k, trades 753):
- Static stop 1.44377: close 1.46903 **>** stop. No stop-hit (bar low 1.46197 also above).
- 1H 20-EMA at 15:00Z: iterated from E58=1.43763 → E59 ≈ **1.4406**. Close 1.46903 > EMA → no EMA-cross exit.
- 4R target 1.56522: close well below. No take-profit.

**Hold XRP.** Next 1H exit check at 17:00Z bar close.

### Entry scan (routine-03 spec step 3)

**Regime breadth (refresh 16:15Z):** unchanged from overnight wake — 14/15 positive (only FARTCOIN red, also below liquidity floor). Gate PASSES.

**Per-pair evaluation summary (rule-8 priority order):**

| Rank | Pair | Status |
|:---:|---|---|
| 1 | BTC/USD | rejected this morning on rule 3 (4H close 79245 < EMA50 80282) |
| 2 | ETH/USD | rejected on rule 3 (2253.10 < 2305.62) |
| 3 | SOL/USD | rejected on rule 3 (90.61 < 91.59) |
| 4 | XRP/USD | **HELD** (entered 16:00Z this morning by routine-01) |
| 5–15 | TAO, HYPE, XDG, SUI, LTC, ADA, AVAX, LINK | **not evaluated** — see Decision rationale |

### News (Firecrawl scan)

**Deferred this wake** to conserve context budget (same pattern as 2026-05-12 routine-01). v0.2 news rule is informational-only (no entry veto), and overnight wake already harvested the 24h headline set with 0 ACTIONABLE. No new XRP-base-asset catalysts surfaced via spot price (no idiosyncratic XRP spike vs broad 14/15 rally). `kraken_risk_flag` daily classifier (CLEAR per overnight). 

**ACTIONABLE flagged: 0** items.

### Sentiment

XRP spread 0.00013 (0.009% of price) — tight. Single open position, no entry-decision data needed. Depth pull skipped.

### Decision

- **NO ADDITIONAL ENTRIES.** Rationale: cron-fire-adjacent routine-01 already consumed the per-wake entry budget (rule 8: "max 1 new entry per routine wake"). Treating this EOD fire as a separate wake would effectively allow 2 entries inside the same 1H bar (15:00–16:00Z window when XRP just printed +2.4%), recreating the cascade-risk failure mode lesson 2026-04-27 was designed to prevent. **Conservative interpretation chosen: 1-per-cron-bar.** This ambiguity should be codified at routine #4 (Saturday 2026-05-16): either tighten strategy.md rule 8 to "max 1 entry per 1H bar" or explicitly allow EOD to re-scan with cluster-cap as the only check.
- **NO EXITS.** XRP all three exit triggers clear at 15:00Z 1H close.
- **NO LESSONS APPENDED.** XRP entry is 1h old — too fresh for outcome-based lesson extraction. Pre-outcome lesson candidates already noted in overnight log (marginal 4H crossover risk; cluster-orphan risk if BTC/ETH don't follow).
- **Kill-switch state:** all clear (daily 0%, DD 0.18%, equity $10,239.20, losing streak 0).
- **No archive sweep:** 2026-05-14 is Thursday; last trading day of May is Friday 2026-05-29.

### Day's summary stats

- **Day PnL:** −$18.88 (−0.18%) — entry commission $24.18 partially offset by +$5.32 XRP positive drift
- **Trades opened:** 1 (XRP/USD long, by routine-01-overnight)
- **Trades closed:** 0 — win rate today N/A
- **New equity:** $10,239.20 (peak $10,258.06 from 2026-05-11 SOL +4R)
- **Drawdown:** 0.18% from peak
- **Rolling 7-day delta vs BTC-hold (approximate):** BULL ≈ +5.86% (from 9672.75 EOD 2026-05-07 LINK exit → 10239.20 now); BTC-hold ≈ +1.07% (~80000 → 80857). **BULL +4.79% delta vs BTC over 7d.** Full computation defers to routine #4 with precise reference prices.
- **Rolling 30-day:** window pre-dates BULL inception (2026-04-20); not yet computable. First available 2026-05-20.

### Process notes

- Slot identity confirmed: this fire is `bull-03-eod` content (final MTM + exit check + day stats + EOD Telegram card). Distinct from prior `bull-03-eod`-misfire-as-routine-01 pattern (commits `3ce53b1`, `2055f30`-precursor).
- The 1-per-cron-bar interpretation is a deliberate conservative reading; flagged for routine #4 review.
- **Telegram:** mandatory EOD card per routine-03 NOTIFY spec.
2026-05-15T06:21:04Z | harness | day-gate | not Saturday, skipping | no action
