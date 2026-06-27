# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-06-27T16:45Z routine-01-overnight (PT Sat 2026-06-27 09:45 — OFF-SCHEDULE Saturday fire vs M-F cron `0 6 * * 1-5`; routine markdown has no day-gate so executed normally). **1 ENTRY: SOL/USD 110.1608 @ 72.7364, stop 71.3184, target 78.4084 (entry-rule-v0.4-momentum, rule-8 winner over SUI/LTC/AVAX).** Regime **5a PASS 14/15 positive median +1.60%** (only HYPE −0.71% negative); SBD CLEAR. R3 (4H>EMA50) finally repaired for 5 pairs (SOL/SUI/LTC/AVAX/FARTCOIN) after a multi-wake binding period. All Ring 3 kill switches CLEAR. Watchdog 1 finding (routine-07 35h stale — carry-over, routine-04 territory).

> **Prior rebuilds:** 2026-06-26T20:00Z routine-02-midday (flat, 12/15 positive median +1.05%, SBD CLEAR); 2026-06-26T15:53Z routine-01-overnight (flat, 11/15 positive median +1.21%, regime flipped to PASS but R3 binding 0/15); 2026-06-26T04:11Z routine-03-eod (flat, 2/15 positive median −2.84%, SBD cleared).

## Account

- Starting equity: **$10,000.00**
- Cash: **$2,380.18** (post-open: $10,413.87 − $8,012.86 cost basis − $20.83 entry commission)
- Realized PnL (all-time): **+$413.87** (unchanged — no closures this wake)
  - [archived earlier rows trimmed for brevity — full ledger preserved in trade_log.md]
  - HYPE −$58.18 (exit-stop-hit 2026-05-06T15:00Z, −1.02R)
  - BTC +$1.42 (exit-ema-cross 2026-05-06T19:00Z, +0.06R)
  - LTC −$48.58 (exit-stop-hit 2026-05-07T01:00Z, −1.03R)
  - XRP −$37.68 (exit-stop-hit 2026-05-07T14:00Z, −1.05R)
  - LINK +$103.03 (exit-ema-cross 2026-05-07T20:00Z, +1.69R)
  - SOL +$585.35 (exit-4R-target 2026-05-11T19:00Z, +4.03R)
  - XRP −$21.92 (exit-ema-cross 2026-05-15T04:00Z, −0.14R) — corrected
  - HYPE +$413.62 (missed-scheduler replay exit-4R-target 2026-05-21T08:00Z, +4.04R)
  - TAO −$29.84 (missed-scheduler replay exit-ema20-confirm 2026-05-22T01:00Z, −0.50R)
  - HYPE −$33.98 (missed-scheduler replay exit-ema20-confirm 2026-05-22T02:00Z, −0.29R)
  - SOL −$45.64 (missed-scheduler replay exit-stop-hit 2026-05-22T15:00Z, −1.43R)
  - AVAX −$35.83 (missed-scheduler replay exit-ema20-confirm 2026-05-22T16:00Z, −0.94R)
  - BTC −$33.70 (exit-stop-hit 2026-05-25T22:00Z, −1.07R)
  - TAO −$114.75 (missed-scheduler replay exit-ema20-confirm 2026-05-26T18:00Z, −0.58R)
  - XRP −$101.40 (missed-scheduler replay exit-ema20-confirm 2026-05-30T23:00Z, −0.65R)
  - TAO +$621.22 (missed-scheduler replay exit-4R-target 2026-06-13T09:00Z, +4.04R)
  - BTC −$47.27 (missed-scheduler replay exit-ema20-confirm 2026-06-14T13:00Z, −0.60R)
  - ETH −$214.33 (missed-scheduler replay exit-stop-hit 2026-06-16T15:00Z, −1.32R)
  - HYPE −$182.64 (missed-scheduler replay exit-stop-hit 2026-06-17T12:00Z, −1.15R)
  - SOL −$199.87 (exit-stop-hit intrabar replay 2026-06-17T18:00Z, −1.28R)
  - SOL +$232.13 (missed-scheduler replay exit-ema20-confirm 2026-06-22T15:00Z, +1.51R gross)
  - SOL −$50.00 (correction-previous-row friction adjustment 2026-06-22T16:00Z, net SOL exit = +$182.13 / +1.19R)
- Unrealized PnL (open positions, mark to last $72.64): **−$10.78** raw / **−$31.61** including paid entry commission
- Position values (MTM @ $72.64): **$8,002.08**
- Current equity (cash + MTM): **$10,382.26** (vs $10,413.87 pre-trade; −$31.61 = entry commission + intra-bar mark drift)
- Equity peak: **$10,875.85** (set 2026-06-13T09:00Z at TAO 4R close — unchanged)
- Drawdown from peak: **4.54%** ($493.59 below peak; widened from 4.25% by entry friction + mark)
- Since-inception return: **+3.82%** ($10,382.26 / $10,000 − 1)

## Open positions

| Pair | Side | Size | Entry | Stop | Target | Entry time (UTC) | Stop dist | Risk ($) | Cluster | Last | MTM | Unrealized R |
|------|------|-----:|------:|-----:|-------:|------------------|---------:|---------:|---------|-----:|----:|-------------:|
| SOL/USD | long | 110.1608 | 72.7364 | 71.3184 | 78.4084 | 2026-06-27T16:00:00Z | 1.418 | $156.21 | BTC-cluster | 72.64 | $8,002.08 | −0.07R (mark drift; commission excluded) |

