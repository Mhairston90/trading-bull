# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md`; the log remains the source of truth.
> **Last rebuild:** 2026-09-26T13:20Z routine-01-overnight (PT 2026-09-26 06:20) — retroactive ADA exit at 06:00Z close 0.254014 (-0.29R / -$44.92 gross, exit-ema20-2bar-recovery replay); new SOL/USD long opened this wake at 12:00Z 1H bar close 121.07; rule 8 selected SOL as highest 30d notional rank among 6 full-pass candidates (SOL 3, SUI 8, TAO 9, LTC 11, AVAX 12, LINK 13). Off-schedule Saturday fire noted.

## Account

- Starting equity: **$10,000.00**
- Cash: **$1,173.45** ($10,264.60 − $9,091.15 SOL position cost)
- Realized PnL: **+$264.60** ($309.52 + (-$44.92 ADA))
- Unrealized PnL: **$0.00** (fresh SOL entry at bar-close 121.07, MTM equal to entry on last closed 1H bar)
- Current equity: **$10,264.60**
- Equity peak: **$11,068.89**
- Drawdown from peak: **7.27%**
- Since-inception return: **+2.65%**

## Open positions

| Pair | Side | Size | Entry | Stop | Target | Cost | Unrealized R | Notes |
|------|------|-----:|------:|-----:|-------:|-----:|-------------:|-------|
| SOL/USD | long | 75.09 | 121.07 | 119.0198 | 129.2708 | $9,091.15 | +0.00R | 2×ATR stop = 2.0502; risk $153.95 = 1.500% equity; rule-8 winner rank 3; BTC-cluster 1/2 |

Portfolio risk-at-moment: **1.500%** (SOL $153.95 / $10,264.60).
Open positions: **1 / 8** (strategy cap 1/4; BTC cluster 1/2 — SOL in cluster).

## Day summary — PT 2026-09-26

- **Day PnL**: **-$44.92 / -0.44%** (ADA -0.29R stop-out via 2-bar EMA20 recovery replay).
- **Trades opened**: **1** (SOL/USD long, entry-rule-v0.4-momentum-rule8-winner).
- **Trades closed**: **1** (ADA/USD long, exit-ema20-2bar-recovery-missed-scheduler-replay).
- **Win rate today**: **0/1 (0.00%)** on closed trades.
- **Time-in-trade (ADA)**: **2h** (04:00Z open → 06:00Z close).

## Rolling benchmark (07-10 last live equity → 09-26 latest)

- **BULL 30d** (08-27 → 09-26): **-2.08%** (ADA -0.44% marked down from -1.64%).
- **BULL 7d** (09-19 → 09-26): **-2.08%** (same window).
- **BTC-hold 30d** (approx 08-27 close ~$79.5k → 09-26T13Z live ~$83.99k): **+5.65%**.
- **BTC-hold 7d** (09-19 close ~$76.4k → 09-26T13Z live ~$83.99k): **+9.94%**.
- **BULL vs BTC-hold 30d**: **-7.73pp behind** BTC.
- **BULL vs BTC-hold 7d**: **-12.02pp behind** BTC.
- **90d benchmark**: not-yet-computable (post-outage cross-window with 74d gap; will resume at next EOD after 10-15).

## Overnight action — ADA exit + SOL entry (rule-8 winner among 6 full-pass candidates)

**Regime (indicators.py 13:13Z snapshot):** 6/15 positive 24h, median -0.15% → **5a PASS** (margin +2 vs 4-floor, thin), **5a-SBD CLEAR** both legs (6/15 > 1 AND median -0.15% > -1.0%).

**ADA retroactive exit:** rule 1 (W22-G) fired at 06:00Z 1H bar close. Computed EMA20 (SMA-seeded over 100 bars, α=2/21):
- 04:00Z close 0.256558, EMA20 0.255288 → ABOVE (+$0.00127)
- 05:00Z close 0.254976, EMA20 0.255259 → BELOW (bar 1)
- 06:00Z close 0.254014, EMA20 0.255140 → BELOW (bar 2, exit fires)
- Exit fill: 0.254014 (bar close, no slippage per 07-10 BTC precedent). Gross PnL -$44.92, R -0.29. Reason tag `exit-ema20-2bar-recovery-missed-scheduler-replay`.

