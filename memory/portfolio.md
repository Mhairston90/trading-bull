# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-06-14T04:11Z routine-03-eod (Sat 21:11 PT — 2026-06-13 PT trading day EOD; first weekday EOD that the cron `0 21 * * 1-5` skips intentionally landed on a Sat-fire — slot ID `bull-03-eod` verified, body content matched, date-labeling guard checked: PT date 2026-06-13 stamped throughout, not the UTC date 2026-06-14). **Position management + EOD entry scan, no events.** BTC/USD long 0.168 @ $64,188.10 has had 13 full 1H closes since entry (15:00, 16:00, 17:00, 18:00, 19:00, 20:00, 21:00, 22:00, 23:00 UTC 06-13 + 00:00, 01:00, 02:00, 03:00 UTC 06-14). **Exit checks (per strategy v0.4):** (1) Exit rule 1 (W22-G two-bar EMA20 confirm) — zero closes below 1H 20-EMA in the 13-bar chain. EMA20 from `scripts/indicators.py` 04:10:49Z snapshot = **$63,762**; lowest post-entry close $63,944.3 (17:00) is $182.3 above the EMA. **Rule 1 inert.** (2) Exit rule 2 (2×ATR stop $63,720.62) — lowest intra-bar low across the 13 post-entry bars was $63,893.2 (16:00), $172.58 above stop. **Stop not pierced.** (3) Exit rule 3 (4R take-profit $66,058.02) — highest 1H high $64,750.0 (21:00 UTC bar), $1,308 below target. **Not hit.** (4) **Breakeven ratchet (W22-H-partial):** requires +2R unrealized at a 1H close = price ≥ $65,123.06. Highest 1H close was $64,560.9 (01:00 UTC), $562.16 below ratchet threshold = unrealized R +0.80 on best close. **Ratchet not armed; stop stays at $63,720.62.** **No exits this wake.** **MTM:** BTC last 1H close $64,512.8 (Kraken 1H OHLCV 03:00 UTC); spot $64,490.3 via `kraken_multi_ticker` 04:10:49Z. EOD convention uses last 1H close = $64,512.8. Position notional **$10,838.15** = 0.168 × $64,512.8. Cash $92.25 (unchanged since BTC entry — no events). Equity **$10,930.40**. Unrealized PnL **+$54.55** = 0.168 × (64,512.8 − 64,188.10) gross; net R **+0.69**. **Equity vs peak:** $10,930.40 MTM > realized peak $10,875.85 by $54.55 — **realized peak not updated** (peaks track realized closes, not intrabar MTM, per inception convention). Drawdown **0.00%**.