Portfolio risk-at-moment: **1.50%** of equity (SOL stop-distance × size / equity = 156.21 / 10,413.87). Cap 4% → 2.50pp headroom.
Open positions: **1 / 8** (strategy v0.4 max-concurrent 4 → 1/4 used; BTC-cluster 1/2 used — SOL counted; cap leaves 1 cluster slot).
Breakeven ratchet (W22-H-partial): not yet armed (requires +2R unrealized 1H close — currently −0.07R).

## Overnight snapshot — 2026-06-27 PT (Sat, OFF-SCHEDULE — M-F cron fired Sat)

| Metric | Value |
|---|---|
| Wake type | routine-01-overnight (OFF-SCHEDULE Saturday — routine has no day-gate, executed) |
| Open positions MTM | $8,002.08 (1 long SOL) |
| Exits this wake | 0 (no positions to exit pre-trade) |
| Entries this wake | **1 (SOL/USD long 110.1608 @ 72.7364)** |
| Equity (cash + MTM) | **$10,382.26** |
| Equity peak | $10,875.85 (unchanged; need +$493.59 to retake) |
| Drawdown from peak | **4.54%** |
| Loss streak | 0 trading days |
| Day-to-date realized PnL (2026-06-27 PT) | $0.00 |

## Active kill-switch state

- Daily realized + unrealized 2026-06-27 PT: **−$31.61 / −0.30%** of equity — CLEAR (cap 5%).
- Consecutive losing trading days: **0** (cap 7, full headroom). CLEAR.
- Max drawdown: **4.54%** from peak $10,875.85 (cap 25%, warn 12.5%, 7.96pp to warn) — CLEAR.
- Equity floor: $10,382.26 > $7,500 floor — CLEAR.
- MCP availability: Kraken OK (`kraken_multi_ticker` via indicators.py returned all 15 pairs; `kraken_ticker` + `kraken_spread` confirm fresh SOL quotes). CLEAR.
- Regime gate (rule 5a): **PASS** — **14/15** positive 24h, median **+1.60%**. Only HYPE −0.71% negative; broad rally led by NEAR +4.95%, AVAX +4.23%, LTC +4.19%, FARTCOIN +3.06%. Entries no longer pre-rejected.
- Regime sub-state (rule 5a-SBD): **CLEAR.** Positives = 14 (≫ 1 ceiling); median +1.60% (≫ −1.0% floor).
- Active 5b cooldowns: **None.** Last stop-out 2026-06-17T18:00Z SOL — well past 24h.
- Cluster cap (rule 6a, BTC-cluster {BTC,ETH,SOL,TAO,AVAX,SUI,LINK}): **1/2** used (SOL). 1 slot remaining.
- Watchdog: 1 finding (A heartbeat: routine-07 35h stale, +5h past 30h threshold — carry-over, routine-04 territory; Telegram alert auto-sent).
- **All Ring 3 kill switches CLEAR.** Routine-01-overnight 2026-06-27T16:45Z (OFF-schedule Saturday fire): **0 exits, 1 entry (SOL +110.1608)**.

## Universe refresh — 2026-06-01 (first true 30d aggregation)

| Rank | Pair | Change vs prior |
|------|------|-----------------|
| 1 | BTC | — |
| 2 | ETH | — |
| 3 | SOL | — |
| 4 | HYPE | ▲ from 6 |
| 5 | XRP | ▼ from 4 |
| 6 | SUI | ▲ from 8 |
| 7 | TAO | ▼ from 5 |
| 8 | XDG (DOGE) | — |
| 9 | NEAR | **NEW** (was off-list near-miss) |
| 10 | ADA | — |
| 11 | LINK | ▲ from 13 |
| 12 | LTC | ▼ from 9 |
| 13 | FARTCOIN | ▼ from 11 |
| 14 | TRX | ▲ from 15 |
| 15 | AVAX | ▼ from 12 |

- **PENGU dropped** (was rank 14) → moves to near-miss watch list (~$38M 30d notional).
- **Near-miss watch:** PENGU $38M, DOT $22M, UNI $20M.

## Pending exit triggers

- **SOL/USD long:** stop $71.3184 (2×ATR initial), target $78.4084 (+4R). EMA20 exit fires on 2 consecutive 1H closes < EMA20 (current EMA20 ~71.81). Breakeven ratchet arms when unrealized R ≥ 2.0 at 1H close (price ≥ $75.57).

Next entry-eligible scan: routine-02-midday is non-entering; first true next entry slot = routine-03-eod Sat 2026-06-27 ~21:00 PT (= Sun 04:00Z). With 1 cluster slot remaining and regime gate PASSing, additional cluster entries possible if a fresh R3 PASS emerges. SUI/LTC/AVAX/FARTCOIN remain on the watchlist; FARTCOIN still blocked by R4a liquidity.

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | ≈ −0.3% (SOL +$182 winner offset by stop-outs; flat through 06-23→06-26; new SOL entry just opened) | ≈ −6.6% (BTC ~$65k → $60.74k) | ≈ +6.3% | BULL ahead 7d |
| 30d | ≈ +3.82% (inception $10k 2026-04-20; equity $10,382.26 mark) | ≈ −22.2% (BTC 30d ago ~$78k → today $60.74k) | ≈ +26.0% | BULL well ahead |
| 90d | — | — | — | not computable (BULL inception 2026-04-20 = 68 days ago; window first computable ~2026-07-19) |

(7d/30d figures approximate. BTC recovered overnight from $59.5k → $60.74k (+2.1%), part of broad altcoin-led rally that flipped R3 across 5 pairs and finally produced a TECH-PASS entry slot.)
