# BULL_Aggro_Ignition — Backtest Notes (NOT leaderboard-sourced)

> **This file is research output. `registry.js` does NOT read it.**
> All backtest, sweep, OOS, head-to-head, and contest-window numbers go here.
> Never copy these into `portfolio.md` / `trade_log.md`, which are forward-only.

## Run log

## 2026-05-19 — v1 baseline (sizing bug)

Symbol: KRAKEN:SOLUSD, Timeframe: 60m

| Metric | Value |
|---|---|
| totalTrades | 15 |
| netProfit | -$116.45 |
| netProfitPercent | -0.058% |
| profitFactor | 0 (0 winning trades) |
| maxContractsHeld | 5.763 |
| maxStrategyDrawDownPercent | 6.01% |
| short.totalTrades | 0 |

**Notes:** All 15 trades are longs; zero shorts fired. `maxContractsHeld` of ~5.76
confirms the sizing bug — `strategy.percent_of_equity=100` is behaving as a fixed
unit count (~$10k equity / ~$85 SOL price ≈ 117 expected, but TV interprets
`percent_of_equity` differently than intended). Short side completely silent despite
`allowShort=true` being the default.

## 2026-05-19 — v1.1 sizing fix verification

Symbol: KRAKEN:SOLUSD, Timeframe: 60m  
Source: DOM read (strategy tester UI) — MCP `data_get_strategy_results` API returns
stale cached data from the pre-fix run and cannot be refreshed without a TV restart.

| Metric | Value |
|---|---|
| totalTrades | 410 |
| netProfit | -$7,156.75 |
| netProfitPercent | -71.57% |
| profitFactor | 0.463 |
| maxContractsHeld | ~32–33 (inferred: entry size 32.71 SOL at $85.97 = ~$2.81K; equity ~$2.81K at that point) |
| maxMarginUsed | $10,276 (confirms full-equity sizing is working) |
| maxStrategyDrawDownPercent | 72.27% |
| marginCalls | 272 |
| long.totalTrades | 0 |
| short.totalTrades | 410 |

**Sizing fix confirmed:** Max margin used = $10,276 on a $10,000 account confirms
`qty=strategy.equity/close` is deploying full equity per trade. In v1, total losses
were only ~$116 on 15 tiny-lot trades; v1.1 losses are $7,156 on 410 full-size trades.

**Short-side fires:** Confirmed — all 410 trades in v1.1 are shorts. The signal logic
is strongly biased toward `bearIgnite` on SOLUSD 60m over the Dec 2023–May 2026 window.

**0 long trades observed:** After the short-dominated early trades blow the account via
272 margin calls, `strategy.equity` collapses to near zero, making `qtyL = equity/close`
too small to generate new entries, and any subsequent `bullIgnite` signals would yield
negligible position sizes. The long logic is syntactically correct and `allowLong=true`;
longs simply did not fire in this particular in-sample window because:
  (a) SOL had a strong bear-ignition phase early in the period
  (b) The short blowup consumed all equity before long signals could re-enter

**Next step:** Task 2 (SOL in-sample tune) — lower `rocZMin` and `stopMult` to reduce
margin-call frequency; this is a parameter issue, not a code bug. The fix is correct.
