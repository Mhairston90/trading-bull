# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-06-28T20:00Z routine-02-midday (PT Sun 2026-06-28 13:00 — OFF-SCHEDULE Sunday fire vs M-F cron `0 13 * * 1-5`; routine markdown has no day-gate so executed normally). **0 entries / 0 exits** — portfolio FLAT (no open positions to mark-to-market, no exit checks possible, midday rule forbids new entries). Equity unchanged $10,212.32; DD 6.10% (peak $10,875.85 unchanged). All Ring 3 kill switches CLEAR. Day-to-date PnL $0 (no trades on PT 2026-06-28). Loss-streak still 1 day (yesterday's SOL stop). **SOL/USD 5b cooldown LAPSED at 2026-06-28T19:00Z (~1h before this wake) — SOL now re-entry-eligible at next entry-scan routine (overnight #1 or EOD #3).** Regime state not re-scored this wake (midday is position management only); last authoritative read = routine-03-eod 16:22Z showing 5a FAIL / SBD ACTIVE per `scripts/indicators.py`.

> **Prior rebuilds:** 2026-06-28T16:22Z routine-03-eod (flat, SBD ACTIVE re-engaged); 2026-06-27T21:30Z routine-02-midday (SOL/USD stop-out intrabar −$201.55 / −1.29R); 2026-06-27T16:45Z routine-01-overnight (OPEN SOL/USD 110.1608 @ $72.7364, 14/15 PASS); 2026-06-26T20:00Z routine-02-midday (flat, 12/15 PASS).

## Account

- Starting equity: **$10,000.00**
- Cash: **$10,212.32** (post-close: $2,380.18 + $7,832.14 exit proceeds — exit notional $7,852.56 less $20.42 exit commission)
- Realized PnL (all-time): **+$212.32** (was +$413.87; −$201.55 SOL stop-out this wake)
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
  - **SOL −$201.55 (exit-stop-hit-intrabar 2026-06-27T19:00Z, −1.29R)** — this wake
- Unrealized PnL (open positions): **$0** — FLAT
- Position values: **$0**
- Current equity (cash + MTM): **$10,212.32**
- Equity peak: **$10,875.85** (set 2026-06-13T09:00Z at TAO 4R close — unchanged)
- Drawdown from peak: **6.10%** ($663.53 below peak; widened from 4.54% by today's stop-out)
- Since-inception return: **+2.12%** ($10,212.32 / $10,000 − 1)

## Open positions

(none — portfolio flat after SOL stop-out)

Portfolio risk-at-moment: **0.00%** of equity. Cap 4% → full 4pp headroom.
Open positions: **0 / 8** (strategy v0.4 max-concurrent 4 → 0/4 used; BTC-cluster 0/2 used).
Breakeven ratchet (W22-H-partial): N/A — no open positions.

## Midday snapshot — 2026-06-28 PT (Sun, OFF-SCHEDULE — M-F cron fired Sun)

| Metric | Value |
|---|---|
| Wake type | routine-02-midday (OFF-SCHEDULE Sunday — routine has no day-gate, executed) |
| Open positions MTM | $0 (flat — no positions to mark) |
| Exits this wake | 0 (no positions to exit) |
| Entries this wake | 0 (routine forbids midday entries) |
| Equity (cash + MTM) | **$10,212.32** (unchanged) |
| Equity peak | $10,875.85 (unchanged; need +$663.53 to retake) |
| Drawdown from peak | **6.10%** |
| Loss streak | 1 trading day (yesterday's −$201.55 SOL stop) |
| Day-to-date realized PnL (2026-06-28 PT) | **$0 / 0.00%** |

## Active kill-switch state

- Daily realized + unrealized 2026-06-28 PT: **$0 / 0.00%** of equity — CLEAR (cap 5%, 5.00pp headroom).
- Consecutive losing trading days: **1** (cap 7, 6 days headroom). CLEAR. Today flat so streak holds at 1.
- Max drawdown: **6.10%** from peak $10,875.85 (cap 25%, warn 12.5%, 6.40pp to warn) — CLEAR.
- Equity floor: $10,212.32 > $7,500 floor — CLEAR.
- MCP availability: Kraken OK (`indicators.py` pulled 720× 4H bars/pair cleanly). CLEAR.
- Regime gate (rule 5a): **FAIL** — 1/15 positive 24h (only TRX +0.86%), median −1.92%. Flipped from Sat overnight 14/15 PASS within ~24h.
- Regime sub-state (rule 5a-SBD): **ACTIVE** — both conditions met (≤1 positive AND median ≤ −1.0%). Defensive exit tightens to 9-EMA two-bar confirmation while active. No open positions to defend this wake.
- Active 5b cooldowns: **NONE** (SOL/USD cooldown LAPSED at 2026-06-28T19:00Z, ~1h before this wake; re-entry now permitted).
- Cluster cap (rule 6a, BTC-cluster): **0/2** used. Full headroom.
- Watchdog: not run this wake (midday is lean / position management; carry-over status from prior wakes ALL CLEAR).
- Regime gate (rule 5a) / SBD: not re-scored this wake (midday is position management only). Last authoritative read at routine-03-eod 16:22Z = 5a FAIL 1/15 positive, SBD ACTIVE — will be re-evaluated by next entry-scan routine.
- **All Ring 3 kill switches CLEAR.** Routine-02-midday 2026-06-28T20:00Z (OFF-schedule Sunday fire): **0 trades**.

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

(none — flat)

Next entry-eligible scan: routine-01-overnight (PT Mon 2026-06-29 ~06:00 = 13:00Z). SOL/USD 5b cooldown has now lapsed (was 2026-06-28T19:00Z) — SOL is technically eligible for next-wake entry, subject to regime re-scoring (if SBD still ACTIVE then all entries remain blocked). LTC also on the recent TECH-PASS short list; same SBD-block applies if regime persists.

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | ≈ −2.0% (SOL net ~−$19 across 06-20→06-27 cycle, equity $10,212.32 flat today) | ≈ −7.5% (BTC ~$64.6k → $59.8k) | ≈ +5.5% | BULL ahead 7d |
| 30d | ≈ +2.12% (inception $10k 2026-04-20; equity $10,212.32 mark unchanged) | ≈ −23.4% (BTC 30d ago ~$78k → today $59,798.5) | ≈ +25.5% | BULL well ahead |
| 90d | — | — | — | not computable (BULL inception 2026-04-20 = 69 days ago; window first computable ~2026-07-19) |

(7d/30d figures approximate. Today flat, no new contribution. SBD reactivation within 24h of yesterday's PASS underscores the Sat overnight regime-flip fragility — flagged as observation, not actionable from a flat book.)
