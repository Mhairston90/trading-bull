# Variant v0.12-sbd-exit — Synthetic Portfolio

> **Paper-paper account.** Synthetic $10K starting equity.
> **Category:** LAB hypothesis / instrumented twin (SBD classifier + 9-EMA defensive exit vs v0.2 baseline)
> **Last rebuild:** 2026-05-29T22:30:00Z (gap-recovery backfill applied — see trade_log.md header)
>
> **LEADERBOARD-SOURCED — FORWARD PAPER-PAPER ONLY.** Rebuilt from this variant's
> `trade_log.md`. The 2026-05-19→2026-05-29 trades were recovered on 2026-05-29
> (user-authorized) after a routine-#7 scheduler gap; see trade_log.md header.

## Account

- Starting equity: **$10,000.00**
- Cash: **$9,863.26**
- Realized PnL: **-136.74**
- Unrealized PnL: **$0.00** (flat — no open positions)
- Current equity: **$9,863.26**
- Equity peak: **$10,606.00**
- Drawdown: **7.00%**

## Open positions

(none)

Open positions: **0 / 4** (momentum cap inherited from v0.2 rule 6).

## Active kill-switch state

All clear. Max drawdown over the backfilled window was 7.00% (killswitch 25%).

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
- Promotion-eligible: 2026-06-18

## Notes

Instrumented twin of the SBD change adopted into main v0.3. Backfilled 2026-05-29
after the routine-#7 13-day scheduler gap (05-16→05-29). SBD is rare; in calm/mixed
tape this account tracks v0.2. Sibling exit-logic variants: v0.10-exit-confirm, v0.11-breakeven-2R.
