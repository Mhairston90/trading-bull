# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-06-18T14:05Z routine-01-overnight (PT label 2026-06-18 Thu, on-schedule cron fire — cron `0 6 * * 1-5` PT = 13:00 UTC). **No entries, no exits this wake** — flat into Thursday session. Entry scan: regime **5a FAIL** (0/15 positive 24h, median −2.26%) **AND 5a-SBD ACTIVE** (positives ≤1, median ≤ −1.0%) — second consecutive wake under SBD. Zero technical candidates (no pair passes R1+R2 simultaneously); regime gate moot. State unchanged from EOD: equity **$10,231.74**, drawdown **5.92%**, loss streak **3 trading days** (cap 7). Day 2026-06-18 PT starts flat. 5b cooldowns: HYPE cleared 12:00Z, SOL active until 18:00Z.

> **Prior rebuild:** 2026-06-18T04:11Z routine-03-eod (PT label 2026-06-17). EOD scan: regime 5a FAIL + SBD ACTIVE. Day 06-17 close: −$382.51 / −3.60% (HYPE stop −$182.64 + SOL stop −$199.87). Equity $10,231.74, DD 5.92%, loss streak 3.

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

## Day summary — 2026-06-18 PT (Thu, in-progress)

| Metric | Value |
|---|---|
| Day realized PnL | **$0.00** (no closes) |
| Day unrealized PnL | **$0.00** (flat) |
| Day total PnL | **$0.00** |
| Day % (vs $10,231.74 prior-day close) | **0.00%** |
| Trades opened today | **0** |
| Trades closed today | **0** |
| Win rate today | n/a (no closes) |
| Equity (current) | **$10,231.74** |
| Equity peak (realized) | **$10,875.85** (unchanged) |
| Drawdown from peak | **5.92%** |
| Loss streak | **3** trading days (BTC Sun, ETH Tue, Wed [HYPE+SOL]) — pending Thu close |

## Active kill-switch state

- Daily realized 2026-06-18 PT: **$0.00 / 0.00%** — loss cap 5% (5.00% headroom), CLEAR.
- Daily total (realized + unrealized) 2026-06-18 PT: **$0.00 / 0.00%** — CLEAR.
- Consecutive losing trading days: **3** (BTC Sun, ETH Tue, Wed; cap 7, 4 of headroom). Thu starts flat — streak holds at 3 unless realized loss accrues by EOD.
- Max drawdown: **5.92%** from peak $10,875.85 (cap 25%, warn 12.5%, 6.58% to warn) — CLEAR.
- Equity floor: $10,231.74 > $7,500 floor — CLEAR.
- Regime gate (rule 5a): **FAIL** — 0/15 positive 24h, median −2.26% (< 4/15 floor). All new entries rejected this wake.
- Regime sub-state (rule 5a-SBD): **ACTIVE** — positives ≤1 AND median ≤ −1.0% (0/15 positive, median −2.26%). Second consecutive wake under SBD (activated 2026-06-18T04:11Z EOD). Exit 1-SBD (two-bar 9-EMA tightening) would apply to any open positions; BULL is flat so no defensive impact this wake. Avoided-give-back ledger this wake = $0 (no open positions).
- Active 5b cooldowns: **HYPE cleared 2026-06-18T12:00Z**; **SOL 2026-06-17T18:00Z exit-stop-hit — 5b active until 2026-06-18T18:00Z** (~4h remaining at wake time).
- **All clear (kill switches).** routine-01-overnight 2026-06-18T14:05Z (Thu 07:05 PT, on-schedule fire): **0 OPEN**, **0 CLOSE**, **0 NEW ENTRIES** (regime 5a FAIL + SBD ACTIVE; zero technical candidates regardless — no pair passes R1+R2 simultaneously). Kraken REST clean via `scripts/indicators.py` (15 pairs × 720 1H bars + 720 4H bars converged). Watchdog 7 informational findings (1× heartbeat routine-07 104h, 6× variant stale-MTM 105h) — auto-alerted by `watchdog.py --telegram`, does not affect BULL state.

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

Next entry-eligible scan: routine-02-midday Thu 2026-06-18T12:00 PT (= 2026-06-18T19:00Z cron). 5b cooldown for SOL clears at 18:00Z (overlap with midday wake — eligible at midday). Regime 5a/SBD re-evaluated each wake — SBD may persist if cascade continues, or clear if any rally lifts positives ≥2 OR median above −1.0%.

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | ≈ −0.74% realized (unchanged from EOD; no new realized today) | ≈ +3% (BTC drifting; 7d window ending today) | ≈ −3.7% | BULL underperforms 7d |
| 30d | ≈ +2.32% (inception $10k 2026-04-20; window fully computable) | ≈ −21% (BTC 2026-05-13 ~$81.3k → today ~$63.9k) | ≈ +23.3% | BULL well ahead |
| 90d | — | — | — | not computable (BULL inception 2026-04-20 = 59 days ago; window first computable ~2026-07-19) |

(7d / 30d figures approximate. Today's regime cascade (BTC ~$63.9k, −2.0% 24h) widens 30d BULL outperformance since BULL is flat while BTC continues bleeding. Day starts flat; metrics update on next wake if entries are eligible.)
