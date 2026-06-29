# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-06-29T04:11Z routine-03-eod (PT Sun 2026-06-28 21:11 — second EOD fire for PT 2026-06-28 calendar date; the 16:22Z fire was the late-running PT-Sat-21:00 scheduled slot, this 04:11Z fire is the actual PT-Sun-21:00 slot. Cron is `0 21 * * 1-5` so both Sunday fires are OFF-SCHEDULE; routine markdown has no day-gate so executed normally). **1 entry / 0 exits** — OPENED **SOL/USD long 82.3578 @ $72.6163** (stop $70.7563 / target $80.0563 / 1.50% risk = $153.18). Regime flipped back **5a PASS 9/15 positive median +0.25% / SBD CLEAR** (was 5a FAIL 1/15 / SBD ACTIVE at 16:22Z this morning — second flip in 12h, reinforces [[2026-06-17-regime-rate-of-change]] lesson). TECH-PASS pairs: SOL, LTC, AVAX. Rule 8 winner = SOL (rank 3). SOL 5b cooldown LAPSED at 2026-06-28T19:00Z (~9h before this wake). All Ring 3 kill switches CLEAR. Cash check PASS ($5,996 notional+commission < $10,212 cash). Equity $10,212.32 → **$10,193.78** MTM (−$18.54 = −0.18% from entry friction: $15.55 commission + $2.99 slippage drag, no realized loss).

> **Prior rebuilds:** 2026-06-28T20:00Z routine-02-midday (flat, OFF-SCHED Sun, SOL cooldown lapsed at 19:00Z); 2026-06-28T16:22Z routine-03-eod (flat, SBD ACTIVE re-engaged); 2026-06-27T21:30Z routine-02-midday (SOL/USD stop-out intrabar −$201.55 / −1.29R); 2026-06-27T16:45Z routine-01-overnight (OPEN SOL/USD 110.1608 @ $72.7364, 14/15 PASS).

## Account

- Starting equity: **$10,000.00**
- Cash: **$4,216.25** (was $10,212.32; less SOL entry notional $5,980.52 less entry commission $15.55 @ 0.26%)
- Realized PnL (all-time): **+$212.32** (unchanged — no closes this wake)
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
  - SOL −$201.55 (exit-stop-hit-intrabar 2026-06-27T19:00Z, −1.29R)
