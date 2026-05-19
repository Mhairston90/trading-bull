# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-05-19 (routine-01-overnight) — no-op rebuild: 0 new trades since 2026-05-16, account still flat, equity unchanged $10,236.14. Kill-switch state re-verified against live Kraken data (risk_flag CLEAR). Prior binding event retained below for audit. Originally: 2026-05-16 (routine-03-eod) — XRP/USD closed on the 1H 20-EMA cross-down at **2026-05-15T04:00Z** (the binding first exit); a concurrently-written routine-02-midday rebuild booked an `exit-stop-hit` at 2026-05-15T13:00Z (−$206.37), **superseded** — see "Trade-log correction" below. Account is flat.

## Account

- Starting equity: **$10,000.00**
- Cash: **$10,236.14**
- Realized PnL (all-time): **+$236.18**
  - BTC −$9.14 (exit-ema-cross 2026-04-24T04:00Z)
  - TRX −$26.69 (exit-stop-hit 2026-04-24T20:00Z)
  - LTC +$39.40 (exit-ema-cross 2026-04-25T17:00Z, +1.32R)
  - ADA −$38.77 (exit-ema-cross 2026-04-25T17:00Z, −1.21R)
  - AVAX −$34.04 (exit-ema-cross 2026-04-25T17:00Z, −0.99R)
  - ETH −$34.68 (exit-stop-hit 2026-04-27T05:00Z, −1.06R)
  - BTC −$28.77 (exit-stop-hit 2026-04-27T05:00Z, −1.08R)
  - SOL −$33.82 (exit-stop-hit 2026-04-27T05:00Z, −1.06R)
  - TAO −$56.38 (exit-stop-hit 2026-04-27T05:00Z, −1.03R)
  - TAO −$64.37 (exit-stop-hit 2026-04-29T14:00Z, −1.02R)
  - HYPE −$58.18 (exit-stop-hit 2026-05-06T15:00Z, −1.02R)
  - BTC +$1.42 (exit-ema-cross 2026-05-06T19:00Z, +0.06R)
  - LTC −$48.58 (exit-stop-hit 2026-05-07T01:00Z, −1.03R)
  - XRP −$37.68 (exit-stop-hit 2026-05-07T14:00Z, −1.05R)
  - LINK +$103.03 (exit-ema-cross 2026-05-07T20:00Z, +1.69R)
  - SOL +$585.35 (exit-4R-target 2026-05-11T19:00Z, +4.03R)
  - XRP −$21.92 (exit-ema-cross 2026-05-15T04:00Z, −0.14R) — corrected; supersedes the routine-02-midday-logged 2026-05-15T13:00Z exit-stop-hit −$206.37
- Unrealized PnL: **$0.00** (no open positions)
- Position values (MTM): **$0.00**
- Current equity (cash + positions MTM): **$10,236.14**
- Equity peak: **$10,258.06** (set 2026-05-11 midday at 4R take-profit on SOL)
- Drawdown from peak: **0.21%**

## Open positions

| Pair | Side | Size | Entry | Stop | Stop dist | R-risk | Last px | Unreal PnL | Unreal R |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| — | — | — | — | — | — | — | — | — | — |

None. Account is flat.

Portfolio risk-at-moment: **0.00%** of equity (cap 4%, flat).
Open positions: **0 / 8** (strategy v0.2 max-concurrent 4 → 0/4 used; cluster {BTC,ETH,SOL,TAO,AVAX,SUI,LINK} 0/2).

## Trade-log correction (2026-05-16, routine-03-eod)

During this EOD wake a concurrent `routine-02-midday` instance wrote:
`2026-05-15T13:00:00Z | CLOSE | XRP/USD | long | 6334 | 1.44305 | — | — | -1.03 | -206.37 | exit-stop-hit`
and rebuilt portfolio.md to equity $10,051.73.

That exit is **superseded**. Per `strategy.md` Exits — "Exit when ANY of the following is true … checked at the close of each 1H candle. No intra-bar exits" — the binding exit is the *first* condition true at a 1H close. Replaying XRP 1H closes from the 2026-05-14T16:00Z entry:

- **Exit rule 1 (1H close < 1H 20-EMA): first true at 2026-05-15T04:00:00Z** — close 1.47298 vs 20-EMA ≈ 1.4780. EMA seeded as SMA of 1H closes 2026-05-13 03:00→22:00Z (= 1.439169), iterated 30 bars; cross-checked vs prior EOD's independent EMA ≈ 1.4406 @ 2026-05-14 15:00Z. Bars 05-14 16:00Z→05-15 03:00Z all closed *above* the rising EMA (closes 1.479–1.536 vs EMA 1.444–1.479); 05-15 04:00Z (close 1.47298 < EMA 1.4780) is the first close below.
- Exit rule 2 (static stop 1.44377): first 1H close ≤ stop not until 2026-05-15T13:00Z (close 1.43187); intra-bar lows 05-14 16:00Z→05-15 04:00Z all ≥ 1.47298 — stop untouched before the EMA-cross even ignoring "no intra-bar exits".

The EMA-cross at 04:00Z closes the position ~9h before any stop interaction, so the 13:00Z stop-out cannot occur. Correction row appended to `trade_log.md` at the true candle-close timestamp `2026-05-15T04:00:00Z`, reason `correction-previous-row`, per `skills/log-trade.md` ("never rewrite past rows; append a correction row"). Net realized **−$21.92 (−0.14R)** after 0.26%/side commissions and 0.05% exit slippage (fill 1.47224 = 1.47298 × 0.9995). Cash = $935.19 + ($9,325.19 − $24.25 comm) = **$10,236.14**.

Flagged for routine #4 (Sat 2026-05-16): (a) codify that any late/concurrent routine fire must replay *all* unprocessed 1H closes and apply the earliest exit trigger, not just the latest bar; (b) resolve the duplicate-CLOSE race when multiple routine instances act on the same open position; (c) reconcile the "no intra-bar exits" rule vs the intra-bar stop interpretation used by routine-02.

## Active kill-switch state

- Daily realized: XRP close −$21.92 ≈ **−0.21%** of equity (booked candle-date 2026-05-15) — within 5% LOSS cap
- Consecutive losing trading days: 05-07 W, 05-11 W, 05-12 flat, 05-13 flat, 05-14 flat (open only), **05-15 L** (XRP −0.14R) → streak **1** (cap 7)
- Max drawdown: 0.21% from peak $10,258.06 (cap 25%, warn 12.5%) — clear
- Equity floor: $10,236.14 > $7,500 floor — OK
- **All clear. Trading authorized.** No open positions.
- **2026-05-19 routine-01 regime note:** entry rule 5a (regime-confirmation gate) FAILED this wake — only 1/15 universe pairs positive on 24h (TRX +0.03%), threshold >= 4/15. All new entries rejected by strategy v0.2 rule 5a; not a kill switch. Broad BTC-led risk-off in news (BTC ~-6% over several days, largest BTC-ETF outflows since Jan); daily risk_flag independently CLEAR. Zero portfolio exposure to the pullback (flat). XRP last px 1.37446.

## Pending exit triggers

- None — portfolio is flat.

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | ≈ +5.8% (approx) | ≈ −3 to −4% (approx) | ≈ +9% (approx) | BULL ahead (approx) |
| 30d | — | — | — | — |
| 90d | — | — | — | — |

(7d figures approximate — precise reference-price computation deferred to routine #4. 30d window pre-dates BULL inception 2026-04-20; first computable 2026-05-20.)
