# BULL Strategy — v0.4 (W22 amended 2026-05-20)

> **Gated file.** BULL may propose edits only via weekly memo → Telegram `[Y/N]`. Never edit autonomously.
> **Version:** v0.4
> **Last approved:** 2026-05-20 (off-cycle W22 proposal — G+H-partial: two-bar EMA exit confirmation + breakeven stop ratchet at +2R; user delegated choice via interactive chat "do whatever you suggest"; agent selected Option C: G + breakeven half of H, **4R take-profit retained per `feedback-perf-analysis-framing` memory**)
> **Prior versions:**
>   - v0.3 (2026-05-19 W21 — F: synchronized-breakdown classifier + Exit 1-SBD)
>   - v0.2 (2026-04-29 W19 — D: RSI cap + regime gate + re-entry cooldown)
>   - v0.1 (2026-04-28 W18 — A: cluster cap, B: liquidity floor, C: one-per-wake)
>   - v0-seed (2026-04-20 standup)
> **Next review:** routine #4, Saturday 2026-05-23

## Philosophy

Minimal momentum baseline. Long-only. One concept bucket (`momentum`). Expected to evolve in week 1.

## Universe

Read from `memory/universe.md` (top 15 Kraken USD pairs, refreshed monthly).

## Entries (long-only)

Enter LONG when **all** of the following are true on a just-closed 1H candle:

1. 1H close > 1H 20-EMA
2. 1H RSI(14) > 55
2a. **(W19-D)** 1H RSI(14) <= **80** at entry-scan close. Climactic readings (>80) have produced poor expectancy in mean-reverting tape — cf. lesson 2026-04-29 (TAO @ RSI 86.1 → −1.02R 21h later). The upper cap rejects late-stage momentum entries while preserving the >55 floor. Combined: entry requires **55 < RSI14 <= 80**.
3. 4H close > 4H 50-EMA
4. Pair has >= 10 candles of history on both 1H and 4H (no ultra-fresh listings)
4a. **(W18-B)** Pair has 24h notional volume >= **$2.0M USD** at time of entry-scan, measured from Kraken MCP `kraken_ticker`. Filters out thin-liquidity pairs whose 1H bars wick beyond 2×ATR stops (lesson 2026-04-24 TRX). Pairs currently affected: FARTCOIN, AVAX, LINK, PENGU, TRX (re-evaluated each entry-scan, not statically blocked).
5. No existing open position in this pair
5a. **(W19-D)** Regime-confirmation gate: at entry-scan time, count universe pairs with positive 24h % change. If **< 4 of 15** are positive, reject all new entries this wake. Lesson 2026-04-29: TAO entered when only 2/15 pairs were positive (TAO + XDG); divergent tape indicated non-confirmed regime, position reversed and stopped.
5a-SBD. **(W21-F)** Synchronized-breakdown sub-state: at entry-scan time, classify regime = **SYNCHRONIZED_BREAKDOWN** when **both** (i) **<= 1 of 15** universe pairs positive on 24h % change, **and** (ii) **median 24h % change across the 15 universe pairs <= −1.0%**. SBD is a strict subset of a 5a failure — the reject-all-new-entries behavior of 5a still applies unchanged. SBD **additionally** triggers the defensive trend exit (Exit rule 1-SBD). SBD is re-evaluated every wake and clears automatically when (i) or (ii) is no longer true. Origin: fragility audit 2026-05-19 — the contest's only paid edge was positioning for the 2026-05-12→05-17 synchronized breakdown; BULL is long-only by mandate and cannot take the offensive (short) side, but 5a-SBD captures the mandate-legal defensive half (stop bleeding open longs faster). Every wake SBD is active, `research_log.md` records the classification and an estimated avoided-give-back (open-position unrealized R at the 9-EMA exit vs. modeled 20-EMA exit) so the gate's defensive value is measured.
5b. **(W19-D)** Same-pair re-entry cooldown: do not open a new position in a pair within **24h** of a stop-out (`exit-stop-hit`) on that pair. Forward-looking guard against same-day re-entry chop.
6. Current open positions < 4 (v0 deliberately uses half the 8-position cap)
6a. **(W18-A)** Concurrent positions in the BTC-correlated cluster `{BTC, ETH, SOL, TAO, AVAX, SUI, LINK}` <= **2**. Empirically these pairs move together on 1H (cascade event 2026-04-27T05:00Z stopped 4/4 cluster positions in a single bar). Cap limits worst-case correlated tail loss to ~2R.
7. Portfolio risk-at-moment + this trade's risk <= 4%
8. **(W18-C)** Max **1** new entry per routine wake. If multiple pairs are eligible at the same wake, prefer the pair with **highest 30d notional rank** (i.e., XBT > ETH > SOL > TAO etc. per `memory/universe.md`). Remaining eligible entries re-evaluated at next wake; if no longer eligible (e.g., RSI dropped below 55), they are skipped — this is intentional, the rule is meant to prevent same-bar cluster fills.

