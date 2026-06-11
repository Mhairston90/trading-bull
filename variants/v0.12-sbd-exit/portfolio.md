# Variant v0.12-sbd-exit — Synthetic Portfolio

> **Paper-paper account.** Synthetic $10K starting equity.
> **Category:** LAB hypothesis / instrumented twin (SBD classifier + 9-EMA defensive exit vs v0.2 baseline)
> **Last rebuild:** 2026-06-12T05:00Z (routine-07 wake 2026-06-11 22:00 PT — 0 trades; 48h replay)
>
> **LEADERBOARD-SOURCED — FORWARD PAPER-PAPER ONLY.** Rebuilt from this variant's
> `trade_log.md`. The 2026-05-19→2026-05-29 trades were recovered on 2026-05-29
> (user-authorized) after a routine-#7 scheduler gap; see trade_log.md header.

## Account

- Starting equity: **$10,000.00**
- Cash: **$9,880.74**
- Realized PnL: **-$119.26** (7 backfilled trades −$136.74 + HYPE +$17.48 closed 2026-05-31T11:00Z)
- Unrealized PnL: **$0.00** (no open positions)
- Position values (MTM): **$0.00**
- Current equity: **$9,880.74**
- Equity peak: **$10,606.00**
- Drawdown: **6.84%** ((10,606 − 9,880.74) / 10,606)

## Open positions

_(none — HYPE/USD closed 2026-05-31T11:00Z exit-ema-cross; SBD inactive at the time → default 20-EMA)_

Open positions: **0 / 4** (momentum cap inherited from v0.2 rule 6).

## Active kill-switch state

All clear. Book flat. Drawdown from peak 6.84% (KS at 25%). Equity $9,880.74 > $7,500 floor.

## Performance (2026-05-19 → 2026-06-09)

| Metric | Value |
|--------|-------|
| Closed trades | 8 |
| Win rate | 25% |
| Avg R per trade | -0.08 |
| Profit factor | 0.84 |
| Net return | -1.19% |
| Max drawdown | 7.00% |

> Conservative vs the SBD hypothesis: exits use v0.2/20-EMA timing; the SBD 9-EMA
> tightening would only have reduced the losers further. The single 4R winner
> (HYPE) hit the take-profit target, which SBD does not alter.

## Days live

- Spin-up: 2026-05-19
- As of last rebuild: **24 days**
- Promotion-eligible: 2026-06-18

## Notes

Instrumented twin of the SBD change adopted into main v0.3. Backfilled 2026-05-29
after the routine-#7 13-day scheduler gap (05-16→05-29). SBD is rare; in calm/mixed
tape this account tracks v0.2. Sibling exit-logic variants: v0.10-exit-confirm, v0.11-breakeven-2R.

### Routine #7 wake log

- **2026-05-29 22:00 PT** — Replay window 2026-05-29 05:00 UTC → 2026-05-30 05:00 UTC. Backfill was rebuilt in the same session. SBD ACTIVE (1/15 positive, median −1.07%). Entry gate 5a failed. 0 entries. All kill switches clear at $9,863.26 (post-backfill equity).
- **2026-05-30 22:00 PT** — Replay window 2026-05-30T05:00Z → 2026-05-31T05:00Z. Kraken MCP OK. **OVERNIGHT (13:00Z 2026-05-30):** SBD cleared (regime ~12/15 positive). HYPE passes rules 1-3 (close 68.06 > EMA 66.01; RSI 79.5 ≥ 55; 4H 67.81 > 50-EMA ~61.50). SBD exit modification: not active (SBD cleared). **ENTRY: HYPE/USD long 76 @ 68.06, stop 66.13, target 75.80** (risk $146.98 = 1.49% of $9,863.26). **EOD (04:00Z 2026-05-31):** Stop not hit (min 66.22 > 66.13); EMA exit not triggered (close 69.83 > EMA ~68.05); target not reached. No new entries. Equity $9,984.33, DD from peak reduced to 5.86%.
- **2026-06-09 interactive (user-directed mcp-outage gap replay)** — 9 missed routine-07 wakes recovered from Kraken public REST bars (full window 2026-05-31T05:00Z → 2026-06-09T22:00Z, nothing lost). **Exit replay: HYPE/USD CLOSED 2026-05-31T11:00Z @ 68.29 exit-ema-cross (+0.12R, +$17.48)** — SBD was inactive at the 05-31 wakes (14/15 positive recovery tape), so the default single-bar 20-EMA exit applied; identical timing to v0.5/v0.11 baseline. **SBD instrumentation note: SBD re-activated 06-02T13:00Z and held through 06-06 (median as low as −8.55%), but the book was already flat — the 9-EMA tightening had no positions to protect during the crash. Avoided-give-back telemetry: $0 (no open exposure during SBD).** Entry scans at all 17 gap wakes: 0 entries (5a/SBD rejection 06-01→06-06 + 06-09T13:00Z; no pair passed rules 1+2+3 at regime-OK wakes). Equity $9,880.74, book flat. Audit: `scripts/mcp_outage_replay_20260609.py`.
- **2026-06-11 22:00 PT** — replay window 2026-06-10T05:00Z → 2026-06-12T05:00Z (48h; last rebuild 2026-06-09 22:00Z). Kraken MCP OK (BTC/USD $62,563; 4H OHLCV unavailable). Wakes: OVERNIGHT (2026-06-10T13:00Z), EOD (2026-06-11T04:00Z), OVERNIGHT (2026-06-11T13:00Z), EOD (2026-06-12T04:00Z). **OVERNIGHT 2026-06-10T13:00Z:** SBD active → 5a FAIL. SBD exit logic: book flat → no positions to tighten to 9-EMA. 0 entries. **EOD 2026-06-11T04:00Z:** SBD active (1/15 positive, median −2.30%) → 5a FAIL. 0 entries. **OVERNIGHT 2026-06-11T13:00Z:** SBD active → 5a FAIL. 0 entries. **EOD 2026-06-12T04:00Z:** 5a PASS, SBD CLEARED (15/15 positive). SBD 9-EMA override deactivated. Entry scan: all 15 pairs fail rule 3 (4H close < 4H 50-EMA — same universal fail as sibling v0.5). **0 entries.** Exit replay no-op (book flat). Kill switches all clear at $9,880.74. Drawdown 6.84% unchanged. Days live: **24**.
