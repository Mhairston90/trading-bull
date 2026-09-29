# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md`; the log remains the source of truth.
> **Last rebuild:** 2026-09-29T17:30Z routine-02-midday (PT 2026-09-29 10:30) — **off-schedule Tue midday fire ~2.5h early vs cron 13:00 PT**; book flat, no MTM change, no exits.

## Account

- Starting equity: **$10,000.00**
- Cash: **$10,263.72** (equity = cash since no open positions)
- Realized PnL: **+$263.72** ($264.60 − $0.88 SOL 09-27 close)
- Unrealized PnL: **$0.00** (flat)
- Current equity: **$10,263.72**
- Equity peak: **$11,068.89**
- Drawdown from peak: **7.28%**
- Since-inception return: **+2.64%**

## Open positions

_None._ Book is flat.

Portfolio risk-at-moment: **0.00%**.
Open positions: **0 / 8** (strategy cap 0/4; BTC cluster 0/2).

## Day summary — PT 2026-09-27 (this EOD)

- **Day PnL**: **+$35.16 / +0.34%** (equity $10,228.56 EOD PT 09-26 → $10,263.72 EOD PT 09-27 after SOL round-trip close). Prior EOD had SOL @ MTM $120.59 unrealized −$36.04; today SOL exited at $121.6894 realizing net −$0.88 → net equity uplift +$35.16.
- **Trades opened**: **0**.
- **Trades closed**: **1** (SOL/USD long 75.09 @ $121.6894, R −0.01 / net −$0.88, exit-ema20-confirm-missed-scheduler-replay).
- **Win rate today**: 0/1 = 0.00% (net-loser by $0.88, but essentially a scratch — +0.30R gross flipped to −0.01R net by round-trip friction).
- **Time-in-trade (SOL)**: 27h (12:00Z 09-26 → 15:00Z 09-27).

## Rolling benchmark (marked to close of SOL exit 15:00Z 09-27 + current 04:13Z 09-28 snapshot)

- **BULL 30d** (08-28 → 09-28 wake): **-1.64%** approx (equity $10,263.72 vs ~$10,435 baseline 30d ago).
- **BULL 7d** (09-21 → 09-28 wake): **-2.09%** approx (same window post-outage).
- **BTC-hold 30d** (~$79,500 → live $83,404.80): **+4.91%**.
- **BTC-hold 7d** (~$76,398 → live $83,404.80): **+9.17%**.
- **BULL vs BTC-hold 30d**: **-6.55pp behind** BTC (+0.41pp vs overnight -6.96pp).
- **BULL vs BTC-hold 7d**: **-11.26pp behind** BTC (+0.03pp vs overnight -11.29pp).
- **90d benchmark**: not-yet-computable (post-outage cross-window 74d gap; will resume after 10-15).

## Exit-rule replay — SOL/USD (bars 13:00Z 09-27 → 03:00Z 09-28 covered)

**Rule 1 (W22-G two-bar 20-EMA break) FIRED at 15:00Z 09-27 close.**
- Bar 13:00Z close $123.17 vs EMA20 ~122.40 → ABOVE (+$0.77)
- Bar 14:00Z close $121.68 vs EMA20 ~122.35 → BELOW (−$0.67) [bar 1 of confirmation]
- Bar 15:00Z close $121.75 vs EMA20 ~122.31 → BELOW (−$0.56) [bar 2 of confirmation → **EXIT FIRES**]
- EMA20 anchored from indicators.py 13:12Z 09-27 (122.298 at 12:00Z close) and rolled forward with α = 2/21 = 0.0952; converged EMA at 03:00Z close 121.699 (indicators.py 04:13Z), cross-checked backward to 15:00Z ≈ 122.16–122.31 band. Both 14:00Z and 15:00Z closes below by ≥$0.4 on the converged basis.
- Exit fill: $121.75 × (1 − 0.0005 slippage) = **$121.6894**.
- Gross PnL: 75.09 × (121.6894 − 121.07) = +$46.51 / +0.30R gross.
- Round-trip commission: (9091.15 + 9137.66) × 0.0026 = **$47.39**.
- Net PnL: 46.51 − 47.39 = **−$0.88 / −0.01R net** (scratch, commission-eaten).

**Rule 1-SBD**: NOT APPLICABLE — regime 5a FAIL (3/15 positive) but SBD leg-1 (≤1 positive) not met, so 20-EMA basis retained.

**Rule 2 (static stop 119.0198)**: NOT HIT prior to exit (14:00Z low $121.40 > stop; 15:00Z low $121.28 > stop). Post-exit trivia: 04:00Z 09-28 (still forming) has intrabar low $119.00 = $0.02 below stop, but position had already exited at 15:00Z 09-27.

**Rule 3 (4R target 129.2708)**: NOT HIT (max close $124.44 at 09:00Z 09-27 = +1.64R).

