# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-06-17T17:52Z routine-01-overnight (PT label 2026-06-17, **late cron fire** — cron `0 6 * * 1-5` PT = 13:00 UTC, actual fire 17:52 UTC, **4h52m delay**). Two events processed: (1) **HYPE stop-out replay** detected via Kraken 1H OHLCV history — stop pierce on 11:00Z bar (low $70.60 < stop $71.6714), fill at stop × 0.9995 = $71.6356, CLOSE timestamp 12:00Z (bar close); realized -$182.64 / -1.15R net. (2) **Entry scan on fire-time 16:00Z bar via `indicators.py`** identified BTC and SOL as both technically eligible (regime 12/15 positive 24h, median +1.17% → 5a PASS / SBD CLEAR). **R8 tiebreak:** BTC rank 1 wins on notional but sizing 0.176428 BTC × $65,847.11 = **$11,617.27 required notional exceeds available cash $10,431.61** by $1,185.66 — BTC could not be filled on spot (mandate forbids leverage). Treated cash-insufficient as pre-entry-check REJECT, advanced to next rule-8 eligible per "rule-8 fallback" interpretation (mandate-compliant: still one entry per wake, no cluster fill). SOL/USD opened at 17:00Z (close of 16:00Z bar): entry $73.7268 (0.05% adverse slippage on $73.69 close), ATR14 = $0.74901, stop distance 2×ATR = $1.49802, stop **$72.2288**, target (4R) **$79.7189**. Size = 1.5% × $10,431.61 / $1.49802 = **104.454002 SOL**, cost $7,701.06, cash post-entry **$2,730.55**. Position MTM @ 16:00Z close $73.69 = $7,697.22; unrealized PnL = **-$3.84** (slippage only). Day P&L for 2026-06-17 PT (vs prior EOD $10,612.15): realized -$182.64 (HYPE stop) + unrealized -$3.84 (SOL slippage) = **-$186.48 / -1.74%**. **Equity:** $10,427.77. **Peak unchanged $10,875.85.** **Drawdown 4.12%** — CLEAR (warn 12.5%). **Loss streak: 3 trading days** (BTC Sun -0.60R, ETH Tue -1.32R, HYPE Wed -1.15R; cap 7, 4 of headroom). **Watchdog (this wake, `--telegram`):** 7 findings — 1× A heartbeat (routine-07 84h late vs 30h threshold) + 6× D stale-MTM (variants v0.12-sbd-exit / v0.13-trend-confirm / v0.14-recovery-trend / v0.3-vol-compression / v0.5-cluster-cap-tight / v0.7-vol-comp-defensive — all 85h since last MTM, scheduler gap). Auto-alerted via Telegram; informational only, BULL state unaffected. **Lessons:** one new lesson appended on cash-constraint blocking BTC top-rank entry (rule-8 fallback policy for routine-04 evaluation). All kill switches CLEAR. **Telegram: late-fire overnight digest sent** per routine §NOTIFY (new OPEN + stop-out CLOSE both fired this run). Next routine: routine-02-midday Wed 06-17T19:00Z (cron `0 12 * * 1-5` PT).

> **Prior rebuild:** 2026-06-17T04:11Z routine-03-eod. HYPE EOD entry @ $74.4972 56.342770 units, stop $71.6714, target $85.8004 (post-ETH-stop equity $10,614.25, day -2.00%, DD 2.42%, loss streak 2).

> **Prior rebuild (06-16 midday):** 2026-06-16T20:08Z routine-02-midday. ETH/USD 5.1162 stop-out exit replay 2026-06-16T15:00Z via Exit rule 2 (intrabar stop pierce). Orphan-write entry @ 12:00Z handled per source-of-truth rule. Realized -1.32R / -$214.33 net.

## Account

- Starting equity: **$10,000.00**
- Cash: **$2,730.55** (was $10,614.25; net flow: -$182.64 HYPE realized loss, -$7,701.06 SOL entry cost)
- Realized PnL (all-time): **+$431.61** ($614.25 prior + -$182.64 HYPE today)
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
- Unrealized PnL (open positions): **−$3.84** (SOL @ MTM $73.69)
- Position values (MTM): **$7,697.22** (SOL 104.454002 × $73.69)
- Current equity (cash + positions MTM): **$10,427.77**
- Equity peak: **$10,875.85** (set 2026-06-13T09:00Z at TAO 4R close — unchanged)
- Drawdown from peak: **4.12%** ($448.08 below peak)
- Since-inception return: **+4.28%** ($10,427.77 / $10,000 − 1)

## Open positions

| Pair | Side | Size | Entry | Stop | Target | Unrealized PnL | R-risk | Opened |
|------|------|------|-------|------|--------|----------------|--------|--------|
| SOL/USD | long | 104.454002 | $73.7268 | $72.2288 | $79.7189 | −$3.84 (MTM $73.69) | $156.47 (1.50% eq) | 2026-06-17T17:00Z |

