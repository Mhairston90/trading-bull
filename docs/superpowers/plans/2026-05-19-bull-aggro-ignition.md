# BULL_Aggro_Ignition Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Validate-or-falsify the convex momentum-ignition crypto strategy (`BULL_Aggro_Ignition`) end-to-end and ship it to forward paper only if it clears the spec §7 acceptance bar; otherwise document the failure and stop.

**Architecture:** Single-symbol Pine v6 strategy in TradingView (`/BULL_*` namespace), backtested via the Pine Strategy Tester across 6 Kraken crypto symbols on 30m and 60m intraday timeframes. All R&D output (param sweeps, OOS tables, head-to-head vs approach C, contest-window slice) lives in a single `backtest_notes.md` file that the external Strategy Leaderboard does **not** read. A forward-paper strategy folder (`portfolio.md` / `trade_log.md` + leaderboard registry entry) is created **only** if the acceptance bar passes.

**Tech Stack:** Pine v6 (TradingView), TradingView MCP tools (`pine_*`, `chart_*`, `data_get_strategy_results`, `data_get_trades`, `capture_screenshot`), git on the `trading-bull` repo, markdown deliverables.

**Spec:** [docs/superpowers/specs/2026-05-19-bull-aggro-ignition-design.md](../specs/2026-05-19-bull-aggro-ignition-design.md)

**Contest deadline:** 2026-06-06. Spec §7 is the gate; honest failure beats curve-fit ship.

---

## File Structure

All paths relative to the `trading-bull` repo root.

- **Create** `strategies/bull-aggro-ignition/README.md` — strategy doc, links to spec + this plan.
- **Create** `strategies/bull-aggro-ignition/backtest_notes.md` — single source for all R&D output. **Off-leaderboard.** Append-only sections per task. The Strategy Leaderboard registry does NOT and MUST NOT reference this file.
- **Create** `strategies/bull-aggro-ignition/BULL_Aggro_Ignition_v1.pine` — audit copy of the current TradingView source (read-only mirror; the live script lives in TV).
- **Create** `strategies/bull-aggro-ignition/BULL_Aggro_RS_v1.pine` — audit copy of the cross-sectional challenger.
- **Conditional (Task 6, only if pass):**
  - `strategies/bull-aggro-ignition/portfolio.md` — forward-paper only, $10k synthetic, header banner: "LEADERBOARD-SOURCED — FORWARD PAPER-PAPER ONLY."
  - `strategies/bull-aggro-ignition/trade_log.md` — forward-paper only, same banner.
  - One entry added to `C:/Users/Mhair/OneDrive/Desktop/strategy-leaderboard/registry.js` with `live_start_iso` set to the ship date (separate repo, separate commit, requires user push approval).
- **No modifications** to `memory/strategy.md`, `memory/guardrails.md`, BULL's `memory/portfolio.md` or `memory/trade_log.md`, any `variants/*`, or anything in TradingView outside the `/BULL_*` namespace.

**Pine scripts** live in TradingView (out-of-repo). `BULL_Aggro_Ignition_v1` already exists there from the brainstorm session (compiles clean; sizing/short-side bugs documented). `BULL_Aggro_RS_v1` is created in Task 4.

---

## Acceptance Bar (Spec §7 — referenced by Tasks 3, 4, 6)

A run passes only if **all** of the following hold over the OOS symbol set (DOGE, AVAX, LINK, BTC, ETH) with the SOL-tuned params applied unchanged:
1. Net positive AND profit factor **> 1.3** aggregate OOS.
2. Positive expectancy on **≥ 4 of 6** symbols (SOL counts; not one-symbol-carried).
3. Max strategy drawdown **<** buy-hold drawdown on the same window.
4. **≥ 30 closed trades** aggregate OOS.
5. Beats approach C (cross-sectional) on risk-adjusted return OR is clearly complementary (low return correlation).

---

## Task 1: Fix v1 mechanics — sizing + short-side firing

**Goal:** Make the Pine probe usable: position sizing must reflect 100% of equity per trade, and short entries must fire when bear-ignition conditions are met. Without this, every later result is garbage.

**Files:**
- Modify (TradingView, in-place): Pine script `BULL_Aggro_Ignition_v1`
- Create: `strategies/bull-aggro-ignition/README.md`
- Create: `strategies/bull-aggro-ignition/backtest_notes.md`

- [ ] **Step 1: Create the strategy folder + README**

Create `strategies/bull-aggro-ignition/README.md`:

```markdown
# BULL_Aggro_Ignition — Crypto convex momentum-ignition strategy

**Status:** R&D — validation in progress (see backtest_notes.md).
**Spec:** docs/superpowers/specs/2026-05-19-bull-aggro-ignition-design.md
**Plan:** docs/superpowers/plans/2026-05-19-bull-aggro-ignition.md
**Pine namespace:** /BULL_*  (TradingView only — not productionized to leaderboard).

This folder will only contain `portfolio.md` / `trade_log.md` and a leaderboard
registry entry if the strategy clears the spec §7 acceptance bar. Until then,
all output is research and lives in `backtest_notes.md` (NOT registry-sourced).
```

