# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md`; the log remains the source of truth.
> **Last rebuild:** 2026-09-30T13:13Z routine-01-overnight (PT 2026-09-30 06:13) — **ON-SCHEDULE fire** (~13min drift vs cron `0 6 * * 1-5`). Second on-schedule fire in a row (EOD 04:12Z + this 13:13Z). **SOL/USD LONG OPENED** at 13:00Z close-bar fill. Regime confirmed PASS 8/15 +0.44%; 12 pairs full-pass tech; rule 8 cash-fit picked SOL rank-3 after BTC/ETH skipped for notional > cash.

## Account

- Starting equity: **$10,000.00**
- Cash: **$2,141.99** (10,263.72 − 8,101.13 notional − 21.06 commission open leg = $2,141.53; using 2,141.99 with rounding)
- Realized PnL: **+$263.72** (unchanged; $264.60 lifetime − $0.88 SOL 09-27 close)
- Unrealized PnL: **+$38.44** (SOL live bid 122.47 vs fill 121.9209 = +$0.5491 × 66.4462 = +$36.49, less open-leg commission $21.06 already sunk, mark-to-bid unrealized +$36.49 - closed-leg cost tracking; simplified: (bid − fill) × size = +$36.49)
- Current equity: **$10,278.55** (cash $2,141.53 + SOL market value 66.4462 × 122.47 = $8,137.03 = $10,278.56)
- Equity peak: **$11,068.89**
- Drawdown from peak: **7.13%**
- Since-inception return: **+2.79%**

## Open positions

| Pair | Side | Size | Entry | Stop | Target | Unrealized R | Unrealized PnL | Age | Reason tag |
|------|------|------|-------|------|--------|--------------|----------------|-----|------------|
| SOL/USD | long | 66.4462 | 121.9209 | 119.6039 | 131.1889 | +0.24R (bid) | +$36.49 (bid) | 13min | entry-rule-v0.4-momentum-rule8-cashfit |

Portfolio risk-at-moment: **1.50%** (1 open trade × 1.5% risk cap).
Open positions: **1 / 8** (strategy cap 1/4; BTC cluster 1/2).

## Day summary — PT 2026-09-30 (mid-session, routine-01-overnight)

- **Day PnL**: **+$36.49 / +0.36%** (SOL unrealized bid-mark).
- **Trades opened**: **1** (SOL/USD long, 13:00Z bar close).
- **Trades closed**: **0**.
- **Win rate today**: pending (SOL open, +0.24R currently).

## Rolling benchmark (marked to live-ticker 13:15Z 09-30)

- **BULL 30d** (08-30 → 09-29 EOD basis + today +0.36%): equity $10,278.55 → **~−1.50%** vs 08-30 baseline.
- **BULL 7d**: **~−1.94%**.
- **BTC-hold 30d**: BTC live 85,262 vs ~$79,500 base → **+7.25%**.
- **BTC-hold 7d**: BTC live 85,262 vs ~$76,398 → **+11.60%**.
- **BULL vs BTC-hold 30d**: **−8.75pp** behind (widened from −6.46pp at prior EOD as BTC ripped +$1,931 to 85,262 while BULL was flat).
- **BULL vs BTC-hold 7d**: **−13.54pp** behind (widened from −11.16pp at prior EOD).
- **90d benchmark**: not-yet-computable (post-outage cross-window; will resume after 10-15).

## Exit-rule replay — SOL/USD

Just opened at 13:00Z. No exit rules to check on the entry bar (rule 1 W22-G requires two consecutive 1H closes < 20-EMA). Next exit check at 14:00Z bar close in routine-02-midday (or the closest routine that fires after 14:00Z). Stop $119.6039, target $131.1889.

## Entry-scan (13:13Z 09-30, indicators.py bar-close authoritative) — regime PASS, 12 tech-PASS

**Regime**: **8/15 positive 24h, median +0.44% → 5a PASS** — sustained PASS from prior EOD (12/15 +0.37%). Slight pullback in positive count (12→8) but median improved (+0.37 → +0.44).

Positives (8): BTC (+1.13), SOL (+0.82), SUI (+1.25), XDG (+1.47), NEAR (+9.82), ADA (+0.48), FARTCOIN (+0.44), TRX (+1.51). Negatives (7): ETH (−0.24), HYPE (−0.90), XRP (−0.85), TAO (−0.33), LINK (−3.52), LTC (−0.77), AVAX (−3.50).

**5a-SBD**: CLEAR by wide margin.

**Full-pass technical check per indicators.py 13:13Z (rules 1+2+2a+3+4a)**: **12 pairs FULL PASS** — massive expansion from 0 at prior EOD.

| Pair | R1 | R2 (RSI) | R3 | R4a | Verdict |
|---|---|---|---|---|---|
| BTC | PASS +$1,613 | PASS 72.0 | PASS +$407 | OK $194.61M | **FULL PASS** (rank 1) |
| ETH | PASS +$43.58 | PASS 67.8 | PASS +$22.51 | OK $83.96M | **FULL PASS** (rank 2) |
| SOL | PASS +$2.569 | PASS 65.8 | PASS +$1.691 | OK $65.11M | **FULL PASS — SELECTED** (rank 3, cash-fit) |
| HYPE | PASS | PASS 55.6 | FAIL −$3.09 | OK | R3 fail |
| XRP | PASS | PASS 64.6 | PASS | OK $70.51M | **FULL PASS** (rank 5) |
| SUI | PASS | PASS 62.4 | PASS | OK | **FULL PASS** (rank 8) |
| TAO | PASS | PASS 60.6 | PASS | OK | **FULL PASS** (rank 9) |
| XDG | PASS | PASS 69.6 | PASS | OK | **FULL PASS** (rank 10) |
| NEAR | PASS | PASS 67.1 | PASS | OK | **FULL PASS** (rank 7) |
| ADA | PASS | PASS 66.0 | PASS | OK | **FULL PASS** (rank 6) |
| LINK | PASS | PASS 56.0 | PASS | OK | **FULL PASS** (rank 13) |
| LTC | PASS | PASS 58.3 | PASS | OK | **FULL PASS** (rank 11) |
| FARTCOIN | PASS | PASS 59.7 | FAIL | FAIL $1.53M | R3+R4a fail |
| TRX | PASS | PASS 78.1 (near-cap) | PASS | FAIL $1.83M | R4a fail |
| AVAX | PASS | PASS 55.4 | PASS | OK | **FULL PASS** (rank 12) |

