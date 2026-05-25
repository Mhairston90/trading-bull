# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-05-25 routine-02-midday — MTM-only re-mark against Kraken last 77370.3 (XXBTZUSD ticker @ ~20:00Z). No exit rule fired this wake: latest closed 1H bar 19:00Z close 77384.6 sits above the rebuilt 20-EMA 77290.75 (W22-G two-bar EMA-confirm exit not even one bar deep); 2×ATR stop 77122.02 not pierced intra-bar (lowest 1H low since entry = 77300.0 at 19:00Z); 4R target 79902.52 untouched; unrealized R = (77370.3 − 77678.12)/(77678.12 − 77122.02) = −0.554, well below the +2R breakeven ratchet threshold. Per routine #2 mandate, NO new entries this midday wake (entry responsibility is overnight/EOD only). Kill switches all clear. Equity $10,487.25, DD 2.25% from peak $10,728.95 (warn threshold 12.5%), day PnL −$17.23 / −0.16% vs flat day-open equity $10,504.48. No Telegram (no exit, no kill switch, no drawdown warning). Prior routine-03-eod rebuild marker (last px 77670.1, equity $10,497.38) superseded; binding XRP correction (2026-05-15T04:00Z exit-ema-cross −$21.92) preserved below for audit.

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
- Unrealized PnL: **−$10.40** (BTC @ last 77370.3 vs entry 77678.12: 0.0338 × −307.82 = −$10.40, −0.554R; entry commission $6.83 already deducted from cash, close-side commission ~$6.83 not yet booked)
- Position values (MTM): **$2,615.12** (0.0338 × 77370.3)
- Current equity (cash + positions MTM): **$10,487.25**
- Equity peak: **$10,728.95** (set 2026-05-21 during missed-scheduler HYPE 4R take-profit replay)
- Drawdown from peak: **2.25%**

## Open positions

| Pair | Side | Size | Entry | Stop | Stop dist | R-risk | Last px | Unreal PnL | Unreal R |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| BTC/USD | long | 0.0338 | 77678.12 | 77122.02 | 556.10 | $18.80 (0.18%) | 77370.3 | −$10.40 | −0.55 |

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

- Daily realized: $0 today (no closes); day PnL incl. unrealized −$17.23 = **−0.16%** vs day-open equity $10,504.48 — within 5% LOSS cap. Prior active day 2026-05-22 realized −$145.29 (−1.36%).
- Consecutive losing trading days: 05-21 W, 05-22 L → streak **1** (cap 7); no trading days 05-23/05-24 (weekend); 05-25 has 1 open / 0 closed so streak unchanged.
- Max drawdown: 2.25% from peak $10,728.95 (cap 25%, warn 12.5%) — clear, well below warn
- Equity floor: $10,487.25 > $7,500 floor — OK
- **All clear. Trading authorized.** 1 open position (BTC long).
- **2026-05-25 routine-02-midday note:** Mark-to-market only (routine #2 does NOT open new positions). Latest closed 1H bar 19:00Z close 77384.6; 20-EMA at 19:00Z ≈ 77290.75 (seed SMA of 05-23 09:00→05-24 04:00 = 75884.445, iterated forward with α=2/21); close > EMA, so the W22-G two-bar EMA-confirm exit has zero bars of confirmation. Stop 77122.02 unhit — lowest 1H low since entry (15:00→19:00Z) = 77300.0 at 19:00Z; partial 20:00Z bar low 77361.2. Unrealized R −0.554 — well below the +2R breakeven ratchet trigger. Per rule 3 (4R target 79902.52), no take-profit. Kraken risk_flag re-checked 2026-05-25T13:53:49Z CLEAR. No exits, no entries, no Telegram. Next exit re-eval at 21:00Z 1H close.

## Pending exit triggers

- BTC/USD: stop 77122.02 (2×ATR from entry, fixed); 4R target 79902.52; EMA-cross exit per W22-G requires two consecutive 1H closes < 20-EMA (20-EMA at 19:00Z ≈ 77290.75; no bars below EMA yet); breakeven ratchet activates when unrealized R ≥ 2.0 at any 1H close (currently −0.55R).

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | ≈ +5.6% (approx) | ≈ −3 to −4% (approx) | ≈ +9% (approx) | BULL ahead (approx) |
| 30d | — | — | — | — |
| 90d | — | — | — | — |

(7d figures approximate — precise reference-price computation deferred to routine #4. 30d window pre-dates BULL inception 2026-04-20; first computable 2026-05-20.)