- Unrealized PnL (open positions): **−$18.54** ($15.55 entry commission + $2.99 fill-slippage-to-bar-close MTM drift on SOL)
- Position values: **$5,977.53** MTM (SOL 82.3578 @ $72.58 bar close)
- Current equity (cash + MTM): **$10,193.78**
- Equity peak: **$10,875.85** (set 2026-06-13T09:00Z at TAO 4R close — unchanged)
- Drawdown from peak: **6.27%** ($682.07 below peak; widened from 6.10% by today's entry friction)
- Since-inception return: **+1.94%** ($10,193.78 / $10,000 − 1)

## Open positions

| Pair | Side | Size | Entry | Stop | Target | Stop dist (2×ATR) | Risk $ | Risk % | MTM | Unreal PnL | Bars held | Breakeven ratchet |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SOL/USD | long | 82.3578 | $72.6163 | $70.7563 | $80.0563 | $1.86 | $153.18 | 1.50% | $5,977.53 @ $72.58 | −$18.54 (incl $15.55 entry commission) | 0 (just opened) | inactive (−$0.02R, needs +2R for ratchet) |

Portfolio risk-at-moment: **1.50%** of equity. Cap 4% → 2.50pp headroom.
Open positions: **1 / 8** (strategy v0.4 max-concurrent 4 → 1/4 used; BTC-cluster 1/2 used — SOL in cluster).
Breakeven ratchet (W22-H-partial): SOL inactive (unrealized R ≈ 0; needs +2R = $80.34 to trigger).

## EOD snapshot — 2026-06-28 PT (Sun, OFF-SCHEDULE — M-F cron fired Sun 21:00 PT slot)

| Metric | Value |
|---|---|
| Wake type | routine-03-eod (OFF-SCHEDULE Sunday — 2nd EOD for PT 2026-06-28 calendar date) |
| Entries this wake | **1** (SOL/USD long 82.3578 @ $72.6163) |
| Exits this wake | 0 |
| Day-to-date realized PnL (PT 2026-06-28) | **$0 / 0.00%** (no closes) |
| Day-to-date MTM PnL (PT 2026-06-28) | **−$18.54 / −0.18%** (entry friction only) |
| Equity (cash + MTM) | **$10,193.78** |
| Equity peak | $10,875.85 (unchanged; need +$682.07 to retake) |
| Drawdown from peak | **6.27%** |
| Loss streak | 1 trading day (yesterday's −$201.55 SOL stop, holds at 1; today no realized closes) |
| Trades today | 1 opened, 0 closed |

## Active kill-switch state

- Daily realized + unrealized PT 2026-06-28: **−$18.54 / −0.18%** of equity — CLEAR (cap 5%, 4.82pp headroom).
- Consecutive losing trading days: **1** (cap 7, 6 days headroom). CLEAR. Today no closes so streak holds.
- Max drawdown: **6.27%** from peak $10,875.85 (cap 25%, warn 12.5%, 6.23pp to warn) — CLEAR.
- Equity floor: $10,193.78 > $7,500 floor — CLEAR.
- MCP availability: Kraken OK (`indicators.py` pulled 720× 4H bars/pair cleanly; `kraken_spread` SOL OK). CLEAR.
- Regime gate (rule 5a): **PASS** — 9/15 positive 24h (SOL +2.57, LTC +2.27, AVAX +3.54, FARTCOIN +9.36 leading), median +0.25%. **Flipped back from 16:22Z FAIL within ~12h.**
- Regime sub-state (rule 5a-SBD): **CLEAR.** Positives 9 (≫ 1 ceiling); median +0.25% (≫ −1.0% floor).
- Active 5b cooldowns: **NONE** (SOL/USD cooldown lapsed 2026-06-28T19:00Z, ~9h before this wake — used as fresh entry).
- Cluster cap (rule 6a, BTC-cluster): **1/2** used (SOL only). Full headroom for 1 more.
- Watchdog: 7 findings (1× A heartbeat routine-07 35h stale; 6× D stale-MTM in variant directories with open positions — all carry-over class, not Ring 3). Telegram auto-alert sent.
- **All Ring 3 kill switches CLEAR.** Routine-03-eod 2026-06-29T04:11Z (OFF-schedule Sunday-21:00-PT-slot fire): **1 entry, 0 exits**.

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

- SOL/USD long: stop $70.7563 (2×ATR), target $80.0563 (4R take-profit), Exit-1 trigger = two consecutive 1H closes < 1H 20-EMA ($71.367 ≈ current EMA), breakeven ratchet activates at +2R = $76.336 (will not fire until close at/above that level).

Next entry-eligible scan: routine-01-overnight (PT Mon 2026-06-29 ~06:00 = 13:00Z). LTC and AVAX remain TECH-PASS but blocked by rule-8 single-entry-per-wake constraint applied this wake. AVAX is non-cluster so could be paired with SOL next wake subject to portfolio risk cap (would push 1.50% → ~3.0%, still under 4% cap).

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | ≈ −2.2% (SOL net ~−$19 across 06-20→06-27 cycle, equity dropped to $10,193.78 MTM today) | ≈ −7.5% (BTC ~$64.6k → $59.95k) | ≈ +5.3% | BULL ahead 7d |
| 30d | ≈ +1.94% (inception $10k 2026-04-20; equity $10,193.78 MTM mark) | ≈ −23.1% (BTC 30d ago ~$78k → today $59,948.1) | ≈ +25.0% | BULL well ahead |
| 90d | — | — | — | not computable (BULL inception 2026-04-20 = 70 days ago; window first computable ~2026-07-19) |

(7d/30d figures approximate. Today opened a fresh SOL position at $72.6163; outcome will drive PT-29 onward.)