- [ ] **Step 2: Create the backtest notes file with header**

Create `strategies/bull-aggro-ignition/backtest_notes.md`:

```markdown
# BULL_Aggro_Ignition — Backtest Notes (NOT leaderboard-sourced)

> **This file is research output. `registry.js` does NOT read it.**
> All backtest, sweep, OOS, head-to-head, and contest-window numbers go here.
> Never copy these into `portfolio.md` / `trade_log.md`, which are forward-only.

## Run log
(populated by tasks below)
```

- [ ] **Step 3: Read current Pine source from TradingView**

Use the MCP tool to confirm the current source:
```
mcp__tradingview-mcp__pine_get_source
```
Save the returned source to `strategies/bull-aggro-ignition/BULL_Aggro_Ignition_v1.pine` for audit (write tool, exact verbatim contents).

- [ ] **Step 4: Diagnose v1 sizing — set chart and read current behavior**

```
mcp__tradingview-mcp__chart_set_symbol  symbol=KRAKEN:SOLUSD
mcp__tradingview-mcp__chart_set_timeframe  timeframe=60
mcp__tradingview-mcp__data_get_strategy_results
```
Expected: confirm baseline — net negative, maxContractsHeld implausibly low (probe showed ~5.76 on $10k/$85 SOL; expected ~117). Record raw metrics under a new `## 2026-05-19 — v1 baseline (sizing bug)` section in `backtest_notes.md`.

- [ ] **Step 5: Fix sizing — modify Pine `strategy()` header and entry calls**

Replace the strategy header line in the TradingView source (use `mcp__tradingview-mcp__pine_set_source` with the full updated source):

OLD:
```pine
strategy("BULL_Aggro_Ignition_v1",
     overlay=true,
     initial_capital=10000,
     default_qty_type=strategy.percent_of_equity,
     default_qty_value=100,
     pyramiding=0,
     commission_type=strategy.commission.percent,
     commission_value=0.26,
     slippage=2,
     process_orders_on_close=true,
     calc_on_every_tick=false)
```

NEW:
```pine
strategy("BULL_Aggro_Ignition_v1",
     overlay=true,
     initial_capital=10000,
     default_qty_type=strategy.cash,
     default_qty_value=10000,
     currency=currency.USD,
     pyramiding=0,
     commission_type=strategy.commission.percent,
     commission_value=0.26,
     slippage=2,
     process_orders_on_close=true,
     calc_on_every_tick=false)
```

Rationale: `strategy.cash` with `default_qty_value=10000` deploys $10k notional per entry (re-evaluated against current equity at order time via explicit `qty` if needed). This avoids the percent_of_equity edge case that produced the tiny contract count.

- [ ] **Step 6: Replace fixed-qty entries with equity-scaled explicit qty**

In the same `pine_set_source` update, change the two `strategy.entry` calls so the sleeve always deploys the current equity:

OLD:
```pine
if flat and allowLong and bullIgnite
    strategy.entry("L", strategy.long)
```
```pine
if flat and allowShort and bearIgnite
    strategy.entry("S", strategy.short)
```

NEW:
```pine
if flat and allowLong and bullIgnite
    qtyL = strategy.equity / close
    strategy.entry("L", strategy.long, qty=qtyL)
```
```pine
if flat and allowShort and bearIgnite
    qtyS = strategy.equity / close
    strategy.entry("S", strategy.short, qty=qtyS)
```

- [ ] **Step 7: Compile and verify no errors**

```
mcp__tradingview-mcp__pine_smart_compile
```
Expected: `has_errors: false, errors: []`. If errors, capture them via `pine_get_errors`, fix, recompile. Do not proceed until clean.

- [ ] **Step 8: Re-backtest on SOLUSD 60m and verify sizing fix**

```
mcp__tradingview-mcp__chart_set_symbol  symbol=KRAKEN:SOLUSD
mcp__tradingview-mcp__chart_set_timeframe  timeframe=60
mcp__tradingview-mcp__data_get_strategy_results
```
Expected: `maxContractsHeld` ≈ equity / SOL price (order of ~100, not ~5). Record metrics in `backtest_notes.md` under `## 2026-05-19 — v1.1 sizing fix verification` with the contracts and net P&L. If contracts are still implausibly small, debug `strategy.equity` / `default_qty_value` interaction before continuing.

- [ ] **Step 9: Verify short-side fires — pull the trade list**

```
mcp__tradingview-mcp__data_get_trades  max_trades=200
```
Expected: at least one short trade (look for negative size or "S" entry). If zero shorts: this is a real bug. Likely causes to inspect (in order):
  (a) `bearIgnite` requires `cPos <= 1 - closePos` (= 0.4 by default) — confirm bearish bars hit that.
  (b) `rocZ <= -rocZMin` may be too strict — temporarily set `rocZMin = 0.5` via `indicator_set_inputs` and re-test.
  (c) `allowShort` input default is true — confirm not overridden.
