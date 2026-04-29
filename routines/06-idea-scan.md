# Routine 06 — Idea Scan (Friday 18:00 PT weekly)

**Cron:** `0 18 * * 5` (PT) — Fridays at 18:00 PT (runs before Saturday's routine #4 harness so fresh ideas are available for memo drafting)
**Mode:** local
**Context budget target:** 80K tokens

## Purpose

Harvest the past week's content from curated quants/researchers in `memory/idea_sources.md`, extract testable claims, score them, append to `memory/idea_bank.md`. **Idea generation only — never trade authority.**

## READ (in order)

1. `CLAUDE.md`
2. `memory/guardrails.md`
3. `memory/idea_sources.md`
4. `memory/idea_bank.md` (last 90 days, for de-dup)
5. `skills/idea-scan.md`

(Does NOT read strategy.md, portfolio.md, trade_log.md, research_log.md — idea-scan is isolated from trade state by design.)

## VERIFY

- Confirm `FIRECRAWL_API_KEY` is set in environment
- If not: log to `research_log.md` and exit cleanly (no failure, just skip)
- Confirm `idea_sources.md` has at least 1 active source — if not, exit and ALERT in routine #4

## DO

1. **Day-gate:** if today is not Friday → exit with single research_log row `not Friday, skipping`. (Same pattern as routines #4 / #5.)
2. **Per-source harvest:** follow `skills/idea-scan.md` procedure for each active source. Process sources sequentially; allow ~5K tokens per source budget.
3. **De-dup against bank:** before appending, check `idea_bank.md` for any active row (`raw / under-review / proposal-drafted / applied`) with semantic-match claim. Skip if duplicate.
4. **Score and filter:** apply `score >= 8` floor. Drop below-floor ideas without appending.
5. **Append survivors:** new rows in `idea_bank.md` with `status: raw`.
6. **Source health:** for each source, record fetch outcome (success / 404 / no-recent-content / Firecrawl error) for routine #4 quarterly review.

## WRITE

- `memory/idea_bank.md` — new `raw` rows for surviving claims
- `memory/research_log.md` — one summary row using **legacy** single-line schema:
  ```
  YYYY-MM-DDTHH:MMZ | idea-scan | system | <N> sources fetched, <M> claims extracted, <K> survived score floor, <L> deduped, <P> appended | no trade action
  ```
  (Idea-scan does not use the W19-E analyst-role schema — no entry decision is made.)

## COMMIT

```bash
git add memory/idea_bank.md memory/research_log.md
git commit -m "routine-06-idea-scan YYYY-MM-DD: <N> sources, <P> new ideas appended"
git push origin main
```

If no changes (e.g., low-yield week or non-Friday day-gate):
```bash
git commit --allow-empty -m "routine-06-idea-scan YYYY-MM-DD: <reason>"
```

## NOTIFY

**Silent by default.** Send Telegram ONLY if:
- All sources failed Firecrawl this run (degraded ingestion warning)
- A high-score idea (`score >= 13`) was harvested — one-line preview to draw user's attention before Saturday memo drafting
- An `idea_sources.md` URL appears permanently broken (suggest replacement)

Otherwise silent. Routine #4 Saturday will surface the bank's contents in the memo.

## Mandate footnote

This routine adds a research input. It does NOT:
- Modify strategy.md, guardrails.md, research_log.md schema, or any other routine
- Trigger trades or modify portfolio
- Override the Ring-2 `[Y/N]` channel for strategy edits — every applied idea must still pass through a weekly memo and explicit user approval

If at any future point this routine were proposed to influence trades directly, that would be a Ring-2 strategy.md edit, not a routine #6 expansion.
