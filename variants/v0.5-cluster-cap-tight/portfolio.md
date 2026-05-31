# Variant v0.5-cluster-cap-tight — Synthetic Portfolio

> **Paper-paper account.** Synthetic $10K starting equity.
> **Last rebuild:** 2026-05-31T05:00:00Z (routine-07 wake 2026-05-30 22:00 PT — 1 OPEN; see notes)

## Account

- Starting equity: **$10,000.00**
- Cash: **$4,745.75**
- Realized PnL (variant lifetime): **$0.00**
- Unrealized PnL: **+$136.29** (HYPE/USD long 77 × (69.83 − 68.06))
- Position values (MTM): **$5,376.91** (77 × $69.83)
- Current equity (cash + positions MTM): **$10,122.66**
- Equity peak: **$10,122.66** (set this wake)
- Drawdown from peak: **0.00%**

## Open positions

| Pair | Side | Size | Entry | Stop | Target | Entry time | ATR at entry | Unrealized R |
|------|------|------|-------|------|--------|------------|--------------|-------------|
| HYPE/USD | LONG | 77 | 68.06 | 66.13 | 75.80 | 2026-05-30T13:00Z | 0.967 | +0.92R |

Portfolio risk-at-moment: **1.49%** (77 × 1.934 / $10,000; cap 4%).
Open positions: **1 / 4** (variant max-concurrent 4; cluster cap: HYPE not in cluster → 0/**1** cluster slot used).

## Active kill-switch state

- Daily realized: **0.00%** (cap 5%) — no closed positions this wake
- Daily realized + unrealized: **+1.23%** — positive, no loss trigger
- Consecutive losing trading days: 0 (cap 7)
- Max drawdown: 0.00% (cap 25%, warn 12.5%)
- Equity floor: $10,122.66 > $7,500 — OK
- **All clear. HYPE/USD long open.**

## Rolling performance vs main BULL v0.4

| Window | v0.5 return | main return | Delta | BTC-hold | Result |
|--------|-------------|-------------|-------|----------|--------|
| 7d  | +1.23% (1 open HYPE) | ≈ +0.6% (XRP exit -0.65R; HYPE recovery) | +0.6% | ≈ −4.4% (BTC $77.6k→$74.1k May 24→31) | v0.5 ahead — HYPE position outperforming |
| 30d | +1.23% (unrealized) | +5.58% (main competition net) | −4.35% | −2.20% (BTC $75,750→$74,082 Apr 29→May 31) | MAIN AHEAD net; but v0.5 above BTC-hold by +3.43% |
| 90d | — | — | — | — | not yet 90 days live |

## Days live

- Spin-up: 2026-04-29
- As of last rebuild: **32 days**
- Promotion-eligible date: **2026-05-29 (reached)** — 0 closed trades in rolling 30d (need ≥10) → NOT promotion-eligible; 1 open position accumulating

## Notes

Tests whether tightening cluster cap from 2 to 1 (rule 6a) reduces cascade-event tail loss enough to justify foregone trend capture in cluster rallies. Single-rule parameter change vs v0.2.

### Routine #7 wake log

- **2026-05-12 22:00 PT** — past-24h replay window = 2026-05-11 16:00 UTC → 2026-05-12 16:00 UTC. Same entry-eval as v0.3 minus the vol-compression gate. At EOD-prior (positive 6/15) no pair passed rules 1+2+3 jointly. At OVERNIGHT positive 0/15 → 5a rejected all entries. MIDDAY had 6 candidates {BTC, SOL, XRP, DOGE, SUI, FARTCOIN} but variants honor main's no-midday-entry default. Result: 0 entries, 0 open positions. All kill switches clear at $10,000 equity.
- **2026-05-16 22:00 PT (this wake)** — past-24h replay window = 2026-05-15 10:00 UTC → 2026-05-16 10:00 UTC. Wakes evaluated: OVERNIGHT (2026-05-15 13:00 UTC), MIDDAY (2026-05-15 20:00 UTC, default-skip), EOD (2026-05-16 04:00 UTC). Broadly-red tape — all 15 pairs negative 24h; 05-15 13:00Z synchronized crash bar. Rule 5a (≥4/15 positive) rejected all entries at both eligible wakes (0/15 at EOD); cluster-cap 6a never reached. Result: 0 entries, 0 open positions. All kill switches clear at $10,000 equity.
- **2026-05-29 22:00 PT** — past-24h replay window 2026-05-29 05:00 UTC → 2026-05-30 05:00 UTC. Kraken MCP OK (BTC/USD $73,183 smoke test). Regime: **1/15** universe pairs positive 24h (HYPE +0.67%); median 24h change −1.07%; **SBD active** this wake (≤1/15 positive AND median ≤−1.0%). Wakes evaluated: OVERNIGHT (2026-05-29 13:00 UTC), MIDDAY (2026-05-29 20:00 UTC, default-skip), EOD (2026-05-30 04:00 UTC). Rule 5a (≥4/15 positive) rejected all entries at both eligible wakes (1/15 positive). Cluster-cap 6a never reached. 0 entries. No open positions — exit replay no-op. All kill switches clear at $10,000 synthetic equity. **30-day time threshold reached this wake.** 0 trades in rolling 30d window (need ≥10) → NOT promotion-eligible; variant continues in LAB.
- **2026-05-30 22:00 PT** — replay window 2026-05-30T05:00Z → 2026-05-31T05:00Z. Kraken MCP OK (BTC/USD $74,078 smoke test). **OVERNIGHT wake (13:00Z 2026-05-30):** Regime recovered from May 28/29 SBD — BTC +0.95% 24h, HYPE +8.44% 24h (62.76→68.06), TAO +1.12%, SOL +1.30%; estimated ≥12/15 pairs positive; rule 5a PASS, SBD CLEARED. Pair scan: BTC/TAO fail rule 3 (4H close < 4H 50-EMA, regime early recovery). HYPE: 1H close 68.06 > 20-EMA 66.01 ✓; RSI(14) ≈ 79.5 ≥ 55 ✓; 4H close 67.81 > 50-EMA proxy ~61.50 ✓; cluster-cap OK (HYPE not in cluster). **ENTRY: HYPE/USD LONG 77 units at 68.06, stop 66.13, target 75.80, ATR 0.967.** **EOD wake (04:00Z 2026-05-31):** 14/15 positive, median +0.47% (per main portfolio). Exit replay: HYPE min since entry 66.22 (16:00Z bar low) > stop 66.13 → not hit; high 69.88 < target 75.80; 20-EMA at EOD ~68.05, HYPE close 69.83 > EMA → no EMA exit. Position open. Entry scan: HYPE already open; no other pairs pass rule 3 per main analysis; no new entries. Kill switches all clear. Equity $10,122.66, net +1.23% unrealized.