## Position sizing

- Risk per trade: 1.5% of current equity
- Stop distance: 2 × ATR(14) on 1H
- Size = (equity × 0.015) / stop distance, rounded down to Kraken minimum lot

## Stop management (W22-H-partial, added 2026-05-20)

- At the close of each 1H candle, compute unrealized R = `(close - entry) / (entry - initial_stop)`.
- **Once unrealized R ≥ 2.0 at any 1H close, move the active stop from the original 2×ATR level UP TO THE ENTRY PRICE (breakeven).**
- The stop ratchets **up only** — once moved, it stays at breakeven for the life of the trade. This rule does not trail further beyond breakeven (a fuller trailing mechanism is a separate future change).
- Effect: a trade that has reached +2R unrealized can no longer become a realized loser (modulo round-trip friction; net result is a near-scratch close, not a stop-out at −1R).
- **Strictly risk-reducing** — only moves the stop closer to current price, never further away.
- Lesson source: `lessons.md` 2026-05-15 profit-give-back (score 9, XRP 2026-05-14 archetype: ran ~+2.8R, round-tripped to −0.14R). Paper-paper evidence track: `variants/v0.11-breakeven-2R/` (now subsumed by this main change).

## Exits

Exit the position when **any** of the following is true:

1. **(W22-G, modified 2026-05-20)** **Two consecutive 1H closes < 1H 20-EMA.** The exit fires on the close of the second below-EMA bar. A single-bar EMA tag-and-recover (`close[1] < EMA` AND `close[0] ≥ EMA`) does **not** trigger this exit. Lesson source: `lessons.md` 2026-04-24 commission-drag (score 8, 3 instances: BTC 2026-04-22, BTC 2026-05-05, XRP 2026-05-14 — each a small favorable move flipped to a small net loss by friction on a single-bar EMA cross). Paper-paper evidence track: `variants/v0.10-exit-confirm/` (now subsumed by this main change).
1-SBD. **(W21-F, W22-G amended)** While regime = SYNCHRONIZED_BREAKDOWN (per rule 5a-SBD), Exit rule 1 tightens to: **two consecutive 1H closes < 1H 9-EMA**. The same two-bar confirmation applies during SBD (SBD already implies multi-day persistence — one bar of additional patience adds modest adverse-motion budget without undermining SBD's defensive intent). Reverts to the 20-EMA two-bar exit automatically when SBD clears.
2. Price hits the active stop (initial 2×ATR level at entry, or entry price once breakeven ratchet has fired per the Stop management rule) — **unchanged by SBD**
3. Unrealized PnL ≥ 4R (take profit) — **unchanged by SBD, unchanged by W22.** Per `feedback-perf-analysis-framing` memory, the 4R tail is the designed payoff for a momentum strategy; the W22 proposal explicitly considered lowering to 3R (option D) and rejected that path. The 4R target stays.

Exits are checked at the close of each 1H candle. No intra-bar exits.

## Concept buckets declared

- `momentum`: 100%
- `mean-reversion`: 0%
- `news-reactive`: 0%

(These buckets are referenced by routine #5 allocation review. Shifts >20% between buckets are Ring 2 gated.)

## Known limitations of v0

- Long-only — misses downtrends
- Single entry signal — low diversity of edge
- No regime filter — will likely overtrade in chop
- No news awareness — mandate allows, v0 ignores

These are intentional. Routine #4 will propose upgrades with backtested evidence.
