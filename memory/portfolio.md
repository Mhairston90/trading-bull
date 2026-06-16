# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-06-16T12:30Z routine-02-midday (off-schedule fire — cron `0 13 * * 1-5` slotted for Tue 13:00 PT / 20:00 UTC but framework dispatched ~7h early; same off-schedule treatment as the prior weekend fires). **Position management only — flat book, no exits to check, no entries permitted in midday per spec.** Account is fully in cash since Sun 06-14T13:00Z BTC EMA20-confirm exit (-0.60R / -$47.27). **State unchanged since routine-01-overnight 2026-06-14T17:14Z** (no routine wakes recorded in the intervening ~43h — Mon 06-15 routines did not fire; this is the first wake to resume). **Equity:** $10,828.58 (cash, no positions). **Equity peak:** $10,875.85 unchanged. **Drawdown:** 0.43% — CLEAR (12.5% warn). **Kill switches:** all CLEAR (daily realized $0 today, loss streak 1 from Sun BTC scratch, equity $10,828.58 well above $7,500 floor). **Live breadth (informational, no entry impact this routine):** 14/15 positive 24h via `kraken_multi_ticker` 12:30Z (only TRX -0.31 negative; median +1.27%) — 5a PASS, SBD CLEAR. BTC last $66,166.5 (vs Sun exit $64,240.66, +3.00% in the 43h carry — would have produced ~+5.0R unrealized had the EMA20-confirm exit not fired; archetype-consistent with the W22-G commission-drag lesson: tight-range two-bar exits give back upside when the larger move resumes). HYPE +6.01%, NEAR +11.2%, TAO +3.88%, XRP +3.47%, ETH +2.05%. Skipping any post-hoc what-if accounting per `feedback-perf-analysis-framing` — the strategy v0.4 rule fired as designed, the post-exit move is what it is. **No writes to trade_log this wake. Telegram silent** (no kill, no exit, no DD warn). Next on-schedule wake: depending on which routines re-thread first — routine-01-overnight cron `0 6 * * 1-5` would fire Wed 06-17T13:00Z if Mon/Tue schedule continues missing.

> **Prior rebuild (Sun AM):** 2026-06-14T17:14Z routine-01-overnight (**Sun off-schedule fire** — cron `0 6 * * 1-5` does not fire Sunday; framework dispatched anyway, fourth consecutive off-schedule weekend fire after Sat routine-01/02/03; slot ID `bull-01-overnight` verified, body content matched, dirty-tree finding from watchdog was transient — `git status` clean at routine start). **MATERIAL EVENT — BTC/USD 0.168 stop-out exit replay 2026-06-14T13:00Z** via Exit rule 1 (W22-G two-bar EMA20 confirm). Walked 1H closes since the 2026-06-14T04:11Z routine-03-eod snapshot: 04:00Z $64,320.2 / 05:00Z $64,331.7 / 06:00Z $64,257.5 / 07:00Z $64,409.8 / 08:00Z $64,430.3 / 09:00Z $64,570.0 / 10:00Z $64,500.1 / 11:00Z $64,521.5 / **12:00Z $64,282.9 (first below-EMA20 — back-prop EMA $64,333) / 13:00Z $64,272.8 (second below-EMA20 — back-prop EMA $64,327 — Exit rule 1 fires at this bar close per W22-G two-bar confirmation)** / 14:00Z $63,941.5 / 15:00Z $63,982.4 / 16:00Z $63,915.4 (script-confirmed EMA $64,228, FAIL -312.7). Exit fill price with 0.05% adverse slippage: $64,272.8 × 0.9995 = **$64,240.66**. **Realized: -0.60R / -$47.27 net** (gross +$8.83 = 0.168 × 52.56; commission roundtrip 0.52% on (64,188.10+64,240.66) × 0.168 = $56.10). Tag `exit-ema20-confirm-missed-scheduler-replay` matching the 2026-05-22 TAO/HYPE/AVAX precedent for off-schedule wakes catching exits that fired between scheduled runs. **Exit checks vs other rules:** (2) 2×ATR stop $63,720.62 not pierced — lowest intra-bar low post-entry was $63,850.7 (14:00 UTC bar), $130.08 above stop. (3) 4R take-profit $66,058.02 not hit — highest 1H high post-entry was $64,750.0 (06-13 21:00 UTC bar), $1,308 below target. (Breakeven ratchet not armed — highest post-entry 1H close $64,570.0 [06-14 09:00 UTC] = +0.82R, below +2R threshold $65,123.06; stop never moved off the initial 2×ATR level.) **Cash math:** $92.25 + (0.168 × $64,240.66 - $56.10 commission) = $92.25 + $10,736.33 = **$10,828.58**. **Realized PnL all-time:** $875.85 - $47.27 = **+$828.58**. **Equity:** $10,828.58 (no open positions, equity = cash). **Equity peak:** $10,875.85 unchanged (set 2026-06-13T09:00Z at TAO 4R close; today's BTC scratch did not approach). **Drawdown from peak:** ($10,875.85 - $10,828.58) / $10,875.85 = **0.43%** (CLEAR — 25% kill / 12.5% warn). **Loss streak:** 0 → **1** (BTC -$47.27 is a small net loss; would have been roughly +$10 gross before friction — single-bar EMA-confirm exits in tight ranges remain commission-dominated, same archetype that motivated W22-G's two-bar confirmation but the two-bar rule still fires when both bars are sub-EMA20 in succession, as today). 7-day kill at 7 consecutive — current 1 far from cap.

