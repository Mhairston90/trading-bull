# Variant v0.3-vol-compression — Synthetic Portfolio

> **Paper-paper account.** Synthetic $10K starting equity. Does NOT affect main BULL portfolio or any real broker.
> **Rebuilt each routine #7 wake** from this variant's `trade_log.md`.
> **Last rebuild:** 2026-06-14T05:00Z (routine-07 wake 2026-06-13 22:00 PT — TAO CLOSE +4.29R/+$643.90, BTC OPEN OVERNIGHT/CLOSE −0.26R/−$18.51, SOL OPEN EOD; 2 closed trades lifetime)

## Account

- Starting equity: **$10,000.00**
- Cash: **$9.44** ($10,625.39 − 155 SOL × $68.49 notional)
- Realized PnL (variant lifetime): **+$625.39** (TAO/USD +$643.90 +4.29R closed 2026-06-13T09:00Z; BTC/USD −$18.51 −0.26R closed 2026-06-13T17:00Z)
- Unrealized PnL: **$0.00** (SOL 155 × ($68.49 − $68.49) = $0 at EOD entry price)
- Position values (MTM): **$10,615.95** (SOL 155 × $68.49)
- Current equity (cash + positions MTM): **$10,625.39**
- Equity peak: **$10,643.90** (set 2026-06-13T09:00Z at TAO 4R close; prior peak $10,000 at spin-up)
- Drawdown from peak: **0.17%** ($10,643.90 → $10,625.39 after BTC −$18.51)

## Open positions

| Pair | Side | Size | Entry | Entry time (UTC) | Stop | 4R target | Risk ($) | Risk (% equity) |
|------|------|------|-------|------------------|------|-----------|----------|-----------------|
| SOL/USD | LONG | 155 | 68.49 | 2026-06-14T04:00Z | 67.560 | 72.210 | 144.15 | 1.36% |

Portfolio risk-at-moment: **1.36%** (cap 4%).
Open positions: **1 / 4** (cluster {BTC,ETH,SOL,TAO,AVAX,SUI,LINK} 1/2).

## Active kill-switch state

- Daily realized: +$625.39 (TAO +$643.90 − BTC $18.51; net positive, loss cap is downside-only) — clear vs 5% cap
- Consecutive losing trading days: 0 (cap 7)
- Max drawdown: 0.17% from peak $10,643.90 (cap 25%, warn 12.5%) — clear
- Equity floor: $10,625.39 > $7,500 — OK
- **All clear. 1 open position (SOL/USD). 2 closed trades lifetime (TAO +4.29R, BTC −0.26R).**

## Rolling performance (vs main BULL v0.2)

| Window | v0.3 return | v0.2 main return | Delta | BTC-hold | Result |
|--------|-------------|------------------|-------|----------|--------|
| 7d  | 0.00% | — | — | −3.01% (BTC 7d) | v0.3 in cash; BTC fell 3.01% over 7d (May 22→29) |
| 30d | 0.00% | +6.63% (main since Apr 29) | −6.63% | −3.39% (BTC Apr 29→May 29: $75,750→$73,183) | MAIN AHEAD; 0 trades — NOT promotion-eligible (need ≥10 in 30d) |
| 90d | — | — | — | — | not yet 90 days live |

