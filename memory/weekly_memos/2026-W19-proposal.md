# BULL Strategy Proposal — 2026-W19

> **STATUS: DRAFT — pending user review**
> **Off-cycle proposal.** Drafted 2026-04-29 (Wed) at user request after deep-dive on TradingAgents framework (YouTube video analysis). Normal channel is routine #4 Saturday (2026-05-02); this memo is for off-cycle Telegram-equivalent approval.
>
> **Type:** Mixed. Proposal D is Ring 2 (`strategy.md` edits). Proposal E is Ring 1 (process-only change to `research_log.md` convention) but lays groundwork for a future Ring-2 news-veto rule.
> **Origin:** Lesson `2026-04-29 — RSI extremity + divergent tape (TAO same-day re-entry)` in `memory/lessons.md`, plus comparative analysis vs. TradingAgents multi-agent framework.
> **Backtest evidence:** **NOT included** — would require routine #4's TradingView harness. Approval based on trade-log evidence + lesson recommendations is at user discretion.

## Headline summary

Two proposed changes. Together they address the open lesson from 2026-04-29 (TAO climactic-RSI + divergent-tape entry → −1.02R / −$64.37) and add the missing news-awareness layer the mandate allows but v0 ignores.

| # | Title | Addresses lesson | Confidence | Ring |
|---|---|---|---|---|
| D | Climactic-RSI + regime-confirmation + re-entry cooldown | 2026-04-29 TAO | medium-high | 2 |
| E | Research_log analyst-role split + news pass | (new — mandate gap) | medium | 1 |

**Note on framing:** Inspiration came from TradingAgents' "Bull vs. Bear debate" mechanism. The implementation here is *not* LLM-judgment-based — that would conflict with BULL's deterministic-rule core. Instead, D codifies the three specific veto conditions surfaced in lesson 2026-04-29 as hard rules. E adds structured information gathering (analyst roles) without giving the LLM trade-decision authority.

**Not bundled here:**
- Lesson 2026-04-24 (BTC commission drag) — still deferred to routine #4 Saturday with backtest evidence on exit-confirmation thresholds.
- Volatility-compression filter — same.

---

## Proposal D — Climactic-RSI cap, regime-confirmation gate, re-entry cooldown

### Current rules (`strategy.md` § Entries, rules 2 and 5)

```
2. 1H RSI(14) > 55
...
5. No existing open position in this pair
```

### Proposed additions (3 new sub-rules)

```
2a. 1H RSI(14) <= 80 at entry-scan close. Climactic readings (>80)
    have produced poor expectancy in mean-reverting tape — cf.
    lesson 2026-04-29 (TAO @ RSI 86.1 → −1.02R 21h later). The
    upper cap rejects late-stage momentum entries while preserving
    the >55 floor.

5a. Regime-confirmation gate: at entry-scan time, count universe
    pairs with positive 24h % change. If < 4 of 15 are positive,
    reject all new entries this wake. Lesson 2026-04-29: TAO entered
    when only 2/15 pairs were positive (TAO + XDG); divergent tape
    indicated non-confirmed regime, position reversed and stopped.

5b. Same-pair re-entry cooldown: do not open a new position in a
    pair within 24h of a stop-out (exit-stop-hit) on that pair.
    Lesson 2026-04-29: TAO was stopped 2026-04-27T05:00Z (cascade)
    and re-entered 2026-04-28T17:00Z (~36h later — outside cooldown,
    so this rule wouldn't have prevented it; included as
    forward-looking guard against tighter same-day re-entries).
```

### Evidence (trade-log)

- **TAO 2026-04-28T17:00Z entry → 2026-04-29T14:00Z stop:** RSI14 ≈ 86.1 at entry, only 2/15 universe pairs positive on 24h. Both warning signals were noted in `research_log.md` at entry-scan time but no rule consumed them. Result: −1.02R / −$64.37.
- **Cascade context:** the 4-position cluster stop on 2026-04-27 was already addressed by W18-A (cluster cap) and W18-C (one-per-wake). This proposal layers on top by catching late-stage / unconfirmed entries that pass the W18 filters.

