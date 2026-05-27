# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-05-27T~15:30Z routine-03-eod (late-firing; cron-target 04:00Z = 21:00 PT 2026-05-26). No trades this wake (account flat going in; entry scan SKIP — all 8 liquidity-passing pairs failed rule 1 or rule 2 at just-closed 14:00Z 1H bar). No state delta vs routine-02-midday rebuild: cash/equity $10,356.03, DD 3.48% from peak $10,728.95, losing-day streak 3 (05-22, 05-25, 05-26). BTC same-pair cooldown expired 22:00Z 05-26; no current cooldowns active. Kill switches all clear.

## Account

- Starting equity: **$10,000.00**
- Cash: **$10,356.03** (paper book: $6,084.36 + net sale proceeds $4,271.67)
- Realized PnL (all-time): **+$356.03**
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
  - TAO −$114.75 (missed-scheduler replay exit-ema20-confirm 2026-05-26T18:00Z, −0.58R)
- Unrealized PnL (open positions): **$0.00** (flat)
- Position values (MTM): **$0.00**
- Current equity (cash + positions MTM): **$10,356.03**
- Equity peak: **$10,728.95** (set 2026-05-21 during missed-scheduler HYPE 4R take-profit replay)
- Drawdown from peak: **3.48%**

## Open positions

(none — account flat)

Portfolio risk-at-moment: **0.00%** of equity (cap 4%).
Open positions: **0 / 8** (strategy v0.4 max-concurrent 4 → 0/4 used; cluster {BTC,ETH,SOL,TAO,AVAX,SUI,LINK} 0/2).

## Active kill-switch state

- Daily realized: −$114.75 on 2026-05-26 PT trading day = **−1.10%** vs day-open equity $10,470.78 — within 5% LOSS cap. No additional realized PnL since (no trades 2026-05-27).
- Consecutive losing trading days: 05-21 W, 05-22 L, 05-25 L, 05-26 L → streak **3** (cap 7); weekend 05-23/05-24 no trading days.
- Max drawdown: 3.48% from peak $10,728.95 (cap 25%, warn 12.5%) — clear, well below warn.
- Equity floor: $10,356.03 > $7,500 floor — OK.
- **All clear. Trading authorized.** Account flat. BTC same-pair cooldown expired 2026-05-26T22:00Z; no active 5b cooldowns. routine-03-eod 2026-05-27 entry scan SKIP — every liquidity-passing pair (BTC, ETH, SOL, XRP, TAO, HYPE, XDG, SUI) failed rule 1 or rule 2 at the just-closed 14:00Z 1H bar (broad late-session pullback dragged most closes back below their 1H 20-EMAs). Next entry-scan opportunity: routine-01-overnight tomorrow.

## Pending exit triggers

(no open positions)

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | ≈ +2.4% (approx) | ≈ −3% (approx) | ≈ +5% (approx) | BULL ahead (approx) |
| 30d | — | — | — | — |
| 90d | — | — | — | — |

(7d figures approximate — precise reference-price computation deferred to routine #4. 30d window pre-dates BULL inception 2026-04-20; first computable 2026-05-20.)
