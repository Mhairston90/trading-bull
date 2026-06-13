# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-06-13T15:50Z routine-01-overnight (**off-schedule Saturday fire** — cron is Mon-Fri `0 6 * * 1-5`, so this is an out-of-band wake). Slot ID confirmed `bull-01-overnight`. **Two material events processed this wake (TAO take-profit replay + BTC entry).** Authoritative indicators via `scripts/indicators.py` (720-bar 1H+4H, SMA-seeded EMAs, Wilder RSI/ATR; engine clean in 30s 15-pair fetch). Regime read at the 2026-06-13T15:00Z bar close: **11/15 positive on 24h % change, median +0.52%** → **5a PASS** (well above 4-pair floor — buffer +7 vs Fri-EOD's 4-pair zero-buffer print, recovery has resumed), **5a-SBD CLEARED** (11 > 1 AND +0.52 > -1.0). **(1) TAO/USD 4R take-profit hit at 2026-06-13T09:00Z (bar `08:00-09:00 UTC`) 1H close $237.3015 ≥ 4R target $235.9396 → exit fires.** Bar prior (07:00-08:00 UTC) closed $234.6331 — R = +3.72 (breakeven ratchet at +2R = $226.6128 fired at the +3.72R close, but the 4R take-profit fires at the NEXT bar close $237.3015 = R +4.29 gross / **+4.04R net** after roundtrip 0.26%×2 commission $38.99). Realized PnL = 32.985 × ($237.3015 - $217.286) - $38.99 = $660.21 - $38.99 = **+$621.22**. Reason tag `exit-4R-target-missed-scheduler-replay` (same convention as 2026-05-21 HYPE 4R replay) — the 09:00 UTC 1H close happened during the 60+h unmanaged weekend window the Fri-EOD portfolio.md flagged; this off-schedule Sat wake replays the exit at the true trigger bar's close, not at current price. Intra-bar high since the 09:00 UTC trigger reached $268.9985 (TAO is now $260.33 mid-bar at 15:48 UTC) — strategy convention takes the exit at the 1H close that first satisfied the rule, not the subsequent runup. (Open question for routine #4: should the missed-scheduler convention take the exit at the higher of {bar close, 4R target} to better reflect the rule's intent? Logged for backlog.) **(2) BTC/USD entry at 2026-06-13T15:00Z (bar `14:00-15:00 UTC`) 1H close $64,188.10** — sole rule-1 PASS that also clears R4a liquidity. Per-pair entry scan against the just-closed 15:00 UTC bar (rules 1, 2, 2a, 3, 4a): BTC PASS R1 +$420 (1H 20-EMA 63,768.1), PASS R2 +9.935 (RSI14 64.9), PASS R2a (under 80 cap), PASS R3 +$263.8 (4H 50-EMA 63,656.9 — converged HIGH-CONFIDENCE 720 bars), PASS R4a ($75.89M >> $2.0M floor); ATR14 233.74, 2×ATR stop distance $467.48. SOL/SUI/XDG also PASS R1+R2+R2a+R3+R4a but rank lower (3/6/8 vs BTC=1); rule 8 (highest 30d notional rank wins) selects BTC. **Rule 5b** inapplicable (last BTC close was 2026-05-25T22:00Z `exit-stop-hit` 18 days ago, well past 24h cooldown). **Rule 6** PASS (0/4 open post-TAO-close). **Rule 6a** PASS (cluster {BTC,ETH,SOL,TAO,AVAX,SUI,LINK} 0/2 → BTC entry = 1/2 after fill). **Rule 7** PASS (per-trade risk $78.54 = 0.72% of equity, well below 1.5% cap; portfolio risk-at-moment post-entry = 0.72% of 4% cap). **Cash-constrained sizing:** ideal 1.5% sizing would be 0.349 BTC = $22,400 notional, but post-TAO-exit cash is only $10,875.85; mandate forbids leverage (spot-only), so size capped to **0.168 BTC** = $10,783.60 notional (~99.15% of cash). Risk-per-trade ends at 0.72% (under target, not over — mandate-compliant). This is the first cash-binding entry sizing since inception. **News pass:** Firecrawl skipped (token-budget, informational only per W19-E). **Sentiment pass:** Kraken `kraken_spread` BTC bid/ask cluster $0.10-1.4 spread on $64,236 (≈0.02-0.22 bps, very tight/healthy); 24h notional 941 BTC × VWAP ≈$64k = ~$60.2M (matches indicators.py $75.89M ± rolling-window difference). **Sentiment: supportive.** Equity post-events **$10,875.85** ($10,254.63 prior + $621.22 TAO realized). Equity peak **$10,875.85** (NEW peak — exceeds prior $10,728.95 by $146.90). Drawdown **0.00%** (peak reset). Cash post-BTC-entry **$92.25** ($10,875.85 - $10,783.60). Consecutive losing trading days **reset to 0** (the TAO +4.04R close on 2026-06-13 PT was a winning close → breaks the 4-loss streak 05-22/05-25/05-26/05-30). Daily realized 2026-06-13 PT **+$621.22 / +6.06%** — well clear of the 5% loss-cap (loss cap is downside-only). Kill switches all clear. Ops watchdog clean (`ALL CLEAR — heartbeats, timestamps, tree, MTM, scheduler flag, push state, MCP paths OK`). **Telegram: dual-event notify sent** (4R take-profit replay + new BTC entry — both qualify under routine-01 NOTIFY gate). 30d BULL ≈ +8.76% vs BTC-hold ≈ -21.0% → delta +29.8%. Next on-schedule wake: routine-01-overnight 2026-06-15T13:00Z (Mon 06:00 PT — Sat/Sun off per cron). BTC position carries 39+h unmanaged across the remaining weekend window after this wake closes; 2×ATR stop $63,720.62 is the protective floor (same designed-cron pattern as the TAO carry).