Document the diagnosis and fix in `backtest_notes.md`. Once a short trade is confirmed in the trade list, proceed.

- [ ] **Step 10: Save the verified Pine source to repo audit copy**

```
mcp__tradingview-mcp__pine_get_source
```
Write returned source to `strategies/bull-aggro-ignition/BULL_Aggro_Ignition_v1.pine` (overwrites the Step 3 snapshot).

- [ ] **Step 11: Commit**

```bash
git add strategies/bull-aggro-ignition/README.md strategies/bull-aggro-ignition/backtest_notes.md strategies/bull-aggro-ignition/BULL_Aggro_Ignition_v1.pine
git commit -m "bull-aggro-ignition: fix v1 sizing + short-side, record baseline

Task 1 of validation plan. Sizing was strategy.percent_of_equity (yielded
tiny contracts); replaced with strategy.cash + explicit qty=equity/close.
Verified short-side fires. All raw metrics in backtest_notes.md."
```

---

## Task 2: In-sample parameter tune on SOL 60m and 30m

**Goal:** Identify a *robust* parameter region (not a single best cell) on SOLUSD across two timeframes. Output: one chosen `v1.1` parameter set carried unchanged into OOS.

**Files:**
- Modify (TradingView, runtime): script inputs via `indicator_set_inputs` per sweep cell
- Append: `strategies/bull-aggro-ignition/backtest_notes.md`

- [ ] **Step 1: Define sweep grid in backtest_notes.md**

Append section `## Task 2 — SOL in-sample sweep`. Document the grid (do NOT change the Pine source — only inputs vary):

```
timeframe   : [30, 60]
rangeMult   : [1.6, 1.8, 2.0, 2.2, 2.5]
volMult     : [1.5, 1.8, 2.0, 2.3]
rocZMin     : [0.5, 1.0, 1.5]
stopMult    : [1.5, 2.0, 2.5]
chandMult   : [2.0, 3.0, 4.0]
maxBars     : [24, 48, 96]
closePos    : 0.60 (fixed for now)
lookback    : 50  (fixed)
rocLen, rocZLen, atrLen : defaults (10, 50, 14)
```

Full Cartesian is 2*5*4*3*3*3*3 = 1080 cells — too many. Use a **fractional sweep**: 1 timeframe pass, holding all but one knob fixed at center, then refine. Document the order: rangeMult → volMult → rocZMin → stopMult → chandMult → maxBars → timeframe revisit.

- [ ] **Step 2: Sweep rangeMult on SOL 60m (5 runs)**

For each value in [1.6, 1.8, 2.0, 2.2, 2.5]:
```
mcp__tradingview-mcp__chart_set_symbol  symbol=KRAKEN:SOLUSD
mcp__tradingview-mcp__chart_set_timeframe  timeframe=60
mcp__tradingview-mcp__indicator_set_inputs  (set rangeMult to value; other inputs at center: volMult=2.0, rocZMin=1.0, stopMult=2.0, chandMult=3.0, maxBars=48)
mcp__tradingview-mcp__data_get_strategy_results
```
Append a markdown table row per run to `backtest_notes.md`:

```
| rangeMult | trades | win% | net% | PF | maxDD% | sharpe |
|-----------|-------:|-----:|-----:|---:|-------:|-------:|
| 1.6       | ...    | ...  | ...  | ...| ...    | ...    |
| 1.8       | ...    | ...  | ...  | ...| ...    | ...    |
| 2.0       | ...    | ...  | ...  | ...| ...    | ...    |
| 2.2       | ...    | ...  | ...  | ...| ...    | ...    |
| 2.5       | ...    | ...  | ...  | ...| ...    | ...    |
```

Pick the value with the **best PF among rows with ≥ 20 trades and PF > 1.0**. If no row clears those filters, mark rangeMult inconclusive and continue to the next knob using center.

- [ ] **Step 3: Sweep volMult holding rangeMult at chosen value (4 runs)**

Same protocol as Step 2 for volMult ∈ [1.5, 1.8, 2.0, 2.3]. Record table. Pick by same criterion.

- [ ] **Step 4: Sweep rocZMin (3 runs)**

Same protocol for rocZMin ∈ [0.5, 1.0, 1.5].

- [ ] **Step 5: Sweep stopMult (3 runs)**

Same protocol for stopMult ∈ [1.5, 2.0, 2.5]. Special concern: stopMult interacts with PF. Also record largest losing trade as % — if stopMult=1.5 produces a worst trade > -2× the others' worst, prefer the wider stop even at small PF cost.

- [ ] **Step 6: Sweep chandMult (3 runs)**

Same protocol for chandMult ∈ [2.0, 3.0, 4.0]. This controls give-back; record avg winning trade size as well.

- [ ] **Step 7: Sweep maxBars (3 runs)**

Same protocol for maxBars ∈ [24, 48, 96].

- [ ] **Step 8: Revisit on SOL 30m**

