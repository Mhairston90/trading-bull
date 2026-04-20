# trading-bull

24/7 autonomous paper-trading agent running on Claude Code Routines.

- **Paper only.** $10,000 starting equity on Kraken spot. No real money, no leverage.
- **Mandate:** see `CLAUDE.md`.
- **Hard risk limits:** see `memory/guardrails.md`.
- **Current strategy:** see `memory/strategy.md`.
- **Trade history:** see `memory/trade_log.md`.

## Routines

| # | When (PT) | Job |
|---|---|---|
| 1 | 06:00 daily | Overnight recap + Telegram digest |
| 2 | 13:00 daily | Midday health check |
| 3 | 21:00 daily | EOD journal + Telegram card |
| 4 | Sat 10:00 | AutoStrategy harness — propose strategy changes |
| 5 | Sun 10:00 | Allocation review |

## Manual run (smoke test)

From Claude Code Desktop: open this folder, click routine `01-overnight`, **Run now**.

## Required environment variables

See `scripts/env-example.md`. All secrets live in the Claude Code local environment, never in this repo.
