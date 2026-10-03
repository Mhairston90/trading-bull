# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md`; the log remains the source of truth.
> **Last rebuild:** 2026-10-02T17:xxZ routine-02-midday (PT 2026-10-02 10:xx Fri) — on-schedule midday. **SOL STOP-OUT intrabar at 17:00Z**; FLAT (0 positions). Pattern-of-5 cashfit stop-outs; consecutive-loss streak 6/7 (one more → 7-day full-pause).

## Account

- Starting equity: **$10,000.00**
- Cash: **$9,686.86** ($1,141.42 prior + $8,590.52 SOL close proceeds − $45.07 round-trip commission ~ reconciles via realized-PnL accounting)
- Realized PnL (since inception): **−$313.14** (−$115.51 prior + −$197.63 SOL 10-02 stop)
- Unrealized PnL: **$0.00** (no open positions)
- Current equity: **$9,686.86**
- Equity peak: **$11,068.89** (unchanged)
- Drawdown from peak: **12.49%** — essentially at 12.5% warn threshold (0.01pp shy)
- Since-inception return: **−3.13%**

## Open positions

*(none)*

Portfolio risk-at-moment: **0.00%** of equity.
Open positions: **0 / 8** (strategy cap 0/4; BTC-cluster 0/2).

## Day summary — PT 2026-10-02 Fri trading day

- **Day PnL (realized)**: **−$197.63 / −1.99%** of PT-midnight equity (SOL stop at 17:00Z / 10:00 PT).
- **Day PnL (vs EOD 10-01 baseline $9,880.14)**: **−$193.28 / −1.96%** (ΔMTM = SOL unrealized −$4.37 at EOD → realized −$197.63 now).
- **Trades opened today**: **0** (SOL opened at 04:00Z = PT 2026-10-01 21:00 Thu, logged to PT 10-01 calendar day).
- **Trades closed today**: **1** (SOL/USD 17:00Z intrabar stop).
- **Win rate today (closed only)**: **0/1** (0%).

## SOL exit mechanics — 2026-10-02T17:00:00Z (PT 2026-10-02 10:00 Fri)

- **Trigger**: 2×ATR stop pierced intrabar. 17:00Z 1H bar low = $119.19 < stop $119.1944 by $0.0044.
- **Price trajectory post-entry**:
  - 04:00Z entry bar: close $123.45 (high $123.62) — strongest post-entry move
  - 05:00Z→13:00Z: holds $121.6–$122.5 range (9 bars sideways)
  - 14:00Z: close $120.58, low $120.06 — breakdown begins
  - 15:00Z: close $119.97, low $119.65
  - 16:00Z: close $119.95, low $119.45
  - **17:00Z: close $119.66, low $119.19 → STOP PIERCED**
  - 18:00Z: close $118.11, low $117.12 — follow-through confirms rejection
- **W22-H breakeven ratchet**: NEVER ARMED. Would arm at close ≥ $125.3630. Peak close post-entry was $123.45 on entry bar itself — $1.91 shy of arm.
- **Fill**: $119.1944 × 0.9995 slippage = $119.1348.
- **Gross PnL**: ($119.1348 − $121.2506) × 72.1076 = **−$152.56**.
- **Commissions**: open $22.73 + close $22.34 = **−$45.07**.
- **Net PnL**: **−$197.63 / −1.03R**.
- **Held**: 13h (entry 04:00Z → stop 17:00Z).

## Rolling benchmark (marked at midday 2026-10-02T17:xxZ, SOL closed)

- **BTC-hold 30d**: BTC $84,560.70 vs ~$79,500 09-01 baseline → **~+6.4%** (BTC pulled back from EOD $85,480 → $84,560 = −1.1% today).
- **BTC-hold 7d**: ~+9.8%.
- **BULL 30d** (equity $9,686.86 vs ~$10,440 09-01 baseline): **~−7.22%**.
- **BULL 7d**: **~−7.68%**.
- **BULL vs BTC-hold 30d**: **~−13.6pp behind** (widened from EOD −12.9pp by SOL stop + BTC pullback net).
- **BULL vs BTC-hold 7d**: **~−17.5pp behind**.
- **90d benchmark**: not-yet-computable (post-outage cross-window).

## Entry context — this wake

- **Routine 02 midday is position management only.** No entries evaluated per routine spec. Entry responsibility belongs to #1 Overnight and #3 EOD.

## Active kill-switch state (routine-02-midday 2026-10-02T17:xxZ / PT 2026-10-02 10:xx Fri)