> **EOD entry scan (W19-E analyst-role split) — 2026-06-13 PT:** authoritative indicators via `scripts/indicators.py` (720-bar 1H + 4H, SMA-seeded EMAs, Wilder RSI/ATR; clean 15-pair fetch in 30s). Regime read at the 03:00 UTC closed bar: **15/15 positive 24h, median +1.90%** → **5a PASS** (well clear of 4-pair floor — breadth has lifted from this morning's 11/15 +0.52% print, recovery continues), **5a-SBD CLEARED** (15 > 1 AND +1.90 > -1.0). TAO leads on +26.88% 24h (RSI 77.9 — under 80 cap but climactic-adjacent). **Per-pair technical scan against 03:00 UTC 1H close + latest 4H close:** BTC excluded (rule 5 — open position); ETH FAIL R3 (-$6.95 vs 4H EMA50 $1,687.82); **SOL PASS** R1+R2+R2a+R3+R4a (R1 +$0.6328, RSI 65.2, R3 +$1.426 = +2.11%, R4a $12.01M; cluster {BTC,ETH,SOL,TAO,AVAX,SUI,LINK} would go 1→2/2 — still PASS R6a); **HYPE PASS** R1+R2+R2a+R3+R4a (R1 +$0.5414, RSI 56.7, R3 +$0.7266 = +1.21%, R4a $13.29M); **XRP PASS** R1+R2+R2a+R3+R4a (R1 +$0.005505, RSI 60.3, R3 +$0.004618 = +0.40%, R4a $9.43M); **SUI PASS** R1+R2+R2a+R3+R4a (R1 +$0.003251, RSI 56.4, R3 +$0.004169 = +0.54%, R4a $5.28M; cluster would 1→2/2); **TAO PASS** R1+R2+R2a+R3+R4a (R1 +$19.32, RSI 77.9 = +22.9 over floor / under cap by 2.1, R3 +$52.63 = +23.6%, R4a $19.27M; cluster would 1→2/2; RSI 77.9 is the highest in the universe and within 2.1 of the 80 climactic-veto, but rule 2a is a strict ≤80 not <80 so this is mandate-eligible); **XDG PASS** R1+R2+R2a+R3+R4a (R1 +$0.0004057, RSI 57.6, R3 +$0.001139 = +1.31%, R4a $3.68M); **NEAR PASS** R1+R2+R2a+R3+R4a (R1 +$0.03047, RSI 58.3, R3 +$0.0247 = +1.17%, R4a $4.41M); ADA FAIL R2 (RSI 54.9) + R3 (-$0.000482); LINK FAIL R1 (-$0.003234) + R2 (RSI 51.3); LTC FAIL R4a ($1.91M < $2.0M); FARTCOIN FAIL R1+R2+R3+R4a; TRX FAIL R1+R2+R3+R4a; AVAX FAIL R3 (-$0.1379) + R4a ($0.84M). **Eligible candidates (7):** SOL (rank 3), HYPE (4), XRP (5), SUI (6), TAO (7), XDG (8), NEAR (9). **Rule 5b cooldowns:** all 7 candidates' most recent close >24h ago (SOL 22d ago, HYPE 22d, XRP 14d, SUI never, TAO entered & exited this morning at 09:00Z = 19h ago — **TAO 5b INACTIVE because the exit was `exit-4R-target` not `exit-stop-hit`**; 5b specifically gates same-pair re-entry after a stop-out, not after a take-profit. XDG never, NEAR never). **Rule 6:** 1/4 used — PASS for a 2nd entry. **Rule 8 (highest 30d notional rank):** SOL wins (rank 3 > HYPE 4 > XRP 5 > SUI 6 > TAO 7 > XDG 8 > NEAR 9). **Rule 7 sizing — CASH-BINDING BLOCK:** ideal SOL trade @ 1.5% risk on $10,930.40 equity = $163.96 risk; stop distance 2×ATR = $0.91043; ideal size = 180.10 SOL = $12,402 notional. Available cash = **$92.25** — fundable size capped to 1.338 SOL = $92.21 notional (99.96% of cash), risk $1.22 = **0.011% of equity** (vs 1.5% target). Roundtrip commission @ 0.52% on $92.21 = $0.48 = 39% of the trade's stop risk; a +4R win nets +$4.40 (+0.04% equity), a −1R loss nets −$1.70 (−0.016% equity) — both below any meaningful R-impact. **Decision: defer SOL entry.** The strategy v0.4 sizing path does not contemplate micro-positions where commission friction exceeds 1/3 of the stop risk; same call as routine-01 morning's note that "the cash-binding BTC entry sizing is the first time post-major-win that the next opportunity hit a cash cap; logged for routine #4 review on whether rule 8 should accept lower-ranked but fully-fundable candidates as an alternative." **The block applies to all 7 eligible candidates** — no candidate is fundable above the friction floor while BTC consumes 99.16% of equity in a single concurrent position. **Structural state:** while BTC carries open, no second concurrent entry will pass the friction floor unless (i) BTC closes (4R take-profit / stop trip / two-bar EMA20 exit) freeing cash, or (ii) the strategy is amended (routine-04 backlog). **0 trade_log writes this wake.** **Telegram: mandatory EOD card sent** per routine §NOTIFY. **Next on-schedule wake:** routine-01-overnight 2026-06-15T13:00Z (Mon 06:00 PT — Sun off per cron). BTC position carries unmanaged ~33h between this fire (04:11Z Sun in UTC = Sat 21:11 PT) and Mon routine-01; protective layers: 2×ATR stop $63,720.62 ($792 / 1.23% below last close), rising 1H EMA20 ($63,762, $750 below close), +0.69R cushion already accrued.

> **Prior rebuild (Sat midday):** 2026-06-13T20:07Z routine-02-midday (Sat 13:07 PT off-schedule fire — cron is Mon-Fri `0 13 * * 1-5`, framework dispatched anyway; same off-schedule treatment as the morning routine-01 wake). Position management only; no events. BTC position 5 closes deep, all above EMA20, lowest low $63,893.2, +0.05R unrealized. Equity $10,879.85, peak unchanged, DD 0.00%. **All clear** (kill switches). No Telegram (no notify-trigger met).

> **Prior rebuild (Sat AM):** 2026-06-13T15:50Z routine-01-overnight (off-schedule Sat fire). **TWO MATERIAL EVENTS — TAO/USD 4R take-profit replay close 2026-06-13T09:00Z $237.3015 = +4.04R / +$621.22 (entered prior EOD @ $217.286; the 09:00 UTC bar was inside the Fri-EOD's flagged 60+h unmanaged weekend window — replay convention takes the exit at the first 1H close that satisfied the rule). + BTC/USD long entry 2026-06-13T15:00Z $64,188.10 size 0.168 (sole rule-1 PASS that also cleared R2/R2a/R3/R4a; rule 8 selected over SOL/SUI/XDG on rank); per-trade risk 0.72% (cash-binding, ideal 1.5% sizing was 0.349 BTC blocked by spot-only mandate).** Equity $10,254.63 → $10,875.85 (+6.06%), NEW peak (prior $10,728.95). Loss streak reset to 0 (TAO winning close breaks 4-loss streak). Telegram dual-event notify sent.

> **Prior rebuild (Fri EOD):** 2026-06-13T04:10Z routine-03-eod (Fri 21:10 PT — 2026-06-12 PT trading day EOD). First entry since XRP exit 2026-05-30 — TAO/USD long opened at 21:00 PT 1H close $217.286. Equity $10,254.63, DD 4.42%, loss-streak 4, regime 4/15 positive (zero-buffer 5a marginal PASS), SBD cleared. Telegram EOD card sent.

## Account

- Starting equity: **$10,000.00**
- Cash: **$92.25** (unchanged — no events this wake)
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
- Unrealized PnL (open positions): **+$54.55** (BTC last 1H close $64,512.8 vs entry $64,188.10, gross; R-multiple +0.69)
- Position values (MTM): **$10,838.15** (BTC 0.168 × $64,512.8 from 03:00 UTC 1H close; spot $64,490.3 mid-04:00 bar)
- Current equity (cash + positions MTM): **$10,930.40**
- Equity peak: **$10,875.85** (set 2026-06-13T09:00Z at TAO 4R close — peak tracks realized closes; MTM $54.55 above does not advance)
- Drawdown from peak: **0.00%** (MTM above peak)
- Since-inception return: **+9.30%** ($10,930.40 / $10,000 − 1)

## Open positions

| Pair | Side | Size | Entry | Entry time (UTC) | Stop | 4R target | Risk ($) | Risk (% equity) | Unrealized R |
|------|------|------|-------|------------------|------|-----------|----------|------------------|--------------|
| BTC/USD | long | 0.168 | 64188.10 | 2026-06-13T15:00:00Z | 63720.62 | 66058.02 | 78.54 | 0.72% | +0.69 |

Portfolio risk-at-moment: **0.72%** of equity (cap 4%).
Open positions: **1 / 8** (strategy v0.4 max-concurrent 4 → 1/4 used; cluster {BTC,ETH,SOL,TAO,AVAX,SUI,LINK} 1/2 — BTC is in cluster).

## Day summary — 2026-06-13 PT

| Metric | Value |
|---|---|
| Day realized PnL | **+$621.22** (TAO 4R replay) |
| Day realized % | **+6.06%** (on day-open equity $10,254.63) |
| Day MTM PnL (incl. BTC unrealized) | **+$675.77** |
| Day total return MTM | **+6.59%** |
| Trades opened today | **1** (BTC/USD long @ 08:00 PT) |
| Trades closed today | **1** (TAO/USD 4R replay @ 02:00 PT, replay processed 08:50 PT) |
| Win rate today | **100%** (1/1) |
| Equity at EOD (MTM) | **$10,930.40** |
| Equity peak (realized) | **$10,875.85** (new, set this morning) |
| Drawdown from peak | **0.00%** |
| Loss streak | **0** (reset this morning) |

## Active kill-switch state

- Daily realized 2026-06-13 PT: **+$621.22 / +6.06%** — loss cap is downside-only, CLEAR.
- Consecutive losing trading days: **0** (TAO winning close broke 4-loss streak 05-22/05-25/05-26/05-30).
- Max drawdown: **0.00%** from peak $10,875.85 (cap 25%, warn 12.5%) — CLEAR.
- Equity floor: $10,930.40 (MTM) > $7,500 floor — CLEAR.
- Regime gate (rule 5a) — **03:00 UTC 1H/4H close via `scripts/indicators.py`**: **15/15 positive, median +1.90%** → **5a PASS** (well clear of 4-pair floor — breadth has continued to lift from this morning's 11/15 +0.52% print). **5a-SBD CLEARED** (15 > 1 AND +1.90 > -1.0).
- No active 5b cooldowns. TAO exited this morning on 4R target (not stop-hit) → 5b inapplicable; BTC entry 2026-06-13 not a re-entry; all other universe pairs' most recent close >24h ago.
- **Watchdog (`scripts/watchdog.py --telegram` @ 04:10:48Z):** `ALL CLEAR — heartbeats, timestamps, tree, MTM, scheduler flag, push state, MCP paths OK`.
- **All clear (kill switches).** routine-03-eod 2026-06-14T04:11Z (Sat 21:11 PT — 2026-06-13 PT EOD): **0 OPENs, 0 CLOSEs.** Kraken MCP AVAILABLE (`kraken_multi_ticker` + `kraken_ohlcv` 20-bar fetch both clean; indicators script 15/15 clean 720-bar pulls in <30s). **Telegram: mandatory EOD card sent.** Next on-schedule wake: routine-01-overnight 2026-06-15T13:00Z (Mon 06:00 PT). **Weekend remaining:** BTC position carries unmanaged ~33h between this fire and Mon routine-01. 2×ATR stop $63,720.62 is the protective floor (BTC last 1H close $64,512.8, stop is $792 / -1.23% away; spot $64,490.3, stop is $770 / -1.19% away).

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
  - Exit rule 1 (W22-G): two consecutive 1H closes < 1H 20-EMA ($63,762). Active. Inert — 13/13 post-entry closes above EMA, lowest post-entry close $63,944.3 = $182.3 above.
  - Exit rule 1-SBD: inert (SBD cleared 15/15 positive +1.90%; trend exit stays at 20-EMA default).
  - Exit rule 2 (stop): $63,720.62. Not pierced (lowest intra-bar low post-entry $63,893.2, $172.58 above stop). Will ratchet to breakeven $64,188.10 once +2R reached at any 1H close (≥ $65,123.06). Highest post-entry 1H close $64,560.9 → ratchet not armed (gap $562.16).
  - Exit rule 3 (4R target): $66,058.02. Not hit (highest post-entry high $64,750.0, gap $1,308).
  - Next exit-check wake: routine-01-overnight 2026-06-15T13:00Z (Mon 06:00 PT). Sun bars will close unmonitored — static stop + rising EMA20 are the protection.

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | ≈ +6.06% realized (+6.59% MTM, TAO 4R dominates) | ≈ +2.0% (BTC ~$63.2k → $64.5k over 7d) | ≈ +4.0–4.6% | BULL ahead on 7d |
| 30d | ≈ +9.30% (inception $10k 2026-04-20; window fully computable) | ≈ −21.0% (BTC 2026-05-13 ~$81.3k → today $64.5k) | ≈ +30.3% | BULL well ahead |
| 90d | — | — | — | not computable (BULL inception 2026-04-20 = 54 days ago; window first computable ~2026-07-19) |

(7d / 30d figures approximate — precise reference-price computation deferred to routine #4. BTC reference $64,490.3 spot this wake. The TAO 4R take-profit replay is the dominant performance driver this week; the day's MTM total return of +6.59% on a single trading PT day is the largest single-day swing since SOL +4R 2026-05-11. The cash-binding observation made this morning is reinforced by tonight's entry-scan outcome — 7 mandate-eligible candidates with no fundable size while BTC consumes 99.16% of equity. Routine #4 backlog item: "rule 8 acceptance of lower-ranked but fully-fundable candidates" gained a second data point this wake — quantify the EV of waiting for BTC to resolve vs. a friction-dominated micro-add.)
