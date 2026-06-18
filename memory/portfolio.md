# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-06-18T04:11Z routine-03-eod (PT label 2026-06-17 Wed, on-schedule cron fire — cron `0 21 * * 1-5` PT = 04:00 UTC). **No entries, no exits this wake** — flat into close. EOD entry scan: regime **5a FAIL** (1/15 positive 24h, median −3.37%) **AND 5a-SBD ACTIVE** (positives ≤1, median ≤ −1.0%). All new entries rejected by regime gate; technical pass would have left only TRX (R4a-failed sub-$2M), so net entries = 0 regardless. State unchanged from midday: equity **$10,231.74**, day **−3.60%**, drawdown **5.92%**, loss streak **3 trading days** (cap 7). 5b cooldowns active: SOL→2026-06-18T18:00Z, HYPE→2026-06-18T12:00Z. **Mandatory EOD Telegram card sent** per routine §NOTIFY.

> **Prior rebuild:** 2026-06-17T20:10Z routine-02-midday. SOL stop-out intrabar replay on 18:00Z bar (fill $72.1927). Net −$199.87 / −1.28R. Equity to $10,231.74, DD 5.92%, day −3.60%.

> **Prior rebuild (06-17 EOD label 06-16):** 2026-06-17T04:11Z routine-03-eod. HYPE EOD entry @ $74.4972 56.342770 units, stop $71.6714, target $85.8004.

## Account

- Starting equity: **$10,000.00**
- Cash: **$10,231.74** (was $2,730.55; SOL stop-out: +$7,540.82 gross proceeds, -$39.63 round-trip commission = net flow -$199.87)
- Realized PnL (all-time): **+$231.74** ($431.61 prior + -$199.87 SOL today)
  - [archived earlier rows trimmed for brevity — full ledger preserved in trade_log.md]
  - HYPE −$58.18 (exit-stop-hit 2026-05-06T15:00Z, −1.02R)
  - BTC +$1.42 (exit-ema-cross 2026-05-06T19:00Z, +0.06R)
  - LTC −$48.58 (exit-stop-hit 2026-05-07T01:00Z, −1.03R)
  - XRP −$37.68 (exit-stop-hit 2026-05-07T14:00Z, −1.05R)
  - LINK +$103.03 (exit-ema-cross 2026-05-07T20:00Z, +1.69R)
  - SOL +$585.35 (exit-4R-target 2026-05-11T19:00Z, +4.03R)
  - XRP −$21.92 (exit-ema-cross 2026-05-15T04:00Z, −0.14R) — corrected
  - HYPE +$413.62 (missed-scheduler replay exit-4R-target 2026-05-21T08:00Z, +4.04R)
  - TAO −$29.84 (missed-scheduler replay exit-ema20-confirm 2026-05-22T01:00Z, −0.50R)
  - HYPE −$33.98 (missed-scheduler replay exit-ema20-confirm 2026-05-22T02:00Z, −0.29R)
  - SOL −$45.64 (missed-scheduler replay exit-stop-hit 2026-05-22T15:00Z, −1.43R)
  - AVAX −$35.83 (missed-scheduler replay exit-ema20-confirm 2026-05-22T16:00Z, −0.94R)
  - BTC −$33.70 (exit-stop-hit 2026-05-25T22:00Z, −1.07R)
  - TAO −$114.75 (missed-scheduler replay exit-ema20-confirm 2026-05-26T18:00Z, −0.58R)
  - XRP −$101.40 (missed-scheduler replay exit-ema20-confirm 2026-05-30T23:00Z, −0.65R)
  - TAO +$621.22 (missed-scheduler replay exit-4R-target 2026-06-13T09:00Z, +4.04R)
  - BTC −$47.27 (missed-scheduler replay exit-ema20-confirm 2026-06-14T13:00Z, −0.60R)
  - ETH −$214.33 (missed-scheduler replay exit-stop-hit 2026-06-16T15:00Z, −1.32R)
  - HYPE −$182.64 (missed-scheduler replay exit-stop-hit 2026-06-17T12:00Z, −1.15R)
  - SOL −$199.87 (exit-stop-hit intrabar replay 2026-06-17T18:00Z, −1.28R)
- Unrealized PnL (open positions): **$0.00** (no open positions)
- Position values (MTM): **$0.00**
- Current equity (cash + positions MTM): **$10,231.74**
- Equity peak: **$10,875.85** (set 2026-06-13T09:00Z at TAO 4R close — unchanged)
- Drawdown from peak: **5.92%** ($644.11 below peak)
- Since-inception return: **+2.32%** ($10,231.74 / $10,000 − 1)

## Open positions

(none)

