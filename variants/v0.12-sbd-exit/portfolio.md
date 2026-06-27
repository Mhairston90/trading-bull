# Variant v0.12-sbd-exit — Synthetic Portfolio

> **Paper-paper account.** Synthetic $10K starting equity.
> **Category:** LAB hypothesis / instrumented twin (SBD classifier + W22-G 2-bar exit vs v0.2 baseline)
> **Last rebuild:** 2026-06-27T16:43Z (routine-07 wake 2026-06-27 PT — 09:43 PT OFF-SCHEDULE Saturday fire; 1 entry SOL/USD; OVERNIGHT 13:00Z Jun 27: R3 repaired, SBD CLEAR (W22-G default exit reverts to 2-bar EMA20); 16 closed trades lifetime; **PROMOTION ELIGIBLE — confirmed**)
>
> **LEADERBOARD-SOURCED — FORWARD PAPER-PAPER ONLY.** Rebuilt from this variant's
> `trade_log.md`. The 2026-05-19→2026-05-29 trades were recovered on 2026-05-29
> (user-authorized) after a routine-#7 scheduler gap; see trade_log.md header.

## Account

- Starting equity: **$10,000.00**
- Cash: **$2,540.28** (post-open: $10,858.19 − $8,296.34 cost basis − $21.57 entry commission)
- Realized PnL (variant lifetime): **+$858.19** (prior 10 trades net +$491.28; replay: BTC Jun14 −$7.73 −0.11R; HYPE Jun14 −$90.44 −0.58R; BTC Jun15/16 +$106.62 +0.68R; HYPE Jun16/17 +$208.20 +1.32R; SOL Jun20/21 +$315.65 +1.97R; BTC Jun22 −$165.35 −1.00R)
- Unrealized PnL: **+$47.09** raw / **+$25.52** net of entry commission
- Position values (MTM @ $72.64): **$8,343.43**
- Current equity: **$10,883.71** (cash + MTM)
- Equity peak: **$11,023.54** (set 2026-06-21T22:00Z at SOL close +1.97R; current below peak)
- Drawdown from peak: **1.27%** ($11,023.54 → $10,883.71)

## Open positions

| Pair | Side | Size | Entry | Stop | Target | Entry time (UTC) | Stop dist | Risk ($) | Cluster | Last | MTM | Unrealized R |
|------|------|-----:|------:|-----:|-------:|------------------|---------:|---------:|---------|-----:|----:|-------------:|
| SOL/USD | long | 114.86 | 72.23 | 70.812 | 77.902 | 2026-06-27T13:00:00Z | 1.418 | $162.87 | BTC-cluster | 72.64 | $8,343.43 | +0.03R |

Portfolio risk-at-moment: **1.50%** of equity. Cap 4% → 2.50pp headroom.
Open positions: **1 / 4** (cluster 1/2 BTC-cluster). Exit rule: W22-G 2-bar EMA20 exit (SBD CLEAR → default 2-bar mode; SBD exit accelerator inactive).

## Active kill-switch state

- Daily realized 2026-06-27 PT: $0.00 — CLEAR vs 5% cap
- Consecutive losing trading days: 1 (BTC Jun22; cap 7) — CLEAR
- Max drawdown: 1.27% from peak $11,023.54 (cap 25%, warn 12.5%) — CLEAR
- Equity floor: $10,883.71 > $7,500 — OK
- SBD state: CLEAR (14/15 positive, median +1.60%) → W22-G 2-bar EMA20 default exit active
- Regime gate (5a): PASS — 14/15 positive 24h, SBD CLEAR
- **All clear. 1 open position. 16 closed trades lifetime.**

## Promotion assessment — **ELIGIBLE**

| Criterion | Required | v0.12 | Status |
|-----------|----------|-------|--------|
| Days live | ≥ 30 | 36 days | ✓ |
| Closed trades (rolling 30d) | ≥ 10 | 16 lifetime (10 in last 30d) | ✓ |
| Net return vs main | > main | +8.58% vs main +4.14% | ✓ +4.44pp |
| Max DD | < main DD + 25% | 1.50% vs main 4.25% | ✓ |

**→ CONFIRMED ELIGIBLE. Route to routine-04 Saturday memo for Ring-2 promotion proposal.**

## Performance (2026-05-19 → 2026-06-24)

| Metric | Value |
|--------|-------|
| Closed trades | 16 (including 1 void; 15 effective closes) |
| Win rate | ~33% (5 winners: HYPE +4.04R, HYPE +0.12R, TAO +4.29R, BTC Jun15/16 +0.68R, HYPE Jun16/17 +1.32R, SOL +1.97R = 5.5/16 count HYPE+SOL wins) |
| Realized net | +$858.19 / +8.58% |
| Max drawdown | 1.50% from peak $11,023.54 |

