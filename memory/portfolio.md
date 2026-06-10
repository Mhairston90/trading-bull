# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-06-11T20:00Z routine-02-midday (Thu 13:00 PT on-schedule fire, cron `0 13 * * 1-5` PT in-window since 2026-06-11 = Thursday). **Third consecutive scheduled wake with Kraken MCP available** (after the 06-10T17:50Z overnight and 06-11T04:00Z EOD). Fresh `kraken_multi_ticker` 15/15 clean at the 13:00 PT pull: **1/15 positive on 24h % change (BTC +0.09), median −2.68% (SOL)**. Sorted: −6.72 (NEAR) / −6.35 (HYPE) / −5.98 (FARTCOIN) / −3.51 (XRP) / −3.39 (LTC) / −3.11 (LINK) / −2.93 (ADA) / −2.68 (AVAX) / −2.55 (SOL) / −2.27 (SUI) / −2.16 (XDG) / −2.09 (TAO) / −0.78 (ETH) / −0.46 (TRX) / +0.09 (BTC). Modest improvement vs the 06-11T04:00Z EOD print (0/15→1/15 positive, median −2.54%→−2.68%) — BTC ticked up but breadth still deeply one-sided. Regime classification (informational only — midday doesn't gate on it): **5a still FAIL** (1 < 4 positive floor); **5a-SBD still ACTIVE** (1 ≤ 1 positive AND median −2.68 ≤ −1.0 threshold; 1.68pts headroom below trigger). SBD's tightened 9-EMA exit override remains inert — **book flat** (17th+ consecutive flat-book wake since XRP exit 2026-05-30T23:00Z). MTM step inert (0 open positions to quote); exit step inert (nothing to evaluate). **Midday entry scan forbidden by routine design** — entry responsibility belongs to routine-01-overnight and routine-03-eod. No trades this wake (0 opened, 0 closed). Equity unchanged **$10,254.63** (cash-only). Day PnL **$0.00 / 0.00%**. Since-start **+2.55%** (52 days from inception 2026-04-20). Drawdown **4.42%** from peak $10,728.95 — unchanged. Consecutive losing trading days: 4 (06-01 → 06-10 all zero-PnL; informal warn-5 still one L away). Kill switches all clear (DD 4.42% < 12.5% warn / 25% cap, equity > $7,500 floor, daily PnL $0 < 5% cap, loss-streak 4 < 7 cap, Kraken MCP AVAILABLE). `kraken_risk_flag` returns NO_DATA (daily_risk_flag.json not mirrored at scripts/ location — informational only per 2026-06-09 fix note; not a kill switch since multi_ticker succeeded). **No Telegram** (silent — routine #2 NOTIFY gate requires kill-switch trip / exit event / DD halfway-warn crossing; none apply, DD comfortably below halfway-warn). BTC reference **$61,743.50** (+0.23% vs the EOD $61,602.10 print) — flat-book through the 06-01→ongoing synchronized breakdown maintains the BULL-vs-BTC-hold delta at ≈+26.6% over the 30d window (designed-in defensive outcome of rules 5a / 5a-SBD per the W21-F fragility audit). **Thu overnight 06-11T13:00Z slot:** no commit between Wed EOD and this midday — either silent-no-output OR didn't fire; flagging for next-harness investigation. Next on-schedule wake: routine-03-eod 2026-06-12T04:00Z (Thu 21:00 PT scheduled).

## Account

- Starting equity: **$10,000.00**
- Cash: **$10,254.63** (unchanged — no trades this routine)
- Realized PnL (all-time): **+$254.63**
  - BTC −$9.14 (exit-ema-cross 2026-04-24T04:00Z) *(archived)*
  - TRX −$26.69 (exit-stop-hit 2026-04-24T20:00Z) *(archived)*
  - LTC +$39.40 (exit-ema-cross 2026-04-25T17:00Z, +1.32R) *(archived)*
  - ADA −$38.77 (exit-ema-cross 2026-04-25T17:00Z, −1.21R) *(archived)*
  - AVAX −$34.04 (exit-ema-cross 2026-04-25T17:00Z, −0.99R) *(archived)*
  - ETH −$34.68 (exit-stop-hit 2026-04-27T05:00Z, −1.06R) *(archived)*
  - BTC −$28.77 (exit-stop-hit 2026-04-27T05:00Z, −1.08R) *(archived)*
  - SOL −$33.82 (exit-stop-hit 2026-04-27T05:00Z, −1.06R) *(archived)*
  - TAO −$56.38 (exit-stop-hit 2026-04-27T05:00Z, −1.03R) *(archived)*
  - TAO −$64.37 (exit-stop-hit 2026-04-29T14:00Z, −1.02R) *(archived)*
  - HYPE −$58.18 (exit-stop-hit 2026-05-06T15:00Z, −1.02R)
  - BTC +$1.42 (exit-ema-cross 2026-05-06T19:00Z, +0.06R)
  - LTC −$48.58 (exit-stop-hit 2026-05-07T01:00Z, −1.03R)
  - XRP −$37.68 (exit-stop-hit 2026-05-07T14:00Z, −1.05R)
  - LINK +$103.03 (exit-ema-cross 2026-05-07T20:00Z, +1.69R)
  - SOL +$585.35 (exit-4R-target 2026-05-11T19:00Z, +4.03R)
  - XRP −$21.92 (exit-ema-cross 2026-05-15T04:00Z, −0.14R) — corrected; supersedes the routine-02-midday-logged 2026-05-15T13:00Z exit-stop-hit −$206.37
  - HYPE +$413.62 (missed-scheduler replay exit-4R-target 2026-05-21T08:00Z, +4.04R)
  - TAO −$29.84 (missed-scheduler replay exit-ema20-confirm 2026-05-22T01:00Z, −0.50R)
  - HYPE −$33.98 (missed-scheduler replay exit-ema20-confirm 2026-05-22T02:00Z, −0.29R)
  - SOL −$45.64 (missed-scheduler replay exit-stop-hit 2026-05-22T15:00Z, −1.43R)
  - AVAX −$35.83 (missed-scheduler replay exit-ema20-confirm 2026-05-22T16:00Z, −0.94R)
  - BTC −$33.70 (exit-stop-hit 2026-05-25T22:00Z, −1.07R)
  - TAO −$114.75 (missed-scheduler replay exit-ema20-confirm 2026-05-26T18:00Z, −0.58R)
  - XRP −$101.40 (missed-scheduler replay exit-ema20-confirm 2026-05-30T23:00Z, −0.65R)
