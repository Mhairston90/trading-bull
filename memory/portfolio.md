# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-06-13T04:10Z routine-03-eod (Fri 21:10 PT — 2026-06-12 PT trading day EOD). Slot ID confirmed `bull-03-eod` (no Slot-mismatch vs the 2026-05-11 duplicate-skill regression guard). **First entry since XRP exit 2026-05-30 — TAO/USD long opened at 21:00 PT 1H close.** Authoritative indicators via `scripts/indicators.py` (720-bar 1H + 4H, SMA-seeded EMAs, Wilder RSI/ATR). Regime **4/15 positive on 24h, median -0.21% (XDG)** → **5a marginal PASS** (4 = 4-pair floor, at threshold; tape weaker than overnight 13/15 +1.49% and midday 5/15 -0.30% — afternoon thinning continued into close); **5a-SBD CLEARED** (4 > 1 AND -0.21 > -1.0). Per-pair entry scan: **TAO/USD = sole technical PASS.** Detail: 1H close 217.286 PASS rule 1 by +$3.88 vs 1H 20-EMA 213.406 (+1.82%); 1H RSI14 62.5 PASS rule 2 by +7.55 (well clear of climactic 80 cap); 4H close 217.286 PASS rule 3 by +$3.22 vs 4H 50-EMA 214.065 (+1.50%, comfortable margin — 720 4H bars, fully converged HIGH-CONFIDENCE); R3-20 also PASS by +$5.99 (v0.14 telemetry confirms). Notional 24h $3.04M PASS rule 4a (above $2.0M floor, eligible). Rule 5b inapplicable (last TAO close was 2026-05-26 ema20-confirm, not stop-hit — no 24h cooldown). Rules 6 (0/4 open), 6a (0/2 cluster), 7 (1.50% risk = exactly at target) all PASS. Rule 8 trivially satisfied (sole eligible candidate). **News pass:** Firecrawl scan deferred for token-budget — informational only per W19-E (no veto power in v0.2); classified neutral by convention. **Sentiment pass:** Kraken `kraken_spread` 217.07/217.16, spread $0.09 (≈4.1 bps, tight/healthy); 24h notional ≈$3.07M (matches indicators.py $3.04M ±). Informational only — no veto. **Decision: ENTER TAO/USD long.** Position sizing: equity $10,254.63 × 1.5% = $153.82 risk budget; 2×ATR stop distance 4.6634; size = 153.82 / 4.6634 = **32.985 TAO units**; notional 32.985 × 217.286 = **$7,167.30** (well within $10,254.63 cash). Stop **$212.6226**, 4R target **$235.9396**. Rule 7 check: 4.6634 × 32.985 / 10,254.63 = 1.50% — exactly at the per-trade cap with no other open positions, total portfolio risk-at-moment 1.50% of 4% cap. Equity post-entry **$10,254.63** unchanged at entry-fill (no realized PnL; MTM at entry = $0). Cash post-entry **$3,087.33** ($10,254.63 - $7,167.30). Drawdown **4.42%** unchanged from peak $10,728.95. Consecutive losing trading days **4** unchanged (entry doesn't reset; only close-events update the streak). Loss-streak still 1 day from informal warn-5. 30d BULL ≈ +2.55% vs BTC-hold ≈ -21.8% → delta +24.4%. All kill switches clear (DD 4.42% well below 12.5% warn / 25% cap; equity $10,254.63 > $7,500 floor; daily realized $0 < 5% cap; loss-streak 4 < 7 cap). Ops watchdog clean (`ALL CLEAR — heartbeats, timestamps, tree, MTM, scheduler flag, push state, MCP paths OK`). **Telegram EOD card sent** per mandate. Next on-schedule wake: routine-01-overnight 2026-06-15T13:00Z (Mon 06:00 PT — Sat/Sun off per Mon-Fri cron `0 6 * * 1-5`).