Switch `chart_set_timeframe timeframe=30` and re-run a *focused* sweep at the values chosen from Steps 2–7 ±1 step on each knob (small grid, ~10 runs). Compare 30m vs 60m chosen-cell PF. Pick the timeframe with the higher PF *unless* trade count on 30m is >2x and DD is comparable, in which case prefer 30m for sample size.

- [ ] **Step 9: Robustness check — pick a region, not a cell**

In `backtest_notes.md`, identify a **robust region**: the chosen cell plus its 6 nearest neighbors (one step on each knob). Confirm at least 5 of 7 are net-positive with PF > 1.1. If not, the surface is too peaky — note this honestly and choose a flatter cell even at lower PF.

- [ ] **Step 10: Document the chosen v1.1 param set**

Append a `## v1.1 chosen params (SOL in-sample)` block to `backtest_notes.md`:

```
timeframe : <X>
rangeMult : <X>
volMult   : <X>
rocZMin   : <X>
stopMult  : <X>
chandMult : <X>
maxBars   : <X>
(others)  : defaults
```
Also record the SOL in-sample metrics for the chosen cell (trades, win%, net%, PF, maxDD%, sharpe).

- [ ] **Step 11: Capture a strategy tester screenshot for the audit trail**

```
mcp__tradingview-mcp__capture_screenshot  region=strategy_tester  filename=bull_aggro_ignition_sol_v11_chosen
```
Reference the saved PNG path in `backtest_notes.md`.

- [ ] **Step 12: Commit**

```bash
git add strategies/bull-aggro-ignition/backtest_notes.md
git commit -m "bull-aggro-ignition: Task 2 SOL in-sample tune, v1.1 params chosen

Fractional sweep across rangeMult/volMult/rocZMin/stopMult/chandMult/
maxBars + timeframe revisit. Robust region check (5-of-7 neighbors
positive). v1.1 params recorded in backtest_notes.md."
```

---

## Task 3: OOS robustness on DOGE, AVAX, LINK, BTC, ETH

**Goal:** Apply the v1.1 params unchanged to 5 OOS symbols. The acceptance bar's portability check.

**Files:**
- Append: `strategies/bull-aggro-ignition/backtest_notes.md`

- [ ] **Step 1: Lock the params — set inputs once to v1.1 and confirm**

```
mcp__tradingview-mcp__indicator_set_inputs  (set all knobs to the v1.1 values from Task 2 Step 10)
```
On SOL 60m (or chosen TF), re-run `data_get_strategy_results` and confirm metrics match Task 2's chosen-cell row (sanity check that inputs persisted).

- [ ] **Step 2: OOS on DOGE**

```
mcp__tradingview-mcp__chart_set_symbol  symbol=KRAKEN:XDGUSD
mcp__tradingview-mcp__chart_set_timeframe  timeframe=<v1.1 TF>
mcp__tradingview-mcp__data_get_strategy_results
mcp__tradingview-mcp__data_get_trades  max_trades=300
```
Append metrics to `backtest_notes.md` Task 3 table.

- [ ] **Step 3: OOS on AVAX**

```
mcp__tradingview-mcp__chart_set_symbol  symbol=KRAKEN:AVAXUSD
mcp__tradingview-mcp__data_get_strategy_results
```
Append row.

- [ ] **Step 4: OOS on LINK**

```
mcp__tradingview-mcp__chart_set_symbol  symbol=KRAKEN:LINKUSD
mcp__tradingview-mcp__data_get_strategy_results
```
Append row.

- [ ] **Step 5: OOS on BTC**

```
mcp__tradingview-mcp__chart_set_symbol  symbol=KRAKEN:XBTUSD
mcp__tradingview-mcp__data_get_strategy_results
```
Append row.

- [ ] **Step 6: OOS on ETH**

```
mcp__tradingview-mcp__chart_set_symbol  symbol=KRAKEN:ETHUSD
mcp__tradingview-mcp__data_get_strategy_results
```
Append row.

- [ ] **Step 7: Compute aggregate OOS metrics**

In `backtest_notes.md`, compute and record:
- Sum of net profit across 5 OOS symbols (notProfit, not %)
- Aggregate profit factor: sum(grossProfit) / sum(|grossLoss|)
- Symbol-positive count: how many of 6 (SOL + 5 OOS) have netProfit > 0
- Aggregate trade count
- Max DD across the set (worst single symbol)

- [ ] **Step 8: Evaluate against acceptance bar criteria 1–4**

In `backtest_notes.md` append a `## Task 3 acceptance check` block. For each criterion (PF > 1.3, ≥4/6 symbols positive, max DD < buy-hold DD, ≥30 trades):
```
- [PF criterion]    pass / fail (actual value vs threshold)
- [breadth]         pass / fail (X of 6 positive)
- [DD]              pass / fail (X% vs buy-hold Y%)
- [sample]          pass / fail (X trades vs 30)
```

If 2 or more criteria fail: **stop here**, jump to Task 6 with `decision = NO-SHIP`. Document the failure clearly. Do not attempt to re-tune to rescue OOS — that is the curve-fit failure mode the spec explicitly forbids (§7 + §9).

