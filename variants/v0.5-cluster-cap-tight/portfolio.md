# Variant v0.5-cluster-cap-tight — Synthetic Portfolio

> **Paper-paper account.** Synthetic $10K starting equity.
> **Last rebuild:** 2026-06-25T19:19Z (routine-07 wake 2026-06-25 PT — off-cron 12:19 PT; 0 entries, 0 trades; SBD ACTIVE 5a FAIL; 11 closed trades lifetime; **PROMOTION CANDIDATE**)

## Account

- Starting equity: **$10,000.00**
- Cash: **$10,943.13** (flat)
- Realized PnL (variant lifetime): **+$942.21** (HYPE +$17.71 +0.12R; void $0; TAO +$644.90 +4.29R; BTC OVERNIGHT −$18.54 −0.26R; BTC EOD Jun14 −$6.17 −0.09R; HYPE Jun14 −$86.26 −0.54R; BTC Jun15 +$120.20 +0.76R; HYPE Jun16 +$142.28 +0.89R; HYPE Jun17 −$63.72 −0.39R; SOL Jun20 +$358.45 +2.22R; BTC Jun22 −$166.65 −1.00R)
- Unrealized PnL: **$0.00** (no open positions)
- Position values (MTM): **$0.00**
- Current equity: **$10,943.13**
- Equity peak: **$11,109.78** (set 2026-06-21T21:00Z at SOL close +2.22R)
- Drawdown from peak: **1.50%** ($11,109.78 → $10,943.13 after BTC Jun22 stop-out)

## Open positions

_None._

Portfolio risk-at-moment: **0.00%** (cap 4%, full headroom).
Open positions: **0 / 4** (cluster 0/1).

## Active kill-switch state

- Daily realized 2026-06-25 PT: $0.00 (last trade was BTC Jun22) — clear vs 5% cap
- Consecutive losing trading days: 1 (BTC stop-out Jun22; cap 7) — clear
- Max drawdown: 1.50% from peak $11,109.78 (cap 25%, warn 12.5%) — clear
- Equity floor: $10,943.13 > $7,500 — OK
- Regime gate: 5a FAIL / SBD ACTIVE at OVERNIGHT 2026-06-24T13:00Z → 0 entries this wake
- **All clear. No open positions. 11 closed trades lifetime (10 effective; 1 void $0).**

## Promotion assessment — **ELIGIBLE**

| Criterion | Required | v0.5 | Status |
|-----------|----------|------|--------|
| Days live | ≥ 30 | 56 days | ✓ |
| Closed trades (rolling 30d) | ≥ 10 | 10 effective closes (all in last 20d) | ✓ |
| Net return vs main | > main | +9.43% vs main +4.14% | ✓ +5.29pp |
| Max DD | < main DD + 25% | 1.50% vs main 4.25% | ✓ |
| Profit factor | > 1.0 | ~3.76 ($1,283 wins / $341 losses) | ✓ |

**→ Route to routine-04 Saturday memo for Ring-2 promotion proposal.**

## Rolling performance vs main BULL v0.4

| Window | v0.5 return | main return | Delta | BTC-hold | Result |
|--------|-------------|-------------|-------|----------|--------|
| 30d | +9.43% (all trades in last 20d) | +4.14% | +5.29% | −20.5% (BTC $75,750→$60,219) | v0.5 WELL AHEAD |
| 90d | — | — | — | — | not yet computable |

## Days live

- Spin-up: 2026-04-29
- As of last rebuild: **57 days**
- **Promotion-eligible: YES** — gate opened; route to routine-04 for proposal draft.

## Notes

Tests whether tightening cluster cap from 2 to 1 (rule 6a) reduces cascade-event tail loss enough to justify foregone trend capture in cluster rallies. Gap replay result: cluster cap didn't severely restrict — v0.5 was able to enter 7 new positions consecutively (HYPE×3, BTC×2, SOL, BTC) because the 1-slot cluster filled and emptied rapidly. The biggest single-trade win was SOL +2.22R/+$358.45 on June 20–21, contributing 38% of the total replay PnL.

### Routine #7 wake log

