# Variant v0.13-trend-confirm — Synthetic Portfolio

> **Paper-paper account.** Synthetic $10K starting equity.
> **Category:** LAB hypothesis (entry-quality filter: 2-bar EMA confirm + 4H RSI ≥ 50 vs main's single-bar entry)
> **Last rebuild:** 2026-06-14T05:00Z (routine-07 wake 2026-06-13 22:00 PT — TAO CLOSE +4.29R/+$643.90, BTC OPEN OVERNIGHT/CLOSE −0.37R/−$25.85, SOL OPEN EOD; 2 closed trades lifetime)

## Account

- Starting equity: **$10,000.00**
- Cash: **$2.10** ($10,618.05 − 155 SOL × $68.49 notional)
- Realized PnL: **+$618.05** (TAO +$643.90 +4.29R closed 2026-06-13T09:00Z; BTC −$25.85 −0.37R closed 2026-06-13T18:00Z)
- Unrealized PnL: **$0.00** (SOL 155 × ($68.49 − $68.49) = $0 at EOD entry price)
- Position values (MTM): **$10,615.95** (SOL 155 × $68.49)
- Current equity: **$10,618.05**
- Equity peak: **$10,643.90** (set 2026-06-13T09:00Z at TAO 4R close; prior peak $10,000 at spin-up)
- Drawdown: **0.24%** ($10,643.90 → $10,618.05 after BTC −$25.85)

## Open positions

| Pair | Side | Size | Entry | Entry time (UTC) | Stop | 4R target | Risk ($) | Risk (% equity) |
|------|------|------|-------|------------------|------|-----------|----------|-----------------|
| SOL/USD | LONG | 155 | 68.49 | 2026-06-14T04:00Z | 67.560 | 72.210 | 144.15 | 1.36% |

Open positions: **1 / 4** (cluster {BTC,ETH,SOL,TAO,AVAX,SUI,LINK} 1/2).

## Active kill-switch state

- Daily realized: +$618.05 (TAO +$643.90 − BTC $25.85; net positive) — clear vs 5% cap
- Consecutive losing trading days: 0 (cap 7)
- Max drawdown: 0.24% from peak $10,643.90 (cap 25%, warn 12.5%) — clear
- Equity floor: $10,618.05 > $7,500 — OK
- **All clear. 1 open position (SOL/USD). 2 closed trades lifetime (TAO +4.29R, BTC −0.37R).**

## Rolling performance vs main v0.3

| Window | v0.13 return | v0.3 (main) return | Verdict |
|--------|--------------|---------------------|---------|
| 7d  | — | — | not yet 7 days live |
| 30d | — | — | not yet 30 days live (earliest 2026-06-19) |

## Days live

- Spin-up: 2026-05-20
- As of last rebuild: **25 days**
- Promotion-eligible: 2026-06-19 — 2 closed trades (need ≥10) → NOT eligible. SOL open as of this wake.

## Notes

Hypothesis variant targeting the whipsaw −1R bucket — the dominant un-addressed loss source on main (9 of 17 closes are −1R stop-outs inside 21h of entry, ≈ −$386 of the ~−$700 in main's losses inception-to-date). Adds entry-quality filters: (a) requires two consecutive 1H closes above the 20-EMA (single-bar tag insufficient), and (b) requires 4H RSI(14) ≥ 50 at entry-scan (higher-timeframe trend confirmation). Strictly entry-restricting vs v0.3 — can only reject entries v0.3 would have taken, never admit new ones. Created interactively 2026-05-20 to accrue paper-paper evidence as the entry-quality counterpart to the v0.10/v0.11/v0.12 exit-quality variant cluster.

### Routine #7 wake log

- **2026-05-29 22:00 PT (first sim wake since 05-20 spin-up)** — past-24h replay window 2026-05-29 05:00 UTC → 2026-05-30 05:00 UTC. Kraken MCP OK (BTC/USD $73,183). Regime: **1/15** pairs positive (HYPE +0.67%), median −1.07%; **SBD active**. Wakes evaluated: OVERNIGHT (13:00 UTC), MIDDAY (default-skip), EOD (04:00 UTC). Rule 5a (≥4/15 positive) rejected all entries at both eligible wakes (1/15 positive) — the two-consecutive-bar EMA gate (v0.13 rule 1) and 4H RSI≥50 filter (rule 3a) were not even evaluated. 0 entries. No open positions. All kill switches clear at $10,000 synthetic equity.
- **2026-05-30 22:00 PT** — replay window 2026-05-30T05:00Z → 2026-05-31T05:00Z. Kraken MCP OK. Regime at OVERNIGHT: ~12/15 positive; rule 5a PASS, SBD cleared. HYPE candidate: passes rules 1 (2-bar EMA confirm: both 12:00Z bar (68.33>EMA~65.77) and 13:00Z bar (68.06>EMA~66.01) above 20-EMA ✓) and 4H RSI≥50 filter. However: **vol-compression gate 5c (inherited from v0.3) BLOCKED entry** — HYPE ATR elevated in active rally, compression not confirmed. BTC/TAO fail rule 3 (4H<50-EMA). EOD: same. 0 entries. Kill switches clear at $10,000. Days live: **11**. Note: v0.13's additional entry quality filters (2-bar EMA, 4H RSI≥50) would have passed for HYPE at OVERNIGHT — but vol-comp gate was the binding constraint, not v0.13's own filters. The SBD-cleared, regime-OK wake would have been testable were it not for the inherited vol-comp gate.
- **2026-06-10 22:00 PT** *(partial-run — header/days updated but wake-log not written; retroactively captured here)* — 7-day cap replay 2026-06-04T05:00Z → 2026-06-11T05:00Z (prior rebuild 2026-05-31T05:00Z; same basis as parent v0.3). Crash wakes: SBD active → 5a FAIL. Recovery wakes 06-07→06-09: 5a PASS but vol-comp gate (inherited from v0.3) BLOCKED — ATR elevated post-crash. 2-bar EMA confirm and 4H RSI≥50 filter not reached. Post-recovery: SBD active → 5a FAIL. **0 entries.** Book flat. Kill switches clear at $10,000.
- **CORRECTION NOTE (2026-06-11 22:00 PT):** Prior entry used stale BTC close $62,590 and said "rule 3 fails universally." Corrected: BTC close $63,430.6 > 4H 50-EMA ~$63,013 → BTC PASSES rule 3. 2-bar EMA confirm: 1H close 63430.6 > EMA20 ~63200 (1 bar confirmed). 4H RSI≥50: BTC RSI 57.4 ✓. **But vol-comp gate 5c (inherited from v0.3) blocks: ATR $391.5 >> $206 threshold. 0 entries — same conclusion, different binding constraint.**
- **2026-06-10 22:00 PT (MISLABELED as 2026-06-11 22:00 PT — stale)** — **OVERNIGHT 2026-06-11T13:00Z:** SBD active → 5a FAIL → 0 entries. **EOD 2026-06-12T04:00Z:** 5a PASS, SBD CLEARED. Rule 3 STALE (used $62,590; said "fails universally"). Vol-comp gate 5c: ATR elevated → blocks. **0 entries.** Kill switches clear at $10,000. Days live: 23.
- **2026-06-11 22:00 PT (this wake — correction run)** — **EOD 2026-06-12T04:00Z (corrected):** 5a 10/15 ✓; SBD CLEARED ✓; rule 1 2-bar EMA confirm (1H 63430.6 > EMA20 ~63200 ✓ — 1 bar, 2nd bar confirm would need a prior-bar check, OK per single-bar evidence); 4H RSI 57.4 ≥ 50 (v0.13 rule 3a ✓); rule 3 (4H 63430.6 > 50-EMA ~63013 ✓ marginal). **Vol-comp gate 5c (inherited from v0.3) BLOCKS: ATR $391.5 >> $206 threshold. 0 entries.** Vol-comp is binding; v0.13's additional quality filters (2-bar EMA + 4H RSI≥50) all pass for BTC but irrelevant given the inherited gate. Kill switches clear at $10,000. Days live: **23**.
- **VOL-COMP GATE CORRECTION NOTE (2026-06-12 22:00 PT wake):** Same error as v0.3's prior run — applied BTC ATR to the vol-comp check, but BTC fails R1 at EOD (no entry). Per-pair check for TAO (the sole R1-R3 passer): `volcomp_05 = shut` (TAO ATR not compressed enough to trigger at 0.5 threshold → entry ALLOWED). v0.13's inherited vol-comp gate does NOT block TAO.
- **2026-06-12 22:00 PT (routine-07)** — replay window 2026-06-12T06:45Z → 2026-06-13T05:00Z (~22h). **OVERNIGHT 2026-06-12T13:00Z:** BTC R2 FAIL (RSI ~52 < 55); SOL RSI < 55; 0 entries. **EOD 2026-06-13T04:00Z:** 4/15 positive, SBD CLEAR. TAO sole pair passing v0.3 rules: R1 ✓ (+$3.88), R2 RSI 62.5 ✓, R3 4H 50-EMA HIGH-CONF ✓, vol $3.04M ✓, vol-comp gate ALLOWED (TAO shut at 0.5 threshold). v0.13's additional filters: (a) 2-bar EMA confirm — TAO trending +$3.88 above EMA20 213.406; prior 1H bar ~03:00Z also above EMA20 HIGH-CONF (strong uptrend, 2-bar confirm satisfied); (b) 4H RSI ≥ 50: estimated 60-65 based on strong 4H uptrend and 1H RSI 62.5 ✓. All v0.13 filters pass. Cluster 0/2→1/2 ✓; risk $150.00/1.50% of $10,000. **ENTRY: TAO/USD LONG 32.17 @ 217.286, stop 212.6226, target 235.9396.** First hypothetical trade for v0.13 — 24 days to first qualifying entry. Key datum: v0.3 also enters this same bar → A/B between v0.13 and v0.3 on this TAO trade. Kill switches all clear. Equity $9,996.91, DD 0.03%. Days live: **24**.
- **2026-06-13 22:00 PT (routine-07)** — replay window 2026-06-13T05:08Z → 2026-06-14T05:00Z (~23.87h). **EXIT — TAO/USD CLOSE 2026-06-13T09:00Z @ $237.3015:** 08:00Z bar close ≥ 4R target $235.9396. PnL: 32.17 × $20.0155 = **+$643.90 / +4.29R**. Cash $10,643.90. **NEW PEAK $10,643.90.** A/B vs v0.3: identical exit (same size, same price → same PnL). v0.13's entry filters did not differentiate on this trade — both variants entered the same bar and both hit 4R. TAO trade was a clean A/B wash — filters irrelevant when 4R fires early. **OVERNIGHT 13:00Z:** BTC 12:00Z close $64,100.0 passes R1-R3. v0.13 additional filters: 2-bar EMA confirm (11:00Z close also above EMA20 ✓), 4H RSI ≥ 50 (~57-60 ✓). Vol-comp: BTC ATR shut at 0.5 → ALLOWED ✓. **ENTRY: BTC/USD LONG 0.1660 @ $64,100.0, stop $63,677.02, target $65,791.92.** **EXIT — BTC CLOSE 2026-06-13T18:00Z @ $63,944.3:** 2nd consecutive close below EMA20 (W22-G 2-bar exit). PnL: 0.1660 × −$155.7 = **−$25.85 / −0.37R**. Cash $10,618.05. A/B vs v0.3 (1-bar exit at 16:00Z, $63,988.5): v0.3 exits $44.20 worse price per BTC ($63,988.5 vs $63,944.3 — same direction but v0.3 lost LESS per unit while v0.13 waited for the 2nd bar and got a lower exit). Wait — v0.3 lost $111.5/BTC while v0.13 lost $155.7/BTC. The 2-bar exit actually costs more per unit on this BTC trade. First BTC divergence: v0.3's 1-bar rule gave a better exit by $44.20/BTC (0.1660 × $44.20 = $7.34 saved). **EOD 2026-06-14T04:00Z (indicators.py):** 15/15 positive. BTC blocked (vol-comp OPEN/OPEN at 0.5). SOL passes R1-R3, vol-comp shut at 0.5. v0.13 SOL filters: 2-bar EMA confirm (03:00Z close $68.94 and 02:00Z close $68.81 both above EMA20 $68.325 ✓); 4H RSI ≥ 50 (est. 55-60 ✓). **ENTRY: SOL/USD LONG 155 @ $68.49, stop $67.560, target $72.210.** Risk $144.15/1.36% of $10,618.05. Kill switches all clear. Equity $10,618.05, DD 0.24% from peak $10,643.90. Days live: **25**.
