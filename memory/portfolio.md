# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-05-29T13:30Z routine-01-overnight (on-time wake, scheduled 06:00 PT Friday). Account flat going in; no trades this wake. Cash/equity $10,356.03 unchanged, DD 3.48% from peak $10,728.95, losing-day streak 3 (05-22, 05-25, 05-26; 05-27/05-28 no trades). No active 5b cooldowns. Kill switches all clear. **Regime: 5a-veto active AND SBD ACTIVE for 3rd consecutive wake** — 1/15 universe pairs positive (HYPE +0.83 only), median 24h −1.19% (clean SBD threshold pass, vs marginal −1.01% prior wake). Defensive 9-EMA two-bar exit applies; book flat → $0 captured. Rule 5a vetoes all entries (1 < 4 needed). BTC 73141.9 (−0.51% 24h); TAO −3.91 / SUI −3.35 / TRX −2.54 / FARTCOIN −2.51 leading the downside. Drift deepening vs prior wake (BTC 73180→73142, TAO 277→251, AVAX 9.42→8.82).

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
- **All clear. Trading authorized — but regime gate (rule 5a) still vetoes entries.** Account flat. No active 5b cooldowns. routine-01-overnight 2026-05-29T13:30Z (on-time): 0 trades / $0 PnL, 1/15 positive (HYPE +0.83 only), median −1.19% → SBD active for 3rd consecutive wake. Defensive 9-EMA two-bar exit applies but book flat → $0 captured. Next entry-scan opportunity: routine-02-midday 2026-05-29T20:00Z (position-management only, no entries by spec); real next entry-scan = routine-03-eod 2026-05-30T04:00Z (last trading day of May for EOD scope → archive sweep due).

## Pending exit triggers

(no open positions)

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | ≈ +2.4% (approx) | ≈ −3% (approx) | ≈ +5% (approx) | BULL ahead (approx) |
| 30d | — | — | — | — |
| 90d | — | — | — | — |

(7d figures approximate — precise reference-price computation deferred to routine #4. 30d window pre-dates BULL inception 2026-04-20; first computable 2026-05-20.)
