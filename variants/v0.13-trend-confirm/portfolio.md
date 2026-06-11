# Variant v0.13-trend-confirm — Synthetic Portfolio

> **Paper-paper account.** Synthetic $10K starting equity.
> **Category:** LAB hypothesis (entry-quality filter: 2-bar EMA confirm + 4H RSI ≥ 50 vs main's single-bar entry)
> **Last rebuild:** 2026-06-12T05:00Z (routine-07 wake 2026-06-11 22:00 PT — 0 trades; see notes)

## Account

- Starting equity: **$10,000.00**
- Cash: **$10,000.00**
- Realized PnL: **$0.00**
- Unrealized PnL: **$0.00**
- Current equity: **$10,000.00**
- Equity peak: **$10,000.00**
- Drawdown: **0.00%**

## Open positions

(none)

Open positions: **0 / 4** (momentum cap inherited from v0.3 rule 6).

## Active kill-switch state

All clear at $10,000 equity.

## Rolling performance vs main v0.3

| Window | v0.13 return | v0.3 (main) return | Verdict |
|--------|--------------|---------------------|---------|
| 7d  | — | — | not yet 7 days live |
| 30d | — | — | not yet 30 days live (earliest 2026-06-19) |

## Days live

- Spin-up: 2026-05-20
- As of last rebuild: **23 days**
- Promotion-eligible: 2026-06-19

## Notes

Hypothesis variant targeting the whipsaw −1R bucket — the dominant un-addressed loss source on main (9 of 17 closes are −1R stop-outs inside 21h of entry, ≈ −$386 of the ~−$700 in main's losses inception-to-date). Adds entry-quality filters: (a) requires two consecutive 1H closes above the 20-EMA (single-bar tag insufficient), and (b) requires 4H RSI(14) ≥ 50 at entry-scan (higher-timeframe trend confirmation). Strictly entry-restricting vs v0.3 — can only reject entries v0.3 would have taken, never admit new ones. Created interactively 2026-05-20 to accrue paper-paper evidence as the entry-quality counterpart to the v0.10/v0.11/v0.12 exit-quality variant cluster.

### Routine #7 wake log

- **2026-05-29 22:00 PT (first sim wake since 05-20 spin-up)** — past-24h replay window 2026-05-29 05:00 UTC → 2026-05-30 05:00 UTC. Kraken MCP OK (BTC/USD $73,183). Regime: **1/15** pairs positive (HYPE +0.67%), median −1.07%; **SBD active**. Wakes evaluated: OVERNIGHT (13:00 UTC), MIDDAY (default-skip), EOD (04:00 UTC). Rule 5a (≥4/15 positive) rejected all entries at both eligible wakes (1/15 positive) — the two-consecutive-bar EMA gate (v0.13 rule 1) and 4H RSI≥50 filter (rule 3a) were not even evaluated. 0 entries. No open positions. All kill switches clear at $10,000 synthetic equity.
- **2026-05-30 22:00 PT** — replay window 2026-05-30T05:00Z → 2026-05-31T05:00Z. Kraken MCP OK. Regime at OVERNIGHT: ~12/15 positive; rule 5a PASS, SBD cleared. HYPE candidate: passes rules 1 (2-bar EMA confirm: both 12:00Z bar (68.33>EMA~65.77) and 13:00Z bar (68.06>EMA~66.01) above 20-EMA ✓) and 4H RSI≥50 filter. However: **vol-compression gate 5c (inherited from v0.3) BLOCKED entry** — HYPE ATR elevated in active rally, compression not confirmed. BTC/TAO fail rule 3 (4H<50-EMA). EOD: same. 0 entries. Kill switches clear at $10,000. Days live: **11**. Note: v0.13's additional entry quality filters (2-bar EMA, 4H RSI≥50) would have passed for HYPE at OVERNIGHT — but vol-comp gate was the binding constraint, not v0.13's own filters. The SBD-cleared, regime-OK wake would have been testable were it not for the inherited vol-comp gate.
- **2026-06-10 22:00 PT** *(partial-run — header/days updated but wake-log not written; retroactively captured here)* — 7-day cap replay 2026-06-04T05:00Z → 2026-06-11T05:00Z (prior rebuild 2026-05-31T05:00Z; same basis as parent v0.3). Crash wakes: SBD active → 5a FAIL. Recovery wakes 06-07→06-09: 5a PASS but vol-comp gate (inherited from v0.3) BLOCKED — ATR elevated post-crash. 2-bar EMA confirm and 4H RSI≥50 filter not reached. Post-recovery: SBD active → 5a FAIL. **0 entries.** Book flat. Kill switches clear at $10,000.
- **2026-06-11 22:00 PT** — replay window 2026-06-11T05:00Z → 2026-06-12T05:00Z (24h). Kraken MCP OK (BTC/USD $62,563; 4H OHLCV unavailable). **OVERNIGHT 2026-06-11T13:00Z:** SBD active → 5a FAIL → 0 entries (2-bar EMA confirm gate not reached). **EOD 2026-06-12T04:00Z:** 5a PASS, SBD CLEARED. 4H RSI≥50 filter (v0.13 rule 3a): BTC RSI ~57.9 → PASSES ✓. 2-bar EMA confirm (rule 1): BTC 1H close ~$62,590 > 1H 20-EMA ~$61,769 — single bar confirmed (2nd bar moot since rule 3 binds first). Rule 3 (4H close < 4H 50-EMA): FAILS universally for all 15 pairs — binding constraint, same as parent v0.3. Vol-comp gate 5c (inherited): ATR elevated → also blocks. **0 entries.** Exit replay no-op (book flat). Kill switches all clear at $10,000. Days live: **23**.