> **EOD entry scan (W19-E analyst-role split) — 2026-06-14 PT, post-exit:** authoritative indicators via `scripts/indicators.py` 17:14:02Z (720-bar 1H + 4H, SMA-seeded EMAs, Wilder RSI/ATR; clean 15-pair fetch). Regime read at the 16:00 UTC closed bar: **3/15 positive 24h (TAO +0.12, LTC +0.55, TRX +0.28), median -0.90%** → **5a FAIL** (3 < 4-pair floor — sharp deterioration from this morning's print of 15/15 +1.90%, which itself was a recovery from a deeper Fri-EOD slump; market gave back the Sat rally in the Sun session). **5a-SBD CLEAR** (3 > 1 positive; SBD requires ≤1). **All new entries rejected this wake per rule 5a.** Per-pair scan still recorded for research_log audit: BTC FAIL R1 (-$312.7) + R2 (RSI 39.8); ETH FAIL R1+R2+R3; SOL FAIL R1+R2+R3 (4H 50-EMA flipped negative -$0.135 vs $67.555); HYPE FAIL R1+R2 (RSI 46.8); XRP FAIL R1+R2+R3; SUI FAIL R1+R2+R3; **TAO PASS R1 (+$0.32) + R3 (+$34.69 vs 4H EMA $228.05) — but FAIL R2 (RSI 54.2, -0.82 under 55 floor)**; XDG FAIL R1+R2+R3; NEAR FAIL R1+R2+R3; ADA FAIL R1+R2 (RSI 29.0) + R3; LINK FAIL R1+R2+R3; **LTC PASS R1 (+$0.018) + R3 (+$0.273) — but FAIL R2 (RSI 53.0, -2.0 under 55 floor)**; FARTCOIN FAIL R1+R2+R3+R4a; **TRX PASS R1+R2 (RSI 59.5) — but FAIL R3 (-$0.0032 vs 4H EMA $0.3214) + R4a ($0.65M < $2.0M)**; AVAX FAIL R1+R2+R3+R4a. **Zero per-pair PASSes survive all rules** (TAO and LTC each one rule short; TRX two rules short and below liquidity floor). Even setting aside 5a, no eligible candidates. **0 trade_log writes for entries this wake.** **Structural read:** post-BTC-exit cash is back to $10,828.58 — friction floor that bound 2nd-position attempts is fully resolved. Next eligible entry (under rule 5a recovery + a per-pair PASS) will size to the full 1.5% risk envelope = $162.43 risk @ this equity. Rule-8 tiebreaker backlog item (cash-aware acceptance) becomes moot for the duration of zero open positions.

> **Prior rebuild (Sat EOD):** 2026-06-14T04:11Z routine-03-eod (Sat 21:11 PT, 2026-06-13 PT trading day EOD). Position management on BTC carry + EOD entry scan flagged 7 mandate-eligible candidates (SOL/HYPE/XRP/SUI/TAO/XDG/NEAR) but all blocked by friction floor: 99.16% of equity in BTC left $92.25 cash, sized-down trades would have had commission > 1/3 of stop risk. **0 trades.** Regime 15/15 +1.90% (5a PASS, SBD CLEAR). Equity $10,930.40 MTM, DD 0.00%. Watchdog ALL CLEAR. Mandatory EOD Telegram sent. Next scheduled wake noted as 2026-06-15T13:00Z (Mon 06:00 PT). [That projection was superseded by this Sun 17:14Z off-schedule fire, which caught the missed 13:00Z exit ~4h late.]

> **Prior rebuild (Sat midday):** 2026-06-13T20:07Z routine-02-midday (Sat 13:07 PT off-schedule fire). BTC carry-only, no events. 5 1H closes deep, all above EMA20 at the time, lowest low $63,893.2, +0.05R unrealized. Equity $10,879.85, DD 0.00%.

> **Prior rebuild (Sat AM):** 2026-06-13T15:50Z routine-01-overnight (off-schedule Sat fire). TAO 4R replay close +4.04R / +$621.22 + BTC 0.168 long opened. Equity jumped $10,254.63 → $10,875.85 (NEW peak), loss-streak reset 4→0.

> **Prior rebuild (Fri EOD):** 2026-06-13T04:10Z routine-03-eod. First entry since XRP exit 2026-05-30 — TAO/USD long opened at 21:00 PT 1H close $217.286. Equity $10,254.63, DD 4.42%, loss-streak 4, regime 4/15 positive (zero-buffer 5a marginal PASS).

## Account

- Starting equity: **$10,000.00**
- Cash: **$10,828.58** (was $92.25; +$10,736.33 from BTC close)
- Realized PnL (all-time): **+$828.58** (was +$875.85; -$47.27 on BTC scratch exit)
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
  - XRP −$21.92 (exit-ema-cross 2026-05-15T04:00Z, −0.14R) — corrected
  - HYPE +$413.62 (missed-scheduler replay exit-4R-target 2026-05-21T08:00Z, +4.04R)
  - TAO −$29.84 (missed-scheduler replay exit-ema20-confirm 2026-05-22T01:00Z, −0.50R)
  - HYPE −$33.98 (missed-scheduler replay exit-ema20-confirm 2026-05-22T02:00Z, −0.29R)
  - SOL −$45.64 (missed-scheduler replay exit-stop-hit 2026-05-22T15:00Z, −1.43R)
  - AVAX −$35.83 (missed-scheduler replay exit-ema20-confirm 2026-05-22T16:00Z, −0.94R)
  - BTC −$33.70 (exit-stop-hit 2026-05-25T22:00Z, −1.07R)
  - TAO −$114.75 (missed-scheduler replay exit-ema20-confirm 2026-05-26T18:00Z, −0.58R)
  - XRP −$101.40 (missed-scheduler replay exit-ema20-confirm 2026-05-30T23:00Z, −0.65R)
  - TAO +$621.22 (missed-scheduler replay exit-4R-target 2026-06-13T09:00Z, +4.04R)
  - **BTC −$47.27 (missed-scheduler replay exit-ema20-confirm 2026-06-14T13:00Z, −0.60R)** — new this wake
- Unrealized PnL (open positions): **$0.00** (no open positions)
- Position values (MTM): **$0.00**
- Current equity (cash + positions MTM): **$10,828.58**
- Equity peak: **$10,875.85** (set 2026-06-13T09:00Z at TAO 4R close — unchanged)
- Drawdown from peak: **0.43%** ($47.27 below peak)
- Since-inception return: **+8.29%** ($10,828.58 / $10,000 − 1)

## Open positions

*(none)*

Portfolio risk-at-moment: **0.00%** of equity (cap 4%).
Open positions: **0 / 8** (strategy v0.4 max-concurrent 4 → 0/4 used; cluster {BTC,ETH,SOL,TAO,AVAX,SUI,LINK} 0/2).

## Day summary — 2026-06-16 PT (Tue midday, off-schedule)

| Metric | Value |
|---|---|
| Day realized PnL | **$0.00** (flat book, no trades) |
| Day realized % | **0.00%** |
| Day MTM PnL | **$0.00** (no positions to MTM) |
| Trades opened today | **0** (midday spec forbids entries) |
| Trades closed today | **0** (no positions) |
| Equity at this wake | **$10,828.58** (cash) |
| Equity peak (realized) | **$10,875.85** (unchanged) |
| Drawdown from peak | **0.43%** (unchanged) |
| Loss streak | **1** (carry from Sun 06-14 BTC scratch; Mon was a zero-trade day, does not advance streak) |

## Day summary — 2026-06-14 PT (Sun, off-schedule wake)

| Metric | Value |
|---|---|
| Day realized PnL | **-$47.27** (BTC W22-G two-bar EMA20 confirm exit) |
| Day realized % | **-0.43%** (on day-open equity $10,930.40 MTM) |
| Day MTM PnL | **-$101.82** (also gave back $54.55 unrealized cushion that BTC carried into Sun open) |
| Day total return MTM | **-0.93%** |
| Trades opened today | **0** (5a FAIL: 3/15 positive blocks all new entries) |
| Trades closed today | **1** (BTC/USD 0.168 long @ 13:00Z UTC = 06:00 PT) |
| Win rate today | **0%** (0/1) |
| Equity at this wake | **$10,828.58** (cash, no positions) |
| Equity peak (realized) | **$10,875.85** (unchanged) |
| Drawdown from peak | **0.43%** |
| Loss streak | **1** (BTC small net loss) |

## Active kill-switch state

- Daily realized 2026-06-14 PT: **-$47.27 / -0.43%** — loss cap 5% (24x below), CLEAR.
- Consecutive losing trading days: **1** (BTC -0.60R; cap 7, 6 trades of headroom).
- Max drawdown: **0.43%** from peak $10,875.85 (cap 25%, warn 12.5%) — CLEAR.
- Equity floor: $10,828.58 > $7,500 floor — CLEAR.
- Regime gate (rule 5a) — **16:00 UTC 1H/4H close via `scripts/indicators.py` 17:14:02Z**: **3/15 positive, median -0.90%** → **5a FAIL** (3 below 4-pair floor — sharp Sun-session reversal from this morning's 15/15 +1.90% print). **5a-SBD CLEAR** (3 > 1 positive AND -0.90 > -1.0 median; SBD inactive but the median is right at the SBD threshold).
- Active 5b cooldowns: **BTC 2026-06-14T13:00Z exit-ema20-confirm — 5b active until 2026-06-15T13:00Z** (24h same-pair re-entry cooldown applies because tag is `exit-ema20-confirm`, but rule 5b text specifies stop-out only: "do not open a new position in a pair within 24h of a stop-out (`exit-stop-hit`)". An EMA-confirm exit is **not** a stop-out → **5b INAPPLICABLE.** Treated symmetrically with TAO 2026-06-13 exit which also bypassed 5b via take-profit tag.) **No active 5b cooldowns.**
- **Watchdog (`scripts/watchdog.py --telegram` @ 17:13:47Z):** found 1 finding (`dirty-tree: 1 uncommitted change(s): M memory/research_log.md`) — **transient/false-positive**; `git status` 5 seconds later returned clean. Likely caught a write-in-flight from an aborted prior session or a watchdog timing race. No action needed.
- **All clear (kill switches).** routine-01-overnight 2026-06-14T17:14Z (Sun 10:14 PT — off-schedule fire): **0 OPENs, 1 CLOSE.** Kraken MCP AVAILABLE (`kraken_multi_ticker` + `kraken_ohlcv` 30-bar fetch both clean; indicators script 15/15 clean 720-bar pulls in <30s). **Telegram: exit-event notify sent** per routine §NOTIFY (CLOSE event triggers brief summary). Next on-schedule wake: routine-01-overnight 2026-06-15T13:00Z (Mon 06:00 PT, ~20h away). **No open positions to carry** — zero exposure means any further Sun price action (favorable or adverse) is irrelevant to BULL.

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

*(none — flat after BTC exit)*

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | ≈ +5.59% realized (TAO +4.04R / +6.21%, BTC -0.60R / -0.43%) | ≈ +1.1% (BTC ~$63.2k → $63.9k over 7d) | ≈ +4.5% | BULL ahead on 7d |
| 30d | ≈ +8.29% (inception $10k 2026-04-20; window fully computable) | ≈ −21.4% (BTC 2026-05-13 ~$81.3k → today $63.9k) | ≈ +29.7% | BULL well ahead |
| 90d | — | — | — | not computable (BULL inception 2026-04-20 = 55 days ago; window first computable ~2026-07-19) |

(7d / 30d figures approximate — precise reference-price computation deferred to routine #4. BTC reference $63,930.2 spot this wake. The TAO 4R win still dominates the trailing window despite today's small give-back. Inception-to-date return slipped from +9.30% peak to +8.29% — a -1.01% retracement, well inside ordinary trade-by-trade noise for this strategy. The two-trade sequence TAO 4R → BTC -0.60R has net realized of +3.44R / +$573.95 over 33 calendar hours, which materially advances the W22-G case file: the rule trimmed today's bleed where the prior rule would have either held to stop-out at -1.0R = -$78.54 or kept holding through whatever the Sun/Mon path delivers. The two-bar confirmation gate prevented an exit on the Fri-EOD-to-Sat overnight wave where 16:00Z bar was the only single below-EMA close.)
