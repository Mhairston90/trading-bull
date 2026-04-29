# BULL Idea Bank — harvested research candidates

> **Append-only.** Routine #6 (idea-scan) writes here weekly. Routine #4 (Saturday harness) reads here when drafting weekly memo proposals.
> **No autonomous trade authority.** Every row is a *candidate idea*, never a trade trigger. Promotion to a strategy rule requires Ring-2 `[Y/N]` like all other strategy edits.
> **Pruned monthly:** rows older than 90d with status `raw` or `pruned` get archived to `memory/archive/idea_bank_YYYY-MM.md` by routine #3.

## Schema

| Field | Description |
|-------|-------------|
| `id` | `IDEA-YYYYMMDD-NN` (auto, sortable) |
| `harvested` | ISO8601 timestamp of routine #6 wake that captured it |
| `source` | Name from `idea_sources.md` |
| `url` | Direct link to the source piece |
| `asset` | `BTC`, `ETH`, `crypto-broad`, `equities` (informational), `regime`, `methodology` |
| `claim` | One-sentence summary of the testable assertion |
| `mechanism` | Why the source thinks this works (1-2 lines) |
| `signal-quality` | 1-5 inherited from `idea_sources.md` |
| `bull-fit` | 1-5 — does this apply to BULL's universe + 1H/4H timeframe + spot-only mandate? |
| `testability` | 1-5 — can we backtest this in TradingView with available data? |
| `score` | `signal-quality + bull-fit + testability` (max 15). Routine #4 prioritizes by score. |
| `status` | `raw` (just harvested), `under-review` (cited in a draft memo), `proposal-drafted` (memo written), `applied` (rule live in `strategy.md`), `superseded` (replaced by a better version), `pruned` (rejected — note why) |
| `notes` | Free text — why it was scored that way, caveats, lookback window claimed |

## Status lifecycle

```
raw → under-review → proposal-drafted → applied
                  ↘                  ↘
                   pruned             superseded
```

- `raw` → `pruned` if routine #4 reviews and decides not to draft
- `proposal-drafted` → `applied` if user replies `[Y]` on the memo
- `proposal-drafted` → `pruned` if user replies `[N]` or 24h timeout
- `applied` → `superseded` when a later proposal replaces the rule

## Honest filters (to keep the bank signal-dense)

Routine #6 should DROP (not even append) ideas that:
- Have no testable claim (pure macro: "BTC will go to $200K by year-end")
- Apply to instruments outside BULL's mandate (perps, options, leverage)
- Apply to timeframes BULL doesn't trade (HFT < 1m, monthly-rebalance > 1d)
- Repeat an idea already in the bank with status `raw`, `under-review`, `proposal-drafted`, or `applied`
- Source is below threshold this week (e.g., raw spam, off-topic)

If routine #6 drops more than 80% of harvested content, that's expected — the goal is signal density, not coverage.

## Bank

| id | harvested | source | url | asset | claim | mechanism | sig | fit | test | score | status | notes |
|----|-----------|--------|-----|-------|-------|-----------|-----|-----|------|-------|--------|-------|
| IDEA-20260429-01 | 2026-04-29T19:55Z | Glassnode Insights | https://insights.glassnode.com/the-week-onchain-week-17-2026/ | BTC | When BTC trades below the True Market Mean (~$78k) AND Short-Term Holder Cost Basis (~$79k), mid-term bias is bearish; reclaim signals trend shift. | Recent buyers' breakeven cohort generates supply pressure when underwater — rallies into TMM/STHCB historically reject in bear regimes. | 5 | 3 | 2 | 10 | **pruned** | **Pruned 2026-04-29:** data-access barrier. True Market Mean and STH Cost Basis are Glassnode-proprietary metrics, not on TradingView and not available via Kraken MCP. Implementing would require Glassnode API integration — out of scope for current toolset (TV + Kraken). Re-evaluate if a Glassnode data feed is added later. |
| IDEA-20260429-02 | 2026-04-29T19:55Z | Glassnode Insights | https://insights.glassnode.com/the-week-onchain-week-17-2026/ | BTC | When Short-Term Holder Realized Profit 24h SMA spikes to ~4× recent baseline, expect local-top rejection within ~24h. | Distribution-into-strength by recent buyers exhausts demand absorption; observed repeatedly in current bear cycle. | 5 | 2 | 1 | 8 | **pruned** | **Pruned 2026-04-29:** same data-access barrier as IDEA-01 + lower fit (BTC-only) and lowest testability. Not worth Glassnode integration alone. |
| IDEA-20260429-03 | 2026-04-29T19:55Z | Glassnode Insights | https://insights.glassnode.com/the-week-onchain-week-17-2026/ | BTC | When 7-day spot CVD on BTC transitions from sustained negative to positive deltas, expect short-term recovery. | Spot CVD is a real-time gauge of buy-vs-sell imbalance; sign-flip indicates exhausted seller initiation. | 4 | 3 | 2 | 9 | raw | **Note 2026-04-29:** held in `raw` pending routine #4 Saturday cost-benefit. CVD via community Pine indicator is feasible but adds integration cost; routine #4 to decide whether it's worth pursuing vs. pure-momentum baseline. Idea remains in bank — not pruned. |
| IDEA-20260429-04 | 2026-04-29T19:55Z | Glassnode Insights | https://insights.glassnode.com/the-week-onchain-week-17-2026/ | regime | When realized vol and implied vol converge (gap < 2%) on BTC, expect range-bound chop; reduce confidence in momentum entries. | Compressed RV/IV gap = limited directional conviction; momentum strategies underperform in low-vol-spread regimes. | 4 | 4 | 3 | 11 | raw | **Priority candidate for routine #4 Saturday 2026-05-02.** Universal (not BTC-only). Directly addresses option (c) deferred from lesson 2026-04-27 (cascade) — "regime filter that pauses new momentum entries when 1H ATR has compressed below recent average". RV-only proxy is cheap (ATR/stdev already in strategy). Threshold needs backtest. |

## Dropped this harvest (logged for audit)

- **Perpetual Market Directional Premium signal** (Glassnode W17): mandate violation — perps outside spot-only.
- **80K options strike pivot / short gamma zones** (Glassnode W17): mandate violation — options outside spot-only.
- **Leveraged-token rebalance flows** (Robot Wealth "To Trend or Not To Trend"): mandate / Kraken-listing — no leveraged tokens in BULL universe.
- **Wealth-management month-end rebalance** (Robot Wealth): equities only, not in mandate.
- **Crypto trend persistence framing** (Robot Wealth): not a new testable claim — reinforces existing momentum-bucket thesis but adds no rule candidate.
- **Robot Wealth "For The Love of The Game"** (within 7d window): meta/career advice, no testable claim.

## Harvest history

| harvest_id | wake | sources_attempted | sources_ok | claims_extracted | survived_floor | deduped | appended | notes |
|------------|------|-------------------|------------|------------------|----------------|---------|----------|-------|
| HARV-20260429-DRYRUN | 2026-04-29T19:55Z manual dry-run | 2 (Glassnode, Robot Wealth) | 2 | 10 | 4 | 0 | 4 | First-ever harvest. Pre-scheduled run validation. RW "To Trend or Not To Trend" was outside 7d window — included for pipeline-validation only, would be excluded under normal routine. Real Friday-cron run will hit all 10 sources. |
