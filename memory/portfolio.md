# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md`; the log remains the source of truth.
> **Last rebuild:** 2026-09-27T13:15Z routine-01-overnight (PT 2026-09-27 06:15) — SOL/USD marked to just-closed 1H bar (12:00Z 09-27 close $123.33); no exits triggered (rule 1 not armed: 11:00Z close 123.89 and 12:00Z close 123.33 both ABOVE EMA20 122.298; static stop $119.0198 not pierced overnight low 120.09; ratchet not armed peak close 09:00Z 124.44 = +1.64R < +2.0R).

## Account

- Starting equity: **$10,000.00**
- Cash: **$1,173.45** ($10,264.60 − $9,091.15 SOL position cost)
- Realized PnL: **+$264.60** ($309.52 − $44.92 ADA)
- Unrealized PnL: **+$169.70** (SOL: 75.09 × ($123.33 − $121.07) = +$169.70)
- Current equity: **$10,434.30**
- Equity peak: **$11,068.89**
- Drawdown from peak: **5.73%**
- Since-inception return: **+4.34%**

## Open positions

| Pair | Side | Size | Entry | Stop | Target | Cost | Unrealized R | Notes |
|------|------|-----:|------:|-----:|-------:|-----:|-------------:|-------|
| SOL/USD | long | 75.09 | 121.07 | 119.0198 | 129.2708 | $9,091.15 | +1.10R | Age 25h; 2×ATR stop 2.0502; risk $153.95 = 1.475% equity; MTM $123.33 (12:00Z 09-27); live $122.91; BTC-cluster 1/2; W22-H ratchet dormant (peak close +1.64R this wake, needs +2.0R to arm) |

Portfolio risk-at-moment: **1.475%** (SOL $153.95 / $10,434.30).
Open positions: **1 / 8** (strategy cap 1/4; BTC cluster 1/2 — SOL in cluster).

## Day summary — PT 2026-09-27 (fresh day, in progress)

- **Day PnL**: **+$205.74 / +2.01%** unrealized MTM improvement (SOL EOD close $120.59 → 12:00Z 09-27 close $123.33; no realized trades this day).
- **Trades opened**: **0**.
- **Trades closed**: **0**.
- **Win rate today**: **N/A** (no closed trades).
- **Time-in-trade (SOL, ongoing)**: **25h** (12:00Z 09-26 → 13:15Z 09-27).

## Rolling benchmark (marked to 12:00Z 09-27 SOL close $123.33)

- **BULL 30d** (08-27 → 09-27 wake): **-0.47%** (BULL equity $10,434.30 vs ~$10,483 baseline; -1.86pp vs EOD from SOL rally).
- **BULL 7d** (09-19 → 09-27 wake): **-0.47%** (same window post-outage).
- **BTC-hold 30d** (~$79,500 → live $84,662): **+6.49%**.
- **BTC-hold 7d** (~$76,398 → live $84,662): **+10.82%**.
- **BULL vs BTC-hold 30d**: **-6.96pp behind** BTC (-8.64pp at EOD; +1.68pp closer via SOL rally).
- **BULL vs BTC-hold 7d**: **-11.29pp behind** BTC.
- **90d benchmark**: not-yet-computable (post-outage cross-window 74d gap; will resume after 10-15).

## Overnight exit-rule evaluation — SOL/USD

**Rule 1 (W22-G, two-bar 20-EMA break)**: NOT ARMED.
- 1H EMA20 (via indicators.py 13:12Z SMA-seeded + Wilder rolled) = **122.298** at 12:00Z close.
- 11:00Z close 123.89 vs EMA20 → ABOVE (+$1.59)
- 12:00Z close 123.33 vs EMA20 → ABOVE (+$1.03)
- Neither of last 2 closes below EMA20 → rule not armed.

**Rule 1-SBD (9-EMA)**: NOT APPLICABLE. Regime 11/15 positive, median +0.84% → not SBD.

**Rule 2 (static 2×ATR stop 119.0198)**: NOT HIT.
- Overnight 12-bar low $120.09 (04:00Z 09-27); 24h low $120.05 per ticker.
- +$1.03 headroom above stop.

**Rule 3 (4R target 129.2708)**: NOT HIT.
- Overnight 12-bar high $124.91 (08:00Z 09-27); current $122.91.
- -$6.36 to target from live.

**W22-H breakeven ratchet**: NOT YET ARMED.
- Peak 1H close of trade so far = 09:00Z 09-27 $124.44 → R = (124.44 − 121.07) / 2.0502 = **+1.64R**.
- Ratchet arms at first 1H close with R ≥ +2.0 (needs close ≥ $125.17). Peak fell $0.73 short.
- Stop remains at initial 2×ATR $119.0198.

**Verdict**: HOLD SOL. No trade_log write.

## Overnight entry scan — 6 full-pass candidates, all cash-blocked (2nd consecutive CASHFIT wake)

**Regime**: 11/15 positive, median +0.84% → 5a PASS (recovered from EOD 8/15 +0.13%; +3 positive count, +0.71pp median in ~9h).