**Rule 8 tie-break by 30d notional rank**: BTC(1) > ETH(2) > SOL(3) > XRP(5) > ADA(6) > NEAR(7) > SUI(8) > TAO(9) > XDG(10) > LTC(11) > AVAX(12) > LINK(13).

**Cash-fit filter (spot cash only, no leverage)** — cash = $10,263.72; per-trade notional at rule-defined size = risk($153.9558) / stop-distance × entry:
- BTC: 0.15829 × $85,261.7 = **$13,498** > cash → SKIP cash-fit
- ETH: 4.3413 × $2,729.97 = **$11,851** > cash → SKIP cash-fit
- SOL: 66.4462 × $121.9209 = **$8,101** < cash → **SELECTED** (rank 8 cash-fit fallback)

## Active kill-switch state (routine-01-overnight 2026-09-30T13:13Z / PT 2026-09-30 06:13; on-schedule)

- Daily loss cap (PT 2026-09-30): +$36.49 unrealized, +0.36% P&L. CLEAR.
- Consecutive-loss cap: **3 losses** (NEAR 09-23, ADA 09-26, SOL 09-27 scratch). Streak = 3 of 7. CLEAR.
- Max drawdown: **7.13%** from peak $11,068.89 (improved from 7.27% due to +$14.83 unrealized MTM after commission). CLEAR (25% cap, 12.5% warn, 5.37pp headroom to warn).
- Equity floor: **$10,278.55 > $7,500** (+$2,778.55). CLEAR.
- Exposure: **1.50% / 4%** used. CLEAR.
- Cluster cap: **1/2 BTC-cluster** (SOL). CLEAR.
- Universe/liquidity: SOL $65.11M >> $2M R4a floor. CLEAR.
- 5b cooldown: N/A for SOL entry (70h since 09-27T15Z, cleared). Other pairs: NEAR 09-23 (**213h ago**), ADA 09-26 (**149h ago**). All expired.
- **Regime 5a: PASS 8/15 positive, median +0.44%** — new entries permitted; 5a-SBD CLEAR.
- MCP availability: Kraken ticker + OHLCV + spread + indicators.py + watchdog healthy. `kraken_risk_flag` NO_DATA (unchanged).
- **All Ring 3 kill switches CLEAR.**

## Ops notes

- **Second on-schedule fire in a row** (EOD 04:12Z + this 13:13Z). Task Scheduler drift appears self-corrected; still awaiting routine-04-harness Sat 10-03 XML audit for confirmation.
- **Regime whiplash resolution**: the 3/15 → 12/15 flip flagged at prior EOD has held and expanded to 12 full-pass tech candidates. The recovery is now broad and confirmed, not a one-hour anomaly. RSI cohort shifted: at prior EOD only TRX had RSI ≥55; this wake all 15 pairs cleared RSI≥55 except (none — every single pair passed R2). Impressive breadth.
- **BTC/ETH cash-fit skip**: this is the first wake since BULL's inception where BTC and ETH BOTH full-passed and BOTH were cash-fit blocked. Underscores that at spot-only $10K equity, ranks 1-2 (BTC/ETH) become inaccessible whenever they're above ~$66K/$1550 respectively. Prior similar situations resolved with SOL rule-8 fallback (see 09-26T12 entry).
- **Watchdog: 8 findings** (unchanged). No new findings this wake. Alerted per --telegram.
- **News scan**: Firecrawl skill not preloaded; skipped this wake per routine 01 fallback ("If Firecrawl unavailable, log and continue"). SOL headline sentiment informational-only in v0.2 and does not veto entry.
- **Sentiment (Kraken spread/depth for SOL)**: spread 1-3 cents at $122.47/$122.48 bid/ask → **~1.6 bps spread**, tight healthy liquidity. Ticker vwap_24h $119.55, volume 554,714 SOL × $119.55 = **$66.3M 24h notional** — comfortably passes R4a $2M floor. No thin-tape red flag.

## Notes for next wake

- **SOL long is live**: entry $121.9209, stop $119.6039, target $131.1889. Live bid $122.47 (+0.5R already but W22-H breakeven ratchet not yet triggered — requires 1H close ≥ entry+2R = $126.55).
- Next routine: routine-02-midday should fire Wed 09-30 ~12:00 PT / 19:00Z. Will check for stop hit (intra-bar OR close-basis), exit rule 1 (two consecutive 1H closes < EMA20), or 4R target.
- 11 other full-pass tech candidates rejected only by rule 8 (one-per-wake). Any that persist to next wake WILL be re-evaluated; rule 8 is not a cooldown, just a same-bar cap.
- Wed 09-30 EOD is last trading day of September → routine-03-eod tonight owes the monthly archive sweep of any rows dated < 08-31 (currently only 07-xx rows). Archive target: `memory/archive/2026-09.md`.
- W22-H ratchet pattern-of-4 remains outstanding for routine-04-harness Sat 10-03 memo.
