# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-05-31T04:00Z routine-03-eod (Sat 21:00 PT fire — cron `0 21 * * 1-5` PT should not fire on Saturday; this is the 2nd off-schedule weekend fire today after routine-02-midday — flagged in research_log; executing the routine since the XRP position triggered exit-ema20-confirm at 23:00Z 05-30 and must be logged). **Replay exit:** at 2026-05-30T22:00:00Z 1H close (1.34053) and 2026-05-30T23:00:00Z 1H close (1.33878), XRP/USD close was below the rising 1H 20-EMA (≈1.34137 / ≈1.34113 respectively) for two consecutive 1H bars, satisfying strategy v0.4 Exit Rule 1 (W22-G two-bar 20-EMA confirmation). Exit fires on the close of the second below-EMA bar = 2026-05-30T23:00:00Z. Slipped fill 1.33811 (0.05% adverse on 1.33878 close). Realized PnL −$101.40 / **−0.65R** on R-risk $155.31. Breakeven ratchet did NOT arm — max 1H close since entry was 1.35089 (17:00Z) → max realized-at-close R ≈ +0.081, well below the 2.0R trigger. Stop hit was avoided ($1.32178 stop, low since entry 1.33556) — the two-bar EMA exit converted a path that was drifting toward the static stop into a smaller −0.65R exit. Cash post-exit $10,254.63 = prior cash $2,574.49 + exit notional $7,720.44 − exit commission $20.07 (entry commission was absorbed at entry). Equity = cash only (0 open) = $10,254.63. **DD 4.42% from peak $10,728.95** (cap 25%, warn 12.5%) — still clear. Losing-day streak extends 3→4 (05-22 L, 05-25 L, 05-26 L, 05-30 L; the no-PnL-realized days 05-27/28/29 neither broke nor extended the streak). Universe regime: 14/15 positive 24h (TRX the lone negative at −0.59%), median ≈+0.47% — Rule 5a PASS, SBD CLEARED. Kraken risk_flag CLEAR. Kill switches all clear. **EOD entry scan:** BTC, TAO, ADA all fail rule 3 (4H close < 4H 50-EMA, regime in early recovery from the 05-27→05-28 selloff that bottomed BTC ~72.6k); HYPE passes rule 3 (close 68.77 > 50-EMA proxy ~61.50) and rule 4a (24h notional ~$30M) and is the only viable rule-3-passing non-cluster candidate, but FAILS rule 2 (1H RSI14 ≈ 53 < 55 floor — recent chop within the rally has dampened momentum). No entry this wake. **0 OPEN, 1 CLOSE.**

## Account

- Starting equity: **$10,000.00**
- Cash: **$10,254.63** (+$7,680.14 this wake from XRP exit net of exit commission)
- Realized PnL (all-time): **+$254.63** (−$101.40 this wake from XRP exit-ema20-confirm)
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

_(none — XRP/USD closed 2026-05-30T23:00:00Z on exit-ema20-confirm replay)_

Portfolio risk-at-moment: **0.00%** of equity (cap 4%).
Open positions: **0 / 8** (strategy v0.4 max-concurrent 4 → 0/4 used; cluster {BTC,ETH,SOL,TAO,AVAX,SUI,LINK} 0/2).

## Active kill-switch state

- Daily realized on 2026-05-30 PT trading day: **−$101.40** (XRP exit at 16:00 PT 05-30 = 23:00Z 05-30) — −0.98% of $10,356.03 start-of-day equity; within 5% LOSS cap (would require ~$518 loss to trip).
- Consecutive losing trading days: 05-21 W, 05-22 L, 05-25 L, 05-26 L, then 05-27/28/29 no-realized-PnL (open XRP), 05-30 L → streak **4** (cap 7; warn at 5 informally).
- Max drawdown: 4.42% from peak $10,728.95 (cap 25%, warn 12.5%) — clear, well below warn.
- Equity floor: $10,254.63 > $7,500 floor — OK.
- **All clear. Trading authorized for next routine.** Regime gate (rule 5a) PASSES (14/15 positive ≥ 4 floor); SBD CLEARED (median 24h % ≈ +0.47% > −1.0% threshold and 14 positive > 1 ceiling). No active 5b cooldowns (XRP exit-ema20-confirm is not `exit-stop-hit` — rule 5b cooldown applies only to stop-outs per strict letter; XRP technically re-eligible at next wake but failed rule 2 this wake anyway). routine-03-eod 2026-05-31T04:00Z (Sat off-schedule wake — see research_log): **0 OPEN, 1 CLOSE.** Next wake: routine-04-harness scheduled Sunday 21:00 PT (= 2026-06-01T04:00Z UTC).

## Pending exit triggers

_(none — no open positions)_

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | ≈ −4.42% (from peak $10,728.95 set 2026-05-21) | ≈ −4.6% (BTC 2026-05-21 ~$77.6k → today $74.0k) | ≈ +0.2% | BULL ahead (thin) |
| 30d | ≈ +2.55% (inception $10k 2026-04-20; window now fully computable since 2026-05-20) | ≈ −9.0% (BTC 2026-04-29 ~$81.3k → today $74.0k) | ≈ +11.6% | BULL ahead |
| 90d | — | — | — | not computable (BULL inception 2026-04-20 = 41 days ago) |

(7d and 30d figures approximate — precise reference-price computation deferred to routine #4. 90d window first computable ~2026-07-19.)
