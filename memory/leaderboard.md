# BULL Strategy Leaderboard

> **Updated each routine #7 wake (daily 22:00 PT).** Tracks main BULL alongside all active LAB variants.
> **Source of truth:** main BULL = `memory/portfolio.md`. Variants = `variants/<name>/portfolio.md`.
> **Read by routine #4 Saturday harness** when drafting weekly memos and evaluating promotion candidates.

## Active rack

| Rank | Strategy | Status | Spin-up | Days live | Trades | Win % | Avg R | Net % | Max DD % | vs BTC-hold | Notes |
|------|----------|--------|---------|-----------|--------|-------|-------|-------|----------|-------------|-------|
| 1    | v0.2 (main)             | MAIN | 2026-04-20 | 9 | 9 | 11.1% | -0.83 | -2.87 | 3.14 | — | live trading; W18 + W19 amendments applied |
| 2    | v0.3-vol-compression    | LAB  | 2026-04-29 | 0 | 0 | —     | —     | —     | —    | — | paper-paper. 30d-eligible 2026-05-29. Source: IDEA-04 |

Ranking is by 30-day rolling net return once variants pass 30-day live threshold. Pre-30d variants sort below main regardless of synthetic stats.

## Cap & rotation

- **Concurrent variants cap:** 3
- **Currently active:** 1 of 3
- Slots 2 and 3 are open. Next qualifying idea_bank row (`score >= 11`) triggers automatic spin-up.

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
