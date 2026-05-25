# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-05-25 routine-03-eod — same-day successor to routine-01-overnight which opened the BTC/USD long earlier in this UTC window (entry 77678.12, 0.0338 BTC, stop 77122.02, 4R target 79902.52, risk $18.80 / 0.18%, ATR14(1h) 278.05). EOD re-mark against Kraken last 77670.1 → BTC MTM $2,625.25, unrealized −$0.27 gross (−0.01R). Day PnL −$7.10 (entry comm $6.83 + 0.05% slippage; no realized closes this trading day). Equity $10,497.38, DD 2.16% from peak $10,728.95. No exit rule fired this wake — routine-01 used the just-closed 14:00→15:00Z 1H bar to enter; no new 1H bar has closed between the two firings, so exit re-evaluation has no fresh candle. No second entry this wake either (rule 8 same-bar guard: routine-01 already consumed the 14:00Z close; opening a second pair on the identical bar would defeat rule 8's stated purpose "prevent same-bar cluster fills"). Kill switches all clear. Routine-01 rebuild marker (last px 77687.6, equity $10,497.97) retained for audit in the prior version of this file via git history. Prior binding correction retained below: XRP/USD true exit was the 2026-05-15T04:00Z 1H 20-EMA cross; the 2026-05-15T13:00Z stop row is superseded by `correction-previous-row`.

## Account

- Starting equity: **$10,000.00**
- Cash: **$7,872.13**
- Realized PnL (all-time): **+$504.48**
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
  - HYPE +$413.62 (missed-scheduler replay exit-4R-target 2026-05-21T08:00Z, +4.04R)
  - TAO −$29.84 (missed-scheduler replay exit-ema20-confirm 2026-05-22T01:00Z, −0.50R)
  - HYPE −$33.98 (missed-scheduler replay exit-ema20-confirm 2026-05-22T02:00Z, −0.29R)
  - SOL −$45.64 (missed-scheduler replay exit-stop-hit 2026-05-22T15:00Z, −1.43R)
  - AVAX −$35.83 (missed-scheduler replay exit-ema20-confirm 2026-05-22T16:00Z, −0.94R)
- Unrealized PnL: **−$0.27** (BTC @ last 77670.1 vs entry 77678.12: 0.0338 × −8.02 = −$0.27, −0.01R; entry comm $6.83 already deducted from cash, close-side comm ~$6.83 not yet booked)
- Position values (MTM): **$2,625.25** (0.0338 × 77670.1)
- Current equity (cash + positions MTM): **$10,497.38**
- Equity peak: **$10,728.95** (set 2026-05-21 during missed-scheduler HYPE 4R take-profit replay)
- Drawdown from peak: **2.16%**

## Open positions

| Pair | Side | Size | Entry | Stop | Stop dist | R-risk | Last px | Unreal PnL | Unreal R |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| BTC/USD | long | 0.0338 | 77678.12 | 77122.02 | 556.10 | $18.80 (0.18%) | 77670.1 | −$0.27 | −0.01 |

Portfolio risk-at-moment: **0.18%** of equity (cap 4%).
Open positions: **1 / 8** (strategy v0.4 max-concurrent 4 → 1/4 used; cluster {BTC,ETH,SOL,TAO,AVAX,SUI,LINK} 1/2).

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

- Daily realized: $0 today (no closes); day PnL incl. unrealized −$7.10 ≈ **−0.07%** — within 5% LOSS cap. Prior active day 2026-05-22 realized −$145.29 (−1.36%).
- Consecutive losing trading days: 05-21 W, 05-22 L → streak **1** (cap 7); no trading days 05-23/05-24 (weekend); 05-25 has 1 open / 0 closed so streak unchanged.
- Max drawdown: 2.16% from peak $10,728.95 (cap 25%, warn 12.5%) — clear
- Equity floor: $10,497.38 > $7,500 floor — OK
- **All clear. Trading authorized.** 1 open position (BTC long).
- **2026-05-25 routine-01 regime note:** entry rule 5a regime gate PASS — 15/15 universe pairs positive on 24h (ADA +1.66, AVAX +2.93, ETH +1.49, FARTCOIN +2.78, HYPE +0.51, LINK +1.99, LTC +0.28, PENGU +1.56, SOL +1.24, SUI +2.20, TAO +1.63, TRX +2.02, BTC +0.92, XDG +0.86, XRP +0.82); median +1.56%. Not synchronized breakdown (need ≤1/15 positive AND median ≤ −1.0%). Kraken risk_flag CLEAR "Markets calm" 2026-05-25T13:53:49Z. Liquidity floor (24h notional ≥ $2M) screened universe to 7 pairs: BTC ($79M), ETH ($58M), HYPE ($23M), SOL ($12M), XRP ($8M), SUI ($7M), TAO ($5M). Per rule 8 single-entry-per-wake, BTC (rank 1) took the slot; ETH/SOL/XRP/TAO/HYPE/SUI logged HOLD-OFF.
- **2026-05-25 routine-03-eod note:** Fired in same UTC window as routine-01 (scheduled-task runner catching up after multi-day stall). EOD MTM-only against BTC last 77670.1 → unrealized −$0.27 (effectively scratch). No exit checks meaningful — same just-closed 1H bar as entry. No second entry taken (rule 8 same-bar guard; next 1H close 16:00Z will permit fresh evaluation). Kill switches independently rechecked: daily PnL −0.07%, DD 2.16%, equity floor clear, streak 1/7. All clear.

## Pending exit triggers

- BTC/USD: stop 77122.02 (2×ATR from entry); 4R target 79902.52; EMA-cross exit per W22-G requires two consecutive 1H closes < 20-EMA; breakeven ratchet activates when unrealized R ≥ 2.0 at any 1H close.

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | ≈ +5.8% (approx) | ≈ −3 to −4% (approx) | ≈ +9% (approx) | BULL ahead (approx) |
| 30d | — | — | — | — |
| 90d | — | — | — | — |

(7d figures approximate — precise reference-price computation deferred to routine #4. 30d window pre-dates BULL inception 2026-04-20; first computable 2026-05-20.)
