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

(empty — first harvest will be routine #6 first run)
