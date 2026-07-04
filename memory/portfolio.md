# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-07-04T20:00Z routine-02-midday (PT Sat 2026-07-04 13:00, **OFF-SCHEDULE Sat fire** — cron `0 13 * * 1-5` is M-F but routine markdown has no day-gate; same off-schedule pattern as this morning's routine-01 fire). **0 trade events this wake.** ETH position 21h old; 20 post-entry 1H bars closed (07-04T00Z→19Z). Kraken `kraken_multi_ticker` (ETH last $1,793.45, 24h +2.12%, high $1,805.52, low $1,742.93) + `kraken_ohlcv` (50× ETH 1H) at 20:00Z. Watchdog not re-run this wake (midday lean-mode; carry-over 8 findings from overnight still stand). **Post-close exit check on ETH/USD (last closed 1H bar 07-04T19:00Z close $1,791.33)**: (i) **1H 20-EMA arithmetic α=2/21 seeded SMA(20) closes 07-03 04Z→07-03 23Z = $1,735.24, forward-marched through 20 bars 07-04 00Z→19Z with the α recursion; EMA at last closed bar 19:00Z = $1,769.27** (R1 PASS +$22.06), last close $1,791.33 = $22.06 above EMA; second-most-recent close $1,792.31 (07-04T18:00Z), EMA at that bar $1,767.02 → $25.29 above EMA → **Exit 1 two-bar confirmation NOT triggered** (both closes well above EMA; trend intact after 15Z-17Z impulse push); (ii) **stop-hit check** since 07-03T23:00Z entry: 20 bar lows (min $1,742.93 at 07-04T02:00Z, unchanged from overnight; recent 3 bar lows 17-19Z were $1,777.69, $1,790.66, $1,787.22 all well above stop) vs stop $1,728.5520 → min headroom $14.38 (worst since entry), current-bar headroom $58.67 — **Exit 2 NOT triggered**; (iii) **4R target check** ($1,870.5820 close basis): highest post-entry 1H close $1,797.82 (07-04T17:00Z bar), highest intrabar high $1,805.52 (same bar) → **Exit 3 NOT triggered**, gap $72.76 on close basis (narrowed from prior $85.01 by 07-04T17:00Z impulse; gap **narrowed $12.25** since overnight); (iv) **breakeven ratchet** arm level +2R close ≥ $1,813.7700: peak close $1,797.82 = +1.4385R (arm-level $15.95 above peak close, closest ETH has come; narrowed from $24.18 at overnight); intrabar peak $1,805.52 = +1.7096R still below +2R arm → **NOT armed**. **Midday routine — NO ENTRY SCAN** per routine spec (position management only; entries reserved for #1 Overnight and #3 EOD). MTM: ETH 5.7481 × $1,793.45 last ticker = **$10,308.93** (vs entry basis 5.7481 × $1,756.958 = $10,099.19; gross unrealized +$209.76; net after $26.26 already-booked open comm = +$183.50 cash-equivalent). **NEW EQUITY PEAK $11,068.89** clears prior peak $11,023.59 (set this morning 07-04T17:00Z overnight also from ETH MTM) by **+$45.30 / +0.41%** — second-consecutive wake setting a paper-only ETH-MTM equity peak; still dependent on ETH holding ≥ ~$1,769.48 (updated peak-defense level) at each future MTM mark. Fourth all-time equity peak (06-13 TAO $10,875.85 → 07-03 SOL $10,885.39 → 07-04T17Z ETH $11,023.59 → 07-04T20Z ETH $11,068.89, all-ETH-MTM back-to-back).

> **Prior rebuilds:** 2026-07-04T17:00Z routine-01-overnight (PT Sat 10:00 OFF-SCHEDULE Sat, 0/0, ETH held +1.148R peak-close unrealized 18h post-entry, stop $14 headroom EMA $25 headroom, arm-level $24 above peak close, 6 TECH-PASS all cash-rejected 9th consec incl. first LINK R4a PASS at rank 13, ADA R2a RSI 83.6 climactic reject, DD 0.00% new peak $11,023.59); 2026-07-04T04:10Z routine-03-eod (PT Fri 21:10 ON-SCHEDULE M-F, PT date 2026-07-03, 0/0, ETH held -0.17R unrealized 5h post-entry, stop $14 headroom EMA $12 headroom, 8 TECH-PASS all cash-rejected 8th consec, +0.93% day from SOL 4R morning realization, DD 0.49%); 2026-07-03T23:15Z routine-02-midday (PT Fri 16:15, ~3h15m late vs nominal 20:00Z; same-wake window as overnight 23:01Z 14 min prior; 0/0, ETH held -0.03R unrealized 43min post-entry, stop 4.92 headroom, silent wake); 2026-07-03T23:01Z routine-01-overnight (PT Fri 16:01, ~10h late; 1 CLOSE SOL 4R +$598.56/+3.88R + 1 OPEN ETH rule-8-fallback @ $1,756.9580; equity peak set $10,885.39 clearing 06-13 TAO peak by +$9.54; 2nd 4R take-profit inception-to-date, 1st post-W22-H ratchet-arm proof-of-mechanism); 2026-07-03T04:11Z routine-03-eod (Thu 21:00 PT ON-SCHEDULE M-F, PT date 2026-07-02, 0/0, SOL held +2.92R unrealized, 9 TECH-PASS all cash-rejected 7th consec, DD 1.32%); 2026-07-02T20:00Z routine-02-midday (Thu 13:00 PT ON-SCHEDULE M-F, 0/0, SOL held +2.99R unrealized, DD 1.20%).

