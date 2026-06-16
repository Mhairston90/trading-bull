# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md` by whichever routine is running.
> `trade_log.md` is the source of truth; this file is a derived snapshot.
> **Last rebuild:** 2026-06-16T20:08Z routine-02-midday (**on-schedule cron fire**, `0 13 * * 1-5` PT = 20:00 UTC). **MATERIAL EVENT — ETH/USD 5.1162 stop-out exit replay 2026-06-16T15:00Z.** **State-of-record anomaly detected at wake start:** trade_log.md had an uncommitted ETH OPEN row (12:00:00Z entry @ $1797.88, stop $1766.13, target $1924.87, tag `entry-rule-v0.4-momentum`) added at file mtime 12:17:29 UTC — **96 seconds after** the prior routine-02-midday flat-book commit `e5f89f6` at 12:15:52 UTC. No routine-01-overnight commit exists between then and now (cron `0 6 * * 1-5` PT was due to fire at 13:00 UTC but no commit appeared on `main`). Matches the known replay-race archetype (cf. 2b5e27e BTC -0.60R race correction 2026-06-14): a concurrent or aborted routine-01 wrote the OPEN row to trade_log.md but failed to commit. **Per CLAUDE.md / skills/log-trade.md, trade_log is canonical source of truth — position is real, this routine processes it.** Entry sizing math is internally consistent with strategy v0.4 (5.1162 × $31.75 stop-distance = $162.44 risk = 1.5% × $10,828.58 prior equity). **Sole irregularity:** the orphan OPEN row used the bar close $1797.88 with no 0.05% adverse slippage applied (conservative model would have logged $1798.78). The row is canonical-as-logged per "Never rewrite past rows" rule; the unfavorable consequence is recorded only on the exit side. Static 2×ATR stop $1766.13 was pierced intrabar on the 2026-06-16T14:00Z 1H bar (low $1762.78, $3.35 below stop) **before** the W22-G two-bar EMA20 confirmation would have fired on that same bar close (both rule 1 and rule 2 triggered on the 14:00Z bar; rule 2 stop intrabar pierce precedes rule 1 bar-close confirm). Exit fill = stop × 0.9995 = **$1765.25** with 0.05% adverse slippage per `skills/decide.md`. Realized PnL: 5.1162 × ($1765.25 - $1797.88) gross = -$166.94, commission 0.26% × 5.1162 × ($1797.88 + $1765.25) = $47.39, **net -$214.33 / -1.32R**. (R is worse than typical -1.0x stop-hit precedent because the orphan entry skipped slippage — effective adverse range $32.63 vs design $31.75, plus commission load on small-relative-to-equity risk.) **Equity:** $10,614.25 (cash). **Peak unchanged.** **Drawdown 2.40%** — CLEAR. **Kill switches all CLEAR.** **Telegram: exit-event notify sent** per routine-02 NOTIFY rule (exit happened). **Live breadth (informational):** **4/15 positive 24h** via `kraken_multi_ticker` 20:08Z (positives AVAX +0.34 / FARTCOIN +5.60 / HYPE +8.67 / SUI +0.13; median TRX -0.58%); 5a marginal-PASS at exactly the 4-floor, SBD CLEAR. Note material session move: BTC last $65,621.8 (-1.45% vs 15:16Z print $66,584.5), 24h -1.0%, sharper than the 12:30Z/15:16Z reads. Next routine: routine-03-eod tonight at 04:00Z Wed (cron `0 21 * * 1-5` PT).

> **Prior rebuild (Tue midday, second wake — early cron fire):** 2026-06-16T15:16Z routine-02-midday (early fire ~4.75h before scheduled 20:00Z slot). Flat-book carry forward. Equity $10,828.58, DD 0.43%. No writes, Telegram silent. **[This rebuild did NOT see the ETH OPEN, which was added to trade_log.md at 12:17:29Z — chronologically *before* the 15:16Z rebuild yet the rebuild reported flat book. This is the central evidence the orphan write happened in the narrow seconds-window between the 12:15:52Z commit and the 15:16Z rebuild's read, with the rebuild having loaded its file snapshot pre-write. The orphan write was thus invisible to two subsequent rebuilds (15:16Z midday and this 20:08Z midday's pre-read) until this routine's read at session start.]**

> **Prior rebuild (Tue midday pre-cron):** 2026-06-16T12:30Z routine-02-midday (off-schedule fire ~7h pre-cron). Flat book carry forward from Sun BTC exit. Equity $10,828.58, DD 0.43%, breadth 14/15 +1.27% median. No writes, no exits, Telegram silent.

> **Prior rebuild (Sun AM):** 2026-06-14T17:14Z routine-01-overnight (**Sun off-schedule fire**). BTC/USD 0.168 stop-out exit replay 2026-06-14T13:00Z via Exit rule 1 (W22-G two-bar EMA20 confirm). Realized -0.60R / -$47.27 net. Equity $10,828.58, DD 0.43%, loss streak 0→1.

## Account

- Starting equity: **$10,000.00**
- Cash: **$10,614.25** (was $10,828.58; -$214.33 from ETH stop close)
- Realized PnL (all-time): **+$614.25** (was +$828.58; -$214.33 on ETH stop)
  - [archived earlier rows trimmed for brevity — full ledger preserved in trade_log.md]
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
  - BTC −$47.27 (missed-scheduler replay exit-ema20-confirm 2026-06-14T13:00Z, −0.60R)
  - **ETH −$214.33 (missed-scheduler replay exit-stop-hit 2026-06-16T15:00Z, −1.32R)** — new this wake
