# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-06-12T04:00Z routine-03-eod (Thu 21:00 PT on-schedule fire, cron `0 21 * * 1-5` PT in-window since 2026-06-11 = Thursday). Slot identity confirmed `bull-03-eod` (no mismatch vs the 2026-05-11 duplicate-skill regression guard). **MAJOR REGIME FLIP this wake.** Fresh `kraken_multi_ticker` 15/15 clean at the 21:00 PT pull: **15/15 positive on 24h % change**, median **+2.72% (HYPE)**. Sorted ascending: +0.28 (TRX) / +1.72 (XRP) / +1.84 (BTC) / +1.88 (ETH) / +2.11 (XDG) / +2.15 (NEAR) / +2.40 (LTC) / +2.72 (HYPE, median) / +2.98 (SOL) / +3.00 (LINK) / +3.01 (AVAX) / +3.03 (TAO) / +3.14 (SUI) / +3.17 (ADA) / +5.71 (FARTCOIN). Sharp reversal vs the 06-11T20:00Z midday print (1/15→15/15 positive, median −2.68%→+2.72%) — first uniformly-positive breadth print since the 06-01→06-09 synchronized breakdown began. Regime classification: **5a PASS** (15 ≥ 4 floor — first PASS since 06-01); **5a-SBD CLEARED** (15 > 1 positive, AND median +2.72 > −1.0 threshold — both conditions exited; SBD inactive for the first time in ~10 days). SBD's tightened 9-EMA exit override deactivates (still inert though — book flat). **Per-pair entry-rule scan (rules 1, 2, 2a, 3) executed:** BTC rank-1 → 1H close 62610.9 > 1H 20-EMA ~61769 (PASS rule 1), 1H RSI14 ≈ 57.9 (PASS rule 2 & 2a) — but **4H close 62610.9 < 4H 50-EMA ~63589 (FAIL rule 3)**. ETH rank-2 → 4H close 1651.35 < 4H 50-EMA ~1670 (FAIL rule 3). ADA rank-10 (strongest non-cluster mover +3.17%) → 4H close 0.16636 < 4H 50-EMA ~0.170 (FAIL rule 3). HYPE rank-4 → 4H close 55.09 < 4H 50-EMA ~58 (FAIL rule 3). **Pattern confirmed: all 15 pairs fail rule 3** — the 4H 50-EMA reflects ~8 days of pre-breakdown prices and the 1-day bounce has not yet reclaimed it. Strategy v0.4 is correctly conservative: 5a/5a-SBD gates designed to block longs *into* the breakdown have cleared, but rule 3 (4H trend filter) still gates *out* of the early recovery until the longer-timeframe trend confirms. **No new entry this wake** (rule 3 vetoes universally; rule 8 single-entry slot moot). Liquidity floors (rule 4a): FARTCOIN $1.15M < $2M floor, TRX $1.99M just-under floor — both excluded even if rule 3 had passed. **Book flat** (18th consecutive flat-book wake since XRP exit 2026-05-30T23:00Z, ~12 days). MTM inert (0 open positions); exit step inert (nothing to evaluate). Equity unchanged **$10,254.63** (cash-only). Day PnL **$0.00 / 0.00%**. Since-start **+2.55%** (53 days from inception 2026-04-20). Drawdown **4.42%** from peak $10,728.95 — unchanged. Consecutive losing trading days: 4 (zero-PnL day does not advance; still 1 L from informal warn-5). Kill switches all clear (DD 4.42% < 12.5% warn / 25% cap, equity > $7,500 floor, daily PnL $0 < 5% cap, loss-streak 4 < 7 cap, Kraken MCP AVAILABLE — 4th consecutive post-fix wake clean). `kraken_risk_flag` returns NO_DATA (informational only per 2026-06-09 fix note). **Telegram EOD card sent** (mandatory daily per routine #3 NOTIFY). BTC reference **$62,590** (+1.6% vs the prior EOD $61,602 print) — recovery underway but BULL stays defensively flat per rule 3 until the 4H trend confirms. 30d BULL-vs-BTC-hold delta ≈ **+25.4%** (BULL +2.55% vs BTC ≈ −22.9% from 30d-ago ~$81.2k). Next on-schedule wake: routine-01-overnight 2026-06-12T13:00Z (Fri 06:00 PT scheduled).

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

- Daily realized on 2026-06-11 PT trading day: **$0.00** (no closes today; last close was XRP exit 2026-05-30 PT, 12 days ago) — clear vs 5% loss cap.
- Consecutive losing trading days: 05-22 L, 05-25 L, 05-26 L, 05-30 L (05-27/28/29/31, 06-01 → 06-11 all no-realized-PnL → streak unchanged) → streak **4** (cap 7; warn at 5 informally — still 1 day from informal warn).
- Max drawdown: **4.42%** from peak $10,728.95 (cap 25%, warn 12.5%) — clear.
- Equity floor: $10,254.63 > $7,500 floor — OK.
- Regime gate (rule 5a) — **freshly measured this wake**: **15/15 positive**, median +2.72% (HYPE) → **5a PASS** (first PASS since 06-01, ~10 days of SBD/regime-fail cleared). **5a-SBD CLEARED** — both conditions (>1 positive AND median >−1.0) exited. SBD's tightened 9-EMA exit override deactivates. Per-pair rule 3 (4H close > 4H 50-EMA) **fails uniformly** — no new entries this wake despite 5a clearance.
- No active 5b cooldowns (XRP 2026-05-30 exit was ema20-confirm, not stop-hit — rule 5b inapplicable; >24h elapsed anyway).
- **All clear (kill switches).** routine-03-eod 2026-06-12T04:00Z (Thu 21:00 PT on-schedule fire): **0 OPEN, 0 CLOSE** (book flat → MTM + exit-check steps inert; per-pair entry-rule scan executed but rule 3 vetoed universally — recovery too young to clear 4H 50-EMA). Kraken MCP available (15/15 ticker clean — 4th post-fix scheduled wake confirmation). Drawdown 4.42% unchanged. Loss-streak 4 unchanged (no closes today, zero-PnL day does not advance). Daily PnL $0. Telegram EOD card sent (mandatory daily). Next on-schedule wake: routine-01-overnight 2026-06-12T13:00Z (Fri 06:00 PT scheduled).

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
| 7d | ≈ 0.0% (held flat at $10,254.63 across the 7d window) | ≈ −1.4% (BTC 2026-06-04 ~$63.5k → today $62.6k) | ≈ +1.4% | BULL barely ahead |
| 30d | ≈ +2.55% (inception $10k 2026-04-20; window fully computable) | ≈ −22.9% (BTC 2026-05-12 ~$81.2k → today $62.6k) | ≈ +25.4% | BULL well ahead |
| 90d | — | — | — | not computable (BULL inception 2026-04-20 = 53 days ago) |

(7d and 30d figures approximate — precise reference-price computation deferred to routine #4. 90d window first computable ~2026-07-19. BTC reference today **$62,590** — BTC +1.6% vs the prior EOD $61,602 print, part of the broad 15/15-positive bounce that flipped 5a/SBD this wake. 7d window now includes the 06-04 bottom, so BTC-hold appears milder here than the 30d figure; the 30d delta is the better representation of BULL's defensive-flat-book through the full breakdown. The strategy stayed flat through the bottom (5a/SBD blocked entries) and now stays flat through the early bounce (rule 3 blocks entries until 4H 50-EMA reclaims) — designed defensive sequence per W21-F.)
