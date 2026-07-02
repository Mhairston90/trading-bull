# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-07-02T04:11Z routine-03-eod (PT Wed 2026-07-01 21:11 ON-SCHEDULE M-F cron `0 21 * * 1-5`; PT date label 2026-07-01 per date-labeling guard). **0 OPEN / 0 CLOSE this wake** — SOL/USD held through the EOD check: all three exit paths passed (20-EMA ≈ $76.93 at last close 07-02T03:00Z, last 1H close $78.64 is $1.71 above; lowest low since entry $73.84 vs stop $73.5918, +25bps headroom, stop NOT pierced; 4R target $82.4019 not hit, peak intrabar high $78.88 at bar 07-01T22:00Z). **Breakeven ratchet still inactive** — peak 1H close since entry = $78.64 at bar 07-02T03:00Z (+1.87R), needs 1H close ≥ $78.878 (+2R) to arm; gap to arm **$0.24**. Intrabar highs $78.88 (07-01T22:00Z) and $78.87 (07-02T03:00Z) touched +2R level exactly but neither bar closed above → **3rd instance of the W22-H intrabar-touch-close-misses pattern in ~10 days** (SOL 06-22, SOL 06-29, SOL 07-01) — noted for routine-04 W27 consolidation per [[lesson 2026-06-29 W22-H ratchet]]. Entry scan ran per EOD spec: regime 5a **PASS 12/15 positive median +2.46%**, SBD **CLEAR**; 7 TECH-PASS candidates ex-SOL (BTC/ETH/XRP/ADA/NEAR/SUI/LTC), **all rule-8 fallback candidates REJECTED by cash-insufficient** (cash $3,670.97 vs required notionals $4,714–$9,340 at strategy-mandated 1.5% sizing) — reinforces [[P-W26-CASHFIT]] pending user `[Y/N]`. Equity MTM **$10,557.55** (+$290.33 / +2.83% day-to-date vs prior EOD $10,267.22 — entirely SOL mark-up, no realized closes). DD **2.93%** (compressed 1.41pp from midday's 4.34%). All Ring 3 kill switches CLEAR. Watchdog 8 findings (routine-07 107h stale carry-over + 6 stale-MTM variants + 1 dirty-tree scripts/ carry-over from prior routine-07 replay session). Monthly archive check: PT 2026-07-01 = first trading day of July → no archive (2026-06 archive completed by 06-30 EOD).

> **Prior rebuilds:** 2026-07-01T20:00Z routine-02-midday (Wed 13:00 PT ON-SCHEDULE M-F, 0/0, SOL held +0.87R unrealized, DD 4.34%); 2026-07-01T15:52Z routine-01-overnight (Wed 06:00 PT slot ~2h52m late fire, 0/0, regime PASS 13/15 SBD CLEAR, SOL held +0.86R unrealized, universe refresh ONDO in / FARTCOIN out); 2026-07-01T04:12Z routine-03-eod (Tue 21:00 PT ON-SCHEDULE M-F, PT date 2026-06-30, 1 entry SOL/USD 87.5709 @ $75.3538 / 0 exits, rule-8 winner over HYPE/SUI/ADA/LTC, regime flipped back PASS 9/15 SBD CLEAR); 2026-06-30T20:00Z routine-02-midday (Tue 13:00 PT ON-SCHEDULE M-F, 0/0, flat, regime FAIL 1/15 SBD ACTIVE); 2026-06-30T15:07Z routine-01-overnight (Tue 06:00 PT slot ~2h7m late fire, 0/0, regime FAIL 0/15 SBD ACTIVE); 2026-06-30T10:30Z routine-03-eod (LATE FIRE Mon 21:00 PT slot — labeled PT 2026-06-29 Mon EOD — closed SOL/USD long +$74.48 / +0.49R net on Exit-1 two-bar EMA20 confirmation, ended day $10,286.93 / +0.91%).

