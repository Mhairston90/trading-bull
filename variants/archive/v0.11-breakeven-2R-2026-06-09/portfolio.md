# Variant v0.11-breakeven-2R — Synthetic Portfolio

> **Paper-paper account.** Synthetic $10K starting equity.
> **Category:** LAB hypothesis (breakeven stop-ratchet at 2R unrealized vs main's static stop)
> **Last rebuild:** 2026-06-09 interactive mcp-outage gap replay (user-directed; Kraken public REST bars 2026-05-31T05:00Z → 2026-06-09T22:00Z — full window recovered)

## Account

- Starting equity: **$10,000.00**
- Cash: **$10,017.71**
- Realized PnL: **+$17.71** (HYPE/USD +0.12R, closed 2026-05-31T11:00Z)
- Unrealized PnL: **$0.00** (no open positions)
- Position values (MTM): **$0.00**
- Current equity: **$10,017.71**
- Equity peak: **$10,122.66** (2026-05-31T05:00Z rebuild, HYPE MTM)
- Drawdown: **1.04%**

## Open positions

_(none — HYPE/USD closed 2026-05-31T11:00Z exit-ema-cross; breakeven ratchet never armed)_

Open positions: **0 / 4** (momentum cap inherited from v0.2 rule 6).

## Active kill-switch state

All clear. Book flat. Equity $10,017.71 > $7,500 floor; DD 1.04% < caps.

## Rolling performance vs main v0.4

| Window | v0.11 return | main (v0.4) return | Verdict |
|--------|--------------|---------------------|---------|
| 7d  | +1.23% (1 open HYPE, unrealized) | ≈ +0.6% | v0.11 ahead on unrealized basis |
| 30d | — | — | not yet 30 days live (earliest 2026-06-15) |

## Days live

- Spin-up: 2026-05-16
- As of last rebuild: **24 days**
- Promotion-eligible: 2026-06-15 (but SUBSUMED by main v0.4 — flagged for retirement at routine #4)

## Notes

Hypothesis variant targeting the profit-give-back lesson (2026-05-15, score 9). Adds a breakeven stop-ratchet: once a trade is up ≥2R, the stop moves to entry so a matured winner cannot round-trip into a loss (XRP 2026-05-14 archetype: ran ~+2.8R, exited −0.14R). Stop ratchets up only; no further trailing. Strictly risk-reducing vs v0.2. Created by routine #4 2026-05-16 to accrue paper-paper evidence while TradingView (needed for the 180d backtest behind a Ring-2 proposal) is unavailable. Sibling exit-logic variant: v0.10-exit-confirm.

### Routine #7 wake log

- **2026-05-29 22:00 PT (first sim wake since 05-16 spin-up)** — past-24h replay window 2026-05-29 05:00 UTC → 2026-05-30 05:00 UTC. Kraken MCP OK (BTC/USD $73,183). Regime: **1/15** pairs positive (HYPE +0.67%), median −1.07%; **SBD active**. Wakes evaluated: OVERNIGHT (13:00 UTC), MIDDAY (default-skip), EOD (04:00 UTC). Rule 5a (≥4/15 positive) rejected all entries at both eligible wakes (1/15 positive). 0 entries. No open positions — breakeven-ratchet exit had nothing to evaluate. All kill switches clear at $10,000 synthetic equity.
- **2026-05-30 22:00 PT** — replay window 2026-05-30T05:00Z → 2026-05-31T05:00Z. Kraken MCP OK (BTC/USD $74,078). **OVERNIGHT (13:00Z 2026-05-30):** Regime recovered — ~12/15 pairs positive, BTC +0.95%, HYPE +8.44%; rule 5a PASS, SBD CLEARED. HYPE passes rules 1-3 (close 68.06 > EMA 66.01; RSI 79.5 ≥ 55; 4H close 67.81 > 50-EMA ~61.50). **ENTRY: HYPE/USD long 77 @ 68.06, stop 66.13, target 75.80 (4R).** Breakeven ratchet: arms at HYPE ≥ 71.94 (entry + 2×ATR×2); max price since entry 69.88 < 71.94 → ratchet NOT armed. **EOD (04:00Z 2026-05-31):** Exit replay — HYPE min 66.22 > stop 66.13 (not hit); close 69.83 > EMA 68.05 (no EMA exit); target 75.80 not reached. No new entries. Kill switches all clear. Equity $10,122.66, net +1.23%. Ratchet still inactive.
- **2026-06-09 interactive (user-directed mcp-outage gap replay)** — 9 missed routine-07 wakes recovered from Kraken public REST bars (full window 2026-05-31T05:00Z → 2026-06-09T22:00Z, nothing lost). **Exit replay: HYPE/USD CLOSED 2026-05-31T11:00Z @ 68.29 exit-ema-cross (+0.12R, +$17.71)** — identical to v0.5 (baseline single-bar EMA exit). **Ratchet datum: the 2R level (71.92) was first reached 2026-05-31T23:00Z, 12 hours AFTER the EMA exit closed the trade — the ratchet never armed and produced no divergence vs baseline on this trade.** (Counterfactual note: had the position survived to 23:00Z, the ratchet would have armed and the 06-01→06-04 slide would have exited at breakeven 68.06 instead of riding to the 66.13 stop — the variant's thesis remains untested but plausible.) Entry scans at all 17 gap wakes: 0 entries (regime gate 06-01→06-06 + 06-09T13:00Z; no pair passed rules 1+2+3 at regime-OK wakes). Equity $10,017.71, book flat. Audit: `scripts/mcp_outage_replay_20260609.py`.