> **Prior rebuild (Fri EOD):** 2026-06-13T04:10Z routine-03-eod (Fri 21:10 PT — 2026-06-12 PT trading day EOD). Slot ID confirmed `bull-03-eod`. **First entry since XRP exit 2026-05-30 — TAO/USD long opened at 21:00 PT 1H close.** Equity $10,254.63, drawdown 4.42%, loss-streak 4, regime 4/15 positive (zero-buffer 5a marginal PASS), SBD cleared. TAO entered at $217.286 size 32.985 (1.5% risk = $153.82), stop $212.6226, 4R target $235.9396, cluster 1/2 used. Telegram EOD card sent. Next wake flagged routine-01-overnight 2026-06-15T13:00Z (Mon 06:00 PT) — TAO position to carry unmanaged across 60+h weekend window with 2×ATR stop as only protection. **What actually happened:** an out-of-band Sat 08:48 PT routine-01 fire (this wake) processed the TAO 4R take-profit replay 6h after the trigger bar closed.

> **Prior rebuild (Fri midday):** 2026-06-12T20:00Z routine-02-midday (Fri 13:00 PT scheduled on-schedule fire). Book flat — 21st consecutive flat-book wake since XRP exit 2026-05-30T23:00Z (13 days). Regime 5/15 positive median -0.30%, SBD cleared. Equity $10,254.63 unchanged. No exits, no entries (midday design forbids entries).

## Account

- Starting equity: **$10,000.00**
- Cash: **$92.25** ($10,875.85 post-TAO-exit cash − $10,783.60 BTC entry notional)
- Realized PnL (all-time): **+$875.85**
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
  - **TAO +$621.22 (missed-scheduler replay exit-4R-target 2026-06-13T09:00Z, +4.04R)** ← this wake
- Unrealized PnL (open positions): **+$1.90** (intra-bar — BTC last $64,199.4 ≈ entry $64,188.10)
- Position values (MTM): **$10,785.50** (BTC 0.168 × intra-bar $64,199.4)
- Current equity (cash + positions MTM): **$10,877.75** (≈$10,875.85 entry-fill + intra-bar drift)
- Equity peak: **$10,875.85** (NEW — set this wake at TAO 4R close, supersedes prior $10,728.95 set 2026-05-21)
- Drawdown from peak: **0.00%**

## Open positions

| Pair | Side | Size | Entry | Entry time (UTC) | Stop | 4R target | Risk ($) | Risk (% equity) |
|------|------|------|-------|------------------|------|-----------|----------|------------------|
| BTC/USD | long | 0.168 | 64188.10 | 2026-06-13T15:00:00Z | 63720.62 | 66058.02 | 78.54 | 0.72% |

