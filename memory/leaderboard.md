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

**Competition deadline:** 2026-07-01. Days remaining as of 2026-06-06: **25**.

Routine #7 daily wake updates a `Competition net %` column below for each tracked strategy.

## Active rack

> **Last refresh:** 2026-05-31 05:00 UTC / routine-07 wake 2026-05-30 22:00 PT — **10 variants simulated, 4 hypothetical trades** (HYPE/USD long opened in v0.5, v0.10, v0.11, v0.12 at OVERNIGHT wake 13:00Z 2026-05-30). Regime recovered from SBD: ~12/15 positive at OVERNIGHT, 14/15 positive at EOD; SBD cleared. Vol-comp variants (v0.3/v0.7/v0.13) blocked by ATR-compression gate. Mean-rev variants (v0.4/v0.8/v0.9) blocked by RSI far from oversold. v0.5/v0.10/v0.11/v0.12 first trades since inception. Codex competition rows carry forward from routine #4 2026-05-16 poll.
> **2026-05-19 (off-cycle, interactive):** main strategy upgraded **v0.2 → v0.3** via Ring-2 2026-W21-F (user `[Y B]` + variant — synchronized-breakdown classifier 5a-SBD + defensive 9-EMA exit 1-SBD). Instrumented twin **v0.12-sbd-exit** spun up (rack now 10/10, full). Synthetic stats for v0.12 begin accruing next routine #7 wake. NOTE: MAIN row strategy version is now "v0.3"; the unrelated LAB variant *named* "v0.3-vol-compression" is a separate namespace — do not conflate.

