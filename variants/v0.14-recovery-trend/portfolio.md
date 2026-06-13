# Variant v0.14-recovery-trend — Synthetic Portfolio

> **Paper-paper account.** Synthetic $10K starting equity.
> **Category:** LAB hypothesis (entry rule 3: 4H 20-EMA trend filter vs main's 50-EMA)
> **Last rebuild:** 2026-06-13T05:08Z (routine-07 wake 2026-06-12 22:00 PT — BTC CLOSE +0.01R + TAO OPEN)

## Account

- Starting equity: **$10,000.00**
- Cash: **$3,011.16** ($10,001.25 post-BTC-close − 32.17 TAO × 217.286 notional)
- Realized PnL: **+$1.25** (BTC/USD closed 2026-06-12T22:00Z @ 63438.5, +0.01R, +$1.25)
- Unrealized PnL: **−$3.09** (TAO 32.17 × (217.19 − 217.286) = −$3.09 MTM at rebuild)
- Position values (MTM): **$6,987.00** (TAO 32.17 × 217.19)
- Current equity: **$9,998.16**
- Equity peak: **$10,020.92** (set 2026-06-12T05:00Z rebuild, BTC MTM high)
- Drawdown: **0.23%** ($10,020.92 → $9,998.16)

## Open positions

| Pair | Side | Size | Entry | Entry time (UTC) | Stop | 4R target | Risk ($) | Risk (% equity) |
|------|------|------|-------|------------------|------|-----------|----------|-----------------|
| TAO/USD | LONG | 32.17 | 217.286 | 2026-06-13T04:00Z | 212.6226 | 235.9396 | 150.02 | 1.50% |

Open positions: **1 / 4** (momentum cap, rule 3 uses 4H 20-EMA). Portfolio risk-at-moment: **1.50%** (cap 4%).

## Active kill-switch state

- Daily realized: +$1.25 (BTC closed 2026-06-12T22:00Z, +0.01R) — clear vs 5% cap
- Consecutive losing trading days: 0 (cap 7)
- Max drawdown: 0.23% from peak $10,020.92 (cap 25%, warn 12.5%) — clear
- Equity floor: $9,998.16 > $7,500 — OK
- **All clear. 1 open position (TAO/USD).**

## Rolling performance vs main v0.4

| Window | v0.14 return | main (v0.4) return | Verdict |
|--------|--------------|---------------------|---------|
| 7d  | — | — | not yet 7 days live |
| 30d | — | — | not yet 30 days live (earliest 2026-07-09) |

## Closed trades summary

| Closed | Win rate | Avg R | Net% |
|--------|----------|-------|------|
| 1 | 100% (1/1) | +0.01R | +0.01% |

## Days live

- Spin-up: 2026-06-09
- As of last rebuild: **4 days**
- Promotion-eligible: 2026-07-09 (after the 2026-07-01 competition deadline — this variant is for learning, not the contest). 1 closed trade (BTC +0.01R); TAO open as of this wake.

## Notes

Tests whether replacing the 4H 50-EMA trend filter with a 20-EMA converts confirmed regime recoveries into trades. Evidence at spin-up: during 06-07→06-09 recovery wakes (8-14/15 positive), 0 pairs passed the 50-EMA filter while 1→14 pairs per wake passed the 20-EMA version. Counterfactual first trade (BTC @ 63,078, 06-08T04:00Z) would likely be a small loser in the current rollover — the dead-cat-bounce risk is acknowledged at spin-up. Regime at spin-up: 2/15 positive, median ≈ −2.4% (5a FAIL) — variant starts blocked, same as main.

### Routine #7 wake log

- **2026-06-10 22:00 PT (MISLABELED as 2026-06-11 22:00 PT — first sim wake, stale)** — replay window 2026-06-10T05:00Z → 2026-06-12T05:00Z. Kraken MCP BTC $62,563; 4H OHLCV unavailable. SBD active at OVERNIGHT 13:00Z + EOD 04:00Z wakes → 5a FAIL → 0 entries. EOD 2026-06-12T04:00Z: 5a PASS but used stale close $62,590 and conservative 0-entry due to unavailable 4H data. **0 entries (conservative).**
- **2026-06-11 22:00 PT (correction run — first real entry)** — replay window corrected to 2026-06-12T04:00Z bar using live Kraken pull. BTC close confirmed 63430.6. **EOD 2026-06-12T04:00Z:** 5a 10/15 positive ✓; SBD CLEARED ✓; rule 1 (1H 63430.6 > EMA20 ~63200 ✓); rule 2 (1H RSI 57.4 ≥ 55 ✓); **rule 3 v0.14: 4H 63430.6 > 4H 20-EMA ~62409 ✓ (clear +$1021, well above the ~$62,100–62,300 prior estimate)**; vol-comp gate N/A (v0.14 does not inherit); cluster 0/4→1/4 ✓; ATR $391.5, stop 2×ATR=$783; cash-capped 0.157653 BTC = ~$10,000 notional, risk $123.4 / 1.23% of $10,000. **ENTRY: BTC/USD LONG 0.157653 @ 63430.6, stop 62647.6, target 66562.6.** This is v0.14's FIRST hypothetical trade. Key observation: 20-EMA filter confirmed BTC passes with $1,021 margin vs 50-EMA's marginal $417 — consistent with spin-up thesis that 20-EMA converts early recovery signals into entries while 50-EMA is still recovering. Other pairs not evaluated (BTC is rank-1 and fills cluster slot). Kill switches all clear. Equity MTM $10,020.92, new peak. DD 0%. Days live: **3**.
- **2026-06-12T06:45Z interactive — ENTRY RE-VALIDATED with converged EMAs:** full 720-bar warm-up gives 4H 20-EMA = **$62,652.1** → close $63,430.6 **PASSES v0.14's rule 3 by +$778.5**. The same re-check VOIDED the v0.5/v0.12 BTC entries (converged 4H 50-EMA $63,682.6 → main's rule 3 FAILS by $252). **v0.14 now holds the rack's only live position and is a clean A/B against main's deferral** — the 20-EMA-vs-50-EMA divergence is real (one passes, one fails, on the same bar with converged math), not a data artifact. Position unchanged: BTC/USD LONG 0.157653 @ 63430.6, stop 62647.6, target 66562.6.
- **2026-06-12 22:00 PT (routine-07)** — replay window 2026-06-12T06:45Z → 2026-06-13T05:00Z (~22h). **EXIT — BTC/USD CLOSE 2026-06-12T22:00Z:** Two consecutive 1H closes below 1H 20-EMA triggered exit. Bar opening 20:00Z: close 63,423.1 < EMA ~63,497.6 (1st); bar opening 21:00Z: close 63,438.5 < EMA ~63,491.7 (2nd consecutive). Exit fires at 22:00Z bar close 63,438.5. Stop 62,647.6 never threatened (min low 62,765.3 on 06:00Z bar). 4R target 66,562.6 not reached (max close 63,943.4). PnL: 0.157653 × $7.9 = **+$1.25 / +0.01R**. Cash post-close $10,001.25. **OVERNIGHT 13:00Z:** BTC R2 FAIL (RSI ~52 < 55); 0 entries. BTC exit check: BTC already closed at 22:00Z (before nominal 13:00Z wake time — exit pre-empted OVERNIGHT scan). **EOD 2026-06-13T04:00Z:** 4/15 positive, SBD CLEAR. Pair scan: BTC FAIL R1 (63,494 < EMA20 ~63,526). TAO sole PASS. Rule 1: 217.286 > EMA20 213.406 ✓ (+$3.88). Rule 2: RSI 62.5 ≥ 55 ✓. Rule 3 v0.14: 4H close 217.286 > 4H 20-EMA ~211.3 ✓ (+$5.99 HIGH-CONF). Cluster 0/2→1/2 ✓. Size: risk $150.02 / 1.50% of $10,001.25 post-close equity → 32.17 TAO. **ENTRY: TAO/USD LONG 32.17 @ 217.286, stop 212.6226, target 235.9396.** Same-bar re-entry (BTC closes → TAO opens at same EOD bar). Kill switches all clear. Equity $9,998.16, DD 0.23% from peak $10,020.92. Days live: **4**.
