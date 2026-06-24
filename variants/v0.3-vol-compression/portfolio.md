# Variant v0.3-vol-compression — Synthetic Portfolio

> **Paper-paper account.** Synthetic $10K starting equity. Does NOT affect main BULL portfolio or any real broker.
> **Rebuilt each routine #7 wake** from this variant's `trade_log.md`.
> **Last rebuild:** 2026-06-24T16:35Z (routine-07 wake 2026-06-24 PT — gap replay 2026-06-14T05:00Z→2026-06-24T13:00Z; SOL CLOSE 2026-06-14T06:00Z −0.27R/−$38.75 (1-bar EMA exit); 0 new entries across 10-day replay (vol-comp gate 5c blocked all); 3 closed trades lifetime)

## Account

- Starting equity: **$10,000.00**
- Cash: **$10,586.64** (flat — SOL closed 2026-06-14T06:00Z)
- Realized PnL (variant lifetime): **+$586.64** (TAO/USD +$643.90 +4.29R; BTC/USD −$18.51 −0.26R; SOL/USD −$38.75 −0.27R)
- Unrealized PnL: **$0.00** (no open positions)
- Position values (MTM): **$0.00**
- Current equity: **$10,586.64**
- Equity peak: **$10,643.90** (set 2026-06-13T09:00Z at TAO 4R close; unchanged)
- Drawdown from peak: **0.54%** ($10,643.90 → $10,586.64)

## Open positions

_None._

Portfolio risk-at-moment: **0.00%** (cap 4%, full headroom).
Open positions: **0 / 4** (cluster 0/2).

## Active kill-switch state

- Daily realized 2026-06-24 PT: $0.00 (last trade was SOL 2026-06-14) — clear vs 5% cap
- Consecutive losing trading days: 0 (cap 7)
- Max drawdown: 0.54% from peak $10,643.90 (cap 25%, warn 12.5%) — clear
- Equity floor: $10,586.64 > $7,500 — OK
- Regime gate: 5a FAIL / SBD ACTIVE at OVERNIGHT 2026-06-24T13:00Z → 0 entries this wake
- **All clear. No open positions. 3 closed trades lifetime (TAO +4.29R, BTC −0.26R, SOL −0.27R).**

## Rolling performance (vs main BULL v0.4)

