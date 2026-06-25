# Variant v0.13-trend-confirm — Synthetic Portfolio

> **Paper-paper account.** Synthetic $10K starting equity.
> **Category:** LAB hypothesis (entry-quality filter: 2-bar EMA confirm + 4H RSI ≥ 50 vs main's single-bar entry)
> **Last rebuild:** 2026-06-25T19:19Z (routine-07 wake 2026-06-25 PT — off-cron 12:19 PT; 0 entries, 0 trades; SBD ACTIVE 5a FAIL; 3 closed trades lifetime)

## Account

- Starting equity: **$10,000.00**
- Cash: **$10,568.45** (flat — SOL closed 2026-06-14T07:00Z)
- Realized PnL (variant lifetime): **+$568.45** (TAO +$643.90 +4.29R; BTC −$25.85 −0.37R; SOL −$49.60 −0.34R)
- Unrealized PnL: **$0.00** (no open positions)
- Position values (MTM): **$0.00**
- Current equity: **$10,568.45**
- Equity peak: **$10,643.90** (set 2026-06-13T09:00Z at TAO 4R close; unchanged)
- Drawdown from peak: **0.71%** ($10,643.90 → $10,568.45)

## Open positions

_None._

Portfolio risk-at-moment: **0.00%** (cap 4%, full headroom).
Open positions: **0 / 4** (cluster 0/2).

## Active kill-switch state

- Daily realized 2026-06-25 PT: $0.00 (last trade was SOL 2026-06-14) — clear vs 5% cap
- Consecutive losing trading days: 0 (cap 7)
- Max drawdown: 0.71% from peak $10,643.90 (cap 25%, warn 12.5%) — clear
- Equity floor: $10,568.45 > $7,500 — OK
- Regime gate: 5a FAIL / SBD ACTIVE at OVERNIGHT 2026-06-24T13:00Z → 0 entries
- **All clear. No open positions. 3 closed trades lifetime (TAO +4.29R, BTC −0.37R, SOL −0.34R).**

## Rolling performance vs main v0.3 AND v0.5

| Window | v0.13 return | v0.3 return | v0.5 return | main return | Verdict |
|--------|--------------|-------------|-------------|-------------|---------|
| 30d | +5.68% | +5.87% | +9.43% | +4.14% | v0.13 trails v0.5 by 3.75pp; v0.13 ahead of main. Vol-comp gate is binding — 3 trades vs v0.5's 10 |
| 90d | — | — | — | — | not yet computable |

## Days live

- Spin-up: 2026-05-20
- As of last rebuild: **36 days**
- Promotion-eligible: 2026-06-19 (reached) — 3 closed trades lifetime (need ≥10) → NOT promotion-eligible. Entry-quality filters (2-bar EMA + 4H RSI≥50) + vol-comp gate block nearly all entries. Very similar outcome to parent v0.3 (0 new entries in gap replay).

## Notes

Hypothesis variant targeting the whipsaw −1R bucket via tighter entry filters: (a) requires two consecutive 1H closes above the 20-EMA (single-bar tag insufficient), and (b) requires 4H RSI(14) ≥ 50 at entry-scan. Also inherits v0.3's vol-comp gate 5c (0.5× threshold) and 2-bar W22-G exit. Gap replay finding: like v0.3, the vol-comp gate blocked all potential HYPE/BTC/SOL entries across the replay window. The SOL exit was worse than v0.3 (−0.34R vs v0.3's −0.27R) because the 2-bar exit waited for one more bar down from v0.3's single-bar exit. Entry quality filters couldn't be evaluated since vol-comp blocked all scans.

### Routine #7 wake log

