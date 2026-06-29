# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-06-29T20:00Z routine-02-midday (PT Mon 2026-06-29 13:00 ON-SCHEDULE M-F cron `0 13 * * 1-5`). **0 entries / 0 exits** — held SOL/USD long 82.3578 from this morning's 04:00Z entry. Position is **+1.71R unrealized** at tick $75.80 (last 1H close $75.86 at bar 29-19). All exit checks PASS: 1H 20-EMA ≈ $73.38 < close $75.86 (Exit 1 not triggered, single-side); lowest low since entry $70.92 (bar 29-05) > stop $70.7563 (stop not pierced); highest high $76.34 (bar 29-17) < target $80.0563 (4R target not hit). Breakeven ratchet still inactive — needs a 1H close ≥ $76.336 (= +2R); the +2R level was touched intrabar (29-17 high $76.34) but no 1H close has reached it (highest close $75.86 at 29-19 = +1.74R). Equity $10,193.78 → **$10,458.97** (+$265.19 = +2.60% intraday from MTM gain on SOL move 13:00Z → 17:00Z bar +$1.78 close-to-close, with continuation to 19:00Z close $75.86). DD compressed from 6.27% → **3.83%**. All Ring 3 kill switches CLEAR.

> **Prior rebuilds:** 2026-06-29T04:11Z routine-03-eod (OPENED SOL/USD 82.3578 @ $72.6163, regime flipped back PASS 9/15 SBD CLEAR); 2026-06-28T20:00Z routine-02-midday (flat, OFF-SCHED Sun, SOL cooldown lapsed at 19:00Z); 2026-06-28T16:22Z routine-03-eod (flat, SBD ACTIVE re-engaged); 2026-06-27T21:30Z routine-02-midday (SOL/USD stop-out intrabar −$201.55 / −1.29R); 2026-06-27T16:45Z routine-01-overnight (OPEN SOL/USD 110.1608 @ $72.7364, 14/15 PASS).

## Account

- Starting equity: **$10,000.00**
- Cash: **$4,216.25** (unchanged from this morning's entry — no exits this wake)
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
- Unrealized PnL (open positions): **+$246.65** ((tick $75.80 − entry $72.6163) × 82.3578 − $15.55 entry commission = +$262.20 − $15.55 = +$246.65; gross unrealized +1.71R)
- Position values: **$6,242.72** MTM (SOL 82.3578 @ tick $75.80)
- Current equity (cash + MTM): **$10,458.97**
- Equity peak: **$10,875.85** (set 2026-06-13T09:00Z at TAO 4R close — unchanged)
- Drawdown from peak: **3.83%** ($416.88 below peak; compressed from 6.27% by +$265.19 MTM gain this wake)
- Since-inception return: **+4.59%** ($10,458.97 / $10,000 − 1)

## Open positions

| Pair | Side | Size | Entry | Stop | Target | Stop dist (2×ATR) | Risk $ | Risk % | MTM | Unreal PnL | Bars held | Breakeven ratchet |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SOL/USD | long | 82.3578 | $72.6163 | $70.7563 | $80.0563 | $1.86 | $153.18 | 1.50% | $6,242.72 @ $75.80 | +$246.65 (incl $15.55 entry commission) | 16 (entry 04:00Z → wake 20:00Z) | inactive (+1.71R tick / +1.74R last close; needs +2R = $76.336 at close to trigger) |

Portfolio risk-at-moment: **1.50%** of equity (using entry-time risk basis; effective risk reduced as position runs in-favor). Cap 4% → 2.50pp headroom.
Open positions: **1 / 8** (strategy v0.4 max-concurrent 4 → 1/4 used; BTC-cluster 1/2 used — SOL in cluster).
Breakeven ratchet (W22-H-partial): SOL inactive (peak 1H close +1.74R at bar 29-19 $75.86; needs +2R = $76.336 close — touched intrabar at 29-17 high $76.34 but the 1H closed at $75.18, ratchet did NOT fire because rule requires the close ≥ +2R).

## Midday snapshot — 2026-06-29 PT Mon (ON-SCHEDULE)

| Metric | Value |
|---|---|
| Wake type | routine-02-midday (ON-SCHEDULE Mon — M-F cron) |
| Entries this wake | 0 (midday rule: no new entries) |
| Exits this wake | 0 (all exit checks PASS) |
| Day-to-date MTM PnL (PT 2026-06-29) | **+$265.19 / +2.60%** (intraday MTM gain on SOL) |
| Equity (cash + MTM) | **$10,458.97** |
| Equity peak | $10,875.85 (unchanged; need +$416.88 to retake) |
| Drawdown from peak | **3.83%** (compressed from 6.27% morning) |
| Loss streak | 1 trading day (Sat 06-27 stop, no closes today so streak holds) |
| Trades today | 1 opened (this morning's EOD wake), 0 closed |

## Active kill-switch state

- Daily realized + unrealized PT 2026-06-29: **+$265.19 / +2.60%** of equity — CLEAR (positive, no daily-loss exposure).
- Consecutive losing trading days: **1** (cap 7, 6 days headroom). CLEAR. Today positive day so far, no closes.
- Max drawdown: **3.83%** from peak $10,875.85 (cap 25%, warn 12.5%, 8.67pp to warn) — CLEAR.
- Equity floor: $10,458.97 > $7,500 floor — CLEAR.
- MCP availability: Kraken OK (`kraken_multi_ticker` + `kraken_ohlcv` 1h 60 bars returned cleanly). CLEAR.
- Regime gate (rule 5a): not re-scored (midday is position management only — last authoritative read routine-03-eod 04:11Z: 5a PASS 9/15 positive median +0.25%).
- Regime sub-state (rule 5a-SBD): not re-scored (last read: CLEAR).
- Active 5b cooldowns: **NONE** (SOL/USD currently open, not in cooldown).
- Cluster cap (rule 6a, BTC-cluster): **1/2** used (SOL only). Full headroom for 1 more (next entry-scan).
- **All Ring 3 kill switches CLEAR.** Routine-02-midday 2026-06-29T20:00Z (ON-SCHEDULE M-F slot): **0 entries, 0 exits, SOL running +1.71R**.

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

- SOL/USD long: stop $70.7563 (2×ATR), target $80.0563 (4R take-profit), Exit-1 trigger = two consecutive 1H closes < 1H 20-EMA (last EMA ≈ $73.38 at close of 29-19, latest close $75.86 = $2.48 above — Exit 1 needs first single-bar break first), breakeven ratchet activates at first 1H close ≥ $76.336 (will move stop $70.7563 → $72.6163 = entry, locking out the −1R loss path).

Next entry-eligible scan: routine-03-eod (PT Mon 2026-06-29 ~21:00 = 04:00Z Tue 2026-06-30). Midday holds the position untouched.

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | ≈ +0.4% (equity climbed to $10,458.97 MTM through Sat-stop −$201, Sun re-entry, Mon SOL ramp) | ≈ −5% est (BTC stable-to-soft) | ≈ +5% est | BULL ahead 7d |
| 30d | ≈ +4.59% (inception $10k 2026-04-20; equity $10,458.97 MTM mark) | ≈ −22% est (BTC 30d ago ~$77k → today ~$60k area) | ≈ +27% est | BULL well ahead |
| 90d | — | — | — | not computable (BULL inception 2026-04-20 = 70 days ago; window first computable ~2026-07-19) |

(7d/30d figures approximate; BTC tick not refreshed this wake since midday is SOL-only MTM.)
