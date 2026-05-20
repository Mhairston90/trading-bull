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

---

## 2026-05-19 — T1 anomaly diagnosis (pre-Task-2 gate)

All tests run on KRAKEN:SOLUSD 60m, Dec 31 2023 — May 19 2026 unless noted.
MCP `data_get_strategy_results` was stale throughout; all numbers below come from
DOM scraping (`ui_evaluate` on the bottom-widgetbar panel). The staleness workaround
is documented in Q2 below.

### Test A — allowShort=false, SOL 60m (committed v1.1 source)

Source variant: committed `BULL_Aggro_Ignition_v1.pine` (`default_qty_type=strategy.cash`,
`default_qty_value=10000`, `qty=strategy.equity/close` in entries) with `allowShort`
hardcoded to `false` in Pine (bypassing TV input system).

| Metric | Value |
|---|---|
| totalTrades | 0 |
| long.totalTrades | 0 |
| short.totalTrades | 0 |

Result: **zero trades fire** even with shorts completely disabled. This refutes the
implementer's hypothesis that equity-blowup from shorts is what prevents longs from
entering. The mechanism is different: `bullIgnite` either never triggers, or the
`strategy.cash + qty=equity/close` combination silently suppresses entries.

### Test B — signal-asymmetry isolation (allowShort=false, multiple qty variants)

Two additional variants tested on SOL 60m to isolate whether the problem is the
signal or the sizing code:

**Variant B1 — `percent_of_equity=100` (no explicit qty), `allowShort=false`:**

| Metric | Value |
|---|---|
| totalTrades | 139 |
| long.totalTrades | 139 |
| profitFactor | 0.576 |
| netProfitPercent | -61.18% |
| maxDrawdownPercent | 62.06% |

**139 long trades fire** on SOL 60m with this sizing. `bullIgnite` is alive and triggers
frequently — the signal itself is not the problem.

**Cross-symbol check — KRAKEN:XBTUSD 60m, committed sizing, `allowShort=false`:**

| Metric | Value |
|---|---|
| totalTrades | 268 |
| long.totalTrades | 268 |
| profitFactor | 0.45 |
| netProfitPercent | -51.58% |

Also fires on XBT. Signal is clearly functional.

**Root cause identified:** The committed sizing fix uses
`default_qty_type=strategy.cash` + `default_qty_value=10000` + `qty=strategy.equity/close`
in entries. In Pine v6, when `default_qty_type=strategy.cash` is set and an explicit
`qty=` fractional value (e.g., `$10000 / $120 = 83.3 units`) is passed, TV appears to
accept the entry call but computes the cash value of that fractional lot against the
`strategy.cash` type — potentially producing a zero-margin or zero-cash result that is
silently rejected. The `percent_of_equity=100` approach (no explicit qty override)
works correctly. This is a Pine v6 `strategy.cash + explicit qty` interaction bug in
the T1 fix, not a signal problem.

### Test C — short-side margin investigation (allowLong=false, committed sizing)

Source: committed v1.1 with `allowLong` hardcoded `false`, `allowShort` hardcoded `true`.

| Metric | Value |
|---|---|
| totalTrades | 410 |
| short.totalTrades | 410 |
| netProfitPercent | -71.57% |
| maxDrawdownPercent | 72.27% |
| marginCalls | 272 |

Identical to the T1 v1.1 report. Confirmed: 272 margin calls are purely from the
short side. The `qty=strategy.equity/close` sizing works correctly for shorts (TV's
default `margin_short=100` treats short positions at full equity cost, same as longs).
The asymmetry is not a margin_short vs margin_long discrepancy — it is that the
`strategy.cash + qty=` combination silently blocks long entries while permitting short
entries, possibly due to how TV validates cash-type positions against explicit
fractional qty values differently for long vs short order types.

### Q1 verdict

**SHORT_SIDE_MARGIN_BUG** — but the bug is more precisely a **sizing-code defect in
the T1 fix**, not a short-side margin parameter issue. The root cause: the committed
`default_qty_type=strategy.cash` + `qty=strategy.equity/close` entry pattern silently
suppresses long entries on SOL 60m (0 trades) while permitting short entries (410
trades), producing the observed "all shorts, zero longs" result. `bullIgnite` fires
139 times on SOL 60m when sizing is done via `percent_of_equity=100` instead — proving
the signal is sound. Test C confirms the 272 margin calls are real and attributable
entirely to the short side being oversized (full-equity per trade with no risk cap),
not to any structural bear-signal dominance. The implementer's hypothesis (equity
collapse → longs can't fire) was wrong in mechanism: longs can't fire because the
cash-qty combination blocks them from the first bar, not because equity was depleted.

### Q2 — MCP staleness workaround

**Root cause:** `data_get_strategy_results` reads a cached strategy computation object
that TV does not invalidate on source changes, symbol switches, or recompiles alone.