**Full-pass (rules 1+2+2a+3+4/4a/5/5a/5b/6/6a/7)** ordered by universe rank:
- **BTC/USD** rank 1 — R1 +$256.4, R2 RSI 63.0, R3 +$1,522 (4H EMA50 83,353.6). 2×ATR $453.92, size 0.34479, cost **$29,229**. → **CASH-FAIL** ($29k vs $1.17k available)
- **ETH/USD** rank 2 — R1 +$5.37, R2 RSI 56.7 thin, R3 +$43.63. 2×ATR $19.71, size 7.9407, cost **$21,494**. → **CASH-FAIL**
- **NEAR/USD** rank 7 — R1 +$0.050, R2 RSI 56.4 thin, R3 +$0.794. 2×ATR $0.23857, size 656.05, cost **$3,402**. → **CASH-FAIL**
- **SUI/USD** rank 8 — R1 +$0.049, R2 RSI 70.2 hot, R3 +$0.220. 2×ATR $0.04442, size 3523.5, cost **$4,431**. → **CASH-FAIL**
- **TAO/USD** rank 9 — R1 +$6.47, R2 RSI 60.1, R3 +$34.15. 2×ATR $11.295, size 13.856, cost **$4,608**. → **CASH-FAIL**
- **XDG/USD** rank 10 — R1 +$0.000899, R2 RSI 58.2, R3 +$0.003402. 2×ATR $0.0016023, size 97,678, cost **$9,592**. → **CASH-FAIL**

**Verdict**: no entry executed this wake. All 6 full-pass candidates require notional cost exceeding available cash $1,173.45. Reproduces the P-W27-CASHFIT archetype (score 9, active) for the 2nd consecutive wake — SOL position occupies ~88.4% of equity, leaving 11.5% cash, insufficient for a 2nd position at 1.5%-risk-per-trade sizing on ANY pair (thinnest by cost was NEAR at $3,402, 2.90× cash).

Rejects with cited failing rule (from indicators.py):
- SOL/USD — R5 (open position)
- HYPE/USD — R2 (RSI 53.0)
- XRP/USD — R2 (RSI 51.2)
- ADA/USD — R2 (RSI 53.9)
- LINK/USD — R1 (close -$0.02) + R2 (RSI 50.8)
- LTC/USD — R1 (close -$0.43) + R2 (RSI 44.2)
- AVAX/USD — R2 (RSI 52.4)
- TRX/USD — R1 + R2 (RSI 41.9) + R3 + R4a (thin $1.07M)
- ONDO/USD — NOT EVALUATED (indicators.py still lists FARTCOIN not ONDO; 3rd wake surfacing this — route to routine-04-harness for config-drift fix)

## Active kill-switch state (routine-01-overnight 2026-09-27T13:15Z / PT 2026-09-27 06:15)

- Daily loss cap (PT 2026-09-27 fresh day): **0.00% realized**, +$205.74 unrealized MTM improvement. CLEAR (5% cap).
- Consecutive-loss cap: **2 losses** (NEAR 09-23, ADA 09-26). Streak = 2 of 7. CLEAR.
- Max drawdown: **5.73%** from peak $11,068.89. CLEAR (25% cap, 12.5% warn, **6.77pp headroom to warn**; -1.86pp vs EOD).
- Equity floor: **$10,434.30 > $7,500** (+$2,934.30). CLEAR.
- Exposure: **1.475% / 4% used** (SOL position). CLEAR.
- Cluster cap: **1/2 BTC-cluster** (SOL). CLEAR.
- Universe/liquidity: SOL notional ~$35.7M > $2M floor. CLEAR.
- 5b cooldown: no active cooldowns (NEAR 09-23T14Z is 95h ago > 24h; ADA 09-26T06Z is 31h ago > 24h — but ADA also R2 fails independently).
- **Regime 5a: PASS 11/15 positive, median +0.84%** — recovered from EOD 8/15 +0.13% (+3 positive count, +0.71pp median in ~9h).
- **5a-SBD: CLEAR** both legs (11 > 1 ceiling by 10; +0.84% > -1.0% floor by +1.84pp).
- MCP availability: Kraken ticker + OHLCV + indicators.py + watchdog all healthy. CLEAR.
- **All Ring 3 kill switches CLEAR.**

## Ops notes

- **Fourth consecutive off-schedule fire this ~24h window** (Sat overnight 06:20Z, Sat midday 20:00Z, Sat EOD 04:27Z 09-27, this Sun overnight 13:15Z 09-27 despite cron `Mon-Fri` mask). Task Scheduler config drift confirmed pattern-of-4. **Routed to routine-04-harness Sat 10-03 for cron audit + Task Scheduler XML review.**
- **SOL rally overnight** — from EOD $120.59 to 07:00Z 09-27 bar high $124.33, held above $123 through 12:00Z close. Peak close +1.64R this wake — W22-H ratchet still needs +0.36R more to arm at any 1H close (needs close ≥ $125.17). Live $122.91 currently +0.90R.
- **Watchdog: 8 findings** (was 9 at EOD, F unpushed cleared by EOD push).
- **Cash-fit reproduced 2nd consecutive wake** — 6 full-pass candidates (was 5 at EOD), all still blocked. P-W27-CASHFIT archetype accruing evidence.
- Not last trading day of month (Sept 30 is next Wed) → no monthly archive this wake.
- Cash buffer $1,173.45 unchanged from EOD (no new trades).
