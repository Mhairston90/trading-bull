# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md`; the log remains the source of truth.
> **Last rebuild:** 2026-10-01T13:20Z routine-01-overnight (PT 2026-10-01 06:20) — on-schedule fire. **ADA stop-out intrabar at 08:00Z closed book flat.** Regime crystallized 14/15 +1.30% → 1/15 -2.74% SBD-ACTIVE between entry (7h ago) and this wake — 4th instance of same-session-stop-after-regime-crystallization pattern.

## Account

- Starting equity: **$10,000.00**
- Cash: **$9,884.51** (prior $4,264.21 + ADA exit proceeds net $5,620.30)
- Realized PnL (since inception): **−$115.51** (prior +$68.04 − ADA stop $183.55)
- Unrealized PnL: **$0.00** (book flat)
- Current equity: **$9,884.51** (cash-only, book flat)
- Equity peak: **$11,068.89** (unchanged)
- Drawdown from peak: **10.70%** (widened from 9.37% EOD by ADA stop-out)
- Since-inception return: **−1.15%**

## Open positions

| Pair | Side | Size | Entry fill | Stop (2×ATR) | Target (4R) | Current MTM | Unrealized $ | Unrealized R |
|------|------|------|-----------|--------------|-------------|-------------|--------------|--------------|
| — | — | — | — | — | — | — | — | — |

Portfolio risk-at-moment: **0.00%** of equity (book flat).
Open positions: **0 / 8** (strategy cap 0/4; BTC-cluster 0/2).

## Day summary — PT 2026-10-01 Thu trading day (in-progress)

- **Day PnL (realized)**: **−$183.55 / −1.82%** (ADA stop-out, 08:00Z = 01:00 PT).
- **Trades opened**: **0** (ADA 07:00Z entry was logged under PT 10-01 EOD label).
- **Trades closed**: **1** (ADA/USD 08:00Z intrabar stop).
- **Win rate today (closed only)**: **0/1** (0%).

## Rolling benchmark (marked to live-ticker 2026-10-01T13:12Z)

