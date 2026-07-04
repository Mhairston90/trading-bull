# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-07-04T17:00Z routine-01-overnight (PT Sat 2026-07-04 10:00, **OFF-SCHEDULE Sat fire** — cron `0 6 * * 1-5` is M-F but routine markdown has no day-gate; nominal Sat routine-04 slot fires later today). **0 trade events this wake.** ETH position 18h old; 17 post-entry 1H bars closed (07-04T00Z→16Z). Kraken `kraken_ohlcv` (24× ETH 1H) + `scripts/indicators.py` full 15-pair authoritative table at 17:00:05Z. Watchdog 8 findings (carry-over class: 1× A routine-07 167h stale, 1× C dirty-tree 4 uncommitted files, 6× D stale-MTM variants 168h); Telegram auto-alert sent by watchdog. **Post-close exit check on ETH/USD (last closed 1H bar 07-04T16:00Z close $1,785.57)**: (i) **1H 20-EMA per indicators.py = $1,759.96** (R1 PASS +$25.61), last close $1,785.57 = $25.61 above EMA; second-most-recent close $1,789.59 (07-04T15:00Z) = $29.63 above EMA → **Exit 1 two-bar confirmation NOT triggered** (both last-two closes well above EMA); (ii) **stop-hit check** since 07-03T23:00Z entry: 17 bar lows (min $1,742.93 at 07-04T02:00Z) vs stop $1,728.5520 → min headroom $14.38, **Exit 2 NOT triggered**; (iii) **4R target check** ($1,870.5820): highest post-entry 1H close $1,789.59 (bar 07-04T15:00Z), highest intrabar $1,796.41 same bar → **Exit 3 NOT triggered**, gap $85.01 on close basis (narrowed from prior $113.51 by 07-04T15:00Z impulse); (iv) **breakeven ratchet** arm level +2R = $1,813.7700 close: peak close $1,789.59 = +1.148R (arm-level $24.18 above); intrabar peak $1,796.41 = +1.389R still below +2R → NOT armed. **Entry scan (W19-E analyst-role split)** per routine spec — **Technical (authoritative `scripts/indicators.py` at 17:00:05Z, 720 4H bars/pair)**: regime 5a **PASS 13/15 positive median +1.82%** (only NEAR −0.13%, FARTCOIN −1.44% negative), SBD **CLEAR** (13 positives ≫ 1 ceiling; median +1.82% ≫ −1.0% floor); TECH-PASS pairs (R1+R2+R2a+R3+R4a all PASS) = **BTC** (R1+$359.6, R2 RSI 66.0, R3 +$1,803, R4a $88.58M), **ETH** (R1+$25.61, R2 RSI 71.9, R3 +$128.1, R4a $30.20M — SKIP: rule 5 already open), **XRP** (R1+$0.02823, R2 RSI 76.4, R3 +$0.08375, R4a $36.61M), **SUI** (R1+$0.006587, R2 RSI 59.5, R3 +$0.04734, R4a $9.75M), **XDG** (R1+$0.00118, R2 RSI 68.4, R3 +$0.003224, R4a $6.19M), **LTC** (R1+$0.8038, R2 RSI 68.9, R3 +$2.004, R4a $3.36M), **LINK** (R1+$0.1343, R2 RSI 70.9, R3 +$0.4834, R4a $2.06M — first LINK R4a PASS at rank #13; scraped by $60k over $2M floor). REJECT reasons: SOL R2 FAIL RSI 53.6, HYPE R1 FAIL + R2 FAIL RSI 49.7, TAO R4a FAIL $1.89M, NEAR R4a FAIL $1.85M, ADA R2a FAIL RSI 83.6>80 climactic cap ([[W19-D]] triggered on +12.05% 24h move), FARTCOIN R1+R2 FAIL + R4a FAIL, TRX R4a FAIL $0.53M, AVAX R4a FAIL $1.58M. **News (informational)**: SKIPPED for all 6 non-open TECH-PASS candidates (cash-blocked deterministic; also 17Z Sat US July 4 holiday low-news window) → default NEUTRAL. **Sentiment (informational)**: not queried per-candidate (rule-8 winner deterministic on 30d rank). **Decision — Rule 8**: TECH-PASS winner order = **BTC (rank 1)** > **XRP (5)** > **SUI (8)** > **XDG (10)** > **LTC (11)** > **LINK (13)**. Sizing per strategy v0.4 (risk = 1.5% × equity $11,023.59 = $165.35; size = risk / 2×ATR14): **BTC** stop-dist $469.60, size 0.3521, notional $22,133.44 + comm $57.55 = **$22,190.99 > cash $759.96 → REJECT cash-insufficient**; **XRP** stop-dist $0.022479, size 7,355, notional $8,627.34 + $22.43 = **$8,649.77 → REJECT cash-insufficient**; **SUI** stop-dist $0.013164, size 12,561, notional $9,629.26 + $25.04 = **$9,654.30 → REJECT cash-insufficient** (would push cluster 2/2 but cash rejects first); **XDG** stop-dist $0.0011649, size 141,946, notional $11,128.95 + $28.94 = **$11,157.88 → REJECT cash-insufficient**; **LTC** stop-dist $0.69667, size 237, notional $10,736.10 + $27.91 = **$10,764.01 → REJECT cash-insufficient**; **LINK** stop-dist $0.1043, size 1,585, notional $12,805.86 + $33.30 = **$12,839.16 → REJECT cash-insufficient** (would push cluster 2/2). **All 6 rule-8 fallback candidates cash-rejected. 0 entries this wake.** **9th consecutive cash-binding wake W24-W27** (06-27 EOD 3× → 07-03 EOD 8× → this wake 6× rejects). P-W26-CASHFIT pending user `[Y/N]`. **NEW EQUITY PEAK $11,023.59** clears prior peak $10,885.39 (set 07-03T20:00Z SOL-exit all-cash) by **+$138.20 / +1.27%** — first paper-only equity peak set by open-position MTM (not realized exit); dependent on ETH holding ≥ ~$1,761.60 at each future MTM mark. Third all-time equity peak this month (06-13 TAO $10,875.85 → 07-03 SOL $10,885.39 → 07-04T17Z ETH-MTM $11,023.59).

