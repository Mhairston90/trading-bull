# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-06-11T04:00Z routine-03-eod (Wed 21:00 PT on-schedule fire; EOD scope = 2026-06-10 PT trading day). **Second post-MCP-fix scheduled wake** (after the 06-10T17:50Z routine-01-overnight, which was the first). Fresh `kraken_multi_ticker` 15/15 clean at the 21:00 PT close: **0/15 positive on 24h % change, median −2.54% (LINK)**. Sorted: −5.81 / −4.72 / −4.31 / −3.15 / −3.07 / −2.99 / −2.95 / −2.54 / −2.12 / −1.83 / −1.73 / −1.03 / −0.38 / −0.38 / −0.14. Tape print materially unchanged from this morning's overnight pull (≈10h prior) — the SBD regime persists. **Rule 5a FAIL** (0 < 4 positive floor) → all 15 pairs rejected at the wake-level veto, per-pair entry-rule scan skipped. **5a-SBD ACTIVE** (≤1/15 positive AND median −2.54 ≤ −1.0 threshold; 1.54pts of headroom below trigger). SBD's tightened 9-EMA exit override remains inert — book flat (16th+ consecutive flat-book wake since XRP exit 2026-05-30T23:00Z; no MTM, no exit checks possible). No technical/news/sentiment passes run (vacuous — 5a uniformly blocks before per-pair eval). No trades this wake (0 opened, 0 closed). Equity unchanged $10,254.63 (cash-only). Day PnL $0 / 0.00%. Since-start +2.55% (51 days). Drawdown 4.42% from peak $10,728.95 — unchanged. Consecutive losing trading days: 4 (06-01 → 06-10 all zero-PnL; warn-5 still one L away). Kill switches all clear (DD 4.42% < 12.5% warn / 25% cap, equity > $7,500 floor, daily PnL $0 < 5% cap, loss-streak 4 < 7 cap, Kraken MCP AVAILABLE). `kraken_risk_flag` returns NO_DATA (daily_risk_flag.json not mirrored at scripts/ location — informational only per 2026-06-09 fix note; not a kill switch since multi_ticker succeeded). **Telegram EOD card sent** (mandatory daily card per routine #3 NOTIFY rule). BTC reference $61,602.10 — flat-book through the 06-01→ongoing synchronized breakdown widens the BULL-vs-BTC-hold delta to ≈+26.8% over the 30d window (designed-in defensive outcome of rules 5a / 5a-SBD per the W21-F fragility audit). No monthly archive this wake (last trading day of June = 2026-06-30). No lessons appended (SBD pattern already captured by 2026-05-19 lesson). Next on-schedule wake: routine-01-overnight 2026-06-11T13:00Z (Thu 06:00 PT scheduled).

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

- Daily realized on 2026-06-10 PT trading day: **$0.00** (no closes today; XRP exit was 2026-05-30 PT, 11 days ago) — clear vs 5% loss cap.
- Consecutive losing trading days: 05-22 L, 05-25 L, 05-26 L, 05-30 L (05-27/28/29/31, 06-01/02/03 no-realized-PnL → streak unchanged) → streak **4** (cap 7; warn at 5 informally — still 1 day from informal warn).
- Max drawdown: **4.42%** from peak $10,728.95 (cap 25%, warn 12.5%) — clear.
- Equity floor: $10,254.63 > $7,500 floor — OK.
- Regime gate (rule 5a) — **freshly measured this wake**: 0/15 positive, median −2.54% → 5a FAIL, 5a-SBD ACTIVE. SBD's tightened 9-EMA exit override is inert (book flat — no open positions to apply to). Avoided-give-back: vacuous (no open positions to compare 9-EMA vs 20-EMA exits on).
- No active 5b cooldowns (XRP 2026-05-30 exit was ema20-confirm, not stop-hit — rule 5b inapplicable; >24h elapsed anyway).
- **All clear (kill switches).** routine-03-eod 2026-06-11T04:00Z (Wed 21:00 PT on-schedule fire; EOD scope = 2026-06-10 PT): **0 OPEN, 0 CLOSE** (book flat → MTM + exit-check steps inert; entry-scan vetoed wake-level by 5a). Kraken MCP available (15/15 ticker clean — 2nd post-fix scheduled wake confirmation). Drawdown 4.42% unchanged. Loss-streak 4 unchanged (no closes today, zero-PnL day does not advance). Daily PnL $0. Telegram EOD card sent (mandatory daily). Next on-schedule wake: routine-01-overnight 2026-06-11T13:00Z (Thu 06:00 PT scheduled).

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
| 7d | ≈ −4.42% (from peak $10,728.95 set 2026-05-21) | ≈ −20.6% (BTC 2026-06-03 ~$77.6k → today $61.6k) | ≈ +16.2% | BULL ahead |
| 30d | ≈ +2.55% (inception $10k 2026-04-20; window fully computable) | ≈ −24.2% (BTC 2026-05-10 ~$81.2k → today $61.6k) | ≈ +26.8% | BULL ahead |
| 90d | — | — | — | not computable (BULL inception 2026-04-20 = 51 days ago) |

(7d and 30d figures approximate — precise reference-price computation deferred to routine #4. 90d window first computable ~2026-07-19. BTC reference today **$61,602** — BTC has dropped another ≈ −9.2% since the 06-09 reference of $67,881, widening BULL's defensive-flat-book delta further. Flat-book through a synchronized breakdown is the designed-in protective outcome of rules 5a/5a-SBD per the W21-F fragility audit.)
