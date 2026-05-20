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

> **Last refresh:** 2026-05-16 22:00 PT (routine-07 wake — 8 variants simulated, 0 hypothetical trades across the past-24h window). Codex competition rows are external read-only and were not re-queried by routine #7; they carry forward from routine #4's 2026-05-16 poll.
> **2026-05-19 (off-cycle, interactive):** main strategy upgraded **v0.2 → v0.3** via Ring-2 2026-W21-F (user `[Y B]` + variant — synchronized-breakdown classifier 5a-SBD + defensive 9-EMA exit 1-SBD). Instrumented twin **v0.12-sbd-exit** spun up (rack now 10/10, full). Synthetic stats for v0.12 begin accruing next routine #7 wake. NOTE: MAIN row strategy version is now "v0.3"; the unrelated LAB variant *named* "v0.3-vol-compression" is a separate namespace — do not conflate.

| Rank | Strategy | Status | Spin-up | Days live | Trades | Win % | Avg R | Net % | Max DD % | Competition net % (since 2026-04-29) | Notes |
|------|----------|--------|---------|-----------|--------|-------|-------|-------|----------|-------------------------------------|-------|
| 1    | v0.4 (main)             | MAIN | 2026-04-20 | 30 | 17 | 23.5% | -0.27 | +2.36 | 3.54 | +5.39 | live trading; **upgraded v0.3→v0.4 2026-05-20 (Ring-2 W22-G + W22-H-partial: two-bar EMA exit confirmation + breakeven stop ratchet at +2R unrealized; 4R take-profit retained; user delegated choice via interactive chat, agent selected Option C per `feedback-perf-analysis-framing`)**. Prior upgrade v0.2→v0.3 2026-05-19 (W21-F: 5a-SBD + Exit 1-SBD). SOL +4.03R/+$585.35 take-profit 2026-05-11; XRP −0.14R/−$21.92 2026-05-15 (the XRP archetype that motivated W22). Equity $10,236.14, flat. Peak $10,258.06 (05-11), DD-from-peak 0.21%. W22 rules apply to new entry-scans/exits only; no retroactive effect on the 17 closed trades |
| 2    | v0.3-vol-compression    | LAB  | 2026-04-29 | 17 | 0 | —     | —     | 0.00  | 0.00 | 0.00 | paper-paper. 30d-eligible 2026-05-29. Source: IDEA-04 (vol-compression entry gate, threshold 0.5×). Has 2 sweep children: v0.6 (0.3), v0.7 (0.7) |
| 3    | v0.4-mean-reversion-sleeve | LAB  | 2026-04-29 | 17 | 0 | —  | —     | 0.00  | 0.00 | 0.00 | paper-paper. 30d-eligible 2026-05-29. Source: internal — concept-bucket diversification. Sweep children: v0.8 (RSI 30), v0.9 (RSI 20) — brackets parent |
| 4    | v0.5-cluster-cap-tight  | LAB  | 2026-04-29 | 17 | 0 | —     | —     | 0.00  | 0.00 | 0.00 | paper-paper. 30d-eligible 2026-05-29. Source: internal — lesson 2026-04-27 cascade. **No sweep child spawned 2026-05-16**: only further perturbation is cluster_cap=0, which v0.5's own README documents as "TOO tight to be useful" — autoloop respects parent's documented rationale, no churn |
| —    | v0.13-trend-confirm     | LAB  | 2026-05-20 | 0 | 0 | — | — | 0.00 | 0.00 | 0.00 | **Hypothesis variant, interactive 2026-05-20.** Source: trade_log whipsaw analysis (9/17 main closes are −1R inside 21h of entry, ≈ −$386 of −$700 in losses; the dominant un-addressed bucket). Entry rule 1 → 2 consecutive 1H closes > 20-EMA; new rule 3a: 4H RSI(14) ≥ 50. Strictly entry-restricting vs v0.3. Spun in v0.6's retired slot. 30d-eligible 2026-06-19 |
| 6    | v0.7-vol-comp-defensive | LAB-SWEEP | 2026-05-12 | 4 | 0 | — | — | 0.00 | 0.00 | 0.00 | **Phase 1 autoloop spawn 2026-05-12.** Parameter sweep of v0.3: threshold 0.5 → 0.7 (more defensive). 30d-eligible 2026-06-11 |
| 7    | v0.8-mean-rev-relaxed   | LAB-SWEEP | 2026-05-12 | 4 | 0 | — | — | 0.00 | 0.00 | 0.00 | **Phase 1 autoloop spawn 2026-05-12.** Parameter sweep of v0.4: RSI floor 25 → 30 (more relaxed). 30d-eligible 2026-06-11 |
| 8    | v0.9-mean-rev-tight     | LAB-SWEEP | 2026-05-16 | 0 | 0 | — | — | 0.00 | 0.00 | 0.00 | **Phase 1 autoloop spawn 2026-05-16 (routine #4).** Parameter sweep of v0.4: RSI floor 25 → 20 (stricter). Brackets parent with v0.8 (20/25/30 expectancy curve). 30d-eligible 2026-06-15 |
| 9    | v0.10-exit-confirm      | LAB-SUBSUMED  | 2026-05-16 | 4 | 0 | — | — | 0.00 | 0.00 | 0.00 | **SUBSUMED by main v0.4** (W22-G applied 2026-05-20). Original hypothesis (2 consecutive 1H closes < 20-EMA exit) is now main's Exit rule 1. Variant now identical to main on the exit-confirmation dimension; will track main on net return going forward. Flagged for retirement audit at routine #4 2026-05-23 — recommend archive, free rack slot. 30d-eligibility moot |
| 10   | v0.11-breakeven-2R      | LAB-SUBSUMED  | 2026-05-16 | 4 | 0 | — | — | 0.00 | 0.00 | 0.00 | **SUBSUMED by main v0.4** (W22-H-partial applied 2026-05-20). Original hypothesis (breakeven stop ratchet at +2R unrealized) is now main's Stop management rule. Variant identical to main on the breakeven dimension. Flagged for retirement audit at routine #4 2026-05-23 — recommend archive, free rack slot |
| 11   | v0.12-sbd-exit          | LAB  | 2026-05-19 | 0 | 0 | — | — | 0.00 | 0.00 | 0.00 | **Hypothesis / instrumented twin, interactive 2026-05-19 (Ring-2 W21-F).** Source: contest fragility audit + lesson 2026-05-19 (synchronized-breakdown defensive asymmetry). v0.2 + 5a-SBD + Exit 1-SBD == live v0.3 ruleset; isolates SBD change vs v0.2 baseline + logs avoided-give-back telemetry. Strictly risk-reducing vs v0.2. Tuneable: sbd_breadth_max(1), sbd_median_max(−1.0), sbd_exit_ema(9). 30d-eligible 2026-06-18 |
| —    | Codex v0 (competitor)   | EXTERNAL | 2026-04-29 | 17 | 1 closed (4 open) | — | +1.91 | -0.20 | 0.20 | **-0.20** | read-only. Poll 2026-05-16 (routine #4). 1 closed SOL +$112.92 (target-hit 05-12); 4 open (BTC/ETH×2/SOL) unrealized −$132.82. Equity $9,980.10 — dropped from +1.04 (05-10) as open ETH/SOL bled |
| —    | Codex Aggro v0 (comp.)  | EXTERNAL | 2026-04-29 | 17 | 1 closed (6 open) | — | -0.33 | -0.43 | 0.43 | **-0.43** | read-only. Poll 2026-05-16. Now SHORT 6 pairs, gross exposure 200.29% (margin — mandate-incompatible, do NOT copy). Cash −$9,967. Equity $9,957.13 |

Ranking is by 30-day rolling net return once variants pass 30-day live threshold. Pre-30d variants sort below main regardless of synthetic stats.

For the **competition** column: net % since 2026-04-29 baseline. This is the metric vs Codex by 2026-07-01 deadline.

## Cap & rotation

- **Concurrent variants cap:** **10** (raised from 3 on 2026-05-12 per user grant for Phase 1 autoloop)
- **Currently active:** 10 of 10 — **rack full** (v0.13-trend-confirm added 2026-05-20 interactive; displaced v0.6-vol-comp-aggressive — see Recently retired)
- **Categories:** 7 hypothesis variants (v0.3-vol-compression, v0.4, v0.5, v0.10, v0.11, v0.12, v0.13) + 3 parameter-sweep variants (v0.7, v0.8, v0.9)
- Rack is at cap. When an 11th variant qualifies: retire worst by 30d net return (parameter-sweep variants retired first; hypothesis variants protected)

## Promotion candidates (current)

(none — hypothesis variants v0.3/v0.4/v0.5 at 17/30 days; earliest promotion-eligible 2026-05-29. Synthetic-trade count remains 0 across all 9 active variants — entry gates still not firing: broadly-red regime persists (0/15 universe pairs positive 2026-05-16). Momentum variants (v0.3/v0.5/v0.6/v0.7/v0.10) blocked by regime gate 5a; mean-reversion variants (v0.4/v0.8/v0.9) blocked by M3 reversal-candle filter — the 2026-05-15 13:00Z synchronized crash bar and the 05-16 04:00Z continuation bar were red universe-wide. Eligibility timer is wall-clock days since spin-up, unaffected by 0 synthetic trades. Routine #4 2026-05-16 harness: no promotion candidate, no Ring-2 proposal — see weekly_memos/2026-W20.md.)

### Last simulator wake

- **2026-05-12 22:00 PT** — Kraken MCP OK, 15/15 pairs fetched. Past-24h replay window 2026-05-11 16:00 UTC → 2026-05-12 16:00 UTC. Wakes evaluated: MIDDAY 2026-05-11 20:00 UTC (default-skip), EOD-prior 2026-05-12 04:00 UTC, OVERNIGHT 2026-05-12 13:00 UTC. **0 hypothetical trades** across all 3 variants. Open positions 0/0/0 → exit replay no-op. Kill switches all clear. Auto-spin-up: IDEA-20260512-01 (score 12, raw) eligible by score but rack at capacity — no spin-up.
- **2026-05-16 22:00 PT** — Kraken MCP OK (BTC/USD smoke test passed), 15/15 pairs fetched. Past-24h replay window 2026-05-15 10:00 UTC → 2026-05-16 10:00 UTC (Kraken's latest closed 1H bar 05-16 10:00Z; routine #7 last ran 05-12 — the 05-13/14/15 wakes were missed, but routine spec scopes replay to trailing 24h, not backfill). Wakes evaluated: OVERNIGHT 2026-05-15 13:00 UTC, MIDDAY 2026-05-15 20:00 UTC (default-skip all variants), EOD 2026-05-16 04:00 UTC. **8 variants simulated** (v0.3–v0.10; v0.10-exit-confirm + v0.9 were added by routine #4 earlier today and picked up automatically). **0 hypothetical trades.** All 8 variants have 0 open positions → exit replay no-op for all (incl. v0.10's modified 2-bar EMA-cross exit — no positions to evaluate). Gate analysis: broadly-red tape, all 15 universe pairs negative on 24h change, 0/15 positive at EOD. Momentum variants v0.3/v0.5/v0.6/v0.7/v0.10 → regime gate 5a (≥4/15 positive) rejected all entries at both eligible wakes. Mean-reversion variants v0.4/v0.8/v0.9 → rule M3 (reversal candle, 1H close > open) failed for all 15 pairs at both eligible wakes (05-15 13:00Z synchronized crash bar; 05-16 04:00Z red universe-wide), blocking before the RSI-floor (M2) differences could matter. Per-variant kill switches: all clear at $10,000 synthetic equity. Auto-retirement check: no triggers (no variant losing to main 60d, none tripped kill switch, rack 8/10 — no forced displacement). Auto-spin-up check (step 8): idea_bank has IDEA-20260512-01 (score 12, raw) and IDEA-20260429-03 (score 9, raw); IDEA-20260512-01 qualifies by score but **routine #7 step 8 gate requires active variants count < 3** and current count is 8 → no auto-spin-up. (Note: leaderboard cap is 10, but step 8's literal count<3 condition governs routine #7 autonomous spin-up; rack-fill is being driven by routine #4's Phase-1 autoloop instead.) Decision logged: no spin-up this wake. **Concurrency note:** routine #4 was spawning rack variants in parallel with this routine #7 run. v0.9 + v0.10 existed by the time the variant-read pass completed and were simulated (0 trades). v0.11-breakeven-2R was created by routine #4 *after* this routine's read pass and was NOT simulated this wake — it was spun up today with 0 positions and an empty trade log, so deferring it to the next routine #7 wake is lossless (it would be regime-gated to 0 trades exactly like the other v0.2-derived momentum variants in this broadly-red tape). Its portfolio.md remains at routine #4's $10,000 spin-up state. Next routine #7 wake (2026-05-17 22:00 PT) will pick it up automatically.

## Recently retired

- **v0.6-vol-comp-aggressive** — retired 2026-05-20 (interactive session, displaced by v0.13-trend-confirm spin-up). 8 days live, 0 synthetic trades (regime-blocked the entire window; broadly-red tape persisted from spin-up through retirement). Archived at `variants/archive/v0.6-vol-comp-aggressive-2026-05-20/`. **Reason:** rack at 10/10 cap; v0.13 (entry-quality hypothesis) had higher informational value than continuing the vol-comp sweep's aggressive endpoint (0.3). Defensive endpoint v0.7 retained — keeps the v0.3-vol-compression sweep's more-informative direction. Parameter-sweep variants retired before hypothesis variants per `variants/README.md` retirement priority. The IDEA-04 (vol-compression) line continues to be tracked via the hypothesis parent v0.3-vol-compression and the defensive sweep v0.7.

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
