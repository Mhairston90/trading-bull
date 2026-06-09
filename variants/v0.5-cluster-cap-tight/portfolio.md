# Variant v0.5-cluster-cap-tight — Synthetic Portfolio

> **Paper-paper account.** Synthetic $10K starting equity.
> **Last rebuild:** 2026-06-09 interactive mcp-outage gap replay (user-directed; Kraken public REST bars 2026-05-31T05:00Z → 2026-06-09T22:00Z — full window recovered, no data loss)

## Account

- Starting equity: **$10,000.00**
- Cash: **$10,017.71**
- Realized PnL (variant lifetime): **+$17.71** (HYPE/USD +0.12R, closed 2026-05-31T11:00Z)
- Unrealized PnL: **$0.00** (no open positions)
- Position values (MTM): **$0.00**
- Current equity (cash + positions MTM): **$10,017.71**
- Equity peak: **$10,122.66** (2026-05-31T05:00Z rebuild, HYPE MTM)
- Drawdown from peak: **1.04%**

## Open positions

_(none — HYPE/USD closed 2026-05-31T11:00Z exit-ema-cross)_

Portfolio risk-at-moment: **0.00%** (cap 4%).
Open positions: **0 / 4** (cluster slots 0/**1**).

## Active kill-switch state

- Daily realized: $0 today (HYPE close was 2026-05-31) — clear vs 5% cap
- Consecutive losing trading days: 0 (cap 7; the single closed trade was a win)
- Max drawdown: 1.04% (cap 25%, warn 12.5%)
- Equity floor: $10,017.71 > $7,500 — OK
- **All clear. Book flat.**

## Rolling performance vs main BULL v0.4

| Window | v0.5 return | main return | Delta | BTC-hold | Result |
|--------|-------------|-------------|-------|----------|--------|
| 7d  | +1.23% (1 open HYPE) | ≈ +0.6% (XRP exit -0.65R; HYPE recovery) | +0.6% | ≈ −4.4% (BTC $77.6k→$74.1k May 24→31) | v0.5 ahead — HYPE position outperforming |
| 30d | +1.23% (unrealized) | +5.58% (main competition net) | −4.35% | −2.20% (BTC $75,750→$74,082 Apr 29→May 31) | MAIN AHEAD net; but v0.5 above BTC-hold by +3.43% |
| 90d | — | — | — | — | not yet 90 days live |

## Days live

- Spin-up: 2026-04-29
- As of last rebuild: **41 days**
- Promotion-eligible date: **2026-05-29 (reached)** — 1 closed trade in rolling 30d (need ≥10) → NOT promotion-eligible

## Notes

Tests whether tightening cluster cap from 2 to 1 (rule 6a) reduces cascade-event tail loss enough to justify foregone trend capture in cluster rallies. Single-rule parameter change vs v0.2.

### Routine #7 wake log

- **2026-05-12 22:00 PT** — past-24h replay window = 2026-05-11 16:00 UTC → 2026-05-12 16:00 UTC. Same entry-eval as v0.3 minus the vol-compression gate. At EOD-prior (positive 6/15) no pair passed rules 1+2+3 jointly. At OVERNIGHT positive 0/15 → 5a rejected all entries. MIDDAY had 6 candidates {BTC, SOL, XRP, DOGE, SUI, FARTCOIN} but variants honor main's no-midday-entry default. Result: 0 entries, 0 open positions. All kill switches clear at $10,000 equity.
- **2026-05-16 22:00 PT (this wake)** — past-24h replay window = 2026-05-15 10:00 UTC → 2026-05-16 10:00 UTC. Wakes evaluated: OVERNIGHT (2026-05-15 13:00 UTC), MIDDAY (2026-05-15 20:00 UTC, default-skip), EOD (2026-05-16 04:00 UTC). Broadly-red tape — all 15 pairs negative 24h; 05-15 13:00Z synchronized crash bar. Rule 5a (≥4/15 positive) rejected all entries at both eligible wakes (0/15 at EOD); cluster-cap 6a never reached. Result: 0 entries, 0 open positions. All kill switches clear at $10,000 equity.
- **2026-05-29 22:00 PT** — past-24h replay window 2026-05-29 05:00 UTC → 2026-05-30 05:00 UTC. Kraken MCP OK (BTC/USD $73,183 smoke test). Regime: **1/15** universe pairs positive 24h (HYPE +0.67%); median 24h change −1.07%; **SBD active** this wake (≤1/15 positive AND median ≤−1.0%). Wakes evaluated: OVERNIGHT (2026-05-29 13:00 UTC), MIDDAY (2026-05-29 20:00 UTC, default-skip), EOD (2026-05-30 04:00 UTC). Rule 5a (≥4/15 positive) rejected all entries at both eligible wakes (1/15 positive). Cluster-cap 6a never reached. 0 entries. No open positions — exit replay no-op. All kill switches clear at $10,000 synthetic equity. **30-day time threshold reached this wake.** 0 trades in rolling 30d window (need ≥10) → NOT promotion-eligible; variant continues in LAB.
- **2026-05-30 22:00 PT** — replay window 2026-05-30T05:00Z → 2026-05-31T05:00Z. Kraken MCP OK (BTC/USD $74,078 smoke test). **OVERNIGHT wake (13:00Z 2026-05-30):** Regime recovered from May 28/29 SBD — BTC +0.95% 24h, HYPE +8.44% 24h (62.76→68.06), TAO +1.12%, SOL +1.30%; estimated ≥12/15 pairs positive; rule 5a PASS, SBD CLEARED. Pair scan: BTC/TAO fail rule 3 (4H close < 4H 50-EMA, regime early recovery). HYPE: 1H close 68.06 > 20-EMA 66.01 ✓; RSI(14) ≈ 79.5 ≥ 55 ✓; 4H close 67.81 > 50-EMA proxy ~61.50 ✓; cluster-cap OK (HYPE not in cluster). **ENTRY: HYPE/USD LONG 77 units at 68.06, stop 66.13, target 75.80, ATR 0.967.** **EOD wake (04:00Z 2026-05-31):** 14/15 positive, median +0.47% (per main portfolio). Exit replay: HYPE min since entry 66.22 (16:00Z bar low) > stop 66.13 → not hit; high 69.88 < target 75.80; 20-EMA at EOD ~68.05, HYPE close 69.83 > EMA → no EMA exit. Position open. Entry scan: HYPE already open; no other pairs pass rule 3 per main analysis; no new entries. Kill switches all clear. Equity $10,122.66, net +1.23% unrealized.
- **2026-06-09 interactive (user-directed mcp-outage gap replay)** — routine-07 missed 9 consecutive wakes (05-31 → 06-08 PT; Kraken MCP path broke 2026-06-02 when the user archived the old `Trading Strategy` folder). Full window 2026-05-31T05:00Z → 2026-06-09T22:00Z replayed from Kraken public REST 1H/4H bars (720-bar history covers the whole gap — nothing permanently lost, superseding the earlier "2-day unrecoverable" estimate). **Exit replay: HYPE/USD CLOSED 2026-05-31T11:00Z @ 68.29 exit-ema-cross (+0.12R, +$17.71)** — close 68.29 < EMA20 68.2922 (marginal, 3bp; logged in trade_log). Entry scans at all 17 gap wakes: regime gate 5a/SBD rejected 06-01 → 06-06 + 06-09T13:00Z (crash: median as low as −8.55% on 06-03, 0/15 positive 06-04→06-06); regime-OK wakes (06-04T04:00Z, 06-07 → 06-09T04:00Z) had **no pair passing rules 1+2+3 jointly** (post-crash: 4H closes below 4H 50-EMA universe-wide; closest call HYPE RSI 54.8 vs 55 floor at 06-04T04:00Z). **0 new entries.** Equity $10,017.71, book flat. Audit: `scripts/mcp_outage_replay_20260609.py` + cached bars.
