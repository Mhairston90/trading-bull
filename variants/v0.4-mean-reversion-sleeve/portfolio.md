# Variant v0.4-mean-reversion-sleeve — Synthetic Portfolio

> **Paper-paper account.** Synthetic $10K starting equity.
> **Last rebuild:** 2026-06-12T05:00Z (routine-07 wake 2026-06-11 22:00 PT — 0 trades; see notes)

## Account

- Starting equity: **$10,000.00**
- Cash: **$10,000.00**
- Realized PnL (variant lifetime): **$0.00**
- Unrealized PnL: **$0.00** (no open positions)
- Position values (MTM): **$0.00**
- Current equity: **$10,000.00**
- Equity peak: **$10,000.00**
- Drawdown from peak: **0.00%**

## Open positions

(none)

Portfolio risk-at-moment: **0.00%** (cap 4%).
Open positions: **0 / 2** (variant max-concurrent 2 — mean-reversion sized smaller than momentum).

## Active kill-switch state

- Daily realized: **0.00%** (cap 5%)
- Consecutive losing trading days: 0 (cap 7)
- Max drawdown: 0.00% (cap 25%, warn 12.5%)
- Equity floor: $10,000 > $7,500 floor — OK
- **All clear.**

## Rolling performance vs main BULL v0.2

| Window | v0.4 return | v0.2 main return | Delta | BTC-hold | Result |
|--------|-------------|------------------|-------|----------|--------|
| 7d  | 0.00% | — | — | −3.01% (BTC 7d) | v0.4 in cash; BTC fell 3.01% over 7d (May 22→29) |
| 30d | 0.00% | +6.63% (main since Apr 29) | −6.63% | −3.39% (BTC Apr 29→May 29: $75,750→$73,183) | MAIN AHEAD; 0 trades — NOT promotion-eligible (need ≥10 in 30d) |
| 90d | — | — | — | — | not yet 90 days live |

## Days live

- Spin-up: 2026-04-29
- As of last rebuild: **44 days**
- Promotion-eligible date: **2026-05-29 (reached)** — 0 trades lifetime (need ≥10 in rolling 30d) → NOT promotion-eligible

## Notes

Tests whether BULL's mandate-allowed-but-unused mean-reversion bucket adds edge uncorrelated to momentum. Looks for oversold bounces (RSI < 25) in pairs whose 4H trend is structurally bullish. Variant-internal bucket allocation is `mean-reversion: 100%`; main BULL bucket allocation in `memory/strategy.md` is unchanged at `momentum: 100%`.

### Routine #7 wake log

