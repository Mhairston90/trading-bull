# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md`; the log remains the source of truth.
> **Last rebuild:** 2026-09-27T04:27Z routine-03-eod (PT 2026-09-26 21:27) — SOL/USD marked to just-closed 1H bar (03:00Z 09-27 close $120.59, which is the 21:00 PT close of PT-09-26); no exits triggered (rule 1 not armed: only 03:00Z below EMA20, 02:00Z above); static stop $119.0198 not pierced (24h low $119.84).

## Account

- Starting equity: **$10,000.00**
- Cash: **$1,173.45** ($10,264.60 − $9,091.15 SOL position cost)
- Realized PnL: **+$264.60** ($309.52 − $44.92 ADA)
- Unrealized PnL: **-$36.04** (SOL: 75.09 × ($120.59 − $121.07) = -$36.04)
- Current equity: **$10,228.56**
- Equity peak: **$11,068.89**
- Drawdown from peak: **7.59%**
- Since-inception return: **+2.29%**

## Open positions

| Pair | Side | Size | Entry | Stop | Target | Cost | Unrealized R | Notes |
|------|------|-----:|------:|-----:|-------:|-----:|-------------:|-------|
| SOL/USD | long | 75.09 | 121.07 | 119.0198 | 129.2708 | $9,091.15 | -0.23R | Age 16h; 2×ATR stop 2.0502; risk $153.95 = 1.505% equity; MTM $120.59; live $120.54; BTC-cluster 1/2 |

Portfolio risk-at-moment: **1.505%** (SOL $153.95 / $10,228.56).
Open positions: **1 / 8** (strategy cap 1/4; BTC cluster 1/2 — SOL in cluster).

## Day summary — PT 2026-09-26

- **Day PnL**: **-$80.96 / -0.79%** (ADA -$44.92 realized + SOL -$36.04 unrealized MTM from entry to 03:00Z 09-27 close).
- **Trades opened**: **1** (SOL/USD long at 12:00Z, entry-rule-v0.4-momentum-rule8-winner).
- **Trades closed**: **1** (ADA/USD long at 06:00Z, exit-ema20-2bar-recovery-missed-scheduler-replay).
- **Win rate today**: **0/1 (0.00%)** on closed trades.
- **Time-in-trade (SOL, ongoing)**: **16h** (12:00Z 09-26 → 04:00Z 09-27).

## Rolling benchmark (EOD-marked to 03:00Z 09-27)

- **BULL 30d** (08-27 → EOD PT-09-26): **-2.43%** (BULL equity $10,228.56 vs ~$10,483 baseline).
- **BULL 7d** (09-19 → EOD PT-09-26): **-2.43%** (same window post-outage).
- **BTC-hold 30d** (~$79,500 → live $84,434): **+6.21%**.
- **BTC-hold 7d** (~$76,398 → live $84,434): **+10.51%**.
- **BULL vs BTC-hold 30d**: **-8.64pp behind** BTC.
- **BULL vs BTC-hold 7d**: **-12.94pp behind** BTC.
- **90d benchmark**: not-yet-computable (post-outage cross-window 74d gap; will resume after 10-15).

## EOD exit-rule evaluation — SOL/USD

**Rule 1 (W22-G, two-bar 20-EMA break)**: NOT ARMED.
- EMA20 series (SMA-seeded 09-23T00Z over first 20 bars = 117.6005, iteratively rolled α=2/21 through 03:00Z 09-27):
  - 02:00Z 09-27: close 121.13, EMA20 121.0138 → ABOVE (+$0.116)
  - 03:00Z 09-27: close 120.59, EMA20 120.9735 → BELOW (-$0.383)
- Only 1 of last 2 closes below EMA20 → single-bar break, does NOT trigger W22-G 2-bar exit.

**Rule 1-SBD (9-EMA)**: NOT APPLICABLE. Regime not SBD (8/15 positive, median +0.13%).

**Rule 2 (static 2×ATR stop 119.0198)**: NOT HIT.
- 24h low $119.84 (per Kraken ticker); +$0.82 headroom.

**Rule 3 (4R target 129.2708)**: NOT HIT.
- Live $120.54; -$8.73 to go.

**Verdict**: hold SOL. No trade_log write.

## EOD entry scan — 5 full-pass candidates, all cash-blocked

**Regime**: 8/15 positive, median +0.13% → 5a PASS (vs midday 3/15 -0.89%; overnight-to-EOD reversal +5 positive count, +1.02pp median).