- **Daily loss cap (PT 10-02 trading day)**: **−1.99% realized** (SOL stop $-197.63 vs PT-midnight equity ~$9909.91). **CLEAR** (<5% cap; 3.01pp headroom).
- **Consecutive-loss cap**: **6 losses** (NEAR 09-23, ADA 09-26, SOL 09-27 scratch, SOL 09-30, ADA 10-01, SOL 10-02). Streak = **6 of 7**. **CLEAR but 1-loss headroom to 7-day full-pause**. Next loss trips Ring 3; requires user `RESUME`.
- **Max drawdown**: **12.49%** from peak $11,068.89 (SOL stop added $197.63 → DD +1.75pp). **CLEAR vs 25% cap but at 12.5% warn threshold** (0.01pp shy). Telegram warn notification sent.
- **Equity floor: $9,686.86 > $7,500** (+$2,186.86). **CLEAR** (2186pp headroom).
- **Exposure: 0.00% / 4%** used. **CLEAR** (flat, no open positions).
- **Cluster cap: 0/2 BTC-cluster**. **CLEAR**.
- **Universe/liquidity**: n/a (no positions).
- **5b cooldown state**: SOL now blocked until **2026-10-03T17:00Z** (24h from stop; freshest cooldown). ADA cleared (10-01T08Z + 24h = 10-02T08Z elapsed). NEAR expired. 12 other pairs CLEAR.
- **Regime 5a (ambient check this wake)**: 9/15 positive 24h (ADA +0.72, AVAX +0.53, ETH +0.25, LINK +0.80, SOL +0.36, SUI +0.22, BTC +0.07, DOGE +0.04, XRP +0.09), 6/15 negative (DOT, FARTCOIN, NEAR, PENGU, TAO, TRX). Median +0.07%. **PASS, SBD CLEAR**.
- **MCP availability**: Kraken multi-ticker + OHLCV healthy; Telegram script healthy; ue-scripts and yt-analysis MCP failed (not needed for BULL ops).
- **All Ring 3 kill switches CLEAR** (but 2 near warn: DD at 12.49% / 12.5% warn, consecutive-loss 6/7).

## Ops notes

- **Pattern-of-5 rule8-cashfit stop-out**: 06-17 SOL fallback, 07-10 BTC +0.23R, 09-30 SOL −1.00R, 10-01 ADA −1.02R, 10-02 SOL −1.03R → **cumulative ≈ −$689** across 5 cashfit instances. Last 3 (09-30, 10-01, 10-02) stopped consecutively. **The 10-02 SOL entry itself was a repeat of the exact 09-30 SOL archetype** (same pair, same tag, 48h apart, both stopped out) — pattern-of-5 realized in <72h.
- **P-W27-CASHFIT** and **P-W25R-SAMESESSION-STOP-GATE** still pending user `[Y/N]` at Sat 10-03 routine-04-harness W25R memo. Evidence pile grew by one more loss this wake.
- **W22-H breakeven ratchet unarmed in 2 consecutive post-W22 SOL trades** (09-30, 10-02) — both never reached +2R before stopping. The W22-H rule is strictly risk-reducing; this pattern suggests it won't fire often in current regime but doesn't harm.
- **Drawdown trajectory**: 10.74% (prior wake) → **12.49%** (this wake, +1.75pp). One more full-R stop pushes DD to ~13.9% (into warn zone). Two more → ~15.3%.
- **Consecutive-loss trajectory**: 5/7 → **6/7**. **One more loss trips 7-day full-pause.** User `RESUME` required to continue trading on 7th consecutive loss.
- **Watchdog findings (8, unchanged)**: routine-06/07 heartbeat dead (A×2), dirty-tree 4 untracked files (C), stale-MTM 5 variant portfolios (D). Known-structural, Telegram-alerted every wake.
- **Monthly archive**: 25 live rows (added SOL CLOSE this wake). Next full archive sweep at month-end 2026-10-30/31.

## Notes for next wake

- **Routine 03 EOD** fires at ~04:00Z 10-03 / 21:00 PT 10-02 Fri. Will MTM FLAT state (no open positions), run full universe entry scan (routine-03 is entry-authorized), and mark day summary.
- **5b cooldowns**: SOL blocked until 10-03T17:00Z (fresh 24h). ADA blocked until 10-02T08Z (already cleared). Other 13 pairs CLEAR.
- **Consecutive-loss sensitivity**: streak at 6/7 means routine-03 EOD entry scan should **flag** that one more loss trips Ring 3. The strategy itself has no explicit "streak gate" — entries proceed by strategy v0.4 compliance. However, this is a user-visibility point.
- **SBD/regime monitoring**: regime stable at 9/15 +0.07% this wake. Volatility of last 2 days (double whiplash day) has quieted — but 2-day sample is thin.
- **W25R memo prep (Sat 10-03 routine-04-harness)**: SOL 10-02 is new evidence for P-W25R-SAMESESSION-STOP-GATE and P-W27-CASHFIT. Memo author should include this trade's bar-by-bar trajectory (13h hold, 3-bar step-down 14→17Z) as detailed case study.
- **No open positions** = no stop management obligations overnight. Routine 03 EOD runs clean entry scan.
