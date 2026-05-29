# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-05-29T20:07Z routine-02-midday (on-time wake, scheduled 13:00 PT Friday). Book flat going in; no trades this wake (midday is position-management only, and there are no positions to manage). Cash/equity $10,356.03 unchanged, DD 3.48% from peak $10,728.95, losing-day streak 3 (05-22, 05-25, 05-26; 05-27/05-28/05-29-so-far no trades). No active 5b cooldowns. Kill switches all clear. **Regime: 5a CLEARED and SBD CLEARED** — 8/15 universe pairs positive (HYPE +7.07, PENGU +2.19, LTC +0.62, XDG +0.50, XRP +0.49, ETH +0.43, LINK +0.12, SOL +0.02), median 24h **+0.02%**. Sharp reversal from this morning's 1/15 positive / −1.19% median. SBD-active streak broken after 3 consecutive wakes (~24h); standard 20-EMA two-bar exit rule (Exit 1) is the live exit again. Read is broadly mixed (BTC −0.04 flat) with isolated alt strength (HYPE +7%) rather than a broad-tape bid — mechanical threshold crossing more than thematic reversal. Entries not opened (midday spec); next entry-scan = routine-03-eod 2026-05-30T04:00Z.

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

- Daily realized: $0 on 2026-05-29 PT trading day so far (no trades) — within 5% LOSS cap.
- Consecutive losing trading days: 05-21 W, 05-22 L, 05-25 L, 05-26 L → streak **3** (cap 7); 05-27, 05-28, 05-29-so-far no trades (streak neither extended nor broken).
- Max drawdown: 3.48% from peak $10,728.95 (cap 25%, warn 12.5%) — clear, well below warn.
- Equity floor: $10,356.03 > $7,500 floor — OK.
- **All clear. Trading authorized AND regime gate (rule 5a) now PASSES (8/15 positive ≥ 4 floor).** SBD cleared after 3-wake streak. Account flat — no positions to apply the relaxed regime to until next entry-scan. No active 5b cooldowns. routine-02-midday 2026-05-29T20:07Z (on-time): 0 trades / $0 PnL (midday is no-entry by spec; book flat → nothing to MTM or exit). Next entry-scan opportunity: routine-03-eod 2026-05-30T04:00Z (last trading day of May for EOD scope → archive sweep due). First entry-scan under cleared 5a regime — per-pair signals on the 03:00Z 1H close will determine whether anything actually opens.

## Pending exit triggers

(no open positions)

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | ≈ +2.4% (approx) | ≈ −3% (approx) | ≈ +5% (approx) | BULL ahead (approx) |
| 30d | — | — | — | — |
| 90d | — | — | — | — |

(7d figures approximate — precise reference-price computation deferred to routine #4. 30d window pre-dates BULL inception 2026-04-20; first computable 2026-05-20.)
