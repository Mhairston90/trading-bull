# Variant v0.14-recovery-trend — Synthetic Portfolio

> **Paper-paper account.** Synthetic $10K starting equity.
> **Category:** LAB hypothesis (4H 20-EMA trend filter).
> **Last rebuild:** 2026-07-29T17:52:00Z bounded routine-07 recovery replay. The missing
> 2026-06-27 SOL OPEN and same-day exit were restored before replaying the
> documented seven-day recoverable window.

## Account

- Starting equity: **$10,000.00**
- Cash: **$3,959.00**
- Realized PnL (variant lifetime): **+$1,205.06**
- Unrealized PnL: **-$3.33**
- Position value: **$7,242.74**
- Current equity: **$11,201.74**
- Equity peak: **$11,402.33**
- Drawdown from peak: **1.76%**
- Net return: **+12.02%**

## Open positions

| Pair | Side | Size | Entry | Stop | Target | Entry time (UTC) | Last | MTM | Unrealized R |
|---|---|---:|---:|---:|---:|---|---:|---:|---:|
| ADA/USD | long | 44389.61800667 | 0.163238 | 0.15945162 | 0.17838353 | 2026-07-29T04:00:00Z | 0.163163 | $7,242.74 | -0.02R |

Portfolio risk-at-moment: **1.50%**.
Open positions: **1 / 4** (BTC cluster 0/2).

## Recovery audit

- Restored omitted SOL OPEN and recovered SOL CLOSE: **-$148.64 / -0.89R**.
- Seven-day closed replay: ETH **+$398.14**, BTC **-$67.59**, ETH **-$129.68**.
- Current paper position: ADA/USD opened 2026-07-29T04:00Z under the 4H 20-EMA rule.
- Older unavailable interval was not invented; it is explicitly outside routine-07's
  seven-day cap.
- Current regime: **3/15 positive, median -1.56%**;
  SBD CLEAR.
- Closed trades represented in the log after recovery: **13**.

## Active kill-switch state

- Daily loss cap: CLEAR
- Consecutive-loss cap: CLEAR
- Max drawdown: **1.76%**
- Equity floor: **$11,201.74 > $7,500**
- Portfolio risk: **1.50% < 4%**
- **All variant kill switches CLEAR.**
