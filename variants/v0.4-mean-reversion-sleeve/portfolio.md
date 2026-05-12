# Variant v0.4-mean-reversion-sleeve — Synthetic Portfolio

> **Paper-paper account.** Synthetic $10K starting equity.
> **Last rebuild:** 2026-05-13T05:00:00Z (routine-07 wake 2026-05-12 22:00 PT — no trades; see notes)

## Account

- Starting equity: **$10,000.00**
- Cash: **$10,000.00**
- Realized PnL (variant lifetime): **$0.00**
- Unrealized PnL: **$0.00** (no open positions)
- Position values (MTM): **$0.00**
- Current equity: **$10,000.00**
- Equity peak: **$10,000.00**
- Drawdown from peak: **0.00%**

## Open positions

(none)

Portfolio risk-at-moment: **0.00%** (cap 4%).
Open positions: **0 / 2** (variant max-concurrent 2 — mean-reversion sized smaller than momentum).

## Active kill-switch state

- Daily realized: **0.00%** (cap 5%)
- Consecutive losing trading days: 0 (cap 7)
- Max drawdown: 0.00% (cap 25%, warn 12.5%)
- Equity floor: $10,000 > $7,500 floor — OK
- **All clear.**

## Rolling performance vs main BULL v0.2

| Window | v0.4 return | v0.2 main return | Delta | BTC-hold | Result |
|--------|-------------|------------------|-------|----------|--------|
| 7d  | — | — | — | — | not yet 7 days live |
| 30d | — | — | — | — | not yet 30 days live (earliest 2026-05-29) |
| 90d | — | — | — | — | not yet 90 days live |

## Days live

- Spin-up: 2026-04-29
- As of last rebuild: **13 days**
- Promotion-eligible date: 2026-05-29

## Notes

Tests whether BULL's mandate-allowed-but-unused mean-reversion bucket adds edge uncorrelated to momentum. Looks for oversold bounces (RSI < 25) in pairs whose 4H trend is structurally bullish. Variant-internal bucket allocation is `mean-reversion: 100%`; main BULL bucket allocation in `memory/strategy.md` is unchanged at `momentum: 100%`.

### Routine #7 wake log

- **2026-05-12 22:00 PT (this wake)** — past-24h replay window = 2026-05-11 16:00 UTC → 2026-05-12 16:00 UTC. EOD-prior (04:00 UTC) lowest 1H RSI was TRX/USD 33.0 — no pair hit M2 RSI<25. OVERNIGHT (13:00 UTC) FARTCOIN/USD reached 20.9 RSI but failed M1 (insufficient 4H history for 200-EMA on a meme listing); other low-RSI pairs (PENGU 25.4, ETH 26.0) above the <25 threshold. Result: 0 entries, 0 open positions. All kill switches clear at $10,000 equity.
