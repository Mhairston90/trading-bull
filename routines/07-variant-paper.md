# Routine 07 — Variant Paper-Paper Simulator (22:00 PT daily)

**Cron:** `0 22 * * *` (PT) — daily at 22:00 PT (after routine #3 EOD at 21:00 PT)
**Mode:** local
**Context budget target:** 100K tokens

> **Date-labeling guard (added 2026-06-11):** this wake fires at 22:00–23:59 PT, which is already the **next calendar day in UTC** (05:00–07:00Z). Label the wake, the leaderboard entry, every `Last rebuild` stamp, and the commit message with the **PT calendar date at fire time** — never the UTC date. Sanity check before WRITE: the wake-label date must equal today's PT date, and every `Last rebuild` timestamp must be ≤ now. The 06-10 and 06-11 wakes both mislabeled themselves +1 day by using the UTC date; the future-dated `Last rebuild` stamps would have truncated the next wake's replay window and skipped ~23h of exit checks on open positions.
**Critical constraint:** does NOT modify main BULL's `memory/strategy.md`, `memory/portfolio.md`, `memory/trade_log.md`, `memory/research_log.md`, or any non-variant routine.

## Purpose

For each active LAB variant in `variants/`, replay the window **since that variant's last successful rebuild** (the `Last rebuild` timestamp in its `portfolio.md`; default 24h on the first run after spin-up; capped at 7 days) of Kraken 1H + 4H bars, apply that variant's entry and exit rules, record any hypothetical trades to the variant's own `trade_log.md`, rebuild that variant's `portfolio.md`, and refresh `memory/leaderboard.md` with current standings.

> **Resilience (added 2026-05-29):** this routine previously replayed only a fixed trailing 24h. If a wake was missed (e.g. the 05-16→05-29 scheduler gap), every entry/exit in the gap was permanently dropped — the v0.12-sbd-exit twin logged zero trades despite v0.2-identical entries firing 7 times. Replaying *since the last successful rebuild* makes missed wakes self-healing.

## READ (in order)

1. `CLAUDE.md`
2. `memory/guardrails.md`
3. `memory/universe.md`
4. `variants/README.md`
5. For each subdirectory in `variants/` that is NOT under `variants/archive/`:
   - `variants/<name>/strategy.md`
   - `variants/<name>/portfolio.md`
   - `variants/<name>/trade_log.md` (last 30 days)
6. `memory/leaderboard.md`
7. `memory/portfolio.md` (read-only, for main BULL stats to populate leaderboard row)
8. `skills/variant-spinup.md`

(Does NOT read or modify `memory/strategy.md`, `memory/trade_log.md`, `memory/research_log.md`.)

## VERIFY

- Confirm Kraken MCP reachable (`kraken_ticker` BTC/USD smoke test)
- If Kraken MCP fails: skip routine, write skip note to `memory/leaderboard.md` `### Last simulator wake` field, do NOT touch variant files (per Ring 3 MCP-failure rule, but localized — main routines are unaffected)

## DO

For EACH active variant:

### 1. Determine replay window, then fetch Kraken bars

- **Replay window (resilience against missed wakes):** start = the `Last rebuild` timestamp in this variant's `portfolio.md` (on the first run after spin-up, use the spin-up date); end = now. **Cap at 7 days** — if the gap is longer, replay only the last 7 days and record the older un-recoverable gap in the leaderboard `Notes`. Do NOT fall back to a fixed 24h: that is the bug that dropped the v0.12 twin's trades.
- For all 15 universe pairs, fetch 1H OHLCV covering the replay window (window length + 20 bars warmup) and 4H OHLCV at **maximum available depth — request 720 bars** (Kraken serves up to 720 per call ≈ 120 days of 4H). **The 4H 50-EMA requires ≥ 200 bars of warm-up to converge**; the previous "trailing 7 days" spec yielded only ~42 bars — mathematically insufficient for a 50-EMA — and produced the $400–500 rule-3 uncertainty on BTC at the 2026-06-11 EOD scan. If a pair has < 150 4H bars of history, flag its rule-3 result LOW-CONFIDENCE in the leaderboard notes.
- Compute trailing indicators per pair: 1H 20-EMA, 1H ATR(14), 1H RSI(14), 4H 50-EMA, 30-day mean ATR(14) on 1H (720 bars — fetch additional history as needed for variants that require it, e.g., v0.3 rule 5c)

### 2. Replay exit rules at every 1H close

For each open position in the variant's portfolio:
- For each 1H close in the replay window (chronological):
  - Evaluate variant exit rules (1H close < 1H 20-EMA, stop hit intra-bar, 4R target hit)
  - If any trigger fires, execute hypothetical CLOSE at the close price (or stop price for stop-hit), append to variant's `trade_log.md`
- Stop after first triggering close per position

### 3. Replay entry rules at routine-equivalent wake times

The three wake-equivalent 1H closes correspond to BULL's main routines:
- 06:00 PT → 13:00 UTC (overnight wake)
- 13:00 PT → 20:00 UTC (midday wake — main does NOT enter, but variants are not subject to that constraint UNLESS the variant strategy explicitly says so. v0.3 inherits v0.2 rules + 5c, so by default variants honor main's wake structure: NO entries at midday.)
- 21:00 PT → 04:00 UTC next day (EOD wake)

For each entry-eligible wake in the replay window that has a closed 1H bar:
- Evaluate variant entry rules in order (rules 1–8 plus any variant-specific additions like v0.3's 5c)
- If all rules pass: execute hypothetical OPEN at the wake-bar close price, with 2× ATR stop, sized per the variant's 1.5%-risk rule. Append to `trade_log.md`.
- If multiple pairs eligible at same wake, apply rule 8 (one-per-wake, prefer highest 30d-rank pair)

### 4. Rebuild variant portfolio

Recompute from `trade_log.md`:
- Cash, realized PnL (sum of CLOSE row R-multiples × per-trade $ risk)
- Unrealized PnL (any open positions × current MTM)
- Equity peak, current drawdown
- Active kill-switch state (per variant — independent of main BULL's kill switches)
- Update `variants/<variant>/portfolio.md` with new state and `Last rebuild` timestamp

### 5. Variant kill-switch check

Each variant has its own kill-switch ledger inherited from `memory/guardrails.md`:
- Daily realized + unrealized loss > 5% of variant equity → variant HALTS new entries until next wake (synthetic — does not require RESUME from user since variant is paper-paper)
- 7 consecutive losing trading days → variant FULL PAUSE; flag for retirement consideration in routine #4 Saturday memo
- Max drawdown > 25% from peak → variant FULL PAUSE; flag for retirement
- Variant equity < $7,500 → variant FULL PAUSE; flag for retirement

Halts are written to `variants/<variant>/portfolio.md` `Active kill-switch state` section. They do NOT trigger Telegram ALERTs (variants are evaluation only) but are noted in the leaderboard `Notes` column.

### 6. Update leaderboard

Recompute the `Active rack` table in `memory/leaderboard.md`:
- Days live = today − spin-up date
- Trades = count of CLOSE rows in trade_log
- Win % = wins / closes × 100
- Avg R = mean of CLOSE row R-multiples
- Net % = (current_equity − $10,000) / $10,000 × 100
- Max DD % = peak-to-trough drawdown across the variant's equity curve
- vs BTC-hold = variant net return − BTC-hold return over the same window (computed from Kraken BTC/USD bars)

Re-rank by 30d rolling net return for variants that have ≥ 30 days live; pre-30d variants sort below main.

### 7. Auto-retirement check

If a variant meets any retirement criterion from `variants/README.md`:
- Lost to main on net return for 60 consecutive days
- Tripped kill switch and unrecovered for 7 days
- Cap-of-3 displaced by a higher-priority candidate

Write retirement plan to `memory/leaderboard.md` `### Recently retired` section with reason, **but do NOT execute the file move** — retirement happens only via routine #4 Saturday memo with user awareness.

### 8. Spin-up check (autonomous variant creation)

If `memory/idea_bank.md` has a row with `status: raw`, `score >= 11`, AND active variants count < 3:
- Run `skills/variant-spinup.md` mandate checklist on the candidate
- If all checks pass: create `variants/v0.X-<name>/` per template, update `idea_bank.md` row to `status: under-review`, append leaderboard entry with `status: LAB`, `Spin-up: today`
- If any check fails: append entry to `memory/leaderboard.md` `### Rejected at spin-up` with reason
- Always log the spin-up decision (taken or rejected) to `memory/leaderboard.md` notes

## WRITE

- `variants/<each-active-variant>/portfolio.md` — rebuilt
- `variants/<each-active-variant>/trade_log.md` — appended OPEN/CLOSE rows
- `memory/leaderboard.md` — refreshed
- `memory/idea_bank.md` — only if a new variant was spun up (status field update)
- New `variants/v0.X-<name>/` directory + 4 files — only if a new variant was spun up

(Does NOT write to `memory/strategy.md`, `memory/portfolio.md`, `memory/trade_log.md`, `memory/research_log.md`, or any other main routine's files.)

## COMMIT

```bash
git add variants/ memory/leaderboard.md memory/idea_bank.md
git commit -m "routine-07-variant-paper YYYY-MM-DD: <N> variants simulated, <X> total hypothetical trades, <spin-up: yes|no>"
git push origin main
```

If no changes: `--allow-empty` with summary message.

## NOTIFY

**Silent by default.** Send Telegram ONLY if:
- A variant tripped a kill switch this wake (informational, no user action needed)
- A new variant was spun up autonomously (informational; the spin-up itself doesn't need approval, but user should know)
- A variant became promotion-eligible this wake (≥ 30 days live + meets all promotion criteria) — Saturday's routine #4 will draft the actual gated proposal

Otherwise silent.

## Mandate footnote

This routine adds a parallel evaluation pipeline. It does NOT:
- Place real Kraken orders or affect main BULL's portfolio
- Modify `memory/strategy.md`, `memory/guardrails.md`, or any main-routine file
- Promote a variant to replace main (that requires Ring-2 `[Y/N]` via routine #4 Saturday memo)
- Override mandate floors — every variant is mandate-checked at spin-up; violations are rejected

If at any point this routine were proposed to push variant trades to real broker execution, that would be a fundamental mandate change requiring explicit user `UNLOCK` per `guardrails.md`.
