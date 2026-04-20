# Routine 03 — End-of-Day Journal (21:00 PT daily)

**Cron:** `0 21 * * 1-5` (PT) — Mon–Fri at 21:00 PT
**Mode:** local
**Context budget target:** 120K tokens

## READ (in order)

1. `CLAUDE.md`
2. `memory/guardrails.md`
3. `memory/strategy.md`
4. `memory/portfolio.md`
5. `memory/trade_log.md` (last 30 days)
6. `memory/research_log.md` (last 7 days)
7. `memory/lessons.md`
8. `skills/decide.md`
9. `skills/log-trade.md`
10. `skills/telegram.md`

## VERIFY

- Re-check kill switches with latest Kraken prices
- Confirm day's activity in trade_log matches expectations from routine #1 + #2 logs

## DO

1. **Final mark-to-market:** Kraken prices as of 21:00 PT close.
2. **Post-close exit check:** Each open position against just-closed 1H candle. Trigger exits per strategy.md rules. Log + rebuild portfolio.
3. **EOD entry scan:** For each universe pair without open position, check entry conditions on just-closed 1H candle. Execute eligible entries.
4. **Extract lessons:** Review today's trades:
   - Any pair stopped out with large gap? → lesson about gap risk
   - Any winners that went well past 4R before we took profit? → lesson about target placement
   - Any entry that immediately reversed? → lesson about entry timing
   - Append up to 2 lessons per day to `lessons.md` (not more; prune weekly).
5. **Compute day's summary stats:**
   - Day PnL ($, %)
   - Trades opened, trades closed, win rate today
   - New equity, drawdown
   - Rolling 7/30-day BULL vs BTC-hold performance
6. **Monthly archive:** If today is the last trading day of the month, move rows older than 30 days from `trade_log.md` and `research_log.md` into `memory/archive/YYYY-MM.md`.

## WRITE

- `memory/trade_log.md` — new entries/exits from this wake
- `memory/portfolio.md` — rewritten
- `memory/research_log.md` — one row with EOD summary numbers
- `memory/lessons.md` — up to 2 new lesson entries (if material)
- `memory/archive/YYYY-MM.md` — only on last trading day of month

## COMMIT

```bash
git add memory/
git commit -m "routine-03-eod YYYY-MM-DD: equity $X,XXX, day <+X.XX%>, <N> trades"
git push origin main
```

## NOTIFY

**Mandatory daily EOD card.** Format per `skills/telegram.md` EOD template:

```
📊 BULL EOD — YYYY-MM-DD

Equity: $X,XXX.XX (±Y.YY%)
Day PnL: ±$XXX (±Y.YY%)
Since start: ±Y.YY%
Drawdown: Z.ZZ%

Trades today: N opened, M closed
- <event lines if any>

Open positions: K/8
Status: ✅ all clear | ⚠️ warning | 🚨 kill switch

vs BTC-hold (rolling 30d): ±W.WW%

Notes:
- <up to 3 bullet lessons or observations>
```
