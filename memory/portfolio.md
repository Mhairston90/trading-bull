# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md`; the log remains the source of truth.
> **Last rebuild:** 2026-10-06T04:13Z routine-03-eod (PT 2026-10-05 21:13 Mon) — on-schedule (+13min drift). First main-routine commit since 10-02 midday (routine-03 EOD missed on 10-02 Fri; weekend non-fire 10-03 Sat & 10-04 Sun; this is first wake since). **NEW ENTRY: NEAR/USD @ $5.254826 (rule-8-winner, rank-7 deterministic after ranks 1-6 all fail R1/R2 technical)**. Marginal 4-floor regime entry — exact 09-23 NEAR archetype flagged in research_log.

## Account

- Starting equity: **$10,000.00**
- Cash: **$5,603.78** ($9,686.86 prior − $4,072.49 NEAR notional − $10.59 open commission)
- Realized PnL (since inception): **−$313.14** (unchanged from 10-02)
- Unrealized PnL: **−$1.88** (NEAR slippage drag at mark; open commission is in cash reduction)
- Current equity: **$9,674.39** (cash $5,603.78 + NEAR MTM $4,070.61)
- Equity peak: **$11,068.89** (unchanged)
- Drawdown from peak: **12.60%** — **BREACHES 12.5% warn threshold by 0.10pp** (first wake above warn)
- Since-inception return: **−3.26%**

## Open positions

| Pair | Side | Size | Entry | Stop | Target 4R | Current | Unrealized $ | Unrealized R | Stop distance | Portfolio risk |
|---|---|---|---|---|---|---|---|---|---|---|
| NEAR/USD | long | 775 | $5.254826 | $5.067336 | $6.004786 | $5.2524 | −$1.88 | −0.01R | $0.18749 | 1.502% |

Portfolio risk-at-moment: **1.502%** of equity (one position, 2×ATR stop distance $0.18749 × 775 = $145.30 vs $9,674.39 equity).
Open positions: **1 / 8** (strategy cap 1/4; BTC-cluster 0/2 — NEAR is not in the cluster).

## Day summary — PT 2026-10-05 Mon trading day

- **Day PnL (realized)**: **$0.00 / 0.00%** of PT-midnight equity (no closes today).
- **Day PnL (unrealized change vs PT-midnight)**: **−$12.47 / −0.129%** (= open commission $10.59 + slippage $1.88 on NEAR entry).
- **Trades opened today**: **1** (NEAR @ 04:00Z = PT 2026-10-05 21:00 Mon close).
- **Trades closed today**: **0**.
- **Win rate today (closed only)**: n/a (no closes).

## NEAR entry mechanics — 2026-10-06T04:00:00Z (PT 2026-10-05 21:00 Mon)

- **Trigger**: strategy v0.4 R1-R8 full-pass deterministic (not fallback). Rank-7 pair wins because ranks 1-6 all fail R1 (close < EMA20) and/or R2 (RSI < 55) technically; rank 12 AVAX also fully passes but loses R8 rank tiebreak to NEAR.
- **Technical (per indicators.py 04:13Z closed-bar)**: R1 close $5.2524 > EMA20 $5.16644 by $0.08596 ✓; R2 RSI 62.7 > 55 ✓; R2a RSI < 80 ✓; R3 4H close > 4H EMA50 by $0.3628 ✓; R4a notional $25.50M > $2.0M ✓; R5 no open NEAR ✓; R5a regime 4/15 positive (EXACT floor, marginal PASS) median −0.65%; R5a-SBD CLEAR (4>1 and −0.65>−1.0); R5b cooldown cleared (NEAR 09-23T14Z stop was 283h ago); R6 0→1/4 strategy cap ✓; R6a NEAR not in BTC-cluster ✓; R7 1.502% < 4% cap ✓; R8 rank-7 wins over rank-12 AVAX ✓.
- **Sizing**: risk 1.5% × $9,686.86 = $145.3029; stop distance 2×ATR = $0.18749; size = $145.3029 / $0.18749 = 774.98 → **775 NEAR**; fill $5.2524 × 1.0005 slippage = $5.254826; stop $5.067336; target 4R $6.004786; notional $4,072.49 fits cash $9,686.86 with $5,603.80 buffer.
- **Open commission**: 0.26% × $4,072.49 = $10.59.
- **News (W19-E, informational)**: no base-asset NEAR scan this wake (Firecrawl bypassed on-schedule for budget; the 4-floor regime is the dominant risk signal, not single-pair news).
- **Sentiment (W19-E, informational)**: NEAR +8.02% 24h change is the strongest in the universe — single-name strength against a −0.65% median regime is itself a divergence signal (NEAR running while the rest of the market bleeds).

