# Variant v0.10-exit-confirm — Synthetic Portfolio

> **Paper-paper account.** Synthetic $10K starting equity.
> **Category:** LAB hypothesis (exit rule 1: 2-bar EMA-cross confirmation vs main's 1-bar)
> **Last rebuild:** 2026-05-31T05:00:00Z (routine-07 wake 2026-05-30 22:00 PT — 1 OPEN; see notes)

## Account

- Starting equity: **$10,000.00**
- Cash: **$4,745.75**
- Realized PnL: **$0.00**
- Unrealized PnL: **+$136.29** (HYPE/USD long 77 × (69.83 − 68.06))
- Position values (MTM): **$5,376.91** (77 × $69.83)
- Current equity: **$10,122.66**
- Equity peak: **$10,122.66** (set this wake)
- Drawdown: **0.00%**

## Open positions

| Pair | Side | Size | Entry | Stop | Target | Entry time | ATR at entry | Unrealized R |
|------|------|------|-------|------|--------|------------|--------------|-------------|
| HYPE/USD | long | 77 | 68.06 | 66.13 | 75.80 | 2026-05-30T13:00Z | 0.967 | +0.92R |

Open positions: **1 / 4** (momentum cap inherited from v0.2 rule 6).

## Active kill-switch state

Daily realized: 0.00% (no closed positions); unrealized: +1.23% (positive). All clear. HYPE/USD long open. Equity $10,122.66 > $7,500 floor.

## Rolling performance vs main v0.4

| Window | v0.10 return | main (v0.4) return | Verdict |
|--------|--------------|---------------------|---------|
| 7d  | +1.23% (1 open HYPE, unrealized) | ≈ +0.6% | v0.10 ahead on unrealized basis |
| 30d | — | — | not yet 30 days live (earliest 2026-06-15) |

## Days live

- Spin-up: 2026-05-16
- As of last rebuild: **15 days**
- Promotion-eligible: 2026-06-15

## Notes

Hypothesis variant targeting the commission-drag lesson (score 8). Only the EMA-cross exit path differs from main: 2 consecutive 1H closes below the 20-EMA required (vs 1). Stop and 4R take-profit unchanged, so divergence vs main occurs only on trades that approach the EMA without first hitting stop/target. Created by routine #4 2026-05-16 to accrue paper-paper evidence while TradingView (needed for the 180d backtest behind a Ring-2 proposal) is unavailable.

### Routine #7 wake log

- **2026-05-16 22:00 PT (first sim wake; spun up earlier today)** — past-24h replay window = 2026-05-15 10:00 UTC → 2026-05-16 10:00 UTC. Wakes: OVERNIGHT (05-15 13:00Z), MIDDAY (05-15 20:00Z, default-skip), EOD (05-16 04:00Z). Inherits v0.2 entry rules incl. regime gate 5a (≥4/15 positive 24h). Broadly-red tape — all 15 pairs negative 24h, 0/15 positive at EOD; 5a rejected all entries at both eligible wakes. 0 entries, 0 open positions, so the modified 2-bar EMA-cross exit had nothing to evaluate (no divergence vs main yet). All kill switches clear at $10,000 equity.
- **2026-05-29 22:00 PT** — past-24h replay window 2026-05-29 05:00 UTC → 2026-05-30 05:00 UTC. Kraken MCP OK (BTC/USD $73,183). Regime: **1/15** pairs positive (HYPE +0.67%), median −1.07%; **SBD active**. Wakes evaluated: OVERNIGHT (13:00 UTC), MIDDAY (default-skip), EOD (04:00 UTC). Rule 5a (≥4/15 positive) rejected all entries at both eligible wakes (1/15 positive). 0 entries. No open positions — 2-bar EMA-cross exit had nothing to evaluate. All kill switches clear at $10,000 synthetic equity.
- **2026-05-30 22:00 PT** — replay window 2026-05-30T05:00Z → 2026-05-31T05:00Z. Kraken MCP OK (BTC/USD $74,078). **OVERNIGHT (13:00Z 2026-05-30):** Regime recovered — ~12/15 pairs positive, BTC +0.95%, HYPE +8.44%; rule 5a PASS, SBD CLEARED. HYPE passes rules 1-3 (close 68.06 > EMA 66.01; RSI 79.5 ≥ 55; 4H close 67.81 > 50-EMA ~61.50). **ENTRY: HYPE/USD long 77 @ 68.06, stop 66.13, target 75.80.** **EOD (04:00Z 2026-05-31):** Exit replay — HYPE min 66.22 > stop 66.13 (not hit); close 69.83 > EMA 68.05 (no EMA exit); 4R target 75.80 not reached. No new entries (HYPE already open; no other pairs pass rule 3; fresh HYPE entry blocked by RSI ≈53 per main analysis). Divergence vs main: v0.10 requires 2-bar EMA confirmation on exit — not yet testable (no closed positions). Kill switches all clear. Equity $10,122.66, net +1.23%.
