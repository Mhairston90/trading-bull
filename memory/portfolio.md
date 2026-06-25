# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-06-25T20:00Z routine-02-midday (Thu 13:00 PT, on-schedule cron fire). Flat throughout — 0 exits, 0 entries (midday non-entering). Equity unchanged at $10,413.87, DD 4.25%. Regime: **5a FAIL 1/15 positive (HYPE +0.19%), median −3.11% (worsened from −2.32% overnight)**; **5a-SBD ACTIVE** (~50h continuous, 6th consecutive SBD wake). Silent (no Telegram triggers).

> **Prior rebuild:** 2026-06-25T16:20Z routine-01-overnight (Thu OFF-CRON 09:20 PT; flat, 0/15 positive, median −2.32%, SBD ~46h).

## Account

- Starting equity: **$10,000.00**
- Cash: **$10,413.87** (unchanged — no trade events this wake)
- Realized PnL (all-time): **+$413.87** (unchanged)
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
- Unrealized PnL (open positions): **$0.00** (flat)
- Position values (MTM): **$0.00**
- Current equity (cash only): **$10,413.87**
- Equity peak: **$10,875.85** (set 2026-06-13T09:00Z at TAO 4R close — unchanged)
- Drawdown from peak: **4.25%** ($461.98 below peak; unchanged — flat wake)
- Since-inception return: **+4.14%** ($10,413.87 / $10,000 − 1)

## Open positions

_None._

Portfolio risk-at-moment: **0.00%** of equity (no open positions; cap 4%, full headroom).
Open positions: **0 / 8** (strategy v0.4 max-concurrent 4 → 0/4 used; cluster cap 0/2).
Breakeven ratchet (W22-H-partial): n/a (no open position).

## Midday snapshot — 2026-06-25 PT (Thu, on-schedule 13:00 PT cron)

| Metric | Value |
|---|---|
| Wake type | routine-02-midday (on-schedule cron fire) |
| Open positions MTM | $0.00 (flat) |
| Exits this wake | 0 (no open positions to exit) |
| Entries this wake | 0 (midday non-entering per routine spec) |
| Equity (cash-only) | **$10,413.87** |
| Equity peak | $10,875.85 (unchanged; need +$461.98 to retake) |
| Drawdown from peak | **4.25%** |
| Loss streak | 0 trading days |
| Day-to-date realized PnL (2026-06-25 PT) | $0.00 |

## Active kill-switch state

- Daily realized + unrealized 2026-06-25 PT: **$0.00 / 0.00%** of equity — CLEAR.
- Consecutive losing trading days: **0** (cap 7, full headroom). CLEAR.
- Max drawdown: **4.25%** from peak $10,875.85 (cap 25%, warn 12.5%, 8.25pp to warn) — CLEAR.
- Equity floor: $10,413.87 > $7,500 floor — CLEAR.
- MCP availability: Kraken OK (multi-ticker returned all 15 universe pairs). CLEAR.
- Regime gate (rule 5a): **FAIL** — **1/15** positive (HYPE +0.19% only; up from 0/15 overnight), median **−3.11%** (worsened from −2.32% overnight; < 4/15 floor). Entries would be rejected pre-technical (midday is non-entering regardless).
- Regime sub-state (rule 5a-SBD): **ACTIVE** — positives = 1 (≤ 1 ✓) AND median −3.11% (≤ −1.0% ✓). SBD continuously active ~50h (6th consecutive SBD wake, since overnight 06-23T13:00Z fire). Defensive value this wake = 0 R (flat).
- Active 5b cooldowns: **None.** No pair under same-pair re-entry guard.
- Watchdog: not re-run this routine (no carry-over change — last full run was overnight 16:20Z, ALL CLEAR).
- **All clear (kill switches).** routine-02-midday 2026-06-25T20:00Z on-schedule fire: **0 exits, 0 entries**. Flat portfolio held into Thu midday inside ~50h continuous SBD. HYPE is the lone positive; broader median has deepened (−2.32% → −3.11%).

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

_None — no open positions._

Next entry-eligible scan: routine-03-eod Thu 2026-06-25 ~21:00 PT (= Fri 04:00Z). Entries still gated by 5a regime recovery (≥ 4/15 positive). With 1/15 positive now (HYPE only) and median deepened from −2.32% → −3.11% over the ~3h45m since overnight, the regime is moving further away from gate-PASS, not closer. Needs 3 additional pairs to flip positive over the next ~8h for any entry to be eligible at EOD.

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | ≈ −1.6% (SOL +$182 winner offset by 06-16/-17 ETH/HYPE/SOL stop-outs; TAO +$621 rolled off) | ≈ −8.9% (BTC ~$65.4k → $59.62k) | ≈ +7.3% | BULL well ahead 7d |
| 30d | ≈ +4.14% (inception $10k 2026-04-20; equity $10,413.87) | ≈ −23.6% (BTC 30d ago ~$78k → today $59.62k) | ≈ +27.7% | BULL well ahead |
| 90d | — | — | — | not computable (BULL inception 2026-04-20 = 66 days ago; window first computable ~2026-07-19) |

(7d/30d figures approximate. BTC drifted slightly lower since overnight 3h45m ago ($59.68k → $59.62k, −0.10%); rolling deltas widen marginally in BULL's favor. SBD persistence continues to help relative performance — by sitting flat BULL avoids the broader 24h leg-down across 14/15 pairs.)