- **2026-05-29 22:00 PT (first sim wake since 05-20 spin-up)** — SBD active (1/15 positive). 5a FAIL → 0 entries. $10,000. Days live: **10**.
- **2026-05-30 22:00 PT** — 12/15 positive; 5a PASS. HYPE passes 2-bar EMA confirm + 4H RSI≥50 filters; vol-comp gate 5c (inherited) BLOCKED. 0 entries. $10,000. Days live: **11**.
- **2026-06-10 22:00 PT** *(partial-run)* — 7-day cap replay. Crash SBD → 5a FAIL. Recovery: 5a PASS but vol-comp blocked. 0 entries. $10,000.
- **CORRECTION NOTE (2026-06-11 22:00 PT):** BTC rule 3 passes with corrected close. 2-bar EMA confirm + 4H RSI≥50 pass for BTC. Vol-comp 5c BLOCKS. 0-entry conclusion unchanged.
- **2026-06-12 22:00 PT (routine-07)** — replay window 2026-06-12T06:45Z → 2026-06-13T05:00Z (~22h). OVERNIGHT: BTC R2 FAIL. EOD: TAO sole PASS. 2-bar EMA confirm ✓; 4H RSI 62.5≥50 ✓. Vol-comp gate: TAO volcomp_05=shut → ALLOWED ✓. **ENTRY: TAO/USD LONG 32.17 @ 217.286.** Days live: **24**.
- **2026-06-13 22:00 PT (routine-07)** — replay window 2026-06-13T05:08Z → 2026-06-14T05:00Z (~23.87h). EXIT TAO +4.29R/+$643.90. NEW PEAK $10,643.90. BTC OVERNIGHT OPEN/CLOSE −0.37R/−$25.85 (2-bar exit). SOL EOD OPEN @ $68.49. Kill switches clear. Equity $10,618.05, DD 0.24%. Days live: **25**.
- **2026-06-24 PT (routine-07 — gap replay via routine07_replay_20260623.py; fired ~09:35 PT off-schedule)** — Replay window: **2026-06-14T05:00Z → 2026-06-24T13:00Z** (10.5 days; fully recovered via Kraken REST 30d history). **EXIT — SOL/USD CLOSE 2026-06-14T07:00Z @ $68.17:** W22-G 2-bar exit: 05:00Z bar close below 1H EMA20 [1st]; 06:00Z bar close 68.17 < EMA20 ~68.33 [2nd consecutive] → fires 1 bar later than v0.3's single-bar exit (v0.3 exited at 06:00Z @ $68.24; v0.13 waits for 07:00Z @ $68.17). PnL: 155×($68.17−$68.49) = **−$49.60/−0.34R** (vs v0.3's −0.27R; 2-bar exit cost extra −0.07R on this SOL exit). Cash $10,568.45. **Entry scans (12 wakes in replay window):** Vol-comp gate 5c (0.5× threshold) BLOCKED all potential momentum entries — same as v0.3. HYPE (Jun14/16/17), BTC (Jun15/22), SOL (Jun20), XDG (Jun22) all blocked. The 2-bar EMA + 4H RSI≥50 entry quality filters were never evaluated (vol-comp gate is the upstream constraint). 0 new entries across 10-day replay. **Key A/B: v0.13 and v0.3 had identical entry outcomes (0 new entries), diverging only at SOL close (v0.13 −0.07R worse due to 2-bar exit). Cannot yet evaluate entry quality filters.** **OVERNIGHT 2026-06-24T13:00Z:** 0/15 positive, SBD ACTIVE → 5a FAIL → 0 entries. All kill switches clear. Days live: **35**.
- **2026-06-25 PT (routine-07, 2026-06-25T19:19Z — off-cron 12:19 PT)** — Watchdog ALL CLEAR. Kraken MCP OK. Replay window: 2026-06-24T16:35Z → 2026-06-25T19:19Z (~26.7h). Wakes evaluated: **EOD 2026-06-25T04:00Z**: 0/15 positive, SBD ACTIVE, 5a FAIL → 0 entries. **OVERNIGHT 2026-06-25T13:00Z**: BTC crashed −4.9%, SBD 5th consecutive wake, 5a FAIL → 0 entries. Vol-comp gate + 2-bar entry filter: not evaluated (5a blocks first). Book flat. Kill switches all clear (equity $10,568.45 unchanged). Days live: **36**.
