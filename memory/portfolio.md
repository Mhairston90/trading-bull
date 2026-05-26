# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-05-26T13:00Z routine-01-overnight — TAO/USD long opened at the 12:00Z 1H close. Strategy v0.4 momentum entry: 14/15 universe pairs positive (5a PASS, no SBD), TAO rank 5 outranks the lone other technical-PASS candidate HYPE (rank 6) per rule 8. Position: 15.273800 TAO @ 286.40410 fill (close 286.261 × 1.0005 slip), 2×ATR(14)=10.28310 stop @ 276.12100, 4R target @ 327.53650, risk $157.06 (1.5% equity). BTC same-pair cooldown still active until 2026-05-26T22:00Z. Kill switches remain clear.

## Account

- Starting equity: **$10,000.00**
- Cash: **$6,084.36** (paper book: $10,470.78 − notional $4,374.05 − entry commission $11.37)
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
- Unrealized PnL (open positions, MTM at last 286.261 close): **−$2.10** = (286.261 − 286.40410) × 15.273800 = −$2.18 (rounded −$2.10)
- Position values (MTM): **$4,372.00** (15.273800 × 286.261)
- Current equity (cash + positions MTM): **$10,456.36**
- Equity peak: **$10,728.95** (set 2026-05-21 during missed-scheduler HYPE 4R take-profit replay)
- Drawdown from peak: **2.54%**

## Open positions

| Pair | Side | Size | Entry | Stop | 4R target | Initial Risk | Unrealized R |
|------|------|------|-------|------|-----------|--------------|--------------|
| TAO/USD | long | 15.273800 | 286.40410 | 276.12100 | 327.53650 | $157.06 (1.5%) | −0.014R |

Portfolio risk-at-moment: **1.50%** of equity (cap 4%).
Open positions: **1 / 8** (strategy v0.4 max-concurrent 4 → 1/4 used; cluster {BTC,ETH,SOL,TAO,AVAX,SUI,LINK} 1/2 — TAO).

## Active kill-switch state

- Daily realized: $0.00 today = **0.00%** vs day-open equity $10,470.78 — within 5% LOSS cap. Prior active day 2026-05-25 realized −$33.70 (−0.32%).
- Consecutive losing trading days: 05-21 W, 05-22 L, 05-25 L → streak **2** (cap 7); no trading days 05-23/05-24 (weekend).
- Max drawdown: 2.54% from peak $10,728.95 (cap 25%, warn 12.5%) — clear, well below warn
- Equity floor: $10,456.36 > $7,500 floor — OK
- **All clear. Trading authorized.** TAO long open; BTC same-pair stop-out cooldown still active until 2026-05-26T22:00Z.

## Pending exit triggers

- **TAO/USD long**: ATR(14)=5.142, initial stop 276.12100 (2×ATR), breakeven ratchet armed at unrealized R ≥ 2.0 → would move stop to 286.40410 entry (Stop-management rule). 4R target 327.53650. Exit rule 1 (W22-G): two consecutive 1H closes < 1H 20-EMA fires exit on 2nd bar; current 1H 20-EMA ≈ 282.48, close 286.26 above EMA → 0/2 confirmation bars. Not in SBD regime so 20-EMA exit applies (not 9-EMA).

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | ≈ +4.6% (approx) | ≈ −2 to −3% (approx) | ≈ +7% (approx) | BULL ahead (approx) |
| 30d | — | — | — | — |
| 90d | — | — | — | — |

(7d figures approximate — precise reference-price computation deferred to routine #4. 30d window pre-dates BULL inception 2026-04-20; first computable 2026-05-20.)