| Window | v0.3 return | main (v0.4) return | Delta | BTC-hold | Result |
|--------|-------------|--------------------|----|----------|--------|
| 30d | +5.87% (since Apr 29 inception) | +4.14% ($10,413.87/$10,000−1) | +1.73% | −20.5% (BTC $75,750→$60,219) | v0.3 AHEAD (but 3 trades vs main's 20+) |
| 90d | — | — | — | — | not yet computable (90d window = 2026-07-22) |

## Days live

- Spin-up: 2026-04-29
- As of last rebuild: **56 days**
- Promotion-eligible date: **2026-05-29 (reached)** — 3 closed trades lifetime (need ≥10 in rolling 30d) → **NOT promotion-eligible.** Vol-comp gate 5c (0.5× threshold) is the binding constraint — blocked all 7 potential entries in the June 14–22 replay window (HYPE Jun14/16/17, BTC Jun15/22, SOL Jun20, XDG Jun22). Evidence of over-restriction accumulating.

## Notes

Tests whether a 0.5× ATR-compression entry gate improves net return / profit factor over main v0.2. Key finding from gap replay: v0.3 made 0 new entries in the June 14–24 replay window (10.5 days), while v0.5 (no gate) made 7 trades and returned +9.43%. The vol-comp gate blocked all rally entries — HYPE ($61→$75), BTC ($64k→$66k), SOL ($69→$73). Vol-comp gate costs ~3.56pp vs v0.5 in this window. **Preliminary conclusion: the 0.5× threshold is too restrictive in trending markets.**

### Routine #7 wake log

- **2026-05-12 22:00 PT** — past-24h replay window = 2026-05-11 16:00 UTC → 2026-05-12 16:00 UTC. Wakes evaluated: MIDDAY (2026-05-11 20:00 UTC, default-skip), EOD-prior (2026-05-12 04:00 UTC), OVERNIGHT (2026-05-12 13:00 UTC). At EOD-prior: positive-24h count 6/15 (regime 5a OK) but no pair passed rules 1+2+3 jointly. At OVERNIGHT: positive-24h count **0/15** → rule 5a rejected all entries. Result: 0 entries, 0 open positions to evaluate exits. All kill switches clear at $10,000 equity.
- **2026-05-16 22:00 PT (this wake)** — past-24h replay window = 2026-05-15 10:00 UTC → 2026-05-16 10:00 UTC. Wakes evaluated: OVERNIGHT (2026-05-15 13:00 UTC), MIDDAY (2026-05-15 20:00 UTC, default-skip), EOD (2026-05-16 04:00 UTC). Broadly-red tape: all 15 universe pairs negative on 24h change; the 05-15 13:00Z bar was a synchronized crash bar across the universe. Rule 5a (≥4/15 positive) **rejected all entries at both eligible wakes** (positive-24h count well below 4; 0/15 at EOD). Vol-compression gate 5c not reached. Result: 0 entries, 0 open positions to evaluate exits. All kill switches clear at $10,000 equity.
- **2026-05-29 22:00 PT** — past-24h replay window 2026-05-29 05:00 UTC → 2026-05-30 05:00 UTC. Kraken MCP OK (BTC/USD $73,183 smoke test). Regime: **1/15** universe pairs positive 24h (HYPE +0.67%); median 24h change −1.07%; **SBD active** this wake (≤1/15 positive AND median ≤−1.0%). Wakes evaluated: OVERNIGHT (2026-05-29 13:00 UTC), MIDDAY (2026-05-29 20:00 UTC, default-skip), EOD (2026-05-30 04:00 UTC). Rule 5a (≥4/15 positive) rejected all entries at both eligible wakes (1/15 positive). Vol-compression gate 5c not reached. 0 entries. No open positions — exit replay no-op. All kill switches clear at $10,000 synthetic equity. **30-day time threshold reached this wake.** 0 trades in rolling 30d window (need ≥10) → NOT promotion-eligible; variant continues in LAB.
- **2026-05-30 22:00 PT** — replay window 2026-05-30T05:00Z → 2026-05-31T05:00Z. Kraken MCP OK (BTC/USD $74,078). Wakes evaluated: OVERNIGHT (13:00Z 2026-05-30), MIDDAY (default-skip), EOD (04:00Z 2026-05-31). Regime at OVERNIGHT: ~12/15 positive 24h (BTC +0.95%, HYPE +8.44%); rule 5a PASS, SBD CLEARED. Candidate pair: HYPE — passes rules 1 (close 68.06 > EMA 66.01), 2 (RSI 79.5 ≥ 55), 3 (4H close 67.81 > 50-EMA ~61.50). **Vol-compression gate 5c BLOCKED entry:** current HYPE 1H ATR(14) ≈ 0.97 is not below 0.5× 30-day mean ATR (market in elevated-vol phase post-HYPE rally — compression gate requires quiet/compressed ATR, not present during active rally). EOD: 14/15 positive; same analysis — HYPE vol-comp gate would block; fresh entry also fails RSI ~53-60 per main analysis. 0 entries. Kill switches all clear at $10,000. Days live: **32**.
- **2026-06-10 22:00 PT routine-07** — Last rebuild was 2026-05-31T05:00Z; gap = 11 days → **7-day cap applied. Permanently unrecoverable: 2026-05-31T05:00Z → 2026-06-04T05:00Z (4 days).** Low risk: book was flat throughout the unrecoverable window; regime was SBD from 06-02 and vol-comp gate was blocking even in the brief 05-31 recovery. Replay window: **2026-06-04T05:00Z → 2026-06-11T05:00Z.** Crash wakes 06-04T13:00Z → 06-06T20:00Z: SBD ACTIVE (0-1/15 positive) → 5a FAIL. Recovery wakes 06-07T04:00Z → 06-09T04:00Z: 5a PASS (8-14/15 positive per gap replay audit) but **vol-comp gate 5c BLOCKED**: the 06-02→06-05 crash spiked 1H ATR(14) 3-5× across the universe; current ATR >> 0.5× 30d-mean throughout recovery (compressed ATR requires quiet tape, not crash-bounce). Post-recovery 06-09T13:00Z → tonight: SBD ACTIVE (1/15 positive BTC, median −2.30% at EOD 06-11T04:00Z) → 5a FAIL. **0 entries across entire 7-day cap window.** Exit replay no-op (book flat). Kill switches all clear at $10,000. Days live: **43**.
- **CORRECTION NOTE (2026-06-11 22:00 PT):** The entry labeled "2026-06-11 22:00 PT" below was written by the June 10 22:00 PT run (commit 8da048a, June 10 23:00:31 PT), which used stale BTC close ~$62,590 and concluded "all 15 pairs fail rule 3." With the corrected June 12 04:00Z bar (BTC close $63,430.6 > 4H 50-EMA ~$63,013), BTC actually **PASSES rule 3** (+$417, 0.66%). The binding constraint for this variant is the **vol-comp gate 5c** (ATR $391.5 >> 0.5× 30d-mean ~$206 threshold), not rule 3. The 0-entry conclusion is unchanged — vol-comp blocks — but the causal chain is different.
- **2026-06-10 22:00 PT (MISLABELED as 2026-06-11 22:00 PT — stale)** — replay window 2026-06-11T05:00Z → 2026-06-12T05:00Z (24h). Kraken MCP OK (BTC/USD $62,563 smoke test; 4H OHLCV unavailable). Wakes evaluated: OVERNIGHT (2026-06-11T13:00Z), MIDDAY (2026-06-11T20:00Z, default-skip), EOD (2026-06-12T04:00Z). **OVERNIGHT 2026-06-11T13:00Z:** SBD active — confirmed by flanking bookends: SBD at prior EOD 2026-06-11T04:00Z (1/15 positive, median −2.30%) AND SBD at midday 2026-06-11T20:00Z (1/15 positive, median −2.68% per main portfolio routine-03-eod); rule 5a FAIL → 0 entries. **EOD 2026-06-12T04:00Z:** MAJOR REGIME FLIP — 15/15 positive, median +2.72% (HYPE), 5a PASS, SBD CLEARED (per routine-03-eod 2026-06-11 main portfolio). Entry scan: all 15 universe pairs fail rule 3 (4H close < 4H 50-EMA — STALE: used BTC close $62,590 vs ~$63,589 EMA). Vol-comp gate 5c: ATR remains elevated post-crash bounce → also blocks. **0 entries.** Exit replay no-op (book flat). Kill switches all clear at $10,000. Days live: 44.
- **2026-06-11 22:00 PT (this wake — correction run)** — replay window 2026-06-12T04:00Z bar confirmed live. **EOD 2026-06-12T04:00Z (corrected):** 5a 10/15 positive ✓; SBD CLEARED ✓; rule 1 (1H 63430.6 > EMA20 ~63200 ✓); rule 2 (1H RSI 57.4 ≥ 55 ✓); rule 3 (4H 63430.6 > 4H 50-EMA ~63013 ✓ — passes marginally; prior session WRONG to say rule 3 fails universally). **Vol-comp gate 5c BLOCKS: current ATR $391.5, 30d-mean ATR ~$412, threshold 0.5×$412 = $206; current ATR far exceeds threshold. 0 entries.** Vol-comp gate is the binding constraint (rule 3 passes for BTC; vol-comp blocks). Exit replay no-op. Kill switches all clear at $10,000. Days live: **44**.
- **VOL-COMP GATE CORRECTION NOTE (2026-06-12 22:00 PT wake):** The above entry's reasoning "current ATR far exceeds threshold → blocks" was based on BTC's ATR ($391.5 >> $206). But BTC fails R1 at EOD (close 63,494 < EMA20 ~63,526), so the vol-comp gate is never even evaluated for BTC. The vol-comp check must be per-pair on the pairs that pass R1-R3. At this wake, TAO is the sole pair passing R1-R3. For TAO: indicators.py reports `volcomp_05 = shut` (atr NOT < 0.5×mean → gate NOT triggered → entry ALLOWED by rule 5c). The prior session incorrectly applied BTC's ATR to a gate that only matters for pairs that reach the entry scan.
- **2026-06-12 22:00 PT (routine-07)** — replay window 2026-06-12T06:45Z → 2026-06-13T05:00Z (~22h). **OVERNIGHT 2026-06-12T13:00Z:** BTC 1H close ~63,406.6 → R1 PASS, but R2 FAIL (RSI ~52 < 55); SOL RSI < 55 pre-rally; 0 entries. **EOD 2026-06-13T04:00Z:** 4/15 positive, SBD CLEAR. TAO sole PASS: R1 ✓ (+$3.88), R2 RSI 62.5 ✓, R3 4H 50-EMA HIGH-CONF ✓ (+$3.22), vol $3.04M ✓. Vol-comp gate 5c: TAO ATR 2.4062, indicators `volcomp_05 = shut` (NOT compressed → rule 5c does NOT reject) → **ALLOWED**. Cluster 0/2→1/2 ✓. Risk $150.00/1.50% of $10,000. **ENTRY: TAO/USD LONG 32.17 @ 217.286, stop 212.6226, target 235.9396.** This is v0.3's FIRST hypothetical trade — 45 days to first qualifying entry. Kill switches all clear. Equity $9,996.91, DD 0.03%. Days live: **45**.
- **2026-06-13 22:00 PT (routine-07)** — replay window 2026-06-13T05:08Z → 2026-06-14T05:00Z (~23.87h). EXIT TAO +4.29R/+$643.90. OVERNIGHT BTC OPEN @ 64100/CLOSE −0.26R/−$18.51 (1-bar EMA exit 17:00Z). EOD SOL OPEN @ 68.49. Kill switches all clear. Equity $10,625.39, DD 0.17% from peak $10,643.90. Days live: **46**.
- **2026-06-24 PT (routine-07 — gap replay via routine07_replay_20260623.py; fired ~09:35 PT off-schedule; date-guard: PT calendar 2026-06-24)** — Replay window: **2026-06-14T05:00Z → 2026-06-24T13:00Z** (10.5 days; Kraken REST 30d history fully covers gap — no unrecoverable bars). **EXIT — SOL/USD CLOSE 2026-06-14T06:00Z @ $68.24:** 05:00Z bar close 68.24 < 1H EMA20 ~68.35 → single-bar v0.3 exit fires immediately after entry (entered EOD 06-13, exits on first bar of replay). PnL: 155×($68.24−$68.49) = **−$38.75/−0.27R**. Cash $10,586.64. DD 0.54% from peak $10,643.90. **Entry scans (12 wakes in replay window):** Vol-comp gate 5c (0.5× threshold) BLOCKED all 7 potential momentum entries — HYPE (Jun14 OVERNIGHT, Jun16 EOD, Jun17 EOD), BTC (Jun15 EOD, Jun22 OVERNIGHT), SOL (Jun20 EOD), XDG (Jun22 OVERNIGHT). All pairs were in active-rally ATR regime (BTC ATR $365-380 >> $206 threshold; HYPE ATR 0.72-1.4 above 0.5× mean; SOL ATR 0.58-0.93 elevated). Zero new entries across entire 10-day window. **A/B signal: v0.5 (no vol-comp gate) made 7 new trades +$298/+$298 net, returned +9.43%; v0.3 made 0 new trades, returned +5.87%. Vol-comp gate cost ~3.56pp in the replay window — strongest evidence to date of over-restriction.** v0.13 (vol-comp + 2-bar exit) same outcome: 0 new entries, 1 exit (SOL −0.34R). **OVERNIGHT 2026-06-24T13:00Z assessment:** 0/15 positive, median −3.05%, SBD ACTIVE → 5a FAIL → 0 entries (regime blocks before gate). **EOD 2026-06-24T04:00Z (already elapsed):** 1/15 positive (AVAX +1.73%), median −3.68% → 5a FAIL. All kill switches clear. Days live: **56**.