- **BTC-hold 30d**: BTC live $83,556 vs ~$79,500 09-01 baseline → **~+5.1%** (pulled back further overnight from EOD $84,018).
- **BTC-hold 7d**: ~+9.1%.
- **BULL 30d** (equity $9,884.51 vs ~$10,440 09-01 baseline): **~−5.33%** (widened from EOD's −3.91% due to ADA stop).
- **BULL 7d**: **~−5.72%**.
- **BULL vs BTC-hold 30d**: **~−10.4pp behind** (widened from EOD's −9.6pp — BTC pullback modest, BULL stop was larger).
- **BULL vs BTC-hold 7d**: **~−14.8pp behind**.
- **90d benchmark**: not-yet-computable (post-outage cross-window; cumulative from pre-outage not comparable).

## ADA stop-out mechanics — 2026-10-01T08:00:00Z

- **Entry** (prior wake routine-03-eod 07:13Z): 22,838 ADA @ $0.253472 fill, stop $0.246859, target $0.279923, risk $151.03 (1.5% equity).
- **Stop trigger**: 08:00Z 1H bar low $0.2452 pierced stop $0.246859 by $0.0017 (0.69% below stop).
- **Fill**: $0.246736 (= $0.246859 × 0.9995 slippage).
- **Gross PnL**: (0.246736 − 0.253472) × 22,838 = −$153.85.
- **Commissions**: open $15.05 + close $14.65 = $29.70.
- **Net PnL**: **−$183.55 / −1.02R**.
- **Hold time**: 1 bar (1 hour).
- **Peak unrealized during hold**: never positive — 07:00Z entry bar close was $0.253345, next bar (08:00Z) opened $0.248373 (-1.9% gap down) and ran to low $0.2452 pierce.

## Regime crystallization — 4th instance of same-session-stop-after-crystallization pattern

**Entry wake** (10-01T07:13Z EOD): 14/15 positive 24h, median **+1.30%** — strongest regime read in weeks, SBD CLEAR by wide margin.
**This wake** (10-01T13:12Z overnight, 6h later): **1/15** positive, median **−2.74%** — 5a FAIL + SBD ACTIVE.
**Delta**: 13 pairs flipped from positive to negative in 6 hours; median moved -4.04pp. This is the **largest regime whiplash of the 4 pattern instances by raw count**.

**Pattern instances** (companion lesson being added this wake):
| Date | Entry wake regime | Stop wake regime | Pair | Entry→stop time | Net R |
|---|---|---|---|---|---|
| 2026-06-17 | 12/15 +1.17% | 1/15 −3.37% | SOL | 1h | −1.28R |
| 2026-07-07 | 12/15 +1.95% | 1/15 −2.94% | HYPE | 6h | −1.02R |
| 2026-09-23 | 4/15 −0.86% | 1/15 −6.18% | NEAR | 1h | −1.01R |
| **2026-10-01** | **14/15 +1.30%** | **1/15 −2.74%** | **ADA** | **1h** | **−1.02R** |

Four instances in ~15 weeks (~1 per 4 weeks cadence). Routes to Sat 10-03 routine-04-harness W25R memo as **P-W25R-SAMESESSION-STOP-GATE** (upgraded from the 09-23 NEAR pattern-of-3 to pattern-of-4).

## Active kill-switch state (routine-01-overnight 2026-10-01T13:20Z / PT 2026-10-01 06:20)

- **Daily loss cap (PT 10-01 trading day)**: **−1.82% realized** (ADA stop). **CLEAR** (<5% cap; 3.18pp headroom).
- **Consecutive-loss cap**: **5 losses** (NEAR 09-23, ADA 09-26, SOL 09-27 scratch, SOL 09-30, ADA 10-01). Streak = **5 of 7**. **CLEAR** (2-loss headroom to 7-day full-pause).
- **Max drawdown: 10.70%** from peak $11,068.89 (widened from 9.37% EOD by ADA stop). **CLEAR** (25% cap, **1.80pp headroom to 12.5% warn** — tightening).
- **Equity floor: $9,884.51 > $7,500** (+$2,384.51). **CLEAR**.
- **Exposure: 0.00% / 4%** used. CLEAR (book flat).
- **Cluster cap: 0/2 BTC-cluster**. CLEAR.
- **Universe/liquidity**: book flat, no exposure to check.
- **5b cooldown state**: ADA blocked until **2026-10-02T08:00Z** (24h from this stop-out); SOL blocked until **2026-10-01T14:00Z** (expires in ~40min). NEAR expired. 12 other pairs CLEAR.
- **Regime 5a**: **FAIL 1/15 −2.74% median → SBD ACTIVE**. No new entries this wake regardless.
- **MCP availability**: Kraken ticker + OHLCV + indicators.py healthy; Telegram script healthy; watchdog healthy.
- **All Ring 3 kill switches CLEAR.**

## Ops notes

- **Regime whiplash severity**: 14/15 +1.30% → 1/15 −2.74% in 6h is the largest intraday regime flip on record for BULL. The 09-29 EOD had a similar magnitude flip (3/15 → 12/15) but in the *opposite* (bullish) direction. These rapid flips are becoming the dominant regime behavior — of 7 wakes 09-23 through 10-01, 5 showed >8-pair regime flips vs prior wake. v0.4's point-in-time 5a snapshot cannot catch these transitions.
- **ADA back-to-back stop-outs**: 2nd ADA stop-out in 5 days (09-26 at −0.29R scratch, 10-01 at −1.02R full-R). Entry archetype was similar both times (rule-8-cashfit or rule-8-winner on mid-range RSI). The 09-26 ADA was a 2-bar W22-G exit; 10-01 ADA was a 1-bar hard-stop. Different exit mechanisms, same outcome: ADA entries have failed 2/2 recent attempts.
- **Rule-8-cashfit pattern-of-4**: this is the 4th rule-8-cashfit entry (07-10 BTC +0.23R-loss, 09-30 SOL −1.00R, 10-01 ADA −1.02R, counting ADA as the 3rd cashfit — plus the informal rule-8-fallback 06-17 SOL). Pattern-of-4 confirms the cashfit-fallback behavior is now operationally dominant. **P-W27-CASHFIT** proposal still pending user `[Y/N]` per lesson 2026-06-17.
- **W22-H breakeven ratchet pattern-of-4**: still slated for Sat 10-03 routine-04-harness W25R memo as **P-W25R-RATCHET-TIGHTEN** (lesson 09-27).
- **New P-W25R-SAMESESSION-STOP-GATE escalation**: this wake adds 4th instance (ADA 10-01) to the SBD-crystallization-within-15h pattern first identified by 09-23 NEAR lesson. The 09-23 lesson explicitly routed to Sat 09-26 memo (never fired due to Sat routine-04 not running); now routes to Sat 10-03 with pattern-of-4 evidence.
- **Drawdown trajectory**: 10.70% is 1.80pp from 12.5% warn threshold. Two consecutive stop-outs = 1.33pp + 0.33pp = 1.66pp drawdown-growth per stop. One more full-R stop = ~12.0% DD; two more = ~13.3% DD (into warn). This is the first time DD has approached warn since the 09-20 scheduler-outage-recovery wake.
- **Watchdog findings (8, unchanged)**: routine-06/07 heartbeat dead (A×2), dirty-tree 4 untracked files (C), stale-MTM 5 variant portfolios (D). Known-structural, Telegram-alerted.

## Notes for next wake

- **Routine 02 midday** fires next ~20:00Z 10-01 = 13:00 PT Thu. Book flat; no positions to MTM. Entry scan under SBD-ACTIVE = reject all new entries per rule 5a-SBD unless regime clears by then.
- **5b cooldowns**: ADA blocked until 10-02T08:00Z (18h+). SOL unlocks 10-01T14:00Z. NEAR expired long ago.
- **Consecutive-loss streak**: 5/7. **Two more losing closes = 7-day full-pause kill switch** (REQUIRES user RESUME per guardrails). First time in the 2-away zone since the 09-23 recovery wake.
- **Drawdown 10.70%**: 1.80pp headroom to 12.5% warn. Monitor closely.
- **SBD defensive posture**: regime 5a + SBD ACTIVE blocks all new entries. If SBD persists for 2+ wakes, lessons.md observation about SBD cadence becoming more frequent is relevant.
- **Monthly archive status**: 23 live rows in trade_log.md; comfortable size, no action needed until month-end.
- **Open positions as of this wake**: NONE — book flat for first time since 10-01 EOD opened ADA.
