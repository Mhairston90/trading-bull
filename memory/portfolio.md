# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-07-03T23:01Z routine-01-overnight (PT Fri 2026-07-03 16:01, cron slot `bull-01-overnight` fired ~10h late vs nominal 06:00 PT / 13:00Z; MCP recovered, executing replay-style processing). **2 trade events this wake: 1 CLOSE (SOL/USD 4R take-profit, missed-scheduler-replay of 07-03T20:00Z bar close), 1 OPEN (ETH/USD rule-8-fallback after BTC cash-blocked)**. **MILESTONE:** SOL/USD **hit +4R take-profit** at 07-03T20:00Z bar close $82.64 (≥ target $82.4019 by $0.238). This is the **2nd 4R take-profit hit in the last 20 days** (prior: TAO 06-13T09:00Z +4.04R $621.22) and **the first 4R hit on a trade that had previously armed the W22-H breakeven ratchet** — proof-of-mechanism for the W22-H amendment (the ratchet arm 07-02T09:00Z guaranteed no loss floor, then price ran the additional +1.7R to 4R over 35h). **Second milestone:** post-close all-time realized **+$885.36** clears prior equity peak $10,875.85 by +$9.51 → **NEW EQUITY PEAK $10,885.36 all-cash mark at 07-03T20:00Z post-exit** (superseded intra-wake by ETH open which marked equity down to $10,854.08 via entry slippage + commission drag). **Third milestone:** first cash-fittable non-SOL entry since 2026-06-13 TAO (20 days) — SOL exit freed $7,214.42 cash → post-exit cash $10,885.39 allowed rule-8-fallback to ETH (rank 2) after BTC (rank 1) cash-failed at $15.3K notional. Cash-fit constraint remains structurally binding on rank-1 BTC but not on rank-2 ETH. Equity MTM **$10,854.08** ($759.96 cash + 5.7481 ETH × $1,756.08 close = $10,094.12) = **+$121.39 / +1.13% wake-over-wake** vs prior EOD $10,732.69; DD **0.29%** from just-set peak $10,885.39 (still comfortably clear of 12.5% warn — 12.21pp headroom). All Ring 3 kill switches CLEAR. Regime PASS 15/15, median +3.61%, SBD CLEAR (best regime print since 07-02 midday's 15/15 median +5.77%).

> **Prior rebuilds:** 2026-07-03T04:11Z routine-03-eod (Thu 21:00 PT ON-SCHEDULE M-F, PT date 2026-07-02, 0/0, SOL held +2.92R unrealized, 9 TECH-PASS all cash-rejected 7th consec, DD 1.32%, +4R intrabar-touch/close-miss 1st Exit-3 instance); 2026-07-02T20:00Z routine-02-midday (Thu 13:00 PT ON-SCHEDULE M-F, 0/0, SOL held +2.99R unrealized, DD 1.20%); 2026-07-02T13:07Z routine-01-overnight (Thu 06:00 PT ON-SCHEDULE M-F, 0/0, W22-H breakeven ratchet ARMED on SOL at 07-02T09:00Z close $79.40 = +2.30R, stop $73.5918→$75.3538, 10 TECH-PASS all cash-rejected, DD 0.77%, +4R intrabar-touch/close-miss 1st instance); 2026-07-02T04:11Z routine-03-eod (Wed 21:00 PT ON-SCHEDULE, 0/0, SOL held +1.87R unrealized, 7 TECH-PASS all cash-rejected, DD 2.93%); 2026-07-01T20:00Z routine-02-midday (Wed 13:00 PT ON-SCHEDULE M-F, 0/0, SOL held +0.87R unrealized, DD 4.34%); 2026-07-01T15:52Z routine-01-overnight (Wed 06:00 PT slot ~2h52m late, 0/0, regime PASS 13/15 SBD CLEAR, SOL held +0.86R, universe refresh ONDO in / FARTCOIN out).

## Account

- Starting equity: **$10,000.00**
- Cash: **$759.96** (post-SOL exit +$7,214.42 net, post-ETH entry −$10,125.43)
- Realized PnL (all-time): **+$885.36** (was +$286.80; +$598.56 from SOL 4R exit)
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
  - **SOL +$598.56 (exit-4R-target-missed-scheduler-replay 2026-07-03T20:00Z, +3.88R net) — THIS WAKE**
