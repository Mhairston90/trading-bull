# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-05-30T20:00Z routine-02-midday (wake fired ~13:00 PT Saturday 2026-05-30; doc-cron is `0 13 * * 1-5` PT Mon–Fri but task scheduler triggered today regardless — flagged in research_log, executing the routine since XRP position needs MTM/exit-check management; behaviorally treated as a normal midday). Open position XRP/USD unchanged (1 open since 2026-05-30T04:00Z entry). Fresh XRP mark = **1.34722** (kraken_multi_ticker). MTM = 5769.659 × 1.34722 = **$7,773.00** (down $8.54 from entry notional $7,781.54). Cash $2,574.49 + MTM $7,773.00 = equity **$10,347.49** (−$8.54 from prior wake's $10,356.03 entry-marked equity). Unrealized R = −0.055 (well above stop, well below 4R target and breakeven-ratchet trigger). No exits triggered: stop $1.32178 not pierced intrabar (min low since entry = 1.33556 at 04:00Z bar); 20-EMA two-bar exit not satisfied (last two just-closed bars 18:00Z close 1.35011 and 19:00Z close 1.34527 BOTH above 1H 20-EMA at those bars ≈1.33969/1.34019); 4R target 1.45638 not approached (max high since entry 1.35211). SBD remains CLEARED (15/15 universe positive on 24h, median +1.49%) → standard 20-EMA exit rule in force. Regime 5a PASS. DD 3.56% from peak $10,728.95 (cap 25%, warn 12.5%). Losing-day streak unchanged 3. Kill switches all clear. Midday writes no entries by spec.

## Account

- Starting equity: **$10,000.00**
- Cash: **$2,574.49** (unchanged this wake — no closes)
- Realized PnL (all-time): **+$356.03** (unchanged this wake — no closes)
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
- Unrealized PnL (open positions): **−$8.54** (XRP marked at 1.34722; in-progress 20:00Z bar)
- Position values (MTM): **$7,773.00** (XRP/USD 5769.659 × 1.34722)
- Current equity (cash + positions MTM): **$10,347.49**
- Equity peak: **$10,728.95** (set 2026-05-21 during missed-scheduler HYPE 4R take-profit replay)
- Drawdown from peak: **3.56%**

## Open positions

| Pair | Side | Size | Entry | Entry time (UTC) | Stop (initial 2×ATR) | Stop (active) | Target (4R) | R-risk ($) | Unrealized R | Unrealized $ | Notes |
|------|------|------|-------|-----------------|----------------------|---------------|-------------|------------|--------------|--------------|-------|
| XRP/USD | long | 5769.659 | 1.34870 | 2026-05-30T04:00:00Z | 1.32178 | 1.32178 | 1.45638 | 155.31 | −0.055 | −8.54 | Mark 1.34722. Breakeven ratchet NOT armed — max close since entry 1.35089 (17:00Z) → max realized-at-close R ≈ +0.081; ratchet requires ≥ 2.0R at any 1H close. Active stop = initial 2×ATR. 16 closed 1H bars since entry; min low 1.33556 (04:00Z), max high 1.35211 (18:00Z) — well bracketed inside stop/target. |

Portfolio risk-at-moment: **1.50%** of equity (cap 4%; this trade = full 1.50% per spec, no other open positions).
Open positions: **1 / 8** (strategy v0.4 max-concurrent 4 → 1/4 used; cluster {BTC,ETH,SOL,TAO,AVAX,SUI,LINK} 0/2; XRP is NOT in the cluster).

## Active kill-switch state

- Daily realized: $0 on 2026-05-30 PT trading day (no closes; only open MTM movement) — within 5% LOSS cap.
- Consecutive losing trading days: 05-21 W, 05-22 L, 05-25 L, 05-26 L → streak **3** (cap 7); 05-27, 05-28, 05-29, 05-30 no-realized-PnL days (streak neither extended nor broken — open XRP position not yet realized).
- Max drawdown: 3.56% from peak $10,728.95 (cap 25%, warn 12.5%) — clear, well below warn.
- Equity floor: $10,347.49 > $7,500 floor — OK.
- **All clear. Trading authorized; regime gate (rule 5a) PASSES (15/15 positive ≥ 4 floor); SBD CLEARED (median 24h % +1.49% > −1.0% threshold and 15 positive > 1 ceiling).** No active 5b cooldowns. routine-02-midday 2026-05-30T20:00Z (Sat off-schedule wake — see research_log note): **0 OPEN, 0 CLOSE.** Next wake: routine-03-eod 2026-05-31T04:00Z (per cron `0 21 * * 1-5` PT, Friday-evening fire was 2026-05-30T04:00Z; next eligible weekday-evening fire is Sunday 21:00 PT for Monday's EOD scope, i.e. 2026-06-01T04:00Z UTC — Saturday/Sunday EOD scopes are not generated by Mon-Fri cron).

## Pending exit triggers

- **XRP/USD**: monitor 1H closes against 20-EMA — if two consecutive 1H closes < 20-EMA (currently ≈1.3402), exit per v0.4 Rule 1 (`exit-ema20-confirm`). Check if XRP unrealized R reaches ≥ 2.0 at any 1H close → ratchet stop from 1.32178 → 1.34870 (entry, breakeven) per Stop management. Static stop 1.32178 in force until either ratchet fires or price hits stop. 4R target 1.45638 (`exit-4R-target`). SBD currently CLEARED → standard 20-EMA exit applies; if SBD re-activates, the tighter 9-EMA two-bar exit (Exit 1-SBD) takes over.

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | ≈ −3.56% (from peak $10,728.95 set 2026-05-21) | ≈ −4.8% (BTC 2026-05-21 ~$77.6k → today $73.9k) | ≈ +1.2% | BULL ahead |
| 30d | ≈ +3.47% (inception $10k 2026-04-20; window now fully computable since 2026-05-20) | ≈ −9.1% (BTC 2026-04-29 ~$81.3k → today $73.9k) | ≈ +12.6% | BULL ahead |
| 90d | — | — | — | not computable (BULL inception 2026-04-20 = 40 days ago) |

(7d and 30d figures approximate — precise reference-price computation deferred to routine #4. 90d window first computable ~2026-07-19.)
