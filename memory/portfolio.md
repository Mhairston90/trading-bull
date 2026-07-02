# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-07-02T13:07Z routine-01-overnight (PT Thu 2026-07-02 06:07 ON-SCHEDULE M-F cron `0 6 * * 1-5`, 7-min execution latency; PT date label 2026-07-02 per date-labeling guard). **0 OPEN / 0 CLOSE this wake — MILESTONE: W22-H breakeven ratchet ARMED on SOL/USD open.** First qualifying +2R 1H close occurred at bar 2026-07-02T09:00Z ($79.40 = +2.30R). **Active stop moved from $73.5918 to $75.3538 (entry breakeven)** per strategy v0.4 stop-management ratchet-up-only rule; risk-at-moment for SOL is now ~$0.00. Break-the-pattern moment: prior 3 SOL trades (06-22, 06-29, 07-01 EOD) all missed the +2R close threshold by <0.5R, per [[lesson 2026-06-29 W22-H ratchet]]; today's 4th attempt cleared decisively. Additionally, **intrabar $82.65 at 07-02T11:00Z exceeded the +4R target $82.4019 by $0.248**, but the bar closed $82.30 = $0.10 short of the +4R close threshold → **Exit-3 not triggered** (1st instance of the intrabar-touch/close-miss pattern at the +4R take-profit level; 4th aggregate instance across both close-basis exit gates in ~11 days). Entry scan: regime 5a **PASS 15/15 positive median +5.77%** (best print since 2026-05-11 rally window), SBD **CLEAR**; **10 non-open TECH-PASS candidates (BTC/ETH/HYPE/XRP/ADA/NEAR/SUI/TAO/LTC/LINK)** — **ALL 10 REJECTED by cash-insufficient** at 1.5%-risk sizing vs $3,670.97 cash (widest-hit cash-fit instance to date; 7th binding recurrence W24-W27). Reinforces [[P-W26-CASHFIT]] pending user Y/N — routine #4 W27 (Sat 2026-07-04) will re-raise. Equity MTM **$10,792.63** (+$235.08 / +2.23% wake-over-wake, all unrealized SOL mark-up). DD **0.77%** (compressed 2.16pp from 2.93%; best DD reading since equity peak set 2026-06-13). All Ring 3 kill switches CLEAR. Watchdog 8 findings (routine-07 116h stale carry-over + 6 stale-MTM variants + 1 dirty-tree scripts/ carry-over — root cause routine-07 has not run in 5+ days).

> **Prior rebuilds:** 2026-07-02T04:11Z routine-03-eod (Wed 21:00 PT ON-SCHEDULE, PT date 2026-07-01, 0/0, SOL held +1.87R unrealized, 7 TECH-PASS all cash-rejected, DD 2.93%); 2026-07-01T20:00Z routine-02-midday (Wed 13:00 PT ON-SCHEDULE M-F, 0/0, SOL held +0.87R unrealized, DD 4.34%); 2026-07-01T15:52Z routine-01-overnight (Wed 06:00 PT slot ~2h52m late fire, 0/0, regime PASS 13/15 SBD CLEAR, SOL held +0.86R unrealized, universe refresh ONDO in / FARTCOIN out); 2026-07-01T04:12Z routine-03-eod (Tue 21:00 PT ON-SCHEDULE M-F, PT date 2026-06-30, 1 entry SOL/USD 87.5709 @ $75.3538 / 0 exits, rule-8 winner over HYPE/SUI/ADA/LTC, regime flipped back PASS 9/15 SBD CLEAR); 2026-06-30T20:00Z routine-02-midday (Tue 13:00 PT ON-SCHEDULE M-F, 0/0, flat, regime FAIL 1/15 SBD ACTIVE); 2026-06-30T15:07Z routine-01-overnight (Tue 06:00 PT slot ~2h7m late fire, 0/0, regime FAIL 0/15 SBD ACTIVE).

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
- Unrealized PnL (open positions): **+$522.42** (SOL 87.5709 × ($81.32 − $75.3538) = 87.5709 × $5.9662 = +$522.42 gross; entry commission $17.16 already booked at open)
- Position values: **$7,121.66** (SOL 87.5709 × $81.32 last 1H close 07-02T12:00Z = $7,121.66 MTM)
- Current equity (cash + MTM): **$10,792.63** (= $3,670.97 cash + $7,121.66 SOL MTM; wake-over-wake PnL = +$235.08 from $10,557.55 prior rebuild)
- Equity peak: **$10,875.85** (set 2026-06-13T09:00Z at TAO 4R close — unchanged)
- Drawdown from peak: **0.77%** ($83.22 below peak; compressed 2.16pp from 2.93% at prior wake; **best DD reading since peak-set on 2026-06-13**)
- Since-inception return: **+7.93%** ($10,792.63 / $10,000 − 1)

