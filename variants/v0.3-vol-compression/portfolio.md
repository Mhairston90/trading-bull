# Variant v0.3-vol-compression — Synthetic Portfolio

> **Paper-paper account.** Synthetic $10K starting equity. Does NOT affect main BULL portfolio or any real broker.
> **Rebuilt each routine #7 wake** from this variant's `trade_log.md`.
> **Last rebuild:** 2026-05-30T05:00:00Z (routine-07 wake 2026-05-29 22:00 PT — no trades; see notes)

## Account

- Starting equity: **$10,000.00**
- Cash: **$10,000.00**
- Realized PnL (variant lifetime): **$0.00**
- Unrealized PnL: **$0.00** (no open positions)
- Position values (MTM): **$0.00**
- Current equity (cash + positions MTM): **$10,000.00**
- Equity peak: **$10,000.00** (set at spin-up 2026-04-29)
- Drawdown from peak: **0.00%**

## Open positions

(none — variant spun up today, awaiting first routine #7 simulation wake)

Portfolio risk-at-moment: **0.00%** (cap 4%).
Open positions: **0 / 8** (variant max-concurrent 4 → 0/4 used; cluster cap 0/2).

## Active kill-switch state

- Daily realized: **0.00%** (cap 5%)
- Daily realized + unrealized: **0.00%** (cap 5%)
- Consecutive losing trading days: 0 (cap 7)
- Max drawdown: 0.00% (cap 25%, warn 12.5%)
- Equity floor: $10,000 > $7,500 floor — OK
- **All clear. Variant authorized to trade paper-paper.**

## Rolling performance (vs main BULL v0.2)

| Window | v0.3 return | v0.2 main return | Delta | BTC-hold | Result |
|--------|-------------|------------------|-------|----------|--------|
| 7d  | 0.00% | — | — | −3.01% (BTC 7d) | v0.3 in cash; BTC fell 3.01% over 7d (May 22→29) |
| 30d | 0.00% | +6.63% (main since Apr 29) | −6.63% | −3.39% (BTC Apr 29→May 29: $75,750→$73,183) | MAIN AHEAD; 0 trades — NOT promotion-eligible (need ≥10 in 30d) |
| 90d | — | — | — | — | not yet 90 days live |

(Populated by routine #7 once windows close.)

## Days live

- Spin-up: 2026-04-29
- As of last rebuild: **30 days**
- Promotion-eligible date: **2026-05-29 (reached today)** — 0 trades in rolling 30d (need ≥10) → NOT promotion-eligible yet

## Notes

This variant exists to test whether a 0.5× ATR-compression entry gate improves net return / profit factor over main v0.2. See `README.md` and `strategy.md` in this directory for full hypothesis.

The variant runs entirely paper-paper. Its trades have NO effect on the real BULL portfolio in `memory/portfolio.md`. The leaderboard at `memory/leaderboard.md` shows side-by-side performance.

### Routine #7 wake log

- **2026-05-12 22:00 PT** — past-24h replay window = 2026-05-11 16:00 UTC → 2026-05-12 16:00 UTC. Wakes evaluated: MIDDAY (2026-05-11 20:00 UTC, default-skip), EOD-prior (2026-05-12 04:00 UTC), OVERNIGHT (2026-05-12 13:00 UTC). At EOD-prior: positive-24h count 6/15 (regime 5a OK) but no pair passed rules 1+2+3 jointly. At OVERNIGHT: positive-24h count **0/15** → rule 5a rejected all entries. Result: 0 entries, 0 open positions to evaluate exits. All kill switches clear at $10,000 equity.
- **2026-05-16 22:00 PT (this wake)** — past-24h replay window = 2026-05-15 10:00 UTC → 2026-05-16 10:00 UTC (Kraken's latest closed 1H bar 05-16 10:00Z; routine #7 last ran 05-12, but routine spec scopes replay to trailing 24h). Wakes evaluated: OVERNIGHT (2026-05-15 13:00 UTC), MIDDAY (2026-05-15 20:00 UTC, default-skip), EOD (2026-05-16 04:00 UTC). Broadly-red tape: all 15 universe pairs negative on 24h change; the 05-15 13:00Z bar was a synchronized crash bar across the universe. Rule 5a (≥4/15 positive) **rejected all entries at both eligible wakes** (positive-24h count well below 4; 0/15 at EOD). Vol-compression gate 5c not reached. Result: 0 entries, 0 open positions to evaluate exits. All kill switches clear at $10,000 equity.
- **2026-05-29 22:00 PT** — past-24h replay window 2026-05-29 05:00 UTC → 2026-05-30 05:00 UTC. Kraken MCP OK (BTC/USD $73,183 smoke test). Regime: **1/15** universe pairs positive 24h (HYPE +0.67%); median 24h change −1.07%; **SBD active** this wake (≤1/15 positive AND median ≤−1.0%). Wakes evaluated: OVERNIGHT (2026-05-29 13:00 UTC), MIDDAY (2026-05-29 20:00 UTC, default-skip), EOD (2026-05-30 04:00 UTC). Rule 5a (≥4/15 positive) rejected all entries at both eligible wakes (1/15 positive). Vol-compression gate 5c not reached. 0 entries. No open positions — exit replay no-op. All kill switches clear at $10,000 synthetic equity. **30-day time threshold reached this wake.** 0 trades in rolling 30d window (need ≥10) → NOT promotion-eligible; variant continues in LAB.
