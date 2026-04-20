# Skill: Logging Trades

Used by routines that open or close paper positions. `trade_log.md` is the source of truth — portfolio.md is derived from it.

## Append format (exactly)

Every trade event is one Markdown table row appended under the `## Entries` header in `trade_log.md`.

```
| 2026-04-21T14:00:00Z | OPEN | SOL/USD | long | 17.6 | 142.10 | 138.50 | — | — | — | entry-rule-v0-momentum |
| 2026-04-22T09:00:00Z | CLOSE | SOL/USD | long | 17.6 | 148.90 | — | — | +1.9 | +119.68 | exit-4R-target |
```

Columns (in order):
1. Timestamp UTC ISO 8601
2. Event: `OPEN` or `CLOSE`
3. Pair: e.g. `SOL/USD`
4. Side: `long` or `short` (v0 is long-only)
5. Size: units of the base asset
6. Price: fill price in USD (includes 0.05% slippage model)
7. Stop: only on OPEN rows, `—` on CLOSE
8. Target: if a static target set, `—` otherwise
9. R at exit: R-multiple at close, `—` on OPEN
10. Realized PnL USD: net of 0.26% commission each side, `—` on OPEN
11. Reason tag: which strategy rule triggered this (e.g. `entry-rule-v0-momentum`, `exit-stop-hit`, `exit-ema-cross`, `exit-4R-target`)

## Rules

- **Append only.** Never rewrite past rows. If a mistake is logged, append a correction row with reason `correction-previous-row`.
- **Chronological.** Never insert out of order. If routine ran late and real-world candle close preceded, use candle-close timestamp.
- **No secrets.** No API responses, no internal calculation dumps — that goes to `research_log.md`.
- **Commit every trade day.** Each routine that appends trades commits immediately in its own commit. Message format: `trade: <N> event(s) <YYYY-MM-DD>` — e.g. `trade: 2 events 2026-04-22`.

## Portfolio rebuild (after every log append)

After appending trade events, immediately:
1. Read all rows in `trade_log.md` newer than last archive
2. Replay them to compute: cash balance, open positions, realized PnL, unrealized PnL (using latest Kraken prices for open positions)
3. Update equity peak if current equity > stored peak
4. Compute drawdown from peak
5. Rewrite `portfolio.md` from scratch with new state (this is the one exception to append-only — portfolio.md is fully rewritten each wake)
6. Check guardrails: update kill-switch state section in portfolio.md
7. Commit `portfolio.md` in the same commit as the trade_log row

## Monthly archive (routine #3 last trading day of month)

- Move rows older than 30 days from `trade_log.md` into `memory/archive/YYYY-MM.md`
- Same schema, just split by month
- Commit: `chore: archive YYYY-MM trades`
