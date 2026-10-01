# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md`; the log remains the source of truth.
> **Last rebuild:** 2026-10-01T07:13Z routine-03-eod (PT 2026-10-01 00:13) — **delayed Wed 09-30 PT EOD fire ~3h13m past 21:00 PT cron**. Opened ADA/USD long (rule-8-cashfit rank-6, BTC/ETH too large). Book 1/8.

## Account

- Starting equity: **$10,000.00**
- Cash: **$4,264.21** (prior $10,068.04 − ADA entry cost $5,788.78 − entry commission $15.05)
- Realized PnL (since inception): **+$68.04** (unchanged this wake)
- Unrealized PnL (ADA open): **−$36.82** (22,838 × $0.252518 live bid = $5,767.01 vs cost basis $5,803.83)
- Current equity: **$10,031.22** (live-ticker MTM)
- Equity peak: **$11,068.89** (unchanged)
- Drawdown from peak: **9.37%** (widened from 9.04% midday by ADA entry's slippage + commission + modest adverse MTM)
- Since-inception return: **+0.31%**

## Open positions

| Pair | Side | Size | Entry fill | Stop (2×ATR) | Target (4R) | Current MTM | Unrealized $ | Unrealized R |
|------|------|------|-----------|--------------|-------------|-------------|--------------|--------------|
| ADA/USD | long | 22,838 | $0.253472 | $0.246859 | $0.279923 | $0.252518 | −$36.82 | −0.24R |

Portfolio risk-at-moment: **1.50%** of equity (= $0.006613 stop-dist × 22,838 size = $151.03 risk / $10,031.22 equity).
Open positions: **1 / 8** (strategy cap 1/4; BTC-cluster 0/2 — ADA not in cluster).

## Day summary — PT 2026-09-30 Wed trading day (covered by this delayed EOD)

- **Day PnL (realized)**: **−$195.68 / −1.91%** (SOL/USD stop-out, routine-02-midday 2026-09-30T20:00Z).
- **Day PnL (incl. new ADA unrealized)**: **−$232.50 / −2.28%**.
- **Trades opened**: **2** (SOL/USD 09-30T13Z, ADA/USD 10-01T07Z — the latter is the entry triggered by this delayed EOD's scan).
- **Trades closed**: **1** (SOL/USD 09-30T14Z intrabar stop).
- **Win rate today (closed only)**: **0/1** (0%).

## Rolling benchmark (marked to live-ticker 2026-10-01T07:14Z)

- **BTC-hold 30d**: BTC live ~$84,018 vs ~$79,500 09-01 baseline → **~+5.7%** (pulled back from midday's +7.25% as BTC fell $85,262 → $84,018 overnight).
- **BTC-hold 7d**: ~+10.0%.
- **BULL 30d** (equity $10,031.22 vs ~$10,440 09-01 baseline): **~−3.91%** (widened from midday's −3.55% due to ADA MTM drag).
- **BULL 7d**: **~−4.32%**.
- **BULL vs BTC-hold 30d**: **~−9.6pp behind** (widened from midday's −10.80pp — BTC gave back some but BULL also lost more, narrowing the gap).
- **BULL vs BTC-hold 7d**: **~−14.3pp behind**.
- **90d benchmark**: not-yet-computable (post-outage cross-window; cumulative from pre-outage not comparable).

## EOD entry-scan rationale — ADA/USD selected via rule-8-cashfit

**Technical** (indicators.py 07:13Z 07:00Z-bar closed): regime **14/15 positive 24h, median +1.30% → 5a PASS** (strongest regime read in weeks; SBD CLEAR by wide margin). 7 of 15 full-pass per rules 1+2+2a+3+4a: BTC, ETH, TAO, XDG, NEAR, ADA, AVAX. Fails: SOL (R2 RSI 53.0), HYPE (R3 −$0.75), XRP (R2+R3), SUI (R2), LINK (R2), LTC (R2), FARTCOIN (R2+R3+R4a), TRX (R1+R2+R4a).

**Rule-8 tie-break by 30d notional rank** (from prior wake order): BTC(1) → ETH(2) → ADA(6) → NEAR(7) → TAO(9) → XDG(10) → AVAX(12). Walking down:
- **BTC** (rank 1): size = $151.0206 / $829.34 2×ATR = 0.18211 BTC; notional 0.18211 × $84,078.4 = **$15,310 > $10,068 cash → SKIP cash-fit**.
- **ETH** (rank 2): size = $151.0206 / $30.402 = 4.9674 ETH; notional 4.9674 × $2,713.8 = **$13,481 > $10,068 → SKIP cash-fit**.
- **ADA** (rank 6, first non-cluster + fit): size = $151.0206 / $0.0066126 = 22,838 ADA; notional 22,838 × $0.253472 = **$5,788.78 < $10,068 → SELECTED**.

**News**: Firecrawl skipped this wake (ADA news informational-only in v0.2; broad-regime context +1.30% median is bullish).

**Sentiment** (Kraken ticker/spread for ADAUSD @ 07:15Z): spread 8.7bps / 0.034% — tight liquidity. 24h vol 28.5M ADA × VWAP $0.25 = **$7.12M notional** (above R4a $2M floor by 3.5×). 24h change **+2.47%**, range $0.241279 / $0.256745, current $0.252572 — ~41% up from 24h low, ~84% up through the day's range. Not at a session ceiling (prior ADA 09-26 archetype was mid-range at entry too). No sentiment red flag.

**pre_entry_check for ADA/USD**:
- open_positions=0 < 8 ✓
- open_positions=0 < strategy.max_concurrent=4 ✓
- new_trade_risk = $151.03 / $10,068 = 1.500%; portfolio 0% + 1.50% = 1.50% < 4% ✓
- new_trade_risk 1.500% ≤ 1.500% ✓
- ADA/USD in universe (rank 6) ✓
- ADA/USD not in open positions ✓
- daily_loss_pct = 1.91% (prior SOL stop) < 5% ✓
- equity $10,068 > $7,500 ✓
- 5b cooldown: last ADA stop-out 09-26T06Z, now 10-01T07Z = 121h > 24h ✓
- Cluster: 0→0/2 (ADA not in BTC-cluster) ✓
- Regime 5a: PASS 14/15 +1.30% ✓
- Rule 8: max 1 new entry this wake, ADA selected via cash-fit after BTC/ETH rejected ✓
- **ACCEPT.**

## Active kill-switch state (routine-03-eod 2026-10-01T07:13Z / PT 2026-10-01 00:13)

- **Daily loss cap (PT 09-30 trading day)**: **−1.91% realized** + ~−0.37% unrealized ADA = **−2.28% total**. **CLEAR** (<5% cap; 2.72pp headroom).
- **Consecutive-loss cap**: **4 losses** (NEAR 09-23, ADA 09-26, SOL 09-27 scratch, SOL 09-30 stop). Streak = **4 of 7**. **CLEAR** (3-loss headroom). ADA entry open, not yet closed.
- **Max drawdown: 9.37%** from peak $11,068.89 (widened from 9.04% at midday due to ADA MTM drag). **CLEAR** (25% cap, **3.13pp headroom to 12.5% warn**).
- **Equity floor: $10,031.22 > $7,500** (+$2,531.22). **CLEAR**.
- **Exposure: 1.50% / 4%** used. CLEAR.
- **Cluster cap: 0/2 BTC-cluster** (ADA not in cluster). CLEAR.
- **Universe/liquidity**: ADA $6.92M notional > $2M floor. CLEAR.
- **5b cooldown state**: SOL blocked until **2026-10-01T14:00Z** (24h from 09-30 stop-out; ~7h remaining). ADA just entered (stop-out would re-trigger). NEAR expired, other 12 pairs CLEAR.
- **Regime 5a**: PASS 14/15 +1.30% median (strongest in weeks). SBD CLEAR by wide margin.
- **MCP availability**: Kraken ticker + OHLCV + indicators.py healthy; Telegram script healthy.
- **All Ring 3 kill switches CLEAR.**

## Ops notes

- **Delayed EOD fire**: Wed 09-30 21:00 PT cron (= 04:00Z 10-01) actually fired at 07:13Z 10-01 = 00:13 PT Thu 10-01, ~3h13m late. This is the first EOD since the 09-29 one. **Labeling choice**: journal + commit labeled **2026-10-01 PT** (fire-time PT date, per date-labeling guard), with explicit flag that the Wed 09-30 PT trading-day outcome (−1.91% SOL stop) is being EOD-processed here for the first time. Guard was written for the Wed 21:00 PT UTC-rollover case; this is a late-fire crossing PT midnight — less-common edge case. Accepting the guard's literal "fire-time PT" semantics; downstream watchdog may re-flag as late (acceptable).
- **Monthly archive catch-up**: moved 29 pre-Sep rows (14 opens, 15 closes incl. 06-22 SOL correction) from `trade_log.md` to `memory/archive/2026-10.md`. The Jul/Aug/Sep archive cadence was missed due to the 07-10 → 09-20 scheduler outage. First row remaining in live log: 2026-09-23T13:00:00Z NEAR OPEN. Live log is now 23 rows (down from 51 pre-archive); comfortable size.
- **5-day activity window (09-23 → 10-01)**: 5 opens, 4 closes, 1 open position. Realized PnL window = −$172.30 NEAR + −$44.92 ADA + −$0.88 SOL + −$195.68 SOL = **−$413.78 net** over 4 closed. Win rate 0/4. All losers with varying magnitudes (−1.01R, −0.29R, −0.01R, −1.00R). This is the window the harness/weekly memo will reflect on Sat 10-03.
- **Rule-8-cashfit cadence**: this is now the 3rd rule-8-cashfit entry (prior: 07-10 BTC +0.23R-loss, 09-30 SOL −1.00R-loss, 10-01 ADA pending). Pattern-of-3 for the informal rule-8-fallback-to-cashfit behavior — P-W27-CASHFIT proposal still pending user `[Y/N]` per lesson 2026-06-17 cash-insufficiency escalation.
- **W22-H breakeven ratchet pattern-of-4**: still slated for Sat 10-03 routine-04-harness W25R memo as P-W25R-RATCHET-TIGHTEN (lesson 2026-09-27 has the 4-instance evidence table + options c/d-modified).
- **09-26 ADA archetype parallel**: 09-26 ADA entry was also rule-8-winner (not cashfit), stopped in 2 bars for −$44.92. Same tech setup (R1/R2/R3/R4a all pass, mid-range RSI), smaller stop distance (ATR 0.004014 then vs 0.003306 now = tighter now). Entry risk profile similar. Watch for same early-stop pattern on the next 2 bars.

## Notes for next wake

- **Routine 01 overnight** fires next ~13:00Z 10-01 = 06:00 PT Thu. First MTM check on ADA position; if still open and above EMA20, no action. If 08:00Z and 09:00Z closes both < 1H EMA20 → W22-G two-bar exit fires at 09:00Z close (replayed by overnight).
- **5b cooldowns**: SOL blocked until 10-01T14:00Z (overnight wake will see cooldown mostly expired or just expired).
- **Consecutive-loss streak**: 4/7. One more losing close = 5/7 (2 away from 7-day full-pause).
- **Drawdown 9.37%**: 3.13pp headroom to 12.5% warn threshold.
- **Monthly archive status**: Sep rows (09-23, 09-26, 09-27, 09-30) all stay in live log until ~Nov 1 cutoff (30-day window). Oct archive opportunity next: Fri 10-30 (last trading day of October) or whenever next EOD after month-end.
- **Open positions as of this wake**: ADA/USD long 22,838 @ $0.253472, stop $0.246859, target $0.279923.