If 0–1 criteria fail and the failure is marginal (e.g., 28 trades vs 30, or DD slightly above): proceed to Task 4 but note the marginal failure; final decision in Task 6 weighs it.

- [ ] **Step 9: Commit**

```bash
git add strategies/bull-aggro-ignition/backtest_notes.md
git commit -m "bull-aggro-ignition: Task 3 OOS run + acceptance check

DOGE/AVAX/LINK/BTC/ETH with SOL-tuned v1.1 params unchanged. Aggregate
metrics + criteria 1-4 pass/fail recorded in backtest_notes.md."
```

---

## Task 4: Head-to-head vs approach C (cross-sectional BTC-relative-strength)

**Goal:** Build and backtest the runner-up edge (Codex-Apex-flavored cross-sectional momentum) on the same 6 symbols, same TF, same window. Compare risk-adjusted return and return correlation with Ignition.

**Files:**
- Create (TradingView): Pine script `BULL_Aggro_RS_v1` (new strategy, /BULL_* namespace)
- Create: `strategies/bull-aggro-ignition/BULL_Aggro_RS_v1.pine` (repo audit copy)
- Append: `strategies/bull-aggro-ignition/backtest_notes.md`

- [ ] **Step 1: Create the new Pine strategy**

```
mcp__tradingview-mcp__pine_new  type=strategy
```
Then `pine_set_source` with:

```pine
//@version=6
// BULL_Aggro_RS_v1 — RESEARCH PROBE (approach C head-to-head challenger)
// Cross-sectional momentum vs BTC: long when coin outperforms BTC by an edge,
// short when underperforms by edge. Single-symbol Pine using BITSTAMP:BTCUSD
// as the leader benchmark. 1x, no leverage.
strategy("BULL_Aggro_RS_v1",
     overlay=true,
     initial_capital=10000,
     default_qty_type=strategy.cash,
     default_qty_value=10000,
     currency=currency.USD,
     pyramiding=0,
     commission_type=strategy.commission.percent,
     commission_value=0.26,
     slippage=2,
     process_orders_on_close=true,
     calc_on_every_tick=false)

btcSym    = input.symbol("BITSTAMP:BTCUSD", "BTC benchmark")
rocLen    = input.int(20,  "ROC bars",         minval=5)
rsEdge    = input.float(2.0,"RS edge (% pts)", step=0.1, minval=0.0)
atrLen    = input.int(14,  "ATR length",       minval=2)
stopMult  = input.float(2.0,"Initial stop ATR mult", step=0.1, minval=0.5)
chandMult = input.float(3.0,"Chandelier trail ATR mult", step=0.1, minval=0.5)
maxBars   = input.int(48,  "Time stop bars",   minval=4)
allowLong = input.bool(true, "Allow longs")
allowShort= input.bool(true, "Allow shorts")

btcClose  = request.security(btcSym, timeframe.period, close, lookahead=barmerge.lookahead_off)

rocCoin   = ta.roc(close,    rocLen)
rocBTC    = ta.roc(btcClose, rocLen)
spread    = rocCoin - rocBTC

atr       = ta.atr(atrLen)

longSig   = spread >=  rsEdge
shortSig  = spread <= -rsEdge

var float entryPx  = na
var float initStop = na
var float trailStop = na
var float hiSince  = na
var float loSince  = na
var int   barsHeld = 0

flat   = strategy.position_size == 0
longP  = strategy.position_size > 0
shortP = strategy.position_size < 0

if flat and allowLong and longSig
    qtyL = strategy.equity / close
    strategy.entry("L", strategy.long, qty=qtyL)
    entryPx := close
    initStop := close - atr * stopMult
    trailStop := initStop
    hiSince := high
    barsHeld := 0

if flat and allowShort and shortSig
    qtyS = strategy.equity / close
    strategy.entry("S", strategy.short, qty=qtyS)
    entryPx := close
    initStop := close + atr * stopMult
    trailStop := initStop
    loSince := low
    barsHeld := 0

if longP
    barsHeld += 1
    hiSince := math.max(nz(hiSince, high), high)
    chand = hiSince - atr * chandMult
    trailStop := math.max(nz(trailStop, initStop), chand)
    stopLvl = math.max(trailStop, initStop)
    strategy.exit("Lx", "L", stop=stopLvl)
    if barsHeld >= maxBars
        strategy.close("L", comment="time")

if shortP
    barsHeld += 1
    loSince := math.min(nz(loSince, low), low)
    chand = loSince + atr * chandMult
    trailStop := math.min(nz(trailStop, initStop), chand)
    stopLvl = math.min(trailStop, initStop)
    strategy.exit("Sx", "S", stop=stopLvl)
    if barsHeld >= maxBars
        strategy.close("S", comment="time")

if flat
    barsHeld := 0
```

- [ ] **Step 2: Compile and confirm no errors**

```
mcp__tradingview-mcp__pine_smart_compile
```
Expected: `has_errors: false`. Fix any errors and recompile until clean.

- [ ] **Step 3: Save audit copy to repo**