## Account

- Starting equity: **$10,000.00**
- Cash: **$3,670.97** (unchanged; no trade events this wake)
- Realized PnL (all-time): **+$286.80** (unchanged; no closes this wake)
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
  - SOL +$74.48 (exit-ema20-confirm-missed-scheduler-replay 2026-06-30T04:00Z, +0.49R net)
- Unrealized PnL (open positions): **+$287.83** (SOL 87.5709 × ($78.64 − $75.3538) = 87.5709 × $3.2862 = +$287.83 gross; entry commission $17.16 already booked at open)
- Position values: **$6,886.58** (SOL 87.5709 × $78.64 last 1H close 07-02T03:00Z = $6,886.58 MTM)
- Current equity (cash + MTM): **$10,557.55** (= $3,670.97 cash + $6,886.58 SOL MTM; wake-over-wake PnL = +$153.25 from $10,404.30 prior rebuild)
- Equity peak: **$10,875.85** (set 2026-06-13T09:00Z at TAO 4R close — unchanged)
- Drawdown from peak: **2.93%** ($318.30 below peak; compressed 1.41pp from 4.34% at prior wake)
- Since-inception return: **+5.58%** ($10,557.55 / $10,000 − 1)

## Open positions

| Pair | Side | Size | Entry | Stop | Target | Notional | Risk-at-moment | Cluster | Entered |
|------|------|------|-------|------|--------|----------|----------------|---------|---------|
| SOL/USD | long | 87.5709 | $75.3538 | $73.5918 | $82.4019 | $6,598.80 | 1.46% ($154.30 / $10,557.55) | BTC-cluster (1/2) | 2026-07-01T04:00Z |

Portfolio risk-at-moment: **1.46%** of equity. Cap 4% → 2.54pp headroom.
Open positions: **1 / 8** (strategy v0.4 max-concurrent 4 → 1/4 used; BTC-cluster 1/2 used).
Breakeven ratchet (W22-H-partial): SOL +1.87R at wake ($78.64 close), needs 1H close ≥ +2R = $78.878 to arm. **Not yet armed**; peak 1H close so far = $78.64 (bar 07-02T03:00Z). Gap to arm = $0.24. Intrabar touched +2R at $78.88 (07-01T22:00Z) and $78.87 (07-02T03:00Z) but neither bar closed above threshold — 3rd instance of the intrabar-touch-close-misses pattern flagged in [[lesson 2026-06-29 W22-H ratchet]].

## EOD snapshot — 2026-07-01 PT Wed 21:00 PT (fired 04:11Z on-cron)

| Metric | Value |
|---|---|
| Wake type | routine-03-eod (Wed 21:00 PT ON-SCHEDULE M-F cron, PT date 2026-07-01, wall-clock UTC 2026-07-02T04:11Z) |
| Entries this wake | **0** (7 TECH-PASS ex-SOL rule-8 fallback candidates BTC/ETH/XRP/ADA/NEAR/SUI/LTC all cash-insufficient — reinforces [[P-W26-CASHFIT]]) |
| Exits this wake | 0 (SOL above stop $73.59 by $5.05, above 20-EMA $76.93 by $1.71, not at 4R target, ratchet not armed) |
| Day-to-date P&L (PT 2026-07-01) | **+$290.33 / +2.83%** vs prior EOD $10,267.22 (all unrealized SOL mark-up, no realized closes) |
| Wake-over-wake P&L | **+$153.25 / +1.47%** (SOL close $76.89 → $78.64 = +$1.75 × 87.5709 = +$153.25 MTM) |
| Equity (cash + MTM) | **$10,557.55** ($3,670.97 cash + $6,886.58 SOL MTM) |
| Equity peak | $10,875.85 (unchanged; need +$318.30 to retake) |
| Drawdown from peak | **2.93%** (compressed 1.41pp from 4.34% at prior wake) |
| Loss streak | 0 trading days (unchanged) |
| Trades today | 0 opened, 0 closed |

