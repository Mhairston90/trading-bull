# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-07-03T23:15Z routine-02-midday (PT Fri 2026-07-03 16:15, cron slot `bull-02-midday` fired ~3h15m late vs nominal 13:00 PT / 20:00Z; same-wake window as the overnight fire at 23:01Z, 14 min prior). **0 trade events this wake** (midday is position-management-only per routine spec). ETH position 43 minutes old at midday check; only 1 post-entry 1H bar closed. Kraken `kraken_multi_ticker` returned ETH last $1,756.07 (24h +3.35%) — MTM update from $10,094.12 → $10,094.06 (delta −$0.06 from 1¢ tick down). Equity **$10,853.99** (−$0.09 wake-over-wake vs overnight $10,854.08). Peak $10,885.39 unchanged. DD **0.29%** unchanged. All Ring 3 kill switches CLEAR (12.21pp headroom to 12.5% warn). No exits triggered: stop $1,728.5520 has $24.92 low-of-bar headroom (23:00Z bar low $1,753.47); 20-EMA $1,735.19 has $20.88 close-to-EMA headroom; 4R target $1,870.5820 is $114.51 above. Breakeven ratchet not armed (unrealized R ≈ −0.03R, arm level +2R = $1,813.77, $57.70 above). Silent — no Telegram triggers.

> **Prior rebuilds:** 2026-07-03T23:01Z routine-01-overnight (PT Fri 16:01, ~10h late vs 06:00 PT nominal; 1 CLOSE SOL 4R +$598.56/+3.88R + 1 OPEN ETH rule-8-fallback @ $1,756.9580; equity peak set $10,885.39 clearing 06-13 TAO peak by +$9.54; 2nd 4R take-profit inception-to-date, 1st post-W22-H ratchet-arm proof-of-mechanism); 2026-07-03T04:11Z routine-03-eod (Thu 21:00 PT ON-SCHEDULE M-F, PT date 2026-07-02, 0/0, SOL held +2.92R unrealized, 9 TECH-PASS all cash-rejected 7th consec, DD 1.32%, +4R intrabar-touch/close-miss 1st Exit-3 instance); 2026-07-02T20:00Z routine-02-midday (Thu 13:00 PT ON-SCHEDULE M-F, 0/0, SOL held +2.99R unrealized, DD 1.20%); 2026-07-02T13:07Z routine-01-overnight (Thu 06:00 PT ON-SCHEDULE M-F, 0/0, W22-H breakeven ratchet ARMED on SOL at 07-02T09:00Z close $79.40 = +2.30R, stop $73.5918→$75.3538, 10 TECH-PASS all cash-rejected, DD 0.77%, +4R intrabar-touch/close-miss 1st instance); 2026-07-02T04:11Z routine-03-eod (Wed 21:00 PT ON-SCHEDULE, 0/0, SOL held +1.87R unrealized, 7 TECH-PASS all cash-rejected, DD 2.93%); 2026-07-01T20:00Z routine-02-midday (Wed 13:00 PT ON-SCHEDULE M-F, 0/0, SOL held +0.87R unrealized, DD 4.34%).

## Account

- Starting equity: **$10,000.00**
- Cash: **$759.96** (unchanged from overnight post-SOL exit +$7,214.42 net, post-ETH entry −$10,125.43)
- Realized PnL (all-time): **+$885.36** (unchanged; +$598.56 from SOL 4R exit this wake)
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
  - SOL +$598.56 (exit-4R-target-missed-scheduler-replay 2026-07-03T20:00Z, +3.88R net)
- Unrealized PnL (open positions): **−$5.11** (ETH 5.7481 × ($1,756.07 − $1,756.9580) = −$5.11; overnight entry commission $26.26 already booked at open)
- Position values: **$10,094.06** (ETH 5.7481 × $1,756.07 last-tick 07-03T23:00Z = $10,094.06 MTM)
- Current equity (cash + MTM): **$10,853.99** (= $759.96 cash + $10,094.06 ETH MTM; wake-over-wake PnL = −$0.09 from overnight $10,854.08, sub-cent price tick)
- Equity peak: **$10,885.39** (unchanged; set 2026-07-03T20:00Z post-SOL-exit all-cash mark)
- Drawdown from peak: **0.29%** ($31.40 below peak; unchanged from overnight mark)
- Since-inception return: **+8.54%** ($10,853.99 / $10,000 − 1)

## Open positions

| Pair | Side | Size | Entry | Stop | Target | Notional | Risk-at-moment | Cluster | Entered |
|------|------|------|-------|------|--------|----------|----------------|---------|---------|
| ETH/USD | long | 5.7481 | $1,756.9580 | $1,728.5520 | $1,870.5820 | $10,094.06 | ~$163.28 / 1.50% | BTC-cluster (1/2) | 2026-07-03T23:00Z |

Portfolio risk-at-moment: **~1.50%** of equity (single ETH position; unchanged). Cap 4% → 2.50pp headroom.
Open positions: **1 / 8** (strategy v0.4 max-concurrent 4 → 1/4 used; BTC-cluster 1/2 used).
Breakeven ratchet (W22-H-partial): NOT armed on ETH (unrealized R ≈ −0.03R, far from +2R threshold). Would arm on any 1H close ≥ $1,756.9580 + 2 × $28.406 = $1,813.7700.

