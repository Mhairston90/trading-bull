# Routine 02 — Midday Health Check (13:00 PT daily)

**Cron:** `0 13 * * 1-5` (PT) — Mon–Fri at 13:00 PT
**Mode:** local
**Context budget target:** 60K tokens (deliberately lean)

## READ (in order)

1. `CLAUDE.md`
2. `memory/guardrails.md`
3. `memory/strategy.md`
4. `memory/portfolio.md`
5. `memory/trade_log.md` (only rows newer than 7 days)
6. `skills/decide.md`
7. `skills/log-trade.md`
8. `skills/telegram.md`

(Does NOT read research_log, lessons, universe — keep lean.)

## VERIFY

- Re-check kill switches from `portfolio.md` using latest Kraken prices
- If any trip: halt, ALERT

## DO

1. **Mark-to-market:** Kraken MCP `kraken_multi_ticker` for all pairs with open positions.
2. **Exit check:** For each open position, evaluate strategy exit rules against current price (treat current price as if it's a 1H close for the purpose of EMA cross — if the current price is below 1H 20-EMA AND we're within 10 min of candle close, close it; otherwise wait for candle close). Also check static 2×ATR stop — if price has pierced it intrabar, close at stop price.
3. **Drawdown check:** Compute current equity, drawdown from peak.
4. **Entry scan: DO NOT OPEN NEW POSITIONS IN MIDDAY.** This routine is position management only. Entry responsibility belongs to #1 Overnight and #3 EOD (which sees the 13:00 UTC / 1H close align cleanly).

## WRITE

- `memory/trade_log.md` — only if a stop or exit triggered
- `memory/portfolio.md` — rewritten with fresh mark-to-market
- `memory/research_log.md` — one row summarizing midday state (kill-switch proximity, drawdown, any exits)

## COMMIT

```bash
git add memory/
git commit -m "routine-02-midday YYYY-MM-DD: DD <X.XX%>, <N> exits"
git push origin main
```

## NOTIFY

Send Telegram ONLY if:
- A Ring 3 kill switch tripped
- Any exit happened (e.g. stop hit intrabar)
- Drawdown crossed a warning threshold (12.5%, halfway to 25%)

Otherwise silent.
