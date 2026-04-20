# Skill: News & Research

Used by routine #1 to scan for material news on universe pairs. Mandate allows news-reactive trading; v0 seed ignores it, but lessons.md captures patterns for future strategy proposals.

## When

- Routine #1 Overnight (06:00 PT): **mandatory** scan
- Routine #4 AutoStrategy (Sat): optional deeper dive if a variant proposal is news-related
- Other routines: do NOT run news — too token-expensive

## How (Firecrawl)

Use the Firecrawl skill (`firecrawl:firecrawl`) via Skill tool, OR shell out via the CLI.

Target sources (in priority order):
1. CoinDesk front page — crypto-specific headlines
2. The Block front page
3. Twitter/X searches for universe pairs — **skip in v1** (rate limits, noisy)
4. A specific pair's Kraken status page if anomaly detected in price

## Scan procedure

```
1. Fetch CoinDesk + TheBlock front pages via firecrawl
2. Extract headlines + publish timestamps from last 24h only
3. For each headline:
   a. Does it mention a universe-pair base asset (BTC, ETH, SOL, etc.)?
   b. Is it market-moving category? (hack, listing, delisting, regulatory, major partnership, macro Fed/SEC)
   c. If yes + yes: flag as ACTIONABLE, append to research_log.md
4. Compile a <=300-word digest for Telegram if 1+ ACTIONABLE items
5. If 0 ACTIONABLE items: write a one-line "nothing material" to research_log.md, Telegram silent
```

## Output to research_log.md

Schema rows in `research_log.md`:

| 2026-04-21T13:00:00Z | overnight | coindesk.com | "SEC approves spot ETH ETF" | ETH universe-pair impact, flagged ACTIONABLE | no action v0 (long-only, no news rule yet) |

## Lesson extraction

After 3+ ACTIONABLE news items in a week for a single pair:
- Append a lesson to `lessons.md` with title "news cluster: <pair>"
- This feeds routine #4 when it decides whether to propose a news-reactive rule

## Hard rules

- No financial advice generation. Facts + impact classification only.
- No market-making off pre-release rumors. Only post-publish headlines.
- No position sizing off news in v1 (mandate allows, seed v0 ignores). Store the signals, don't act on them until strategy.md v1+ proposes a news rule.
