# skill: idea-scan

> Invoked by routine #6. Harvests recent content from sources in `memory/idea_sources.md`, extracts testable claims, scores, and appends to `memory/idea_bank.md`.

## Inputs

- `memory/idea_sources.md` — source list with per-source `signal-quality` and `bull-fit` scores
- `memory/idea_bank.md` — for de-duplication
- `FIRECRAWL_API_KEY` from environment

## Procedure

For each active source in `idea_sources.md`:

1. **Fetch** — Firecrawl the source URL with `formats=["markdown"]` and `onlyMainContent=true`. Cap at 12K tokens per fetch.
2. **Filter to recent** — keep only content dated in the past 7 days (or since last harvest if longer). If the source has multiple posts in window, take the 2 most recent.
3. **Extract testable claims** — for each post, identify any statement matching the pattern:
   > "When [observable condition] is true, [asset/scope] tends to [direction] over [timeframe]"
   Examples:
   - "When 30d realized vol < 30%, BTC tends to break out within 14 days" — testable
   - "BTC is in a structural bull market" — NOT testable (too vague), DROP
   - "Reserve risk < 0.002 has historically marked BTC bottoms" — testable
   - "Funding rates flipping negative on perps means a squeeze is coming" — DROP (perps, outside mandate)
4. **Score per claim:**
   - `signal-quality`: inherited from `idea_sources.md`
   - `bull-fit` (1-5): does it apply to spot crypto on BULL's universe at 1H/4H? 5 = directly, 1 = methodology only, requires translation
   - `testability` (1-5): can it be backtested in TradingView with available indicators / Pine? 5 = single indicator threshold, 1 = needs custom data we don't have
   - `score` = sum (max 15)
5. **Drop low-score** — claims with `score < 8` are not appended (they're below the noise floor).
6. **De-dup** — if the bank already has a `raw / under-review / proposal-drafted / applied` row with the same `claim` (semantic match, not string match), skip.
7. **Append** — add a row per surviving claim to `memory/idea_bank.md` with `status: raw` and `id: IDEA-YYYYMMDD-NN` (NN = sequence within today).

## Output budget

- Aim for **5-15 new ideas per weekly run** across all 10 sources
- If a single source produces > 5 surviving ideas in a wake, take the top 3 by score and skip the rest (likely overweighted)
- If total surviving ideas across all sources < 3, log `low yield this week — consider reviewing source list` to research_log

## Failure modes

- **Firecrawl down on a source** → log `Firecrawl unavailable for <source>` to research_log, continue with other sources. Do not skip the routine.
- **Firecrawl down on all sources** → log to research_log, exit routine cleanly. Per Ring 3, this counts as MCP failure but routine #6 is non-critical so it does NOT halt overall trading.
- **Source URL stale (404)** → mark in research_log, flag for routine #4 to update `idea_sources.md`.
- **Source pivoted (no relevant content in 30d)** → flag in research_log for routine #4 quarterly review.

## Mandate compliance

- Idea-scan does NOT modify `strategy.md`, `guardrails.md`, `research_log.md` schema, or any routine. It writes only to `idea_bank.md` and the standard append row to `research_log.md` (legacy schema, single-line summary).
- Idea-scan does NOT issue trade signals. It does NOT read open positions. It does NOT touch portfolio.
- Promotion of any idea into a strategy rule goes through the existing Ring-2 weekly memo `[Y/N]` flow. No shortcut.
