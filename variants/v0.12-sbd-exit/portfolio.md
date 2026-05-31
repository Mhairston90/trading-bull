# Variant v0.12-sbd-exit — Synthetic Portfolio

> **Paper-paper account.** Synthetic $10K starting equity.
> **Category:** LAB hypothesis / instrumented twin (SBD classifier + 9-EMA defensive exit vs v0.2 baseline)
> **Last rebuild:** 2026-05-31T05:00:00Z (routine-07 wake 2026-05-30 22:00 PT — 1 OPEN)
>
> **LEADERBOARD-SOURCED — FORWARD PAPER-PAPER ONLY.** Rebuilt from this variant's
> `trade_log.md`. The 2026-05-19→2026-05-29 trades were recovered on 2026-05-29
> (user-authorized) after a routine-#7 scheduler gap; see trade_log.md header.

## Account

- Starting equity: **$10,000.00**
- Cash: **$4,677.25**
- Realized PnL: **-$136.74** (from backfilled trades)
- Unrealized PnL: **+$134.52** (HYPE/USD long 76 × (69.83 − 68.06))
- Position values (MTM): **$5,307.08** (76 × $69.83)
- Current equity: **$9,984.33**
- Equity peak: **$10,606.00**
- Drawdown: **5.86%** ((10,606 − 9,984.33) / 10,606)

## Open positions

| Pair | Side | Size | Entry | Stop | Target | Entry time | ATR at entry | SBD exit mod | Unrealized R |
|------|------|------|-------|------|--------|------------|--------------|--------------|-------------|
| HYPE/USD | long | 76 | 68.06 | 66.13 | 75.80 | 2026-05-30T13:00Z | 0.967 | n/a (SBD not active) | +0.92R |

Open positions: **1 / 4** (momentum cap inherited from v0.2 rule 6).

## Active kill-switch state

Daily realized: 0.00% (no closed positions this wake); unrealized: +1.34% (positive). All clear. HYPE/USD long open. Drawdown from peak 5.86% (was 7.00% when flat; recovered with HYPE unrealized gain). KS at 25%.

## Performance (backfilled window 2026-05-19 → 2026-05-26)

| Metric | Value |
|--------|-------|
| Closed trades | 7 |
| Win rate | 14% |
| Avg R per trade | -0.110 |
| Profit factor | 0.82 |
| Net return | -1.37% |
| Max drawdown | 7.00% |

> Conservative vs the SBD hypothesis: exits use v0.2/20-EMA timing; the SBD 9-EMA
> tightening would only have reduced the losers further. The single 4R winner
> (HYPE) hit the take-profit target, which SBD does not alter.

## Days live

- Spin-up: 2026-05-19
- As of last rebuild: **12 days**
- Promotion-eligible: 2026-06-18

## Notes

Instrumented twin of the SBD change adopted into main v0.3. Backfilled 2026-05-29
after the routine-#7 13-day scheduler gap (05-16→05-29). SBD is rare; in calm/mixed
tape this account tracks v0.2. Sibling exit-logic variants: v0.10-exit-confirm, v0.11-breakeven-2R.

### Routine #7 wake log

- **2026-05-29 22:00 PT** — Replay window 2026-05-29 05:00 UTC → 2026-05-30 05:00 UTC. Backfill was rebuilt in the same session. SBD ACTIVE (1/15 positive, median −1.07%). Entry gate 5a failed. 0 entries. All kill switches clear at $9,863.26 (post-backfill equity).
- **2026-05-30 22:00 PT** — Replay window 2026-05-30T05:00Z → 2026-05-31T05:00Z. Kraken MCP OK. **OVERNIGHT (13:00Z 2026-05-30):** SBD cleared (regime ~12/15 positive). HYPE passes rules 1-3 (close 68.06 > EMA 66.01; RSI 79.5 ≥ 55; 4H 67.81 > 50-EMA ~61.50). SBD exit modification: not active (SBD cleared). **ENTRY: HYPE/USD long 76 @ 68.06, stop 66.13, target 75.80** (risk $146.98 = 1.49% of $9,863.26). **EOD (04:00Z 2026-05-31):** Stop not hit (min 66.22 > 66.13); EMA exit not triggered (close 69.83 > EMA ~68.05); target not reached. No new entries. Equity $9,984.33, DD from peak reduced to 5.86%.
