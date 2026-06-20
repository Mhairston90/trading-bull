# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-06-20T14:48Z routine-01-overnight (Sat 07:48 PT — fired outside Mon–Fri cron window, day-of-week anomaly noted in research_log; routine has no day-gate so it proceeds normally). Regime **5a PASS** (9/15 positive, median +0.13% — unchanged from prior wake), SBD CLEAR. **0 OPEN, 0 CLOSE.** Held SOL/USD (entered 13:00Z @ $71.17). MTM @ last $71.96: **$10,329.73** (DD **5.02%**, improved 1.18pp from prior wake on SOL favorable move). All kill switches CLEAR.

> **Prior rebuild:** 2026-06-20T14:42Z routine-03-eod (PT label 2026-06-19 Fri EOD — late fire). Opened SOL/USD 121.5347 @ $71.17. Equity $10,201.36, DD 6.20%. Regime 5a PASS, SBD CLEAR.

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
- Unrealized PnL (open positions): **+$96.01** (SOL: 121.5347 × ($71.96 − $71.17) = +$96.01, +0.626R)
- Position values (MTM @ last $71.96): **$8,747.61** (SOL)
- Current equity (cash + positions MTM): **$10,329.73**
- Equity peak: **$10,875.85** (set 2026-06-13T09:00Z at TAO 4R close — unchanged)
- Drawdown from peak: **5.02%** ($546.12 below peak; improved 1.18pp from prior wake's 6.20% as SOL moved from $70.92 → $71.96)
- Since-inception return: **+3.30%** ($10,329.73 / $10,000 − 1; was +2.01%)

## Open positions

| Pair | Side | Size | Entry | Stop (initial 2×ATR) | Active stop | Target (4R) | Entry ts (UTC) | Last (MTM) | Unrealized R | Unrealized $ |
|---|---|---|---|---|---|---|---|---|---|---|
| SOL/USD | long | 121.5347 | 71.17 | 69.9072 | 69.9072 | 76.2212 | 2026-06-20T13:00:00Z | 71.96 | +0.626 | +96.01 |

Portfolio risk-at-moment: **1.49%** of equity (SOL stop-distance × size / equity = $153.48 / $10,329.73; cap 4%, headroom 2.51%).
Open positions: **1 / 8** (strategy v0.4 max-concurrent 4 → 1/4 used; cluster {BTC,ETH,SOL,TAO,AVAX,SUI,LINK} 1/2 with SOL).
Breakeven ratchet (W22-H-partial): not active (need unrealized R ≥ +2.0 at 1H close; current +0.626R; latest closed 1H bar gave R = 0.0).

## Day summary — 2026-06-20 PT (Sat; routine-01-overnight fired 07:48 PT)

| Metric | Value |
|---|---|
| Day realized PnL (PT Sat) | **$0.00** (no closes this wake) |
| Day unrealized PnL change | **+$128.37** (SOL MTM moved $70.92 → $71.96 since prior wake) |
| Day total PnL (vs prior wake) | **+$128.37** (+1.26% vs $10,201.36 prior) |
| Trades opened today | **0** |
| Trades closed today | **0** |
| Win rate today | n/a (no closes) |
| Equity (current MTM) | **$10,329.73** |
| Equity peak (realized) | **$10,875.85** (unchanged) |
| Drawdown from peak | **5.02%** |
| Loss streak | **3** trading days (no new realized loss; SOL open and favorable but not closed) |

## Active kill-switch state

- Daily realized 2026-06-20 PT: **$0.00 / 0.00%** — loss cap 5% (5.00% headroom), CLEAR.
- Daily total (realized + unrealized vs prior wake) 2026-06-20 PT: **+$128.37 / +1.26%** — CLEAR.
- Consecutive losing trading days: **3** (cap 7, headroom 4). CLEAR.
- Max drawdown: **5.02%** from peak $10,875.85 (cap 25%, warn 12.5%, 7.48pp to warn) — CLEAR.
- Equity floor: $10,329.73 > $7,500 floor — CLEAR.
- Regime gate (rule 5a): **PASS** — 9/15 positive 24h, median +0.13% (≥ 4/15 floor). Entries enabled this wake.
- Regime sub-state (rule 5a-SBD): **CLEAR** — positives = 9 (> 1 ceiling) AND median +0.13% > −1.0%. Default 20-EMA two-bar exit applies.
- Active 5b cooldowns: none (SOL stop-out 2026-06-17T18:00Z = 92h ago, past 24h).
- **All clear (kill switches).** routine-01-overnight 2026-06-20T14:48Z fire: **0 OPEN, 0 CLOSE**, SOL held with favorable MTM move. Regime stable at 9/15 positive (the leading-edge deterioration logged in prior wake did NOT continue into SBD).

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

- SOL: stop $69.9072 (2×ATR initial); target $76.2212 (+4R); EMA20 exit at two consecutive 1H closes below 20-EMA ($70.6934). Breakeven ratchet idle (need unrealized R ≥ +2.0 at 1H close; current intra-bar R +0.626).

Next entry-eligible scan: routine-02-midday Sat 12:00 PT (= Sat 19:00Z) — position management only, no new entries. Routine-03-eod Sat 21:00 PT (= Sun 04:00Z) is next entry-eligible wake if cron permits Sat firing; otherwise routine-01 Mon 06:00 PT.

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | ≈ +0.21% (−0.74% realized + +0.96% unrealized SOL) | ≈ +0.5% (BTC sideways near $63.3k) | ≈ −0.3% | BULL roughly even 7d |
| 30d | ≈ +3.30% (inception $10k 2026-04-20; equity now $10,329.73) | ≈ −22% (BTC 2026-05-21 ~$81.0k → today ~$63.3k) | ≈ +25.3% | BULL well ahead |
| 90d | — | — | — | not computable (BULL inception 2026-04-20 = 61 days ago; window first computable ~2026-07-19) |

(7d/30d figures approximate. SOL position is +0.626R unrealized; W22 breakeven ratchet activates at +2.0R close — currently $1.42 above current price as the trigger.)
