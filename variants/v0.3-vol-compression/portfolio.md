# Variant v0.3-vol-compression — Synthetic Portfolio

> **Paper-paper account.** Synthetic $10K starting equity. Does NOT affect main BULL portfolio or any real broker.
> **Rebuilt each routine #7 wake** from this variant's `trade_log.md`.
> **Last rebuild:** 2026-04-29T22:00:00Z (initial spin-up — no trades yet)

## Account

- Starting equity: **$10,000.00**
- Cash: **$10,000.00**
- Realized PnL (variant lifetime): **$0.00**
- Unrealized PnL: **$0.00** (no open positions)
- Position values (MTM): **$0.00**
- Current equity (cash + positions MTM): **$10,000.00**
- Equity peak: **$10,000.00** (set at spin-up 2026-04-29)
- Drawdown from peak: **0.00%**

## Open positions

(none — variant spun up today, awaiting first routine #7 simulation wake)

Portfolio risk-at-moment: **0.00%** (cap 4%).
Open positions: **0 / 8** (variant max-concurrent 4 → 0/4 used; cluster cap 0/2).

## Active kill-switch state

- Daily realized: **0.00%** (cap 5%)
- Daily realized + unrealized: **0.00%** (cap 5%)
- Consecutive losing trading days: 0 (cap 7)
- Max drawdown: 0.00% (cap 25%, warn 12.5%)
- Equity floor: $10,000 > $7,500 floor — OK
- **All clear. Variant authorized to trade paper-paper.**

## Rolling performance (vs main BULL v0.2)

| Window | v0.3 return | v0.2 main return | Delta | BTC-hold | Result |
|--------|-------------|------------------|-------|----------|--------|
| 7d  | — | — | — | — | not yet 7 days live |
| 30d | — | — | — | — | not yet 30 days live (earliest 2026-05-29) |
| 90d | — | — | — | — | not yet 90 days live |

(Populated by routine #7 once windows close.)

## Days live

- Spin-up: 2026-04-29
- As of last rebuild: **0 days**
- Promotion-eligible date: 2026-05-29 (30 days from spin-up)

## Notes

This variant exists to test whether a 0.5× ATR-compression entry gate improves net return / profit factor over main v0.2. See `README.md` and `strategy.md` in this directory for full hypothesis.

The variant runs entirely paper-paper. Its trades have NO effect on the real BULL portfolio in `memory/portfolio.md`. The leaderboard at `memory/leaderboard.md` shows side-by-side performance.
