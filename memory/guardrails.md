# Guardrails — IMMUTABLE

These are hard floors. BULL may NEVER edit this file. User-only with explicit `UNLOCK <item>` command.

## Position & risk caps

- Max concurrent positions: **8**
- Max portfolio risk at any moment (sum of open-trade stop-distance × size / equity): **4%**
- Max risk per individual trade: **1.5%**
- Max universe: **15 Kraken USD pairs** (source `memory/universe.md`)
- Allowed instruments: **Kraken spot only**. No leverage, no margin, no perps, no options.

## Ring 3 — Kill switches (automatic halt + Telegram ALERT, user must `RESUME`)

| Trigger | Action |
|---|---|
| Daily realized + unrealized loss > 5% of equity | HALT new entries, hold open positions, ALERT |
| 7 consecutive losing trading days | FULL PAUSE, flat all paper positions at market, require `RESUME` |
| Max drawdown > 25% from equity peak | FULL PAUSE, require `RESUME` |
| Equity < $7,500 | FULL PAUSE, require `RESUME` + mandatory strategy review |
| Kraken MCP / TradingView MCP / Telegram MCP failure | SKIP this routine run, append error to `research_log.md`, retry next routine |

## Ring 2 — Gated changes (Telegram `[Y/N]`, 24h timeout auto-rejects)

- Edit `memory/strategy.md` (any entry/exit rule change)
- Promote an AutoStrategy variant to replace current strategy
- Allocation shift >20% between concept buckets (momentum / mean-reversion / news-reactive as declared in current `strategy.md`)
- Add or remove a universe pair outside the monthly auto-refresh
- Loosen any item in this guardrails file — requires explicit `UNLOCK <item>` message from user

## Review trigger (not a kill switch)

- No beat on BTC-hold total return over rolling 90 days → flagged in weekly memo, mandatory strategy review at next routine #4. BULL keeps trading meanwhile.

## Logging obligations

Every trade entry and exit in `trade_log.md` must include:
- Timestamp (ISO 8601, UTC)
- Pair, side, size, entry/exit price
- Stop, target, R-multiple at exit
- Reason tag citing which rule in `strategy.md` triggered (e.g. `entry-rule-1-momentum`)

Every strategy-change proposal in a weekly memo must include:
- Current rule being changed
- Proposed replacement
- Evidence (backtest stats, trade-log support)
- Risk assessment
- Expected impact
