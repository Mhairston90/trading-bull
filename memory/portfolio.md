# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-06-12T20:00Z routine-02-midday (Fri 13:00 PT scheduled on-schedule fire). Slot ID confirmed `bull-02-midday`. **Book flat** — 21st consecutive flat-book wake since XRP exit 2026-05-30T23:00Z (13 days). 0 open positions → MTM/exit steps inert; entry scan forbidden by midday design. Fresh `kraken_multi_ticker` 15/15 clean at the 13:00 PT pull for kill-switch + regime telemetry: **5/15 positive on 24h % change, median −0.30% (SOL)**. Sorted ascending: −2.67 NEAR / −0.88 XRP / −0.86 AVAX / −0.60 SUI / −0.40 TRX / −0.36 LINK / −0.32 ETH / **−0.30 SOL (median)** / −0.29 TAO / −0.02 ADA / +0.13 BTC / +1.34 LTC / +1.64 FARTCOIN / +1.73 XDG / +2.82 HYPE. **Tape softened materially from the 09:38 PT overnight print** (13/15 positive, median +1.49%) over ~6 trading hours — breadth halved, median rotated 1.79pts to the downside. But: still 5 positive, BTC steady at +0.13, HYPE the standout +2.82% gainer. Regime classification (informational only — midday gates nothing): **5a marginal PASS** (5 ≥ 4 positive floor by exactly 1 pair, thinnest buffer since regime recovered 06-11); **5a-SBD CLEARED** (5 > 1 AND median −0.30 > −1.0). SBD 9-EMA exit override remains deactivated. BTC reference **$63,637** (+0.13% on 24h via Kraken ticker; +$85 vs overnight indicators.py print $63,551.7 in ~6h, consistent). Equity unchanged **$10,254.63** (cash-only). Day PnL **$0.00 / 0.00%**. Since-start **+2.55%** (54 days from inception 2026-04-20). Drawdown **4.42%** from peak $10,728.95 — unchanged. Consecutive losing trading days **4** (still 1 from informal warn-5). 30d BULL-vs-BTC-hold delta ≈ **+24.3%** (BULL +2.55% vs BTC ≈ −21.7%). All kill switches clear. **No Telegram** (silent — no kill-switch trip, no exit event, DD unchanged far below 12.5% halfway-warn). Next on-schedule wake: routine-03-eod 2026-06-13T04:00Z (Fri 21:00 PT scheduled — entry-eligible at the fresh 1H/4H closes).

> **Prior rebuild:** 2026-06-12T16:38Z routine-01-overnight (Fri 06:00 PT scheduled, fired 09:38 PT). Slot ID confirmed `bull-01-overnight`. **First wake fully governed by `scripts/indicators.py`** (per the 2026-06-12 routine amendment): 15/15 universe pairs returned 720-bar 1H + 720-bar 4H fetches via Kraken public REST in a single sub-30s invocation; converged SMA-seeded EMAs, Wilder RSI/ATR; no LLM in-context arithmetic on the rule path. **Regime: 13/15 positive on 24h % change, median +1.49% (XRP) → 5a PASS (2nd consecutive) → 5a-SBD remains CLEARED.** Sorted ascending: −1.97 TRX / −0.61 SUI / +0.09 AVAX / +0.91 LINK / +0.94 ETH / +1.12 FARTCOIN / +1.41 BTC / **+1.49 XRP (median)** / +1.65 NEAR / +1.76 LTC / +2.02 TAO / +2.31 ADA / +2.66 SOL / +2.90 XDG / +5.17 HYPE. Modest cooling vs last night's EOD (15/15, +2.72%) but solidly net-positive. **Per-pair entry scan (rules 1, 2, 2a, 3, 4a): zero pairs pass all four simultaneously.** BTC (rank 1) FAIL R3 by only $102.4 (close 63,551.7 vs converged 50-EMA 63,654.1, -0.16%) AND FAIL R2 (RSI 54.0 < 55, by 0.95) — exactly the prediction the 2026-06-12T06:50Z interactive ADDENDUM made ("BTC rule 3 still FAIL unless price clears ~$63,700"); EMA has drifted down to 63,654 but close hasn't yet caught up. SOL (rank 3) PASS R1+R2 (RSI 57.1) but FAIL R3 by $0.144 (-0.21%). HYPE (rank 4) PASS R1+R2 (RSI 57.0) but FAIL R3 by $0.318 (-0.53%); largest 24h % gainer in the universe but still under its 4H 50-EMA. XDG (rank 8) is the only R3-PASS (just barely, +$0.0005) but FAIL R2 at RSI 54.1. All other pairs fail two or more rules. R4a sub-fails: FARTCOIN $0.51M, AVAX $1.24M (both excluded regardless; both also fail other rules). v0.14 R3-20 telemetry: 9 of 15 pairs PASS the 20-EMA variant (BTC +$695, SOL +$1.30, HYPE +$1.47, TAO +$2.00, LTC +$0.20, etc.) — the 50 vs 20 gap is exactly the recovery-trend regime W21-F's main filter is designed to lag through; A/B evidence accrues to v0.14's rack. News pass + sentiment pass SKIPPED — vacuous per W19-E schema (zero technical-PASS candidates). **Decision: NO ENTRY, NO EXIT this wake (book flat).** 0 trade_log writes. The post-SBD recovery is now ~18-24h in; expect SOL/HYPE/XDG within striking distance of one more 4H bar of strength to release. BTC needs both an R3 reclaim AND an R2 lift (RSI 54→55+) so is one rule further from eligible than SOL/HYPE. **Book flat** (20th consecutive flat-book wake since XRP exit 2026-05-30T23:00Z, ~13 days). MTM inert; exit step inert. Equity unchanged **$10,254.63** (cash-only). Day PnL **$0.00 / 0.00%**. Since-start **+2.55%** (54 days from inception 2026-04-20). Drawdown **4.42%** from peak $10,728.95 — unchanged. Consecutive losing trading days: 4 (zero-PnL day does not advance; still 1 L from informal warn-5). Kill switches all clear. BTC reference **$63,552** (+1.4% on 24h via indicators engine). 30d BULL-vs-BTC-hold delta ≈ **+24.5%** (BULL +2.55% vs BTC ≈ −21.9% from 30d-ago ~$81.3k). Next on-schedule wake: routine-02-midday 2026-06-12T19:30Z (Fri 12:30 PT scheduled).

