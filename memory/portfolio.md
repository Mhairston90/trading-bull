# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-06-19T05:16Z routine-03-eod (PT label 2026-06-18 Thu, scheduler fired ~22:16 PT — cron `0 21 * * 1-5` PT). **No entries, no exits this wake** — portfolio flat at wake (no MTM/exit work). Regime sweep (Kraken multi-ticker @ ~05:16Z UTC): **5a FAIL** (1/15 positive — TRX +0.06% — median −1.71%) **AND 5a-SBD ACTIVE** (positives ≤1 AND median ≤ −1.0%) — **fourth consecutive wake under SBD**. Conditions partially recovered from midday (median −3.21% → −1.71%) but SBD threshold still breached. State unchanged: equity **$10,231.74**, drawdown **5.92%**, loss streak **3 trading days** (cap 7 — Thu closes flat so streak holds). All kill switches CLEAR. 5b cooldowns: all clear.

> **Prior rebuild:** 2026-06-18T20:07Z routine-02-midday. Regime 5a FAIL + SBD ACTIVE (1/15 positive — NEAR — median −3.21%). 0 entries, 0 exits.

## Account

- Starting equity: **$10,000.00**
- Cash: **$10,231.74** (unchanged from prior wake; no trades)
- Realized PnL (all-time): **+$231.74**
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

## Day summary — 2026-06-18 PT (Thu, closed)

| Metric | Value |
|---|---|
| Day realized PnL | **$0.00** (no closes) |
| Day unrealized PnL | **$0.00** (flat at close) |
| Day total PnL | **$0.00** |
| Day % (vs $10,231.74 prior-day close) | **0.00%** |
| Trades opened today | **0** |
| Trades closed today | **0** |
| Win rate today | n/a (no closes) |
| Equity (current) | **$10,231.74** |
| Equity peak (realized) | **$10,875.85** (unchanged) |
| Drawdown from peak | **5.92%** |
| Loss streak | **3** trading days (BTC Sun, ETH Tue, Wed [HYPE+SOL]) — Thu flat, streak holds at 3 |

## Active kill-switch state

- Daily realized 2026-06-18 PT: **$0.00 / 0.00%** — loss cap 5% (5.00% headroom), CLEAR.
- Daily total (realized + unrealized) 2026-06-18 PT: **$0.00 / 0.00%** — CLEAR.
- Consecutive losing trading days: **3** (BTC Sun, ETH Tue, Wed; cap 7, 4 of headroom). Thu closed flat — streak holds at 3.
- Max drawdown: **5.92%** from peak $10,875.85 (cap 25%, warn 12.5%, 6.58% to warn) — CLEAR.
- Equity floor: $10,231.74 > $7,500 floor — CLEAR.
- Regime gate (rule 5a): **FAIL** — 1/15 positive 24h (TRX +0.06%), median −1.71% (< 4/15 floor). No entries at EOD scan.
- Regime sub-state (rule 5a-SBD): **ACTIVE** — positives ≤1 AND median ≤ −1.0% (1/15 positive, median −1.71%). **Fourth consecutive wake under SBD** (activated 2026-06-18T04:11Z EOD, persisted through 14:05Z overnight, 20:07Z midday, now). Conditions partially recovered from midday (median −3.21% → −1.71%) but threshold still breached. Exit 1-SBD would apply to open positions; BULL is flat, no defensive impact. Avoided-give-back ledger this wake = $0.
- Active 5b cooldowns: none.
- **All clear (kill switches).** routine-03-eod 2026-06-19T05:16Z (Thu 22:16 PT label 2026-06-18): **0 OPEN**, **0 CLOSE**, **0 NEW ENTRIES** (5a FAIL bars all entries). Kraken multi-ticker clean (15/15 pairs returned). Watchdog: 7 stale findings (routine-07 heartbeat 119h, six variant portfolios MTM stale — informational, not actionable).

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

Next entry-eligible scan: routine-01-overnight Fri 2026-06-19 (cron `0 7 * * 1-5` PT = 14:00Z). No 5b cooldowns active. Regime 5a/SBD re-evaluated each wake — SBD will clear if Fri rally lifts positives ≥2 OR median above −1.0%.

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | ≈ −0.74% realized (unchanged from EOD; no new realized today) | ≈ +3% (BTC drifting; 7d window ending today) | ≈ −3.7% | BULL underperforms 7d |
| 30d | ≈ +2.32% (inception $10k 2026-04-20; window fully computable) | ≈ −21% (BTC 2026-05-13 ~$81.3k → today ~$63.9k) | ≈ +23.3% | BULL well ahead |
| 90d | — | — | — | not computable (BULL inception 2026-04-20 = 59 days ago; window first computable ~2026-07-19) |

(7d / 30d figures approximate. Today's regime cascade (BTC ~$63.9k, −2.0% 24h) widens 30d BULL outperformance since BULL is flat while BTC continues bleeding. Day starts flat; metrics update on next wake if entries are eligible.)
