# BULL Strategy Proposal — 2026-W18

> **Off-cycle proposal.** Drafted 2026-04-28 (Tue) at user request. Normal channel is routine #4 Saturday; this memo is intended to be reviewed by user and either approved via Telegram `[Y/N]` for routine #5 Sunday application, OR superseded by next routine #4's evidence-based version.
>
> **Type:** Ring 2 gated — `strategy.md` edits.
> **Origin:** Three lessons in `memory/lessons.md` (2026-04-24 TRX wick, 2026-04-27 cascade, 2026-04-24 BTC commission drag) plus on-demand deep-dive analysis.
> **Backtest evidence:** **NOT included** — would require routine #4's TradingView harness. Approval based on trade-log evidence only is at user discretion.

## Headline summary

Three proposed edits to `memory/strategy.md`. Together they directly address the two highest-impact failure modes BULL has produced in its 8-day life (cross-asset cascade −$153.65 and TRX wick −$26.69). Combined back-of-envelope estimate: same-week realized loss would have dropped from −$222.89 to ~−$130 (40% better) had these been live.

| # | Title | Addresses lesson | Confidence |
|---|---|---|---|
| A | BTC-cluster correlation cap | 2026-04-27 cascade | high |
| B | Liquidity floor on entries | 2026-04-24 TRX wick | high |
| C | One-entry-per-wake stagger | 2026-04-27 cascade (cluster mechanic) | medium-high |

---

## Proposal A — BTC-cluster correlation cap

### Current rule (`strategy.md` § Entries, rule 6)

```
6. Current open positions < 4 (v0 deliberately uses half the 8-position cap)
```

### Proposed replacement

```
6. Current open positions < 4 (v0 deliberately uses half the 8-position cap)
6a. Concurrent positions in the BTC-correlated cluster
    {BTC, ETH, SOL, TAO, AVAX, SUI, LINK} <= 2.
    The 7 pairs above have empirically high 1H correlation
    (>0.7 estimated from cascade event 2026-04-27T05:00Z where all
    4 simultaneously open positions in this cluster stopped within
    a single 1H bar).
```

### Evidence (trade-log)

- 2026-04-26T21:05Z: 3 simultaneous OPENs in cluster — ETH, BTC, SOL — same wake
- 2026-04-27T04:05Z: 4th OPEN — TAO — added 7h later
- 2026-04-27T05:00Z: ALL FOUR stopped in same 1H bar (intra-bar). R-multiples −1.06, −1.08, −1.06, −1.03 ≈ uncorrelated math would predict ~25% probability of simultaneous stops; actual was 100%
- Net realized that bar: −$153.65 = 69% of all-time BULL losses

### Risk assessment

- **Downside if adopted:** in a clean cross-cluster rally where all 7 pairs trigger together, BULL captures only 2 of 7 instead of up to 4. Estimated 1-2 missed entries per month based on current trade frequency.
- **Downside if NOT adopted:** another cascade event recurs. With current sizing, 4 simultaneous stop-outs = ~−4R = ~$200 loss. Daily-loss kill-switch (5%) absorbs once but consecutive-loss-day counter starts ticking.
- **Upside:** caps tail risk at ~2R per cluster event instead of ~4R.

### Expected impact

- On the 2026-04-27 cascade specifically: would have prevented at least 2 of 4 trades from firing (the 3rd and 4th cluster entries get rejected). Realized loss that day: ~−$80 instead of −$153.65.
- On future entries: marginal impact in normal regime; significant impact in cluster-trigger regime flips.
- Win rate: unchanged in expectation (rule reduces sample, not edge).

---

## Proposal B — Liquidity floor on entries

### Current rule (`strategy.md` § Entries, rule 4)

```
4. Pair has >= 10 candles of history on both 1H and 4H (no ultra-fresh listings)
```

### Proposed replacement

```
4. Pair has >= 10 candles of history on both 1H and 4H (no ultra-fresh listings)
4a. Pair has 24h notional volume >= $2.0M USD at time of entry-scan,
    measured from Kraken MCP `kraken_ticker`.
    Rationale: 2x ATR static stops are sensitive to single-bar wicks
    on thin pairs (lesson 2026-04-24 TRX). $2M/24h is the empirical
    breakpoint where 1H wicks remain bounded.
```

### Evidence (trade-log + universe.md)

- 2026-04-24T20:00Z: TRX/USD CLOSE @ 0.330120, stop was 0.330285. Intra-bar low was 0.319711 — wick reached 3.2% below stop. R = −1.10, $ = −$26.69.
- TRX/USD ranks **#15** in current universe at $1.04M/24h notional — thinnest in BULL's universe
- Pairs filtered out by this rule (current universe): FARTCOIN ($1.52M), AVAX ($1.21M), LINK ($1.17M), PENGU ($1.07M), TRX ($1.04M) — 5 of 15 pairs (33%)
- BULL's only entry in the affected set so far was TRX (lost $26.69). AVAX entered above $2M threshold by margin in older fixture but worth re-checking via universe refresh.

