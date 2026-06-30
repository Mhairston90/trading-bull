# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-06-30T15:07Z routine-01-overnight (Tue 06:00 PT slot, ~2h7m late fire at 08:07 PT). **0 entries / 0 exits** — portfolio entered wake flat after Mon EOD SOL exit; universe rolled fully negative over the ~5h since EOD (0/15 positive, median −3.05%, was 7/15 positive median −0.15% at EOD); regime 5a **FAIL** and 5a-SBD **ACTIVE** (3rd flip-flop in 36h); zero pairs pass any R1 check regardless of regime; nothing to manage, nothing to enter. Equity unchanged $10,286.93 (fully cash). DD unchanged 5.41%. All Ring 3 kill switches CLEAR.

> **Prior rebuilds:** 2026-06-30T10:30Z routine-03-eod (LATE FIRE Mon 21:00 PT slot — labeled PT 2026-06-29 Mon EOD — closed SOL/USD long +$74.48 / +0.49R net on Exit-1 two-bar EMA20 confirmation, gross +0.69R, ratchet did not arm because intrabar +2R was touched but no 1H close cleared the $76.336 threshold; ended day $10,286.93 / +0.91%); 2026-06-29T20:00Z routine-02-midday (held SOL +1.71R unrealized at tick $75.80, equity $10,458.97, DD 3.83%); 2026-06-29T04:11Z routine-03-eod (OPENED SOL/USD 82.3578 @ $72.6163, regime flipped back PASS 9/15 SBD CLEAR); 2026-06-28T20:00Z routine-02-midday (flat, OFF-SCHED Sun, SOL cooldown lapsed at 19:00Z); 2026-06-28T16:22Z routine-03-eod (flat, SBD ACTIVE re-engaged).

## Account

- Starting equity: **$10,000.00**
- Cash: **$10,286.93** (= $4,216.25 prior cash + $6,070.68 net exit proceeds from SOL close at $73.9030 less $15.82 exit commission)
- Realized PnL (all-time): **+$286.80** (= +$212.32 prior + $74.48 SOL exit-ema20-confirm-missed-scheduler-replay 2026-06-30T04:00Z)
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
  - SOL **+$74.48** (exit-ema20-confirm-missed-scheduler-replay 2026-06-30T04:00Z, **+0.49R** net)
- Unrealized PnL (open positions): **$0.00** (flat — SOL closed at this wake)
- Position values: **$0.00** (no open positions)
- Current equity (cash + MTM): **$10,286.93**
- Equity peak: **$10,875.85** (set 2026-06-13T09:00Z at TAO 4R close — unchanged)
- Drawdown from peak: **5.41%** ($588.92 below peak)
- Since-inception return: **+2.87%** ($10,286.93 / $10,000 − 1)

## Open positions

_None._

Portfolio risk-at-moment: **0.00%** of equity. Cap 4% → 4.00pp headroom.
Open positions: **0 / 8** (strategy v0.4 max-concurrent 4 → 0/4 used; BTC-cluster 0/2 used).
Breakeven ratchet (W22-H-partial): N/A (no open positions).

## Overnight snapshot — 2026-06-30 PT Tue

| Metric | Value |
|---|---|
| Wake type | routine-01-overnight (Tue 06:00 PT slot, ~2h7m late at 08:07 PT) |
| Entries this wake | 0 (regime 5a FAIL 0/15 positive + SBD ACTIVE; zero pairs pass R1 anyway) |
| Exits this wake | 0 (flat; SOL closed at prior wake) |
| Day-to-date P&L (PT 2026-06-30) | **$0.00 / 0.00%** (flat, no closes today) |
| Equity (cash + MTM) | **$10,286.93** (all cash) |
| Equity peak | $10,875.85 (unchanged; need +$588.92 to retake) |
| Drawdown from peak | **5.41%** (unchanged) |
| Loss streak | 0 trading days (unchanged) |
| Trades today | 0 opened, 0 closed |

## Active kill-switch state

- Daily realized + unrealized PT 2026-06-30: **$0.00 / 0.00%** of equity — CLEAR (flat, no positions, no closes).
- Consecutive losing trading days: **0** (cap 7, full 7-day headroom; reset by Mon's +$74.48 winner). CLEAR.
- Max drawdown: **5.41%** from peak $10,875.85 (cap 25%, warn 12.5%, 7.09pp to warn) — CLEAR.
- Equity floor: $10,286.93 > $7,500 floor — CLEAR.
- MCP availability: Kraken OK (`kraken_multi_ticker` returned all 15 pairs + `indicators.py` 720-bar series). CLEAR.
- Regime gate (rule 5a): **FAIL** (0/15 positive, median −3.05%) — all entries gated.
- Regime sub-state (rule 5a-SBD): **ACTIVE** (positives 0 ≤ 1 AND median −3.05% ≤ −1.0%). Re-engaged after brief 06-30 EOD CLEAR window — 3rd flip-flop in 36h.
- Active 5b cooldowns: **SOL/USD 24h** until 2026-07-01T04:00Z (exited 06-30T04:00Z via EMA-confirm).
- Cluster cap (rule 6a, BTC-cluster): **0/2** used. Full headroom.
- **All Ring 3 kill switches CLEAR.** Routine-01-overnight 2026-06-30T15:07Z: **0 entries, 0 exits, flat at wake / flat after**.

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

_None — portfolio flat._

Next entry-eligible scan: routine-03-eod Tue 2026-06-30 21:00 PT (= Wed 04:00Z). Gated by regime recovery (≥ 4/15 positive AND SBD clearing). SOL 5b cooldown blocks SOL re-entry until 2026-07-01T04:00Z.

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | ≈ −1.2% (equity climbed to $10,458.97 MTM then exited at $10,286.93; net since 06-23 ~$10,415 → ~−1.2%) | ≈ −5% est (BTC stable-to-soft, $59.3k area) | ≈ +3.8% est | BULL ahead 7d |
| 30d | ≈ +2.87% (inception $10k 2026-04-20; equity $10,286.93 flat-cash mark) | ≈ −23% est (BTC 30d ago ~$77k → today ~$59.3k) | ≈ +26% est | BULL well ahead |
| 90d | — | — | — | not computable (BULL inception 2026-04-20 = 71 days ago; window first computable ~2026-07-19) |

(7d/30d figures approximate; BTC tick read $59,278.7 this wake.)
