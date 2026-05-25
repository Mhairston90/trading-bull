# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-05-25 interactive operator reconciliation — BTC/USD stop exit processed from the first triggering 1H candle. The 2026-05-25T22:00Z closed candle finished at 77041.4, below the fixed stop 77122.02; per the established stop model the paper fill is stop × 0.9995 = **77083.46**. Realized result: **−$33.70 / −1.07R** after entry/exit commissions. BULL is now flat. Kill switches remain clear: equity $10,470.78, DD 2.41% from peak $10,728.95, day PnL −$33.70 / −0.32% vs flat day-open equity $10,504.48. BTC same-pair stop-out cooldown now blocks fresh BTC entries until 2026-05-26T22:00Z.

## Account

- Starting equity: **$10,000.00**
- Cash: **$10,470.78**
- Realized PnL (all-time): **+$470.78**
  - BTC −$9.14 (exit-ema-cross 2026-04-24T04:00Z)
  - TRX −$26.69 (exit-stop-hit 2026-04-24T20:00Z)
  - LTC +$39.40 (exit-ema-cross 2026-04-25T17:00Z, +1.32R)
  - ADA −$38.77 (exit-ema-cross 2026-04-25T17:00Z, −1.21R)
  - AVAX −$34.04 (exit-ema-cross 2026-04-25T17:00Z, −0.99R)
  - ETH −$34.68 (exit-stop-hit 2026-04-27T05:00Z, −1.06R)
  - BTC −$28.77 (exit-stop-hit 2026-04-27T05:00Z, −1.08R)
  - SOL −$33.82 (exit-stop-hit 2026-04-27T05:00Z, −1.06R)
  - TAO −$56.38 (exit-stop-hit 2026-04-27T05:00Z, −1.03R)
  - TAO −$64.37 (exit-stop-hit 2026-04-29T14:00Z, −1.02R)
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
- Unrealized PnL: **$0.00** (flat)
- Position values (MTM): **$0.00**
- Current equity (cash + positions MTM): **$10,470.78**
- Equity peak: **$10,728.95** (set 2026-05-21 during missed-scheduler HYPE 4R take-profit replay)
- Drawdown from peak: **2.41%**

## Open positions

No open positions.

Portfolio risk-at-moment: **0.00%** of equity (cap 4%).
Open positions: **0 / 8** (strategy v0.4 max-concurrent 4 → 0/4 used; cluster {BTC,ETH,SOL,TAO,AVAX,SUI,LINK} 0/2).

## Trade-log correction (2026-05-16, routine-03-eod)

During this EOD wake a concurrent `routine-02-midday` instance wrote:
`2026-05-15T13:00:00Z | CLOSE | XRP/USD | long | 6334 | 1.44305 | — | — | -1.03 | -206.37 | exit-stop-hit`
and rebuilt portfolio.md to equity $10,051.73.

That exit is **superseded**. Per `strategy.md` Exits — "Exit when ANY of the following is true … checked at the close of each 1H candle. No intra-bar exits" — the binding exit is the *first* condition true at a 1H close. Replaying XRP 1H closes from the 2026-05-14T16:00Z entry:

- **Exit rule 1 (1H close < 1H 20-EMA): first true at 2026-05-15T04:00:00Z** — close 1.47298 vs 20-EMA ≈ 1.4780. EMA seeded as SMA of 1H closes 2026-05-13 03:00→22:00Z (= 1.439169), iterated 30 bars; cross-checked vs prior EOD's independent EMA ≈ 1.4406 @ 2026-05-14 15:00Z. Bars 05-14 16:00Z→05-15 03:00Z all closed *above* the rising EMA (closes 1.479–1.536 vs EMA 1.444–1.479); 05-15 04:00Z (close 1.47298 < EMA 1.4780) is the first close below.
- Exit rule 2 (static stop 1.44377): first 1H close ≤ stop not until 2026-05-15T13:00Z (close 1.43187); intra-bar lows 05-14 16:00Z→05-15 04:00Z all ≥ 1.47298 — stop untouched before the EMA-cross even ignoring "no intra-bar exits".

The EMA-cross at 04:00Z closes the position ~9h before any stop interaction, so the 13:00Z stop-out cannot occur. Correction row appended to `trade_log.md` at the true candle-close timestamp `2026-05-15T04:00:00Z`, reason `correction-previous-row`, per `skills/log-trade.md` ("never rewrite past rows; append a correction row"). Net realized **−$21.92 (−0.14R)** after 0.26%/side commissions and 0.05% exit slippage (fill 1.47224 = 1.47298 × 0.9995). Cash = $935.19 + ($9,325.19 − $24.25 comm) = **$10,236.14**.

Flagged for routine #4 (Sat 2026-05-16): (a) codify that any late/concurrent routine fire must replay *all* unprocessed 1H closes and apply the earliest exit trigger, not just the latest bar; (b) resolve the duplicate-CLOSE race when multiple routine instances act on the same open position; (c) reconcile the "no intra-bar exits" rule vs the intra-bar stop interpretation used by routine-02.

## Active kill-switch state

- Daily realized: −$33.70 today = **−0.32%** vs day-open equity $10,504.48 — within 5% LOSS cap. Prior active day 2026-05-22 realized −$145.29 (−1.36%).
- Consecutive losing trading days: 05-21 W, 05-22 L, 05-25 L → streak **2** (cap 7); no trading days 05-23/05-24 (weekend).
- Max drawdown: 2.41% from peak $10,728.95 (cap 25%, warn 12.5%) — clear, well below warn
- Equity floor: $10,470.78 > $7,500 floor — OK
- **All clear. Trading authorized.** Flat, with BTC same-pair stop-out cooldown active until 2026-05-26T22:00Z.
- **2026-05-25 operator reconciliation note:** BTC/USD long from 15:00Z closed at the 22:00Z stop trigger. 22:00Z 1H close 77041.4 was below fixed stop 77122.02; modeled fill 77083.46 = stop × 0.9995 adverse slippage. Gross price loss −$20.10; entry commission $6.83 and exit commission $6.77 bring net realized PnL to **−$33.70**. Two-bar EMA exit was not the binding rule; stop fired first. No entries were scanned or opened.

## Pending exit triggers

- No open positions.

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | ≈ +5.3% (approx) | ≈ −3 to −4% (approx) | ≈ +8% to +9% (approx) | BULL ahead (approx) |
| 30d | — | — | — | — |
| 90d | — | — | — | — |

(7d figures approximate — precise reference-price computation deferred to routine #4. 30d window pre-dates BULL inception 2026-04-20; first computable 2026-05-20.)