### Risk assessment

- **Downside if adopted:** universe effectively shrinks from 15 to 10 for entry purposes. Same pairs remain valid for exit (existing positions hold).
- **Downside if NOT adopted:** continued exposure to wick risk on rank 11-15 pairs. Each instance ~−1R extra slip beyond intended stop-distance.
- **Edge case:** a low-volume pair on a strong move can outperform the top-10. We accept missing those.

### Expected impact

- Eliminates ~33% of universe from entry consideration.
- Eliminates known wick risk on 5 named pairs.
- BULL's existing TAO position not affected (TAO is rank 5, $6.80M).

---

## Proposal C — One-entry-per-wake stagger

### Current rule (`strategy.md` § Entries)

No explicit rule limiting number of new entries per routine wake. Implicit limit is the 4-position cap (rule 6) and 4% portfolio risk cap.

### Proposed replacement (new rule, append to § Entries)

```
8. Max 1 new entry per routine wake. If multiple pairs are eligible at the
   same wake, prefer the highest-ranked pair by 30d notional (i.e., XBT
   beats ETH beats SOL beats TAO etc.). Remaining eligible entries are
   re-evaluated next wake; if no longer eligible by then (e.g., RSI
   dropped below 55), they're skipped.
```

### Evidence (trade-log)

- 2026-04-26T21:05Z wake: 3 simultaneous OPENs (ETH, BTC, SOL) at the same minute — single-wake cluster fill
- These 3 + the 04:05Z TAO entry comprise the cascade event of 2026-04-27T05:00Z

### Risk assessment

- **Downside if adopted:** in trend regime, BULL fills slots more slowly. Across 5 wakes/week × 1 entry max = 5 max entries/week vs current capability for 4 in a single wake.
- **Downside if NOT adopted:** continued single-wake cluster fill. Mechanically: any regime flip that causes ≥2 pairs to simultaneously satisfy entry rules will fill all of them on the same bar — by definition correlated trades.
- **Synergy with Proposal A:** A and C reinforce each other. A caps cluster, C ensures even within-rule fills are time-spread.

### Expected impact

- Same regime-flip event of 2026-04-26 21:05Z: instead of opening ETH+BTC+SOL simultaneously, opens BTC only. ETH and SOL re-evaluated next wake (02-05 hours later). If conditions still hold, they enter; if regime has already turned, they're skipped — exactly the desired behavior.
- Win rate: expected to improve modestly. Trades that would have entered "with the herd" and stopped together get filtered to those that still look good after a few hours of price action.

---

## What this proposal does NOT change

- Risk per trade: stays 1.5%
- 2×ATR stop distance: unchanged (B addresses the wick exposure separately via universe filter)
- 4R take-profit, 1H EMA-cross exit, 1H RSI > 55 entry: unchanged
- Concept buckets (`momentum: 100%`): unchanged — these are entry-side risk-management edits, not bucket reallocation
- Universe size (15): unchanged — Proposal B filters within the 15 by liquidity, doesn't shrink the list

## Application path

If approved (Telegram `[Y]`):

1. Routine #5 next Sunday (2026-05-03 or later) reads this memo, edits `memory/strategy.md` section "Entries" with the 3 changes above
2. Existing TAO position unaffected — rules apply to new entries only
3. Lesson statuses in `memory/lessons.md` updated from `active` to `superseded` for the 3 lessons addressed:
   - 2026-04-24 TRX wick → superseded by Proposal B
   - 2026-04-27 cross-asset cascade → superseded by Proposals A + C
   - 2026-04-24 BTC commission drag → **NOT addressed by this proposal**, remains active for next routine #4

If rejected (Telegram `[N]` or 24h timeout):

1. This memo archived
2. Lessons remain active
3. Next routine #4 (Saturday 2026-05-03) re-evaluates with TradingView backtest evidence

## Honest caveats

- **No backtest.** Routine #4's normal output includes TradingView strategy-tester R-stats over historical data. This proposal has neither. User accepting it is accepting trade-log evidence only.
- **Sample size.** 9 closed trades is below any noise floor. The cascade event drives most of the analysis; without it, BULL would be at −0.69% over 8 days and these proposals would feel more speculative.
- **Lesson #3 (BTC commission drag) deferred.** The exit-confirmation fix (D in earlier analysis) needs more thought on the exact threshold; deliberately not bundled here.
- **Volatility compression filter (E) deferred.** Could be highest-impact OR starve BULL of entries — needs backtest.

## Decision

User reply via Telegram:
- `[Y]` — apply all three proposals at next routine #5
- `[Y A,B]` — apply selected subset only
- `[N]` — reject, lessons stay active
- (no reply within 24h) — auto-rejected per mandate

---

*This memo created 2026-04-28T at user request as off-cycle deep-dive output. Not a substitute for routine #4's evidence-backed Saturday review.*