## Midday snapshot — 2026-07-03 PT Fri 16:15 PT (fired 23:15Z, ~3h15m late vs 13:00 PT nominal; same-wake window as overnight 14 min prior)

| Metric | Value |
|---|---|
| Wake type | routine-02-midday (bull-02-midday slot, PT date 2026-07-03, wall-clock UTC 2026-07-03T23:15Z, ~3h15m late vs nominal 20:00Z fire; same-wake window as overnight 23:01Z) |
| Entries this wake | 0 (midday non-entering per routine spec) |
| Exits this wake | 0 (ETH stop $1,728.5520 not touched; 23:00Z bar low $1,753.47 has $24.92 headroom; 20-EMA $1,735.19 has $20.88 headroom; 4R target $1,870.5820 is $114.51 above) |
| Stop-management events | 0 (ratchet arm level $1,813.77 is $57.70 above current close; unrealized R ≈ −0.03R) |
| Day-to-date P&L (PT 2026-07-03) | **+$121.30 / +1.13%** (unchanged from overnight; ETH marked −$0.06 tick this wake; day P&L still dominated by SOL 4R realization booked at 20:00Z bar) |
| Wake-over-wake P&L | **−$0.09 / −0.001%** vs overnight $10,854.08 (ETH 1¢ tick down × 5.7481 size = −$0.06 MTM, plus reconciliation rounding) |
| Equity (cash + MTM) | **$10,853.99** ($759.96 cash + $10,094.06 ETH MTM) |
| Equity peak | **$10,885.39** (unchanged) |
| Drawdown from peak | **0.29%** (unchanged) |
| Loss streak | 0 trading days (unchanged; today +1.13%) |
| Trades today | 1 opened (ETH), 1 closed (SOL 4R) — unchanged from overnight |

## Active kill-switch state

- Daily realized + unrealized PT 2026-07-03: **+$121.30 / +1.13%** of equity — CLEAR (positive; 5.00% loss cap → 6.13pp headroom to loss cap).
- Consecutive losing trading days: **0** (cap 7, full 7-day headroom). CLEAR.
- Max drawdown: **0.29%** from peak $10,885.39 (cap 25%, warn 12.5%, **12.21pp to warn**) — CLEAR.
- Equity floor: $10,853.99 > $7,500 floor — CLEAR.
- MCP availability: Kraken OK (`kraken_multi_ticker` + `kraken_ohlcv` returned data this wake). CLEAR.
- Regime gate (rule 5a): not re-checked at midday (position-management-only routine, no entries).
- Regime sub-state (rule 5a-SBD): not re-checked at midday.
- Active 5b cooldowns: **none** (SOL exit was 4R take-profit, not stop-hit).
- Cluster cap (rule 6a, BTC-cluster): **1/2** used (ETH). Full headroom left = 1 more slot.
- **All Ring 3 kill switches CLEAR.** Routine-02-midday 2026-07-03T23:15Z: **0 entries, 0 exits, 1 open at wake / 1 open after** (unchanged).

## Universe (unchanged since 2026-07-01 refresh)

Top 15 by 30d notional per `memory/universe.md` (refreshed at 07-01 overnight; next refresh 2026-08-01):

BTC, ETH, SOL, HYPE, XRP, ADA, NEAR, SUI, TAO, XDG, LTC, AVAX, LINK, ONDO, TRX.

## Pending exit triggers

**ETH/USD long — active exits monitored at each 1H close:**
- Exit 1 (W22-G): two consecutive 1H closes < 20-EMA (last-20-close SMA ≈ $1,735.19). Current 1H close $1,756.07 is $20.88 above; trigger requires 2 consecutive closes < ~$1,735.
- Exit 1-SBD (only if regime flips to SBD): two consecutive 1H closes < 9-EMA. Currently inactive (regime PASS 15/15 at overnight).
- Exit 2 (stop-hit): **initial 2×ATR stop $1,728.5520**. Post-open lowest low $1,753.47 (23:00Z bar). Headroom from current close $1,756.07 = $27.52.
- Exit 3 (take-profit): 4R = $1,870.5820. Distance from current close $114.51 (+6.52% notional).
- Breakeven ratchet arm level: +2R close ≥ $1,813.7700 (currently $57.70 below).

Next scheduled wake: routine-03-eod Fri 2026-07-03 21:00 PT = 07-04T04:00Z (entry-eligible). Cluster 1/2 used, so 1 more cluster slot available; position cap 1/4, so 3 more slots. Gated by regime + per-pair TECH-PASS + cash-fit (cash $759.96 tight; only low-notional pairs would fit under 1.5%-risk sizing).

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | ≈ +4.23% (equity 06-26 EOD $10,413.87 → today $10,853.99 MTM) | ≈ +3.46% est (BTC 06-26 ~$60,449 → today $62,496.9) | ≈ +0.77pp | BULL ahead 7d |
| 30d | ≈ +8.54% (inception $10k 2026-04-20; MTM $10,853.99) | ≈ −19% est (BTC 30d ago ~$77k → today $62.5k) | ≈ +27.5pp | BULL well ahead |
| 90d | — | — | — | not computable (BULL inception 2026-04-20 = 74 days ago; window first computable ~2026-07-19) |

(BTC last tick $62,496.9 via `kraken_multi_ticker`, 24h +1.65%.)
