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

**Competition deadline:** 2026-07-01. Days remaining as of 2026-05-29: **33**.

Routine #7 daily wake updates a `Competition net %` column below for each tracked strategy.

## Active rack

> **Last refresh:** 2026-05-29 22:00 PT (routine-07 wake — 10 variants simulated, 0 hypothetical trades across the past-24h window). **SBD active this wake** (1/15 positive, median −1.07%). v0.3/v0.4/v0.5 reached 30-day time threshold; 0 trades → NOT promotion-eligible (need ≥10). Codex competition rows carry forward from routine #4 2026-05-16 poll (not re-queried by routine #7).
> **2026-05-19 (off-cycle, interactive):** main strategy upgraded **v0.2 → v0.3** via Ring-2 2026-W21-F (user `[Y B]` + variant — synchronized-breakdown classifier 5a-SBD + defensive 9-EMA exit 1-SBD). Instrumented twin **v0.12-sbd-exit** spun up (rack now 10/10, full). Synthetic stats for v0.12 begin accruing next routine #7 wake. NOTE: MAIN row strategy version is now "v0.3"; the unrelated LAB variant *named* "v0.3-vol-compression" is a separate namespace — do not conflate.

| Rank | Strategy | Status | Spin-up | Days live | Trades | Win % | Avg R | Net % | Max DD % | Competition net % (since 2026-04-29) | Notes |
|------|----------|--------|---------|-----------|--------|-------|-------|-------|----------|-------------------------------------|-------|
| 1    | v0.4 (main)             | MAIN | 2026-04-20 | 39 | 24 | 20.8% | -0.22 | +3.56 | 3.48 | +6.63 | live trading; strategy v0.4 (W22-G+H: 2-bar EMA exit confirm + breakeven ratchet at +2R). 24 closed trades incl. missed-scheduler replay 05-21→05-26 (HYPE +4.04R, TAO/HYPE/SOL/AVAX/BTC/TAO losses). Equity $10,356.03, flat. Peak $10,728.95 (05-21 HYPE 4R). DD-from-peak 3.48%. Flat since 05-26; regime-gated (rule 5a). SBD ACTIVE 2026-05-29 wake (1/15 positive, median −1.07%). Competition net% +6.63% vs Codex baseline. |
| 2    | v0.3-vol-compression    | LAB  | 2026-04-29 | 30 | 0 | —     | —     | 0.00  | 0.00 | 0.00 | paper-paper. **30d threshold reached 2026-05-29; 0 trades → NOT promotion-eligible (need ≥10 in 30d window)**. Momentum-blocked entire 30d by regime gate (5a). Net%=0 vs main +6.63% → also behind on net return. Source: IDEA-04 (vol-compression gate, threshold 0.5×). Sweep child v0.7 (threshold 0.7) active. |
| 3    | v0.4-mean-reversion-sleeve | LAB  | 2026-04-29 | 30 | 0 | —  | —     | 0.00  | 0.00 | 0.00 | paper-paper. **30d threshold reached 2026-05-29; 0 trades → NOT promotion-eligible**. M3 (reversal candle) + M2 (RSI<25) jointly blocked all EOD entries; M3 failed overnight. Net%=0 vs main +6.63% → behind on net return. Sweep children: v0.8 (RSI 30), v0.9 (RSI 20). |
| 4    | v0.5-cluster-cap-tight  | LAB  | 2026-04-29 | 30 | 0 | —     | —     | 0.00  | 0.00 | 0.00 | paper-paper. **30d threshold reached 2026-05-29; 0 trades → NOT promotion-eligible**. Momentum-blocked entire 30d by regime gate (5a). Net%=0 vs main +6.63% → behind on net return. Source: lesson 2026-04-27 cascade. No sweep child (cluster_cap=0 documented as too tight). |
| —    | v0.13-trend-confirm     | LAB  | 2026-05-20 | 9 | 0 | — | — | 0.00 | 0.00 | 0.00 | **Hypothesis variant, interactive 2026-05-20.** Source: whipsaw analysis (dominant −1R bucket). 2 consecutive 1H closes > 20-EMA + 4H RSI≥50 entry filter. Strictly entry-restricting vs v0.3. Regime-blocked since spin-up (5a). 30d-eligible 2026-06-19. |
| 6    | v0.7-vol-comp-defensive | LAB-SWEEP | 2026-05-12 | 17 | 0 | — | — | 0.00 | 0.00 | 0.00 | **Phase 1 autoloop spawn 2026-05-12.** Parameter sweep of v0.3: threshold 0.5 → 0.7 (more defensive). Regime-blocked since spin-up (5a). 30d-eligible 2026-06-11. |
| 7    | v0.8-mean-rev-relaxed   | LAB-SWEEP | 2026-05-12 | 17 | 0 | — | — | 0.00 | 0.00 | 0.00 | **Phase 1 autoloop spawn 2026-05-12.** Parameter sweep of v0.4: RSI floor 25 → 30 (more relaxed). M3+M2 blocked since spin-up. 30d-eligible 2026-06-11. |
| 8    | v0.9-mean-rev-tight     | LAB-SWEEP | 2026-05-16 | 13 | 0 | — | — | 0.00 | 0.00 | 0.00 | **Phase 1 autoloop spawn 2026-05-16 (routine #4).** Parameter sweep of v0.4: RSI floor 25 → 20 (stricter). Brackets parent with v0.8 (20/25/30 expectancy curve). M3+M2 blocked since spin-up. 30d-eligible 2026-06-15. |
| 9    | v0.10-exit-confirm      | LAB-SUBSUMED  | 2026-05-16 | 13 | 0 | — | — | 0.00 | 0.00 | 0.00 | **SUBSUMED by main v0.4** (W22-G applied 2026-05-20). Original hypothesis now main's Exit rule 1. Regime-blocked since spin-up. Flagged for retirement at routine #4 — recommend archive to free rack slot. 30d-eligibility moot. |
| 10   | v0.11-breakeven-2R      | LAB-SUBSUMED  | 2026-05-16 | 13 | 0 | — | — | 0.00 | 0.00 | 0.00 | **SUBSUMED by main v0.4** (W22-H-partial applied 2026-05-20). Original hypothesis now main's Stop management rule. Regime-blocked since spin-up. Flagged for retirement at routine #4 — recommend archive. |
| 11   | v0.12-sbd-exit          | LAB  | 2026-05-19 | 10 | 0 | — | — | 0.00 | 0.00 | 0.00 | **Hypothesis / instrumented twin.** SBD ACTIVE first wake (2026-05-29): 1/15 positive, median −1.07%; no open positions to evaluate. Telemetry row 1 appended in portfolio.md. 30d-eligible 2026-06-18. |
| —    | Codex v0 (competitor)   | EXTERNAL | 2026-04-29 | 17 | 1 closed (4 open) | — | +1.91 | -0.20 | 0.20 | **-0.20** | read-only. Poll 2026-05-16 (routine #4). 1 closed SOL +$112.92 (target-hit 05-12); 4 open (BTC/ETH×2/SOL) unrealized −$132.82. Equity $9,980.10 — dropped from +1.04 (05-10) as open ETH/SOL bled |
| —    | Codex Aggro v0 (comp.)  | EXTERNAL | 2026-04-29 | 17 | 1 closed (6 open) | — | -0.33 | -0.43 | 0.43 | **-0.43** | read-only. Poll 2026-05-16. Now SHORT 6 pairs, gross exposure 200.29% (margin — mandate-incompatible, do NOT copy). Cash −$9,967. Equity $9,957.13 |

Ranking is by 30-day rolling net return once variants pass 30-day live threshold. Pre-30d variants sort below main regardless of synthetic stats.

For the **competition** column: net % since 2026-04-29 baseline. This is the metric vs Codex by 2026-07-01 deadline.

## Cap & rotation

- **Concurrent variants cap:** **10** (raised from 3 on 2026-05-12 per user grant for Phase 1 autoloop)
- **Currently active:** 10 of 10 — **rack full** (v0.13-trend-confirm added 2026-05-20 interactive; displaced v0.6-vol-comp-aggressive — see Recently retired)
- **Categories:** 7 hypothesis variants (v0.3-vol-compression, v0.4, v0.5, v0.10, v0.11, v0.12, v0.13) + 3 parameter-sweep variants (v0.7, v0.8, v0.9)
- Rack is at cap. When an 11th variant qualifies: retire worst by 30d net return (parameter-sweep variants retired first; hypothesis variants protected)
- **Auto-spin-up step 8 gate:** requires active count < 3 (per routine #7 spec) — not triggered this wake (count 10). idea_bank IDEA-20260512-01 (score 12, under-review) remains queued but blocked by both count gate and rack cap.

## Promotion candidates (current)

(none — v0.3/v0.4/v0.5 crossed the 30-day time threshold today (2026-05-29) but have **0 trades in the rolling 30d window** (need ≥10). Not promotion-eligible. Additionally, net return 0.00% vs main BULL +6.63% → fails the "beats main on net return" criterion as well. Regime-blocked entire 30-day window: momentum variants blocked by 5a (≥4/15 positive never reached during this period); mean-reversion variants blocked by M3/M2 combination. Trade-count eligibility clock continues — if market regime normalizes and trades begin accumulating, promotion could be re-assessed once ≥10 trades accrue. Routine #4 next Saturday to assess retirement of v0.10/v0.11 (SUBSUMED).)

### Last simulator wake

- **2026-05-12 22:00 PT** — Kraken MCP OK, 15/15 pairs fetched. **0 hypothetical trades** across all 3 variants. Kill switches all clear. Auto-spin-up: IDEA-20260512-01 (score 12) eligible by score but rack at capacity — no spin-up.
- **2026-05-16 22:00 PT** — Kraken MCP OK, 15/15 pairs fetched. **8 variants simulated, 0 hypothetical trades.** Broadly-red tape, 0/15 positive at EOD. Momentum variants regime-gated (5a); mean-reversion variants blocked by M3 synchronized crash bar. Per-variant kill switches: all clear. No auto-spin-up (count<3 gate; count was 8). See prior full entry in archive for detail.
- **2026-05-29 22:00 PT** — Kraken MCP OK (BTC/USD $73,183 smoke test). **10 variants simulated, 0 hypothetical trades.** Past-24h replay window 2026-05-29 05:00 UTC → 2026-05-30 05:00 UTC. **Regime: 1/15 pairs positive 24h (HYPE +0.67%); median 24h change −1.07%. SBD ACTIVE** (≤1/15 positive AND median ≤−1.0%). Wakes evaluated: OVERNIGHT 2026-05-29 13:00 UTC, MIDDAY (default-skip), EOD 2026-05-30 04:00 UTC. Gate analysis — Momentum variants (v0.3, v0.5, v0.7, v0.10, v0.11, v0.12, v0.13): rule 5a (≥4/15 positive) rejected all entries at both eligible wakes (1/15 positive). Mean-reversion variants (v0.4, v0.8, v0.9): at OVERNIGHT, M3 (reversal candle) failed universe-wide — 1H bar at 13:00 UTC was red for all sampled pairs; at EOD, M3 passed for BTC/SOL/HYPE/TAO/ADA but M2 (RSI < threshold) failed for all — computed RSI BTC≈55, SOL≈59, HYPE≈75, TAO≈50, ADA≈58 (far from oversold). All 10 variants: 0 open positions → exit replay no-op. Per-variant kill switches: all clear at $10,000 synthetic equity. **30-day milestone:** v0.3/v0.4/v0.5 reached 30-day time threshold; 0 trades → NOT promotion-eligible (need ≥10 in rolling 30d window; also fail net-return criterion vs main +6.63%). Auto-retirement check: no triggers (no 60d underperformance vs main, no kill-switch trips, rack full at 10/10 — no forced displacement by score). Auto-spin-up step 8: count=10 ≫ 3 threshold — no spin-up. v0.12 SBD telemetry: first active-SBD wake logged (no positions to evaluate; row appended in v0.12/portfolio.md). Note: routine #7 had 13-day gap since last run (05-16→05-29); routine spec scopes replay to trailing 24h only — no backfill for missed wakes.

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
