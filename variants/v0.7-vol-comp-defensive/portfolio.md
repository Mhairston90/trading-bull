# Variant v0.7-vol-comp-defensive — Synthetic Portfolio

> **Paper-paper account.** Synthetic $10K starting equity.
> **Category:** LAB-SWEEP (parameter sweep of v0.3, threshold 0.5 → 0.7)
> **Last rebuild:** 2026-06-12T05:00Z (routine-07 wake 2026-06-11 22:00 PT — 0 trades; see notes)

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

Open positions: **0 / 4**. Cluster: 0/2.

## Active kill-switch state

All clear at $10,000 equity.

## Rolling performance vs main v0.2 AND parent v0.3

| Window | v0.7 return | v0.3 (parent) return | v0.2 (main) return | Verdict |
|--------|-------------|----------------------|---------------------|---------|
| 7d  | — | — | — | not yet 7 days live |
| 30d | — | — | — | not yet 30 days live (earliest 2026-06-11) |

## Days live

- Spin-up: 2026-05-12
- As of last rebuild: **31 days**
- Promotion-eligible: **2026-06-11 (reached)** — 0 trades in rolling 30d (need ≥10) → NOT promotion-eligible

## Notes

Parameter sweep — `vol_compression_threshold = 0.7` (vs v0.3's 0.5). Tests whether v0.3 is under-filtering. May produce few trades if regime stays in mild compression.

### Routine #7 wake log

- **2026-05-16 22:00 PT (first sim wake since 05-12 spin-up)** — past-24h replay window = 2026-05-15 10:00 UTC → 2026-05-16 10:00 UTC. Wakes: OVERNIGHT (05-15 13:00Z), MIDDAY (05-15 20:00Z, default-skip), EOD (05-16 04:00Z). Inherits v0.3 rules incl. regime gate 5a. Broadly-red tape — all 15 pairs negative 24h, 0/15 positive at EOD; 5a rejected all entries at both eligible wakes before the stricter 0.7 vol-comp gate was reached. 0 entries, 0 open positions. All kill switches clear at $10,000 equity.
- **2026-05-29 22:00 PT** — past-24h replay window 2026-05-29 05:00 UTC → 2026-05-30 05:00 UTC. Kraken MCP OK (BTC/USD $73,183). Regime: **1/15** pairs positive 24h (HYPE +0.67%), median −1.07%; **SBD active**. Wakes evaluated: OVERNIGHT (2026-05-29 13:00 UTC), MIDDAY (default-skip), EOD (2026-05-30 04:00 UTC). Rule 5a (≥4/15 positive) rejected all entries at both eligible wakes (1/15 positive) before 0.7× vol-comp gate reached. 0 entries. No open positions. All kill switches clear at $10,000 synthetic equity.
- **2026-05-30 22:00 PT** — replay window 2026-05-30T05:00Z → 2026-05-31T05:00Z. Kraken MCP OK. Regime at OVERNIGHT: ~12/15 positive; rule 5a PASS. HYPE passes rules 1-3 but **vol-comp gate 5c (threshold 0.7) BLOCKED**: current HYPE ATR ≈ 0.97; 0.5×30d-mean would need to be > 0.97 (0.7× threshold makes this stricter than v0.3). HYPE in active rally — compression not present. EOD: same analysis. 0 entries. Kill switches clear at $10,000. Days live: **19**.
- **2026-06-10 22:00 PT** *(partial-run — header/days updated but wake-log not written; retroactively captured here)* — 7-day cap replay 2026-06-04T05:00Z → 2026-06-11T05:00Z (same basis as parent v0.3). Crash wakes: SBD active → 5a FAIL. Recovery wakes 06-07→06-09: 5a PASS but vol-comp gate 5c (0.7× threshold) BLOCKED — crash-spiked ATR ~3-5× 30d-mean; 0.7× gate blocks more aggressively than v0.3's 0.5×. Post-recovery 06-09T13:00Z → tonight: SBD active → 5a FAIL. **0 entries.** Book flat. Kill switches clear at $10,000. **30-day promotion threshold reached this wake (day 30 from 2026-05-12 spin-up). 0 trades lifetime → NOT promotion-eligible; variant continues in LAB.**
- **2026-06-11 22:00 PT** — replay window 2026-06-11T05:00Z → 2026-06-12T05:00Z (24h). Kraken MCP OK (BTC/USD $62,563; 4H OHLCV unavailable). **OVERNIGHT 2026-06-11T13:00Z:** SBD active → 5a FAIL → 0 entries. **EOD 2026-06-12T04:00Z:** 5a PASS, SBD CLEARED (15/15 positive, median +2.72%). Entry scan: all 15 pairs fail rule 3 (4H close < 4H 50-EMA; same universal fail as parent v0.3 — 50-EMA ~$63,589 BTC vs close $62,590). Vol-comp gate 5c (0.7× threshold, stricter): ATR elevated post-crash bounce — blocked harder than v0.3's 0.5× gate. **0 entries.** Exit replay no-op (book flat). Kill switches all clear at $10,000. Days live: **31**.
