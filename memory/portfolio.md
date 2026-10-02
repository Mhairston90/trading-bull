# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md`; the log remains the source of truth.
> **Last rebuild:** 2026-10-02T04:12Z routine-03-eod (PT 2026-10-01 21:12) — on-schedule Thu EOD fire. **1 OPEN: SOL/USD long rule-8-cashfit rank-3 after BTC/ETH cash-blocked.** Regime recovered from 1/15 SBD-ACTIVE overnight → 8/15 +0.08% PASS at EOD close (+7 breadth whiplash within same calendar day).

## Account

- Starting equity: **$10,000.00**
- Cash: **$1,141.42** ($9,884.51 prior − $8,743.09 SOL fill cost)
- Realized PnL (since inception): **−$115.51** (unchanged — ADA stop already captured)
- Unrealized PnL: **−$4.37** (SOL slippage drag at fill: 72.1076 × ($121.19 − $121.2506))
- Current equity: **$9,880.14** (cash + position MTM at 04:12Z live-ticker $120.68 would be $9,841 — using 04:00Z close for consistency with entry bar)
- Equity peak: **$11,068.89** (unchanged)
- Drawdown from peak: **10.74%** (slight widening from 10.70% pre-entry from slippage drag)
- Since-inception return: **−1.20%**

## Open positions

| Pair | Side | Size | Entry fill | Stop (2×ATR) | Target (4R) | Current MTM | Unrealized $ | Unrealized R |
|------|------|------|-----------|--------------|-------------|-------------|--------------|--------------|
| SOL/USD | long | 72.1076 | $121.2506 | $119.1944 | $129.4754 | $121.19 (04:00Z close) | −$4.37 | −0.03R |

Portfolio risk-at-moment: **1.50%** of equity (1 position × 1.5% risk per trade).
Open positions: **1 / 8** (strategy cap 1/4; BTC-cluster 1/2).

## Day summary — PT 2026-10-01 Thu trading day

- **Day PnL (realized)**: **−$183.55 / −1.82%** (ADA stop-out 08:00Z = 01:00 PT).
- **Day PnL (realized + unrealized)**: ~**−$187.92 / −1.87%** including SOL slippage drag.
- **Trades opened today**: **2** (ADA 07:00Z PT 00:00; SOL 04:00Z 10-02 = PT 21:00 Thu — both on PT 10-01 calendar day).
- **Trades closed today**: **1** (ADA/USD 08:00Z intrabar stop).
- **Win rate today (closed only)**: **0/1** (0%).

## Rolling benchmark (marked to EOD closed-bar 2026-10-02T04:00:00Z)

- **BTC-hold 30d**: BTC closed-bar $85,480.6 vs ~$79,500 09-01 baseline → **~+7.5%** (expanded from morning's +5.1% on BTC's day rally +2.3%).
- **BTC-hold 7d**: ~+10.9% (continuing to expand).
- **BULL 30d** (equity $9,880.14 vs ~$10,440 09-01 baseline): **~−5.36%**.
- **BULL 7d**: **~−5.76%**.
- **BULL vs BTC-hold 30d**: **~−12.9pp behind** (widened from morning −10.4pp — BTC rallied through the day; BULL day net was small realized loss + near-flat SOL entry).
- **BULL vs BTC-hold 7d**: **~−16.7pp behind**.
- **90d benchmark**: not-yet-computable (post-outage cross-window).

## New SOL entry mechanics — 2026-10-02T04:00:00Z (PT 2026-10-01 21:00 Thu close)

