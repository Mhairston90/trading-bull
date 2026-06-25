# Variant v0.14-recovery-trend — Synthetic Portfolio

> **Paper-paper account.** Synthetic $10K starting equity.
> **Category:** LAB hypothesis (entry rule 3: 4H 20-EMA trend filter vs main's 50-EMA)
> **Last rebuild:** 2026-06-25T19:19Z (routine-07 wake 2026-06-25 PT — off-cron 12:19 PT; 0 entries, 0 trades; SBD ACTIVE 5a FAIL; 9 closed trades lifetime)

## Account

- Starting equity: **$10,000.00**
- Cash: **$11,152.83** (flat)
- Realized PnL (variant lifetime): **+$1,152.83** (BTC +$1.25 +0.01R; TAO +$643.90 +4.29R; BTC OVERNIGHT −$25.85 −0.37R; BTC EOD Jun14 −$7.83 −0.11R; HYPE Jun14 −$91.57 −0.58R; BTC Jun15/16 +$107.94 +0.68R; HYPE Jun16/17 +$210.78 +1.32R; SOL Jun20/21 +$319.57 +1.97R; AVAX Jun22 −$7.37 −0.04R)
- Unrealized PnL: **$0.00** (no open positions)
- Position values (MTM): **$0.00**
- Current equity: **$11,152.83**
- Equity peak: **$11,160.20** (set during AVAX Jun22 position peak MTM; AVAX reached slightly above entry before declining to exit at $6.268)
- Drawdown from peak: **0.07%** ($11,160.20 → $11,152.83)

## Open positions

_None._

Portfolio risk-at-moment: **0.00%** (cap 4%, full headroom).
Open positions: **0 / 4** (cluster 0/2).

## Active kill-switch state

- Daily realized 2026-06-25 PT: $0.00 (last trade was AVAX Jun22) — clear vs 5% cap
- Consecutive losing trading days: 1 (AVAX Jun22; cap 7) — clear
- Max drawdown: 0.07% from peak $11,160.20 (cap 25%, warn 12.5%) — clear
- Equity floor: $11,152.83 > $7,500 — OK
- Regime gate: 5a FAIL / SBD ACTIVE at OVERNIGHT 2026-06-24T13:00Z → 0 entries
- **All clear. No open positions. 9 closed trades lifetime.**

## Rolling performance vs main v0.4

| Window | v0.14 return | main return | Delta | BTC-hold | Result |
|--------|--------------|-------------|-------|----------|--------|
| 30d | +11.53% (all trades in last 12d) | +4.14% | +7.39% | −20.5% | v0.14 FAR AHEAD — best performer in rack |
| 90d | — | — | — | — | not yet computable (90d = 2026-09-07) |

## Closed trades summary

| Metric | Value |
|--------|-------|
| Closed | 9 |
| Win rate | 56% (5/9: BTC +0.01R, TAO +4.29R, BTC Jun15/16 +0.68R, HYPE Jun16/17 +1.32R, SOL +1.97R) |
| Avg R per trade | +0.91R |
| Profit factor | ~5.2 ($1,283 wins / $133 losses) |
| Net return | +11.53% |
| Max drawdown | 0.07% |

## Days live

- Spin-up: 2026-06-09
- As of last rebuild: **16 days**
- Promotion-eligible: 2026-07-09 (after the 2026-07-01 competition deadline). 9 closed trades (need ≥10 for promotion gate). Not yet eligible.

## Notes

Tests whether replacing the 4H 50-EMA trend filter with a 20-EMA converts confirmed regime recoveries into trades. The 20-EMA is closer to price — passes entry more readily, admits earlier-in-recovery entries. Key finding from gap replay: v0.14 took 6 new entries (BTC×2, HYPE×2, SOL, AVAX) using the 4H 20-EMA filter, while v0.5 also took 7 entries using the same 4H 50-EMA (v0.14 has no vol-comp gate AND uses 20-EMA). Both variants entered similar opportunities. v0.14's HYPE Jun16/17 +1.32R and SOL +1.97R match v0.12's 2-bar exit results (same exit rule) and are slightly better than v0.5's 1-bar exits. At 15 days, v0.14 is the top-performing variant at +11.53%.

### Routine #7 wake log

- **2026-06-10 22:00 PT (MISLABELED as 2026-06-11 22:00 PT — first sim wake, stale)** — replay window 2026-06-10T05:00Z → 2026-06-12T05:00Z. SBD active at first 3 wakes → 5a FAIL → 0 entries. EOD 2026-06-12T04:00Z: 5a PASS but used stale close $62,590 → 0 entries (conservative). $10,000. Days live: **3**.
- **2026-06-11 22:00 PT (correction run — first real entry)** — BTC close confirmed $63,430.6. Rule 3 v0.14: 4H close $63,430.6 > 4H 20-EMA ~$62,409 ✓ (+$1,021 clear margin vs 50-EMA's marginal +$417). **ENTRY: BTC/USD LONG 0.157653 @ 63430.6, stop 62647.6, target 66562.6.** v0.14's FIRST trade. Equity MTM $10,020.92. Days live: **3**.
- **2026-06-12T06:45Z interactive — ENTRY RE-VALIDATED:** Converged 720-bar 4H 20-EMA = $62,652.1 → BTC passes rule 3 by +$778.5. Same re-check voided v0.5/v0.12 BTC entries (50-EMA = $63,682.6 → FAILS). v0.14 holds rack's only live position; clean A/B vs main's deferral.
- **2026-06-12 22:00 PT (routine-07)** — BTC CLOSE 2026-06-12T22:00Z +0.01R/+$1.25 (2-bar exit: 20:00Z + 21:00Z bars below 1H EMA20). EOD: TAO sole PASS. **ENTRY: TAO/USD LONG 32.17 @ 217.286.** Equity $9,998.16. Days live: **4**.
- **2026-06-13 22:00 PT (routine-07)** — EXIT TAO +4.29R/+$643.90. NEW PEAK $10,645.15. BTC OVERNIGHT OPEN/CLOSE −0.37R/−$25.85 (2-bar). BTC EOD OPEN @ $64,320.2. Equity $10,619.30, DD 0.24%. Days live: **5**.
- **2026-06-24 PT (routine-07 — gap replay via routine07_replay_20260623.py; fired ~09:35 PT off-schedule)** — Replay window: **2026-06-14T05:00Z → 2026-06-24T13:00Z** (10.5 days; fully recovered via Kraken REST 30d history). **6 new closes, 6 new opens across 12 wakes.** Trade sequence: **BTC EOD Jun14 CLOSE −0.11R/−$7.83** (2-bar exit fires at Jun14T13:00Z); **HYPE Jun14 OPEN/CLOSE −0.58R/−$91.57** (2-bar fires Jun14T16:00Z after 14:00Z+15:00Z bars below EMA; 20-EMA rule 3 PASSES for HYPE, same as v0.5/v0.12; no vol-comp gate); **BTC Jun15/16 OPEN/CLOSE +0.68R/+$107.94** (2-bar fires Jun16T04:00Z after 24h hold); **HYPE Jun16/17 OPEN/CLOSE +1.32R/+$210.78** (2-bar fires Jun17T08:00Z; held 28h from Jun16T04:00Z — best HYPE trade across variants); **SOL Jun20/21 OPEN/CLOSE +1.97R/+$319.57** (2-bar fires Jun21T22:00Z; 41h hold — v0.14's best trade by R); **AVAX Jun22 OPEN/CLOSE −0.04R/−$7.37** (EOD Jun22 entry using 4H 20-EMA: AVAX passes rule 3 with 20-EMA but not 50-EMA; 2-bar exit fires Jun22T20:00Z as AVAX fails to hold the 18:00Z+19:00Z bars above EMA20; minor scalp). **NEW PEAK $11,160.20** set during AVAX peak MTM (Jun22); AVAX close at −$7.37 = barely below entry → essentially breakeven. Net replay realized: +$533.53. Total equity $11,152.83, DD 0.07% from peak. **v0.14 is the best-performing variant at +11.53% — 7.39pp ahead of main.** Key divergence: AVAX Jun22 entry was v0.14-specific (4H 20-EMA passes for AVAX; 50-EMA variant would have missed); essentially a 0 net on this trade. **OVERNIGHT 2026-06-24T13:00Z:** 0/15 positive, SBD ACTIVE → 5a FAIL → 0 entries. All kill switches clear. Days live: **15**.
- **2026-06-25 PT (routine-07, 2026-06-25T19:19Z — off-cron 12:19 PT)** — Watchdog ALL CLEAR. Kraken MCP OK ($59,407 BTC). Replay window: 2026-06-24T16:35Z → 2026-06-25T19:19Z (~26.7h). Wakes evaluated: **EOD 2026-06-25T04:00Z**: 0/15 positive, SBD ACTIVE, 5a FAIL → 0 entries. **OVERNIGHT 2026-06-25T13:00Z**: BTC crashed 61,146→58,218 −4.9%, SBD 5th consecutive wake, 0/15 positive, 5a FAIL → 0 entries. Book flat → no exit triggers. Kill switches all clear (equity $11,152.83 unchanged). v0.14 remains rack leader at +11.53% (16d). Days live: **16**.
