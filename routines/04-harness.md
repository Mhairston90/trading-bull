# Routine 04 — AutoStrategy Harness (Sat 10:00 PT weekly)

**Cron:** `0 10 * * 6` (PT) — Saturday at 10:00 PT
**Mode:** local — REQUIRES TradingView Desktop app running
**Context budget target:** 180K tokens (heaviest routine)

## DAY GATE (run first, before anything else)

Claude Code Desktop runs this Daily, not weekly. Before doing any work, check today's day of week (US Pacific). If today is NOT Saturday, do these 4 things and STOP:
1. Append one row to `memory/research_log.md`: `<UTC timestamp> | harness | day-gate | not Saturday, skipping | no action`
2. `git add memory/research_log.md`
3. `git commit --allow-empty -m "routine-04-harness: day-gate skip (not Sat)"`
4. `git push origin main`
Then exit. Do not READ the rest of the files, do not run TradingView, do not propose anything.

If today IS Saturday, proceed with the full routine below.

## READ (in order)

1. `CLAUDE.md`
2. `memory/guardrails.md`
3. `memory/strategy.md`
4. `memory/portfolio.md`
5. `memory/trade_log.md` (last 90 days)
6. `memory/research_log.md` (last 30 days)
7. `memory/lessons.md`
8. `memory/weekly_memos/` — previous 4 weeks
9. `memory/idea_bank.md` — focus on rows with `status: raw` or `under-review` (added W19, idea-mining subsystem)
10. **Competitor data (read-only, external — added 2026-04-29 per user grant):**
    - `C:\Users\Mhair\OneDrive\Desktop\strategy-leaderboard\registry.js` — full strategy registry (BULL + Codex + others)
    - `C:\Users\Mhair\OneDrive\Desktop\strategy-leaderboard\data\codex\portfolio.md` — Codex v0 current state
    - `C:\Users\Mhair\OneDrive\Desktop\strategy-leaderboard\data\codex\trade_log.md` — Codex v0 trade history
    - `C:\Users\Mhair\OneDrive\Desktop\strategy-leaderboard\data\codex\aggro_portfolio.md` — Codex Aggro v0
    - `C:\Users\Mhair\OneDrive\Desktop\strategy-leaderboard\data\codex\aggro_trade_log.md` — Codex Aggro v0 trades
    - **NEVER write to or modify these files** — read-only competitive intelligence
11. `skills/decide.md`
12. `skills/telegram.md`

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
   - **`idea_bank.md` rows with `status: raw` or `under-review` and `score >= 10`** (W19 idea-mining subsystem). Treat as candidate variants on equal footing with internal lessons; if backtested and selected, mark the bank row `proposal-drafted`. If rejected, mark `pruned` with reason.
   - **Competitor-informed structural observations.** Inspect Codex's `portfolio.md` and `trade_log.md` for trades and structural choices (sleeve model, exposure caps, kill-switch tolerances). Note differences vs BULL's mandate. Where Codex's structural choices look interesting AND compatible with BULL's locked mandate (spot-only, 4% port risk, 1.5%/trade, $10K, 8 positions), consider them as variant candidates. Where they violate mandate (e.g., gross exposure > 100%, leverage proxies), explicitly document the violation in the memo and DO NOT propose. Competitor performance is a benchmark to beat by 2026-07-01, not an instruction to copy.
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