Portfolio risk-at-moment: **1.50%** of equity (cap 4%, 2.5% headroom).
Open positions: **1 / 8** (strategy v0.4 max-concurrent 4 → 1/4 used; cluster {BTC,ETH,SOL,TAO,AVAX,SUI,LINK} 1/2 — SOL in cluster).

## Day summary — 2026-06-17 PT (Wed, morning routine)

| Metric | Value |
|---|---|
| Day realized PnL | **−$182.64** (HYPE stop-hit replay) |
| Day unrealized PnL | **−$3.84** (SOL entry slippage only) |
| Day total PnL | **−$186.48** |
| Day % (vs $10,612.15 prior-day close) | **−1.74%** |
| Trades opened today | **1** (SOL/USD long @ 17:00Z bar close) |
| Trades closed today | **1** (HYPE/USD long stop-out @ 12:00Z bar pierce) |
| Win rate today | **0%** (0/1 closed) |
| Equity (current) | **$10,427.77** |
| Equity peak (realized) | **$10,875.85** (unchanged) |
| Drawdown from peak | **4.12%** |
| Loss streak | **3** trading days (BTC Sun, ETH Tue, HYPE Wed) |

## Active kill-switch state

- Daily realized 2026-06-17 PT: **−$182.64 / −1.72%** — loss cap 5% (2.9x below), CLEAR.
- Daily total (realized + unrealized) 2026-06-17 PT: **−$186.48 / −1.74%** — CLEAR.
- Consecutive losing trading days: **3** (BTC Sun, ETH Tue, HYPE Wed; cap 7, 4 of headroom).
- Max drawdown: **4.12%** from peak $10,875.85 (cap 25%, warn 12.5%) — CLEAR.
- Equity floor: $10,427.77 > $7,500 floor — CLEAR.
- Regime gate (rule 5a) — closed-bar 16:00Z snapshot via `indicators.py`: **12/15 positive, median +1.17%** → 5a PASS (12 > 4 floor); SBD CLEAR (median +1.17% > −1.0%, 12 > 1 positive).
- Active 5b cooldowns: **HYPE 2026-06-17T12:00Z exit-stop-hit — 5b active until 2026-06-18T12:00Z**.
- **Watchdog (this wake, run with --telegram):** 7 findings — 1× A heartbeat (routine-07 84h late vs 30h threshold), 6× D stale-MTM (variants v0.12-sbd-exit / v0.13-trend-confirm / v0.14-recovery-trend / v0.3-vol-compression / v0.5-cluster-cap-tight / v0.7-vol-comp-defensive — all 85h since last MTM). Informational; variant lag does not affect BULL state. Telegram alert auto-sent by watchdog process.
- **All clear (kill switches).** routine-01-overnight 2026-06-17T17:52Z (Wed 10:52 PT — **4h52m late cron fire**, cron `0 6 * * 1-5` PT): **1 OPEN** (SOL fire-time-bar entry with rule-8 fallback after BTC cash-insufficient REJECT), **1 CLOSE** (HYPE stop-out replay at first piercing bar 11:00Z closed 12:00Z). Kraken REST clean (full 15-pair `indicators.py` scan + HYPE 1H history + SOL spread/ticker queries all <5s each). **Telegram: overnight digest sent** per routine §NOTIFY (new OPEN + stop-out CLOSE).

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
| SOL/USD | next 1H close (17:00Z+1h = 18:00Z Wed) | Exit 1 W22-G (2× 1H close < 20-EMA — first sub-EMA bar would be flagged) / Exit 2 stop $72.2288 / Exit 3 target $79.7189 / W22-H breakeven ratchet armed at unrealized R ≥ 2.0 (price ≥ $76.7228) |

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | ≈ +1.43% realized (TAO +4.04R / +6.21%, BTC −0.60R / −0.43%, ETH −1.32R / −1.98%, HYPE −1.15R / −1.72%) + −0.04% unrealized | ≈ +4.0% (BTC ~$63.3k → $65.8k over 7d) | ≈ −2.6% | BULL underperforms 7d (today's HYPE stop compounds prior week's losses; SOL entry not yet contributing) |
| 30d | ≈ +4.28% (inception $10k 2026-04-20; window fully computable) | ≈ −19.1% (BTC 2026-05-13 ~$81.3k → today $65.8k) | ≈ +23.4% | BULL well ahead |
| 90d | — | — | — | not computable (BULL inception 2026-04-20 = 58 days ago; window first computable ~2026-07-19) |

(7d / 30d figures approximate; BTC closed-bar reference $65,814.2 this wake via `indicators.py`. The 7d delta has slipped to −2.6% from yesterday's near-tie, reflecting HYPE's −1.15R stop. The +23.4% 30d outperformance remains dominant, attributable to BULL avoiding the May breakdown via 5a/5a-SBD gates while BTC-hold ate the full move. SOL entry at $73.7268 puts BULL back in market exposure; 4R target $79.7189 ~+8.1% from entry.)