**W22-H breakeven ratchet**: **NEVER ARMED** in this trade. Peak 1H close = 09:00Z 09-27 $124.44 = +1.64R, $0.73 short of +2.0R arm level $125.17. This is the 4th instance of the peak-close < +2R pattern (SOL 06-22 +1.51R, SOL 06-29 +1.74R, ETH 07-04 +1.44R, now SOL 09-27 +1.64R — pattern-of-4). Companion lesson: [[lesson-2026-06-29-w22h-ratchet-2nd-instance]] escalated to pattern-of-3 with 07-04 ETH; this 09-27 SOL adds pattern-of-4 confirmation. Give-back: peak close +1.64R → exit close +0.34R gross (net −0.01R) = ~1.65R of unrealized surrendered — the same architecture the W22-H was designed to catch, but here the ratchet stayed dormant because +2.0R close was never reached.

## Exit-rule replay — no other positions (book was single-position SOL)

## Entry-scan (overnight 13:12Z 09-28) — regime FAIL blocks all new entries; 2 tech-PASS candidates blocked

**Regime**: **3/15 positive 24h, median −1.58% → 5a FAIL** (positive count 3 < 4 floor).

Positive pairs: LINK (+3.99%), NEAR (+0.38%), TRX (+0.34%). Rotation from EOD positives (SUI +5.55% dropped to −5.13%; LINK new positive at +3.99%; NEAR held marginally positive).

**5a-SBD**: CLEAR — leg-1 (≤1 positive) fails (3 > 1); leg-2 (median ≤ −1.0%) met at −1.58% but SBD requires BOTH. Regime is standard 5a FAIL, not SBD.

**Full-pass technical check per indicators.py 13:12Z (rules 1+2+2a+3+4a)**: **2 pairs FULL PASS — ETH and LINK** (first non-zero tech-PASS count in 3 wakes). Both blocked by 5a FAIL. If regime had passed, rule 8 tiebreaker would prefer **ETH (rank 2)** over LINK (rank 13).

| Pair | R1 (>EMA20) | R2 (RSI≥55) | R3 (4H>EMA50) | R4a | Verdict |
|---|---|---|---|---|---|
| BTC | PASS +$8.95 | FAIL RSI 47.5 | FAIL −$381 | OK | R2+R3 fail |
| ETH | **PASS +$22.6** | **PASS RSI 58.5** | **PASS +$1.28** | OK | **FULL PASS** — blocked by 5a |
| SOL | PASS +$0.03 | FAIL RSI 48.0 | PASS +$1.57 | OK | R2 fail (also 5b cooldown til 15:00Z) |
| HYPE | FAIL −$0.01 | FAIL RSI 46.8 | FAIL −$1.49 | OK | technical reject |
| XRP | PASS +$0.023 | PASS RSI 58.2 | FAIL −$0.009 | OK | R3 fail (near miss) |
| SUI | FAIL | FAIL RSI 43.1 | PASS +$0.115 | OK | R1+R2 fail |
| TAO | FAIL | FAIL RSI 43.6 | PASS +$6.71 | OK | R1+R2 fail |
| XDG | FAIL | FAIL RSI 47.1 | FAIL | OK | technical reject |
| NEAR | PASS +$0.011 | FAIL RSI 50.7 | PASS +$0.57 | OK | R2 fail |
| ADA | PASS +$0.0027 | FAIL RSI 53.5 | PASS +$0.001 | OK | R2 fail (near-miss RSI) |
| LINK | **PASS +$0.75** | **PASS RSI 69.9** | **PASS +$0.73** | OK | **FULL PASS** — blocked by 5a |
| LTC | FAIL | FAIL RSI 48.7 | PASS +$4.37 | OK | R1+R2 fail |
| FARTCOIN | FAIL | FAIL RSI 37.1 | FAIL | OK $2.02M | technical reject |
| TRX | PASS +$0.001 | PASS RSI 60.8 | FAIL −$0.004 | FAIL $1.03M | R3+R4a fail |
| AVAX | FAIL | FAIL RSI 42.5 | PASS +$0.14 | OK | R1+R2 fail |

**Verdict**: **2 technical-PASS pairs (ETH, LINK)** — both blocked by regime 5a FAIL. Book stays flat. Rule 8 tiebreaker if regime recovered: ETH (rank 2 notional) > LINK (rank 13).

Note: ONDO/USD still not in `scripts/indicators.py` config (4th consecutive wake) — FARTCOIN listed instead. Routed to routine-04-harness Sat 10-03 for universe config patch.

## Active kill-switch state (routine-02-midday 2026-09-29T17:30Z / PT 2026-09-29 10:30)

