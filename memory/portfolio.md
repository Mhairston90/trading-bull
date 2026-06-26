# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-06-26T15:53Z routine-01-overnight (PT Fri 2026-06-26 08:53, on-schedule cron fire). Flat throughout — 0 exits, 0 entries. Equity unchanged at $10,413.87, DD 4.25%. Regime: **5a PASS 11/15 positive median +1.21% (gate flipped from FAIL since EOD)**, SBD CLEAR. **No TECH-PASS candidates — R3 (4H>EMA50) now the binding gate, 0/15 pairs PASS.** Watchdog ALL CLEAR.

> **Prior rebuilds:** 2026-06-26T04:11Z routine-03-eod (flat, 2/15 positive, median −2.84%, SBD cleared); 2026-06-25T20:00Z routine-02-midday (flat, 1/15 positive, median −3.11%, SBD active).

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

## Overnight snapshot — 2026-06-26 PT (Fri, on-schedule 06:00 PT cron)

| Metric | Value |
|---|---|
| Wake type | routine-01-overnight (on-schedule cron fire) |
| Open positions MTM | $0.00 (flat) |
| Exits this wake | 0 (no open positions to exit) |
| Entries this wake | 0 (0 TECH-PASS candidates; regime now PASS but R3 0/15) |
| Equity (cash-only) | **$10,413.87** |
| Equity peak | $10,875.85 (unchanged; need +$461.98 to retake) |
| Drawdown from peak | **4.25%** |
| Loss streak | 0 trading days |
| Day-to-date realized PnL (2026-06-26 PT) | $0.00 |

## Active kill-switch state

- Daily realized + unrealized 2026-06-26 PT: **$0.00 / 0.00%** of equity — CLEAR.
- Consecutive losing trading days: **0** (cap 7, full headroom). CLEAR.
- Max drawdown: **4.25%** from peak $10,875.85 (cap 25%, warn 12.5%, 8.25pp to warn) — CLEAR.
- Equity floor: $10,413.87 > $7,500 floor — CLEAR.
- MCP availability: Kraken OK (`indicators.py` 720 4H bars per pair, all 15 universe pairs). CLEAR.
- Regime gate (rule 5a): **PASS** — **11/15** positive 24h, median **+1.21%** (major flip vs EOD's 2/15 / −2.84%). Top movers: FARTCOIN +7.66%, SOL +6.26%, HYPE +5.12%; negatives: NEAR −4.00%, TRX −1.26%, ETH −0.52%, TAO −0.28%. Entries are no longer pre-rejected by regime.
- Regime sub-state (rule 5a-SBD): **CLEAR.** Positives = 11 (≫ 1 ceiling); median +1.21% (≫ −1.0% floor). Both conditions fail comfortably; SBD remains lifted from EOD wake.
- Active 5b cooldowns: **None.** No pair under same-pair re-entry guard.
- Watchdog: `scripts/watchdog.py --telegram` ran 2026-06-26T15:53Z — **ALL CLEAR** (no findings, no Telegram alert).
- **All clear (kill switches).** routine-01-overnight 2026-06-26T15:53Z on-schedule fire: **0 exits, 0 entries**. Flat portfolio held; regime gate flipped to PASS but R3 (4H>50-EMA) still 0/15 — no full TECH-PASS candidates.

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

Next entry-eligible scan: routine-02-midday Fri 2026-06-26 ~12:00 PT (= 19:00Z). Regime gate now PASSes (11/15 positive, median +1.21%); the binding gate has shifted to **R3 (4H close > 4H 50-EMA), with 0/15 pairs currently above their 4H 50-EMA.** The overnight rally has not yet propagated to 4H closes — SOL is the closest candidate (4H close ~68.50 vs EMA 69.78, gap −2.6%) and is the only pair currently PASSing both R1 and R2 on a liquid universe pair (FARTCOIN also R1+R2 PASS but FAILs R4a at $0.87M). Watching SOL for R3 PASS over the next 2-3 wakes — would need 4H close above 69.78. R2 floor a secondary concern: HYPE 53.9, AVAX 51.3, SUI 51.1 are next nearest behind SOL.

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | ≈ −1.6% (SOL +$182 winner offset by 06-16/-17 ETH/HYPE/SOL stop-outs; TAO +$621 rolled off) | ≈ −8.2% (BTC ~$64.8k → $59.50k) | ≈ +6.6% | BULL well ahead 7d |
| 30d | ≈ +4.14% (inception $10k 2026-04-20; equity $10,413.87) | ≈ −23.7% (BTC 30d ago ~$78k → today $59.50k) | ≈ +27.8% | BULL well ahead |
| 90d | — | — | — | not computable (BULL inception 2026-04-20 = 67 days ago; window first computable ~2026-07-19) |

(7d/30d figures approximate. BTC ticked down slightly since EOD ($59.95k → $59.50k, −0.75%) but altcoins rallied broadly overnight — regime gate flipped because of altcoin strength, not BTC. BULL remains well ahead on both windows; held flat through the regime-gate FAIL → PASS transition, which is the designed behavior.)
