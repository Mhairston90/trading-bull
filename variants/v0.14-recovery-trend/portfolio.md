# Variant v0.14-recovery-trend — Synthetic Portfolio

> **Paper-paper account.** Synthetic $10K starting equity.
> **Category:** LAB hypothesis (entry rule 3: 4H 20-EMA trend filter vs main's 50-EMA)
> **Last rebuild:** 2026-06-27T16:43Z (routine-07 wake 2026-06-27 PT — 09:43 PT OFF-SCHEDULE Saturday fire; 1 entry SOL/USD; OVERNIGHT 13:00Z Jun 27: R3-20 (4H 20-EMA) repaired; NEW PEAK $11,179.05; 9 closed trades lifetime)

## Account

- Starting equity: **$10,000.00**
- Cash: **$2,609.71** (post-open: $11,152.83 − $8,520.97 cost basis − $22.15 entry commission)
- Realized PnL (variant lifetime): **+$1,152.83** (BTC +$1.25 +0.01R; TAO +$643.90 +4.29R; BTC OVERNIGHT −$25.85 −0.37R; BTC EOD Jun14 −$7.83 −0.11R; HYPE Jun14 −$91.57 −0.58R; BTC Jun15/16 +$107.94 +0.68R; HYPE Jun16/17 +$210.78 +1.32R; SOL Jun20/21 +$319.57 +1.97R; AVAX Jun22 −$7.37 −0.04R)
- Unrealized PnL: **+$48.37** raw / **+$26.22** net of entry commission
- Position values (MTM @ $72.64): **$8,569.34**
- Current equity: **$11,179.05** (cash + MTM) — **NEW PEAK**
- Equity peak: **$11,179.05** (set at OVERNIGHT Jun27 13:00Z SOL entry MTM; prior peak $11,160.20)
- Drawdown from peak: **0.00%** (AT new peak)

## Open positions

| Pair | Side | Size | Entry | Stop | Target | Entry time (UTC) | Stop dist | Risk ($) | Cluster | Last | MTM | Unrealized R |
|------|------|-----:|------:|-----:|-------:|------------------|---------:|---------:|---------|-----:|----:|-------------:|
| SOL/USD | long | 117.97 | 72.23 | 70.812 | 77.902 | 2026-06-27T13:00:00Z | 1.418 | $167.27 | BTC-cluster | 72.64 | $8,569.34 | +0.03R |

Portfolio risk-at-moment: **1.50%** of equity. Cap 4% → 2.50pp headroom.
Open positions: **1 / 4** (cluster 1/2 BTC-cluster).

## Active kill-switch state

- Daily realized 2026-06-27 PT: $0.00 — CLEAR vs 5% cap
- Consecutive losing trading days: 1 (AVAX Jun22; cap 7) — CLEAR
- Max drawdown: 0.00% (AT new peak $11,179.05; cap 25%, warn 12.5%) — CLEAR
- Equity floor: $11,179.05 > $7,500 — OK
- Regime gate (5a): PASS — 14/15 positive 24h, median +1.60%, SBD CLEAR
- **All clear. 1 open position. 9 closed trades lifetime.**

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
- **2026-06-25 PT (routine-07, 2026-06-26T05:06Z — 22:05 PT on-schedule cron fire)** — Watchdog ALL CLEAR. Kraken MCP OK ($59,766.5 BTC). Replay window: 2026-06-25T19:19Z → 2026-06-26T05:06Z (~9.8h). MIDDAY 20:00Z: default skip. **EOD 2026-06-26T04:00Z** (routine-03-eod confirmed 04:11Z): 2/15 positive (SOL +0.77%, HYPE +1.24%), median −2.84%, 5a-SBD briefly CLEARED; 5a FAIL (2/15 < 4/15 floor) → 0 entries. Rule 3 v0.14: HYPE 4H 20-EMA — HYPE close ~$62.60 vs FAIL −0.35 R1 check; SOL R1 PASS but RSI 53.6 FAIL (R2 < 55). All 15 pairs fail R1 or R2; no entry proceeds to rule-3 check. Book flat → exit replay no-op. Post-EOD: SBD re-activated (0/15, −3.88%). Kill switches all clear (equity $11,152.83 unchanged). Rack leader at +11.53%. Days live: **16**.
- **2026-06-27 PT (routine-07, 2026-06-27T16:43Z — 09:43 PT OFF-SCHEDULE Saturday fire)** — Watchdog 1 finding (self-resolving). Kraken MCP OK (14/15 positive, median +1.60%, SBD CLEAR). Replay window: 2026-06-26T05:06Z → 2026-06-27T16:43Z (~35.6h). Wakes: OVERNIGHT Jun26 13:00Z (R3-20 fail: 4H 20-EMA binding same as 50-EMA for all 15 pairs → 0 entries), EOD Jun27 04:00Z (R3-20 binding → 0 entries), **OVERNIGHT Jun27 13:00Z**: 14/15 positive, SBD CLEAR, 5a PASS. SOL R3-20: 4H close $72.70 vs 4H 20-EMA ≈ $69.42 (+$3.28 clear margin, wider than 50-EMA margin of +$2.33). R3-20 PASS ✓ (confirmed to pass simultaneously with main's 50-EMA repair). No vol-comp gate for v0.14. Cluster 0/2→1/2. **ENTRY: SOL/USD LONG 117.97 @ $72.23, stop $70.812, target $77.902 (W22-G 2-bar EMA20 exit).** Cost $8,520.97, commission $22.15, cash $2,609.71. MTM @ $72.64: $8,569.34. Equity $11,179.05 — **NEW PEAK** (prior $11,160.20). Kill switches all clear. Rack leader at +11.79% MTM. Days live: **18**.