**Full-pass rule set (R1+R2+R2a+R3) — post-ADA-exit entry scan:**
| Pair | Rank | 1H close | R1 (EMA20) | R2 (RSI) | R3 (4H EMA50) | 2×ATR | 24h% |
|---|---:|---:|---|---|---|---:|---:|
| **SOL/USD** | **3** | 121.07 | +0.4521 | 55.9 (+0.92) | +6.676 | 2.0502 | +0.30 |
| SUI/USD | 8 | 1.1707 | +0.01618 | 60.3 (+5.28) | +0.1984 | 0.045887 | +2.23 |
| TAO/USD | 9 | 331.124 | +16.55 | 76.8 (+21.85) | +42.47 | 11.976 | +7.96 |
| LTC/USD | 11 | 72.89 | +0.4121 | 55.9 (+0.87) | +8.945 | 2.2323 | +3.99 |
| AVAX/USD | 12 | 10.815 | +0.1653 | 59.4 (+4.37) | +0.8751 | 0.3286 | +2.26 |
| LINK/USD | 13 | 14.2101 | +0.1998 | 62.4 (+7.41) | +1.399 | 0.38836 | +1.26 |

**Rule 8 winner: SOL/USD** (rank 3, highest 30d notional among passers). Note: SOL R2 margin is thin (+0.92 over 55 floor) — the trade is deterministic-rule-driven, not conviction-sized. SOL is in BTC-cluster {BTC,ETH,SOL,TAO,AVAX,SUI,LINK} → cluster count 0/2 → 1/2 after entry.

**Non-universe technical pass:** FARTCOIN R1+R2a+R3 PASS but R2 FAIL (RSI 53.0 < 55) — auto-skipped by universe filter anyway (dropped 07-01).

**Near-misses (informational):** BTC R1 FAIL -$6.16 + R2 FAIL 49.3; ETH R2 FAIL 50.0; HYPE R2 FAIL 49.9; XRP R1 FAIL by $0.011 + R2 FAIL 44.3; NEAR R1 FAIL + R2 FAIL 48.2 (also in 5b window until 09-24T14Z, now expired); XDG R1 FAIL + R2 FAIL 48.5; TRX all-rules FAIL; ADA R2 FAIL 52.1 (just exited).

## Active kill-switch state (routine-01-overnight 2026-09-26T13:20Z / PT 2026-09-26 06:20)

- Daily loss cap (PT 2026-09-26): **-0.44%** (ADA closed -$44.92). CLEAR (5% cap, 4.56pp headroom).
- Consecutive-loss cap: **2 losses** (NEAR 09-23, ADA 09-26). Streak = 2 of 7. CLEAR.
- Max drawdown: **7.27%** from peak $11,068.89. CLEAR (25% cap, 12.5% warn, 5.23pp headroom).
- Equity floor: **$10,264.60 > $7,500** (+$2,764.60 above). CLEAR.
- Exposure: **1.500% / 4% used** (SOL position). CLEAR.
- Cluster cap: **1/2 BTC-cluster** (SOL). CLEAR.
- Universe/liquidity: SOL notional $56.43M > $2M floor. CLEAR.
- 5b cooldown: no active cooldowns (ADA exit was ema20 confirm, not stop-hit; rule 5b applies to `exit-stop-hit` only).
- **Regime 5a: PASS 6/15 positive, median -0.15%** (margin +2, thin).
- **5a-SBD: CLEAR** (both legs: 6/15 > 1 AND median -0.15% > -1.0%).
- MCP availability: Kraken ticker + indicators.py both healthy. CLEAR.
- **All Ring 3 kill switches CLEAR.**

## Ops notes

- **Off-schedule Saturday fire:** routine-01-overnight cron is `0 6 * * 1-5` (Mon-Fri) — scheduler fired on Saturday 2026-09-26. Slot identity `bull-01-overnight` confirmed. Routine executed per spec anyway. Follow-up: route to routine-04-harness (also Sat 09-26 per plan) to review why the cron fired outside its Mon-Fri window.
- **SOL R2 margin thin (+0.92 over 55 floor).** Rule 8 mechanical winner — no discretionary override. Watched for early stop-out risk.
- **Full cash-fit sizing possible** because ADA exit freed $4,893.54 cash before SOL entry evaluated. Post-ADA-exit equity $10,264.60, cash $10,264.60; SOL 75.09 × 121.07 = $9,091.15 leaves $1,173.45 cash buffer. Would have been cashfit'd otherwise ($5,371.06 pre-exit cash was < $9,131 full-size).
- Watchdog fired 8 findings (2 heartbeat routine-06/07 overdue, 1 dirty-tree 4 carry-over files, 5 stale-MTM variants) — telegram alert already auto-sent at 13:12Z. Same as EOD wake; not degraded.
- ONDO/USD (rank 14) still not in indicators.py config — routed to routine-04-harness for reconciliation.
- News scan (Firecrawl) skipped for SOL — v0.2 informational-only, does not veto entries.
- Sentiment (SOL): Kraken spread ~1.2 bps (bid 120.71 / ask 120.72). Good depth.
- Not last trading day of month → no monthly archive this wake.
