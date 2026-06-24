# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-06-24T20:07Z routine-02-midday (PT label 2026-06-24 Wed midday, fired 13:07 PT on cron). Flat read/health-check wake — 0 MTM events, 0 exits, 0 entries (midday cannot enter per routine spec). Equity unchanged at $10,413.87, DD 4.25%. Regime read deteriorated vs EOD 12h ago: **5a FAIL 0/15 positive (was 1/15 AVAX), median −3.59% (was −3.68%); 5a-SBD ACTIVE** (~24h continuous, AVAX flipped negative −3.78%). All kill switches CLEAR. Silent (no Telegram triggers).

> **Prior rebuild:** 2026-06-24T04:11Z routine-03-eod (Tue 21:10 PT — closes out PT 2026-06-23 flat, equity $10,413.87, DD 4.25%, 0 OPEN, 0 CLOSE; 5a FAIL 1/15 positive AVAX +1.73%, median −3.68%, SBD ACTIVE ~12h).

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

## Midday snapshot — 2026-06-24 PT (Wed, 13:07 PT)

| Metric | Value |
|---|---|
| Wake type | routine-02-midday (position management only; cannot enter) |
| Open positions MTM | $0.00 (flat) |
| Exits triggered this wake | 0 |
| Entries this wake | 0 (forbidden by routine spec) |
| Equity (cash-only) | **$10,413.87** |
| Equity peak | $10,875.85 (unchanged; need +$461.98 to retake) |
| Drawdown from peak | **4.25%** |
| Loss streak | 0 trading days |
| Day-to-date realized PnL (2026-06-24 PT) | $0.00 |

## Active kill-switch state

- Daily realized + unrealized 2026-06-24 PT: **$0.00 / 0.00%** of equity — CLEAR.
- Consecutive losing trading days: **0** (cap 7, full headroom). CLEAR.
- Max drawdown: **4.25%** from peak $10,875.85 (cap 25%, warn 12.5%, 8.25pp to warn) — CLEAR.
- Equity floor: $10,413.87 > $7,500 floor — CLEAR.
- MCP availability: Kraken OK (multi-ticker returned all 15 universe pairs). CLEAR.
- Regime gate (rule 5a): **FAIL** — **0/15** positive (was 1/15 AVAX at EOD 12h ago — AVAX has flipped to −3.78%), median −3.59% (< 4/15 floor). Entries would be blocked; midday cannot enter regardless.
- Regime sub-state (rule 5a-SBD): **ACTIVE** — positives = 0 (≤ 1 ceiling) AND median −3.59% (≤ −1.0%). 9-EMA two-bar exit would apply to any open position; **no open positions**, so SBD defensive value this wake = 0 R avoided. SBD has now been continuously active for ~24h (since overnight 06-23T13:00Z fire).
- Active 5b cooldowns: **None.** No pair under same-pair re-entry guard.
- **All clear (kill switches).** routine-02-midday 2026-06-24T20:07Z fire: **0 MTM events, 0 exits, 0 entries**. Flat portfolio held into Wed afternoon inside continuously deteriorating SBD.

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

Next entry-eligible scan: routine-03-eod Wed 2026-06-24 ~21:00 PT (= Thu 04:00Z). Entries still gated by 5a regime recovery (≥ 4/15 positive). With 0/15 positive at midday and median deteriorating, recovery to 4/15 in the next ~8h looks remote. AVAX (prior lone TECH-PASS) has flipped negative; no obvious entry candidate sitting on the threshold.

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | ≈ −2.1% (SOL +$182 winner offset by 06-16/-17 ETH/HYPE/SOL stop-outs; TAO +$621 has now rolled off the 7d window) | ≈ −7.1% (BTC ~$65.2k → $60.6k) | ≈ +5.0% | BULL ahead 7d |
| 30d | ≈ +4.14% (inception $10k 2026-04-20; equity $10,413.87; window aligns with inception within rounding) | ≈ −22.3% (BTC 30d ago ~$78k → today $60.6k) | ≈ +26.4% | BULL well ahead |
| 90d | — | — | — | not computable (BULL inception 2026-04-20 = 65 days ago; window first computable ~2026-07-19) |

(7d/30d figures approximate. BTC dropped further mid-day (~$62.4k → $60.6k) widening BULL's 7d lead. SBD persistence is helping relative performance — by sitting flat BULL avoids the broad-market bleed.)
