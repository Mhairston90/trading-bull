# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-06-23T01:40Z routine-03-eod (PT label 2026-06-22 Mon EOD — fires at 18:40 PT, ~2h before cron 21:00 PT slot; treated as today's EOD). Regime **5a PASS** (6/15 positive, median −0.25%), SBD CLEAR. **0 OPEN, 1 CLOSE (missed-scheduler replay).** Exited SOL/USD 121.5347 @ $73.08 (gross) → friction-corrected to $73.0435 effective via exit-ema20-confirm at 2026-06-22T15:00Z bar close (second consecutive 1H close below 1H EMA20 — bar -0.65 below, prior bar -0.42 below; first below-bar was 14:00Z at $73.37). Realized **+$182.13 / +1.19R net of friction** (gross was +$232.13 / +1.51R; auto-correction row applied −$50 ≈ 2-side commission 0.26%/side + slippage 0.05%/side on $8.8k notional). Second 4R-track winner where the W22-G two-bar rule took the trend break before the breakeven ratchet could be tested (peak close $74.88 at 13:00Z = +2.94R). New equity **$10,413.87** (cash only, no open positions). DD **4.25%** from peak $10,875.85 (improved 0.77pp from prior 5.02%). Loss streak resets to **0** (was 3). All kill switches CLEAR.

> **Prior rebuild:** 2026-06-20T14:48Z routine-01-overnight (Sat 07:48 PT — held SOL favorable +0.626R MTM, equity $10,329.73, DD 5.02%).

## Account

- Starting equity: **$10,000.00**
- Cash: **$10,413.87** (= prior cash $1,582.12 + SOL exit proceeds-net-of-friction $8,831.75 [121.5347 × $73.08 gross − ~$50 commission+slippage])
- Realized PnL (all-time): **+$413.87** (was +$231.74; +$182.13 net from SOL exit this wake after friction correction)
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
  - **SOL +$232.13 (missed-scheduler replay exit-ema20-confirm 2026-06-22T15:00Z, +1.51R gross) ← THIS WAKE**
  - **SOL −$50.00 (correction-previous-row friction adjustment 2026-06-22T16:00Z, net SOL exit = +$182.13 / +1.19R)**
- Unrealized PnL (open positions): **$0.00** (flat)
- Position values (MTM): **$0.00**
- Current equity (cash only): **$10,413.87**
- Equity peak: **$10,875.85** (set 2026-06-13T09:00Z at TAO 4R close — unchanged)
- Drawdown from peak: **4.25%** ($461.98 below peak; improved 0.77pp from prior wake's 5.02% on SOL +1.19R net winning exit)
- Since-inception return: **+4.14%** ($10,413.87 / $10,000 − 1; was +3.30%)

## Open positions

_None._

Portfolio risk-at-moment: **0.00%** of equity (no open positions; cap 4%, full headroom).
Open positions: **0 / 8** (strategy v0.4 max-concurrent 4 → 0/4 used; cluster cap 0/2).
Breakeven ratchet (W22-H-partial): n/a (no open position). Note: the closed SOL trade peaked at $74.88 close 2026-06-22T13:00Z = +2.94R — the ratchet **would have fired** at that close, moving stop from $69.9072 to $71.17 (entry). The EMA exit then fired at 15:00Z $73.08 (above breakeven), so the ratchet did not bind. Net is identical to the actual EMA-confirm path; first time the W22-H ratchet path was nearly engaged on a fresh trade.

## Day summary — 2026-06-22 PT (Mon EOD)

| Metric | Value |
|---|---|
| Day realized PnL (PT Mon, net of friction) | **+$182.13** (SOL exit at 15:00Z = 08:00 PT 06-22; gross +$232.13, friction −$50) |
| Day unrealized PnL change | **−$96.01** (SOL's prior-wake +$96.01 unrealized → converted to +$182.13 net realized) |
| Day total PnL (vs prior wake mark $10,329.73) | **+$84.14 (+0.81%)** |
| Trades opened today | **0** |
| Trades closed today | **1** (SOL exit-ema20-confirm, friction-corrected) |
| Win rate today | **100%** (1/1) |
| Equity (current cash-only) | **$10,413.87** |
| Equity peak (realized) | **$10,875.85** (unchanged; need +$461.98 to retake) |
| Drawdown from peak | **4.25%** |
| Loss streak | **0 trading days** (reset by winning SOL trade) |

## Active kill-switch state

- Daily realized 2026-06-22 PT: **+$182.13 / +1.75%** of equity — loss cap not relevant (gain), CLEAR.
- Daily total (vs prior wake) 2026-06-22 PT: **+$84.14 / +0.81%** — CLEAR.
- Consecutive losing trading days: **0** (cap 7, full headroom; reset from 3 by today's winner). CLEAR.
- Max drawdown: **4.25%** from peak $10,875.85 (cap 25%, warn 12.5%, 8.25pp to warn) — CLEAR.
- Equity floor: $10,413.87 > $7,500 floor — CLEAR.
- Regime gate (rule 5a): **PASS** — 6/15 positive 24h, median −0.25% (≥ 4/15 floor). Entries enabled this wake.
- Regime sub-state (rule 5a-SBD): **CLEAR** — positives = 6 (> 1 ceiling) AND median −0.25% > −1.0%. Default 20-EMA two-bar exit applies.
- Active 5b cooldowns: **SOL/USD** until 2026-06-23T15:00Z (just-exited; 24h re-entry guard active).
- **All clear (kill switches).** routine-03-eod 2026-06-23T01:40Z fire: **0 OPEN, 1 CLOSE** (missed-scheduler replay of SOL EMA exit), now flat. Regime stable at 6/15 positive — borderline-comfortable but no SBD risk.

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

_None — no open positions._

Next entry-eligible scan: routine-01-overnight Tue 2026-06-23 06:00 PT (= 13:00Z) if cron permits — note the recurring missed-scheduler pattern. SOL 5b cooldown clears at 2026-06-23T15:00Z so SOL is re-entry-eligible from the 15:00Z bar onwards.

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | ≈ −0.7% (net of SOL +$182 winner + earlier 06-16/-17 stop-outs) | ≈ −1% (BTC ~$64.4k → ~$64.0k) | ≈ +0.3% | BULL roughly even 7d |
| 30d | ≈ +4.14% (inception $10k 2026-04-20; equity now $10,413.87) | ≈ −21% (BTC 2026-05-21 ~$81.0k → today ~$64.0k) | ≈ +25.1% | BULL well ahead |
| 90d | — | — | — | not computable (BULL inception 2026-04-20 = 63 days ago; window first computable ~2026-07-19) |

(7d/30d figures approximate. The W22-G two-bar EMA exit took +1.51R on SOL today — second 4R-track winner since v0.4. TAO 06-13 hit the 4R target +4.04R; SOL today would have been the 3rd 4R-target had it kept trending after the 13:00Z $74.88 peak — the 4R target $76.22 was $1.34 above the bar high, not reached.)