- Unrealized PnL (open positions): **$0.00** (no open positions)
- Position values (MTM): **$0.00**
- Current equity (cash + positions MTM): **$10,254.63**
- Equity peak: **$10,728.95** (set 2026-05-21 during missed-scheduler HYPE 4R take-profit replay)
- Drawdown from peak: **4.42%**

## Open positions

_(none — book flat since XRP/USD exit 2026-05-30T23:00:00Z)_

Portfolio risk-at-moment: **0.00%** of equity (cap 4%).
Open positions: **0 / 8** (strategy v0.4 max-concurrent 4 → 0/4 used; cluster {BTC,ETH,SOL,TAO,AVAX,SUI,LINK} 0/2).

## Active kill-switch state

- Daily realized on 2026-06-11 PT trading day: **$0.00** (no closes today; last close was XRP exit 2026-05-30 PT, 12 days ago) — clear vs 5% loss cap.
- Consecutive losing trading days: 05-22 L, 05-25 L, 05-26 L, 05-30 L (05-27/28/29/31, 06-01 → 06-10 all no-realized-PnL → streak unchanged) → streak **4** (cap 7; warn at 5 informally — still 1 day from informal warn).
- Max drawdown: **4.42%** from peak $10,728.95 (cap 25%, warn 12.5%) — clear.
- Equity floor: $10,254.63 > $7,500 floor — OK.
- Regime gate (rule 5a) — **freshly measured this wake**: 1/15 positive (BTC +0.09), median −2.68% (SOL) → 5a FAIL, 5a-SBD ACTIVE. SBD's tightened 9-EMA exit override is inert (book flat — no open positions to apply to). Avoided-give-back: vacuous (no open positions to compare 9-EMA vs 20-EMA exits on).
- No active 5b cooldowns (XRP 2026-05-30 exit was ema20-confirm, not stop-hit — rule 5b inapplicable; >24h elapsed anyway).
- **All clear (kill switches).** routine-02-midday 2026-06-11T20:00Z (Thu 13:00 PT on-schedule fire): **0 OPEN, 0 CLOSE** (book flat → MTM + exit-check steps inert; midday entry-scan forbidden by routine design). Kraken MCP available (15/15 ticker clean — 3rd post-fix scheduled wake confirmation). Drawdown 4.42% unchanged. Loss-streak 4 unchanged (no closes today, zero-PnL day does not advance). Daily PnL $0. No Telegram (silent — no kill-switch trip / exit / DD halfway-warn cross). Next on-schedule wake: routine-03-eod 2026-06-12T04:00Z (Thu 21:00 PT scheduled).

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

_(none — no open positions)_

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | ≈ −4.42% (from peak $10,728.95 set 2026-05-21) | ≈ −20.4% (BTC 2026-06-04 ~$77.6k → today $61.7k) | ≈ +16.0% | BULL ahead |
| 30d | ≈ +2.55% (inception $10k 2026-04-20; window fully computable) | ≈ −24.0% (BTC 2026-05-12 ~$81.2k → today $61.7k) | ≈ +26.6% | BULL ahead |
| 90d | — | — | — | not computable (BULL inception 2026-04-20 = 52 days ago) |

(7d and 30d figures approximate — precise reference-price computation deferred to routine #4. 90d window first computable ~2026-07-19. BTC reference today **$61,743.50** — BTC ticked +0.23% since the 06-11T04:00Z EOD print of $61,602; minor noise, BULL's defensive-flat-book delta essentially unchanged. Flat-book through a synchronized breakdown is the designed-in protective outcome of rules 5a/5a-SBD per the W21-F fragility audit.)