### Risk assessment

- **Downside if adopted:**
  - 2a (RSI ≤ 80): rejects entries where momentum is already extended. May miss extension trades in clean trend days. Estimated 1-3 missed entries per month based on observed RSI distribution at recent entry-scans.
  - 5a (regime gate): in choppy regimes (≈half of 1H bars empirically) BULL takes no entries that wake. Frequency cost is real; this trades volume for hit rate.
  - 5b (cooldown): minor — same-day re-entries on stopped pairs are uncommon. Mostly a forward-looking guard.
- **Downside if NOT adopted:**
  - Continued exposure to climactic-RSI entries with poor expectancy. Each occurrence ≈ −1R.
  - No regime gate means BULL can open into divergent tape that historically chops out longs.
- **Upside:**
  - Removes the failure mode lesson 2026-04-29 specifically surfaced.
  - Synergy with W18: cluster cap (A) + one-per-wake (C) + regime gate (5a) form a coherent set — A/C limit *correlated* fills, 5a limits *poorly-timed* fills.

### Expected impact

- TAO 2026-04-28T17:00Z entry would have been rejected on TWO grounds (RSI 86 > 80 AND 2/15 < 4/15 positive). −$64.37 avoided.
- Win rate: expected to improve modestly (rejecting bottom-quartile entry conditions).
- Frequency: expected −20% to −30% entries per week. Acceptable for v0.1 — BULL is not entry-starved.

### Calibration notes

- RSI cap of **80** chosen because TAO entry was 86.1 and historical 80+ readings on 1H BTC/ETH have ≈40% win rate (back-of-envelope, not backtested). Could tighten to 75 or loosen to 85 — 80 is the conventional threshold.
- Regime gate threshold of **4/15** is one-quarter of universe positive. Could tighten to 5 or 6 with more evidence. 4 is a soft lower bound — anything tighter and we'd have rejected legitimate entry days.
- Cooldown of **24h** matches the bar-frequency BULL operates at. Could extend to 48h.

---

## Proposal E — Research_log analyst-role split + news pass

### Current convention

`memory/research_log.md` records entry-scan output as a single flat block per wake: candidates, RSI/EMA values, decision. No structure, no news, no sentiment.

### Proposed convention (process change, no strategy rule)

Each routine wake's research entry uses the following sub-sections:

```markdown
## YYYY-MM-DDTHH:MMZ — routine-NN-<name>

### Technical (rule-driven, deterministic)
- Per-pair RSI14, 1H/4H EMA state, 4H regime, ATR14
- Pass/fail per entry rule (1, 2, 2a, 3, 4, 4a, 5, 5a, 5b, 6, 6a, 7, 8)
- Final candidate list

### News (Firecrawl-driven, informational only in v0.1)
- For each candidate, scan headlines from 2 sources
  (e.g. coindesk.com, theblock.co) tagged with the pair's base
  asset over the past 6h
- Record: top 3 headlines + 1-line summary each
- Tag: "neutral / supportive / contradictory" relative to long bias
- **Does NOT veto entries in v0.1** — informational only

### Sentiment (passive — Kraken depth/spread proxy in v0.1)
- For each candidate, record bid/ask spread bps + top-of-book depth
  via Kraken MCP `kraken_spread` and `kraken_depth`
- Wide spread or thin depth = sentiment caveat, recorded but no veto

### Decision
- Final action this wake (OPEN / SKIP / HOLD)
- Cite which rule(s) drove the decision
```

### Why this is Ring 1 (process-only)

This proposal does NOT add or modify any rule in `strategy.md`. It restructures *how* `research_log.md` is written and adds a Firecrawl call per candidate. The trade decision still flows through deterministic strategy rules — News and Sentiment sections are evidence collection, not decision authority.

The mandate explicitly allows news awareness. v0 strategy ignores it. This proposal moves the *infrastructure* into place without yet wiring it into a rule.

