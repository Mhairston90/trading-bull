# Routine 01 — Overnight Recap (06:00 PT daily)

**Cron:** `0 6 * * 1-5` (PT) — Mon–Fri at 06:00 PT
**Mode:** local (this machine, this Claude Code)
**Context budget target:** 100K tokens

## READ (in order)

1. `CLAUDE.md`
2. `memory/guardrails.md`
3. `memory/strategy.md`
4. `memory/portfolio.md`
5. `memory/universe.md`
6. `memory/trade_log.md` (only rows newer than 30 days)
7. `memory/research_log.md` (only rows newer than 7 days)
8. `memory/lessons.md`
9. `skills/decide.md`
10. `skills/log-trade.md`
11. `skills/research.md`
12. `skills/telegram.md`

## VERIFY

- Confirm no Ring 3 kill switch is tripped (read `portfolio.md` kill-switch state section)
- If tripped: skip to NOTIFY step with status quo, do not open new positions

## DO

1. **Overnight price pull:** Kraken MCP `kraken_multi_ticker` for all 15 universe pairs. Note % moves since yesterday 21:00 PT.
2. **Position check on each open position:** Did price action overnight hit any stops? If so, execute paper exit at stop price, log to trade_log, rebuild portfolio. (This is the only path that closes during this routine.)
3. **Entry scan:** For each pair in universe not currently open, fetch 1H + 4H OHLCV and check entry conditions per `strategy.md`. Compute indicators in-line.
4. **News scan:** Use `skills/research.md` — pull CoinDesk + TheBlock front pages via Firecrawl, extract 24h headlines, classify.
5. **Place eligible new entries:** For each entry signal that passes `pre_entry_check` (see `skills/decide.md`), append OPEN row to `trade_log.md`, rebuild `portfolio.md`.
6. **Append research_log entries** for every news item and every REJECTed entry (with reason).
7. **First-of-month universe refresh:** If today is the 1st (or first weekday of month if 1st is weekend): query `kraken_pairs` + compute 30d volumes, rewrite `memory/universe.md` with top 15. Commit separately.

## WRITE

- `memory/trade_log.md` — any new OPEN or stop-out CLOSE rows
- `memory/portfolio.md` — rewritten from trade log
- `memory/research_log.md` — news + rejects
- `memory/universe.md` — only on first-of-month
- `memory/lessons.md` — only if news cluster or notable price anomaly triggers an entry

## COMMIT

```bash
git add memory/
git commit -m "routine-01-overnight YYYY-MM-DD: <N> trades, <N> research items"
git push origin main
```

If no changes: commit with `--allow-empty` and message `routine-01-overnight YYYY-MM-DD: no action`.

## NOTIFY

Send Telegram via `scripts/telegram_send.py` ONLY if any of:
- A Ring 3 kill switch tripped → ALERT template
- Any new OPEN or stop-out CLOSE during this run → brief summary
- A news item was classified ACTIONABLE → headline + impact line
- Universe was refreshed → "universe refreshed: <new pairs in> / <dropped>"

Otherwise silent. Absence of message = "all clear, nothing to flag."
