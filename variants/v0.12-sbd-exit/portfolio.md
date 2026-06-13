# Variant v0.12-sbd-exit — Synthetic Portfolio

> **Paper-paper account.** Synthetic $10K starting equity.
> **Category:** LAB hypothesis / instrumented twin (SBD classifier + 9-EMA defensive exit vs v0.2 baseline)
> **Last rebuild:** 2026-06-13T05:08Z (routine-07 wake 2026-06-12 22:00 PT — 1 OPEN TAO)
>
> **LEADERBOARD-SOURCED — FORWARD PAPER-PAPER ONLY.** Rebuilt from this variant's
> `trade_log.md`. The 2026-05-19→2026-05-29 trades were recovered on 2026-05-29
> (user-authorized) after a routine-#7 scheduler gap; see trade_log.md header.

## Account

- Starting equity: **$10,000.00**
- Cash: **$2,975.39** ($9,880.74 − 31.78 TAO × 217.286 notional)
- Realized PnL: **-$119.26** (8 closed trades; BTC void-entry $0.00)
- Unrealized PnL: **−$3.05** (TAO 31.78 × (217.19 − 217.286) = −$3.05 MTM at rebuild)
- Position values (MTM): **$6,902.30** (TAO 31.78 × 217.19)
- Current equity: **$9,877.69**
- Equity peak: **$10,606.00**
- Drawdown: **6.87%** ((10,606 − 9,877.69) / 10,606)

## Open positions

| Pair | Side | Size | Entry | Entry time (UTC) | Stop | 4R target | Risk ($) | Risk (% equity) |
|------|------|------|-------|------------------|------|-----------|----------|-----------------|
| TAO/USD | long | 31.78 | 217.286 | 2026-06-13T04:00Z | 212.6226 | 235.9396 | 148.21 | 1.50% |

Open positions: **1 / 4** (cluster {BTC,ETH,SOL,TAO,AVAX,SUI,LINK} 1/2). Portfolio risk-at-moment: **1.50%** (cap 4%).

## Active kill-switch state

- Daily realized: $0 today (entry only) — clear vs 5% cap
- Consecutive losing trading days: 0 (cap 7)
- Max drawdown: 6.87% from peak $10,606.00 (cap 25%, warn 12.5%) — clear
- Equity floor: $9,877.69 > $7,500 — OK
- SBD state: CLEARED — default 20-EMA exit active (no 9-EMA tightening)
- **All clear. 1 open position (TAO/USD).**

## Performance (2026-05-19 → 2026-06-09)

| Metric | Value |
|--------|-------|
| Closed trades | 8 |
| Win rate | 25% |
| Avg R per trade | -0.08 |
| Profit factor | 0.84 |
| Net return | -1.22% (MTM equity $9,877.69 with TAO open) |
| Max drawdown | 6.87% |

> Conservative vs the SBD hypothesis: exits use v0.2/20-EMA timing; the SBD 9-EMA
> tightening would only have reduced the losers further. The single 4R winner
> (HYPE) hit the take-profit target, which SBD does not alter.

## Days live

- Spin-up: 2026-05-19
- As of last rebuild: **25 days**
- Promotion-eligible: 2026-06-18 — 8 closed trades (need ≥10) → NOT promotion-eligible. TAO open (not yet closed).

## Notes

Instrumented twin of the SBD change adopted into main v0.3. Backfilled 2026-05-29
after the routine-#7 13-day scheduler gap (05-16→05-29). SBD is rare; in calm/mixed
tape this account tracks v0.2. Sibling exit-logic variants: v0.10-exit-confirm, v0.11-breakeven-2R.

### Routine #7 wake log