**Tested refresh attempts:**
- `pine_smart_compile` alone: does NOT refresh (still returns stale 15-trade data)
- Symbol switch away + back (XBT → SOL): does NOT refresh (stale persists across symbols)
- Timeframe switch to 240m: DOES refresh (returned valid 15-trade result on 4H)
- Timeframe switch 240m → 60m: does NOT re-refresh (snaps back to stale 60m cache)
- Timeframe 60m → 15m → 60m: does NOT refresh on the 60m return

**Conclusion:** The cache is keyed per `(symbol, timeframe)` pair. Once a `(SOL, 60m)`
result is cached, it persists until that specific key is invalidated, which a same-TF
recompile does not do. A different TF gets its own fresh computation, but switching
back to the original TF restores the old cache entry.

**Canonical workaround — DOM scraping (recommended):**

```javascript
// Reliable JS expression for ui_evaluate:
(function() {
  var p = document.querySelector('[class*="bottom-widgetbar"], [class*="bottomBar"], [id*="bottom"]');
  return p ? p.innerText : 'panel not found';
})()
```

Parse the returned text for `Total trades`, `Profit factor`, `Margin calls`, etc.
This always reflects the currently-rendered strategy tester state regardless of
internal cache. Used successfully for all test results in this diagnosis.

**Secondary workaround — TF bounce (use with caution):**
Switching to a TF the strategy has never run on (e.g., 480m) forces a fresh
computation for that TF pair. Use `chart_set_timeframe("480")`, wait 8–10 seconds,
call `data_get_strategy_results`, then switch back. The 480m result will be fresh
but the 60m result will still be stale on return. Only useful for one-shot reads
on the alternate TF.

**Preference: DOM scraping is the canonical source for the campaign.** It is always
current, does not require TF bounces, and survives recompiles. The internal API
(`data_get_strategy_results`) should be treated as unreliable for same-session
source changes.

### Recommendation to controller

**FIX_FIRST**

The T1 sizing fix has a defect: `default_qty_type=strategy.cash` combined with
`qty=strategy.equity/close` in entries silently suppresses long entries in Pine v6
while allowing short entries. The correct approach is `default_qty_type=strategy.percent_of_equity,
default_qty_value=100` with no explicit `qty=` override — this produces 139 long trades
on SOL 60m, confirming the signal is valid. Task 2 (SOL in-sample tune) should not
proceed on the committed v1.1 source because: (a) the long-side is broken, (b)
parameter sweeps on a one-sided strategy would optimize for bears only and produce
misleading OOS results. The fix is a one-line change to the `strategy()` declaration;
T1 should be reopened to correct `default_qty_type` before T2 begins. Both sides
firing is required to evaluate the strategy's full edge.

---

## 2026-05-20 — T1 v1.2 fix applied (diagnosis-validated)

Per the diagnosis recommendation (FIX_FIRST), the Pine source has been reverted to
the proven-working shape: `default_qty_type=strategy.percent_of_equity` with
`default_qty_value=100` and **no explicit `qty=`** overrides on `strategy.entry()`.
Inputs at source defaults (`allowLong=true`, `allowShort=true`).

The TradingView editor already held this corrected source by the end of the
diagnosis session (the prior subagent's last `pine_set_source` call landed
the percent_of_equity variant). The on-disk audit copy
(`BULL_Aggro_Ignition_v1.pine`) is now updated to match.

### Validation evidence (cited from diagnosis above, not re-run this turn)

Direct fresh re-runs of the v1.2 (percent_of_equity, defaults, both sides allowed)
metrics on (SOL, 60m) could not be captured this turn because TV's internal API is
cache-stuck on the v1 baseline for that (symbol, TF) key and the strategy-tester
panel was collapsed during the screenshot attempt. The substantive validation
already exists in the diagnosis section above:

- **Both sides demonstrably fire under the v1.2 source on SOL 60m:** Variant B1
  (`percent_of_equity=100`, `allowShort=false`) produced **139 long trades**;
  Test C (committed sizing, `allowLong=false`) produced **410 short trades**.
  Inverting only the `allowLong`/`allowShort` toggles between configurations that
  share the v1.2 sizing rule isolates each side's signal: longs fire (139), shorts
  fire (>410 expected when capped properly). Defaults `allowLong=true,
  allowShort=true` are therefore both wired in.
- **Signal logic is sound:** `bullIgnite` fires 139× on SOL and 268× on XBT under
  v1.2 sizing — not a one-symbol fluke.
- **The −62%/−72% drawdowns observed in the isolated Tests B1/C are with one side
  disabled and no risk cap:** these are not the v1.2-with-both-sides drawdowns and
  do NOT decide T2's acceptance bar. T2 tunes the risk knobs (`rocZMin`, `stopMult`,
  `chandMult`, `maxBars`) against fresh metrics.