> **Prior rebuild (Fri midday):** 2026-06-12T20:00Z routine-02-midday (Fri 13:00 PT scheduled on-schedule fire). Slot ID confirmed `bull-02-midday`. **Book flat** — 21st consecutive flat-book wake since XRP exit 2026-05-30T23:00Z (13 days). 0 open positions → MTM/exit steps inert; entry scan forbidden by midday design. Fresh `kraken_multi_ticker` 15/15 clean at the 13:00 PT pull for kill-switch + regime telemetry: **5/15 positive on 24h % change, median −0.30% (SOL)**. Sorted ascending: −2.67 NEAR / −0.88 XRP / −0.86 AVAX / −0.60 SUI / −0.40 TRX / −0.36 LINK / −0.32 ETH / **−0.30 SOL (median)** / −0.29 TAO / −0.02 ADA / +0.13 BTC / +1.34 LTC / +1.64 FARTCOIN / +1.73 XDG / +2.82 HYPE. **Tape softened materially from the 09:38 PT overnight print** (13/15 positive, median +1.49%) over ~6 trading hours — breadth halved, median rotated 1.79pts to the downside. But: still 5 positive, BTC steady at +0.13, HYPE the standout +2.82% gainer. Regime classification (informational only — midday gates nothing): **5a marginal PASS** (5 ≥ 4 positive floor by exactly 1 pair, thinnest buffer since regime recovered 06-11); **5a-SBD CLEARED** (5 > 1 AND median −0.30 > −1.0). SBD 9-EMA exit override remains deactivated. BTC reference **$63,637** (+0.13% on 24h via Kraken ticker; +$85 vs overnight indicators.py print $63,551.7 in ~6h, consistent). Equity unchanged **$10,254.63** (cash-only). Day PnL **$0.00 / 0.00%**. Since-start **+2.55%** (54 days from inception 2026-04-20). Drawdown **4.42%** from peak $10,728.95 — unchanged. Consecutive losing trading days **4** (still 1 from informal warn-5). 30d BULL-vs-BTC-hold delta ≈ **+24.3%** (BULL +2.55% vs BTC ≈ −21.7%). All kill switches clear. **No Telegram** (silent — no kill-switch trip, no exit event, DD unchanged far below 12.5% halfway-warn). Next on-schedule wake: routine-03-eod 2026-06-13T04:00Z (Fri 21:00 PT scheduled — entry-eligible at the fresh 1H/4H closes).

