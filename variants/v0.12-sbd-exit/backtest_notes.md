# v0.12-sbd-exit — Backtest Notes (NOT leaderboard-sourced)

> **This file is for validation only. `registry.js` does NOT read it.**
> Backtest / reconstructed P&L lives here and must never be copied into
> `trade_log.md` or `portfolio.md` (those are forward-paper-only, leaderboard-sourced).
> Method: manual reconstruction from Kraken 1H OHLCV (`kraken_ohlcv XRPUSD 1h`,
> pulled 2026-05-19). Not a TradingView-harness backtest.

## Question

Over the contest window (2026-05-04 →), what would the SBD rules (5a-SBD +
Exit 1-SBD) have changed vs live v0.2?

## Structural pre-filter

- **Entries: zero change.** 5a-SBD is a strict subset of an already-failing 5a
  (it only classifies when 5a has already rejected all entries). The contest
  entry set under the twin is identical to v0.2.
- **Exits: only the EMA-cross exit is affected, and only while SBD is active.**
  Stop-hits and 4R-target exits are untouched. Contest exit-ema-cross trades:
  LINK 05-07 (+1.69R), BTC 05-06 (+0.06R), XRP 05-15 (−0.14R). LINK/BTC were in
  early-May rally tape (not a synchronized breakdown). The only candidate that
  overlaps the 05-12→05-17 risk-off is **XRP 2026-05-14T16:00Z → 05-15T04:00Z**.

## XRP trade — 9-EMA vs 20-EMA reconstruction

Entry 2026-05-14T16:00Z @ 1.46806 (size 6334, stop 1.44377). Actual exit:
20-EMA cross-down 2026-05-15T04:00Z, close 1.47298 → realized **−$21.92 (−0.14R)**
(per `portfolio.md` correction). XRP ran to a 1H close of 1.53618 @ 05-14T18:00Z
(≈ +2.8R) then round-tripped.

9-EMA (k=0.2), seeded SMA of 9 closes 05-13 19:00→05-14 03:00 = 1.42461,
iterated forward. First 1H close **below** the 9-EMA after entry:

| Bar (UTC) | Close | 9-EMA | Close vs 9-EMA |
|-----------|------:|------:|----------------|
| 05-14 18:00 | 1.53618 | 1.4771 | above |
| 05-14 21:00 | 1.49773 | 1.4912 | above |
| 05-14 22:00 | 1.50056 | 1.4930 | above |
| **05-14 23:00** | **1.48508** | **1.49145** | **BELOW → 9-EMA exit fires** |

9-EMA exit at 05-14T23:00Z, close 1.48508 (fill 1.48434 after 0.05% slippage),
0.26%/side commissions ≈ $48.6 → **≈ +$54 net (≈ +0.5R)**, vs the actual
**−$21.92**. Mechanically the faster exit is worth **≈ +$76 / ≈ +0.6R** on this trade.

## BUT — the SBD gate would NOT have been satisfied

Exit 1-SBD only engages while regime = SYNCHRONIZED_BREAKDOWN (≤1/15 universe
pairs positive 24h AND median 24h ≤ −1.0%). At the 9-EMA exit bar (05-14T23:00Z):

- BULL **entered** XRP at 05-14T16:00Z, which means **rule 5a passed → ≥4/15
  pairs were positive** at 16:00Z. SBD requires ≤1/15.
- XRP was mid-blow-off (+~8% intraday, CoinShares-noted XRP/SOL rotation inflows
  *while BTC bled*) — an **idiosyncratic** pump, not a universe-wide decline.
- `portfolio.md` independently documents the **synchronized 0/15 crash bar as
  2026-05-15T13:00Z** — ~9h *after* BULL had already exited via the normal
  20-EMA cross at 05-15T04:00Z.

For SBD to fire by 05-14T23:00Z, universe breadth would have had to collapse
from ≥4/15 to ≤1/15 within 7 hours while XRP itself was still elevated — and the
documented universe-wide break was a full day later. **Reasoned conclusion:
SBD was not active during the XRP hold; Exit 1-SBD never engages.**

(Caveat: this is a strong inference from the entry-time 5a-pass + the documented
05-15T13:00Z crash timing, not a full 15-pair breadth series. A definitive call
would require pulling 1H OHLCV for all 15 pairs and computing per-bar breadth/
median — offered, not yet run. The 5a-pass-at-entry fact alone makes SBD-by-23:00Z
very unlikely.)

## Verdict

**Over the contest window the SBD twin would have been behaviorally identical to
live v0.2 — net delta ≈ $0. It would not have changed a single contest trade.**

This is not a failure of the rule — it is the rule being correctly *narrow*:
- The XRP give-back was an **idiosyncratic blow-off round-trip**, not a
  synchronized breakdown. SBD is deliberately scoped to universe-wide breaks and
  correctly stays out of idiosyncratic moves.
- The genuine synchronized crash (05-15T13:00Z) arrived after BULL was already
  flat via the ordinary exit.

## Implications (honest)

1. **Evidentiary value of SBD remains ~zero** — the contest contained no
   "holding-a-position-while-SBD-active" event. The rule is unfalsified, not
   validated. The v0.12 forward twin + a future genuine SBD episode are still
   the only real evidence path.
2. The XRP give-back that motivated the lesson is better addressed by a
   **regime-independent** mechanism — exactly what variant **v0.11-breakeven-2R**
   does (stop ratchets to BE at +2R, no regime gate). v0.11 *would* have cut the
   XRP loss; v0.3-SBD would not. Worth noting when both come up for review.
3. SBD's dual breadth+depth threshold may be strict enough that it fires rarely.
   The `sbd_*` params are declared tuneable for exactly this; the autoloop can
   sweep them once forward data exists.

*No `trade_log.md` / `portfolio.md` rows written. Leaderboard unaffected.*