- **Pre-entry rank evaluation**: BTC rank-1 (notional $15,196 > $9,884 cash → SKIP cash-fit); ETH rank-2 ($12,374 > $9,884 → SKIP); SOL rank-3 ($8,743 < $9,884 → SELECTED).
- **Full-pass technical check per indicators.py 04:12Z** (720×1H + converged 4H): R1 +$2.48 (close $121.19 > EMA20 $118.71), R2 RSI 69.5 (>55), R2a OK (<80), R3 +$3.20 (4H close > 4H EMA50 $117.99), R4a $38.56M notional (>$2M floor, 19× cushion).
- **Regime 5a**: 8/15 positive 24h, median +0.08% → PASS, SBD CLEAR. **Recovery from this morning overnight 1/15 −2.74% SBD-ACTIVE** (+7 breadth whiplash in 15h; companion to morning overnight 14/15 → 1/15 −13 flip).
- **Cluster**: SOL in BTC-cluster {BTC, ETH, SOL, TAO, AVAX, SUI, LINK}. 0 → 1/2 ✓.
- **5b cooldown**: SOL last stop-out 2026-09-30T14:00Z. Elapsed 38h > 24h → CLEAR.
- **pre_entry_check**: all 8 checks ACCEPT (positions 0<8, cap 0<4, risk 0.00+1.50=1.50<4.00, per-trade 1.50≤1.50, in universe, not open, day loss 1.82<5.0, equity $9,884.51 > $7,500).
- **Fill**: $121.19 × 1.0005 slippage = $121.2506.
- **Stop (2×ATR)**: $121.2506 − $2.0562 = $119.1944 (ATR14 = $1.0281).
- **Target (4R)**: $121.2506 + $8.2248 = $129.4754.
- **Size**: $148.27 risk / $2.0562 risk-per-share = **72.1076 SOL**.
- **Notional**: $8,743.09 (fits cash $9,884.51 with $1,141.42 buffer).
- **Tag**: `rule8-cashfit`. **4th cashfit instance** (06-17 SOL fallback, 07-10 BTC, 09-30 SOL, 10-01 ADA, now 10-01 SOL).

## Entry context — elevated risk flags

- **Consecutive-loss streak = 5 of 7** (two more losing closes = 7-day full-pause kill switch requires user `RESUME`).
- **Drawdown 10.74%**, 1.76pp headroom to 12.5% warn, 14.26pp to 25% full-pause.
- **Two intraday regime whiplashes same day**: 14/15 +1.30% (overnight entry wake) → 1/15 −2.74% (overnight stop wake, 6h) → 8/15 +0.08% (this EOD wake, 15h). The W-20-type velocity rule would catch this entry (|ΔPositive| = +7 ≥ 6).
- **Second SOL entry in 48h** (prior SOL 09-30T13Z stopped 1h later for −1.00R; 5b expired at 09-30T14Z + 24h = 10-01T14Z, now 10-02T04Z = 14h past clear).
- **Pattern-of-4 cashfit becoming pattern-of-5** with this entry pending outcome.
- **P-W25R-SAMESESSION-STOP-GATE** (option b + option d) and **P-W27-CASHFIT** both still pending user `[Y/N]` at Sat 10-03 routine-04-harness W25R memo.
- Entry taken strictly per strategy v0.4 compliance. BULL does not autonomously edit strategy; proposed gates require Ring-2 approval.

## Active kill-switch state (routine-03-eod 2026-10-02T04:12Z / PT 2026-10-01 21:12)