> **Prior rebuild:** 2026-06-12T16:38Z routine-01-overnight (Fri 06:00 PT scheduled, fired 09:38 PT). Slot ID confirmed `bull-01-overnight`. **First wake fully governed by `scripts/indicators.py`** (per the 2026-06-12 routine amendment): 15/15 universe pairs returned 720-bar 1H + 720-bar 4H fetches via Kraken public REST in a single sub-30s invocation; converged SMA-seeded EMAs, Wilder RSI/ATR; no LLM in-context arithmetic on the rule path. **Regime: 13/15 positive on 24h % change, median +1.49% (XRP) → 5a PASS (2nd consecutive) → 5a-SBD remains CLEARED.** Sorted ascending: −1.97 TRX / −0.61 SUI / +0.09 AVAX / +0.91 LINK / +0.94 ETH / +1.12 FARTCOIN / +1.41 BTC / **+1.49 XRP (median)** / +1.65 NEAR / +1.76 LTC / +2.02 TAO / +2.31 ADA / +2.66 SOL / +2.90 XDG / +5.17 HYPE. Modest cooling vs last night's EOD (15/15, +2.72%) but solidly net-positive. **Per-pair entry scan (rules 1, 2, 2a, 3, 4a): zero pairs pass all four simultaneously.** BTC (rank 1) FAIL R3 by only $102.4 (close 63,551.7 vs converged 50-EMA 63,654.1, -0.16%) AND FAIL R2 (RSI 54.0 < 55, by 0.95) — exactly the prediction the 2026-06-12T06:50Z interactive ADDENDUM made ("BTC rule 3 still FAIL unless price clears ~$63,700"); EMA has drifted down to 63,654 but close hasn't yet caught up. SOL (rank 3) PASS R1+R2 (RSI 57.1) but FAIL R3 by $0.144 (-0.21%). HYPE (rank 4) PASS R1+R2 (RSI 57.0) but FAIL R3 by $0.318 (-0.53%); largest 24h % gainer in the universe but still under its 4H 50-EMA. XDG (rank 8) is the only R3-PASS (just barely, +$0.0005) but FAIL R2 at RSI 54.1. All other pairs fail two or more rules. R4a sub-fails: FARTCOIN $0.51M, AVAX $1.24M (both excluded regardless; both also fail other rules). v0.14 R3-20 telemetry: 9 of 15 pairs PASS the 20-EMA variant (BTC +$695, SOL +$1.30, HYPE +$1.47, TAO +$2.00, LTC +$0.20, etc.) — the 50 vs 20 gap is exactly the recovery-trend regime W21-F's main filter is designed to lag through; A/B evidence accrues to v0.14's rack. News pass + sentiment pass SKIPPED — vacuous per W19-E schema (zero technical-PASS candidates). **Decision: NO ENTRY, NO EXIT this wake (book flat).** 0 trade_log writes. The post-SBD recovery is now ~18-24h in; expect SOL/HYPE/XDG within striking distance of one more 4H bar of strength to release. BTC needs both an R3 reclaim AND an R2 lift (RSI 54→55+) so is one rule further from eligible than SOL/HYPE. **Book flat** (20th consecutive flat-book wake since XRP exit 2026-05-30T23:00Z, ~13 days). MTM inert; exit step inert. Equity unchanged **$10,254.63** (cash-only). Day PnL **$0.00 / 0.00%**. Since-start **+2.55%** (54 days from inception 2026-04-20). Drawdown **4.42%** from peak $10,728.95 — unchanged. Consecutive losing trading days: 4 (zero-PnL day does not advance; still 1 L from informal warn-5). Kill switches all clear. BTC reference **$63,552** (+1.4% on 24h via indicators engine). 30d BULL-vs-BTC-hold delta ≈ **+24.5%** (BULL +2.55% vs BTC ≈ −21.9% from 30d-ago ~$81.3k). Next on-schedule wake: routine-02-midday 2026-06-12T19:30Z (Fri 12:30 PT scheduled).

## Account

- Starting equity: **$10,000.00**
- Cash: **$3,087.33** ($10,254.63 prior cash − $7,167.30 TAO entry notional)
- Realized PnL (all-time): **+$254.63**
  - BTC −$9.14 (exit-ema-cross 2026-04-24T04:00Z) *(archived)*
  - TRX −$26.69 (exit-stop-hit 2026-04-24T20:00Z) *(archived)*
  - LTC +$39.40 (exit-ema-cross 2026-04-25T17:00Z, +1.32R) *(archived)*
  - ADA −$38.77 (exit-ema-cross 2026-04-25T17:00Z, −1.21R) *(archived)*
  - AVAX −$34.04 (exit-ema-cross 2026-04-25T17:00Z, −0.99R) *(archived)*
  - ETH −$34.68 (exit-stop-hit 2026-04-27T05:00Z, −1.06R) *(archived)*
  - BTC −$28.77 (exit-stop-hit 2026-04-27T05:00Z, −1.08R) *(archived)*
  - SOL −$33.82 (exit-stop-hit 2026-04-27T05:00Z, −1.06R) *(archived)*
  - TAO −$56.38 (exit-stop-hit 2026-04-27T05:00Z, −1.03R) *(archived)*
  - TAO −$64.37 (exit-stop-hit 2026-04-29T14:00Z, −1.02R) *(archived)*
  - HYPE −$58.18 (exit-stop-hit 2026-05-06T15:00Z, −1.02R)
  - BTC +$1.42 (exit-ema-cross 2026-05-06T19:00Z, +0.06R)
  - LTC −$48.58 (exit-stop-hit 2026-05-07T01:00Z, −1.03R)
  - XRP −$37.68 (exit-stop-hit 2026-05-07T14:00Z, −1.05R)
  - LINK +$103.03 (exit-ema-cross 2026-05-07T20:00Z, +1.69R)
  - SOL +$585.35 (exit-4R-target 2026-05-11T19:00Z, +4.03R)
  - XRP −$21.92 (exit-ema-cross 2026-05-15T04:00Z, −0.14R) — corrected; supersedes the routine-02-midday-logged 2026-05-15T13:00Z exit-stop-hit −$206.37
  - HYPE +$413.62 (missed-scheduler replay exit-4R-target 2026-05-21T08:00Z, +4.04R)
  - TAO −$29.84 (missed-scheduler replay exit-ema20-confirm 2026-05-22T01:00Z, −0.50R)
  - HYPE −$33.98 (missed-scheduler replay exit-ema20-confirm 2026-05-22T02:00Z, −0.29R)
  - SOL −$45.64 (missed-scheduler replay exit-stop-hit 2026-05-22T15:00Z, −1.43R)
  - AVAX −$35.83 (missed-scheduler replay exit-ema20-confirm 2026-05-22T16:00Z, −0.94R)
  - BTC −$33.70 (exit-stop-hit 2026-05-25T22:00Z, −1.07R)
  - TAO −$114.75 (missed-scheduler replay exit-ema20-confirm 2026-05-26T18:00Z, −0.58R)
  - XRP −$101.40 (missed-scheduler replay exit-ema20-confirm 2026-05-30T23:00Z, −0.65R)