> **Prior rebuilds:** 2026-07-04T04:10Z routine-03-eod (PT Fri 21:10 ON-SCHEDULE M-F, PT date 2026-07-03, 0/0, ETH held -0.17R unrealized 5h post-entry, stop $14 headroom EMA $12 headroom, 8 TECH-PASS all cash-rejected 8th consec, +0.93% day from SOL 4R morning realization, DD 0.49%); 2026-07-03T23:15Z routine-02-midday (PT Fri 16:15, ~3h15m late vs nominal 20:00Z; same-wake window as overnight 23:01Z 14 min prior; 0/0, ETH held -0.03R unrealized 43min post-entry, stop 4.92 headroom, silent wake); 2026-07-03T23:01Z routine-01-overnight (PT Fri 16:01, ~10h late; 1 CLOSE SOL 4R +$598.56/+3.88R + 1 OPEN ETH rule-8-fallback @ $1,756.9580; equity peak set $10,885.39 clearing 06-13 TAO peak by +$9.54; 2nd 4R take-profit inception-to-date, 1st post-W22-H ratchet-arm proof-of-mechanism); 2026-07-03T04:11Z routine-03-eod (Thu 21:00 PT ON-SCHEDULE M-F, PT date 2026-07-02, 0/0, SOL held +2.92R unrealized, 9 TECH-PASS all cash-rejected 7th consec, DD 1.32%); 2026-07-02T20:00Z routine-02-midday (Thu 13:00 PT ON-SCHEDULE M-F, 0/0, SOL held +2.99R unrealized, DD 1.20%); 2026-07-02T13:07Z routine-01-overnight (Thu 06:00 PT ON-SCHEDULE M-F, 0/0, W22-H breakeven ratchet ARMED on SOL at 07-02T09:00Z close $79.40 = +2.30R, stop $73.5918→$75.3538, 10 TECH-PASS all cash-rejected, DD 0.77%, +4R intrabar-touch/close-miss 1st instance); 2026-07-02T04:11Z routine-03-eod (Wed 21:00 PT ON-SCHEDULE, 0/0, SOL held +1.87R unrealized, 7 TECH-PASS all cash-rejected, DD 2.93%).