(Populated by routine #7 once windows close.)

## Days live

- Spin-up: 2026-04-29
- As of last rebuild: **46 days**
- Promotion-eligible date: **2026-05-29 (reached)** — 2 closed trades lifetime (need ≥10 in rolling 30d) → NOT promotion-eligible. SOL open as of this wake.

## Notes

This variant exists to test whether a 0.5× ATR-compression entry gate improves net return / profit factor over main v0.2. See `README.md` and `strategy.md` in this directory for full hypothesis.

The variant runs entirely paper-paper. Its trades have NO effect on the real BULL portfolio in `memory/portfolio.md`. The leaderboard at `memory/leaderboard.md` shows side-by-side performance.

### Routine #7 wake log

- **2026-05-12 22:00 PT** — past-24h replay window = 2026-05-11 16:00 UTC → 2026-05-12 16:00 UTC. Wakes evaluated: MIDDAY (2026-05-11 20:00 UTC, default-skip), EOD-prior (2026-05-12 04:00 UTC), OVERNIGHT (2026-05-12 13:00 UTC). At EOD-prior: positive-24h count 6/15 (regime 5a OK) but no pair passed rules 1+2+3 jointly. At OVERNIGHT: positive-24h count **0/15** → rule 5a rejected all entries. Result: 0 entries, 0 open positions to evaluate exits. All kill switches clear at $10,000 equity.
- **2026-05-16 22:00 PT (this wake)** — past-24h replay window = 2026-05-15 10:00 UTC → 2026-05-16 10:00 UTC (Kraken's latest closed 1H bar 05-16 10:00Z; routine #7 last ran 05-12, but routine spec scopes replay to trailing 24h). Wakes evaluated: OVERNIGHT (2026-05-15 13:00 UTC), MIDDAY (2026-05-15 20:00 UTC, default-skip), EOD (2026-05-16 04:00 UTC). Broadly-red tape: all 15 universe pairs negative on 24h change; the 05-15 13:00Z bar was a synchronized crash bar across the universe. Rule 5a (≥4/15 positive) **rejected all entries at both eligible wakes** (positive-24h count well below 4; 0/15 at EOD). Vol-compression gate 5c not reached. Result: 0 entries, 0 open positions to evaluate exits. All kill switches clear at $10,000 equity.
- **2026-05-29 22:00 PT** — past-24h replay window 2026-05-29 05:00 UTC → 2026-05-30 05:00 UTC. Kraken MCP OK (BTC/USD $73,183 smoke test). Regime: **1/15** universe pairs positive 24h (HYPE +0.67%); median 24h change −1.07%; **SBD active** this wake (≤1/15 positive AND median ≤−1.0%). Wakes evaluated: OVERNIGHT (2026-05-29 13:00 UTC), MIDDAY (2026-05-29 20:00 UTC, default-skip), EOD (2026-05-30 04:00 UTC). Rule 5a (≥4/15 positive) rejected all entries at both eligible wakes (1/15 positive). Vol-compression gate 5c not reached. 0 entries. No open positions — exit replay no-op. All kill switches clear at $10,000 synthetic equity. **30-day time threshold reached this wake.** 0 trades in rolling 30d window (need ≥10) → NOT promotion-eligible; variant continues in LAB.
- **2026-05-30 22:00 PT** — replay window 2026-05-30T05:00Z → 2026-05-31T05:00Z. Kraken MCP OK (BTC/USD $74,078). Wakes evaluated: OVERNIGHT (13:00Z 2026-05-30), MIDDAY (default-skip), EOD (04:00Z 2026-05-31). Regime at OVERNIGHT: ~12/15 positive 24h (BTC +0.95%, HYPE +8.44%); rule 5a PASS, SBD CLEARED. Candidate pair: HYPE — passes rules 1 (close 68.06 > EMA 66.01), 2 (RSI 79.5 ≥ 55), 3 (4H close 67.81 > 50-EMA ~61.50). **Vol-compression gate 5c BLOCKED entry:** current HYPE 1H ATR(14) ≈ 0.97 is not below 0.5× 30-day mean ATR (market in elevated-vol phase post-HYPE rally — compression gate requires quiet/compressed ATR, not present during active rally). EOD: 14/15 positive; same analysis — HYPE vol-comp gate would block; fresh entry also fails RSI ~53-60 per main analysis. 0 entries. Kill switches all clear at $10,000. Days live: **32**.
- **2026-06-10 22:00 PT routine-07** — Last rebuild was 2026-05-31T05:00Z; gap = 11 days → **7-day cap applied. Permanently unrecoverable: 2026-05-31T05:00Z → 2026-06-04T05:00Z (4 days).** Low risk: book was flat throughout the unrecoverable window; regime was SBD from 06-02 and vol-comp gate was blocking even in the brief 05-31 recovery. Replay window: **2026-06-04T05:00Z → 2026-06-11T05:00Z.** Crash wakes 06-04T13:00Z → 06-06T20:00Z: SBD ACTIVE (0-1/15 positive) → 5a FAIL. Recovery wakes 06-07T04:00Z → 06-09T04:00Z: 5a PASS (8-14/15 positive per gap replay audit) but **vol-comp gate 5c BLOCKED**: the 06-02→06-05 crash spiked 1H ATR(14) 3-5× across the universe; current ATR >> 0.5× 30d-mean throughout recovery (compressed ATR requires quiet tape, not crash-bounce). Post-recovery 06-09T13:00Z → tonight: SBD ACTIVE (1/15 positive BTC, median −2.30% at EOD 06-11T04:00Z) → 5a FAIL. **0 entries across entire 7-day cap window.** Exit replay no-op (book flat). Kill switches all clear at $10,000. Days live: **43**.
- **CORRECTION NOTE (2026-06-11 22:00 PT):** The entry labeled "2026-06-11 22:00 PT" below was written by the June 10 22:00 PT run (commit 8da048a, June 10 23:00:31 PT), which used stale BTC close ~$62,590 and concluded "all 15 pairs fail rule 3." With the corrected June 12 04:00Z bar (BTC close $63,430.6 > 4H 50-EMA ~$63,013), BTC actually **PASSES rule 3** (+$417, 0.66%). The binding constraint for this variant is the **vol-comp gate 5c** (ATR $391.5 >> 0.5× 30d-mean ~$206 threshold), not rule 3. The 0-entry conclusion is unchanged — vol-comp blocks — but the causal chain is different.
- **2026-06-10 22:00 PT (MISLABELED as 2026-06-11 22:00 PT — stale)** — replay window 2026-06-11T05:00Z → 2026-06-12T05:00Z (24h). Kraken MCP OK (BTC/USD $62,563 smoke test; 4H OHLCV unavailable). Wakes evaluated: OVERNIGHT (2026-06-11T13:00Z), MIDDAY (2026-06-11T20:00Z, default-skip), EOD (2026-06-12T04:00Z). **OVERNIGHT 2026-06-11T13:00Z:** SBD active — confirmed by flanking bookends: SBD at prior EOD 2026-06-11T04:00Z (1/15 positive, median −2.30%) AND SBD at midday 2026-06-11T20:00Z (1/15 positive, median −2.68% per main portfolio routine-03-eod); rule 5a FAIL → 0 entries. **EOD 2026-06-12T04:00Z:** MAJOR REGIME FLIP — 15/15 positive, median +2.72% (HYPE), 5a PASS, SBD CLEARED (per routine-03-eod 2026-06-11 main portfolio). Entry scan: all 15 universe pairs fail rule 3 (4H close < 4H 50-EMA — STALE: used BTC close $62,590 vs ~$63,589 EMA). Vol-comp gate 5c: ATR remains elevated post-crash bounce → also blocks. **0 entries.** Exit replay no-op (book flat). Kill switches all clear at $10,000. Days live: 44.
- **2026-06-11 22:00 PT (this wake — correction run)** — replay window 2026-06-12T04:00Z bar confirmed live. **EOD 2026-06-12T04:00Z (corrected):** 5a 10/15 positive ✓; SBD CLEARED ✓; rule 1 (1H 63430.6 > EMA20 ~63200 ✓); rule 2 (1H RSI 57.4 ≥ 55 ✓); rule 3 (4H 63430.6 > 4H 50-EMA ~63013 ✓ — passes marginally; prior session WRONG to say rule 3 fails universally). **Vol-comp gate 5c BLOCKS: current ATR $391.5, 30d-mean ATR ~$412, threshold 0.5×$412 = $206; current ATR far exceeds threshold. 0 entries.** Vol-comp gate is the binding constraint (rule 3 passes for BTC; vol-comp blocks). Exit replay no-op. Kill switches all clear at $10,000. Days live: **44**.
- **VOL-COMP GATE CORRECTION NOTE (2026-06-12 22:00 PT wake):** The above entry's reasoning "current ATR far exceeds threshold → blocks" was based on BTC's ATR ($391.5 >> $206). But BTC fails R1 at EOD (close 63,494 < EMA20 ~63,526), so the vol-comp gate is never even evaluated for BTC. The vol-comp check must be per-pair on the pairs that pass R1-R3. At this wake, TAO is the sole pair passing R1-R3. For TAO: indicators.py reports `volcomp_05 = shut` (atr NOT < 0.5×mean → gate NOT triggered → entry ALLOWED by rule 5c). The prior session incorrectly applied BTC's ATR to a gate that only matters for pairs that reach the entry scan.
- **2026-06-12 22:00 PT (routine-07)** — replay window 2026-06-12T06:45Z → 2026-06-13T05:00Z (~22h). **OVERNIGHT 2026-06-12T13:00Z:** BTC 1H close ~63,406.6 → R1 PASS, but R2 FAIL (RSI ~52 < 55); SOL RSI < 55 pre-rally; 0 entries. **EOD 2026-06-13T04:00Z:** 4/15 positive, SBD CLEAR. TAO sole PASS: R1 ✓ (+$3.88), R2 RSI 62.5 ✓, R3 4H 50-EMA HIGH-CONF ✓ (+$3.22), vol $3.04M ✓. Vol-comp gate 5c: TAO ATR 2.4062, indicators `volcomp_05 = shut` (NOT compressed → rule 5c does NOT reject) → **ALLOWED**. Cluster 0/2→1/2 ✓. Risk $150.00/1.50% of $10,000. **ENTRY: TAO/USD LONG 32.17 @ 217.286, stop 212.6226, target 235.9396.** This is v0.3's FIRST hypothetical trade — 45 days to first qualifying entry. Key observation: vol-comp gate finally allows after 45d of elevated-ATR environments; TAO's ATR is the first pair to show sufficient compression at EOD while simultaneously passing R1-R3. Kill switches all clear. Equity $9,996.91, DD 0.03%. Days live: **45**.
- **2026-06-13 22:00 PT (routine-07)** — replay window 2026-06-13T05:08Z → 2026-06-14T05:00Z (~23.87h). **EXIT — TAO/USD CLOSE 2026-06-13T09:00Z @ $237.3015:** 08:00Z bar close $237.3015 ≥ 4R target $235.9396 → 4R exit fires. PnL: 32.17 × $20.0155 = **+$643.90 / +4.29R**. Cash post-close $10,643.90. **NEW PEAK $10,643.90.** **OVERNIGHT 13:00Z:** BTC 12:00Z bar close $64,100.0 passes R1 (+$250 above EMA20), R2 (RSI ~58), R3 (4H 50-EMA +$338), R4a, 5a pos. Vol-comp 5c: BTC ATR ~$211 vs 0.5×mean ~$206 — shut at 0.5 → ALLOWED ✓. **ENTRY: BTC/USD LONG 0.1660 @ $64,100.0, stop $63,677.02, target $65,791.92.** Cash-binding (ideal 0.3774 BTC). **EXIT — BTC/USD CLOSE 2026-06-13T17:00Z @ $63,988.5:** 16:00Z 1H close $63,988.5 < EMA20 ~$64,003 — single-bar v0.3 exit rule. Stop $63,677.02 not hit. PnL: 0.1660 × −$111.5 = **−$18.51 / −0.26R**. Cash post-close $10,625.39. **EOD 2026-06-14T04:00Z (indicators.py):** 15/15 positive, median +1.32%. BTC blocked (vol-comp OPEN/OPEN at 0.5). SOL passes R1-R3, vol-comp `shut` at 0.5 → ALLOWED. **ENTRY: SOL/USD LONG 155 @ $68.49, stop $67.560, target $72.210.** Risk $144.15/1.36% of $10,625.39. Kill switches all clear. Equity $10,625.39, DD 0.17% from peak $10,643.90. Days live: **46**.