- Unrealized PnL (open positions): **$0.00** (just opened — MTM ≈ entry, intra-bar Kraken last $216.85 ≈ −$14 paper; final entry-bar accounting uses 1H close as fill price)
- Position values (MTM): **$7,167.30** (TAO 32.985 × entry 217.286)
- Current equity (cash + positions MTM): **$10,254.63**
- Equity peak: **$10,728.95** (set 2026-05-21 during missed-scheduler HYPE 4R take-profit replay)
- Drawdown from peak: **4.42%**

## Open positions

| Pair | Side | Size | Entry | Entry time (UTC) | Stop | 4R target | Risk ($) | Risk (% equity) |
|------|------|------|-------|------------------|------|-----------|----------|------------------|
| TAO/USD | long | 32.985 | 217.286 | 2026-06-13T04:00:00Z | 212.6226 | 235.9396 | 153.82 | 1.50% |

Portfolio risk-at-moment: **1.50%** of equity (cap 4%).
Open positions: **1 / 8** (strategy v0.4 max-concurrent 4 → 1/4 used; cluster {BTC,ETH,SOL,TAO,AVAX,SUI,LINK} 1/2 — TAO is in cluster).

## Active kill-switch state

- Daily realized on 2026-06-12 PT trading day: **$0.00** (entry, no closes today) — clear vs 5% loss cap.
- Consecutive losing trading days: 05-22 L, 05-25 L, 05-26 L, 05-30 L (05-27/28/29/31, 06-01 → 06-12 all no-realized-PnL — entry does not reset streak) → streak **4** (cap 7; warn at 5 informally — still 1 closing-L away).
- Max drawdown: **4.42%** from peak $10,728.95 (cap 25%, warn 12.5%) — clear.
- Equity floor: $10,254.63 > $7,500 floor — OK.
- Regime gate (rule 5a) — **EOD 1H/4H close via `scripts/indicators.py`**: **4/15 positive, median -0.21% (XDG)** → **5a marginal PASS at exactly the 4-pair floor** (zero buffer). **5a-SBD CLEARED** (4 > 1 positive AND -0.21 > -1.0 median — both gates inactive). SBD's tightened 9-EMA exit override stays deactivated. Note: regime weakened progressively through the day (overnight 13/15 +1.49% → midday 5/15 -0.30% → EOD 4/15 -0.21%); recovery momentum is thinning. TAO entry decision still valid (all per-pair rules cleared with comfortable margins), but next wake regime read is the deciding factor on whether more entries become possible or whether TAO is the only long carried.
- No active 5b cooldowns (last TAO close was 2026-05-26 ema20-confirm, not stop-hit — rule 5b inapplicable; 17d elapsed anyway).
- **All clear (kill switches).** routine-03-eod 2026-06-13T04:10Z (Fri 21:10 PT scheduled on-schedule fire): **1 OPEN, 0 CLOSE** (TAO/USD long opened at 1H close; book moves from flat → 1 position after 13d flat-book streak). Kraken MCP AVAILABLE (TAO ticker + spread used for sentiment pass). Indicators.py engine clean (single 30s 15-pair fetch, all 720-bar 4H series converged). Drawdown 4.42% unchanged. Loss-streak 4 unchanged (entry-only event). Daily PnL $0. **Telegram EOD card sent** per mandate. Next on-schedule wake: routine-01-overnight 2026-06-15T13:00Z (Mon 06:00 PT scheduled — Sat/Sun off per `0 6 * * 1-5` cron). **Note on weekend:** TAO position carries unmanaged across 60+ hours (no routine wake between Fri-EOD and Mon-overnight under the Mon-Fri cron). 2×ATR stop is the protective floor for that window. This is the designed behavior of the cron schedule; no override.