## Account

- Starting equity: **$10,000.00**
- Cash: **$10,254.63** (unchanged — no trades this routine)
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
- Unrealized PnL (open positions): **$0.00** (no open positions)
- Position values (MTM): **$0.00**
- Current equity (cash + positions MTM): **$10,254.63**
- Equity peak: **$10,728.95** (set 2026-05-21 during missed-scheduler HYPE 4R take-profit replay)
- Drawdown from peak: **4.42%**

## Open positions

_(none — book flat since XRP/USD exit 2026-05-30T23:00:00Z)_

Portfolio risk-at-moment: **0.00%** of equity (cap 4%).
Open positions: **0 / 8** (strategy v0.4 max-concurrent 4 → 0/4 used; cluster {BTC,ETH,SOL,TAO,AVAX,SUI,LINK} 0/2).

## Active kill-switch state

- Daily realized on 2026-06-12 PT trading day: **$0.00** (no closes today; last close was XRP exit 2026-05-30 PT, 13 days ago) — clear vs 5% loss cap.
- Consecutive losing trading days: 05-22 L, 05-25 L, 05-26 L, 05-30 L (05-27/28/29/31, 06-01 → 06-12 all no-realized-PnL → streak unchanged) → streak **4** (cap 7; warn at 5 informally — still 1 day from informal warn).
- Max drawdown: **4.42%** from peak $10,728.95 (cap 25%, warn 12.5%) — clear.
- Equity floor: $10,254.63 > $7,500 floor — OK.
- Regime gate (rule 5a) — **midday refresh via `kraken_multi_ticker` (24h-change snapshot, not entry-eligible per midday design)**: **5/15 positive**, median **−0.30% (SOL)** → **5a marginal PASS** (1-pair-from-fail buffer — softened from overnight 13/15 +1.49% over ~6h). **5a-SBD remains CLEARED** — both conditions (>1 positive: 5>1 ✓; median >−1.0: −0.30>−1.0 ✓) inactive. SBD's tightened 9-EMA exit override stays deactivated. Midday gates nothing on regime — informational telemetry only. Per-pair rule 3 not re-measured (no 1H/4H bar closes since the overnight scan). The afternoon thinning narrows the recovery margin; next entry-eligible read is routine-03-eod 2026-06-13T04:00Z at the 21:00 PT 1H + 4H closes.
- No active 5b cooldowns (XRP 2026-05-30 exit was ema20-confirm, not stop-hit — rule 5b inapplicable; >24h elapsed anyway).
- **All clear (kill switches).** routine-02-midday 2026-06-12T20:00Z (Fri 13:00 PT scheduled on-schedule fire): **0 OPEN, 0 CLOSE** (book flat → MTM + exit-check steps inert; entry scan forbidden by midday design). Kraken MCP AVAILABLE (15/15 multi_ticker clean for kill-switch + regime telemetry). Drawdown 4.42% unchanged. Loss-streak 4 unchanged (no closes today). Daily PnL $0. **No Telegram** (silent — routine-02 NOTIFY gate: no kill-switch trip, no exit event, no DD halfway-warn crossing — DD comfortably below 12.5%). Next on-schedule wake: routine-03-eod 2026-06-13T04:00Z (Fri 21:00 PT scheduled — entry-eligible at 1H/4H closes).

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

_(none — no open positions)_

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | ≈ 0.0% (held flat at $10,254.63 across the 7d window) | ≈ +0.7% (BTC 2026-06-05 ~$63.2k → today $63.64k, span includes the 06-05 $60k low) | ≈ −0.7% | BULL slightly behind BTC on 7d |
| 30d | ≈ +2.55% (inception $10k 2026-04-20; window fully computable) | ≈ −21.7% (BTC 2026-05-13 ~$81.3k → today $63.64k) | ≈ +24.3% | BULL well ahead |
| 90d | — | — | — | not computable (BULL inception 2026-04-20 = 54 days ago) |

(7d and 30d figures approximate — precise reference-price computation deferred to routine #4. 90d window first computable ~2026-07-19. BTC reference today **$63,637** (midday `kraken_multi_ticker`) — BTC +0.13% on 24h, continued shallow bounce. 7d window includes the 06-05 $60k low so BTC-hold shows a small net positive return on that span; the 30d delta is the better representation of BULL's defensive-flat-book through the full breakdown. The strategy stayed flat through the bottom (5a/SBD blocked entries) and continues defensive in the early bounce — designed defensive sequence per W21-F.)