Portfolio risk-at-moment: **0.00%** of equity (cap 4%, full 4% headroom).
Open positions: **0 / 8** (strategy v0.4 max-concurrent 4 → 0/4 used; cluster {BTC,ETH,SOL,TAO,AVAX,SUI,LINK} 0/2).

## Day summary — 2026-06-17 PT (Wed)

| Metric | Value |
|---|---|
| Day realized PnL | **−$382.51** (HYPE stop -$182.64 + SOL stop -$199.87) |
| Day unrealized PnL | **$0.00** (flat) |
| Day total PnL | **−$382.51** |
| Day % (vs $10,612.15 prior-day close) | **−3.60%** |
| Trades opened today | **1** (SOL/USD long @ 17:00Z bar close, stopped same session) |
| Trades closed today | **2** (HYPE/USD stop-out @ 12:00Z; SOL/USD stop-out @ 18:00Z bar) |
| Win rate today | **0%** (0/2 closed) |
| Equity (current) | **$10,231.74** |
| Equity peak (realized) | **$10,875.85** (unchanged) |
| Drawdown from peak | **5.92%** |
| Loss streak | **3** trading days (BTC Sun, ETH Tue, Wed [HYPE+SOL]) |

## Active kill-switch state

- Daily realized 2026-06-17 PT: **−$382.51 / −3.60%** — loss cap 5% (1.40% headroom), CLEAR.
- Daily total (realized + unrealized) 2026-06-17 PT: **−$382.51 / −3.60%** — CLEAR.
- Consecutive losing trading days: **3** (BTC Sun, ETH Tue, Wed; cap 7, 4 of headroom).
- Max drawdown: **5.92%** from peak $10,875.85 (cap 25%, warn 12.5%, 6.58% to warn) — CLEAR.
- Equity floor: $10,231.74 > $7,500 floor — CLEAR.
- Regime gate (rule 5a): **FAIL** — 1/15 positive 24h, median −3.37% (< 4/15 floor). All new entries rejected this wake.
- Regime sub-state (rule 5a-SBD): **ACTIVE** — positives ≤1 AND median ≤ −1.0%. Exit 1-SBD (two-bar 9-EMA tightening) would apply to any open positions; BULL is flat so no defensive impact this wake. Per 5a-SBD instrumentation requirement, avoided-give-back = $0 (no open positions). First SBD activation since 2026-05-19 archive period.
- Active 5b cooldowns: **SOL 2026-06-17T18:00Z exit-stop-hit — 5b active until 2026-06-18T18:00Z**; **HYPE 2026-06-17T12:00Z exit-stop-hit — 5b active until 2026-06-18T12:00Z**.
- **All clear (kill switches).** routine-03-eod 2026-06-18T04:11Z (Wed 21:11 PT, on-schedule fire — PT label 2026-06-17): **0 OPEN**, **0 CLOSE**, **0 NEW ENTRIES** (regime 5a FAIL + SBD ACTIVE). Kraken REST clean via `scripts/indicators.py` (15 pairs × 720 1H bars + 720 4H bars converged). Watchdog 7 informational findings (1× heartbeat routine-07 94h, 6× variant stale-MTM 95h) — auto-alerted by `watchdog.py --telegram`, does not affect BULL state. **Telegram: mandatory EOD card sent** per routine §NOTIFY.

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

(no open positions — none active)

Next entry-eligible scan: routine-01-overnight Thu 2026-06-18T05:00 PT (= 2026-06-18T12:00Z cron). 5b cooldowns clear in order: HYPE at 12:00Z (overlap with overnight wake — eligible at exact bar), SOL at 18:00Z (clear by midday wake). Regime 5a/SBD re-evaluated each wake — may persist if cascade continues.

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | ≈ −0.74% realized (TAO +4.04R / +6.21%, BTC −0.60R / −0.43%, ETH −1.32R / −1.98%, HYPE −1.15R / −1.72%, SOL −1.28R / −1.91%) | ≈ +4.0% (BTC ~$63.3k → $65.8k over 7d) | ≈ −4.7% | BULL underperforms 7d (today's double stop-out compounds prior week's losses) |
| 30d | ≈ +2.32% (inception $10k 2026-04-20; window fully computable) | ≈ −19.1% (BTC 2026-05-13 ~$81.3k → today $65.8k) | ≈ +21.4% | BULL well ahead |
| 90d | — | — | — | not computable (BULL inception 2026-04-20 = 58 days ago; window first computable ~2026-07-19) |

(7d / 30d figures approximate. 30d outperformance compressed from yesterday's +23.4% by today's −3.60% day vs roughly flat BTC; still dominant +21.4%. Today's full reversal of the SOL entry — opened and stopped within ~2 hours of the entry-bar close — is the key event for the lessons file: the rule-8 cash-fallback entry got knocked out same-session by an SBD-shaped intraday selloff that wasn't visible on the 16:00Z entry-scan bar.)
