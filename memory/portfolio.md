# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-06-26T04:11Z routine-03-eod (PT Thu 2026-06-25 21:11, on-schedule cron fire). Flat throughout — 0 exits, 0 entries. Equity unchanged at $10,413.87, DD 4.25%. Regime: **5a FAIL 2/15 positive (SOL +0.77%, HYPE +1.24%), median −2.84% (improved from −3.11% midday)**; **5a-SBD CLEARED** after ~50h continuous active (positives now 2 > 1 ceiling). EOD card sent (mandatory). Watchdog ALL CLEAR.

> **Prior rebuilds:** 2026-06-25T20:00Z routine-02-midday (flat, 1/15 positive, median −3.11%, SBD active); 2026-06-25T16:20Z routine-01-overnight (flat, 0/15 positive, median −2.32%, SBD ~46h).

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

## EOD snapshot — 2026-06-25 PT (Thu, on-schedule 21:00 PT cron)

| Metric | Value |
|---|---|
| Wake type | routine-03-eod (on-schedule cron fire) |
| Open positions MTM | $0.00 (flat) |
| Exits this wake | 0 (no open positions to exit) |
| Entries this wake | 0 (0 TECH-PASS candidates + 5a FAIL regime) |
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
- MCP availability: Kraken OK (`indicators.py` 720 4H bars per pair, all 15 universe pairs). CLEAR.
- Regime gate (rule 5a): **FAIL** — **2/15** positive (SOL +0.77%, HYPE +1.24%; up from 1/15 midday), median **−2.84%** (improved from −3.11% midday; still < 4/15 floor). Entries rejected pre-technical regardless.
- Regime sub-state (rule 5a-SBD): **CLEARED** — positives = 2 (> 1 ceiling, condition (i) FAILS). SBD was continuously active ~50h (since overnight 06-23T13:00Z fire, 6 consecutive wakes); cleared this wake. Defensive value over the ~50h SBD window = 0 R avoided (flat throughout).
- Active 5b cooldowns: **None.** No pair under same-pair re-entry guard.
- Watchdog: `scripts/watchdog.py --telegram` ran 2026-06-26T04:10Z — **ALL CLEAR** (no findings, no Telegram alert). Routine-07 and variant-MTM staleness flags from prior wakes have cleared — most recent variant scaffold commits and routine-07 paper variant runs caught up.
- **All clear (kill switches).** routine-03-eod 2026-06-26T04:11Z on-schedule fire: **0 exits, 0 entries**. Flat portfolio held; SBD posture lifted; regime gate still FAIL at 2/15 positive vs 4/15 floor.

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

Next entry-eligible scan: routine-01-overnight Fri 2026-06-26 ~06:00 PT (= 13:00Z). Entries still gated by 5a regime recovery (≥ 4/15 positive). With 2/15 positive now (SOL +0.77%, HYPE +1.24%) and median improved from −3.11% → −2.84% over the ~8h since midday, regime is now moving back toward gate-PASS direction (after a midday deterioration). Still need 2 additional pairs to flip positive over the next ~9h for any entry to be eligible overnight. SBD has cleared — open positions, if any, would revert from 9-EMA two-bar exit back to 20-EMA two-bar exit. R2 (RSI ≥ 55) is currently the most-binding per-pair gate: SOL 54.4, HYPE 53.7, LTC 52.6 are within striking distance.

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | ≈ −1.6% (SOL +$182 winner offset by 06-16/-17 ETH/HYPE/SOL stop-outs; TAO +$621 rolled off) | ≈ −8.4% (BTC ~$65.4k → $59.95k) | ≈ +6.8% | BULL well ahead 7d |
| 30d | ≈ +4.14% (inception $10k 2026-04-20; equity $10,413.87) | ≈ −23.1% (BTC 30d ago ~$78k → today $59.95k) | ≈ +27.2% | BULL well ahead |
| 90d | — | — | — | not computable (BULL inception 2026-04-20 = 67 days ago; window first computable ~2026-07-19) |

(7d/30d figures approximate. BTC ticked up since midday ($59.62k → $59.95k, +0.55%) — rolling deltas narrow marginally vs BTC but BULL remains well ahead on both windows. The ~50h SBD spell ending here had no realized cost to BULL (held flat throughout) and a modest opportunity cost vs nothing — the broader tape was deeply red, so flat was correct.)