- **2026-05-12 22:00 PT** — past-24h replay window = 2026-05-11 16:00 UTC → 2026-05-12 16:00 UTC. EOD-prior (04:00 UTC) lowest 1H RSI was TRX/USD 33.0 — no pair hit M2 RSI<25. OVERNIGHT (13:00 UTC) FARTCOIN/USD reached 20.9 RSI but failed M1 (insufficient 4H history for 200-EMA on a meme listing); other low-RSI pairs (PENGU 25.4, ETH 26.0) above the <25 threshold. Result: 0 entries, 0 open positions. All kill switches clear at $10,000 equity.
- **2026-05-16 22:00 PT (this wake)** — past-24h replay window = 2026-05-15 10:00 UTC → 2026-05-16 10:00 UTC. Wakes evaluated: OVERNIGHT (2026-05-15 13:00 UTC), MIDDAY (2026-05-15 20:00 UTC, default-skip), EOD (2026-05-16 04:00 UTC). M3 (reversal candle: 1H close > open) **failed for all 15 universe pairs at BOTH eligible wakes** — the 05-15 13:00Z bar was a synchronized red crash bar (HYPE flat, rest red) and the 05-16 04:00Z bar was red universe-wide in the continued risk-off tape. M3 blocks before M2 RSI-floor is reached, so the variant took 0 entries regardless of RSI. 0 open positions to exit. All kill switches clear at $10,000 equity.
- **2026-05-29 22:00 PT** — past-24h replay window 2026-05-29 05:00 UTC → 2026-05-30 05:00 UTC. Kraken MCP OK (BTC/USD $73,183). Wakes evaluated: OVERNIGHT (2026-05-29 13:00 UTC), MIDDAY (default-skip), EOD (2026-05-30 04:00 UTC). At OVERNIGHT: M3 (reversal candle: 1H close > open AND close > prior low) failed for all sampled pairs — the 1H bar closing at 13:00 UTC was red for BTC, SOL, HYPE, TAO, ADA, SUI. At EOD: M3 passed for BTC/SOL/HYPE/TAO/ADA; M2 (RSI < 25) failed for all — computed RSI: BTC≈55, SOL≈59, HYPE≈75, TAO≈50, ADA≈58, far from oversold. 0 entries. No open positions. All kill switches clear at $10,000 synthetic equity. **30-day time threshold reached this wake.** 0 trades in rolling 30d window (need ≥10) → NOT promotion-eligible; variant continues in LAB.
- **2026-05-30 22:00 PT** — replay window 2026-05-30T05:00Z → 2026-05-31T05:00Z. Kraken MCP OK (BTC/USD $74,078). Wakes evaluated: OVERNIGHT (13:00Z 2026-05-30), MIDDAY (default-skip), EOD (04:00Z 2026-05-31). OVERNIGHT: M3 check at 13:00Z — HYPE 1H bar was red (open 68.34, close 68.06); BTC green but RSI BTC ~62 >> 25 threshold; TAO RSI ~59 >> 25. M2 (RSI < 25) failed all pairs — market in recovery/rally mode, no pairs approaching oversold. EOD: M3 passed for several pairs (BTC/SOL/TAO/HYPE green bars); M2 (RSI < 25): BTC RSI ~70, SOL RSI ~65+, HYPE RSI ~60 — none near oversold per recovery RSI levels consistent with main portfolio EOD analysis. 0 entries. Kill switches all clear at $10,000. Days live: **32**.
- **2026-06-10 22:00 PT** *(partial-run — header/days updated but wake-log not written; retroactively captured here)* — 7-day cap replay (last rebuild 2026-05-31T05:00Z; gap 11 days → cap to 2026-06-04T05:00Z → 2026-06-11T05:00Z). Crash wakes 06-04T13:00Z → 06-06T20:00Z: SBD active (0-1/15 positive) → 5a FAIL; M3 also failed (red bars in crash). Recovery wakes 06-07T04:00Z → 06-09T04:00Z: 5a PASS; M3 green for some pairs; M2 (RSI < 25): recovering RSI 55-75 across board — no pair approaching oversold. Post-recovery 06-09T13:00Z → tonight: SBD active (1/15 positive BTC at EOD 06-11T04:00Z, median −2.30%) → 5a FAIL. **0 entries across 7-day cap window.** Book flat. Kill switches clear at $10,000.
- **2026-06-11 22:00 PT** — replay window 2026-06-11T05:00Z → 2026-06-12T05:00Z (24h). Kraken MCP OK (BTC/USD $62,563; 4H OHLCV unavailable — connection error). Wakes evaluated: OVERNIGHT (2026-06-11T13:00Z), MIDDAY (default-skip), EOD (2026-06-12T04:00Z). **OVERNIGHT 2026-06-11T13:00Z:** SBD active (confirmed by flanking bookends) — mean-rev variants ignore 5a by design, but M3 check (reversal candle): red/mixed bars in declining tape → M3 FAIL → 0 entries. **EOD 2026-06-12T04:00Z:** 5a PASS, SBD CLEARED (major regime flip — 15/15 positive, median +2.72%). M3 PASSES (green bars in 15/15 positive bounce ✓). M2 (RSI < 25 for v0.4): BTC 1H RSI ~57.9 — far above 25 threshold. Full 15/15 positive tape → no pair near oversold. M1 (4H close > 4H 200-EMA): uncertain (4H API unavailable); post-10-day crash, most pairs likely below their 200-EMAs. **0 entries.** Exit replay no-op (book flat). Kill switches all clear at $10,000. Days live: **44**.