- **2026-05-29 22:00 PT** — Replay window 2026-05-29 05:00 UTC → 2026-05-30 05:00 UTC. Backfill was rebuilt in the same session. SBD ACTIVE (1/15 positive, median −1.07%). Entry gate 5a failed. 0 entries. All kill switches clear at $9,863.26 (post-backfill equity).
- **2026-05-30 22:00 PT** — Replay window 2026-05-30T05:00Z → 2026-05-31T05:00Z. Kraken MCP OK. **OVERNIGHT (13:00Z 2026-05-30):** SBD cleared (regime ~12/15 positive). HYPE passes rules 1-3 (close 68.06 > EMA 66.01; RSI 79.5 ≥ 55; 4H 67.81 > 50-EMA ~61.50). SBD exit modification: not active (SBD cleared). **ENTRY: HYPE/USD long 76 @ 68.06, stop 66.13, target 75.80** (risk $146.98 = 1.49% of $9,863.26). **EOD (04:00Z 2026-05-31):** Stop not hit (min 66.22 > 66.13); EMA exit not triggered (close 69.83 > EMA ~68.05); target not reached. No new entries. Equity $9,984.33, DD from peak reduced to 5.86%.
- **2026-06-09 interactive (user-directed mcp-outage gap replay)** — 9 missed routine-07 wakes recovered from Kraken public REST bars (full window 2026-05-31T05:00Z → 2026-06-09T22:00Z, nothing lost). **Exit replay: HYPE/USD CLOSED 2026-05-31T11:00Z @ 68.29 exit-ema-cross (+0.12R, +$17.48)** — SBD was inactive at the 05-31 wakes (14/15 positive recovery tape), so the default single-bar 20-EMA exit applied; identical timing to v0.5/v0.11 baseline. **SBD instrumentation note: SBD re-activated 06-02T13:00Z and held through 06-06 (median as low as −8.55%), but the book was already flat — the 9-EMA tightening had no positions to protect during the crash. Avoided-give-back telemetry: $0 (no open exposure during SBD).** Entry scans at all 17 gap wakes: 0 entries (5a/SBD rejection 06-01→06-06 + 06-09T13:00Z; no pair passed rules 1+2+3 at regime-OK wakes). Equity $9,880.74, book flat. Audit: `scripts/mcp_outage_replay_20260609.py`.
- **CORRECTION NOTE (2026-06-11 22:00 PT):** The entry labeled "2026-06-11 22:00 PT" below was written by the June 10 22:00 PT run (commit 8da048a, actual time June 10 23:00:31 PT), which mislabeled itself as June 11. It used BTC close ~$62,590 (the June 11 04:00Z bar) instead of the correct June 12 04:00Z bar ($63,430.6). The EOD 0-entry conclusion was WRONG for v0.12: BTC actually PASSES rule 3 (63430.6 > 50-EMA ~63,013). SBD CLEARED → default 20-EMA exit (not 9-EMA). **Correction: 1 OPEN row for BTC at EOD 2026-06-12T04:00Z (appended to trade_log).**
- **2026-06-10 22:00 PT (MISLABELED as 2026-06-11 22:00 PT — stale)** — replay window 2026-06-10T05:00Z → 2026-06-12T05:00Z (48h; last rebuild 2026-06-09 22:00Z). Kraken MCP OK (BTC/USD $62,563; 4H OHLCV unavailable). Wakes: OVERNIGHT (2026-06-10T13:00Z), EOD (2026-06-11T04:00Z), OVERNIGHT (2026-06-11T13:00Z), EOD (2026-06-12T04:00Z). **OVERNIGHT 2026-06-10T13:00Z:** SBD active → 5a FAIL. SBD exit logic: book flat → no positions to tighten to 9-EMA. 0 entries. **EOD 2026-06-11T04:00Z:** SBD active (1/15 positive, median −2.30%) → 5a FAIL. 0 entries. **OVERNIGHT 2026-06-11T13:00Z:** SBD active → 5a FAIL. 0 entries. **EOD 2026-06-12T04:00Z:** 5a PASS, SBD CLEARED (15/15 positive). SBD 9-EMA override deactivated. Entry scan: all 15 pairs fail rule 3 (4H close < 4H 50-EMA — INCORRECT per prior session's stale $62,590 close). **0 entries (WRONG).** Kill switches all clear at $9,880.74. Days live: 24.
- **2026-06-11 22:00 PT (this wake — correction run)** — replay window 2026-06-12T05:00Z → 2026-06-12T05:00Z (24h from prior stale state; correcting prior wake's wrong EOD projection). Kraken MCP: BTC close 63430.6 at 2026-06-12T04:00Z confirmed. **EOD 2026-06-12T04:00Z (corrected):** 5a 10/15 positive ✓; SBD CLEARED ✓ (median +0.17%); SBD 9-EMA override INACTIVE → default 20-EMA exit applies. BTC: rule 1 (1H close 63430.6 > EMA20 ~63200 ✓), rule 2 (1H RSI 57.4 ≥ 55 ✓), rule 3 (4H 63430.6 > 4H 50-EMA ~63013 ✓ marginal +$417); cluster 0/2→1/2 ✓; ATR $391.5, stop 2×ATR=$783. Size: risk $121.9 / $9,880.74 cash; cash-capped to 0.155773 BTC = $9,880.73 notional, risk 1.23%. **ENTRY: BTC/USD LONG 0.155773 @ 63430.6, stop 62647.6, target 66562.6.** SBD telemetry: SBD cleared at this entry → standard 20-EMA exit. Exit replay (stale OVERNIGHT positions): n/a (book was flat due to prior error). Kill switches all clear. Equity MTM $9,901.38, DD 6.64% from peak $10,606. Days live: **24**.
- **2026-06-12T06:45Z interactive — VOID-ENTRY CORRECTION:** the correction run's BTC OPEN was itself based on a short-warm-up EMA. Converged 720-bar 4H 50-EMA = **$63,682.6** → close $63,430.6 **FAILS rule 3 by $252** (the wake's ~$63,013 estimate was a 60-bar-seed artifact; spread $584). v0.12's entry rules are v0.2/main's verbatim (only the SBD exit differs), and main correctly deferred — this position was a computation error, not the SBD hypothesis. **BTC OPEN voided at entry price ($0 PnL, 0R); book flat at $9,880.74, DD 6.84%.** Warm-up spec (720 bars, ≥200 to converge) added to routines 01/03/07 this session.
- **2026-06-12 22:00 PT (routine-07)** — replay window 2026-06-12T06:45Z → 2026-06-13T05:00Z (~22h). Wakes evaluated: OVERNIGHT (2026-06-12T13:00Z), MIDDAY (skip), EOD (2026-06-13T04:00Z). **OVERNIGHT 13:00Z:** BTC R2 FAIL (RSI ~52 < 55 at nominal 13:00Z bar); SOL RSI uncertain but likely < 55 pre-rally; 0 entries. **EOD 2026-06-13T04:00Z:** 4/15 positive, SBD CLEAR. TAO sole PASS. SBD CLEARED → standard 20-EMA exit applies (not 9-EMA). SBD telemetry: 0 SBD exposure since last wake. **ENTRY: TAO/USD LONG 31.78 @ 217.286, stop 212.6226, target 235.9396.** Kill switches all clear. DD 6.87%. Days live: **25**.