Portfolio risk-at-moment: **0.72%** of equity (cap 4%).
Open positions: **1 / 8** (strategy v0.4 max-concurrent 4 → 1/4 used; cluster {BTC,ETH,SOL,TAO,AVAX,SUI,LINK} 1/2 — BTC is in cluster).

## Active kill-switch state

- Daily realized on 2026-06-13 PT trading day: **+$621.22 / +6.06%** (TAO 4R take-profit replay) — well clear of 5% loss cap (which is downside-only). Day is net positive.
- Consecutive losing trading days: **reset to 0** (TAO +4.04R close on 2026-06-13 was a winning realized day, breaking the prior streak 05-22 L / 05-25 L / 05-26 L / 05-30 L = 4).
- Max drawdown: **0.00%** from new peak $10,875.85 (cap 25%, warn 12.5%) — clear.
- Equity floor: $10,875.85 > $7,500 floor — OK.
- Regime gate (rule 5a) — **15:00 UTC 1H/4H close via `scripts/indicators.py`**: **11/15 positive, median +0.52%** → **5a PASS** (well clear of 4-pair floor, recovery resumed after Fri-EOD's zero-buffer print). **5a-SBD CLEARED** (11 > 1 positive AND +0.52 > -1.0 median). SBD's tightened 9-EMA exit override stays deactivated.
- No active 5b cooldowns (TAO closed 09:00Z on 4R target not stop-hit → 5b inapplicable; BTC last close 2026-05-25 was 18d ago).
- **All clear (kill switches).** routine-01-overnight 2026-06-13T15:50Z (Sat 08:50 PT off-schedule fire): **1 OPEN (BTC entry), 1 CLOSE (TAO 4R replay)**. Kraken MCP AVAILABLE (multi_ticker + spread + ohlcv all clean). Indicators.py engine clean. **Telegram dual-event notify sent** per routine #1 NOTIFY gate (both 4R take-profit replay + new entry qualify). Next on-schedule wake: routine-01-overnight 2026-06-15T13:00Z (Mon 06:00 PT). **Note on weekend remaining:** BTC position carries unmanaged across ~45h between this Sat 08:50 PT fill and Mon 06:00 PT next routine. 2×ATR stop $63,720.62 is the protective floor (BTC last $64,199.4, stop is $479 / -0.75% away). This is the designed cron behavior given the Mon-Fri schedule.

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

- BTC/USD long 0.168 @ 64188.10:
  - Exit rule 1 (W22-G): two consecutive 1H closes < 1H 20-EMA (currently 63,768.1). Active.
  - Exit rule 1-SBD: inert (SBD currently cleared).
  - Exit rule 2 (stop): $63,720.62. Will ratchet to breakeven $64,188.10 once +2R reached at any 1H close (≥ $65,123.06).
  - Exit rule 3 (4R target): $66,058.02.
  - First eligible exit-check wake: routine-01-overnight 2026-06-15T13:00Z (Mon 06:00 PT). Weekend bars between this fill and that wake will close unmonitored — static stop is the only protection across that window.

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | ≈ +6.06% (mostly the TAO 4R take-profit today) | ≈ +1.5% (BTC ~$63.2k → $64.2k over 7d) | ≈ +4.6% | BULL ahead on 7d |
| 30d | ≈ +8.76% (inception $10k 2026-04-20; window fully computable) | ≈ −21.0% (BTC 2026-05-13 ~$81.3k → today $64.2k) | ≈ +29.8% | BULL well ahead |
| 90d | — | — | — | not computable (BULL inception 2026-04-20 = 54 days ago) |

(7d / 30d figures approximate — precise reference-price computation deferred to routine #4. 90d window first computable ~2026-07-19. BTC reference $64,199.4 (this wake `kraken_multi_ticker`) — BTC +1.03% on 24h. The TAO 4R take-profit replay is the dominant performance driver this week; flat-book through the breakdown plus catching the bounce on a single trade is exactly the W21-F+W22 designed defensive-then-offensive sequence. The cash-binding BTC entry sizing is the first time post-major-win that the next opportunity hit a cash cap; logged for routine #4 review on whether rule 8 should accept lower-ranked but fully-fundable candidates as an alternative.)