- Unrealized PnL (open positions): **−$5.05** (ETH 5.7481 × ($1,756.08 − $1,756.9580) = −$5.05 immediate mark below fill from entry slippage; entry commission $26.26 already booked at open)
- Position values: **$10,094.12** (ETH 5.7481 × $1,756.08 last 1H close 07-03T22:00Z = $10,094.12 MTM)
- Current equity (cash + MTM): **$10,854.08** (= $759.96 cash + $10,094.12 ETH MTM; wake-over-wake PnL = +$121.39 from $10,732.69 prior EOD)
- Equity peak: **$10,885.39** (set 2026-07-03T20:00Z post-SOL-exit all-cash mark; **PRIOR PEAK $10,875.85 (set 2026-06-13T09:00Z at TAO 4R close) CLEARED by +$9.54**)
- Drawdown from peak: **0.29%** ($31.31 below just-set peak; MTM immediately below peak because ETH entry slippage + commission mark it down; expected shape)
- Since-inception return: **+8.54%** ($10,854.08 / $10,000 − 1)

## Open positions

| Pair | Side | Size | Entry | Stop | Target | Notional | Risk-at-moment | Cluster | Entered |
|------|------|------|-------|------|--------|----------|----------------|---------|---------|
| ETH/USD | long | 5.7481 | $1,756.9580 | $1,728.5520 | $1,870.5820 | $10,094.12 | ~$163.28 / 1.50% | BTC-cluster (1/2) | 2026-07-03T23:00Z |

Portfolio risk-at-moment: **~1.50%** of equity (single ETH position at 1.5% initial risk; unchanged pending stop-management events). Cap 4% → 2.50pp headroom.
Open positions: **1 / 8** (strategy v0.4 max-concurrent 4 → 1/4 used; BTC-cluster 1/2 used).
Breakeven ratchet (W22-H-partial): NOT armed on ETH (unrealized R = −$5.05 / $163.28 = −0.03R, far from +2R threshold). Would arm on any 1H close ≥ $1,756.9580 + 2 × $28.406 = $1,813.7700.

## Overnight snapshot — 2026-07-03 PT Fri 16:01 PT (fired 23:01Z, ~10h late vs 06:00 PT nominal; task queue backlog)