- **2026-05-12 22:00 PT** — 0 entries (5a FAIL at OVERNIGHT 0/15 positive). Equity $10,000. Days live: **13**.
- **2026-05-16 22:00 PT (this wake)** — 0 entries (5a FAIL at both wakes; crash tape −0/15). Equity $10,000. Days live: **17**.
- **2026-05-29 22:00 PT** — 0 entries (SBD active 1/15 positive; 5a FAIL). 30-day threshold reached. 0 trades in rolling 30d. NOT promotion-eligible. Equity $10,000. Days live: **30**.
- **2026-05-30 22:00 PT** — OVERNIGHT HYPE OPEN @ 68.06 (cluster 0/1 ✓). EOD: stop not hit; EMA not triggered; target not reached. Equity MTM $10,122.66. Days live: **31**.
- **2026-06-09 interactive (user-directed mcp-outage gap replay)** — 9 missed wakes recovered. HYPE CLOSE 2026-05-31T11:00Z @ 68.29 +0.12R +$17.71 (exit-ema-cross). 17 gap-wake entry scans: 0 entries (5a/SBD rejection 06-01→06-06 + 06-09T13:00Z; no pair passed R1+R2+R3 at regime-OK wakes). BTC EOD 06-12T04:00Z OPEN (correction run). Equity $10,017.71. Days live: **41**.
- **CORRECTION NOTE (2026-06-11 22:00 PT):** BTC EOD 06-12T04:00Z entry was based on short-warm-up EMA. Converged 720-bar 4H 50-EMA = $63,682.6 → BTC fails rule 3 by $252. BTC OPEN voided ($0 PnL). Equity $10,017.71. Days live: **42**.
- **2026-06-12 22:00 PT (routine-07)** — replay window 2026-06-12T06:45Z → 2026-06-13T05:00Z. OVERNIGHT 13:00Z: BTC R2 FAIL (RSI ~52). EOD 2026-06-13T04:00Z: TAO sole PASS. ENTRY: TAO LONG 32.22 @ 217.286. Days live: **45**.
- **2026-06-13 22:00 PT (routine-07)** — replay window 2026-06-13T05:08Z → 2026-06-14T05:00Z. EXIT TAO +4.29R/+$644.90. OVERNIGHT BTC OPEN/CLOSE −0.26R/−$18.54. EOD BTC OPEN @ 64320.2. Equity $10,644.07, DD 0.17%. Days live: **46**.
- **2026-06-24 PT (routine-07 — gap replay via routine07_replay_20260623.py; fired ~09:35 PT off-schedule)** — Replay window: **2026-06-14T05:00Z → 2026-06-24T13:00Z** (10.5 days; fully recovered via Kraken REST 30d history). **7 new closes, 6 new opens across 12 wakes evaluated. New peak $11,109.78 set at SOL close Jun21.** Trade sequence: BTC EOD Jun14 CLOSE −0.09R/−$6.17 (12:00Z bar 1-bar EMA exit); HYPE OVERNIGHT Jun14 OPEN/CLOSE −0.54R/−$86.26 (whipsaw 2h); BTC EOD Jun15 OPEN/CLOSE +0.76R/+$120.20 (held ~18h); HYPE EOD Jun16 OPEN/CLOSE +0.89R/+$142.28 (held ~15h); HYPE EOD Jun17 OPEN/CLOSE −0.39R/−$63.72 (whipsaw 2h); SOL EOD Jun20 OPEN/CLOSE +2.22R/+$358.45 (held ~41h → BEST TRADE in replay); BTC OVERNIGHT Jun22 OPEN/CLOSE −1.00R/−$166.65 (stop hit ~2h after entry). Net new realized: +$298.13. Total realized +$942.21. **OVERNIGHT 2026-06-24T13:00Z:** 0/15 positive, SBD ACTIVE → 5a FAIL → 0 entries. **EOD 2026-06-24T04:00Z (elapsed):** 1/15 positive, SBD ACTIVE → 5a FAIL. **PROMOTION CANDIDATE: 56 days live, 10 effective closes, +9.43% return, DD 1.50%, PF ~3.76 — all gates pass.** All kill switches clear. Days live: **56**.
- **2026-06-25 PT (routine-07, 2026-06-25T19:19Z — off-cron 12:19 PT)** — Watchdog ALL CLEAR. Kraken MCP OK ($59,407 BTC). Replay window: 2026-06-24T16:35Z → 2026-06-25T19:19Z (~26.7h). Wakes evaluated: **EOD 2026-06-25T04:00Z**: 0/15 positive, SBD ACTIVE, 5a FAIL → 0 entries. **OVERNIGHT 2026-06-25T13:00Z**: BTC crashed 61,146→58,218 −4.9%, SBD 5th consecutive wake, 0/15 positive, 5a FAIL → 0 entries. Book flat → no exit triggers. Kill switches all clear (equity $10,943.13 unchanged). **PROMOTION CANDIDATE status unchanged** (57d live, 10 effective closes, +9.43%, DD 1.50%). Days live: **57**.