## Rolling benchmark (marked at EOD 2026-10-06T04:13Z, NEAR filled)

- **BTC price now**: $85,493.1 (per indicators.py 1H close).
- **BTC-hold 30d**: BTC $85,493 vs ~$79,800 09-05 baseline → **~+7.1%**. BTC continues steady grind; +$933 since 10-02 midday mark ($84,560 → $85,493).
- **BTC-hold 7d**: BTC $85,493 vs ~$84,400 09-28 baseline → **~+1.29%**.
- **BULL 30d** (equity $9,674.39 vs ~$10,480 09-05 estimate): **~−7.69%**.
- **BULL 7d** (equity $9,674.39 vs ~$10,068 09-28 estimate): **~−3.91%**.
- **BULL vs BTC-hold 30d**: **~−14.8pp behind** (widened from 10-02 −13.6pp by BTC +0.9pp + BULL −0.3pp this period).
- **BULL vs BTC-hold 7d**: **~−5.2pp behind** (improved from −17.5pp 10-02 as 7d window rolled past the 09-27→10-02 loss cluster).
- **90d benchmark**: not-yet-computable (post-outage cross-window still spans the gap).

## Entry context — this wake

- **Routine 03 EOD is entry-authorized** per routine spec. Full universe scan executed via indicators.py.
- Entry selection was deterministic — single pair survived R1-R8 at rank R8 tiebreak. No judgment call on technicals.
- **Judgment call made on entry acceptability**: with regime at EXACT 4-floor matching 09-23 NEAR same-session stop archetype + streak 6/7 + routine-04 memo missed (no Ring-2 approved mitigations) + three pending Ring-2 proposals (options a/b/d from 10-01 lesson, plus post-outage DEFER heuristic) that would all BLOCK this entry — this is a strategy-v0.4-compliant HIGH-RISK entry. Executed per mandate (strategy compliance is the governing text; backlog proposals do not block execution).

## Active kill-switch state (routine-03-eod 2026-10-06T04:13Z / PT 2026-10-05 21:13 Mon)

- **Daily loss cap (PT 10-05 trading day)**: **0.00% realized, −0.129% unrealized** vs PT-midnight equity $9,686.86. **CLEAR** (<5% cap; 4.87pp headroom).
- **Consecutive-loss cap**: **6 losses** (NEAR 09-23, ADA 09-26, SOL 09-27 scratch, SOL 09-30, ADA 10-01, SOL 10-02). Streak **6/7**. **CLEAR but 1-loss headroom.** NEAR 10-06 stop-out would trip Ring 3; user `RESUME` required.
- **Max drawdown**: **12.60% from peak $11,068.89**. **BREACHES 12.5% warn threshold by 0.10pp** — first time above warn. Still well below 25% kill cap (12.40pp headroom). Telegram EOD card will flag.
- **Equity floor: $9,674.39 > $7,500** (+$2,174.39). **CLEAR** (2174pp headroom).
- **Exposure: 1.502% / 4%** used. **CLEAR** (2.498pp headroom).
- **Cluster cap: 0/2 BTC-cluster**. **CLEAR** (NEAR not in cluster).
- **Universe/liquidity**: NEAR R4a $25.50M >> $2.0M floor. **CLEAR**.
- **5b cooldown state**: no fresh cooldowns post-NEAR entry. SOL 10-02T17Z stop cleared at 10-03T17Z. ADA 10-01T08Z stop cleared at 10-02T08Z. All 14 remaining pairs CLEAR.
- **Regime 5a (ambient this wake)**: 4/15 positive 24h (HYPE +3.26, NEAR +8.02, AVAX +2.26, TRX +0.05), 11/15 negative (BTC −0.65, ETH −0.62, SOL −0.33, XRP −0.86, SUI −3.41, TAO −0.31, XDG −1.37, ADA −1.09, LINK −2.68, LTC −1.13, FARTCOIN −6.80). Median −0.65%. **MARGINAL PASS at EXACT 4-floor, SBD CLEAR**.
- **MCP availability**: Kraken multi-ticker (via indicators.py REST) healthy; Telegram script healthy; ue-scripts and yt-analysis MCP failed (not needed for BULL ops).
- **All Ring 3 kill switches CLEAR** but DD now 0.10pp above 12.5% warn + streak 1 loss away from Ring 3 full-pause.

## Ops notes