## Account

- Starting equity: **$10,000.00**
- Cash: **$759.96** (unchanged from overnight; no OPEN/CLOSE this wake)
- Realized PnL (all-time): **+$885.36** (unchanged; last realized was SOL 4R exit 07-03T20:00Z)
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
- Unrealized PnL (open positions): **+$209.76 gross / +$183.50 net** (ETH 5.7481 × ($1,793.45 − $1,756.9580) = +$209.76 gross MTM; overnight entry commission $26.26 already booked at open, so cash-equivalent unrealized = +$183.50)
- Position values: **$10,308.93** (ETH 5.7481 × $1,793.45 ticker last at 20:00Z = $10,308.93 MTM)
- Current equity (cash + MTM): **$11,068.89** (= $759.96 cash + $10,308.93 ETH MTM; wake-over-wake PnL = **+$45.30 / +0.41%** vs prior overnight $11,023.59, driven by ETH mark $1,785.57 (07-04T16Z close, used at overnight) → $1,793.45 = +$7.88/share × 5.7481)
- Equity peak: **$11,068.89** (**NEW PEAK set this wake**; clears prior $11,023.59 from 07-04T17:00Z overnight-wake mark by +$45.30 / +0.41%; second consecutive paper-only equity peak set by open-position MTM rather than realized exit)
- Drawdown from peak: **0.000%** (peak set this bar; 12.50pp headroom to 12.5% warn cap)
- Since-inception return: **+10.69%** ($11,068.89 / $10,000 − 1)

## Open positions

| Pair | Side | Size | Entry | Stop | Target | Notional | Risk-at-moment | Cluster | Entered |
|------|------|------|-------|------|--------|----------|----------------|---------|---------|
| ETH/USD | long | 5.7481 | $1,756.9580 | $1,728.5520 | $1,870.5820 | $10,308.93 | ~$163.28 / 1.48% | BTC-cluster (1/2) | 2026-07-03T23:00Z |

Portfolio risk-at-moment: **~1.48%** of equity (single ETH position; risk denominator moved as equity grew). Cap 4% → 2.52pp headroom.
Open positions: **1 / 8** (strategy v0.4 max-concurrent 4 → 1/4 used; BTC-cluster 1/2 used).
Breakeven ratchet (W22-H-partial): NOT armed on ETH (peak close +1.4385R vs +2R arm threshold; peak intrabar +1.7096R at 07-04T17Z bar high $1,805.52; arm level close ≥ $1,813.7700, currently $15.95 above peak close). Would arm on any 1H close ≥ $1,813.7700.
**Peak-defense level (informational)**: ETH close/mark ≥ ~$1,769.48 required to preserve $11,068.89 equity peak on future MTM marks (below this, next wake will show DD from peak > 0.00%).

## Midday snapshot — 2026-07-04 PT Sat 13:00 (fired 20:00Z 07-04, OFF-SCHEDULE Sat)

| Metric | Value |
|---|---|
| Wake type | routine-02-midday (bull-02-midday slot, PT date 2026-07-04, wall-clock UTC 2026-07-04T20:00Z, OFF-SCHEDULE Sat — cron M-F, no day-gate in markdown) |
| Entries this wake | 0 (midday spec: NO new entries — position management only) |
| Exits this wake | 0 (ETH: stop $58.67 headroom on last close, EMA $22.06 above on last close, 4R target $72.76 above) |
| Stop-management events | 0 (ratchet arm level $1,813.77 is $15.95 above peak close $1,797.82; peak unrealized R = +1.4385R at 07-04T17:00Z close) |
| Wake-over-wake P&L | **+$45.30 / +0.41%** vs prior overnight $11,023.59 (ETH MTM +$7.88/share × 5.7481 over 3h — 16Z close $1,785.57 → 20Z ticker $1,793.45) |
| Equity (cash + MTM) | **$11,068.89** ($759.96 cash + $10,308.93 ETH MTM) |
| Equity peak | **$11,068.89 (NEW; +$45.30 vs prior)** |
| Drawdown from peak | **0.000%** (peak set this bar) |
| Loss streak | 0 trading days (positive open MTM) |
| Trades today | 0 opened, 0 closed this wake (running week: 1 OPEN 1 CLOSE on 07-03) |

