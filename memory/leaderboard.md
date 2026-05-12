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

> **Last refresh:** 2026-05-12 22:00 PT (routine-07 wake — 3 variants simulated, 0 hypothetical trades across the past-24h window). Competition column for Codex rows is **not refreshed this wake** — those are external read-only and were not re-queried; numbers carry forward from 2026-05-10.

| Rank | Strategy | Status | Spin-up | Days live | Trades | Win % | Avg R | Net % | Max DD % | Competition net % (since 2026-04-29) | Notes |
|------|----------|--------|---------|-----------|--------|-------|-------|-------|----------|-------------------------------------|-------|
| 1    | v0.2 (main)             | MAIN | 2026-04-20 | 22 | 16 | 25.0% | -0.23 | +2.58 | 3.54 | +5.62 | live trading; SOL +4.03R take-profit 2026-05-11T19:00Z brought equity to new peak $10,258.06; flat since |
| 2    | v0.3-vol-compression    | LAB  | 2026-04-29 | 13 | 0 | —     | —     | 0.00  | 0.00 | 0.00 | paper-paper. 30d-eligible 2026-05-29. Source: IDEA-04 (vol-compression entry gate, threshold 0.5×). Has 2 sweep children: v0.6 (0.3), v0.7 (0.7) |
| 3    | v0.4-mean-reversion-sleeve | LAB  | 2026-04-29 | 13 | 0 | —  | —     | 0.00  | 0.00 | 0.00 | paper-paper. 30d-eligible 2026-05-29. Source: internal — concept-bucket diversification. Has 1 sweep child: v0.8 (RSI 30) |
| 4    | v0.5-cluster-cap-tight  | LAB  | 2026-04-29 | 13 | 0 | —     | —     | 0.00  | 0.00 | 0.00 | paper-paper. 30d-eligible 2026-05-29. Source: internal — response to lesson 2026-04-27 cascade |
| 5    | v0.6-vol-comp-aggressive | LAB-SWEEP | 2026-05-12 | 0 | 0 | — | — | 0.00 | 0.00 | 0.00 | **Phase 1 autoloop spawn 2026-05-12.** Parameter sweep of v0.3: threshold 0.5 → 0.3 (more aggressive). 30d-eligible 2026-06-11 |
| 6    | v0.7-vol-comp-defensive | LAB-SWEEP | 2026-05-12 | 0 | 0 | — | — | 0.00 | 0.00 | 0.00 | **Phase 1 autoloop spawn 2026-05-12.** Parameter sweep of v0.3: threshold 0.5 → 0.7 (more defensive). 30d-eligible 2026-06-11 |
| 7    | v0.8-mean-rev-relaxed   | LAB-SWEEP | 2026-05-12 | 0 | 0 | — | — | 0.00 | 0.00 | 0.00 | **Phase 1 autoloop spawn 2026-05-12.** Parameter sweep of v0.4: RSI floor 25 → 30 (more relaxed). 30d-eligible 2026-06-11 |
| —    | Codex v0 (competitor)   | EXTERNAL | 2026-04-29 | 13 | 0 closed (4 open) | — | — | +1.04 | 0.00 | **+1.04** | read-only. As of last poll 2026-05-10. Multi-sleeve: trend (BTC/ETH/SOL longs) + relative_strength (ETH long). Equity $10,104.03 |
| —    | Codex Aggro v0 (comp.)  | EXTERNAL | 2026-04-29 | 13 | 1 closed | — | -0.33 | -0.33 | 0.33 | **-0.33** | read-only. As of last poll 2026-05-10. 1 closed trade -$33.21. Equity $9,966.79 |

Ranking is by 30-day rolling net return once variants pass 30-day live threshold. Pre-30d variants sort below main regardless of synthetic stats.

For the **competition** column: net % since 2026-04-29 baseline. This is the metric vs Codex by 2026-07-01 deadline.

## Cap & rotation

- **Concurrent variants cap:** **10** (raised from 3 on 2026-05-12 per user grant for Phase 1 autoloop)
- **Currently active:** 6 of 10 — 4 slots open
- **Categories:** 3 hypothesis variants (v0.3, v0.4, v0.5) + 3 parameter-sweep variants (v0.6, v0.7, v0.8)
- Future qualifying idea_bank rows OR autoloop parameter sweeps will fill remaining 4 slots
- When 11th variant qualifies: retire worst by 30d net return (parameter-sweep variants retired first; hypothesis variants protected)

## Promotion candidates (current)

(none — all 3 variants 13/30 days into eligibility window. Earliest promotion-eligible date 2026-05-29. Synthetic-trade count remains 0 across all variants — entry gates have not fired in the available wake windows since spin-up. Eligibility timer measures wall-clock days since spin-up, not synthetic-bar count, so 2026-05-29 milestone is unaffected.)

### Last simulator wake

- **2026-05-12 22:00 PT** — Kraken MCP OK, 15/15 pairs fetched. Past-24h replay window 2026-05-11 16:00 UTC → 2026-05-12 16:00 UTC (Kraken's latest closed 1H bar; midday 2026-05-12 20:00 UTC bar not yet closed in Kraken's stream at routine fire time). Wakes evaluated: MIDDAY 2026-05-11 20:00 UTC (default-skip for all variants), EOD-prior 2026-05-12 04:00 UTC, OVERNIGHT 2026-05-12 13:00 UTC. **0 hypothetical trades** across all 3 variants. Open positions: 0/0/0 → exit replay no-op. Kill switches: all clear. Auto-retirement check: no triggers. Auto-spin-up check: idea_bank has IDEA-20260512-01 (ETF-flow 30d-MA sign-flip, score 12, raw) eligible by score, **but active rack at 3/3 capacity** — routine #7 step 8 requires count < 3 to auto-spin-up, so no spin-up this wake. Flagged for routine #4 Saturday: with a score-12 raw row queued, the cap-of-3 rotation rule in `variants/README.md` says the worst-performing 30d variant should be displaced — re-evaluate once any variant has ≥30d evidence.

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
