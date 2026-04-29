# BULL Idea Sources — curated quants & researchers

> **Purpose:** input list for routine #6 (idea-scan). Each source is content that BULL ingests weekly to surface candidate strategy ideas. **No source on this list has authority over BULL's trades.** They feed the idea bank, which feeds memo drafting, which feeds the Ring-2 `[Y/N]` channel.
> **Cadence:** reviewed quarterly. Add/remove sources via off-cycle proposal or routine #4.
> **Scoring inputs:** for each source we record `signal-quality` (1-5) and `bull-fit` (1-5) so routine #6 can weight harvested ideas.

## Selection criteria

A source is on this list iff:
- Publicly accessible content (no paywall-only)
- Substack, blog, or X long-form
- Methodology, on-chain data, or specific testable claims — not pure-TA chart drawings
- At least monthly publication
- BULL-relevant scope: spot crypto, OR factor/quant methodology that translates to crypto

Sources that fail any of the above get cut.

## Active sources (10)

| # | Name | Channel | URL | Scope | Signal | Fit | Notes |
|---|------|---------|-----|-------|--------|-----|-------|
| 1 | Arthur Hayes | Substack | https://cryptohayes.substack.com/ | Crypto macro, specific BTC/ETH/alt setups | 4 | 4 | High signal but verbose; extract concrete trade theses only |
| 2 | Willy Woo | Substack + X | https://woocharts.com/ , @woonomic | On-chain BTC valuation, NVT, threshold signals | 4 | 4 | Quantified thresholds — easy to translate to rules |
| 3 | Robot James / Robot Wealth | Substack | https://robotwealth.com/blog/ | Quant setups, mean-reversion + momentum | 5 | 4 | Methodology gold, occasionally crypto-specific |
| 4 | Glassnode Insights | Substack | https://insights.glassnode.com/ | On-chain reports with explicit thresholds | 5 | 5 | Direct rule candidates (e.g. SOPR, reserve risk) |
| 5 | CryptoQuant / Ki Young Ju | Substack + X | https://cryptoquant.com/insights , @ki_young_ju | Exchange flows, miner reserves | 4 | 4 | Sometimes too short-form; rate-limit harvest |
| 6 | Coin Metrics | Substack | https://coinmetrics.substack.com/ | Weekly on-chain dashboards | 4 | 4 | State of the Network is the high-yield piece |
| 7 | Marcos López de Prado | X + papers | https://www.linkedin.com/in/lopezdeprado/ , @lopezdeprado | Quant methodology, ML-finance | 5 | 3 | Methodology heavy, asset-agnostic — translate, don't copy |
| 8 | Corey Hoffstein / Newfound | Substack | https://blog.thinknewfound.com/ | Factor research, return stacking | 4 | 3 | Equities-leaning; harvest factor ideas applicable to crypto |
| 9 | Ari Paul | X | https://x.com/AriDavidPaul | Practitioner views, occasional setups | 3 | 4 | Lower signal density — harvest only when he posts long-form |
| 10 | Lyn Alden | Substack | https://www.lynalden.com/articles/ | Macro framing, BTC stance | 4 | 3 | Macro context, rarely a direct rule — informs regime view |

## Excluded sources (reference — do not harvest)

To keep the harvest signal-dense, the following are explicitly NOT on the list. Document why:

- **Pure-TA chart twitter** (CredibleCrypto, CryptoBullet1, etc.) — high noise, no methodology
- **Maxis / influencers without published analysis** — vibes only
- **Paywalled-only services** (Delphi premium, Messari pro) — Firecrawl can't access
- **Telegram-group leakers** — unreliable provenance
- **YouTube-only chartists** — transcript extraction is lossy and TA-heavy

If a future source qualifies for inclusion, propose via routine #4 weekly memo with `signal` and `fit` scores.

## Refresh policy

- Routine #4 (Saturday) reviews `idea_bank.md` for source-level performance: which sources produced ideas that survived to proposal stage?
- Quarterly (every 13 weeks): re-score `signal` and `fit`, drop sources scoring < 6 combined, propose replacements.
- Source becomes paywalled / dies / pivots → flag in routine #4, drop next week.