- Unrealized PnL (open positions): **$0.00** (no open positions)
- Position values (MTM): **$0.00**
- Current equity (cash + positions MTM): **$10,614.25**
- Equity peak: **$10,875.85** (set 2026-06-13T09:00Z at TAO 4R close — unchanged)
- Drawdown from peak: **2.40%** ($261.60 below peak)
- Since-inception return: **+6.14%** ($10,614.25 / $10,000 − 1)

## Open positions

*(none — ETH closed at stop this wake)*

Portfolio risk-at-moment: **0.00%** of equity (cap 4%).
Open positions: **0 / 8** (strategy v0.4 max-concurrent 4 → 0/4 used; cluster {BTC,ETH,SOL,TAO,AVAX,SUI,LINK} 0/2).

## Day summary — 2026-06-16 PT (Tue, this wake)

| Metric | Value |
|---|---|
| Day realized PnL | **-$214.33** (ETH stop-hit replay) |
| Day realized % | **-1.98%** (on day-open equity $10,828.58) |
| Day MTM PnL | **-$214.33** (no other positions) |
| Trades opened today | **1** (ETH/USD orphan-write entry, logged 12:17:29Z by uncommitted routine-01) |
| Trades closed today | **1** (ETH/USD 5.1162 long @ 14:00Z UTC bar via intrabar stop pierce) |
| Win rate today | **0%** (0/1) |
| Equity at this wake | **$10,614.25** (cash, no positions) |
| Equity peak (realized) | **$10,875.85** (unchanged) |
| Drawdown from peak | **2.40%** |
| Loss streak | **2** (BTC Sun -0.60R + ETH Tue -1.32R, two consecutive losing trade-days — but only one trade per day so loss-streak-by-day is also 2) |

## Active kill-switch state

- Daily realized 2026-06-16 PT: **-$214.33 / -1.98%** — loss cap 5% (2.5x below), CLEAR.
- Consecutive losing trading days: **2** (BTC Sun -0.60R, ETH Tue -1.32R; cap 7, 5 trades of headroom).
- Max drawdown: **2.40%** from peak $10,875.85 (cap 25%, warn 12.5%) — CLEAR.
- Equity floor: $10,614.25 > $7,500 floor — CLEAR.
- Regime gate (rule 5a) — **live 24h via `kraken_multi_ticker` 20:08Z**: **4/15 positive (AVAX/FARTCOIN/HYPE/SUI), median -0.58%** → **5a marginal-PASS at floor** (4 == 4 floor). **5a-SBD CLEAR** (4 > 1 positive AND median -0.58% > -1.0% threshold; either condition alone clears SBD).
- Active 5b cooldowns: **ETH 2026-06-16T15:00Z exit-stop-hit — 5b active until 2026-06-17T15:00Z** (24h same-pair re-entry cooldown applies; stop-out tag → rule 5b APPLICABLE — first active 5b cooldown since 2026-05-25 BTC stop).
- **Watchdog:** not run this wake (routine-02 spec doesn't require it; the pre-existing trade-log mtime mismatch was caught manually via diff inspection).
- **All clear (kill switches).** routine-02-midday 2026-06-16T20:08Z (Tue 13:08 PT — on-schedule cron fire ~8 min late): **1 CLOSE** (ETH stop replay), **0 OPENs** (midday spec forbids entries). Kraken MCP AVAILABLE (`kraken_ticker` ETHUSD + `kraken_ohlcv` 30-bar 1H + `kraken_multi_ticker` 15-pair all clean <3s). **Telegram: exit-event notify sent** per routine §NOTIFY (CLOSE event triggers brief summary; orphan-write anomaly also flagged in the message body for visibility, not because routine §NOTIFY mandates it — discretionary inclusion given the state-of-record concern).

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

*(none — flat after ETH stop close)*

## Rolling performance

| Window | BULL return | BTC-hold return | Delta | Result |
|--------|-------------|-----------------|-------|--------|
| 7d | ≈ +3.60% realized (TAO +4.04R / +6.21%, BTC -0.60R / -0.43%, ETH -1.32R / -1.98%) | ≈ +3.8% (BTC ~$63.2k → $65.6k over 7d) | ≈ -0.2% | BULL roughly tied on 7d (slight underperformance from today's ETH stop give-back; the TAO 4R win is no longer a clean dominator) |
| 30d | ≈ +6.14% (inception $10k 2026-04-20; window fully computable) | ≈ −19.3% (BTC 2026-05-13 ~$81.3k → today $65.6k) | ≈ +25.4% | BULL well ahead |
| 90d | — | — | — | not computable (BULL inception 2026-04-20 = 57 days ago; window first computable ~2026-07-19) |

(7d / 30d figures approximate; BTC reference $65,621.8 spot this wake. The ETH stop today is a clean illustration of the loss-cap mechanism doing its job in a sub-$10 adverse intrabar move — the 14:00Z bar low $1762.78 was only $3.35 below the stop $1766.13, and the stop fill at $1765.25 captured roughly the design adverse range. **Caveat:** the orphan-write entry skipped the conservative 0.05% slippage model on the entry side, which is the proximate cause of -1.32R rather than the typical -1.05R-to-1.10R stop-hit R. Documented in research_log for routine-04 lesson-eligibility evaluation. Inception-to-date return slipped from +9.30% peak to +6.14% — a -3.16% retracement, second-worst since strategy launch, but well inside drawdown caps and consistent with the long-only-strategy-in-bearish-tape archetype.)
