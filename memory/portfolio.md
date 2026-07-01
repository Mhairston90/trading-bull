# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-07-01T20:00Z routine-02-midday (PT Wed 2026-07-01 13:00 ON-SCHEDULE M-F cron `0 13 * * 1-5`). **0 OPEN / 0 CLOSE this wake** — SOL/USD held through the midday check: all three exit paths passed (20-EMA ≈ $75.67, last 1H close $76.89 is $1.22 above; lowest low since entry $73.84 vs stop $73.5918, +25bps headroom; 4R target $82.4019 not hit, peak intrabar high $78.17). Breakeven ratchet **still inactive** — peak 1H close since entry = $77.68 at bar 17:00Z (+1.32R), needs 1H close ≥ $78.878 (+2R) to arm; gap to arm **$1.20**. Equity MTM $10,404.30 (+$1.50 wake-over-wake, +$137.08 / +1.33% day-to-date). DD 4.34% (compressed 0.01pp from overnight's 4.35%). All Ring 3 kill switches CLEAR. Midday spec followed — **no entry scan run** (position management only). Silent (no exits, no kill switch, no DD warn crossing).

> **Prior rebuilds:** 2026-07-01T15:52Z routine-01-overnight (Wed 06:00 PT slot ~2h52m late fire, 0/0, regime PASS 13/15 SBD CLEAR, SOL held +0.86R unrealized, universe refresh ONDO in / FARTCOIN out); 2026-07-01T04:12Z routine-03-eod (Tue 21:00 PT ON-SCHEDULE M-F, PT date 2026-06-30, 1 entry SOL/USD 87.5709 @ $75.3538 / 0 exits, rule-8 winner over HYPE/SUI/ADA/LTC, regime flipped back PASS 9/15 SBD CLEAR); 2026-06-30T20:00Z routine-02-midday (Tue 13:00 PT ON-SCHEDULE M-F, 0/0, flat, regime FAIL 1/15 SBD ACTIVE); 2026-06-30T15:07Z routine-01-overnight (Tue 06:00 PT slot ~2h7m late fire, 0/0, regime FAIL 0/15 SBD ACTIVE); 2026-06-30T10:30Z routine-03-eod (LATE FIRE Mon 21:00 PT slot — labeled PT 2026-06-29 Mon EOD — closed SOL/USD long +$74.48 / +0.49R net on Exit-1 two-bar EMA20 confirmation, ended day $10,286.93 / +0.91%); 2026-06-29T20:00Z routine-02-midday (held SOL +1.71R unrealized at tick $75.80, equity $10,458.97, DD 3.83%).

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
- Unrealized PnL (open positions): **+$134.53** (SOL 87.5709 × ($76.89 − $75.3538) = 87.5709 × $1.5362 = +$134.53 gross; entry commission $17.16 already booked at open)
- Position values: **$6,733.33** (SOL 87.5709 × $76.89 last 1H close = $6,733.33 MTM)
- Current equity (cash + MTM): **$10,404.30** (= $3,670.97 cash + $6,733.33 SOL MTM; wake-over-wake PnL = +$1.50 from $10,402.80 prior rebuild)
- Equity peak: **$10,875.85** (set 2026-06-13T09:00Z at TAO 4R close — unchanged)
- Drawdown from peak: **4.34%** ($471.55 below peak; compressed 0.01pp from 4.35% at prior wake)
- Since-inception return: **+4.04%** ($10,404.30 / $10,000 − 1)

## Open positions

| Pair | Side | Size | Entry | Stop | Target | Notional | Risk-at-moment | Cluster | Entered |
|------|------|------|-------|------|--------|----------|----------------|---------|---------|
| SOL/USD | long | 87.5709 | $75.3538 | $73.5918 | $82.4019 | $6,598.80 | 1.48% ($154.30 / $10,404.30) | BTC-cluster (1/2) | 2026-07-01T04:00Z |

Portfolio risk-at-moment: **1.48%** of equity. Cap 4% → 2.52pp headroom.
Open positions: **1 / 8** (strategy v0.4 max-concurrent 4 → 1/4 used; BTC-cluster 1/2 used).
Breakeven ratchet (W22-H-partial): SOL +0.87R at wake ($76.89 close), needs 1H close ≥ +2R = $78.878 to arm. **Not yet armed**; peak 1H close so far = $77.68 (bar 17:00Z). Gap to arm = $1.20.

## Midday snapshot — 2026-07-01 PT Wed 13:00 PT (fired 20:00Z on-cron)