## Active kill-switch state

- Daily realized + unrealized PT 2026-07-04: **+$236.65 / +2.19%** of equity (vs prior EOD $10,832.24) — CLEAR (positive; 5.00% loss cap → 7.19pp headroom to loss cap).
- Consecutive losing trading days: **0** (cap 7, full 7-day headroom). CLEAR.
- Max drawdown: **0.000%** from new peak $11,068.89 (cap 25%, warn 12.5%, **12.50pp to warn**) — CLEAR.
- Equity floor: $11,068.89 > $7,500 floor — CLEAR.
- MCP availability: Kraken OK (`kraken_multi_ticker` returned ETH ticker; `kraken_ohlcv` returned 50 ETH 1H bars). CLEAR.
- Regime gate (rule 5a): NOT re-scored this wake (midday spec: position management only; last authoritative read overnight 17:00Z = 13/15 positive median +1.82% PASS). CLEAR by inheritance.
- Regime sub-state (rule 5a-SBD): NOT re-scored (inherited CLEAR from overnight).
- Active 5b cooldowns: **none** (last stop-out 2026-06-27T19:00Z SOL cooldown lapsed 2026-06-28T19:00Z).
- Cluster cap (rule 6a, BTC-cluster): **1/2** used (ETH). Full headroom left = 1 more slot.
- **All Ring 3 kill switches CLEAR.** Routine-02-midday 2026-07-04T20:00Z: **0 entries, 0 exits, 1 open at wake / 1 open after** (unchanged); **NEW EQUITY PEAK $11,068.89 set this wake** (2nd consecutive wake setting new peak via ETH MTM).

## Universe (unchanged since 2026-07-01 refresh)

Top 15 by 30d notional per `memory/universe.md` (refreshed at 07-01 overnight; next refresh 2026-08-01):

BTC, ETH, SOL, HYPE, XRP, ADA, NEAR, SUI, TAO, XDG, LTC, AVAX, LINK, ONDO, TRX.

## Pending exit triggers

**ETH/USD long — active exits monitored at each 1H close:**
- Exit 1 (W22-G): two consecutive 1H closes < 20-EMA. Current 20-EMA at last closed bar (19:00Z) = $1,769.27; last close $1,791.33 is $22.06 above. Trigger requires 2 consecutive closes < ~$1,770 (level rising as trend persists).
- Exit 1-SBD (only if regime flips to SBD): two consecutive 1H closes < 9-EMA. Currently inactive (regime PASS inherited).
- Exit 2 (stop-hit): **initial 2×ATR stop $1,728.5520**. Post-open lowest low $1,742.93 (07-04T02:00Z bar, unchanged since overnight). Headroom from current mark $1,793.45 = $64.90.
- Exit 3 (take-profit): 4R = $1,870.5820. Distance from current mark $77.13 (+4.30% notional).
- Breakeven ratchet arm level: +2R close ≥ $1,813.7700 (currently $20.32 above current mark; $15.95 above peak close $1,797.82 = 07-04T17:00Z bar).

Next scheduled wake: routine-03-eod PT Sat 2026-07-04 21:00 = 07-05T04:00Z (OFF-SCHEDULE Sat as cron M-F, same as this wake) OR routine-01-overnight Sun 2026-07-05 06:00 PT. Cluster 1/2 used; position cap 1/4, 3 more slots. Gated by regime + per-pair TECH-PASS + cash-fit (cash $759.96 still binding on every low-notional pair under 1.5%-risk sizing).

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | ≈ +6.28% (equity 06-27 EOD ~$10,415 → today $11,068.89 MTM) | ≈ +4.02% est (BTC ~$60,437 → ~$62,867) | ≈ +2.26pp | BULL ahead 7d |
| 30d | ≈ +10.69% (inception $10k 2026-04-20; MTM $11,068.89) | ≈ −18.4% est (BTC 30d ago ~$77k → today ~$62.9k) | ≈ +29.1pp | BULL well ahead |
| 90d | — | — | — | not computable (BULL inception 2026-04-20 = 75 days ago; window first computable ~2026-07-19) |

(BTC last closed 1H ≈ $62,867 via overnight `scripts/indicators.py` reading; not re-pulled midday.)