## Active kill-switch state

- Daily realized + unrealized PT 2026-07-01: **+$290.33 / +2.83%** of equity — CLEAR (positive; 5.00% loss cap → 7.83pp headroom to loss cap).
- Consecutive losing trading days: **0** (cap 7, full 7-day headroom). CLEAR.
- Max drawdown: **2.93%** from peak $10,875.85 (cap 25%, warn 12.5%, **9.57pp to warn**) — CLEAR.
- Equity floor: $10,557.55 > $7,500 floor — CLEAR.
- MCP availability: Kraken OK (`kraken_multi_ticker` + `kraken_ohlcv` + `indicators.py` all returned data). CLEAR.
- Regime gate (rule 5a): **PASS 12/15 positive median +2.46%** per `scripts/indicators.py` at 04:11:38Z (authoritative source). HYPE/FARTCOIN/TRX the 3 negatives.
- Regime sub-state (rule 5a-SBD): **CLEAR** (12 positives ≫ 1 ceiling; median +2.46% ≫ −1.0% floor).
- Active 5b cooldowns: **none**.
- Cluster cap (rule 6a, BTC-cluster): **1/2** used (SOL). Full headroom left = 1 more slot.
- **All Ring 3 kill switches CLEAR.** Routine-03-eod 2026-07-02T04:11Z: **0 entries, 0 exits, 1 open at wake / 1 open after**.

## Universe (unchanged since 2026-07-01 refresh)

Top 15 by 30d notional per `memory/universe.md` (refreshed at 07-01 overnight; next refresh 2026-08-01):

BTC, ETH, SOL, HYPE, XRP, ADA, NEAR, SUI, TAO, XDG, LTC, AVAX, LINK, ONDO, TRX.

## Pending exit triggers

**SOL/USD long** — exit conditions checked at each 1H close:
- Exit 1 (W22-G): two consecutive 1H closes < 20-EMA (~$76.93 at last close). Currently 1H close $78.64 is $1.71 above; trigger requires 2 consecutive closes < ~$76.93.
- Exit 1-SBD (only if regime flips back to SBD): two consecutive 1H closes < 9-EMA. Currently inactive (regime PASS).
- Exit 2 (stop-hit): active stop $73.5918 (2×ATR14 at entry). Ratchet inactive until +2R close ≥ $78.878. Gap to arm = $0.24.
- Exit 3 (take-profit): 4R = $82.4019 (peak intrabar so far $78.88 at bar 07-01T22:00Z, gap $3.52).

Next entry-eligible scan: routine-01-overnight Thu 2026-07-02 06:00 PT (= 13:00Z Thu). Cluster 1/2 used, so 1 more cluster slot available; position cap 1/4, so 3 more slots. Gated by regime and per-pair TECH-PASS. **Cash-fit constraint remains dominant** (this EOD: BTC/ETH/XRP/ADA/NEAR/SUI/LTC all TECH-PASS but all REJECTED cash-insufficient) — unless SOL closes (freeing cash) or a low-vol pair passes tech at a stop distance small enough to fit at $3,670 cash with 1.5% risk sizing.

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | ≈ +1.4% (equity 06-24 ~$10,414 → today $10,557.55 MTM) | ≈ −0.7% est (BTC 06-24 ~$61.3k → today $60.9k) | ≈ +2.1% est | BULL ahead 7d |
| 30d | ≈ +5.58% (inception $10k 2026-04-20; MTM $10,557.55) | ≈ −21% est (BTC 30d ago ~$77k → today $60.9k) | ≈ +27% est | BULL well ahead |
| 90d | — | — | — | not computable (BULL inception 2026-04-20 = 73 days ago; window first computable ~2026-07-19) |

(BTC tick read $60,854.2 live (multi-ticker) this wake, `indicators.py` 1H close $60,986.)