## Account

- Starting equity: **$10,000.00**
- Cash: **$759.96** (unchanged from overnight post-SOL-exit +$7,214.42 net, post-ETH-entry −$10,125.43)
- Realized PnL (all-time): **+$885.36** (unchanged; last realized was SOL 4R exit at prior overnight wake 07-03T20:00Z bar)
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
- Unrealized PnL (open positions): **+$164.46 gross / +$138.20 net** (ETH 5.7481 × ($1,785.57 − $1,756.9580) = +$164.46 gross MTM; overnight entry commission $26.26 already booked at open, so cash-equivalent unrealized = +$138.20)
- Position values: **$10,263.63** (ETH 5.7481 × $1,785.57 last-closed 1H 07-04T16:00Z = $10,263.63 MTM)
- Current equity (cash + MTM): **$11,023.59** (= $759.96 cash + $10,263.63 ETH MTM; wake-over-wake PnL = **+$191.35 / +1.77%** vs prior EOD $10,832.24, driven by ETH close $1,752.28 → $1,785.57 = +$33.29/share × 5.7481)
- Equity peak: **$11,023.59** (**NEW PEAK set this wake**; clears prior $10,885.39 from 07-03T20:00Z SOL-exit mark by +$138.20 / +1.27%; first paper-only equity peak set by open-position MTM rather than realized exit)
- Drawdown from peak: **0.000%** (peak set this bar; 12.50pp headroom to 12.5% warn cap)
- Since-inception return: **+10.24%** ($11,023.59 / $10,000 − 1)

## Open positions

| Pair | Side | Size | Entry | Stop | Target | Notional | Risk-at-moment | Cluster | Entered |
|------|------|------|-------|------|--------|----------|----------------|---------|---------|
| ETH/USD | long | 5.7481 | $1,756.9580 | $1,728.5520 | $1,870.5820 | $10,263.63 | ~$163.28 / 1.48% | BTC-cluster (1/2) | 2026-07-03T23:00Z |

Portfolio risk-at-moment: **~1.48%** of equity (single ETH position; risk denominator moved as equity grew). Cap 4% → 2.52pp headroom.
Open positions: **1 / 8** (strategy v0.4 max-concurrent 4 → 1/4 used; BTC-cluster 1/2 used).
Breakeven ratchet (W22-H-partial): NOT armed on ETH (peak close +1.148R vs +2R arm threshold; peak intrabar +1.389R). Would arm on any 1H close ≥ $1,813.7700 (currently $24.18 above peak close).
**Peak-defense level (informational)**: ETH close ≥ ~$1,761.60 required to preserve $11,023.59 equity peak on future MTM marks (below this, next wake will show DD from peak > 0.00%).

## Overnight snapshot — 2026-07-04 PT Sat 10:00 PT (fired 17:00Z 07-04, OFF-SCHEDULE Sat)

| Metric | Value |
|---|---|
| Wake type | routine-01-overnight (bull-01-overnight slot, PT date 2026-07-04, wall-clock UTC 2026-07-04T17:00Z, OFF-SCHEDULE Sat — cron M-F, no day-gate in markdown) |
| Entries this wake | 0 (all 6 rule-8 fallback candidates cash-rejected; 9th consecutive cash-binding wake) |
| Exits this wake | 0 (ETH: stop $14.38 headroom, EMA $25.61 close-to-EMA headroom on last close, 4R target $85.01 above) |
| Stop-management events | 0 (ratchet arm level $1,813.77 is $24.18 above current close; peak unrealized R = +1.148R at 07-04T15:00Z close $1,789.59) |
| Wake-over-wake P&L | **+$191.35 / +1.77%** vs prior EOD $10,832.24 (ETH MTM +$33.29/share × 5.7481 = +$191.35 over ~13h) |
| Equity (cash + MTM) | **$11,023.59** ($759.96 cash + $10,263.63 ETH MTM) |
| Equity peak | **$11,023.59 (NEW; +$138.20 vs prior)** |
| Drawdown from peak | **0.000%** (peak set this bar) |
| Loss streak | 0 trading days (positive open MTM) |
| Trades today | 0 opened, 0 closed this wake (running week: 1 OPEN 1 CLOSE on 07-03) |