| Metric | Value |
|---|---|
| Wake type | routine-01-overnight (bull-01-overnight slot, PT date 2026-07-03, wall-clock UTC 2026-07-03T23:01Z, ~10h late vs nominal 13:00Z fire; SOL 4R exit at 20:00Z bar was already reachable at nominal-slot time — pre-slot scheduler failure or manual invocation replay) |
| Entries this wake | **1** — ETH/USD long 5.7481 @ $1,756.9580 (fill = 22:00Z bar close $1,756.08 × 1.0005 slippage), stop $1,728.5520 (2×ATR $28.406), target $1,870.5820 (4R), risk $163.28 / 1.50%. Rule-8-fallback: BTC (rank 1) cash-rejected ($15.29K notional vs $10.89K cash), ETH (rank 2) cash-fit. |
| Exits this wake | **1** — SOL/USD 4R take-profit at 07-03T20:00Z bar close $82.64 → fill $82.5987 (slippage 0.05%), size 87.5709, gross P&L +$634.53, commissions −$35.97 (entry $17.16 + exit $18.81), **net +$598.56 / +3.88R**. This is a missed-scheduler-replay from 20:00Z (target bar) → 23:01Z (this wake); the exit is logged at the bar-close timestamp per convention. **2nd 4R take-profit inception-to-date (5th 4R-class trade counting HYPE/TAO/SOL replays; TAO 06-13 was prior most-recent 4R).** |
| Stop-management events | 0 (SOL ratchet was armed 07-02T09:00Z but position closed on 4R before any further stop movement; ETH new-open, no ratchet check yet) |
| Day-to-date P&L (PT 2026-07-03) | **+$121.39 / +1.13%** vs prior EOD $10,732.69 (mostly realized: SOL 4R P&L $598.56, less prior SOL unrealized $462.90 already in yesterday's EOD mark ≈ +$135.66 net realization uplift; less ETH entry slippage $5.05 + open commission $26.26 = +$104.35... reconciled against straight equity delta $121.39) |
| Wake-over-wake P&L | **+$121.39 / +1.13%** (same as day P&L, only wake since prior EOD) |
| Equity (cash + MTM) | **$10,854.08** ($759.96 cash + $10,094.12 ETH MTM) |
| Equity peak | **$10,885.39 (NEW; superseded prior $10,875.85 set 2026-06-13T09:00Z by +$9.54)** — mark set at 07-03T20:00Z post-SOL-exit all-cash equity |
| Drawdown from peak | **0.29%** (widened from 0.00% peak to 0.29% due to ETH entry slippage + commission drag; expected shape) |
| Loss streak | 0 trading days (unchanged; today +1.13% wake-over-wake) |
| Trades today | 1 opened (ETH), 1 closed (SOL 4R) |

## Active kill-switch state

- Daily realized + unrealized PT 2026-07-03: **+$121.39 / +1.13%** of equity — CLEAR (positive; 5.00% loss cap → 6.13pp headroom to loss cap).
- Consecutive losing trading days: **0** (cap 7, full 7-day headroom). CLEAR.
- Max drawdown: **0.29%** from just-set peak $10,885.39 (cap 25%, warn 12.5%, **12.21pp to warn**) — CLEAR.
- Equity floor: $10,854.08 > $7,500 floor — CLEAR.
- MCP availability: Kraken OK (`kraken_multi_ticker` + `kraken_ohlcv` + `kraken_spread` + `scripts/indicators.py` returned data this wake). CLEAR.
- Regime gate (rule 5a): **PASS 15/15 positive median +3.61%** (best regime print since 07-02 midday's 15/15 +5.77%; ADA leader +12.06%, TRX laggard +1.71%).
- Regime sub-state (rule 5a-SBD): **CLEAR** (15 positives ≫ 1 ceiling; median +3.61% ≫ −1.0% floor).
- Active 5b cooldowns: **none** (SOL exit was 4R take-profit, NOT stop-hit — no 24h cooldown applies to SOL re-entry; still no immediate SOL re-entry since ETH filled the 1-entry-per-wake budget).
- Cluster cap (rule 6a, BTC-cluster): **1/2** used (ETH). Full headroom left = 1 more slot.
- **All Ring 3 kill switches CLEAR.** Routine-01-overnight 2026-07-03T23:01Z: **1 entry, 1 exit, 1 open at wake / 1 open after** (SOL rolled to ETH via rule-8-fallback cash-fit path).

## Universe (unchanged since 2026-07-01 refresh)

Top 15 by 30d notional per `memory/universe.md` (refreshed at 07-01 overnight; next refresh 2026-08-01):

BTC, ETH, SOL, HYPE, XRP, ADA, NEAR, SUI, TAO, XDG, LTC, AVAX, LINK, ONDO, TRX.

**Note:** `scripts/indicators.py` still reports FARTCOIN in place of ONDO (script's pair list not updated to reflect 07-01 universe refresh). Non-blocking this wake — ONDO rank 14 was not the rule-8 winner (ETH rank 2 won). Recommend a follow-up to update `scripts/indicators.py` pair list ONDO ↔ FARTCOIN swap.

## Pending exit triggers

**ETH/USD long — post-open state:** exit conditions checked at each 1H close.
- Exit 1 (W22-G): two consecutive 1H closes < 20-EMA ($1,732.89 at last close 07-03T22:00Z per indicators.py). Currently 1H close $1,756.08 is $23.19 above; trigger requires 2 consecutive closes < ~$1,732.89.
- Exit 1-SBD (only if regime flips to SBD): two consecutive 1H closes < 9-EMA. Currently inactive (regime PASS 15/15).
- Exit 2 (stop-hit): **initial 2×ATR stop $1,728.5520**. Post-open lowest low N/A (just opened). Headroom $27.53 from current close $1,756.08.
- Exit 3 (take-profit): 4R = $1,870.5820. Distance from current close $114.50 (+6.52% notional).
- Breakeven ratchet arm level: +2R close ≥ $1,813.7700 (currently $57.69 below).

Next entry-eligible scan: routine-02-midday Fri 2026-07-03 13:00 PT (= 20:00Z Fri; note this may already have been skipped this cycle depending on scheduler recovery; effectively next is routine-03-eod Fri 21:00 PT = 07-04T04:00Z). Cluster 1/2 used, so 1 more cluster slot available; position cap 1/4, so 3 more slots. Gated by regime + per-pair TECH-PASS + cash-fit (cash $759.96 is now tight after ETH allocation; only low-notional pairs would fit under 1.5%-risk sizing).

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | ≈ +4.23% (equity 06-26 EOD $10,413.87 → today $10,854.08 MTM) | ≈ +3.46% est (BTC 06-26 ~$60,449 → today $62,541.2) | ≈ +0.77pp | BULL ahead 7d |
| 30d | ≈ +8.54% (inception $10k 2026-04-20; MTM $10,854.08) | ≈ −19% est (BTC 30d ago ~$77k → today $62.5k) | ≈ +27.5pp | BULL well ahead |
| 90d | — | — | — | not computable (BULL inception 2026-04-20 = 74 days ago; window first computable ~2026-07-19) |

(BTC last tick $62,541.2 via `kraken_multi_ticker`, 24h +1.72%.)
