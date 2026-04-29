# BULL Strategy Leaderboard

> **Updated each routine #7 wake (daily 22:00 PT).** Tracks main BULL alongside all active LAB variants.
> **Source of truth:** main BULL = `memory/portfolio.md`. Variants = `variants/<name>/portfolio.md`.
> **Read by routine #4 Saturday harness** when drafting weekly memos and evaluating promotion candidates.

## Competition window — vs Codex (deadline 2026-07-01)

User stated 2026-04-29 that BULL is in a head-to-head paper-trading competition with Codex/ChatGPT. Winner gets $200/mo, loser dropped. Codex strategies hadn't traded yet as of 2026-04-29; competition effectively starts when both sides are running.

**Competition baseline (snapshot 2026-04-29 14:00Z):**

| Strategy | Equity at baseline | Trades pre-baseline | Trades since baseline |
|----------|-------------------:|---------------------|----------------------:|
| BULL v0.2 (main) | $9,712.70 | 9 (sunk-cost, pre-competition) | 0 |
| Codex v0         | $10,000.00 | 0 | 0 |
| Codex Aggro v0   | $10,000.00 | 0 | 0 |

**Competition net %** = (current equity − baseline equity) / baseline equity. This is the apples-to-apples metric for the July 1 contest. Pre-baseline trades count toward learning but not toward the contest scoreboard.

**Competition deadline:** 2026-07-01. Days remaining as of baseline: 63.

Routine #7 daily wake updates a `Competition net %` column below for each tracked strategy.

## Active rack

| Rank | Strategy | Status | Spin-up | Days live | Trades | Win % | Avg R | Net % | Max DD % | Competition net % (since 2026-04-29) | Notes |
|------|----------|--------|---------|-----------|--------|-------|-------|-------|----------|-------------------------------------|-------|
| 1    | v0.2 (main)             | MAIN | 2026-04-20 | 9 | 9 | 11.1% | -0.83 | -2.87 | 3.14 | 0.00 | live trading; W18 + W19 amendments applied |
| 2    | v0.3-vol-compression    | LAB  | 2026-04-29 | 0 | 0 | —     | —     | —     | —    | 0.00 | paper-paper. 30d-eligible 2026-05-29. Source: IDEA-04 (vol-compression entry gate, threshold 0.5×) |
| 3    | v0.4-mean-reversion-sleeve | LAB  | 2026-04-29 | 0 | 0 | —  | —     | —     | —    | 0.00 | paper-paper. 30d-eligible 2026-05-29. Source: internal — concept-bucket diversification (mean-reversion 100% in this variant). Tests RSI<25 oversold-bounce in 4H uptrends. |
| 4    | v0.5-cluster-cap-tight  | LAB  | 2026-04-29 | 0 | 0 | —     | —     | —     | —    | 0.00 | paper-paper. 30d-eligible 2026-05-29. Source: internal — direct response to lesson 2026-04-27 cascade. Cluster cap tightened from 2 to 1. |

Ranking is by 30-day rolling net return once variants pass 30-day live threshold. Pre-30d variants sort below main regardless of synthetic stats.

For the **competition** column: net % since 2026-04-29 baseline. This is the metric vs Codex by 2026-07-01 deadline.

## Cap & rotation

- **Concurrent variants cap:** 3
- **Currently active:** 3 of 3 — **rack at capacity**
- Future idea_bank rows scoring ≥ 11 will trigger auto-displacement of the worst-performing variant by 30-day net return at routine #7 wake (per `variants/README.md` cap rule).

## Promotion candidates (current)

(none — v0.3 is too young. Earliest promotion-eligible date 2026-05-29.)

## Recently retired

(none yet.)

## Recently promoted

(none yet.)

## Rejected at spin-up (mandate-violation log)

(none yet.)

## How to read this file

- **MAIN** is the live strategy in `memory/strategy.md`. Its `portfolio.md` reflects real paper trades on Kraken via routines #1/#2/#3.
- **LAB** variants are paper-paper — synthetic $10K accounts that simulate trades against the same Kraken bars main BULL sees, but without affecting main's portfolio.
- A variant with higher 30d net return than main is a *candidate* for promotion — routine #4 Saturday drafts a Ring-2 `[Y/N]` proposal when criteria pass.
- A variant cannot replace main without explicit user `[Y]`. The mandate's strategy-edit gate applies to promotion, not to variant spin-up.

## Cross-references

- Variant rack docs: `variants/README.md`
- Spin-up procedure: `skills/variant-spinup.md`
- Daily simulation routine: `routines/07-variant-paper.md`
- Idea source for v0.3: `memory/idea_bank.md` IDEA-20260429-04