## Active kill-switch state

- Daily realized + unrealized PT 2026-07-04: **+$191.35 / +1.77%** of equity — CLEAR (positive; 5.00% loss cap → 6.77pp headroom to loss cap).
- Consecutive losing trading days: **0** (cap 7, full 7-day headroom). CLEAR.
- Max drawdown: **0.000%** from new peak $11,023.59 (cap 25%, warn 12.5%, **12.50pp to warn**) — CLEAR.
- Equity floor: $11,023.59 > $7,500 floor — CLEAR.
- MCP availability: Kraken OK (`kraken_ohlcv` returned 24 ETH bars this wake; `scripts/indicators.py` produced full 15-pair table). CLEAR.
- Regime gate (rule 5a): **PASS** 13/15 positive median +1.82% per `scripts/indicators.py` (authoritative). CLEAR.
- Regime sub-state (rule 5a-SBD): **CLEAR** (13 positives ≫ 1; median +1.82% ≫ −1.0%).
- Active 5b cooldowns: **none** (SOL exit 07-03T20:00Z was 4R take-profit, not stop-hit; last stop-out 2026-06-27T19:00Z SOL cooldown lapsed 2026-06-28T19:00Z).
- Cluster cap (rule 6a, BTC-cluster): **1/2** used (ETH). Full headroom left = 1 more slot.
- **All Ring 3 kill switches CLEAR.** Routine-01-overnight 2026-07-04T17:00Z: **0 entries, 0 exits, 1 open at wake / 1 open after** (unchanged); **NEW EQUITY PEAK $11,023.59 set this wake**.

## Universe (unchanged since 2026-07-01 refresh)

Top 15 by 30d notional per `memory/universe.md` (refreshed at 07-01 overnight; next refresh 2026-08-01):

BTC, ETH, SOL, HYPE, XRP, ADA, NEAR, SUI, TAO, XDG, LTC, AVAX, LINK, ONDO, TRX.

## Pending exit triggers

**ETH/USD long — active exits monitored at each 1H close:**
- Exit 1 (W22-G): two consecutive 1H closes < 20-EMA ($1,759.96 per indicators.py). Current 1H close $1,785.57 is $25.61 above; trigger requires 2 consecutive closes < ~$1,760.
- Exit 1-SBD (only if regime flips to SBD): two consecutive 1H closes < 9-EMA. Currently inactive (regime PASS 13/15).
- Exit 2 (stop-hit): **initial 2×ATR stop $1,728.5520**. Post-open lowest low $1,742.93 (07-04T02:00Z bar). Headroom from current close $1,785.57 = $57.02.
- Exit 3 (take-profit): 4R = $1,870.5820. Distance from current close $85.01 (+4.76% notional).
- Breakeven ratchet arm level: +2R close ≥ $1,813.7700 (currently $28.20 below; peak close was $1,789.59 = $24.18 short of arm).

Next scheduled wake: routine-04-harness Sat 2026-07-04 08:00 PT = 07-04T15:00Z (already past — will fire late) OR routine-01-overnight Sun 2026-07-05 06:00 PT (OFF-SCHEDULE Sun same as this wake). Cluster 1/2 used; position cap 1/4, 3 more slots. Gated by regime + per-pair TECH-PASS + cash-fit (cash $759.96 still binding on every low-notional pair under 1.5%-risk sizing).

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | ≈ +5.85% (equity 06-27 EOD ~$10,415 → today $11,023.59 MTM) | ≈ +4.02% est (BTC 06-27 ~$60,437 → today $62,866.9 close-basis) | ≈ +1.83pp | BULL ahead 7d |
| 30d | ≈ +10.24% (inception $10k 2026-04-20; MTM $11,023.59) | ≈ −18.4% est (BTC 30d ago ~$77k → today $62.9k) | ≈ +28.6pp | BULL well ahead |
| 90d | — | — | — | not computable (BULL inception 2026-04-20 = 75 days ago; window first computable ~2026-07-19) |

(BTC last closed 1H $62,866.9 via `scripts/indicators.py`.)
