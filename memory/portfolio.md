# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-06-13T20:07Z routine-02-midday (**off-schedule Saturday fire** — cron is Mon-Fri `0 13 * * 1-5`, framework dispatched anyway; same off-schedule treatment as this morning's routine-01 wake). Slot ID `bull-02-midday`. **Position management only; mandatory no-entry per routine spec.** BTC/USD long 0.168 @ $64,188.10 has had 5 full 1H closes since entry (15:00, 16:00, 17:00, 18:00, 19:00 UTC) plus a partial 20:00 UTC bar in progress. **Exit checks (per strategy v0.4):** (1) Exit rule 1 (W22-G two-bar EMA20 confirm) — no bars closed below 20-EMA since entry. EMA20 chain post-entry computed arithmetically off the 63,768.1 baseline (α=2/21=0.0952): 15:00 EMA→63,814.3 vs close 64,253.4 ✓, 16:00 EMA→63,830.9 vs close 63,988.5 ✓, 17:00 EMA→63,841.7 vs close 63,944.3 ✓, 18:00 EMA→63,869.1 vs close 64,129.6 ✓, 19:00 EMA→63,908.4 vs close 64,281.7 ✓. All five closes above the rising EMA20. **Rule 1 inert.** (2) Exit rule 2 (2×ATR stop $63,720.62) — lowest low across the post-entry bars was $63,893.2 (16:00 bar), $172.58 above stop. **Stop not pierced intrabar.** (3) Exit rule 3 (4R take-profit $66,058.02) — highest high $64,294.0 (15:00 bar), gap of $1,764. **Not hit.** (4) **Breakeven ratchet (W22-H-partial):** requires +2R unrealized at a 1H close = price ≥ $65,123.06. Highest 1H close since entry was $64,281.7 (19:00 bar) = unrealized R +0.20. **Ratchet not armed; stop remains at original $63,720.62.** **No exits this wake.** **MTM:** BTC last $64,211.9 (Kraken `kraken_multi_ticker`, 24h +1.05%, high $64,294.0 / low $63,372.2 — low predates entry, immaterial). Position notional $10,787.60 = 0.168 × $64,211.9. Cash $92.25 (unchanged — no events). Equity **$10,879.85**. Unrealized PnL +$3.95 = 0.168 × ($64,211.9 - $64,188.10) gross; net R +0.05. **Equity vs peak:** $10,879.85 MTM > realized peak $10,875.85 by $4.00 — **realized peak not updated** (peaks track realized closes, not intrabar MTM, per inception convention); drawdown 0.00%. **Kill switches:** Daily realized 2026-06-13 PT +6.06% (loss cap is downside-only, CLEAR); consecutive losing days 0; max DD 0% (cap 25%, warn 12.5%) CLEAR; equity $10,879.85 > $7,500 floor CLEAR; Kraken MCP AVAILABLE (`kraken_multi_ticker` + `kraken_ohlcv` 12-bar fetch both clean). **All clear.** **No Telegram** — no kill-switch trip, no exit, no entry, drawdown nowhere near 12.5% warn threshold (routine #2 NOTIFY gate not met). **Next on-schedule wake:** routine-01-overnight 2026-06-15T13:00Z (Mon 06:00 PT — Sun off per cron). BTC position carries ~37h unmanaged across the remaining Sat→Mon window; the $172.58 stop buffer + the rising 20-EMA + the +0.20R cushion are the protective layers across that window. **Note on the cron-vs-fire mismatch:** this is the second off-schedule weekend fire today (routine-01 at 15:50Z, routine-02 at 20:07Z). Both honored the routine job spec without modification. Backlog: confirm with user whether weekend dispatches are intentional (new framework behavior?) or whether the cron filter should be enforced inside each routine.