## Open positions

| Pair | Side | Size | Entry | Stop (RATCHETED) | Target | Notional | Risk-at-moment | Cluster | Entered |
|------|------|------|-------|------------------|--------|----------|----------------|---------|---------|
| SOL/USD | long | 87.5709 | $75.3538 | **$75.3538** (breakeven, ratchet armed 2026-07-02T09:00Z) | $82.4019 | $7,121.66 | **~$0.00 / 0.00%** | BTC-cluster (1/2) | 2026-07-01T04:00Z |

Portfolio risk-at-moment: **~0.00%** of equity (post-ratchet breakeven stop). Cap 4% → full headroom.
Open positions: **1 / 8** (strategy v0.4 max-concurrent 4 → 1/4 used; BTC-cluster 1/2 used).
Breakeven ratchet (W22-H-partial): **ARMED at 2026-07-02T09:00Z** (bar close $79.40 = +2.30R > +2R threshold $78.878 by $0.522). Active stop moved from $73.5918 → $75.3538. Post-arm peak 1H close = $82.30 at bar 07-02T11:00Z = +3.94R (short of +4R take-profit close threshold $82.4019 by $0.10; that bar's intrabar high $82.65 DID exceed the target by $0.248 but Exit-3 is 1H-close-only). Latest close $81.32 = +3.39R. Ratchet is up-only per strategy v0.4; will remain at $75.3538 for life of trade.

## Overnight snapshot — 2026-07-02 PT Thu 06:00 PT (fired 13:07Z on-cron)

| Metric | Value |
|---|---|
| Wake type | routine-01-overnight (Thu 06:00 PT ON-SCHEDULE M-F cron, PT date 2026-07-02, wall-clock UTC 2026-07-02T13:07Z, 7-min execution latency) |
| Entries this wake | **0** (10 non-open TECH-PASS candidates BTC/ETH/HYPE/XRP/ADA/NEAR/SUI/TAO/LTC/LINK all cash-insufficient at 1.5%-risk sizing — widest-hit cash-fit REJECT to date; reinforces [[P-W26-CASHFIT]]) |
| Exits this wake | 0 (SOL above breakeven $75.3538 by $5.97, above 20-EMA $78.694 by $2.63, intrabar $82.65 exceeded 4R target but bar closed $82.30 < $82.4019 by $0.10) |
| Stop-management events | **1 — W22-H breakeven ratchet ARMED** (bar 2026-07-02T09:00Z close $79.40 = +2.30R). Active stop $73.5918 → $75.3538. |
| Day-to-date P&L (PT 2026-07-02) | **+$235.08 / +2.23%** vs prior EOD $10,557.55 (all unrealized SOL mark-up, no realized closes) |
| Wake-over-wake P&L | **+$235.08 / +2.23%** (SOL close $78.64 → $81.32 = +$2.68 × 87.5709 = +$234.69 MTM) |
| Equity (cash + MTM) | **$10,792.63** ($3,670.97 cash + $7,121.66 SOL MTM) |
| Equity peak | $10,875.85 (unchanged; need +$83.22 to retake) |
| Drawdown from peak | **0.77%** (compressed 2.16pp from 2.93% at prior wake — best DD since peak-set on 2026-06-13) |
| Loss streak | 0 trading days (unchanged) |
| Trades today | 0 opened, 0 closed |

## Active kill-switch state

- Daily realized + unrealized PT 2026-07-02: **+$235.08 / +2.23%** of equity — CLEAR (positive; 5.00% loss cap → 7.23pp headroom to loss cap).
- Consecutive losing trading days: **0** (cap 7, full 7-day headroom). CLEAR.
- Max drawdown: **0.77%** from peak $10,875.85 (cap 25%, warn 12.5%, **11.73pp to warn**) — CLEAR.
- Equity floor: $10,792.63 > $7,500 floor — CLEAR.
- MCP availability: Kraken OK (`kraken_multi_ticker` + `kraken_ohlcv` + `indicators.py` all returned data). CLEAR.
- Regime gate (rule 5a): **PASS 15/15 positive median +5.77%** per `scripts/indicators.py` at 13:07:37Z (authoritative source). Universe-wide green; best regime print since 2026-05-11 rally window.
- Regime sub-state (rule 5a-SBD): **CLEAR** (15 positives ≫ 1 ceiling; median +5.77% ≫ −1.0% floor). SBD emphatically off.
- Active 5b cooldowns: **none**.
- Cluster cap (rule 6a, BTC-cluster): **1/2** used (SOL). Full headroom left = 1 more slot.
- **All Ring 3 kill switches CLEAR.** Routine-01-overnight 2026-07-02T13:07Z: **0 entries, 0 exits, 1 open at wake / 1 open after (ratchet-armed)**.

## Universe (unchanged since 2026-07-01 refresh)

Top 15 by 30d notional per `memory/universe.md` (refreshed at 07-01 overnight; next refresh 2026-08-01):

BTC, ETH, SOL, HYPE, XRP, ADA, NEAR, SUI, TAO, XDG, LTC, AVAX, LINK, ONDO, TRX.

## Pending exit triggers

**SOL/USD long — post-ratchet state:** exit conditions checked at each 1H close.
- Exit 1 (W22-G): two consecutive 1H closes < 20-EMA (~$78.694 at last close). Currently 1H close $81.32 is $2.63 above; trigger requires 2 consecutive closes < ~$78.694.
- Exit 1-SBD (only if regime flips back to SBD): two consecutive 1H closes < 9-EMA. Currently inactive (regime PASS 15/15).
- Exit 2 (stop-hit): **active stop $75.3538 (breakeven, post-ratchet)**. Ratchet armed 07-02T09:00Z; up-only, will not trail higher. Post-arm lowest low $79.32 = +$3.97 headroom.
- Exit 3 (take-profit): 4R = $82.4019 (missed by $0.10 on close 07-02T11:00Z at $82.30 despite intrabar high $82.65 = +$0.248 over target).

Next entry-eligible scan: routine-02-midday Thu 2026-07-02 13:00 PT (= 20:00Z Thu). Cluster 1/2 used, so 1 more cluster slot available; position cap 1/4, so 3 more slots. Gated by regime (currently PASS 15/15, very supportive) and per-pair TECH-PASS (10 candidates today, all cash-blocked). **Cash-fit constraint remains dominant** — unless SOL closes (freeing ~$7.1k cash) or a low-vol pair (LTC / XRP / XDG when it re-passes R3) passes tech at a stop distance small enough to fit at $3,670 cash with 1.5% risk sizing.

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | ≈ +3.7% (equity 06-25 ~$10,405 → today $10,792.63 MTM) | ≈ −0.5% est (BTC 06-25 ~$61,850 → today $61,533.4) | ≈ +4.2% est | BULL ahead 7d |
| 30d | ≈ +7.93% (inception $10k 2026-04-20; MTM $10,792.63) | ≈ −20% est (BTC 30d ago ~$77k → today $61.5k) | ≈ +28% est | BULL well ahead |
| 90d | — | — | — | not computable (BULL inception 2026-04-20 = 74 days ago; window first computable ~2026-07-19) |

(BTC tick read $61,533.4 live (multi-ticker) this wake, `indicators.py` 1H close $61,466.7.)