```
mcp__tradingview-mcp__pine_get_source
```
Write returned source verbatim to `strategies/bull-aggro-ignition/BULL_Aggro_RS_v1.pine`.

- [ ] **Step 4: Backtest RS_v1 on all 6 symbols, same TF as Ignition v1.1**

For each symbol in `[KRAKEN:SOLUSD, KRAKEN:XDGUSD, KRAKEN:AVAXUSD, KRAKEN:LINKUSD, KRAKEN:XBTUSD, KRAKEN:ETHUSD]`:
```
mcp__tradingview-mcp__chart_set_symbol  symbol=<symbol>
mcp__tradingview-mcp__chart_set_timeframe  timeframe=<v1.1 TF>
mcp__tradingview-mcp__data_get_strategy_results
```
Append a markdown table to `backtest_notes.md` `## Task 4 — Approach C (BULL_Aggro_RS_v1)`:
```
| symbol | trades | win% | net$ | PF | maxDD% |
```

Note: On BTC itself, `rocCoin - rocBTC` is always 0, so the strategy is no-op. That's expected — exclude BTC from RS aggregate, or replace BTC's leader benchmark with ETH for the BTC row only (document choice).

- [ ] **Step 5: Compute aggregate RS metrics**

Sum net$, aggregate PF, count symbol-positive, total trades — same way as Task 3 Step 7.

- [ ] **Step 6: Head-to-head comparison table**

In `backtest_notes.md` append:
```
| metric                  | Ignition v1.1 | RS v1 |
|-------------------------|--------------:|------:|
| aggregate net$          |               |       |
| aggregate PF            |               |       |
| symbol-positive count   |               |       |
| max DD% (worst symbol)  |               |       |
| trade count             |               |       |
| sharpe (avg of symbols) |               |       |
```

- [ ] **Step 7: Compute return correlation (complementarity check)**

For each symbol, collect the equity-curve final values per month (or per week if monthly is too few points). Compute Pearson correlation between Ignition's and RS's monthly returns across symbols. Append:
```
return correlation Ignition vs RS: <r>
```
A correlation < 0.5 supports the "complementary" branch of acceptance criterion 5 even if one underperforms.

- [ ] **Step 8: Evaluate acceptance criterion 5**

In `backtest_notes.md`:
- If Ignition's risk-adjusted return (PF) > RS's: criterion 5 = pass (beats).
- Else if correlation < 0.5 and both are individually profitable: criterion 5 = pass (complementary).
- Else: criterion 5 = fail.

- [ ] **Step 9: Commit**

```bash
git add strategies/bull-aggro-ignition/BULL_Aggro_RS_v1.pine strategies/bull-aggro-ignition/backtest_notes.md
git commit -m "bull-aggro-ignition: Task 4 head-to-head vs approach C (RS_v1)

Built BULL_Aggro_RS_v1 (cross-sectional BTC-relative-strength). Backtested
on same 6 symbols + same TF. Head-to-head table, correlation, and
acceptance criterion 5 recorded in backtest_notes.md."
```

---

## Task 5: Contest-window slice (informational, not a gate)

**Goal:** Document what each strategy would have produced over the contest window (2026-05-04 → present) for the user's reference. NOT a promotion gate.

**Files:**
- Append: `strategies/bull-aggro-ignition/backtest_notes.md`

- [ ] **Step 1: Add date-range filter to Pine scripts (temporary input)**

For both strategies, add (via `pine_set_source` on each in turn):
```pine
startTime = input.time(timestamp("2026-05-04T00:00:00Z"), "Contest start")
endTime   = input.time(timestamp("2026-06-06T00:00:00Z"), "Contest end")
inWindow  = time >= startTime and time <= endTime
```
And wrap entries with `and inWindow`:
```pine
if flat and allowLong and bullIgnite and inWindow
    ...
if flat and allowShort and bearIgnite and inWindow
    ...
```
Recompile both. Confirm `has_errors: false`.

- [ ] **Step 2: Re-backtest both strategies on all 6 symbols within the window**

Same per-symbol loop as Tasks 3 and 4 Steps 2–6, but with the date filter active. Append a `## Task 5 — Contest window 2026-05-04..present` section to `backtest_notes.md`:
```
| strategy | symbol | trades | net$ | PF | notes |
```

- [ ] **Step 3: Compute aggregate contest-window net P&L for each strategy**

Add summary lines:
```
Ignition v1.1 contest-window total net $: <X>
RS v1        contest-window total net $: <X>
```
Note explicitly: **these are backtest numbers, not forward — they may NOT be claimed on the leaderboard.** Repeat the off-leaderboard reminder.

- [ ] **Step 4: Remove date-range filter from both Pine scripts**

`pine_set_source` for both, removing the `startTime`/`endTime`/`inWindow` additions so future runs are unrestricted. Recompile both; confirm clean.

- [ ] **Step 5: Update repo audit copies**

For each script, `pine_get_source` and overwrite `strategies/bull-aggro-ignition/BULL_Aggro_Ignition_v1.pine` and `strategies/bull-aggro-ignition/BULL_Aggro_RS_v1.pine` with the de-filtered source.