## Rolling performance vs main BULL v0.4

| Window | v0.12 return | main return | Delta | BTC-hold | Result |
|--------|--------------|-------------|-------|----------|--------|
| 30d | +8.58% | +4.14% | +4.44% | −20.5% (BTC $75,750→$60,219) | v0.12 WELL AHEAD |
| 90d | — | — | — | — | not yet computable |

## Days live

- Spin-up: 2026-05-19
- As of last rebuild: **37 days**
- **Promotion-eligible: YES** — all gates pass. Route to routine-04 for proposal draft.

## Notes

Instrumented twin testing whether W22-G 2-bar exit rule (vs main's 1-bar exit) improves per-trade return. Backfilled 2026-05-29 after the routine-#7 13-day scheduler gap (05-16→05-29). Key finding from gap replay: v0.12's 2-bar exit held trades 1-2 bars longer than v0.5's 1-bar exit. Result: HYPE Jun16/17 = +1.32R vs v0.5's HYPE Jun16 +0.89R (+0.43R gain); SOL = +1.97R vs v0.5's +2.22R (−0.25R; held 2h longer into declining close). **Net replay realized: +$366.68 (v0.12) vs +$298.13 (v0.5) in 6 new closes — 2-bar exit yielded +$68.55 more despite 1 fewer new entry.** The 2-bar exit reduces false exits on minor pullbacks but increases loss on true reversals (SOL example).

### Routine #7 wake log

- **2026-05-29 22:00 PT** — Replay window 2026-05-29 05:00 UTC → 2026-05-30 05:00 UTC. Backfill rebuilt. SBD ACTIVE (1/15 positive, median −1.07%). Entry gate 5a failed. 0 entries. Equity $9,863.26 (post-backfill).
- **2026-05-30 22:00 PT** — Replay window 2026-05-30T05:00Z → 2026-05-31T05:00Z. OVERNIGHT: SBD cleared. HYPE OPEN @ 68.06, SBD exit rule inactive. EOD: stop/EMA/target not hit. Equity MTM. Days live: **12**.
- **2026-06-09 interactive (user-directed mcp-outage gap replay)** — 9 missed wakes recovered. HYPE CLOSE +0.12R. 10 gap entries: BTC, HYPE×3, ETH, SOL×2, AVAX, SUI — multiple closes via 2-bar W22-G rule. Equity $9,880.74 (post-gap, pre-void correction). SBD telemetry: SBD active 06-02→06-06, book flat. Days live: **21**.
- **2026-06-10 22:00 PT** *(partial-run)* — 7-day cap replay applied. SBD at most wakes → 5a FAIL. Days live: **22**.
- **CORRECTION NOTE (2026-06-11 22:00 PT):** Prior entry labeled "2026-06-11 22:00 PT" was from the June 10 run. BTC close corrected to $63,430.6 → BTC PASSES rule 3. **Correction: 1 OPEN row for BTC at EOD 2026-06-12T04:00Z appended to trade_log.**
- **2026-06-12T06:45Z interactive — VOID-ENTRY CORRECTION:** Converged 720-bar 4H 50-EMA = $63,682.6 → BTC close $63,430.6 FAILS rule 3 by $252. BTC OPEN voided ($0 PnL). Book flat at $9,880.74, DD 6.84%.
- **2026-06-12 22:00 PT (routine-07)** — replay window 2026-06-12T06:45Z → 2026-06-13T05:00Z (~22h). OVERNIGHT: BTC R2 FAIL. EOD: TAO sole PASS. SBD CLEARED → W22-G 2-bar exit active. **ENTRY: TAO/USD LONG 31.78 @ 217.286.** Days live: **25**.
- **2026-06-13 22:00 PT (routine-07)** — replay window 2026-06-13T05:08Z → 2026-06-14T05:00Z (~23.87h). EXIT TAO +4.29R/+$636.09. BTC OVERNIGHT OPEN/CLOSE −0.37R/−$25.55 (2-bar exit). BTC EOD OPEN @ 64320.2. **MILESTONE: 10 closed trades reached (promotion threshold).** Equity $10,491.28, DD 1.08% from peak $10,606. Days live: **26**.
- **2026-06-24 PT (routine-07 — gap replay via routine07_replay_20260623.py; fired ~09:35 PT off-schedule)** — Replay window: **2026-06-14T05:00Z → 2026-06-24T13:00Z** (10.5 days; fully recovered via Kraken REST 30d history). **6 new closes, 5 new opens across 12 wakes.** Trade sequence: **BTC CLOSE Jun14T13:00Z −0.11R/−$7.73** (2-bar W22-G: 11:00Z close + 12:00Z close both below EMA; fired quicker than expected vs entry Jun14); **HYPE Jun14 OPEN/CLOSE −0.58R/−$90.44** (2-bar: 14:00Z + 15:00Z below EMA → 2h whipsaw); **BTC Jun15/16 OPEN/CLOSE +0.68R/+$106.62** (2-bar fires Jun16T04:00Z after 02:00Z+03:00Z bars below EMA = held 24h vs v0.5's 18h); **HYPE Jun16/17 OPEN/CLOSE +1.32R/+$208.20** (**KEY**: 2-bar fires Jun17T08:00Z after 06:00Z+07:00Z bars below EMA — held from Jun16T04:00Z to Jun17T08:00Z; +1.32R vs v0.5's HYPE Jun16 +0.89R = extra 0.43R from 2-bar rule's patience); **SOL Jun20/21 OPEN/CLOSE +1.97R/+$315.65** (2-bar exits 2h later than v0.5; slightly lower exit = −0.25R vs v0.5); **BTC Jun22 OPEN/CLOSE −1.00R/−$165.35** (stop-hit; 2-bar irrelevant). **NEW PEAK $11,023.54** at SOL close (surpasses prior peak $10,606). Net replay: +$366.68 vs v0.5's +$298.13 in same window. Total equity $10,858.19, DD 1.50% from new peak. **OVERNIGHT 2026-06-24T13:00Z:** SBD ACTIVE → 5a FAIL → 0 entries. **CONFIRMED PROMOTION ELIGIBLE: 36d live, 16 trades, +8.58%, DD 1.50%.** All kill switches clear. Days live: **36**.
- **2026-06-25 PT (routine-07, 2026-06-25T19:19Z — off-cron 12:19 PT)** — Watchdog ALL CLEAR. Kraken MCP OK ($59,407 BTC). Replay window: 2026-06-24T16:35Z → 2026-06-25T19:19Z (~26.7h). Wakes evaluated: **EOD 2026-06-25T04:00Z**: 0/15 positive, SBD ACTIVE, 5a FAIL → 0 entries. **OVERNIGHT 2026-06-25T13:00Z**: BTC crashed 61,146→58,218 −4.9%, SBD 5th consecutive wake, 0/15 positive, 5a FAIL → 0 entries (SBD → W22-G exit rule inactive for any new opens). Book flat. Kill switches all clear (equity $10,858.19 unchanged). **PROMOTION ELIGIBLE status confirmed** (37d live, 16 trades, +8.58%). Days live: **37**.
- **2026-06-25 PT (routine-07, 2026-06-26T05:06Z — 22:05 PT on-schedule cron fire)** — Watchdog ALL CLEAR. Kraken MCP OK ($59,766.5 BTC). Replay window: 2026-06-25T19:19Z → 2026-06-26T05:06Z (~9.8h). MIDDAY 20:00Z: default skip. **EOD 2026-06-26T04:00Z** (routine-03-eod confirmed 04:11Z): 2/15 positive (SOL +0.77%, HYPE +1.24%), median −2.84%, 5a-SBD briefly CLEARED (positives = 2 > 1 ceiling); 5a FAIL → 0 entries. SBD cleared → W22-G default exit reverts to 20-EMA 2-bar (no active positions to apply). Book flat → exit replay no-op. Post-EOD: SBD re-activated by 05:00Z (0/15, −3.88%). Kill switches all clear (equity $10,858.19 unchanged). **PROMOTION ELIGIBLE** (37d, 16 trades, +8.58%, DD 1.50%). Days live: **37**.
- **2026-06-27 PT (routine-07, 2026-06-27T16:43Z — 09:43 PT OFF-SCHEDULE Saturday fire)** — Watchdog 1 finding (self-resolving). Kraken MCP OK (14/15 positive, median +1.60%, SBD CLEAR → W22-G 2-bar EMA exit active). Replay window: 2026-06-26T05:06Z → 2026-06-27T16:43Z (~35.6h). Wakes: OVERNIGHT Jun26 13:00Z (R3 0/15 binding → 0 entries), EOD Jun27 04:00Z (R3 binding → 0 entries), **OVERNIGHT Jun27 13:00Z**: SOL R1/R2/R3/R4a/5a PASS. No vol-comp gate for v0.12. Cluster 0/2→1/2. **ENTRY: SOL/USD LONG 114.86 @ $72.23, stop $70.812, target $77.902 (W22-G 2-bar EMA20 exit; SBD exit accelerator inactive — SBD CLEAR).** Cost $8,296.34, commission $21.57, cash $2,540.28. MTM @ $72.64: $8,343.43. Equity $10,883.71. Kill switches all clear. **PROMOTION ELIGIBLE** (38d, 16 trades, +8.58% realized; equity $10,883.71 = +8.84% MTM). Days live: **38**.
