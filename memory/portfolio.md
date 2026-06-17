# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-06-17T04:11Z routine-03-eod (PT label 2026-06-16, **on-schedule cron fire** `0 21 * * 1-5` PT). **EOD entry scan executed:** HYPE/USD opened long. Indicators table (720-bar converged): HYPE R1 PASS (close $74.46 > EMA20 by +$1.245), R2 PASS (RSI14 59.8 = +4.85 over 55 floor), R2a OK (RSI 59.8 < 80), R3 PASS (4H close > 4H 50-EMA by +$10.04 / +15.6% margin), R4 OK (720 bars history both 1H/4H), R4a OK ($38.08M 24h notional > $2.0M floor), R5 OK (no existing position), R5a PASS (6/15 positive 24h, median -0.11%), R5a-SBD CLEAR (6 > 1 positive AND median -0.11% > -1.0%), R5b OK (no recent HYPE stop; only ETH on 5b cooldown till 2026-06-17T15:00Z), R6 OK (0/4 open), R6a OK (HYPE not in BTC-correlated cluster), R7 OK (1.50% per-trade vs 4% portfolio cap), R8 OK (1 entry this wake). News: skipped per time budget — informational only, does not veto in v0.4. Sentiment: Kraken `kraken_spread` 04:11:58Z shows tight 1-3¢ spread on $75.13 = ~2.7 bps — supportive. Entry fill = 1H close $74.46 × 1.0005 = **$74.4972** (0.05% adverse slippage per `skills/decide.md`); ATR14 = $1.4129; stop distance = 2×ATR = $2.8258; stop = **$71.6714**; target = entry + 4 × stop distance = **$85.8004**. Size = 1.5% × $10,614.25 / $2.8258 = **56.342770 units**. R-risk = $159.21. Cash post-entry = $10,614.25 - 56.342770 × $74.4972 = **$6,416.87**. Position MTM @ 03:00Z bar close $74.46 = $4,195.28; unrealized PnL = **-$2.10** (entry slippage only, position not yet moved adversely). Day P&L vs prior day close $10,828.58 = **-$216.43 / -2.00%** (ETH realized -$214.33 + HYPE unrealized -$2.10). **Equity:** $10,612.15. **Peak unchanged.** **Drawdown 2.42%** — CLEAR. **Watchdog (this wake):** 7 informational findings — A heartbeat (routine-07 70h vs 30h threshold) + 6 D stale-MTM on variants (v0.12-sbd-exit, v0.13-trend-confirm, v0.14-recovery-trend, v0.3-vol-compression, v0.5-cluster-cap-tight, v0.7-vol-comp-defensive — all 71h since last MTM, due to weekend/Monday scheduler gap). Telegram alert auto-sent by watchdog. Variant lag is not a BULL-state issue; flagged for routine-07 catch-up. All kill switches CLEAR. **Telegram: EOD card sent** per routine §NOTIFY (mandatory daily). Next routine: routine-01-overnight Wed 06-17T13:00Z (cron `0 6 * * 1-5` PT).

> **Prior rebuild:** 2026-06-16T20:08Z routine-02-midday. ETH/USD 5.1162 stop-out exit replay 2026-06-16T15:00Z via Exit rule 2 (intrabar stop pierce). Orphan-write entry @ 12:00Z handled per source-of-truth rule. Realized -1.32R / -$214.33 net. Equity $10,614.25, DD 2.40%, loss streak 1→2.

> **Prior rebuild (Sun AM):** 2026-06-14T17:14Z routine-01-overnight. BTC/USD 0.168 stop-out exit replay 2026-06-14T13:00Z via Exit rule 1 (W22-G two-bar EMA20 confirm). Realized -0.60R / -$47.27 net. Equity $10,828.58, DD 0.43%, loss streak 0→1.

## Account

- Starting equity: **$10,000.00**
- Cash: **$6,416.87** (was $10,614.25; -$4,197.38 entry cost for HYPE)
- Realized PnL (all-time): **+$614.25** (unchanged this wake — HYPE entry only)
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
- Unrealized PnL (open positions): **−$2.10** (HYPE @ MTM $74.46)
- Position values (MTM): **$4,195.28** (HYPE 56.342770 × $74.46)
- Current equity (cash + positions MTM): **$10,612.15**
- Equity peak: **$10,875.85** (set 2026-06-13T09:00Z at TAO 4R close — unchanged)
- Drawdown from peak: **2.42%** ($263.70 below peak)
- Since-inception return: **+6.12%** ($10,612.15 / $10,000 − 1)

## Open positions

| Pair | Side | Size | Entry | Stop | Target | Unrealized PnL | R-risk | Opened |
|------|------|------|-------|------|--------|----------------|--------|--------|
| HYPE/USD | long | 56.342770 | $74.4972 | $71.6714 | $85.8004 | −$2.10 (MTM $74.46) | $159.21 (1.50% eq) | 2026-06-17T04:00Z |

