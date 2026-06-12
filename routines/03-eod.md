# Routine 03 — End-of-Day Journal (21:00 PT daily)

**Cron:** `0 21 * * 1-5` (PT) — Mon–Fri at 21:00 PT
**Mode:** local
**Context budget target:** 120K tokens

> **Date-labeling guard (added 2026-06-11):** this wake fires at 21:00+ PT, which is already the **next calendar day in UTC** (04:00–05:00Z). Label the EOD journal, the commit message, and all "today" references with the **PT calendar date at fire time** — never the UTC date. Sanity check before WRITE: the label date must equal today's PT date. (Commit `6d9102b`, the 06-10 PT EOD, mislabeled its body "Thu 21:00 PT"; routine #7 made the same +1-day error twice.)

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
3. **EOD entry scan (W19-E analyst-role split):** For each universe pair without open position, run the three analyst passes:
   - **Technical:** check entry conditions per `strategy.md` (rules 1, 2, 2a, 3, 4, 4a, 5, 5a, 5b, 6, 6a, 7, 8) on just-closed 1H candle. **Indicator computation (amended 2026-06-12): run `python scripts/indicators.py` and treat its table as authoritative** (720-bar converged EMA/RSI/ATR, per-rule margins, regime 5a/SBD, 2×ATR stops). Do NOT compute indicators in-line when the script is available — in-context math produced the $584 50-EMA error on 06-11. Fallback only if the script fails: ≥ 200 4H bars for the 50-EMA; < 150 bars → rule 3 LOW-CONFIDENCE.
   - **News:** for each technical-PASS candidate, Firecrawl scan headlines (CoinDesk + TheBlock, past 6h, base-asset tagged), tag `neutral / supportive / contradictory`. Informational only — does NOT veto in v0.2.
   - **Sentiment:** Kraken `kraken_spread` + `kraken_depth` per candidate. Informational only.
   Execute eligible entries. Log to `research_log.md` using the W19-E schema (Technical / News / Sentiment / Decision subsections).
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
