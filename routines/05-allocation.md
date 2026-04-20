# Routine 05 — Allocation Review (Sun 10:00 PT weekly)

**Cron:** `0 10 * * 0` (PT) — Sunday at 10:00 PT
**Mode:** local
**Context budget target:** 120K tokens

## READ (in order)

1. `CLAUDE.md`
2. `memory/guardrails.md`
3. `memory/strategy.md`
4. `memory/portfolio.md`
5. `memory/trade_log.md` (last 90 days)
6. `memory/weekly_memos/` — current + previous 4 weeks
7. `memory/lessons.md`
8. `skills/telegram.md`

## VERIFY

- Kraken MCP responding
- If a proposal from routine #4 is pending approval: check for user reply in the user-provided Telegram reply text. If found, apply or reject per instruction before doing any allocation work.

## DO

1. **Compute concept-bucket performance** over the last 90 days:
   - For each bucket declared in `strategy.md` (momentum / mean-reversion / news-reactive):
     - Trades attributable to this bucket (via reason tag on trade_log)
     - Win rate, average R, contribution to total PnL
2. **Compute vs BTC-hold:**
   - BULL return over last 90 days
   - BTC spot return over same 90 days
   - Delta
3. **Propose allocation shift (if any):**
   - If any bucket has a negative-PnL rolling 30-day AND positive-PnL rolling 90-day, leave it alone (could be noise)
   - If any bucket has a negative rolling 90-day, propose reducing its allocation by up to 20% (or zeroing it if it has never been positive)
   - If a bucket has been consistently strong (top-quartile R over 90d), propose increasing allocation by up to 20%
   - **Proposals >20% are Ring 2 gated** per guardrails
4. **Apply pending strategy edits:** If routine #4's proposal got a `Y` reply since the Sunday before:
   - Apply the diff to `memory/strategy.md`
   - Commit with message `feat(strategy): apply W<NN> proposal — <headline>`
   - Append to strategy.md's `Last approved` line with date and memo reference
5. **Write allocation memo section** into the current weekly memo (same file as routine #4):

```markdown
## Allocation review (Sunday)

| Bucket | % of trades | Contribution to PnL | Rolling 30d R | Rolling 90d R | Proposal |
|--------|-------------|---------------------|---------------|---------------|----------|

## vs BTC-hold rolling windows
| Window | BULL | BTC-hold | Delta |
|--------|------|----------|-------|

## Allocation change proposed: yes | no
<if yes: exact new bucket weights + rationale>
```

## WRITE

- `memory/weekly_memos/YYYY-Www.md` — append allocation section
- `memory/strategy.md` — only if user approved a previous proposal (this routine is the one that applies)
- `memory/research_log.md` — one row summary

## COMMIT

Separate commits if multiple logical changes:

```bash
git add memory/strategy.md
git commit -m "feat(strategy): apply W<NN> proposal — <headline>"

git add memory/weekly_memos/ memory/research_log.md
git commit -m "routine-05-allocation YYYY-Www: allocation proposal <yes|no>"

git push origin main
```

## NOTIFY

**Mandatory weekly allocation digest.** Format:

```
📈 BULL Sunday Review — W17

vs BTC-hold:
  7d: BULL +0.4% / BTC +0.1% / Δ +0.3%
  30d: +1.2% / +0.8% / Δ +0.4%
  90d: +3.5% / +2.1% / Δ +1.4%

Concept buckets:
  momentum:       100% allocation, 12 trades, +1.8R avg
  mean-reversion:   0% (not in strategy v0)
  news-reactive:    0% (not in strategy v0)

Proposal: <none | Y/N gated message per template>
Applied W<NN> strategy change: <yes + headline | no>
```