| Rank | Strategy | Status | Spin-up | Days live | Trades | Win % | Avg R | Net % | Max DD % | Competition net % (since 2026-04-29) | Notes |
|------|----------|--------|---------|-----------|--------|-------|-------|-------|----------|-------------------------------------|-------|
| 1    | v0.4 (main)             | MAIN | 2026-04-20 | 41 | 24 | 20.8% | -0.22 | +2.55 | 4.42 | +5.58 | live trading; strategy v0.4. Equity $10,254.63, flat (0 open). Peak $10,728.95 (05-21). DD-from-peak 4.42%. XRP exit-ema20-confirm −0.65R on 2026-05-30 (4 consec losing trading days). SBD CLEARED (14/15 positive at EOD 05-31). Losing streak 4 (cap 7). Competition net% +5.58% vs Codex baseline. |
| 2    | v0.5-cluster-cap-tight  | LAB  | 2026-04-29 | 32 | 0 | —     | —     | +1.23 | 0.00 | +1.23 | paper-paper. **First trade this wake: HYPE/USD long 77 @ 68.06 (OVERNIGHT 13:00Z 2026-05-30)**. Stop 66.13, target 75.80. MTM at EOD 69.83 → unrealized +$136.29, equity $10,122.66. **30d threshold reached; 0 closed trades → NOT promotion-eligible yet.** Vol-comp variants blocked; v0.5 (no vol-comp gate) entered on regime recovery. vs BTC-hold (Apr 29): +3.43% |
| 3    | v0.3-vol-compression    | LAB  | 2026-04-29 | 32 | 0 | —     | —     | 0.00  | 0.00 | 0.00 | paper-paper. **30d threshold reached; 0 trades → NOT promotion-eligible (need ≥10)**. Vol-compression gate (0.5× ATR threshold) blocked HYPE this wake — market in elevated-ATR rally phase. Net%=0 vs main +5.58% → behind on net return. vs BTC-hold: +2.20% |
| 4    | v0.4-mean-reversion-sleeve | LAB  | 2026-04-29 | 32 | 0 | —  | —     | 0.00  | 0.00 | 0.00 | paper-paper. **30d threshold reached; 0 trades → NOT promotion-eligible**. M2 (RSI<25) failed all pairs at both wakes — broad recovery put RSIs in 55-80 range. Net%=0. Sweep children: v0.8 (RSI 30), v0.9 (RSI 20). vs BTC-hold: +2.20% |
| —    | v0.13-trend-confirm     | LAB  | 2026-05-20 | 11 | 0 | — | — | 0.00 | 0.00 | 0.00 | **Hypothesis variant, interactive 2026-05-20.** 2 consecutive 1H closes > 20-EMA + 4H RSI≥50. Vol-comp gate (inherited from v0.3) blocked HYPE this wake — gate was binding constraint (not v0.13's own additional filters). 30d-eligible 2026-06-19. |
| 6    | v0.7-vol-comp-defensive | LAB-SWEEP | 2026-05-12 | 19 | 0 | — | — | 0.00 | 0.00 | 0.00 | **Phase 1 autoloop spawn 2026-05-12.** Threshold 0.5 → 0.7. Vol-comp gate (stricter threshold) blocked HYPE. 30d-eligible 2026-06-11. |
| 7    | v0.8-mean-rev-relaxed   | LAB-SWEEP | 2026-05-12 | 19 | 0 | — | — | 0.00 | 0.00 | 0.00 | **Phase 1 autoloop spawn 2026-05-12.** RSI floor 25 → 30. M2 (RSI<30) failed all pairs at both wakes (RSIs 55-80). 30d-eligible 2026-06-11. |
| 8    | v0.9-mean-rev-tight     | LAB-SWEEP | 2026-05-16 | 15 | 0 | — | — | 0.00 | 0.00 | 0.00 | **Phase 1 autoloop spawn 2026-05-16.** RSI floor 25 → 20. M2 (RSI<20) failed all — no deeply oversold pairs in recovery tape. 30d-eligible 2026-06-15. |
| 9    | v0.10-exit-confirm      | LAB-SUBSUMED  | 2026-05-16 | 15 | 0 | — | — | +1.23 | 0.00 | +1.23 | **SUBSUMED by main v0.4** (W22-G). **First trade this wake: HYPE/USD long 77 @ 68.06**. Stop 66.13, target 75.80. MTM 69.83 → unrealized +$136.29, equity $10,122.66. 2-bar EMA exit rule not yet testable (no closed trades). Flagged for retirement at routine #4. |
| 10   | v0.11-breakeven-2R      | LAB-SUBSUMED  | 2026-05-16 | 15 | 0 | — | — | +1.23 | 0.00 | +1.23 | **SUBSUMED by main v0.4** (W22-H-partial). **First trade: HYPE/USD long 77 @ 68.06**. Stop 66.13, target 75.80. Breakeven ratchet arms at HYPE≥71.94 (2R=3.88/unit); max 69.88 → not armed. Equity $10,122.66. Flagged for retirement at routine #4. |
| 11   | v0.12-sbd-exit          | LAB  | 2026-05-19 | 12 | 7 | 14.3% | -0.11 | -0.16 | 7.00 | -0.16 | **7 closed trades (backfill 05-19→05-26)**. **This wake: HYPE/USD long 76 @ 68.06** (1.49% risk of $9,863.26 equity). Stop 66.13, target 75.80. MTM 69.83 → equity $9,984.33. DD from peak reduced from 7.00% to 5.86%. SBD exit modification inactive (SBD cleared). 30d-eligible 2026-06-18. |
| —    | Codex v0 (competitor)   | EXTERNAL | 2026-04-29 | 17 | 1 closed (4 open) | — | +1.91 | -0.20 | 0.20 | **-0.20** | read-only. Poll 2026-05-16 (routine #4). 1 closed SOL +$112.92 (target-hit 05-12); 4 open (BTC/ETH×2/SOL) unrealized −$132.82. Equity $9,980.10 — dropped from +1.04 (05-10) as open ETH/SOL bled |
| —    | Codex Aggro v0 (comp.)  | EXTERNAL | 2026-04-29 | 17 | 1 closed (6 open) | — | -0.33 | -0.43 | 0.43 | **-0.43** | read-only. Poll 2026-05-16. Now SHORT 6 pairs, gross exposure 200.29% (margin — mandate-incompatible, do NOT copy). Cash −$9,967. Equity $9,957.13 |

Ranking is by 30-day rolling net return once variants pass 30-day live threshold. Pre-30d variants sort below main regardless of synthetic stats.

For the **competition** column: net % since 2026-04-29 baseline. This is the metric vs Codex by 2026-07-01 deadline.

## Cap & rotation

- **Concurrent variants cap:** **10** (raised from 3 on 2026-05-12 per user grant for Phase 1 autoloop)
- **Currently active:** 10 of 10 — **rack full** (v0.13-trend-confirm added 2026-05-20 interactive; displaced v0.6-vol-comp-aggressive — see Recently retired)
- **Categories:** 7 hypothesis variants (v0.3-vol-compression, v0.4-mean-rev, v0.5, v0.10, v0.11, v0.12, v0.13) + 3 parameter-sweep variants (v0.7, v0.8, v0.9)
- Rack is at cap. When an 11th variant qualifies: retire worst by 30d net return (parameter-sweep variants retired first; hypothesis variants protected)
- **Auto-spin-up step 8 gate:** requires active count < 3 (per routine #7 spec) — not triggered this wake (count 10). idea_bank IDEA-20260512-01 (score 12, under-review) remains queued but blocked by count gate and rack cap.

## Promotion candidates (current)

(none — v0.5 is the only ≥30d variant with positive net return (+1.23% unrealized from HYPE open), but **0 closed trades in rolling 30d window** (need ≥10). Not promotion-eligible. v0.3/v0.4-mean-rev at 0% net, also not promotion-eligible. The HYPE position opened this wake is the first trade signal for these variants after 32 days of regime-blocked conditions. Promotion clock starts once closed trades accumulate. Routine #4 next Saturday to assess retirement of v0.10/v0.11 (SUBSUMED) — note: both SUBSUMED variants now have their first live trades (HYPE long), providing some differentiation signal before retirement decision.)

### Last simulator wake

- **2026-05-12 22:00 PT** — Kraken MCP OK, 15/15 pairs fetched. **0 hypothetical trades** across all 3 variants. Kill switches all clear. Auto-spin-up: IDEA-20260512-01 (score 12) eligible by score but rack at capacity — no spin-up.
- **2026-05-16 22:00 PT** — Kraken MCP OK, 15/15 pairs fetched. **8 variants simulated, 0 hypothetical trades.** Broadly-red tape, 0/15 positive at EOD. Momentum variants regime-gated (5a); mean-reversion variants blocked by M3 synchronized crash bar. Per-variant kill switches: all clear. No auto-spin-up (count<3 gate; count was 8). See prior full entry in archive for detail.
- **2026-05-29 22:00 PT** — Kraken MCP OK (BTC/USD $73,183 smoke test). **10 variants simulated, 0 hypothetical trades.** Past-24h replay window 2026-05-29 05:00 UTC → 2026-05-30 05:00 UTC. **Regime: 1/15 pairs positive 24h (HYPE +0.67%); median 24h change −1.07%. SBD ACTIVE** (≤1/15 positive AND median ≤−1.0%). All 10 variants: 0 open positions → exit replay no-op. Per-variant kill switches: all clear at $10,000 synthetic equity. **30-day milestone:** v0.3/v0.4-mean-rev/v0.5 reached 30-day time threshold; 0 trades → NOT promotion-eligible (need ≥10 in rolling 30d window). Auto-spin-up step 8: count=10 — no spin-up.
- **2026-05-30 22:00 PT** — Kraken MCP OK (BTC/USD $74,078 smoke test). **10 variants simulated, 4 hypothetical trades (4 OPEN rows).** Replay window 2026-05-30T05:00Z → 2026-05-31T05:00Z. **Regime recovered from SBD:** OVERNIGHT wake (13:00Z 2026-05-30) ~12/15 positive (BTC +0.95%, HYPE +8.44%, TAO +1.12%, SOL +1.30%, FARTCOIN +0.56%; others inferred positive from broad recovery pattern); EOD wake (04:00Z 2026-05-31) 14/15 positive per main portfolio analysis, median +0.47%. SBD CLEARED. Wakes evaluated: OVERNIGHT (13:00Z), MIDDAY (default-skip), EOD (04:00Z). **OVERNIGHT gate analysis:** Momentum variants with vol-comp gate (v0.3, v0.7, v0.13): HYPE passed rules 1-3 but current 1H ATR(14)≈0.97 is NOT below 0.5× 30d mean — vol-comp gate blocked (elevated ATR post-HYPE rally). Mean-rev variants (v0.4, v0.8, v0.9): M2 (RSI<threshold) failed all pairs — RSIs in 55-80 range during recovery. Momentum variants WITHOUT vol-comp gate (v0.5, v0.10, v0.11, v0.12): **HYPE ENTERED at 13:00Z close (68.06)**. HYPE: rule 1 ✓ (68.06>EMA 66.01), rule 2 ✓ (RSI 79.5≥55), rule 3 ✓ (4H 67.81>50-EMA proxy ~61.50), cluster-cap OK (HYPE not in main cluster). Entry details: stop 66.13 (2×ATR 0.967), target 75.80 (4R), size 77 units (v0.5/v0.10/v0.11 from $10K) / 76 units (v0.12 from $9,863.26). **EOD exit replay:** HYPE min since entry 66.22 (16:00Z bar low) > stop 66.13 — not hit. Close 69.83 > EMA 68.05 → no EMA exit. 4R target 75.80 not reached. **EOD entry scan:** HYPE already open; no other pairs pass rule 3 (main portfolio confirmed BTC/TAO/ADA fail rule 3; HYPE RSI ~53 per main fails fresh-entry rule 2). 0 new entries at EOD. Per-variant kill switches: all clear. Auto-retirement: no triggers (no 60d underperformance, no kill-switch trips, rack full — no displacement). Auto-spin-up: count=10 >> 3 gate — no spin-up. **Leaderboard realignment:** v0.5 now leads ≥30d LAB rack at +1.23% unrealized, displacing v0.3/v0.4-mean-rev (0%) for rank 2.
- **2026-06-03 22:00 PT — SKIP: Kraken MCP + TradingView MCP both unavailable.** Attempted Kraken MCP smoke test (BTC/USD): no Kraken tools present in session. TradingView MCP CDP also failed ("fetch failed" after 5 attempts). Both primary and fallback data sources unreachable. **Per Ring-3 MCP-failure rule (localized to routine #7): skipping simulation, no variant files touched.** Pending replay window: 2026-05-31T05:00Z → 2026-06-04T05:00Z (72h / 3 days — 4 consecutive missed routine-07 wakes: 05-31, 06-01, 06-02, 06-03 PT). Gap within 7-day cap; replay will self-heal at next successful Kraken MCP session. Context from main portfolio during gap: 2026-06-02T15:00Z overnight showed 0/15 positive pairs, median −4.53% → **SBD likely active** during gap. v0.5/v0.10/v0.11/v0.12 have HYPE/USD long open (entry 68.06, stop 66.13) — HYPE price during gap unknown, stop-hit resolution deferred to next wake.
- **2026-06-04 22:00 PT — SKIP: Kraken MCP + TradingView MCP both unavailable.** Same failure mode as 2026-06-03. Kraken MCP: no tools present in session. TradingView MCP CDP: "fetch failed" after 5 attempts. **Per Ring-3 MCP-failure rule (localized to routine #7): skipping simulation, no variant files touched.** Pending replay window now: 2026-05-31T05:00Z → 2026-06-05T05:00Z (**5 days — 5 consecutive missed routine-07 wakes: 05-31, 06-01, 06-02, 06-03, 06-04 PT**). Gap within 7-day cap; replay will self-heal at next successful Kraken MCP session. **Critical: if MCP unavailability persists through 2026-06-07 (06-06 PT wake), the gap will exceed the 7-day cap and replay recovery will be partial.** v0.5/v0.10/v0.11/v0.12 HYPE/USD long still open (entry 68.06, stop 66.13, target 75.80) — stop-hit resolution continues to be deferred. Main portfolio (routine-03 2026-06-04) shows book flat at $10,254.63 with Kraken MCP also unavailable there.
- **2026-06-05 22:00 PT — SKIP: Kraken MCP unavailable.** Attempted Kraken MCP smoke test (BTC/USD): no Kraken tools present in session (ToolSearch returned no matches for "kraken"). TradingView MCP is connected (tools available via deferred loader) but cannot substitute for Kraken OHLCV data — variant entries/exits are priced against Kraken bars specifically. **Per Ring-3 MCP-failure rule (localized to routine #7): skipping simulation, no variant files touched.** Pending replay window: 2026-05-31T05:00Z → 2026-06-06T05:00Z (**6 days — 6 consecutive missed routine-07 wakes: 05-31, 06-01, 06-02, 06-03, 06-04, 06-05 PT**). Gap still within 7-day cap. **Critical: if MCP unavailability persists through 2026-06-07 (06-07 PT wake), the gap will exceed the 7-day cap and recovery will be partial — oldest hours beyond the cap will be permanently unrecoverable.** v0.5/v0.10/v0.11/v0.12 HYPE/USD long still open (entry 68.06, stop 66.13, target 75.80) — stop-hit resolution continues to be deferred. Main portfolio (routine-02-midday 2026-06-05) flat at $10,254.63, Kraken MCP also unavailable there.
- **2026-06-06 22:00 PT — SKIP: Kraken MCP unavailable.** ToolSearch for "kraken" returned no matches — Kraken MCP tools not present in session. TradingView MCP is connected. **Per Ring-3 MCP-failure rule (localized to routine #7): skipping simulation, no variant files touched.** Pending replay window: 2026-05-31T05:00Z → 2026-06-07T05:00Z (**7 days — 7 consecutive missed routine-07 wakes: 05-31, 06-01, 06-02, 06-03, 06-04, 06-05, 06-06 PT**). **Gap is now exactly at the 7-day cap.** If Kraken MCP is still unavailable at the next wake (2026-06-07 22:00 PT), replay will be capped at 7 days and the hours prior to 2026-06-07T05:00Z will be permanently unrecoverable. v0.5/v0.10/v0.11/v0.12 HYPE/USD long remains open (entry 68.06, stop 66.13, target 75.80) — HYPE has been trading since 2026-05-31 and the stop/target outcome is completely unknown; stop-hit resolution must await Kraken data. Main portfolio flat at $10,254.63 (EOD 2026-06-06). 0 trades on main today.

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