- Daily loss cap (PT 2026-09-29 in-progress): flat book, 0.00% P&L intra-day. CLEAR.
- Consecutive-loss cap: **3 losses** (NEAR 09-23 −1.01R, ADA 09-26 −0.29R, SOL 09-27 −0.01R scratch). Streak = 3 of 7. CLEAR.
- Max drawdown: **7.28%** from peak $11,068.89 (unchanged; book flat, no MTM). CLEAR (25% cap, 12.5% warn, **5.22pp headroom to warn**).
- Equity floor: **$10,263.72 > $7,500** (+$2,763.72). CLEAR.
- Exposure: **0.00%** / 4% used (flat book). CLEAR.
- Cluster cap: **0/2 BTC-cluster**. CLEAR.
- Universe/liquidity: N/A (flat book).
- 5b cooldown: SOL 09-26T12Z (**76h ago**) CLEAR; ADA 09-26T06Z (**82h ago**) CLEAR; NEAR 09-23T14Z (**168h ago**) CLEAR. All expired.
- **Regime 5a: FAIL 3/15 positive live-ticker, median −0.82%** — informational only; midday does not run entry scan per routine spec.
- **5a-SBD: CLEAR** — leg-1 (≤1 positive) fails (3>1); leg-2 (median ≤ −1.0%) fails (−0.82 > −1.0). Standard 5a FAIL, not SBD.
- MCP availability: Kraken multi-ticker healthy (15/15 pairs returned in one call). CLEAR.
- **All Ring 3 kill switches CLEAR.**

### Midday note (09-29T17:30Z)

Book flat since 09-27T15Z SOL close. No positions to mark, no exits to evaluate. Live-ticker regime deteriorated vs 09-25T20Z midday (was 13/15 positive median +3.14%; now 3/15 positive median −0.82%). Bar-close authoritative regime not recomputed at midday. Next entry decision is tomorrow overnight (13:00Z 09-30 = 06:00 PT Wed). No Telegram notify (no kill switch, no exit, no DD-warning threshold crossed).

**Off-schedule fire flag:** routine fired at 17:30Z (10:30 PT) vs cron `0 13 * * 1-5` (13:00 PT) — ~2.5h early. Same Task Scheduler drift pattern flagged in prior overnight ops notes (5-of-5 pattern routed to routine-04-harness Sat 10-03 for cron audit). This adds 6th off-schedule instance. Off-schedule fire did no harm here (flat book, midday routine bars entries anyway).

## Ops notes

- **5th consecutive off-schedule fire in ~24h window** (Sat overnight 06:20Z, Sat midday 20:00Z, Sat EOD 04:27Z, Sun overnight 13:15Z, this Sun EOD 04:13Z 09-28 despite cron `0 21 * * 1-5` = Mon-Fri only). Task Scheduler mask has evidently drifted or is misconfigured to fire Sat + Sun. **Routed to routine-04-harness Sat 10-03 for cron audit + Task Scheduler XML review** (5-of-5 pattern is well past evidence threshold).
- **Missed-scheduler-replay caught a real exit** — the retroactive replay of SOL Rule 1 at 15:00Z 09-27 close is the intended safety-net behavior. Without this off-schedule Sun EOD fire (or the next scheduled Mon 06:00Z overnight ~2h from now), the SOL exit would have been delayed by ~13 more hours during which unrealized went from +$51 (15:00Z) → nearly $0 (03:00Z 09-28 close $119.80 nearly at stop). Off-schedule fire actually reduced friction here.
- **W22-H breakeven ratchet pattern-of-4** — SOL 09-27 peak close +1.64R falls into the same close-vs-intrabar gap pattern as SOL 06-22 (+1.51R), SOL 06-29 (+1.74R), ETH 07-04 (+1.44R). All 4 peaked between +1.4R and +1.8R at 1H close; none armed the +2.0R breakeven ratchet; all gave back most/all of the unrealized. Note: 09-27 SOL peak intrabar was $124.91 = +1.66R intrabar (bar high 08:00Z), also below +2.0R intrabar — so even an intrabar-arm variant of W22-H would NOT have caught this instance. See lessons.md new entry below.
- **Watchdog: 8 findings** (unchanged from overnight — routine-06 heartbeat, routine-07 heartbeat, C dirty-tree 4 files, D stale-MTM ×5 variants). No new findings.
- **Cash-fit constraint no longer binding** — book is flat, all $10,263.72 available for next entry.
- Not last trading day of month (Sept 30 is next Wed) → no monthly archive this wake.

## Notes for next wake

- Book is flat; next Monday routine-01-overnight (06:00 PT Mon 09-28 = 13:00Z 09-28) can execute any entry cleanly (no cash constraint). Expected regime by then: depends on Sunday overnight (Asia session) tape.
- 5b cooldown on SOL active until 15:00Z 09-28 (any Mon 06:00 PT wake before then blocks SOL re-entry, but rank-1 BTC and rank-2 ETH are unblocked — if regime recovers and their R1/R2 pass).
- W22-H ratchet pattern-of-4 escalation triggered: route to routine-04-harness Sat 10-03 memo as candidate P-W25R-RATCHET-TIGHTEN with options from the 07-04 ETH lesson (options a/b/c/d for lowering close threshold or moving to intrabar+close-confirm hybrid).
