# Skill: Making Entry/Exit Decisions

Used by routines #1, #2, #3 when BULL evaluates whether to open or close a paper position.

## Decision flow (per pair per wake)

```
1. Read current strategy from memory/strategy.md
2. Read guardrails from memory/guardrails.md
3. Read current portfolio from memory/portfolio.md
4. For each pair in memory/universe.md:
   a. Fetch Kraken 1H + 4H OHLCV via Kraken MCP (last 60 bars 1H, 60 bars 4H)
   b. Compute required indicators (EMA, RSI, ATR) per strategy.md
   c. Check entry conditions — ALL must be true
   d. If entry conditions pass:
      - Verify guardrails (position count, portfolio risk)
      - Size the position per strategy.md
      - Place paper trade (append to trade_log.md)
5. For each open position:
   a. Fetch latest Kraken 1H close
   b. Check exit conditions from strategy.md
   c. If any exit triggers:
      - Close paper position (append to trade_log.md)
      - Update portfolio.md
```

## How to compute indicators

BULL does NOT run its own Python indicator libraries in routines. Use one of:

- **Kraken MCP** `kraken_ohlcv` + compute EMA/RSI/ATR arithmetically in the prompt (small series, tractable)
- **TradingView MCP** `data_get_study_values` on a BULL-namespaced chart if already loaded

For v0 seed strategy, indicators are simple enough for arithmetic:
- 20-EMA = exponential smoothing with α = 2/(20+1)
- RSI(14) = standard gain/loss ratio over 14 bars
- ATR(14) = average true range over 14 bars

Show your work in the research_log when computing, so it can be audited.

## Paper trade rules

- "Fill" price = just-closed candle's close + half a tick of slippage (add 0.05% for the conservative model)
- No partial fills, no queue — assume full size fills at the model price
- Commission: 0.26% per side (Kraken taker) — deducted from PnL in trade_log
- No short side in v0 (strategy is long-only)

## Guardrail pre-check (MUST run before every paper fill)

```
pre_entry_check(pair, size, entry, stop):
    if len(open_positions) >= 8: REJECT "position cap"
    if len(open_positions) >= strategy.max_concurrent: REJECT "strategy cap"
    if (open_positions_risk + new_trade_risk) > 0.04 * equity: REJECT "portfolio risk"
    if new_trade_risk > 0.015 * equity: REJECT "per-trade risk"
    if pair not in universe: REJECT "off-universe"
    if pair in [p.pair for p in open_positions]: REJECT "already open"
    if daily_loss_pct > 0.05: REJECT "kill switch"
    if equity < 7500: REJECT "floor"
    return ACCEPT
```

Every REJECT is logged to research_log with reason.

## Exit execution

On exit trigger:
- Close at 1H candle close (same conservative slippage model: 0.05%)
- Compute realized PnL in USD and R-multiple
- Append two rows to trade_log: the exit event + the closing pair's summary row
- Update portfolio.md
- If exit was a stop-out and 2 stops have hit in last 24h for same pair → append a lesson to lessons.md (pattern detection)
