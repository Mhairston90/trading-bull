# Routine 04 — AutoStrategy Harness (Sat 10:00 PT weekly)

**Cron:** `0 10 * * 6` (PT) — Saturday at 10:00 PT
**Mode:** local — REQUIRES TradingView Desktop app running
**Context budget target:** 180K tokens (heaviest routine)

## READ (in order)

1. `CLAUDE.md`
2. `memory/guardrails.md`
3. `memory/strategy.md`
4. `memory/portfolio.md`
5. `memory/trade_log.md` (last 90 days)
6. `memory/research_log.md` (last 30 days)
7. `memory/lessons.md`
8. `memory/weekly_memos/` — previous 4 weeks
9. `skills/decide.md`
10. `skills/telegram.md`

## VERIFY

- TradingView Desktop is running and MCP connected (`tv_health_check` via TradingView MCP)
- Kraken MCP responding (`kraken_ticker` on BTC/USD smoke test)

If either fails: skip harness, write skip reason to research_log, Telegram ALERT.

## DO

1. **Gather evidence (current week's trades):**
   - Win rate, average R, max drawdown, trade count
   - Per-entry-rule performance if strategy has multiple rules
   - Rolling 30/90-day vs BTC-hold
2. **Generate 3–5 strategy variants** that are candidates to beat current strategy. Variants come from:
   - Lessons marked with score ≥7
   - Pattern observations in research_log (news clusters, gap events)
   - Parameter tweaks to current strategy
   - New entry rules (e.g. add RSI extremes for mean-reversion)
3. **Backtest each variant** using TradingView MCP:
   - Create Pine Script in `/BULL_variant_<name>` namespace
   - Load on a 1H SOL/USD chart (or whichever pair had most current-strategy activity)
   - Run strategy over last 180 days
   - Pull metrics via `data_get_strategy_results`
4. **Rank variants vs current strategy control:**
   - Must beat on net return AND profit factor
   - Must not increase max drawdown by >25%
   - Ties broken by trade count (prefer more trades — stronger statistical base)
5. **Select up to 1 variant to propose.** (More than 1 fragments attention and approval.)
6. **Write weekly memo** to `memory/weekly_memos/YYYY-Www.md`:

```markdown
# Weekly Memo YYYY Week WW

## Performance this week
- Trades: N (win rate X%)
- PnL: $XXX (±Y.YY%)
- Drawdown: Z.ZZ%
- vs BTC-hold: ±W.WW%

## Lessons added this week
- <bullet list from lessons.md additions>

## Variants tested
| Variant | Net return | PF | DD | Trades | Verdict |
|---------|------------|----|----|--------|---------|

## Proposal (or "none — current strategy retained")
Change: <exact diff to strategy.md>
Evidence: <backtest numbers>
Risk: <what could go wrong>
Expected impact: <best estimate in R/trade or %/week>

## Open questions for user
<any judgment calls BULL can't make on its own>
```

7. **Prune lessons:** If `lessons.md` has >50 entries, sort by score desc, drop below 50. Log prune count in memo.

## WRITE

- `memory/weekly_memos/YYYY-Www.md` — new memo
- `memory/lessons.md` — pruned if needed, with score updates
- `memory/research_log.md` — one row with harness summary

## COMMIT

```bash
git add memory/
git commit -m "routine-04-harness YYYY-Www: <N> variants, proposal <yes|no>"
git push origin main
```

## NOTIFY

**Mandatory weekly memo digest.** If a proposal exists, use gated approval template from `skills/telegram.md`. If no proposal, send a short retention note:

```
BULL W17 memo — no change proposed
Current strategy retained. Evidence: <1-line rationale>.
See weekly_memos/2026-W17.md.
```

## GATED APPROVAL WAIT

After sending the approval request:
- Do NOT edit `memory/strategy.md` until user replies in Telegram chat
- The user's reply is read in the next routine wake (#5 Sunday or #1 Monday)
- If user replies `Y`: routine #5 or #1 applies the diff to `strategy.md`, commits with approval reference, notifies "applied"
- If user replies `N`: routine #5 or #1 appends a rejection note to the memo, notifies "rejected"
- If 24h elapses with no reply: auto-reject, same as `N`
- (v1 gating is informal — user replies in Telegram, next routine reads Telegram manually via user paste. Polling getUpdates is a v2.)
