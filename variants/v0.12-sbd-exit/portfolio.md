# Variant v0.12-sbd-exit — Synthetic Portfolio

> **Paper-paper account.** Synthetic $10K starting equity.
> **Category:** LAB hypothesis / instrumented twin (SBD classifier + 9-EMA defensive exit vs v0.2 baseline)
> **Last rebuild:** 2026-05-19T00:00:00Z (initial spin-up)

## Account

- Starting equity: **$10,000.00**
- Cash: **$10,000.00**
- Realized PnL: **$0.00**
- Unrealized PnL: **$0.00**
- Current equity: **$10,000.00**
- Equity peak: **$10,000.00**
- Drawdown: **0.00%**

## Open positions

(none)

Open positions: **0 / 4** (momentum cap inherited from v0.2 rule 6).

## Active kill-switch state

All clear at $10,000 equity.

## Rolling performance

| Window | v0.12 return | v0.2 baseline | main v0.3 | Verdict |
|--------|--------------|---------------|-----------|---------|
| 7d  | — | — | — | not yet 7 days live |
| 30d | — | — | — | not yet 30 days live (earliest 2026-06-18) |

## SBD telemetry (avoided-give-back log)

| Wake (UTC) | SBD active? | Breadth (pos/15) | Median 24h % | Open pos | 9-EMA exit unreal R | Modeled 20-EMA exit R | Est. give-back avoided |
|------------|-------------|------------------|--------------|----------|---------------------|-----------------------|------------------------|
| (none yet — spun up 2026-05-19) | | | | | | | |

## Days live

- Spin-up: 2026-05-19
- Promotion-eligible: 2026-06-18

## Notes

Instrumented twin of the SBD change adopted live into main v0.3 (Ring-2 2026-W21-F, user `[Y B]` + variant, 2026-05-19). Isolates the synchronized-breakdown exit-tightening so its avoided-give-back can be measured cleanly vs the v0.2 pre-change baseline, independent of live-execution noise. SBD is rare — in calm/mixed tape this account is identical to v0.2. Sibling exit-logic variants: v0.10-exit-confirm, v0.11-breakeven-2R.