**Full-pass (rules 1+2+2a+3+4/4a/5/5a/5b/6/6a/7)** ordered by universe rank:
- **BTC/USD** rank 1 — R1 +$175.7, R2 RSI 57.5, R3 +$1,149 (4H EMA50 83,231). 2×ATR $426.23, size 0.35984, cost **$30,378.61**. → **CASH-FAIL** ($30k vs $1.17k available)
- **ETH/USD** rank 2 — R1 +$5.17, R2 RSI 55.3, R3 +$34.26. 2×ATR $19.70, size 7.786, cost **$20,986**. → **CASH-FAIL**
- **HYPE/USD** rank 4 — R1 +$0.80, R2 RSI 61.6, R3 +$1.67. 2×ATR $1.2054, size 127.24, cost **$11,861**. → **CASH-FAIL**
- **NEAR/USD** rank 7 — R1 +$0.083, R2 RSI 57.9, R3 +$0.72. 2×ATR $0.2244, size 683.77, cost **$3,442.79**. → **CASH-FAIL**
- **SUI/USD** rank 8 — R1 +$0.006, R2 RSI 55.3, R3 +$0.16. 2×ATR $0.0351, size 4372.14, cost **$5,117.60**. → **CASH-FAIL**

**Verdict**: no entry executed this wake. All 5 full-pass candidates require notional cost exceeding available cash $1,173.45. This is the P-W27-CASHFIT archetype — SOL position occupies ~89% of equity, leaving no room for a 2nd position at 1.5%-risk-per-trade sizing on any pair (thinnest by cost was NEAR at $3,443, still 2.9× cash). Reproducing the pattern documented in `lessons.md` 2026-07-05 CASHFIT (score 9, still active). Cluster cap (SOL is BTC-cluster 1/2) would additionally block BTC/ETH/SUI even if cash were available.

Rejects with cited failing rule (from indicators.py):
- SOL/USD — R5 (open position)
- XRP/USD — R1 (close < EMA20) + R2 (RSI 39.0)
- XDG/USD — R1 + R2 (RSI 42.0)
- ADA/USD — R1 + R2 (RSI 43.9)
- LINK/USD — R1 + R2 (RSI 51.1)
- LTC/USD — R1 + R2 (RSI 43.8)
- TRX/USD — R1 + R2 (RSI 17.2) + R3 + R4a
- AVAX/USD — R1 + R2 (RSI 49.7)
- TAO/USD — R2 (RSI 52.2) — technical R1+R3 pass but RSI below 55 floor
- ONDO/USD — NOT EVALUATED (indicators.py still lists FARTCOIN not ONDO; route to routine-04-harness for config-drift fix)

## Active kill-switch state (routine-03-eod 2026-09-27T04:27Z / PT 2026-09-26 21:27)

- Daily loss cap (PT 2026-09-26): **-0.79%** (ADA -$44.92 realized + SOL -$36.04 unrealized MTM). CLEAR (5% cap, 4.21pp headroom).
- Consecutive-loss cap: **2 losses** (NEAR 09-23, ADA 09-26). Streak = 2 of 7. CLEAR.
- Max drawdown: **7.59%** from peak $11,068.89. CLEAR (25% cap, 12.5% warn, 4.91pp headroom to warn — no threshold crossed).
- Equity floor: **$10,228.56 > $7,500** (+$2,728.56 above). CLEAR.
- Exposure: **1.505% / 4% used** (SOL position). CLEAR.
- Cluster cap: **1/2 BTC-cluster** (SOL). CLEAR.
- Universe/liquidity: SOL notional ~$28.8M > $2M floor. CLEAR.
- 5b cooldown: no active cooldowns (NEAR stop-out 09-23T14Z is 62h ago > 24h; ADA exit 09-26T06Z at 22h — but ADA R2 fails anyway).
- **Regime 5a: PASS 8/15 positive, median +0.13%** — recovered from midday 3/15 -0.89% (reversal +5 positive, +1.02pp median in ~8h).
- **5a-SBD: CLEAR** both legs (8 > 1 ceiling; +0.13% > -1.0% floor).
- MCP availability: Kraken ticker + OHLCV + indicators.py + watchdog all healthy. CLEAR.
- **All Ring 3 kill switches CLEAR.**

## Ops notes

- **Third consecutive Saturday off-schedule fire this PT-day** (overnight, midday, EOD all fired Sat despite cron `Mon-Fri` mask). Scheduler config drift confirmed. Flagged for routine-04-harness for cron audit.
- **Regime recovery overnight** — from midday 3/15 -0.89% to EOD 8/15 +0.13%. 5a PASS restored. Leg-2 SBD headroom now +1.13% (vs $0.11 at midday). Book is once again entry-eligible on regime alone — but cash-blocked mechanically (see entry scan).
- **SOL trade at -0.23R at EOD** (still well inside noise; -$36 unrealized on 16h hold). No discretionary action justified.
- **Watchdog: 9 findings** (was 8 at midday, +1 new: F unpushed — local main 1 commit ahead of origin; the midday routine's commit `d79b0d6` did not push). This EOD commit will push both.
- Not last trading day of month (Sept 30 is next Wed) → no monthly archive this wake.
- Cash buffer $1,173.45 unchanged from midday (no new trades).
