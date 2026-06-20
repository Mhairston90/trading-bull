# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-06-20T14:42Z routine-03-eod (PT label 2026-06-19 Fri EOD — scheduler fired ~10h42m late at Sat 07:42 PT due to harness drift; using freshest 13:00Z signal-bar, not the original 04:00Z fire-time bar; signal still valid per strategy.md). Regime **5a PASS** (9/15 positive, median +0.13%; weakening from 15/15 at 11:17Z snapshot — flagged below), SBD CLEAR. **1 entry executed: SOL** (only fully-eligible candidate; ETH/HYPE dropped between snapshots — ETH RSI 61.1→52.0, HYPE R1 PASS→FAIL). Equity at wake (MTM @ last $70.92): **$10,201.36** (DD 6.20%). All kill switches CLEAR.

> **Prior rebuild:** 2026-06-19T20:07Z routine-02-midday (PT label 2026-06-19 Fri). Position management only — flat portfolio, no MTM action. Equity $10,231.74 unchanged. DD 5.92%. Loss streak 3.

## Account

- Starting equity: **$10,000.00**
- Cash: **$1,582.12** (was $10,231.74; spent $8,649.62 on SOL entry 121.5347 × $71.17)
- Realized PnL (all-time): **+$231.74** (unchanged; no closes this wake)
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
- Unrealized PnL (open positions): **−$30.38** (SOL: 121.5347 × ($70.92 − $71.17) = −$30.38, −0.198R)
- Position values (MTM @ last $70.92): **$8,619.24** (SOL)
- Current equity (cash + positions MTM): **$10,201.36**
- Equity peak: **$10,875.85** (set 2026-06-13T09:00Z at TAO 4R close — unchanged)
- Drawdown from peak: **6.20%** ($674.49 below peak; +0.28pp from prior wake's 5.92%, driven by SOL entry slipping to $70.92 vs $71.17 entry)
- Since-inception return: **+2.01%** ($10,201.36 / $10,000 − 1; was +2.32%)

## Open positions

| Pair | Side | Size | Entry | Stop (initial 2×ATR) | Active stop | Target (4R) | Entry ts (UTC) | Last (MTM) | Unrealized R | Unrealized $ |
|---|---|---|---|---|---|---|---|---|---|---|
| SOL/USD | long | 121.5347 | 71.17 | 69.9072 | 69.9072 | 76.2212 | 2026-06-20T13:00:00Z | 70.92 | -0.198 | -30.38 |

Portfolio risk-at-moment: **1.50%** of equity (SOL stop-distance × size / equity = $153.48 / $10,201.36; cap 4%, headroom 2.50%).
Open positions: **1 / 8** (strategy v0.4 max-concurrent 4 → 1/4 used; cluster {BTC,ETH,SOL,TAO,AVAX,SUI,LINK} 1/2 with SOL).
Breakeven ratchet (W22-H-partial): not active (need unrealized R ≥ +2.0 at 1H close; currently −0.198R).

## Day summary — 2026-06-19 PT (Fri EOD; cron fired Sat 07:42 PT, ~10h42m late)

| Metric | Value |
|---|---|
| Day realized PnL (PT Fri) | **$0.00** (no closes during PT Fri trading day) |
| Day unrealized PnL | **−$30.38** (SOL entry, late-fire bar 13:00Z = Sat morning UTC — strictly attributable to post-Friday market hours but bucketed to this wake per routine date label) |
| Day total PnL | **−$30.38** (−0.30% vs prior $10,231.74) |
| Trades opened today | **1** (SOL/USD) |
| Trades closed today | **0** |
| Win rate today | n/a (no closes) |
| Equity (current MTM) | **$10,201.36** |
| Equity peak (realized) | **$10,875.85** (unchanged) |
| Drawdown from peak | **6.20%** |
| Loss streak | **3** trading days (BTC Sun, ETH Tue, Wed [HYPE+SOL]; Thu/Fri flat — streak holds at 3, no new realized loss today) |

## Active kill-switch state

- Daily realized 2026-06-19 PT: **$0.00 / 0.00%** — loss cap 5% (5.00% headroom), CLEAR.
- Daily total (realized + unrealized) 2026-06-19 PT: **−$30.38 / −0.30%** — CLEAR, 4.70% headroom to 5% daily-loss cap.
- Consecutive losing trading days: **3** (no new closed loss today; cap 7, headroom 4). CLEAR.
- Max drawdown: **6.20%** from peak $10,875.85 (cap 25%, warn 12.5%, 6.30% to warn) — CLEAR.
- Equity floor: $10,201.36 > $7,500 floor — CLEAR.
- Regime gate (rule 5a): **PASS** — 9/15 positive 24h, median +0.13% (≥ 4/15 floor). Entries enabled this wake.
- Regime sub-state (rule 5a-SBD): **CLEAR** — positives = 9 (> 1 ceiling) AND median +0.13% > −1.0%. Default 20-EMA two-bar exit applies.
- Active 5b cooldowns: none (SOL stop-out was 2026-06-17T18:00Z, 68h ago — well past 24h).
- **All clear (kill switches).** routine-03-eod 2026-06-20T14:42Z fire (PT label 2026-06-19 Fri EOD): **1 OPEN** (SOL @ $71.17, signal-bar 13:00Z), **0 CLOSE**, **MTM @ last $70.92 = $8,619.24**. Regime weakening trajectory flagged (15/15 → 9/15 in 3.5h between two indicator snapshots) — entry took the freshest signal per strategy.md; SBD-leading-edge filter (lesson 2026-06-17 recommendation a) NOT codified, so does not block.

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

- SOL: stop $69.9072 (2×ATR initial); target $76.2212 (+4R); EMA20 exit at two consecutive 1H closes below 20-EMA ($70.6934 from 13:00Z bar). Breakeven ratchet idle (need unrealized R ≥ +2.0 at 1H close).

Next entry-eligible scan: routine-01-overnight Sat 2026-06-20 04:00 PT (Sat 11:00Z). Regime re-evaluation each wake.

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | ≈ −1.05% (−0.74% realized + −0.30% unrealized SOL entry; modest deterioration vs prior wake) | ≈ +2% (BTC trending sideways; 7d window mostly captures the 06-13→06-17 selloff offset by stabilization) | ≈ −3.1% | BULL underperforms 7d |
| 30d | ≈ +2.01% (inception $10k 2026-04-20; equity now $10,201.36) | ≈ −22% (BTC 2026-05-21 ~$81.0k → today ~$63.3k) | ≈ +24.0% | BULL well ahead |
| 90d | — | — | — | not computable (BULL inception 2026-04-20 = 60 days ago; window first computable ~2026-07-19) |

(7d/30d figures approximate. SOL entry slightly drags equity at the wake snapshot but is within designed 1.5% risk envelope; W22 breakeven ratchet provides the asymmetric defensive backstop if SOL runs to +2R.)
