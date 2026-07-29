# Variant v0.12-sbd-exit — Synthetic Portfolio

> **Paper-paper account.** Synthetic $10K starting equity.
> **Category:** LAB hypothesis / instrumented twin.
> **Last rebuild:** 2026-07-29T17:52:00Z bounded routine-07 recovery replay. The missing
> 2026-06-27 SOL OPEN was restored to the source-of-truth log and its same-day
> EMA20 exit was recovered. The documented seven-day replay window
> (2026-07-22T17:00Z onward) was then simulated deterministically.
>
> **LEADERBOARD-SOURCED — FORWARD PAPER-PAPER ONLY.**

## Account

- Starting equity: **$10,000.00**
- Cash: **$10,909.04**
- Realized PnL (variant lifetime): **+$909.04**
- Unrealized PnL: **$0.00**
- Current equity: **$10,909.04**
- Equity peak: **$11,101.09**
- Drawdown from peak: **1.73%**
- Net return: **+9.09%**

## Open positions

(none)

Portfolio risk-at-moment: **0.00%**.
Open positions: **0 / 4** (BTC cluster 0/2).

## Recovery audit

- Restored omitted SOL OPEN and recovered SOL CLOSE: **-$144.72 / -0.89R**.
- Seven-day replay: ETH **+$387.62**, BTC **-$65.80**, ETH **-$126.25**.
- Older unavailable interval was not invented; it is explicitly outside routine-07's
  seven-day cap.
- Current regime: **3/15 positive, median -1.56%**;
  SBD CLEAR.
- Closed trades represented in the log after recovery: **20**.

## Active kill-switch state

- Daily loss cap: CLEAR
- Consecutive-loss cap: CLEAR
- Max drawdown: **1.73%**
- Equity floor: **$10,909.04 > $7,500**
- **All variant kill switches CLEAR.**