## Universe refresh — 2026-06-01 (first true 30d aggregation)

| Rank | Pair | Change vs prior |
|------|------|-----------------|
| 1 | BTC | — |
| 2 | ETH | — |
| 3 | SOL | — |
| 4 | HYPE | ▲ from 6 |
| 5 | XRP | ▼ from 4 |
| 6 | SUI | ▲ from 8 |
| 7 | TAO | ▼ from 5 |
| 8 | XDG (DOGE) | — |
| 9 | NEAR | **NEW** (was off-list near-miss) |
| 10 | ADA | — |
| 11 | LINK | ▲ from 13 |
| 12 | LTC | ▼ from 9 |
| 13 | FARTCOIN | ▼ from 11 |
| 14 | TRX | ▲ from 15 |
| 15 | AVAX | ▼ from 12 |

- **PENGU dropped** (was rank 14) → moves to near-miss watch list (~$38M 30d notional).
- **Near-miss watch:** PENGU $38M, DOT $22M, UNI $20M.

## Pending exit triggers

- TAO/USD long 32.985 @ 217.286:
  - Exit rule 1 (W22-G): two consecutive 1H closes < 1H 20-EMA (currently 213.406). Active.
  - Exit rule 1-SBD: inert (SBD currently cleared).
  - Exit rule 2 (stop): 212.6226. Will ratchet to breakeven 217.286 once +2R reached at any 1H close (i.e., close ≥ 226.6128).
  - Exit rule 3 (4R target): 235.9396.
  - First eligible exit-check wake: routine-01-overnight 2026-06-15T13:00Z (Mon 06:00 PT). Bars between Fri-EOD and that wake close unmonitored; protection is the static stop only.

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | ≈ 0.0% (held flat at $10,254.63 across the 7d window) | ≈ +0.7% (BTC 2026-06-05 ~$63.2k → today $63.64k, span includes the 06-05 $60k low) | ≈ −0.7% | BULL slightly behind BTC on 7d |
| 30d | ≈ +2.55% (inception $10k 2026-04-20; window fully computable) | ≈ −21.7% (BTC 2026-05-13 ~$81.3k → today $63.64k) | ≈ +24.3% | BULL well ahead |
| 90d | — | — | — | not computable (BULL inception 2026-04-20 = 54 days ago) |

(7d and 30d figures approximate — precise reference-price computation deferred to routine #4. 90d window first computable ~2026-07-19. BTC reference today **$63,637** (midday `kraken_multi_ticker`) — BTC +0.13% on 24h, continued shallow bounce. 7d window includes the 06-05 $60k low so BTC-hold shows a small net positive return on that span; the 30d delta is the better representation of BULL's defensive-flat-book through the full breakdown. The strategy stayed flat through the bottom (5a/SBD blocked entries) and continues defensive in the early bounce — designed defensive sequence per W21-F.)