| Metric | Value |
|---|---|
| Wake type | routine-02-midday (Wed 13:00 PT ON-SCHEDULE M-F cron, PT date 2026-07-01) |
| Entries this wake | 0 (midday spec = position management only, no entry scan) |
| Exits this wake | 0 (SOL above stop $73.59 by $3.30, above 20-EMA $75.67 by $1.22, not at 4R target, ratchet not armed) |
| Day-to-date P&L (PT 2026-07-01) | **+$137.08 / +1.33%** (unrealized SOL mark-up, no realized closes) |
| Wake-over-wake P&L | **+$1.50 / +0.01%** (SOL held roughly flat since overnight $76.87 close → midday $76.89 close) |
| Equity (cash + MTM) | **$10,404.30** ($3,670.97 cash + $6,733.33 SOL MTM) |
| Equity peak | $10,875.85 (unchanged; need +$471.55 to retake) |
| Drawdown from peak | **4.34%** (compressed 0.01pp from 4.35% at prior wake) |
| Loss streak | 0 trading days (unchanged) |
| Trades today | 0 opened, 0 closed |

## Active kill-switch state

- Daily realized + unrealized PT 2026-07-01: **+$137.08 / +1.33%** of equity — CLEAR (positive; 5.00% loss cap → 6.33pp headroom to loss cap).
- Consecutive losing trading days: **0** (cap 7, full 7-day headroom). CLEAR.
- Max drawdown: **4.34%** from peak $10,875.85 (cap 25%, warn 12.5%, **8.16pp to warn**) — CLEAR.
- Equity floor: $10,404.30 > $7,500 floor — CLEAR.
- MCP availability: Kraken OK (`kraken_multi_ticker` + `kraken_ohlcv` returned all pairs). CLEAR.
- Regime gate (rule 5a): **not re-scored** at midday per routine spec; last authoritative read `scripts/indicators.py` overnight 07-01T15:52Z = **PASS 13/15 SBD CLEAR**. Informational multi-ticker snapshot this wake = 14/15 positive 24h (only HYPE −2.83% negative), directionally consistent with PASS.
- Regime sub-state (rule 5a-SBD): last authoritative = **CLEAR**.
- Active 5b cooldowns: **none**.
- Cluster cap (rule 6a, BTC-cluster): **1/2** used (SOL). Full headroom left = 1 more slot.
- **All Ring 3 kill switches CLEAR.** Routine-02-midday 2026-07-01T20:00Z: **0 entries, 0 exits, 1 open at wake / 1 open after**.

## Universe (unchanged since 2026-07-01 refresh)

Top 15 by 30d notional per `memory/universe.md` (refreshed at 07-01 overnight; next refresh 2026-08-01):

BTC, ETH, SOL, HYPE, XRP, ADA, NEAR, SUI, TAO, XDG, LTC, AVAX, LINK, ONDO, TRX.

## Pending exit triggers

**SOL/USD long** — exit conditions checked at each 1H close:
- Exit 1 (W22-G): two consecutive 1H closes < 20-EMA (~$75.67 at last close). Currently 1H close $76.89 well above; trigger requires 2 consecutive closes < ~$75.67.
- Exit 1-SBD (only if regime flips back to SBD): two consecutive 1H closes < 9-EMA. Currently inactive (regime PASS).
- Exit 2 (stop-hit): active stop $73.5918 (2×ATR14 at entry). Ratchet inactive until +2R close ≥ $78.878.
- Exit 3 (take-profit): 4R = $82.4019 (peak intrabar so far $78.17 at bar 16:00Z, gap $4.23).

Next entry-eligible scan: routine-03-eod Wed 2026-07-01 21:00 PT (= 04:00Z Thu). Cluster 1/2 used, so 1 more cluster slot available; position cap 1/4, so 3 more slots. Gated by regime and per-pair TECH-PASS. **Cash-fit constraint remains dominant:** cash $3,671 too small for BTC/ETH sizing; SUI/ADA borderline; likely no new entry until SOL closes (freeing cash) unless a low-vol pair passes tech at a stop distance ≥ ~2.7% of price.

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | ≈ 0% (equity 06-24 ~$10,414 → today $10,404.30 MTM) | ≈ −2.0% est (BTC 06-24 ~$61.1k → today $59.9k) | ≈ +2.0% est | BULL ahead 7d |
| 30d | ≈ +4.04% (inception $10k 2026-04-20; MTM $10,404.30) | ≈ −22% est (BTC 30d ago ~$77k → today $59.9k) | ≈ +26% est | BULL well ahead |
| 90d | — | — | — | not computable (BULL inception 2026-04-20 = 73 days ago; window first computable ~2026-07-19) |

(BTC tick read $59,903.5 live (multi-ticker) this wake.)