Portfolio risk-at-moment: **1.50%** of equity (cap 4%, 2.5% headroom).
Open positions: **1 / 8** (strategy v0.4 max-concurrent 4 → 1/4 used; cluster {BTC,ETH,SOL,TAO,AVAX,SUI,LINK} 0/2 — HYPE not in cluster).

## Day summary — 2026-06-16 PT (Tue, EOD)

| Metric | Value |
|---|---|
| Day realized PnL | **−$214.33** (ETH stop-hit replay) |
| Day unrealized PnL | **−$2.10** (HYPE entry slippage, no adverse move yet) |
| Day total PnL | **−$216.43** |
| Day % (vs $10,828.58 prior-day close) | **−2.00%** |
| Trades opened today | **2** (ETH 12:00Z orphan-write entry; HYPE 04:00Z Wed UTC EOD entry — PT date 06-16) |
| Trades closed today | **1** (ETH 5.1162 long @ 14:00Z bar via intrabar stop pierce) |
| Win rate today | **0%** (0/1 closed) |
| Equity at EOD | **$10,612.15** |
| Equity peak (realized) | **$10,875.85** (unchanged) |
| Drawdown from peak | **2.42%** |
| Loss streak | **2** trading days (BTC Sun −0.60R, ETH Tue −1.32R) |

## Active kill-switch state

- Daily realized 2026-06-16 PT: **−$214.33 / −1.98%** — loss cap 5% (2.5x below), CLEAR.
- Consecutive losing trading days: **2** (BTC Sun, ETH Tue; cap 7, 5 of headroom).
- Max drawdown: **2.42%** from peak $10,875.85 (cap 25%, warn 12.5%) — CLEAR.
- Equity floor: $10,612.15 > $7,500 floor — CLEAR.
- Regime gate (rule 5a) — closed-bar 03:00Z snapshot via `indicators.py`: **6/15 positive, median −0.11%** → 5a PASS (6 > 4 floor); SBD CLEAR (median −0.11% > −1.0%, 6 > 1 positive).
- Active 5b cooldowns: **ETH 2026-06-16T15:00Z exit-stop-hit — 5b active until 2026-06-17T15:00Z**.
- **Watchdog (this wake, run with --telegram):** 7 findings — 1× A heartbeat (routine-07 70h late vs 30h threshold), 6× D stale-MTM (variants v0.12-sbd-exit / v0.13-trend-confirm / v0.14-recovery-trend / v0.3-vol-compression / v0.5-cluster-cap-tight / v0.7-vol-comp-defensive — all 71h since last MTM). Informational; variant lag does not affect BULL state. Telegram alert auto-sent by watchdog process.
- **All clear (kill switches).** routine-03-eod 2026-06-17T04:11Z (Tue 21:11 PT — on-schedule cron fire): **1 OPEN** (HYPE EOD entry), **1 CLOSE day-total** (ETH stop, processed earlier at midday). Kraken MCP AVAILABLE (`kraken_ticker` HYPEUSD + `kraken_spread` HYPEUSD clean <2s; full 15-pair indicator scan via `indicators.py` clean). **Telegram: EOD card sent** per routine §NOTIFY (mandatory daily).

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

| Pair | Next check | Trigger |
|------|------------|---------|
| HYPE/USD | next 1H close (04:00Z+1h = 05:00Z Wed) | Exit 1 W22-G (2× 1H close < 20-EMA — first sub-EMA bar would be flagged) / Exit 2 stop $71.6714 / Exit 3 target $85.8004 / W22-H breakeven ratchet armed at unrealized R ≥ 2.0 (price ≥ $80.1488) |

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | ≈ +3.58% realized (TAO +4.04R / +6.21%, BTC −0.60R / −0.43%, ETH −1.32R / −1.98%) + −0.02% unrealized | ≈ +4.1% (BTC ~$63.2k → $65.8k over 7d) | ≈ −0.5% | BULL roughly tied on 7d (slight underperformance from today's ETH stop give-back; HYPE entry not yet contributing) |
| 30d | ≈ +6.12% (inception $10k 2026-04-20; window fully computable) | ≈ −19.1% (BTC 2026-05-13 ~$81.3k → today $65.8k) | ≈ +25.2% | BULL well ahead |
| 90d | — | — | — | not computable (BULL inception 2026-04-20 = 58 days ago; window first computable ~2026-07-19) |

(7d / 30d figures approximate; BTC closed-bar reference $65,781.5 this wake via `indicators.py`. HYPE entry $74.4972 is mid-day-3 of an 8-day run from $51 base; entry RSI 59.8 is non-climactic with comfortable headroom to the 80 cap; 4H +15.6% over EMA50 is the strongest R3 margin of the eligible set. The ETH stop today reduces 7d delta vs BTC to a near-tie; the +25.2% 30d outperformance remains the dominant figure, all attributable to BULL avoiding the May breakdown via 5a/5a-SBD gates while BTC-hold ate the full move.)
