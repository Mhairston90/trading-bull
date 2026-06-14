# Variant v0.12-sbd-exit — Synthetic Portfolio

> **Paper-paper account.** Synthetic $10K starting equity.
> **Category:** LAB hypothesis / instrumented twin (SBD classifier + 9-EMA defensive exit vs v0.2 baseline)
> **Last rebuild:** 2026-06-14T05:00Z (routine-07 wake 2026-06-13 22:00 PT — TAO CLOSE +4.29R/+$636.09, BTC OPEN OVERNIGHT/CLOSE −0.37R/−$25.55, BTC OPEN EOD; 10 closed trades lifetime)
>
> **LEADERBOARD-SOURCED — FORWARD PAPER-PAPER ONLY.** Rebuilt from this variant's
> `trade_log.md`. The 2026-05-19→2026-05-29 trades were recovered on 2026-05-29
> (user-authorized) after a routine-#7 scheduler gap; see trade_log.md header.

## Account

- Starting equity: **$10,000.00**
- Cash: **$0.62** ($10,491.28 − 0.1631 BTC × $64,320.2 notional ≈ $0.62)
- Realized PnL: **+$491.28** (8 prior trades −$119.26; TAO +$636.09 +4.29R closed 2026-06-13T09:00Z; BTC OVERNIGHT −$25.55 −0.37R closed 2026-06-13T18:00Z; BTC void $0.00)
- Unrealized PnL: **$0.00** (BTC 0.1631 × ($64,320.2 − $64,320.2) = $0 at EOD entry price)
- Position values (MTM): **$10,490.66** (BTC 0.1631 × $64,320.2)
- Current equity: **$10,491.28**
- Equity peak: **$10,606.00** (set from prior HYPE win — not surpassed this wake)
- Drawdown: **1.08%** (($10,606 − $10,491.28) / $10,606)

## Open positions

| Pair | Side | Size | Entry | Entry time (UTC) | Stop | 4R target | Risk ($) | Risk (% equity) |
|------|------|------|-------|------------------|------|-----------|----------|-----------------|
| BTC/USD | long | 0.1631 | 64320.2 | 2026-06-14T04:00Z | 63897.22 | 66012.12 | 68.98 | 0.66% |

Open positions: **1 / 4** (cluster {BTC,ETH,SOL,TAO,AVAX,SUI,LINK} 1/2). Portfolio risk-at-moment: **0.66%** (cap 4%). SBD CLEARED → W22-G 2-bar exit active on this position.

## Active kill-switch state

- Daily realized: +$610.54 (TAO +$636.09 − BTC OVERNIGHT $25.55; net positive) — clear vs 5% cap
- Consecutive losing trading days: 0 (cap 7)
- Max drawdown: 1.08% from peak $10,606.00 (cap 25%, warn 12.5%) — clear
- Equity floor: $10,491.28 > $7,500 — OK
- SBD state: CLEARED — W22-G 2-bar exit active on BTC position (no 9-EMA tightening)
- **All clear. 1 open position (BTC/USD). 10 closed trades lifetime.**

## Performance (2026-05-19 → 2026-06-09)

| Metric | Value |
|--------|-------|
| Closed trades | 10 (8 prior + TAO +4.29R + BTC OVERNIGHT −0.37R; void excluded) |
| Win rate | 30% (3/10: HYPE +4.04R, HYPE +0.12R, TAO +4.29R) |
| Avg R per trade | +0.33 (net R sum 3.27 / 10 trades) |
| Profit factor | 1.63 (8.45 winners / 5.18 losers) |
| Net return | +4.91% (equity $10,491.28 vs $10,000 start; BTC EOD open) |
| Max drawdown | 1.08% (from peak $10,606) |

> Conservative vs the SBD hypothesis: exits use v0.2/20-EMA timing; the SBD 9-EMA
> tightening would only have reduced the losers further. The single 4R winner
> (HYPE) hit the take-profit target, which SBD does not alter.

## Days live

- Spin-up: 2026-05-19
- As of last rebuild: **26 days**
- Promotion-eligible: 2026-06-18 — **10 closed trades (threshold reached!) → promotion-eligible by trade count.** BTC EOD open. See routine-04 for promotion review gate.

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
- **2026-06-13 22:00 PT (routine-07)** — replay window 2026-06-13T05:08Z → 2026-06-14T05:00Z (~23.87h). **EXIT — TAO/USD CLOSE 2026-06-13T09:00Z @ $237.3015:** 08:00Z bar close ≥ 4R target $235.9396. PnL: 31.78 × $20.0155 = **+$636.09 / +4.29R**. SBD CLEARED → standard exit; 4R fires first. Cash $10,516.83. Total realized +$516.83 (from −$119.26). DD from peak $10,606 now 0.84% ($89.17). **OVERNIGHT 13:00Z:** BTC passes R1-R4, SBD CLEARED → W22-G 2-bar exit active. **ENTRY: BTC/USD LONG 0.1641 @ $64,100.0, stop $63,677.02, target $65,791.92.** SBD telemetry: SBD CLEARED at entry → W22-G 2-bar exit, not 9-EMA tightening. **EXIT — BTC CLOSE 2026-06-13T18:00Z @ $63,944.3:** 17:00Z bar close $63,944.3 < EMA20 ~$63,998 — 2nd consecutive close below 1H EMA20 (16:00Z close $63,988.5 [1st], 17:00Z $63,944.3 [2nd]) → W22-G 2-bar rule fires. PnL: 0.1641 × −$155.7 = **−$25.55 / −0.37R**. Cash $10,491.28. Total realized +$491.28. **EOD 2026-06-14T04:00Z (indicators.py):** 15/15 positive, SBD CLEAR → W22-G 2-bar exit active. BTC passes all rules. **ENTRY: BTC/USD LONG 0.1631 @ $64,320.2, stop $63,897.22, target $66,012.12.** SBD telemetry: CLEARED throughout — 0 SBD exposure this wake, 0 avoided-give-back. **MILESTONE: 10 closed trades reached this wake (threshold for promotion-eligible). Avg R +0.33, profit factor 1.63. Promotion gate opens 2026-06-18 but competition deadline 2026-07-01 — routing #4 to review.** Kill switches all clear. Equity $10,491.28, DD 1.08% from peak $10,606. Days live: **26**.
