# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-05-30T04:00Z routine-03-eod (on-time wake, scheduled 21:00 PT Friday 2026-05-29; cron `0 21 * * 1-5` PT). EOD card scope = 2026-05-29 PT trading day. **Account opened first new position since 2026-05-26 TAO exit: LONG XRP/USD @ 1.34870** sized 5769.659 units (risk 1.50% / 2×ATR stop 1.32178 / 4R target 1.45638). Regime 5a PASS (10/15 universe positive, median +0.81%); SBD CLEARED (8/15 positive on prior wake → 10/15 now, broad recovery). v0.4 entry rules all PASS on XRP at the just-closed 03:00→04:00Z 2026-05-30 1H bar. Cash $2,574.49 + position MTM $7,781.54 = equity $10,356.03 unchanged at entry. DD 3.48%, losing-day streak unchanged 3. Monthly archive sweep executed (2026-05-29 is last trading day of May): rows 2026-04-21 → 2026-04-29 moved to `memory/archive/2026-05.md`. Kill switches all clear.

## Account

- Starting equity: **$10,000.00**
- Cash: **$2,574.49** (paper book: $10,356.03 − $7,781.54 XRP entry notional)
- Realized PnL (all-time): **+$356.03** (unchanged this wake — entry only, no closes)
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
- Unrealized PnL (open positions): **$0.00** (XRP marked to entry at this wake; in-progress 04:00Z bar not yet closed)
- Position values (MTM): **$7,781.54** (XRP/USD 5769.659 × 1.34870 entry)
- Current equity (cash + positions MTM): **$10,356.03**
- Equity peak: **$10,728.95** (set 2026-05-21 during missed-scheduler HYPE 4R take-profit replay)
- Drawdown from peak: **3.48%**

## Open positions

| Pair | Side | Size | Entry | Entry time (UTC) | Stop (initial 2×ATR) | Stop (active) | Target (4R) | R-risk ($) | Unrealized R | Unrealized $ | Notes |
|------|------|------|-------|-----------------|----------------------|---------------|-------------|------------|--------------|--------------|-------|
| XRP/USD | long | 5769.659 | 1.34870 | 2026-05-30T04:00:00Z | 1.32178 | 1.32178 | 1.45638 | 155.31 | 0.00 | 0.00 | breakeven ratchet not yet armed (requires unrealized R ≥ 2.0 at any 1H close per v0.4 Stop management); active stop = initial 2×ATR; entry on just-closed 03:00→04:00Z 1H bar |

Portfolio risk-at-moment: **1.50%** of equity (cap 4%; this trade = full 1.50% per spec, no other open positions).
Open positions: **1 / 8** (strategy v0.4 max-concurrent 4 → 1/4 used; cluster {BTC,ETH,SOL,TAO,AVAX,SUI,LINK} 0/2; XRP is NOT in the cluster).

## Active kill-switch state

- Daily realized: $0 on 2026-05-29 PT trading day (entry only, no closes) — within 5% LOSS cap.
- Consecutive losing trading days: 05-21 W, 05-22 L, 05-25 L, 05-26 L → streak **3** (cap 7); 05-27, 05-28, 05-29 no-realized-PnL days (streak neither extended nor broken — open position not yet realized).
- Max drawdown: 3.48% from peak $10,728.95 (cap 25%, warn 12.5%) — clear, well below warn.
- Equity floor: $10,356.03 > $7,500 floor — OK.
- **All clear. Trading authorized; regime gate (rule 5a) PASSES (10/15 positive ≥ 4 floor); SBD CLEARED.** No active 5b cooldowns (XRP last exit 2026-05-15T04:00Z `exit-ema-cross`, not a stop-hit — rule 5b inapplicable; also >>24h ago). routine-03-eod 2026-05-30T04:00Z (on-time): **1 OPEN (XRP), 0 CLOSE.** Next wake: routine-01-overnight 2026-06-01T13:00Z (Mon — cron skips weekend Sat/Sun).

## Pending exit triggers

- **XRP/USD**: monitor 1H closes against 20-EMA — if two consecutive 1H closes < 20-EMA, exit per v0.4 Rule 1 (`exit-ema20-confirm`). Check if XRP unrealized R reaches ≥ 2.0 at any 1H close → ratchet stop from 1.32178 → 1.34870 (entry, breakeven) per Stop management. Static stop 1.32178 in force until either ratchet fires or price hits stop. 4R target 1.45638 (`exit-4R-target`). SBD currently CLEARED → standard 20-EMA exit applies; if SBD re-activates, the tighter 9-EMA two-bar exit (Exit 1-SBD) takes over.

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | ≈ −3.48% (from peak $10,728.95 set 2026-05-21) | ≈ −5.7% (BTC 2026-05-21 ~$77.6k → today $73.3k) | ≈ +2.2% | BULL ahead |
| 30d | ≈ +3.56% (inception $10k 2026-04-20; window now fully computable since 2026-05-20) | ≈ −10% (BTC 2026-04-29 ~$81.3k → today $73.3k) | ≈ +13.6% | BULL ahead |
| 90d | — | — | — | not computable (BULL inception 2026-04-20 = 40 days ago) |

(7d and 30d figures approximate — precise reference-price computation deferred to routine #4. 90d window first computable ~2026-07-19.)
