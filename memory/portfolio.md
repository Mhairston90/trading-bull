# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-06-19T20:07Z routine-02-midday (PT label 2026-06-19 Fri, scheduler fired ~07 min late at 20:07Z — cron `0 13 * * 1-5` PT = 20:00 UTC). **Position management only — no entries permitted per routine spec.** Portfolio flat at wake; **MTM and exit-check skipped (no open positions to evaluate)**. Equity **$10,231.74** (unchanged), drawdown **5.92%** (unchanged — flat for 4 consecutive wakes since SOL stop-out 2026-06-17T18:00Z), loss streak **3 trading days** (cap 7; Fri flat through midday, streak holds). All kill switches CLEAR. Regime gate 5a/SBD not re-evaluated (no entry decision at midday); next re-check at routine-03-eod Fri 21:00 PT = Sat 04:00 UTC.

> **Prior rebuild:** 2026-06-19T15:39Z routine-01-overnight. Regime 5a FAIL (2/15 positive, median −1.86%) + SBD CLEAR (positives = 2 > 1 ceiling; SBD lifted after 4-wake episode). 0 entries, 0 exits.

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

## Day summary — 2026-06-19 PT (Fri, open)

| Metric | Value |
|---|---|
| Day realized PnL | **$0.00** (no closes yet) |
| Day unrealized PnL | **$0.00** (flat at wake) |
| Day total PnL | **$0.00** |
| Day % (vs $10,231.74 prior-day close) | **0.00%** |
| Trades opened today | **0** |
| Trades closed today | **0** |
| Win rate today | n/a (no closes) |
| Equity (current) | **$10,231.74** |
| Equity peak (realized) | **$10,875.85** (unchanged) |
| Drawdown from peak | **5.92%** |
| Loss streak | **3** trading days (BTC Sun, ETH Tue, Wed [HYPE+SOL]; Thu flat) — Fri opens flat, streak still holds at 3 |

## Active kill-switch state

- Daily realized 2026-06-19 PT: **$0.00 / 0.00%** — loss cap 5% (5.00% headroom), CLEAR.
- Daily total (realized + unrealized) 2026-06-19 PT: **$0.00 / 0.00%** — CLEAR.
- Consecutive losing trading days: **3** (BTC Sun, ETH Tue, Wed; cap 7, headroom 4). Thu closed flat, Fri opens flat — streak holds at 3.
- Max drawdown: **5.92%** from peak $10,875.85 (cap 25%, warn 12.5%, 6.58% to warn) — CLEAR.
- Equity floor: $10,231.74 > $7,500 floor — CLEAR.
- Regime gate (rule 5a): **FAIL** — 2/15 positive 24h (LTC +0.23%, TRX +0.34%), median −1.86% (< 4/15 floor). No entries at overnight scan.
- Regime sub-state (rule 5a-SBD): **CLEAR** — positives = 2 (> 1 ceiling). **SBD lifted after 4 consecutive wakes** (2026-06-18T04:11Z EOD → 14:05Z overnight → 20:07Z midday → 05:16Z EOD; clear now at 15:39Z). Exit 1 reverts from 9-EMA two-bar (SBD) to 20-EMA two-bar (default). No open positions affected.
- Active 5b cooldowns: none.
- **All clear (kill switches).** routine-02-midday 2026-06-19T20:07Z (Fri 13:07 PT): **0 OPEN**, **0 CLOSE**, **0 MTM action** (flat — no positions to mark or exit-check). Regime gate not re-evaluated at midday (entry decision belongs to routines #1/#3). Drawdown trajectory: 5.92% × 4 consecutive wakes (no movement since SOL stop-out 2026-06-17T18:00Z). Halfway-to-warn ($9,516.37) is $715.37 below current cash.

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

Next entry-eligible scan: routine-03-eod Fri 2026-06-19T04:00Z PT = 04:00Z UTC Sat (routine-02-midday is read-only, no entries). No 5b cooldowns active. Regime 5a/SBD re-evaluated each wake — SBD cleared this wake (positives = 2); 5a still gating at 2/15 (needs ≥4 for entries).

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | ≈ −0.74% realized (unchanged from EOD; no new realized today) | ≈ +3% (BTC drifting; 7d window ending today) | ≈ −3.7% | BULL underperforms 7d |
| 30d | ≈ +2.32% (inception $10k 2026-04-20; window fully computable) | ≈ −21% (BTC 2026-05-13 ~$81.3k → today ~$63.9k) | ≈ +23.3% | BULL well ahead |
| 90d | — | — | — | not computable (BULL inception 2026-04-20 = 59 days ago; window first computable ~2026-07-19) |

(7d / 30d figures approximate. Today's regime cascade (BTC ~$63.9k, −2.0% 24h) widens 30d BULL outperformance since BULL is flat while BTC continues bleeding. Day starts flat; metrics update on next wake if entries are eligible.)