- [ ] **Step 6: Commit**

```bash
git add strategies/bull-aggro-ignition/backtest_notes.md strategies/bull-aggro-ignition/BULL_Aggro_Ignition_v1.pine strategies/bull-aggro-ignition/BULL_Aggro_RS_v1.pine
git commit -m "bull-aggro-ignition: Task 5 contest-window backtest slice

Informational only (not a promotion gate). Filter applied/removed; both
audit copies refreshed. Numbers labeled clearly as backtest, off-leaderboard."
```

---

## Task 6: Decision — ship to forward paper, or stop

**Goal:** Apply the acceptance bar deterministically. If all 5 criteria pass: spin a forward-paper strategy entry. If any fail: write a failure summary, do nothing else.

**Files:**
- Append: `strategies/bull-aggro-ignition/backtest_notes.md`
- **Conditional (PASS only):**
  - Create: `strategies/bull-aggro-ignition/portfolio.md`
  - Create: `strategies/bull-aggro-ignition/trade_log.md`
  - Modify (separate repo, separate commit, separate user-approved push): `C:/Users/Mhair/OneDrive/Desktop/strategy-leaderboard/registry.js`

- [ ] **Step 1: Tabulate the 5 acceptance criteria**

In `backtest_notes.md` append `## Task 6 — Acceptance decision`. For each criterion from spec §7:
```
1. Aggregate PF > 1.3 OOS:                pass / fail (value X)
2. ≥ 4 of 6 symbols net positive:         pass / fail (X of 6)
3. Max strategy DD < buy-hold DD:         pass / fail (X% vs Y%)
4. ≥ 30 closed trades aggregate OOS:      pass / fail (X trades)
5. Beats or complements approach C:        pass / fail (rationale)
```

- [ ] **Step 2: Branch on the result**

If **all 5 pass** → continue to Step 3 (SHIP branch).
If **any fail** → skip to Step 9 (NO-SHIP branch).

### SHIP branch (Steps 3–8 — execute only if all 5 pass)

- [ ] **Step 3: Create forward-paper portfolio.md**

Create `strategies/bull-aggro-ignition/portfolio.md`:
```markdown
# BULL_Aggro_Ignition — Forward Paper Portfolio

> **LEADERBOARD-SOURCED — FORWARD PAPER-PAPER ONLY.** This file is rebuilt only
> from this strategy's forward `trade_log.md`. Never reflect backtest /
> reconstructed P&L here — backtest findings live in `backtest_notes.md`, which
> the leaderboard does not read.
> **Last rebuild:** <YYYY-MM-DDTHH:MMZ> (initial spin-up)

## Account
- Starting equity: **$10,000.00**
- Cash: **$10,000.00**
- Realized PnL: **$0.00**
- Unrealized PnL: **$0.00**
- Current equity: **$10,000.00**
- Equity peak: **$10,000.00**
- Drawdown: **0.00%**

## Open positions
(none)

## Days live
- Spin-up: <today ISO date>
- Promotion / kill review: ongoing; weekly memo addendum.

## Notes
Forward paper-paper only. Backtest validation passed §7 acceptance bar; see
backtest_notes.md for the audit trail. SBD-style hygiene applies — backtest
numbers must never appear in this file.
```

- [ ] **Step 4: Create forward-paper trade_log.md**

Create `strategies/bull-aggro-ignition/trade_log.md`:
```markdown
# BULL_Aggro_Ignition — Forward Trade Log

> **LEADERBOARD-SOURCED — FORWARD PAPER-PAPER ONLY.** Never write backtest /
> reconstructed / hypothetical-historical rows here. Defense-in-depth: the
> leaderboard registry entry sets `live_start_iso` to the spin-up date, so
> the adapter filters out any trade entered before then even if one is
> mistakenly added.

| Timestamp (UTC) | Event | Pair | Side | Size | Price | Stop | Target | R at exit | Realized PnL | Reason tag |
|-----------------|-------|------|------|------|-------|------|--------|-----------|--------------|------------|

(empty — spun up <today>)
```

- [ ] **Step 5: Commit the trading-bull additions**

```bash
git add strategies/bull-aggro-ignition/portfolio.md strategies/bull-aggro-ignition/trade_log.md strategies/bull-aggro-ignition/backtest_notes.md
git commit -m "bull-aggro-ignition: SHIP — acceptance bar passed, forward paper

All 5 spec §7 criteria pass (recorded in backtest_notes.md). Forward
paper portfolio + trade_log created with forward-only banners. Leaderboard
registry entry follows in the strategy-leaderboard repo."
```

- [ ] **Step 6: Add the leaderboard registry entry**

