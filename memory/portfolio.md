# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-06-05T20:00Z routine-02-midday (Fri 13:00 PT scheduled cron, on-time). Book still flat — no MTM, no exit checks (0 open positions, 8th consecutive flat-book wake since XRP exit 2026-05-30T23:00Z). Midday entry scan forbidden by routine design (position-management only). Kraken MCP not loaded (9th consecutive wake without it since 2026-06-02T15:00Z) — informational only, no impact since no positions to mark. TradingView MCP registered but unused (no positions to quote). No trades this wake (0 opened, 0 closed). Equity unchanged $10,254.63 (cash-only). Day PnL $0 / 0.00%. Drawdown 4.42% from peak $10,728.95 — unchanged. Consecutive losing trading days: 4 (informal warn at 5 still one closing-L away). Kill switches all clear (DD 4.42% < 12.5% warn / 25% cap, equity $10,254.63 > $7,500 floor, daily PnL $0 < 5% cap, loss-streak 4 < 7 cap). Silent Telegram (no kill-switch trip, no exit event, DD below halfway-warn). Prior wake (2026-06-05T04:11Z EOD): flat, MCP dual-degraded, EOD entry scan skipped, EOD card sent.

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

- Daily realized on 2026-06-04 PT trading day: **$0.00** (no closes today; XRP exit was 2026-05-30 PT, 5 days ago) — clear vs 5% loss cap.
- Consecutive losing trading days: 05-22 L, 05-25 L, 05-26 L, 05-30 L (05-27/28/29/31, 06-01/02/03 no-realized-PnL → streak unchanged) → streak **4** (cap 7; warn at 5 informally — still 1 day from informal warn).
- Max drawdown: **4.42%** from peak $10,728.95 (cap 25%, warn 12.5%) — clear.
- Equity floor: $10,254.63 > $7,500 floor — OK.
- Regime gate (rule 5a) — not re-evaluated this wake (midday is position-management only, no entry scan; last observed 2026-06-03 indicated 5a fail / 5a-SBD active). Will be refreshed next overnight/EOD wake. SBD's tightened 9-EMA exit override is inert (book flat — no open positions to apply to).
- No active 5b cooldowns (XRP 2026-05-30 exit was ema20-confirm, not stop-hit — rule 5b inapplicable; >24h elapsed anyway).
- **All clear (kill switches).** routine-02-midday 2026-06-05T20:00Z (Fri 13:00 PT on-time): **0 OPEN, 0 CLOSE** (book flat → MTM step inert; no exit checks possible; midday entry scan forbidden by design). Kraken MCP not loaded (informational — no positions to mark); TradingView MCP registered, unused. Drawdown 4.42% unchanged. Loss-streak 4 unchanged (no closes). Silent Telegram (no kill-switch trip, no exits, DD below halfway-warn). Next wake: routine-03-eod 2026-06-06T04:00Z (Fri 21:00 PT scheduled).

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
| 7d | ≈ −4.42% (from peak $10,728.95 set 2026-05-21) | ≈ −12.5% (BTC 2026-05-26 ~$77.6k → today $67.9k) | ≈ +8.1% | BULL ahead |
| 30d | ≈ +2.55% (inception $10k 2026-04-20; window now fully computable) | ≈ −16.4% (BTC 2026-05-03 ~$81.2k → today $67.9k) | ≈ +18.9% | BULL ahead |
| 90d | — | — | — | not computable (BULL inception 2026-04-20 = 43 days ago) |

(7d and 30d figures approximate — precise reference-price computation deferred to routine #4. 90d window first computable ~2026-07-19. BTC reference today $67,881 — overnight breakdown widened the BULL vs BTC-hold delta materially as BULL stayed flat through the −4.82% BTC 24h.)