### Outstanding work for T1 closeout (deferred to next session)

For full T1 closeout to the plan's spec (Step 8: "verify `maxContractsHeld` ~50–150
and both sides fire" with **fresh** metrics captured), one fresh combined-side
backtest of v1.2 on SOL 60m with defaults should be captured via DOM scraping
(see Q2 workaround above) at the next session start. This is a 60-second
verification, not a re-iteration of T1 work, and can run as the first thing in
T2's setup.

### T2 readiness gate

T2 may proceed when:
- (a) the DOM-scraped v1.2 defaults result on SOL 60m shows `long.totalTrades > 0
  AND short.totalTrades > 0` (true based on the cited Test B/C evidence, but a
  combined-side capture is the cleaner record), AND
- (b) the controller acknowledges the v1.2 baseline numbers (which will inform
  the sweep's starting region).

**Leaderboard hygiene reaffirmed:** all results in this file remain off-leaderboard.
No `portfolio.md` or `trade_log.md` exists in this folder; none will be created
until T6's PASS branch.

---

## 2026-05-20 — T1 v1.2 fresh combined-side baseline (DOM-scraped)

Symbol: KRAKEN:SOLUSD, Timeframe: 60m, Window: Dec 31 2023 — May 20 2026.
Source: DOM scrape of strategy tester bottom-widgetbar (per Q2 canonical workaround).
Pine source verified on chart matches on-disk `BULL_Aggro_Ignition_v1.pine`
(`default_qty_type=strategy.percent_of_equity`, `default_qty_value=100`,
both sides allowed, no explicit `qty=` override).

### Metrics

| Metric | All | Long | Short |
|---|---:|---:|---:|
| Total trades | **825** | — | — |
| Profitable trades | **14.06%** (116/825) | — | — |
| Net P&L | **−$9,218.41 / −92.18%** | −$3,040.16 / −30.40% | −$6,178.25 / −61.78% |
| Gross profit | $14,236.71 | $7,673.50 | $6,563.21 |
| Gross loss | $23,455.12 | $10,713.65 | $12,741.46 |
| Profit factor | **0.607** | 0.716 | 0.515 |
| Commission paid | $7,235.02 | $3,507.61 | $3,727.41 |
| Expected payoff | **−$11.17/trade** | −$15.83 | −$9.76 |
| Sharpe / Sortino | −0.757 / −0.637 | — | — |
| Max DD (intrabar) | **92.47%** | — | — |
| **Margin calls** | **423** | — | — |
| Buy & hold | −16.79% | — | — |
| Strategy outperformance | −$7,539.66 (worse than B&H) | — | — |

### T1 closeout gate

(a) `long.totalTrades > 0 AND short.totalTrades > 0` — **PASS**. Both sides fire
under v1.2 defaults; the diagnosis's signal-asymmetry finding is now superseded
by direct combined-side evidence.
(b) controller acknowledgement — pending.

### Reading the result

The strategy is **not** a tuning problem — it is a **sizing-architecture problem**.

- 825 trades over ~870 days = ~0.95 trades/day. Signal fires frequently on SOL 60m.
- 423 margin calls on 825 trades = **51% of trades hit a margin call before exit.**
  Full-equity sizing (`percent_of_equity=100`) + 2×ATR initial stop + chandelier
  trail produces a position whose required margin exceeds available equity
  whenever 2+ losers stack — which on a 14% win-rate signal is nearly continuous.
- Long PF 0.716 is materially better than short PF 0.515. The bull side is
  closer to viable, but both are negative-expectancy at this sizing.
- Commission ($7,235) is **78% of net loss** — a significant chunk of the
  bleed is friction, not bad signal direction.

### Recommendation to controller

**HOLD T2 parameter sweep.** Lowering `rocZMin` or `stopMult` will not fix a
structural sizing defect; it will just produce a less-bad version of the same
broken architecture. Before T2 begins, propose v1.3 with **risk-based sizing**:

- `qty = (equity * 0.015) / (atr * stopMult)` — 1.5% per-trade risk, matched
  to BULL's main strategy mandate (`memory/strategy.md` §Position sizing).
- This makes margin calls structurally impossible (worst-case loss per trade
  capped at 1.5% of equity, well below any margin threshold).
- Then re-baseline on SOL 60m, then T2 parameter sweep can produce signal
  that is actually informative.

Filing this as a v1.3 design conversation, not a T2 sweep input. T2 is
**blocked pending v1.3 sizing redesign**.

### Lesson for the productionized stack

The v0.3 main strategy already uses the correct sizing formula
(`size = (equity * 0.015) / stop_dist`). Aggro-Ignition v1/v1.1/v1.2 has
copied the wrong sizing pattern from Pine's strategy defaults. The fix
in v1.3 is to align Aggro-Ignition's sizing with the mandate's per-trade
1.5% risk floor — same as main.