In `C:/Users/Mhair/OneDrive/Desktop/strategy-leaderboard/registry.js`, immediately after the `BULL v0.12-SBD (twin)` block, add:
```javascript
{
  // BULL_Aggro_Ignition — convex momentum-ignition crypto strategy, shipped
  // to forward paper after passing spec §7 acceptance (see trading-bull
  // strategies/bull-aggro-ignition/backtest_notes.md for the validation
  // audit trail). live_start_iso = honest ship date — backtest P&L must
  // NEVER be claimed on the leaderboard.
  name: 'BULL Aggro Ignition',
  starting_capital: 10000,
  killswitch_dd_pct: 25,
  live_start_iso: '<today ISO date>T00:00:00Z',
  source: {
    type: 'bull-github',
    portfolio_path: 'strategies/bull-aggro-ignition/portfolio.md',
    trade_log_path: 'strategies/bull-aggro-ignition/trade_log.md',
  },
  adapter: adaptBull,
},
```

- [ ] **Step 7: Run the leaderboard test suite**

```bash
cd "C:/Users/Mhair/OneDrive/Desktop/strategy-leaderboard"
npm test
```
Expected: all tests pass (currently 108/108). If any fail, fix the registry entry and re-run.

- [ ] **Step 8: Smoke + ask user before pushing the registry change**

```bash
cd "C:/Users/Mhair/OneDrive/Desktop/strategy-leaderboard"
npm run smoke
```
Confirm `BULL Aggro Ignition` row renders cleanly with `0 trades / 0.0%` (fresh spin-up) and no errors.

**STOP — ask user explicitly:** "Acceptance bar passed. Trading-bull ship is committed; ready to commit + push the strategy-leaderboard registry entry to `main`. OK to push?"

Do not push without explicit `yes`. Push only the staged `registry.js` change (mirror the prior surgical-staging approach if registry.js has unrelated uncommitted churn).

After push (only if approved):
```bash
cd "C:/Users/Mhair/OneDrive/Desktop/trading-bull/.claude/worktrees/suspicious-mcnulty-b037cd"
git push origin HEAD:main
```
Also push the trading-bull commits (Tasks 1–6 ship branch) to main, with the same rebase/conflict pattern used earlier this session (fetch, rebase onto origin/main, push).

Mark this task complete only after both repos are in sync.

### NO-SHIP branch (Step 9 — execute only if any criterion failed)

- [ ] **Step 9: Write failure summary and stop**

In `backtest_notes.md` append `## Task 6 — NO-SHIP decision`:
```
Result: ACCEPTANCE BAR NOT MET. Strategy does not ship to forward paper.

Failed criteria:
- <list each failed criterion with actual value vs threshold>

Honest summary:
<2-3 sentence plain-English explanation of why the edge did not generalize.
Examples: 'curve-fit to SOL — failed on 4 of 5 OOS symbols';
'positive in aggregate but DD exceeds buy-hold'; 'too few trades to trust'.>

Decision: do NOT create portfolio.md / trade_log.md. Do NOT add a leaderboard
registry entry. Strategy stays in R&D. Possible future paths:
- Different edge concept (see spec §3 approach A or revisit C in isolation)
- Different universe / timeframe
- Different signal mechanics
These are out of scope for this plan.
```

Commit:
```bash
git add strategies/bull-aggro-ignition/backtest_notes.md
git commit -m "bull-aggro-ignition: NO-SHIP — acceptance bar not met, R&D closed

Failure summary recorded in backtest_notes.md. No portfolio.md/trade_log.md
created; no leaderboard registry entry. Curve-fit-avoidance discipline held."
```

Then **STOP**. Do not iterate the same strategy hoping it will pass on re-tune — that is exactly the curve-fit failure spec §7 + §9 forbid. A new design needs a new spec + brainstorm cycle.

---

## Self-Review Notes (post-write)

- **Spec coverage:** §1 goal (Tasks 1–6); §2 edge thesis (encoded in Task 1 Pine source); §3 rules (Task 1 fixes, Task 2 tunes); §4 risk model (`strategy.cash`, no leverage — Task 1); §5 namespace + leaderboard hygiene (Task 1 file creation, Task 6 banners, Task 6 Step 6 registry); §6 validation steps 1–6 map directly to Tasks 1–6; §7 acceptance bar referenced in Tasks 3, 4, 6 explicitly; §8 non-goals respected throughout; §9 open risks: late-entry slippage measured in Tasks 3/4 results, sparse sample handled by Task 3 Step 8 stop-rule, curve-fit guard is Task 3 Step 8 + Task 6 §7 enforcement.
- **Placeholder scan:** clean — no TBD/TODO; all sweeps have concrete grids; all decision rules are explicit; pass/fail thresholds are numeric.
- **Type/name consistency:** `BULL_Aggro_Ignition_v1` and `BULL_Aggro_RS_v1` used consistently. Param names (`rangeMult`, `volMult`, `rocZMin`, etc.) match between Task 1 source and Task 2 sweep grid. File paths under `strategies/bull-aggro-ignition/` consistent across tasks.
- **One known-quirk:** Pine's `strategy.cash` + explicit `qty=strategy.equity/close` is intentionally redundant to belt-and-suspenders fix the sizing bug. If the explicit `qty` works, `default_qty_value=10000` is moot — that's fine; document in Task 1 Step 8 if the sizing fix renders the cash default unused.
