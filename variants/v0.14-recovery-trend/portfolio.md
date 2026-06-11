# Variant v0.14-recovery-trend — Synthetic Portfolio

> **Paper-paper account.** Synthetic $10K starting equity.
> **Category:** LAB hypothesis (entry rule 3: 4H 20-EMA trend filter vs main's 50-EMA)
> **Last rebuild:** 2026-06-12T05:00Z (routine-07 wake 2026-06-11 22:00 PT — 0 trades; first sim wake; 48h replay; see notes)

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

Open positions: **0 / 4** (momentum cap inherited from v0.4 rule 6).

## Active kill-switch state

All clear at $10,000 equity.

## Rolling performance vs main v0.4

| Window | v0.14 return | main (v0.4) return | Verdict |
|--------|--------------|---------------------|---------|
| 7d  | — | — | not yet 7 days live |
| 30d | — | — | not yet 30 days live (earliest 2026-07-09) |

## Days live

- Spin-up: 2026-06-09
- As of last rebuild: **3 days**
- Promotion-eligible: 2026-07-09 (after the 2026-07-01 competition deadline — this variant is for learning, not the contest)

## Notes

Tests whether replacing the 4H 50-EMA trend filter with a 20-EMA converts confirmed regime recoveries into trades. Evidence at spin-up: during 06-07→06-09 recovery wakes (8-14/15 positive), 0 pairs passed the 50-EMA filter while 1→14 pairs per wake passed the 20-EMA version. Counterfactual first trade (BTC @ 63,078, 06-08T04:00Z) would likely be a small loser in the current rollover — the dead-cat-bounce risk is acknowledged at spin-up. Regime at spin-up: 2/15 positive, median ≈ −2.4% (5a FAIL) — variant starts blocked, same as main.

### Routine #7 wake log

- **2026-06-11 22:00 PT (first sim wake)** — replay window 2026-06-10T05:00Z → 2026-06-12T05:00Z (48h from 2026-06-09 spin-up). Kraken MCP OK (BTC/USD $62,563; 4H OHLCV unavailable — connection error on both retry attempts). Wakes: OVERNIGHT (2026-06-10T13:00Z), EOD (2026-06-11T04:00Z), OVERNIGHT (2026-06-11T13:00Z), EOD (2026-06-12T04:00Z). **OVERNIGHT 2026-06-10T13:00Z:** SBD active → rule 5a FAIL → 0 entries. **EOD 2026-06-11T04:00Z:** SBD active (1/15 positive, median −2.30%) → 5a FAIL → 0 entries. **OVERNIGHT 2026-06-11T13:00Z:** SBD active → 5a FAIL → 0 entries. **EOD 2026-06-12T04:00Z:** 5a PASS, SBD CLEARED (15/15 positive, median +2.72%). Rule 1 (1H close > 1H 20-EMA): BTC ~$62,590 > ~$61,769 ✓. Rule 2 (1H RSI ≥ 55): BTC ~57.9 ✓. **Rule 3 (4H close > 4H 20-EMA — v0.14's EMA filter): 4H OHLCV API UNAVAILABLE (connection error — 2 attempts failed).** From 1H-derived 4H closes: estimated BTC 4H 20-EMA ≈ $62,100–62,300 at this wake vs close $62,590 → rule 3 LIKELY PASSES for BTC (margin ~$300–500). Spin-up evidence (1–14 pairs passed the 20-EMA version at comparable recovery wakes 06-07→06-09) suggests multiple pairs may pass. Vol-compression gate: **v0.14 does NOT inherit vol-comp gate** (by design — isolating the 4H 20-EMA filter). **CONSERVATIVE LOG: 0 entries — 4H 20-EMA could not be confirmed without live 4H OHLCV data. ATR also unavailable for position sizing.** This is potentially v0.14's first simulation-eligible event; the rule 3 estimate will be tracked retrospectively next wake. Exit replay no-op (book flat). Kill switches all clear at $10,000. Days live: **3**.