- **Daily loss cap (PT 10-01 trading day)**: **−1.87% realized+unrealized** (ADA $-183.55 + SOL slippage $-4.37). **CLEAR** (<5% cap; 3.13pp headroom).
- **Consecutive-loss cap**: **5 losses** (NEAR 09-23, ADA 09-26, SOL 09-27 scratch, SOL 09-30, ADA 10-01). Streak = **5 of 7**. **CLEAR** (2-loss headroom to 7-day full-pause).
- **Max drawdown: 10.74%** from peak $11,068.89 (ADA stop + SOL slippage). **CLEAR** (25% cap; 1.76pp headroom to 12.5% warn — tightening).
- **Equity floor: $9,880.14 > $7,500** (+$2,380.14). **CLEAR**.
- **Exposure: 1.50% / 4%** used. CLEAR.
- **Cluster cap: 1/2 BTC-cluster**. CLEAR (1 slot remaining).
- **Universe/liquidity**: SOL rank-3 in universe, $38.56M 24h notional far above R4a floor.
- **5b cooldown state**: ADA blocked until **2026-10-02T08:00Z** (~4h). SOL now OPEN (not blocked). NEAR expired. 11 other pairs CLEAR.
- **Regime 5a**: **PASS 8/15 +0.08% median → SBD CLEAR** (recovered from this morning's SBD-ACTIVE).
- **MCP availability**: Kraken ticker + OHLCV + indicators.py healthy; Telegram script healthy; watchdog healthy.
- **All Ring 3 kill switches CLEAR.**

## Ops notes

- **Regime double-whiplash day**: 14/15 → 1/15 → 8/15 in a single PT calendar day is unprecedented in BULL's 20-week history. Overnight was −13 breadth collapse; EOD is +7 breadth recovery. Net day: 14/15 → 8/15 = −6 breadth. Rapid-flip regimes are now the dominant tape behavior over the last ~2 weeks.
- **SOL entry archetype parallel to 09-30**: same pair, same rule-8-cashfit tag, 48h apart. The 09-30 entry stopped 1h later. The 10-01 lesson explicitly identifies this archetype (same-session-stop-after-regime-crystallization) as pattern-of-4. If this SOL entry survives the overnight 05:00-13:00Z window without stop-out, it will be the first same-day-cashfit SOL to break the pattern. If it stops out before the next midday wake, it would form pattern-of-5 within the exact same calendar day as the pattern-of-4 escalation.
- **Rule-8-cashfit cumulative P&L**: 06-17 SOL −$158, 07-10 BTC +$46, 09-30 SOL −$196, 10-01 ADA −$184 = **−$492 cumulative** over 4 cashfit entries. SOL 10-01 is 5th. Pending P-W27-CASHFIT would address the pattern.
- **Drawdown trajectory**: 10.74% today, +0.04pp from this morning (SOL slippage only; ADA stop already in). One more full-R stop would push DD to ~12.1% (0.4pp from 12.5% warn). Two more = ~13.4% (into warn).
- **Watchdog findings (8, unchanged)**: routine-06/07 heartbeat dead (A×2), dirty-tree 4 untracked files (C), stale-MTM 5 variant portfolios (D). Known-structural, Telegram-alerted every wake.
- **Monthly archive**: 23 live rows this morning + 1 OPEN this wake = **24 rows** in trade_log.md. Comfortable size; next full archive sweep at month-end 2026-10-30/31.

## Notes for next wake

- **Routine 01 overnight** fires next ~13:00Z 10-02 Fri = 06:00 PT. SOL position to MTM against 12:00Z just-closed bar (8 bars after entry).
- **5b cooldowns**: ADA blocked until 10-02T08:00Z (4h away). SOL now OPEN (not blocked). Other 13 pairs CLEAR.
- **Consecutive-loss streak**: 5/7. Still 2 away from 7-day full-pause. SOL exit outcome will update the count (+1 loss → 6/7, scratch → 5/7, +1R or better → resets per guardrails).
- **SBD/regime monitoring**: regime recovered to 8/15 but may whipsaw again overnight given the day's double-flip. Next wake re-evaluates.
- **Open position stop management**: SOL stop at $119.1944 is the active stop (2×ATR). W22-H breakeven ratchet arms at close ≥ +2R unrealized ($121.2506 + 2 × $2.0562 = $125.3630). Not yet armed.
- **Lesson update candidate**: if SOL survives overnight, update the 10-01 pattern lesson's "cumulative cashfit P&L" line and note the first same-archetype positive-outcome. If SOL stops out, the 10-01 lesson becomes pattern-of-5 with the fastest cadence on record (two instances same calendar day).