> **Prior rebuild (Sat morning earlier):** 2026-06-13T15:50Z routine-01-overnight (**off-schedule Saturday fire** — cron is Mon-Fri `0 6 * * 1-5`, so this is an out-of-band wake). Slot ID confirmed `bull-01-overnight`. **Two material events processed this wake (TAO take-profit replay + BTC entry).** Authoritative indicators via `scripts/indicators.py` (720-bar 1H+4H, SMA-seeded EMAs, Wilder RSI/ATR; engine clean in 30s 15-pair fetch). Regime read at the 2026-06-13T15:00Z bar close: **11/15 positive on 24h % change, median +0.52%** → **5a PASS** (well above 4-pair floor — buffer +7 vs Fri-EOD's 4-pair zero-buffer print, recovery has resumed), **5a-SBD CLEARED** (11 > 1 AND +0.52 > -1.0). **(1) TAO/USD 4R take-profit hit at 2026-06-13T09:00Z (bar `08:00-09:00 UTC`) 1H close $237.3015 ≥ 4R target $235.9396 → exit fires.** Bar prior (07:00-08:00 UTC) closed $234.6331 — R = +3.72 (breakeven ratchet at +2R = $226.6128 fired at the +3.72R close, but the 4R take-profit fires at the NEXT bar close $237.3015 = R +4.29 gross / **+4.04R net** after roundtrip 0.26%×2 commission $38.99). Realized PnL = 32.985 × ($237.3015 - $217.286) - $38.99 = $660.21 - $38.99 = **+$621.22**. Reason tag `exit-4R-target-missed-scheduler-replay` (same convention as 2026-05-21 HYPE 4R replay) — the 09:00 UTC 1H close happened during the 60+h unmanaged weekend window the Fri-EOD portfolio.md flagged; this off-schedule Sat wake replays the exit at the true trigger bar's close, not at current price. Intra-bar high since the 09:00 UTC trigger reached $268.9985 (TAO is now $260.33 mid-bar at 15:48 UTC) — strategy convention takes the exit at the 1H close that first satisfied the rule, not the subsequent runup. (Open question for routine #4: should the missed-scheduler convention take the exit at the higher of {bar close, 4R target} to better reflect the rule's intent? Logged for backlog.) **(2) BTC/USD entry at 2026-06-13T15:00Z (bar `14:00-15:00 UTC`) 1H close $64,188.10** — sole rule-1 PASS that also clears R4a liquidity. Per-pair entry scan against the just-closed 15:00 UTC bar (rules 1, 2, 2a, 3, 4a): BTC PASS R1 +$420 (1H 20-EMA 63,768.1), PASS R2 +9.935 (RSI14 64.9), PASS R2a (under 80 cap), PASS R3 +$263.8 (4H 50-EMA 63,656.9 — converged HIGH-CONFIDENCE 720 bars), PASS R4a ($75.89M >> $2.0M floor); ATR14 233.74, 2×ATR stop distance $467.48. SOL/SUI/XDG also PASS R1+R2+R2a+R3+R4a but rank lower (3/6/8 vs BTC=1); rule 8 (highest 30d notional rank wins) selects BTC. **Rule 5b** inapplicable (last BTC close was 2026-05-25T22:00Z `exit-stop-hit` 18 days ago, well past 24h cooldown). **Rule 6** PASS (0/4 open post-TAO-close). **Rule 6a** PASS (cluster {BTC,ETH,SOL,TAO,AVAX,SUI,LINK} 0/2 → BTC entry = 1/2 after fill). **Rule 7** PASS (per-trade risk $78.54 = 0.72% of equity, well below 1.5% cap; portfolio risk-at-moment post-entry = 0.72% of 4% cap). **Cash-constrained sizing:** ideal 1.5% sizing would be 0.349 BTC = $22,400 notional, but post-TAO-exit cash is only $10,875.85; mandate forbids leverage (spot-only), so size capped to **0.168 BTC** = $10,783.60 notional (~99.15% of cash). Risk-per-trade ends at 0.72% (under target, not over — mandate-compliant). This is the first cash-binding entry sizing since inception. **News pass:** Firecrawl skipped (token-budget, informational only per W19-E). **Sentiment pass:** Kraken `kraken_spread` BTC bid/ask cluster $0.10-1.4 spread on $64,236 (≈0.02-0.22 bps, very tight/healthy); 24h notional 941 BTC × VWAP ≈$64k = ~$60.2M (matches indicators.py $75.89M ± rolling-window difference). **Sentiment: supportive.** Equity post-events **$10,875.85** ($10,254.63 prior + $621.22 TAO realized). Equity peak **$10,875.85** (NEW peak — exceeds prior $10,728.95 by $146.90). Drawdown **0.00%** (peak reset). Cash post-BTC-entry **$92.25** ($10,875.85 - $10,783.60). Consecutive losing trading days **reset to 0** (the TAO +4.04R close on 2026-06-13 PT was a winning close → breaks the 4-loss streak 05-22/05-25/05-26/05-30). Daily realized 2026-06-13 PT **+$621.22 / +6.06%** — well clear of the 5% loss-cap (loss cap is downside-only). Kill switches all clear. Ops watchdog clean (`ALL CLEAR — heartbeats, timestamps, tree, MTM, scheduler flag, push state, MCP paths OK`). **Telegram: dual-event notify sent** (4R take-profit replay + new BTC entry — both qualify under routine-01 NOTIFY gate). 30d BULL ≈ +8.76% vs BTC-hold ≈ -21.0% → delta +29.8%. Next on-schedule wake: routine-01-overnight 2026-06-15T13:00Z (Mon 06:00 PT — Sat/Sun off per cron). BTC position carries 39+h unmanaged across the remaining weekend window after this wake closes; 2×ATR stop $63,720.62 is the protective floor (same designed-cron pattern as the TAO carry).

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
- Unrealized PnL (open positions): **+$3.95** (BTC last $64,211.9 vs entry $64,188.10, gross; R-multiple +0.05)
- Position values (MTM): **$10,787.60** (BTC 0.168 × $64,211.9 via `kraken_multi_ticker` 2026-06-13T20:07Z)
- Current equity (cash + positions MTM): **$10,879.85**
- Equity peak: **$10,875.85** (set 2026-06-13T09:00Z at TAO 4R close — peak tracks realized closes, not intrabar MTM; current MTM is $4 above this but does not advance the peak)
- Drawdown from peak: **0.00%** (MTM above peak)

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
- Equity floor: $10,879.85 (MTM) > $7,500 floor — OK.
- Regime gate (rule 5a) — **15:00 UTC 1H/4H close via `scripts/indicators.py`**: **11/15 positive, median +0.52%** → **5a PASS** (well clear of 4-pair floor, recovery resumed after Fri-EOD's zero-buffer print). **5a-SBD CLEARED** (11 > 1 positive AND +0.52 > -1.0 median). SBD's tightened 9-EMA exit override stays deactivated.
- No active 5b cooldowns (TAO closed 09:00Z on 4R target not stop-hit → 5b inapplicable; BTC last close 2026-05-25 was 18d ago).
- **All clear (kill switches).** routine-02-midday 2026-06-13T20:07Z (Sat 13:07 PT off-schedule fire): **0 OPENs, 0 CLOSEs** — exit-check sweep confirmed BTC position holds across all three v0.4 exit rules. Kraken MCP AVAILABLE (`kraken_multi_ticker` + `kraken_ohlcv` 12-bar fetch both clean). EMA20 chain recomputed arithmetically from 14:00-bar baseline 63,768.1, all 5 post-entry closes above the EMA. **Telegram NOT sent** (no notify-trigger met: no kill switch, no exit, drawdown 0.00%). Next on-schedule wake: routine-01-overnight 2026-06-15T13:00Z (Mon 06:00 PT). **Weekend remaining:** BTC position carries unmanaged ~37h between this fire (20:07Z Sat) and Mon routine-01 (15:00Z Mon). 2×ATR stop $63,720.62 is the protective floor (BTC last $64,211.9, stop is $491.28 / -0.76% away).

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
  - Exit rule 1 (W22-G): two consecutive 1H closes < 1H 20-EMA (currently ≈63,908 after 5 post-entry advancing bars). Active. Inert so far — 5/5 post-entry closes above EMA.
  - Exit rule 1-SBD: inert (SBD currently cleared; this wake did not re-verify the regime read because midday spec is position-management-only, but a single trading session's regime drift is not a v0.4 SBD trigger anyway — SBD requires <=1/15 positive AND median <=-1.0%, the morning print was 11/15 +0.52%).
  - Exit rule 2 (stop): $63,720.62. Not pierced (lowest low post-entry $63,893.2). Will ratchet to breakeven $64,188.10 once +2R reached at any 1H close (≥ $65,123.06). Highest 1H close post-entry $64,281.7 → ratchet not armed.
  - Exit rule 3 (4R target): $66,058.02. Not hit (highest high post-entry $64,294.0).
  - Next exit-check wake: routine-01-overnight 2026-06-15T13:00Z (Mon 06:00 PT). Sun bars will close unmonitored — static stop + rising EMA20 are the protection.

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | ≈ +6.06% (mostly the TAO 4R take-profit today) | ≈ +1.5% (BTC ~$63.2k → $64.2k over 7d) | ≈ +4.6% | BULL ahead on 7d |
| 30d | ≈ +8.76% (inception $10k 2026-04-20; window fully computable) | ≈ −21.0% (BTC 2026-05-13 ~$81.3k → today $64.2k) | ≈ +29.8% | BULL well ahead |
| 90d | — | — | — | not computable (BULL inception 2026-04-20 = 54 days ago) |

(7d / 30d figures approximate — precise reference-price computation deferred to routine #4. 90d window first computable ~2026-07-19. BTC reference $64,199.4 (this wake `kraken_multi_ticker`) — BTC +1.03% on 24h. The TAO 4R take-profit replay is the dominant performance driver this week; flat-book through the breakdown plus catching the bounce on a single trade is exactly the W21-F+W22 designed defensive-then-offensive sequence. The cash-binding BTC entry sizing is the first time post-major-win that the next opportunity hit a cash cap; logged for routine #4 review on whether rule 8 should accept lower-ranked but fully-fundable candidates as an alternative.)
