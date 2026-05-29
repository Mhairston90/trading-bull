# Variant v0.12-sbd-exit — Synthetic Portfolio

> **Paper-paper account.** Synthetic $10K starting equity.
> **Category:** LAB hypothesis / instrumented twin (SBD classifier + 9-EMA defensive exit vs v0.2 baseline)
> **Last rebuild:** 2026-05-30T05:00:00Z (routine-07 wake 2026-05-29 22:00 PT — no trades; see notes)
>
> **LEADERBOARD-SOURCED — FORWARD PAPER-PAPER ONLY.** Rebuilt only from this
> variant's forward `trade_log.md`. Never reflect backtest/reconstructed P&L
> here — backtest findings live in `backtest_notes.md`, which the leaderboard
> does not read. Equity stays $10,000.00 until the first forward routine-#7 trade.

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
| 2026-05-30T05:00Z | Yes | 1/15 | −1.07% | 0 | N/A (no open positions) | N/A | N/A |

## Days live

- Spin-up: 2026-05-19
- Promotion-eligible: 2026-06-18

## Notes

Instrumented twin of the SBD change adopted live into main v0.3 (Ring-2 2026-W21-F, user `[Y B]` + variant, 2026-05-19). Isolates the synchronized-breakdown exit-tightening so its avoided-give-back can be measured cleanly vs the v0.2 pre-change baseline, independent of live-execution noise. SBD is rare — in calm/mixed tape this account is identical to v0.2. Sibling exit-logic variants: v0.10-exit-confirm, v0.11-breakeven-2R.

### Routine #7 wake log

- **2026-05-29 22:00 PT (first sim wake since 05-19 spin-up)** — past-24h replay window 2026-05-29 05:00 UTC → 2026-05-30 05:00 UTC. Kraken MCP OK (BTC/USD $73,183). Regime: **1/15** pairs positive (HYPE +0.67%), median −1.07%; **SBD ACTIVE** (1/15 ≤1 AND median ≤−1.0%). Wakes evaluated: OVERNIGHT (13:00 UTC), MIDDAY (default-skip), EOD (04:00 UTC). Rule 5a (≥4/15 positive) rejected all entries at both eligible wakes (1/15 positive). 0 entries. No open positions — SBD 9-EMA exit-tightening had nothing to evaluate; telemetry row appended above. All kill switches clear at $10,000 synthetic equity.