- **W22-H ratchet state**: not yet armed on NEAR (needs +2R close = NEAR close ≥ $5.629806). Currently NEAR at $5.2524 = +0.00R unrealized.
- **Pattern-of-6 rule8-cashfit-class** (loosely counting rule-8-winner as same class since all 5 prior were rank-pivot picks): 06-17 SOL fallback, 07-10 BTC +0.23R, 09-30 SOL −1.00R, 10-01 ADA −1.02R, 10-02 SOL −1.03R, 10-05 NEAR (open). This entry is **not strictly cashfit** since NEAR notional $4,072 fits cash $9,686 easily; it's rank-pivot because ranks 1-6 fail R1/R2 technically. Classification: **rank-pivot-tech-only** (not cashfit).
- **Pending Ring-2 proposals (all still backlog)**:
  - P-W27-CASHFIT (routine-04-harness W25R)
  - P-W25R-SAMESESSION-STOP-GATE (options a/b/d from 10-01 ADA lesson, score 9)
  - P-W25R-RATCHET-TIGHTEN (from 09-27 SOL W22-H lesson, score 8)
  - P-W25R-POSTOUTAGE-DEFER-HEURISTIC (from 09-23 lesson, score 6)
  - Sat 10-03 memo missed (routine-04-harness watchdog A — 96h+ since last routine-03 and no routine-04 since 09-23 memo-prep). User `[Y/N]` on prior proposals also pending.
- **Watchdog findings (10, +2 from prior wake)**: routine-01 heartbeat dead 111h (A, NEW escalation — was previously tracked but now above 80h threshold), routine-03 heartbeat dead 96h (A, NEW escalation), routine-06/07 heartbeat dead (A×2, unchanged), dirty-tree 4 untracked files (C, unchanged), stale-MTM 5 variant portfolios (D×5, unchanged). Telegram-alerted via --telegram.
- **Scheduler diagnosis**: 10-02 EOD missed (last routine-03 was 10-01). 10-03 Sat non-fire (Mon-Fri cron). 10-04 Sun non-fire. 10-05 Mon EOD this is first wake since. Cron appears to have skipped 10-02 Fri EOD — unknown cause; possibly OS sleep or scheduler service hiccup. The 10-05 Mon EOD fire this wake is on-schedule (+13min drift from 21:00 PT target).
- **Drawdown trajectory**: 12.49% (prior wake) → 12.60% (this wake, +0.11pp from NEAR open-commission + slippage drag alone). NEAR hitting stop would add ~$145 realized → DD ~14.1%. NEAR hitting 4R target would add ~$580 realized → DD ~6.6%.
- **Consecutive-loss trajectory**: 6/7 (unchanged, no closes this wake). NEAR stop-out = 7/7 → Ring 3 full-pause requires `RESUME`.

## Lessons status

No new lessons appended this wake. The NEAR entry under exact 4-floor regime is a direct companion case to [[lesson-2026-09-23-same-session-stop-after-regime-crystallization]] (score 8, NEAR 09-23) and [[lesson-2026-10-01-pattern-of-4]] (score 9, ADA 10-01). Outcome of this NEAR trade (expected within 1-24h) will add 1 more data point to the P-W25R-SAMESESSION-STOP-GATE evidence base — a WIN would partly falsify the pattern; a LOSS would be pattern-of-5 and strengthen Ring-2 urgency.

## Notes for next wake

- **Routine 01 overnight** fires at ~04:00 PT 10-06 (= 11:00Z). Will MTM NEAR position against overnight 1H bars. Priority action: check whether 05:00Z, 06:00Z, 07:00Z, 08:00Z bars kept NEAR above EMA20 (currently $5.16644, trailing up at ~2% per hour). Stop at $5.067336 — intraday NEAR 24h low was $4.918 (per indicators.py historical bars), so stop is above session-local lows.
- **Routine 02 midday** fires ~12:00 PT 10-06 (= 19:00Z). Will MTM mid-session NEAR state.
- **Priority watch**: NEAR 24h = +8.02% while market −0.65% median = NEAR running against the tape. Could continue (strong signal) or reverse (profit-taking into weak market). The 4-floor regime adds systemic risk — if regime tips to 3/15 or below mid-trade, cross-market selling could drag NEAR with it even if NEAR-specific signal holds.
- **Ring 3 proximity**: streak 6/7 + DD 12.60% both near trip thresholds. One stop-out = 7-day pause. Monitor closely.
- **5b cooldowns**: no active cooldowns post-NEAR entry. All 14 non-NEAR pairs CLEAR.
- **Regime monitoring**: 4-floor marginal is 1-pair move from SBD risk (if any 1 of HYPE/NEAR/AVAX/TRX flips negative → 3/15 → 5a FAIL, no new entries + SBD defensive exits trigger if also median ≤−1.0%).