### Why it matters

- **Fills the mandate gap.** v0 deliberately ignores news; lesson-mining requires having news data to mine.
- **Powers future Ring-2 proposals.** Once we have N weeks of "headline at entry vs. trade outcome" data, we can propose evidence-backed rules like "reject entries when news section tags 'contradictory'" — backed by actual stats instead of vibes.
- **Borrows TradingAgents' best idea minus the LLM-vibe risk.** Their analyst-role split is the structurally interesting piece; their LLM-debate decision authority is the part BULL should NOT borrow.

### Cost / risk

- Adds ~30s per routine wake for Firecrawl calls (5-8 candidate pairs × 2 sources). Acceptable.
- Firecrawl API budget: ~10 calls per wake × 4 wakes/day × 7 days = 280 calls/week. Within reasonable monthly Firecrawl plan.
- Failure mode: if Firecrawl fails, news section logs `Firecrawl unavailable` and routine continues. Existing kill-switch covers this (per `guardrails.md` Ring 3: MCP failure → skip routine).

### What this proposal does NOT do

- Does not gate trades on news (no Ring-2 rule change).
- Does not introduce LLM-judgment trade decisions.
- Does not change `strategy.md`.
- Does not change kill switches or risk caps.

---

## What this proposal does NOT change

- All risk caps, position caps, stop distances, take-profit, exit rules.
- Concept buckets (`momentum: 100%`).
- Universe size or composition.
- Any guardrail in `guardrails.md`.
- Routine schedule.

## Application path

If approved (Telegram `[Y]`):

1. Routine #5 next Sunday (2026-05-03) reads this memo and applies:
   - **D:** edits `memory/strategy.md` § Entries to add rules 2a, 5a, 5b
   - **E:** edits `memory/research_log.md` header with new schema convention; updates routines #1 and #2 markdown to write the new sections
2. Lesson 2026-04-29 in `memory/lessons.md` updated from `active` to `superseded` (Proposal D addresses it).
3. Existing/new positions: no retroactive effect; rules apply to new entry-scans only.

If rejected (Telegram `[N]` or 24h timeout):

1. Memo archived.
2. Lesson 2026-04-29 remains active.
3. Next routine #4 (Saturday 2026-05-02) re-evaluates D with TradingView backtest evidence. E can be re-proposed independently.

If partial (`[Y D]` or `[Y E]`):

- D and E are independent. Either can be approved without the other.
- Inside D, the three sub-rules (2a, 5a, 5b) are tightly coupled but separable — `[Y D-2a only]` is a valid response.

## Honest caveats

- **No backtest.** Same caveat as W18. RSI cap of 80, regime threshold of 4/15, cooldown of 24h — all chosen by reasoning from one trade. Saturday's routine #4 with TradingView harness would tighten these numbers.
- **Sample size: 1.** Lesson 2026-04-29 is a single trade. Could be noise. Counter: the warning signals were *visible at entry-scan time*; rejecting them costs little even if the lesson is partially noise.
- **E increases routine wall-clock time.** Firecrawl adds latency. Acceptable, monitor.
- **E without D = data without action.** If only E is approved, BULL collects news/sentiment data but does nothing with it. Still useful (powers future proposals), but the immediate trade behavior doesn't change.
- **TradingAgents framework comparison was the catalyst, not the source of evidence.** The actual evidence trail is BULL's own lesson 2026-04-29. The video provided framing.

## Decision

User reply via Telegram (or chat-channel equivalent):
- `[Y]` — apply both proposals at next routine #5
- `[Y D]` or `[Y E]` — apply selected only
- `[Y D-2a]` etc. — apply specific sub-rule only
- `[N]` — reject, lesson 2026-04-29 stays active
- (no reply within 24h) — auto-rejected per mandate

---

*Drafted 2026-04-29T at user request after analysis of `https://www.youtube.com/watch?v=9FoEsXNGLwI` (TradingAgents framework). Comparative analysis preserved in chat transcript; this memo records only the BULL-specific actionable proposals.*
