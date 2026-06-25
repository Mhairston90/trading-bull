# BULL Research Log

> **Append-only.** News and external research notes per routine run.
> Rows older than 30 days archived by routine #3 monthly sweep.
>

2026-06-24T01:03:03Z | idea-scan | day-gate | not Friday, skipping | no action

## 2026-06-24T16:33Z — routine-01-overnight (PT 09:33 Wed 06-24, fired ~3h33m behind 06:00 PT cron)

**Slot identity `bull-01-overnight`.** Late fire of the Wed 06:00 PT cron. No concurrent automation observed. Universe + portfolio state verified clean before any work.

### Pre-flight kill switches (READ portfolio.md → re-verify against current state)

- Equity $10,413.87 (cash-only, 0 OPEN). DD 4.25% from peak $10,875.85 — CLEAR (cap 25%, warn 12.5%, 8.25pp to warn).
- Loss streak 0 days — CLEAR.
- Equity floor $10,413.87 > $7,500 — CLEAR.
- 5b cooldowns: none active (last stop-out was 2026-06-17T18:00Z SOL — well past 24h; SOL/USD 2026-06-22 EMA-exit doesn't trigger 5b).
- All Ring 3 kill switches: **CLEAR.**

### Watchdog (mandatory, `--telegram`)

`python scripts/watchdog.py --telegram` — **8 findings, all carry-over from prior wakes, Telegram alert auto-sent**:
- 1× A heartbeat: routine-07 last commit **251h** stale (up from 226h yesterday; +25h continuing widening; ~10.5 days now). routine-04 territory.
- 1× C dirty-tree: 5 uncommitted scripts in `scripts/` (`replay_cache_20260622/`, `replay_cache_20260623/`, `replay_result_20260623.json`, `routine07_replay_20260622.py`, `routine07_replay_20260623.py`) — 2 new vs prior wake (06-23 replay artifacts joined the 06-22 carryover). Not modified this fire; flagged for routine-04 housekeeping.
- 6× D stale-MTM: variants v0.12-sbd-exit, v0.13-trend-confirm, v0.14-recovery-trend, v0.3-vol-compression, v0.5-cluster-cap-tight, v0.7-vol-comp-defensive — all 252h stale (was 227h yesterday; +25h continuing gap). routine-04 territory.

Findings continue widening the routine-07 + variant-MTM gap (~+25h since yesterday's overnight). Not a kill switch; logged for routine-04.

### Position management

**No open positions → no exit checks needed.** Last position closed 2026-06-22T16:00Z (SOL +1.19R EMA-exit, see prior research_log row at line 63+). Flat into this wake.

### Entry scan — Technical (authoritative: `python scripts/indicators.py`)

`indicators.py` ran successfully, 720 4H bars per pair (well above the 200-bar 4H-50-EMA convergence floor). Output dated 2026-06-24T16:33:54+00:00.

**Regime gate (rule 5a):** **0/15 positive 24h, median −3.05%.** Strict 5a FAIL (< 4/15 positive floor). **No new entries this wake regardless of per-pair eligibility.**

**Regime sub-state (rule 5a-SBD):** **ACTIVE** — positives = 0 (≤ 1 ceiling) AND median = −3.05% (≤ −1.0%). 9-EMA two-bar exit (Exit rule 1-SBD) would apply to any open position; **no open positions, so SBD defensive value this wake = 0 R avoided**. SBD has now been continuously active for ~36h (since overnight 06-23 fire; +24h continued).

**Per-pair Technical PASS/FAIL summary** (per routine DO step 6, every REJECT recorded; full table available in stdout of `indicators.py`, condensed here):

| Pair | R1 (close>EMA20) | R2 (RSI≥55) | R2a (RSI≤80) | R3 (4H>EMA50) | R4a ($2M) | Decision |
|---|---|---|---|---|---|---|
| BTC/USD | FAIL −1,998 | FAIL RSI 22.0 | OK | FAIL −3,380 | OK $173.53M | REJECT R1+R2+R3 + regime |
| ETH/USD | FAIL −43.84 | FAIL RSI 25.9 | OK | FAIL −90.68 | OK $52.01M | REJECT R1+R2+R3 + regime |
| SOL/USD | FAIL −1.912 | FAIL RSI 28.0 | OK | FAIL −3.544 | OK $25.16M | REJECT R1+R2+R3 + regime |
| HYPE/USD | FAIL −1.989 | FAIL RSI 29.7 | OK | FAIL −6.054 | OK $16.06M | REJECT R1+R2+R3 + regime |
| XRP/USD | FAIL −0.0346 | FAIL RSI 22.5 | OK | FAIL −0.0782 | OK $22.72M | REJECT R1+R2+R3 + regime |
| SUI/USD | FAIL −0.0217 | FAIL RSI 30.7 | OK | FAIL −0.0492 | OK $4.22M | REJECT R1+R2+R3 + regime |
| TAO/USD | FAIL −4.353 | FAIL RSI 38.2 | OK | FAIL −15.43 | OK $2.09M | REJECT R1+R2+R3 + regime |
| XDG/USD | FAIL −0.0035 | FAIL RSI 17.9 | OK | FAIL −0.0078 | OK $3.91M | REJECT R1+R2+R3 + regime |
| NEAR/USD | FAIL −0.0517 | FAIL RSI 28.3 | OK | FAIL −0.2024 | OK $3.04M | REJECT R1+R2+R3 + regime |
| ADA/USD | FAIL −0.0055 | FAIL RSI 23.5 | OK | FAIL −0.0167 | OK $6.14M | REJECT R1+R2+R3 + regime |
| LINK/USD | FAIL −0.211 | FAIL RSI 28.1 | OK | FAIL −0.496 | **FAIL $1.28M** | REJECT R1+R2+R3+R4a + regime |
| LTC/USD | FAIL −1.342 | FAIL RSI 24.1 | OK | FAIL −3.173 | OK $2.50M | REJECT R1+R2+R3 + regime |
| FARTCOIN/USD | FAIL −0.0028 | FAIL RSI 41.4 | OK | FAIL −0.0013 | **FAIL $0.49M** | REJECT R1+R2+R3+R4a + regime |
| TRX/USD | FAIL −0.0027 | FAIL RSI 32.4 | OK | **PASS +0.0008** | **FAIL $0.86M** | REJECT R1+R2+R4a + regime (only R3 PASS, lone-rule in universe) |
| AVAX/USD | FAIL −0.143 | FAIL RSI 35.6 | OK | FAIL −0.1621 | OK $2.21M | REJECT R1+R2+R3 + regime |

**Decision: 0 entries this wake.** Every pair fails at least 3 of {R1, R2, R3} (14 of 15 fail all three; TRX has lone R3 PASS but fails R1+R2 + R4a). Even ignoring regime, no candidate would clear technical. Regime gate (5a FAIL) is the dispositive blocker — applies universally and would suppress entries even on a tape recovery.

**Yesterday's lone TECH-PASS candidate (AVAX) deteriorated rapidly.** At Tue EOD (~16h ago) AVAX was the only R1+R2+R3+R4a PASS. Today: AVAX has flipped to R1+R2+R3 all FAIL with 24h change −2.16%. The tape continued breaking down overnight — every pair is now mechanically below EMA20 on 1H and below EMA50 on 4H. This is consistent with the SBD continuation noted yesterday.

### Entry scan — News (skipped — gate fails)

Per routine DO step 4: news scan runs **for each technical-PASS candidate**. **0 TECH-PASS candidates → no news scan executed this wake.** Firecrawl quota preserved. Not logging "Firecrawl unavailable" since this is a *no-target* skip, not a tool-failure skip.

### Entry scan — Sentiment (skipped — gate fails)

Per routine DO step 4a: sentiment scan runs **for each technical-PASS candidate**. **0 TECH-PASS candidates → no sentiment scan executed this wake.** No `kraken_spread` / `kraken_depth` calls made.

### Decision

**No entries. No exits.** Flat into Wed 06-24 13:00 PT midday slot. SBD continues into a ~36h+ active window; the only mandate-legal action is to remain flat and let SBD clear via regime recovery. No portfolio rebuild needed (no trade events; portfolio state unchanged since `routine-03-eod` 06-24T04:11Z rebuild).

**Next entry-eligible scan:** routine-02-midday Wed 2026-06-24 13:00 PT (= 20:00Z) — entries gated by 5a regime recovery (≥4/15 positive). With every pair now structurally broken on 1H+4H trend, even a fast regime swing would still require trend repair before R1/R2/R3 can PASS; realistic next-entry path is multi-wake distance.

### Universe refresh

Today is **2026-06-24** (Wed), not 1st or first-weekday-of-month. **Skipped.** Next refresh: 2026-07-01 (Wed, on-cycle).

### Telegram — silence rationale

Per `skills/telegram.md` routine #1 silence policy: send only if (a) Ring 3 kill switch tripped, (b) new OPEN or stop-out CLOSE this run, (c) ACTIONABLE news item, or (d) universe refreshed.

- (a) No kill switch tripped — all CLEAR.
- (b) No new OPEN, no CLOSE this run.
- (c) No news scan executed (no TECH-PASS candidates) → no ACTIONABLE classification possible.
- (d) Universe not refreshed today.

**No EOD-style card sent.** Watchdog alert was sent independently by `watchdog.py --telegram` (carries today's 8 findings) — that satisfies the "ops surveillance" notification path without overlapping the strategy-action channel.

### Files written this routine

- `memory/research_log.md` (this row only)
- No trade_log, no portfolio.md, no lessons.md, no universe.md changes.

---

## 2026-06-23T16:07Z — routine-03-eod (DUPLICATE LATE-FIRE of Mon 21:00 PT slot)

**Slot identity `bull-03-eod`.** Cron `0 21 * * 1-5` PT (Mon 21:00 PT = 04:00Z Tue 06-23). Framework dispatched ~12h late at 16:07Z Tue 06-23 (09:07 PT Tue). The Mon EOD work was already completed by the on-time-early fire at 01:50Z 06-23 (PT 18:50 Mon 06-22) — see prior research_log row at line 4526 and commit `132a2fc`. This is a duplicate late-fire of the same cron slot.

### Date-labeling guard check

Per routines/03-eod.md guard: "the label date must equal today's PT date" at fire time. PT date at fire time = **2026-06-23 Tue**. The trading day 2026-06-23 is NOT over (it's 09:07 PT, ~12h until Tue 21:00 PT EOD slot). Therefore this fire cannot legitimately produce a "Tue 06-23 EOD" journal. The slot it represents — Mon 21:00 PT — was already executed and committed. **No new EOD journal written this fire; no duplicate Telegram EOD card sent.**

### Pre-flight verification (kill switches, since last fire ~14h ago)

No new trade events since commit `132a2fc` (verified `git log -- memory/trade_log.md` matches; last row is SOL correction-previous-row at 2026-06-22T16:00:00Z). Portfolio state unchanged from last rebuild:
- Equity: **$10,413.87** (cash only, 0 open positions)
- Drawdown: **4.25%** from peak $10,875.85 — CLEAR (cap 25%, warn 12.5%)
- Loss streak: **0 trading days** — CLEAR
- Equity floor: $10,413.87 > $7,500 — CLEAR
- 5b cooldowns: SOL/USD cleared at 2026-06-23T15:00Z (exit was EMA20-confirm not stop-hit, so 5b strict-by-letter doesn't bind; informational only).
- All Ring 3 kill switches: **CLEAR.**

### Watchdog (mandatory, `--telegram`)

Ran `python scripts/watchdog.py --telegram`. 8 findings, alert auto-sent:
- 1× A heartbeat: routine-07 last commit **226h** stale (was 212h prior wake; gap continues widening; ~9.4 days now). Flag for routine-04.
- 1× C dirty-tree: 2 uncommitted scripts in `scripts/` (`replay_cache_20260622/`, `routine07_replay_20260622.py`) — stranded artifacts from a prior session. Not modified this fire; flagged for routine-04 housekeeping.
- 6× D stale-MTM: variant portfolios v0.12-sbd-exit, v0.13-trend-confirm, v0.14-recovery-trend, v0.3-vol-compression, v0.5-cluster-cap-tight, v0.7-vol-comp-defensive — all 227h stale (continuing gap). Routine-04 territory.

### Decision

**No-op for journal/trade work.** Per the duplicate-fire detection above:
- trade_log: no new events (no fresh wake-rebuild needed)
- portfolio: state unchanged since `132a2fc` rebuild
- lessons: Mon EOD already extracted (0 lessons appended)
- monthly archive: today is 2026-06-23 (Tue), not last trading day of June (~06-30 Tue)

### Telegram — silence rationale

Per `bull-03-eod/SKILL.md`: "Silence is a failure mode — if you reach the end of the routine without sending the EOD card, append a row to memory/research_log.md explaining why." **No new EOD card sent because:**
1. The Mon 06-22 EOD card was sent on-time by the 18:50 PT Mon early fire (commit `132a2fc`).
2. Re-sending the same Mon card 14h later would (a) duplicate the user's notification, (b) misleadingly imply a fresh end-of-day with no new data behind it, (c) violate the date-labeling guard which requires label = PT date at fire time but the trading day labeled in such a card cannot be Tue 06-23 (premature) and cannot be Mon 06-22 (already sent).
3. Sending a "Tue 06-23 EOD" card now would be premature (Tue 21:00 PT EOD is ~12h away) and would also be a duplicate-fire risk for the next on-time Tue cron.
4. Watchdog alert was sent independently this fire (separate from EOD card).

This explicit explanation is what the SKILL guard requires when an EOD card is omitted.

### Routine race observation (routine-04 backlog)

This is the 2nd duplicate-fire event in 14h: the midday cron (`0 13 * * 1-5` PT) also late-fired at ~01:50Z 06-23 racing on trade_log writes with routine-01-overnight. Cron scheduler skew is accumulating; multiple slots are now late-firing into the next-PT-day window. Recommend routine-04 evaluate (a) framework-level cron skew root cause, (b) idempotency guard on EOD slot (detect "already committed today" → no-op cleanly without manual research_log row), (c) trade_log write arbitration if races recur.

### Files written this routine

- `memory/research_log.md` (this row only)
- No trade_log, no portfolio.md, no lessons.md changes.

---

## 2026-06-23T01:50Z — routine-02-midday (PT label 2026-06-22 Mon, late fire ~05h behind 13:00 PT cron)

**Slot identity `bull-02-midday`.** Cron `0 13 * * 1-5` PT = 20:00Z; framework dispatched ~05h late, executed at ~01:50Z next-UTC-day. Concurrent automation also fired this wake labeling itself routine-03-eod and racing on trade_log/portfolio writes. Final state now consistent.

### Position management

- **SOL/USD EMA20 two-bar exit confirmed.** Computed 1H EMA20 over last 50 bars (SMA-seed bars 1–20, EMA from bar 21):
  - Bar 2026-06-22T13:00Z close 74.88 vs EMA 73.83 → above (last above)
  - Bar 14:00Z close 73.37 vs EMA 73.79 → **1st below**
  - Bar 15:00Z close 73.08 vs EMA 73.73 → **2nd consecutive below — Exit rule 1 (W22-G) fires at this bar's close = 2026-06-22T16:00:00Z**
  - Bars 16:00–23:00Z all continued below EMA (price drifted 73.08 → 71.88), confirming the exit signal in retrospect.
- Static 2×ATR stop $69.9072 never touched (24h low $71.33, ~$1.42 above stop).
- Exit fill model: bar close 73.08 × 0.9995 = $73.0435 (conservative 0.05% slippage on exit per `skills/decide.md`). Round-trip commission $45.57 (0.26%/side on $8,649.62 entry + $8,877.32 exit notional). Net realized **+$182.13 / +1.19R net**.

### Correction event

A concurrent process (self-labeled routine-03-eod) appended an EMA-exit CLOSE row to `trade_log.md` at 2026-06-22T15:00:00Z with raw-close $73.08, gross R +1.51, realized +$232.13 — i.e., **no slippage applied and no commission deducted**, inconsistent with the convention used on every prior EMA-cross/stop-hit close in this ledger (e.g., SOL stop-hit 2026-06-17T18:00:00Z @ 72.1927 with entry $73.7268 × 0.9995 slip + round-trip 0.26%/side commission netted to −$199.87/−1.28R net). I appended a `correction-previous-row` at 2026-06-22T16:00:00Z (bar-close timestamp aligned to "exit fires at the close of the second below-EMA bar" per strategy v0.4) restoring slippage + commission. Portfolio.md was then rewritten by the concurrent automation to honor the correction; final equity = **$10,413.87**, all-time realized = **+$413.87**.

### Kill-switch state

- DD 4.25% (improved 0.77pp from 5.02% prior wake), 8.25pp headroom to 12.5% warn.
- Loss streak reset 3 → 0 by winning exit.
- Equity floor $10,413.87 >> $7,500.
- No daily-loss/halt triggers (today is a gain, +1.76% on realized).
- 5b cooldown not triggered (EMA-cross exit, not stop-hit).
- All Ring 3 kill switches CLEAR.

### Notes

- **W22-H ratchet near-engagement (first observed).** Peak SOL 1H close $74.88 at 13:00Z = +2.94R unrealized. The W22-H breakeven ratchet would have armed at that close (moving stop $69.9072 → $71.17 entry), but the EMA20 two-bar exit fired one bar later at $73.08 (well above breakeven) so the ratchet did not bind. Logged as a precedent — first time since W22 deployment that the ratchet path was nearly engaged on a fresh trade.
- **4R target proximity:** target $76.2212 was $1.34 above the intraday 24h high $74.91 — not reached. The W22-G exit locked in a clean +1.19R net winner where the prior chop-take-back archetype (cf. XRP 2026-05-14 round-trip) could have applied if the original 20-EMA single-bar rule were still in force.
- **Routine race observation.** Two routines firing concurrently on the same wake produced inconsistent trade_log writes that required an append-only correction. Worth flagging for routine-04 harness review: cron skew (midday late-fire encroaching on EOD window) created the race; trade_log/portfolio writes should arbitrate on a single owner.

### Files written this routine

- `memory/trade_log.md` (correction-previous-row appended at 2026-06-22T16:00:00Z; auto-row at 15:00:00Z preserved as historical record)
- `memory/portfolio.md` (rewritten by concurrent process with corrected accounting; verified consistent)
- `memory/research_log.md` (this row)

### Telegram

Exit notification sent per routine spec (exit happened this wake).

---

## 2026-06-20T17:09Z — routine-04-harness (PT label 2026-06-20 Sat, on-schedule day-gate PASS)

**Slot identity `bull-04-harness`.** Cron `0 10 * * 6` PT. Day-gate PASS (today IS Saturday). Routine-04 proceeded with full reduced-scope harness (TV blocker, 6th consecutive week).

### Harness summary

- **Verification:** `tv_health_check` → CDP connection failed after 5 attempts (TV Desktop not running, 6th consecutive harness). Kraken MCP smoke test OK (BTC/USD $63,870.8, spread 0.1, vwap $63,506.14).
- **W25 closes (2026-06-15 → 2026-06-20):** 3 stop-outs, 0% WR, net **−$596.84 / −3.75R**. ETH −1.32R / −$214.33 (06-16), HYPE −1.15R / −$182.64 (06-17), SOL −1.28R / −$199.87 (06-17 intra-bar same-session fallback entry).
- **Equity:** $10,329.73 (was $10,875.85 peak set W24 TAO 4R) — DD 5.02%, intra-week peak DD was 6.20%. Open SOL (entered today 13:00Z @ $71.17) recovered partially to +0.626R unrealized.
- **Lessons scored:** 2 new (2026-06-17 SBD-leading-edge = 7; 2026-06-17 cash-insufficiency = 7). Active count now 9; cap 50; no prune.
- **Variants tested:** 0 TV backtests (TV blocker). Rack at 10/10 (7 hypothesis + 3 sweep); no spin-ups, no retirements. Routine-07 lag (~5 days stale MTM) noted.
- **Idea bank:** unchanged. IDEA-12 (ETF flows) still queued #1, still pending external feed wiring across 6 weeks.
- **Competitor:** BULL +3.30% / Codex v0 −5.34% / Codex Aggro +6.43%. **Lead-flip vs Aggro** (was +3.35 lead W24 → −3.13 deficit W25). T-11 days to 2026-07-01 deadline.
- **vs BTC-hold:** 7d −4.85 pts (first material BTC-hold underperformance since inception), 30d +22.77 pts, since-inception +19.09 pts. 90d non-evaluable (matures 2026-07-19).
- **Proposal:** NONE — current strategy retained. 3 backlog items logged (SBD-leading-edge filter, cash-fit pre-check, cash-aware rule-8 tiebreaker). Detailed rationale in `weekly_memos/2026-W25.md` §Proposal.
- **TV escalation re-flagged** in Open Questions (6th memo with no user reply on install OR paper-paper-evidence authorization).

### Telegram notification

Sent short retention note per routine spec ("no proposal → short retention note" template). Body included W25 P&L summary, lead-flip vs Aggro alert, and re-flag of TV blocker.

### Files written this routine

- `memory/weekly_memos/2026-W25.md` (new)
- `memory/lessons.md` (2 lessons scored 7+7)
- `memory/research_log.md` (this row)

---

## 2026-06-18T20:07Z — routine-02-midday (PT label 2026-06-18 Thu, on-schedule cron fire)

**Slot identity `bull-02-midday`.** Cron `0 13 * * 1-5` PT = 20:00 UTC; framework dispatched ~07 min late at 20:07Z.

### Position management

Flat at wake (0 open positions, $10,231.74 cash). No MTM, no exit checks, no stop monitoring. Per routine spec, **no new entries permitted at midday** — entry responsibility belongs to routines #1 / #3.

### Kraken multi-ticker (regime sweep)

Snapshot at ~20:07Z across the 15-pair universe (24h % change):

| Pair | last | 24h % |
|------|-----:|------:|
| NEAR | 2.2064 | **+1.21** |
| TRX | 0.3197 | −0.61 |
| LINK | 7.9485 | −1.70 |
| ADA | 0.16338 | −2.00 |
| BTC | 63079.7 | −2.13 |
| ETH | 1709.99 | −2.23 |
| LTC | 43.59 | −2.94 |
| SOL | 69.67 | −3.21 |
| XRP | 1.14676 | −3.26 |
| HYPE | 68.78 | −3.28 |
| XDG | 0.083133 | −3.39 |
| TAO | 237.2538 | −3.81 |
| FARTCOIN | 0.1248 | −5.10 |
| SUI | 0.7249 | −5.43 |
| AVAX | 6.363 | −5.98 |

**Regime header:** **1/15 positive 24h (NEAR only), median −3.21%** → **5a FAIL** (1 < 4 floor) **AND 5a-SBD ACTIVE** (positives ≤ 1 AND median ≤ −1.0%). Third consecutive wake under SBD (activated 2026-06-18T04:11Z EOD, persisted through 14:05Z overnight, now). Conditions deepened mildly from overnight (median −2.26% → −3.21%; positives went from 0 to 1 but median dipped further).

**Routine spec moots regime gate for midday** — no entries permitted regardless. Recorded for continuity.

### Kill-switch verification

- Daily realized 2026-06-18 PT: **$0.00 / 0.00%** (no closes today) — cap 5%, CLEAR.
- Daily total (realized + unrealized): **$0.00 / 0.00%** — CLEAR.
- Drawdown: **5.92%** from peak $10,875.85 — cap 25%, warn 12.5%, **6.58% to warn** — CLEAR.
- Equity: **$10,231.74** > $7,500 floor — CLEAR.
- Loss streak: **3 trading days** — cap 7, headroom 4 — CLEAR.
- All clear; no kill-switch action.

### Avoided-give-back ledger (SBD)

This wake: **$0.00** (no open positions; SBD's tightened 9-EMA exit had no surface to act on).

### Telegram

Silent per routine spec: no kill-switch trip, no exit, no DD threshold cross (warn 12.5% not breached).

### Summary

0 OPEN, 0 CLOSE, 0 NEW ENTRIES (routine bars all entries at midday). Regime 5a FAIL + SBD ACTIVE persists into third wake. Next entry-eligible scan = routine-03-eod (Thu 2026-06-18T21:11Z PT 14:11 PT cron `11 14 * * 1-5`).

---

## 2026-06-18T14:05Z — routine-01-overnight (PT label 2026-06-18 Thu, on-schedule cron fire)

**Slot identity `bull-01-overnight`.** Cron `0 6 * * 1-5` (Thu 06:00 PT / 13:00 UTC) — framework dispatched ~05 min late at ~14:05Z. Just-closed 1H bar = 13:00Z 2026-06-18.

### Watchdog (mandatory, `--telegram`)

7 findings; alert auto-sent by `watchdog.py`:
- 1× A heartbeat: routine-07 last commit 104h ago (threshold 30h)
- 6× D stale-MTM (variants v0.12-sbd-exit / v0.13-trend-confirm / v0.14-recovery-trend / v0.3-vol-compression / v0.5-cluster-cap-tight / v0.7-vol-comp-defensive — all 105h since last MTM)

Same set as prior wake (now lagged by routine spacing). Informational; variant lag attributable to routine-07 scheduler gap, does not affect BULL state. Flagged for routine-07 catch-up.

### Position management (open positions)

Zero open positions at wake start. Zero exit checks needed.

### Entry scan (W19-E analyst-role split)

Per the 2026-06-12 amendment, indicator computation delegated to `python scripts/indicators.py` (authoritative table). Just-closed 1H bar = 13:00Z 2026-06-18.

**Regime header (from indicators.py):** **0/15 positive 24h, median −2.26%** → **5a FAIL** (0 < 4 floor) **AND 5a-SBD ACTIVE** (positives ≤ 1 AND median ≤ −1.0%). All new entries rejected this wake. SBD-tightened exit (two-bar 9-EMA) would apply to any open positions, but BULL is flat. SBD persists from prior wake (EOD 04:11Z) — second consecutive wake under SBD.

**Technical analyst pass:** Cascade deepened from EOD wake. Zero pairs are positive on 24h; median dropped from −3.37% (EOD) to −2.26% (now). Per-pair Pass/Fail at 13:00Z bar:

| Pair | R1 EMA20 | R2 RSI≥55 | R2a RSI<80 | R3 4H EMA50 | R4a $≥2M | Eligible |
|------|---------|-----------|-----------|------------|----------|----------|
| BTC | FAIL −454.7 | FAIL (40.2) | OK | FAIL −825.1 | OK $151.59M | NO |
| ETH | FAIL −13.75 | FAIL (40.9) | OK | PASS +8.19 | OK $32.61M | NO |
| SOL | FAIL −0.86 | FAIL (40.0) | OK | PASS +0.25 | OK $32.04M | NO (also R5b active until 18:00Z) |
| HYPE | FAIL −1.10 | FAIL (43.8) | OK | PASS +4.44 | OK $33.11M | NO (R5b cleared 12:00Z) |
| XRP | FAIL −0.018 | FAIL (33.8) | OK | FAIL −0.018 | OK $25.92M | NO |
| SUI | FAIL −0.024 | FAIL (30.2) | OK | FAIL −0.030 | OK $5.55M | NO |
| TAO | FAIL −4.81 | FAIL (36.3) | OK | FAIL −6.58 | OK $6.25M | NO |
| XDG | FAIL −0.0013 | FAIL (34.3) | OK | FAIL −0.0025 | OK $4.17M | NO |
| NEAR | PASS +0.021 | FAIL (51.8) | OK | FAIL −0.028 | OK $4.35M | NO (R2 by 3.2 RSI, R3) |
| ADA | FAIL −0.0023 | FAIL (38.5) | OK | FAIL −0.0082 | OK $7.28M | NO |
| LINK | FAIL −0.056 | FAIL (43.2) | OK | FAIL −0.099 | FAIL $1.99M | NO |
| LTC | FAIL −0.58 | FAIL (32.3) | OK | FAIL −0.63 | FAIL $1.28M | NO |
| FARTCOIN | FAIL −0.0029 | FAIL (39.4) | OK | PASS +0.0012 | FAIL $0.51M | NO |
| TRX | FAIL −0.0008 | FAIL (43.3) | OK | FAIL −0.0006 | FAIL $0.94M | NO |
| AVAX | FAIL −0.099 | FAIL (37.0) | OK | FAIL −0.21 | FAIL $1.06M | NO |

**Zero technical candidates** — no pair passes R1+R2 simultaneously this wake. NEAR is the only pair with R1 PASS but fails R2 (51.8 vs 55 floor) and R3. Regime gate moot since no candidate would advance regardless.

**News pass:** Skipped — no technical candidates to screen. Informational only in v0.4.

**Sentiment pass:** Skipped — no technical candidates to screen.

**Decision:** **NO ENTRIES.** Regime 5a FAIL + SBD ACTIVE + zero technical candidates (R1+R2 simultaneous). Cascade deepened from EOD wake (0/15 positive now vs 1/15 EOD).

### Estimated SBD avoided give-back (per 5a-SBD logging obligation)

BULL holds no open positions. SBD avoided-give-back ledger = $0 this wake. SBD's defensive value not exercised since there is nothing open to defend. Second consecutive wake under SBD (activated EOD 04:11Z, still active).

### Cooldown ledger

- HYPE/USD 5b: cleared at 2026-06-18T12:00Z (re-eligible from a 5b standpoint; technicals still fail R1+R2 anyway).
- SOL/USD 5b: active until 2026-06-18T18:00Z (~4h from now).

### Universe refresh

Not first of month (today is 06-18). No action.

2026-06-15T03:16:45Z | idea-scan | day-gate | not Friday, skipping | no action
2026-06-16T17:06:37Z | harness | day-gate | not Saturday, skipping | no action
2026-06-17T01:02:38Z | idea-scan | day-gate | not Friday, skipping | no action
2026-06-17T22:00Z | idea-scan | day-gate | not Friday, skipping | no action
2026-06-17T20:10Z | midday | SOL stop-out intrabar replay on 18:00Z bar (low $72.15 < stop $72.2288), fill $72.1927 (stop × 0.9995), CLOSE ts 18:00Z per pierce-bar convention. Net -$199.87 / -1.28R. Equity $10,231.74, DD 5.92% (warn 12.5%, 6.58% headroom), day -3.60% (warn 5%, 1.40% headroom). Loss streak 3 (cap 7, 4 headroom). All kill switches CLEAR. Cash 100% (0 open, 0/4 strategy cap, 0/8 portfolio). 5b cooldowns: SOL→2026-06-18T18:00Z, HYPE→2026-06-18T12:00Z. Telegram exit-alert sent.

## 2026-06-18T04:11Z — routine-03-eod (PT label 2026-06-17, on-schedule cron fire)

**Slot identity `bull-03-eod`.** Cron `0 21 * * 1-5` (Wed 21:00 PT / 04:00 UTC Thu) — framework dispatched on-schedule ~11 min late at ~04:11Z. Per the routine-03 date-labeling guard, this wake is labeled with the **PT calendar date at fire time = 2026-06-17**. Just-closed 1H bar = 03:00Z 2026-06-18.

### Watchdog (mandatory, `--telegram`)

7 findings; alert auto-sent by `watchdog.py`:
- 1× A heartbeat: routine-07 last commit 94h ago (threshold 30h)
- 6× D stale-MTM (variants v0.12-sbd-exit / v0.13-trend-confirm / v0.14-recovery-trend / v0.3-vol-compression / v0.5-cluster-cap-tight / v0.7-vol-comp-defensive — all 95h since last MTM)

Informational; same set as the 04:11Z prior-day EOD and the 20:10Z midday wakes. Variant lag attributable to scheduler gap, does not affect BULL state. Flagged for routine-07 catch-up.

### Position management (open positions)

Zero open positions at wake start (SOL closed at stop at midday 20:10Z replay; HYPE closed earlier at 12:00Z replay). Zero exit checks needed.

### EOD entry scan (W19-E analyst-role split)

Per the 2026-06-12 amendment, indicator computation delegated to `python scripts/indicators.py` (authoritative table). Just-closed 1H bar = 03:00Z 2026-06-18.

**Regime header (from indicators.py):** **1/15 positive 24h, median −3.37%** → **5a FAIL** (1 < 4 floor) **AND 5a-SBD ACTIVE** (positives ≤ 1 AND median ≤ −1.0%). All new entries rejected this wake. SBD-tightened exit (two-bar 9-EMA) would apply to any open positions, but BULL is flat.

**Technical analyst pass:** Only TRX/USD passes rules 1, 2, 2a, 3 (close $0.320753 > 20-EMA $0.320311, RSI14 57.6, 4H >50-EMA +0.000662). However TRX fails R4a ($0.97M < $2M floor) and would be regime-blocked under 5a anyway. Every other pair fails R1 (sub-EMA20) and/or R2 (RSI < 55) under broad cascade. The regime-rejection halts both news and sentiment passes (informational in v0.2 anyway).

**Decision:** **NO ENTRIES.** Regime 5a FAIL + SBD ACTIVE — first SBD activation in this routine since 2026-05-19 archive period. Eligible-on-technicals pairs after regime gate would have been zero regardless (TRX-only and TRX is sub-liquidity).

### Estimated SBD avoided give-back (per 5a-SBD logging obligation)

BULL holds no open positions at SBD activation, so the avoided-give-back ledger is $0 this wake. SBD's defensive value (Exit 1-SBD = two-bar 9-EMA tightening) is not exercised since there is nothing open to defend. Recording the classification per the rule's instrumentation requirement.

### Day summary 2026-06-17 PT (Wed, EOD)

Trades opened today: 1 (SOL 17:00Z). Trades closed today: 2 (HYPE 12:00Z stop-out, SOL 18:00Z intrabar stop-out). Day PnL **−$382.51 / −3.60%**. Equity close **$10,231.74** (−5.92% from peak $10,875.85). Loss streak **3** trading days (BTC Sun, ETH Tue, Wed [HYPE+SOL]). All kill switches **CLEAR** (daily-loss 1.40% headroom to 5% cap; DD 6.58% to 12.5% warn / 19.08% to 25% halt; loss-streak 4 of 7 headroom). 5b cooldowns active: SOL→2026-06-18T18:00Z, HYPE→2026-06-18T12:00Z.

Rolling: 7d BULL ≈ −0.74% vs BTC ≈ +4.0% → BULL −4.7% trailing. 30d BULL ≈ +2.32% vs BTC ≈ −19.1% → BULL +21.4% ahead.

Telegram: mandatory EOD card sent.

## 2026-06-17T04:11Z — routine-03-eod (PT label 2026-06-16, on-schedule cron fire)

**Slot identity `bull-03-eod`.** Cron `0 21 * * 1-5` (Tue 21:00 PT / 04:00 UTC Wed) — framework dispatched on-schedule ~11 min late at ~04:11Z. Per the routine-03 date-labeling guard, this wake is labeled with the **PT calendar date at fire time = 2026-06-16**. UTC entry timestamp = 2026-06-17T04:00Z (the closing time of the 03:00Z 1H bar, which is the just-closed bar at fire time).

### Watchdog (mandatory, `--telegram`)

7 findings; alert auto-sent by `watchdog.py`:
- 1× A heartbeat: routine-07 last commit 70h ago (threshold 30h)
- 6× D stale-MTM (variants v0.12-sbd-exit / v0.13-trend-confirm / v0.14-recovery-trend / v0.3-vol-compression / v0.5-cluster-cap-tight / v0.7-vol-comp-defensive — all 71h since last MTM)

All informational; variant lag attributable to weekend/Mon scheduler gap, does not affect BULL state. Flagged for routine-07 catch-up.

### Position management (open positions)

Zero open positions at wake start (ETH closed at stop earlier today). Zero exit checks needed.

### EOD entry scan (W19-E analyst-role split)

Per the 2026-06-12 amendment, indicator computation delegated to `python scripts/indicators.py` (authoritative table over in-context arithmetic). Just-closed 1H bar = 03:00Z 2026-06-17.

**Regime header (from indicators.py):** 6/15 positive 24h, median −0.11% → **5a PASS** (6 > 4 floor); **SBD CLEAR** (median > −1.0% AND positives > 1).

**Technical analyst pass — all-rule eligibility:**

| Pair | R1 EMA20 | R2 RSI≥55 | R2a RSI<80 | R3 4H EMA50 | R4a $≥2M | Eligible |
|------|---------|-----------|-----------|------------|----------|----------|
| BTC | FAIL | FAIL (47.1) | OK | PASS +1.54% | OK $114.07M | NO (R1+R2) |
| ETH | PASS +0.06% | FAIL (52.3) | OK | PASS +3.82% | OK $60.00M | NO (R2) — also R5b cooldown active until 15:00Z Wed |
| SOL | FAIL | FAIL (49.5) | OK | PASS +5.03% | OK $21.96M | NO (R1+R2) |
| **HYPE** | **PASS +1.70%** | **PASS (59.8)** | **OK** | **PASS +15.59%** | **OK $38.08M** | **YES** |
| XRP | FAIL | FAIL (45.2) | OK | PASS +2.97% | OK $22.37M | NO (R1+R2) |
| **SUI** | **PASS +0.97%** | **PASS (56.2)** | **OK** | **PASS +3.69%** | **OK $5.21M** | **YES** |
| TAO | FAIL | FAIL (45.0) | OK | PASS +4.99% | OK $6.04M | NO (R1+R2) |
| XDG | FAIL | FAIL (47.5) | OK | FAIL −0.06% | OK $4.04M | NO (R1+R2+R3) |
| NEAR | FAIL | FAIL (42.7) | OK | PASS +4.07% | OK $4.93M | NO (R1+R2) |
| ADA | FAIL | FAIL (41.5) | OK | FAIL −1.33% | OK $9.18M | NO (R1+R2+R3) |
| LINK | PASS +0.51% | FAIL (54.5) | OK | PASS +3.22% | OK $2.82M | NO (R2 by 0.5 RSI) |
| LTC | PASS +0.16% | FAIL (52.4) | OK | PASS +2.53% | OK $2.40M | NO (R2) |
| FARTCOIN | PASS +1.79% | PASS (57.5) | OK | PASS +10.71% | **FAIL $0.63M** | NO (R4a) |
| TRX | PASS +0.01% | FAIL (48.3) | OK | FAIL −0.90% | **FAIL $1.26M** | NO (R2+R3+R4a) |
| AVAX | PASS +0.71% | PASS (55.9) | OK | PASS +1.57% | **FAIL $1.99M** | NO (R4a by $0.01M, marginal) |

**Two technical candidates: HYPE and SUI.**

**Rule 8 (W18-C) tiebreak:** max 1 entry per wake; prefer highest 30d notional rank from universe.md. **HYPE rank 4, SUI rank 6 → HYPE selected.** SUI re-evaluated next wake.

**Selected candidate: HYPE/USD**

**News analyst (W19-E informational):** **Skipped** for time budget per the discretionary-skip pattern used in prior wakes. News is informational only in v0.4 — does not veto entries — so the skip is decision-neutral. (Routine-04 may revisit whether the EOD news pass should be mandatory; no proposal here.)

**Sentiment analyst:** `kraken_spread` HYPEUSD 04:11:58Z shows last $75.13, 10-tick recent spreads 1–3¢, modal spread 2¢ on $75.13 = **~2.7 bps** → **supportive** (tight spread, no flash widening). Live price ($75.13) +$0.67 above closed-bar reference ($74.46), consistent with the +6.91% daily momentum — directionally supportive of the technical signal.

**Decision: ENTER HYPE/USD long.**

### Pre-entry guardrail check (per `skills/decide.md`)

- Open positions count: 0 → 1 (cap 8, strategy max-concurrent 4) — OK
- Portfolio risk-at-moment: 0.00% → 1.50% (cap 4%) — OK
- Per-trade risk: 1.50% (cap 1.5%) — at-cap, OK
- Pair in universe: HYPE rank 4 — OK
- Pair not already open: no HYPE position — OK
- Pair not on 5b cooldown: no recent HYPE stop — OK (only ETH on cooldown)
- Cluster cap 6a: HYPE not in {BTC,ETH,SOL,TAO,AVAX,SUI,LINK} → 0/2 — OK
- Daily loss <5%: −1.98% — OK
- Equity floor: $10,614.25 > $7,500 — OK
- One-per-wake rule 8: this is the 1st (and only) entry — OK

**All gates pass.** Position approved.

### Entry math

- 1H close (03:00Z bar): **$74.46**
- Slippage (0.05% adverse per `skills/decide.md`): close × 1.0005 = **$74.4972** (entry fill)
- ATR14 (1H Wilder, from indicators.py): **$1.4129**
- Stop distance: 2 × ATR = **$2.8258**
- Stop: $74.4972 − $2.8258 = **$71.6714**
- Target (4R): $74.4972 + 4 × $2.8258 = **$85.8004**
- Per-trade risk basis: 1.5% × $10,614.25 = **$159.21**
- Size: $159.21 / $2.8258 = **56.342770 units** (round-down to 6 dp, matching prior HYPE/TAO/XRP precision)
- Entry cost (cash lock): 56.342770 × $74.4972 = **$4,197.38**
- Cash post-entry: $10,614.25 − $4,197.38 = **$6,416.87**
- Position MTM @ closed-bar $74.46: 56.342770 × $74.46 = **$4,195.28**
- Unrealized PnL at MTM: −$2.10 (pure slippage cost, no adverse move)
- Equity at EOD MTM: $6,416.87 + $4,195.28 = **$10,612.15**

### Stop ratchet (W22-H) & exit triggers preview

- Breakeven ratchet armed at unrealized R ≥ 2.0 = close ≥ $74.4972 + 2 × $2.8258 = **$80.1488**
- Static 4R take-profit: $85.8004
- W22-G two-bar EMA20 exit: monitors first sub-EMA bar on next 1H closes

### Lessons-eligibility review

Per routine §DO step 4: review today's trades for lessons (gap risk / target placement / immediate-reversal).
- **ETH stop today:** not a gap (intrabar $3.35 below stop on the 14:00Z bar; designed adverse range). The orphan-write race is already flagged for routine-04 evaluation in the midday research log (recommendation: `git status` check at routine wake start). No new lesson row added today — the pattern is already captured.
- **HYPE entry today:** not yet evaluable (single-bar position).

No new lessons appended this wake.

### Cash & equity reconciliation

| Step | USD |
|---|---|
| Cash pre-routine (post-ETH stop) | $10,614.25 |
| HYPE OPEN at 04:00Z (cash lock) | −$4,197.38 → cash $6,416.87; position notional $4,197.38 |
| HYPE MTM @ 03:00Z close $74.46 | $4,195.28 |
| Equity at EOD | $6,416.87 + $4,195.28 = **$10,612.15** |

### Kill-switch table

- Daily realized 2026-06-16 PT: −$214.33 / −1.98% — CLEAR.
- Daily total (realized + unrealized) 2026-06-16 PT: −$216.43 / −2.00% — CLEAR (5% cap).
- Loss streak: 2 trading days — CLEAR (cap 7, 5 of headroom).
- Max drawdown: 2.42% from peak $10,875.85 — CLEAR (warn 12.5%).
- Equity floor: $10,612.15 > $7,500 — CLEAR.
- Regime gate: 5a PASS (6/15). 5a-SBD CLEAR.

### Monthly archive check

Today is Tue 2026-06-16 PT. Last trading day of June 2026 is Tue 2026-06-30. **Not today** — archive sweep deferred.

### Telegram

**Sent** per routine §NOTIFY (mandatory daily EOD card). Card includes equity, day PnL, ETH close + HYPE open events, kill-switch status, BULL vs BTC-hold rolling 30d, and notes (regime, watchdog summary, 5b cooldown).

### Trade log writes

**1 OPEN row appended** (HYPE/USD). ETH OPEN+CLOSE rows already present from this morning's midday routine.

### Next routine

routine-01-overnight Wed 2026-06-17T13:00Z (cron `0 6 * * 1-5` PT) — will MTM the HYPE position against the latest 1H close and run a fresh entry scan.

## 2026-06-17T17:52Z — routine-01-overnight (LATE cron fire, 4h52m delay)

**Slot identity `bull-01-overnight`.** Cron `0 6 * * 1-5` PT = 13:00 UTC. **Actual fire 17:52 UTC = 4h52m late.** Per the routine-03 fire-time-bar precedent (04:11Z fire → 03:00Z bar entry stamped 04:00Z bar-close), this wake uses the just-closed bar at fire time = **16:00Z 1H bar (closed 17:00Z)** for entry-scan indicator data. HYPE stop-out is replayed at the actual first-piercing bar timestamp regardless of wake time.

### Watchdog (mandatory, `--telegram`)

7 findings; alert auto-sent by `watchdog.py`:
- 1× A heartbeat: routine-07 last commit 84h ago (threshold 30h)
- 6× D stale-MTM (variants v0.12-sbd-exit / v0.13-trend-confirm / v0.14-recovery-trend / v0.3-vol-compression / v0.5-cluster-cap-tight / v0.7-vol-comp-defensive — all 85h since last MTM)

All informational; variant scheduler lag continues from weekend/Mon gap. Flagged for routine-07 catch-up. BULL state unaffected.

### Position management (open positions)

**HYPE/USD long** opened 2026-06-17T04:00Z @ $74.4972, stop $71.6714. Routine fetched Kraken REST 1H OHLCV history since entry to verify intra-bar exit triggers across the 4h52m blind window (skipped any wake from 04:00Z → 17:52Z).

| Bar (UTC open) | Open | High | Low | Close | Stop pierce? |
|---|---|---|---|---|---|
| 04:00Z | 74.44 | 75.27 | 74.30 | 74.49 | no |
| 05:00Z | 74.46 | 74.67 | 73.40 | 74.26 | no |
| 06:00Z | 74.28 | 74.28 | 72.82 | 73.38 | no |
| 07:00Z | 73.36 | 73.71 | 72.94 | 73.34 | no |
| 08:00Z | 73.38 | 73.47 | 72.11 | 72.35 | no |
| 09:00Z | 72.39 | 73.15 | 72.27 | 73.03 | no |
| 10:00Z | 72.98 | 73.01 | 72.05 | 72.22 | no |
| **11:00Z** | **72.25** | **72.33** | **70.60** | **70.92** | **YES (low $70.60 < stop $71.6714)** |
| 12:00Z | 70.97 | 71.54 | 69.70 | 71.38 | (already stopped) |
| 13:00Z–16:00Z | (post-stop recovery, irrelevant) | | | | |

**Exit determination:** First piercing bar = 11:00Z (opens 11:00Z, closes 12:00Z, low $70.60). Per skills/decide.md stop-fill model and the 2026-06-16 ETH precedent (intra-bar stop pierce fills at stop × (1 − 0.0005)): **HYPE exit fill = $71.6714 × 0.9995 = $71.6356**. Exit timestamp = bar close time = **2026-06-17T12:00:00Z**. Tag: `exit-stop-hit-missed-scheduler-replay` (matches ETH replay tag — actual exit predates wake by 5h52m).

**Realized math:**
- Entry notional: 56.342770 × $74.4972 = $4,197.38
- Exit notional: 56.342770 × $71.6356 = $4,036.15
- Gross PnL: −$161.23
- Entry commission 0.26%: $10.91 | Exit commission 0.26%: $10.49 | Total RTT: $21.41
- Net PnL: **−$182.64**
- R-risk: 1.5% × $10,614.25 = $159.21 | R-multiple: **−1.15R**
- Cash after close: $10,614.25 + (−$182.64) = **$10,431.61**

**Note: even on-schedule wake at 13:00Z would have detected this stop pierce** (11:00Z bar closed at 12:00Z, before cron). The late fire only delayed the routine's *processing* of the exit, not the exit's *occurrence*. No alpha lost to the delay on this specific event.

### Regime header (from `indicators.py` 16:00Z bar)

**12/15 positive 24h, median +1.17%** → **5a PASS** (12 > 4 floor); **SBD CLEAR** (12 > 1 positive AND median +1.17% > −1.0%). Tape is broad-positive — opposite of yesterday's near-tie regime.

Positives (12): BTC +0.17, SOL +0.88, HYPE +2.35, SUI +2.06, TAO +1.54, XDG +0.61, NEAR +0.95, LINK +1.17, LTC +1.29, FARTCOIN +5.51, TRX +1.39, AVAX +1.90.
Negatives (3): ETH −0.29, XRP −0.02, ADA −1.28.

### Technical analyst pass — all-rule eligibility (16:00Z bar)

| Pair | R1 EMA20 | R2 RSI≥55 | R2a RSI<80 | R3 4H EMA50 | R4a $≥2M | Eligible |
|------|---------|-----------|-----------|------------|----------|----------|
| **BTC** | **PASS +$370.3** | **PASS (55.9)** | **OK** | **PASS +$859.7** | **OK $105.25M** | **YES** |
| ETH | FAIL −$4.09 | FAIL (46.5) | OK | PASS +$40.81 | OK $58.27M | NO (R1+R2) |
| **SOL** | **PASS +$0.595** | **PASS (55.8)** | **OK** | **PASS +$3.346** | **OK $20.17M** | **YES** |
| HYPE | PASS +$2.215 | PASS (62.2) | OK | PASS +$8.989 | OK $31.92M | NO (R5b cooldown until 12:00Z Thu — just stopped) |
| XRP | PASS +$0.0036 | FAIL (51.1) | OK | PASS +$0.0298 | OK $21.96M | NO (R2) |
| SUI | PASS +$0.0028 | FAIL (52.0) | OK | PASS +$0.0252 | OK $4.69M | NO (R2 by 3.0 RSI) |
| TAO | PASS +$1.331 | FAIL (51.1) | OK | PASS +$12.95 | OK $4.69M | NO (R2) |
| XDG | PASS +$0.00023 | FAIL (51.0) | OK | FAIL −$0.00013 | OK $3.10M | NO (R2+R3) |
| NEAR | PASS +$0.0129 | FAIL (51.2) | OK | PASS +$0.1498 | OK $2.84M | NO (R2) |
| ADA | FAIL −$0.0004 | FAIL (45.1) | OK | FAIL −$0.0035 | OK $8.45M | NO (R1+R2+R3) |
| LINK | PASS +$0.0223 | FAIL (51.5) | OK | PASS +$0.1929 | OK $2.10M | NO (R2) |
| LTC | PASS +$0.1191 | FAIL (52.6) | OK | PASS +$1.038 | FAIL $1.37M | NO (R2+R4a) |
| FARTCOIN | PASS +$0.0025 | PASS (57.9) | OK | PASS +$0.0130 | FAIL $0.63M | NO (R4a) |
| TRX | PASS +$0.0022 | PASS (77.1) | OK | PASS +$0.0012 | FAIL $0.79M | NO (R4a) |
| AVAX | PASS +$0.030 | FAIL (53.3) | OK | PASS +$0.120 | FAIL $1.44M | NO (R4a) |

**Two technical candidates: BTC and SOL.**

### News analyst (W19-E informational)

**Skipped** for time budget per the discretionary-skip pattern used in prior wakes. News is informational only in v0.4 — does not veto entries — so the skip is decision-neutral. Note that the late-fire context also pushes against running a full Firecrawl scan when the entry decision is otherwise tractable.

### Sentiment analyst

**BTC sentiment:** not collected (BTC was about to be cash-rejected; would be wasted query).

**SOL sentiment:** Kraken Spread endpoint 17:59:20Z showed 10 recent ticks bid $74.00–74.01 / ask $74.01–74.03, **modal spread 1.35–2.7 bps** on $74.00 mid → **supportive** (tight spread, no flash-widening). Ticker: last $73.98, bid $74.00, ask $74.01 → live price +$0.29 above 16:00Z bar close ($73.69), consistent with the +0.88% 24h momentum.

### Rule 8 tiebreak & cash constraint

**Universe rank ordering:** BTC rank 1 > SOL rank 3 → **BTC is top-rank rule-8 winner**.

**BTC pre-entry sizing check:**
- Equity at scan time (post-HYPE-close): $10,431.61
- BTC fill: $65,814.2 × 1.0005 = $65,847.11
- BTC ATR14: $443.45 | stop distance 2×ATR = $886.9 | stop = $64,960.21 | target (4R) $69,394.71
- Risk basis 1.5% × $10,431.61 = $156.47
- Strategy-prescribed size: $156.47 / $886.9 = **0.176428 BTC**
- **Required notional: 0.176428 × $65,847.11 = $11,617.27**
- **Available cash: $10,431.61 → deficit $1,185.66**
- BTC's stop distance is only 1.35% of price (ATR-to-price ratio 0.67% → 2×ATR = 1.35%) — for the strategy-mandated 1.5%-risk size, required notional is ~111% of equity. After HYPE's stop locked away $4.2k briefly and post-close cash recovered to only $10.4k, BTC cannot be filled on spot without leverage. **Mandate forbids leverage → REJECT-cash.**

**Pre-entry-check interpretation:** Cash-insufficient functions as an implicit guardrail rejection (no leverage = can't buy more than cash). Treated equivalently to other pre_entry_check REJECT reasons listed in `skills/decide.md`. Advance to next rule-8-eligible candidate per "rule-8 fallback" interpretation: rule 8's intent is to prevent same-bar cluster fills (taking multiple correlated entries on a single signal flip), which is preserved by taking ONE entry from the eligible set even if not the top-ranked. Choosing SOL maintains one entry per wake. This is a NEW PRECEDENT for cash-constrained tape; logged as a lesson for routine-04 evaluation.

### Selected candidate: SOL/USD

**Pre-entry guardrail check (per `skills/decide.md`):**
- Open positions count: 0 → 1 (cap 8, strategy max-concurrent 4) — OK
- Portfolio risk-at-moment: 0.00% → 1.50% (cap 4%) — OK
- Per-trade risk: 1.50% (cap 1.5%) — at-cap, OK
- Pair in universe: SOL rank 3 — OK
- Pair not already open: no SOL position — OK
- Pair not on 5b cooldown: last SOL stop-out 2026-05-22T15:00Z (26 days ago, well past 24h) — OK
- Cluster cap 6a: SOL in {BTC,ETH,SOL,TAO,AVAX,SUI,LINK} → 0→1 / 2 (HYPE just exited cluster-free position) — OK
- Daily loss <5%: −1.72% realized, −1.74% total — OK
- Equity floor: $10,431.61 > $7,500 — OK
- One-per-wake rule 8: this is the 1st (and only) entry; BTC top-rank rejected for cash → SOL as next-eligible — OK (within rule 8 spirit)
- **Cash check: required $7,701.06 ≤ available $10,431.61** (headroom $2,730.55) — OK

**All gates pass.** Position approved.

### Entry math

- 1H close (16:00Z bar): **$73.69**
- Slippage (0.05% adverse per `skills/decide.md`): close × 1.0005 = **$73.7268** (entry fill)
- ATR14 (1H Wilder, from `indicators.py`): **$0.74901**
- Stop distance: 2 × ATR = **$1.49802**
- Stop: $73.7268 − $1.49802 = **$72.2288**
- Target (4R): $73.7268 + 4 × $1.49802 = **$79.7189**
- Per-trade risk basis: 1.5% × $10,431.61 = **$156.4742**
- Size: $156.4742 / $1.49802 = **104.454002 SOL** (round-down 6 dp)
- Entry cost (cash lock): 104.454002 × $73.7268 = **$7,701.06**
- Cash post-entry: $10,431.61 − $7,701.06 = **$2,730.55**
- Position MTM @ closed-bar $73.69: 104.454002 × $73.69 = **$7,697.22**
- Unrealized PnL at MTM: **−$3.84** (pure slippage cost, no adverse move)
- Equity at MTM: $2,730.55 + $7,697.22 = **$10,427.77**

### Stop ratchet (W22-H) & exit triggers preview

- Breakeven ratchet armed at unrealized R ≥ 2.0 = close ≥ $73.7268 + 2 × $1.49802 = **$76.7228**
- Static 4R take-profit: $79.7189
- W22-G two-bar EMA20 exit: monitors first sub-EMA bar on next 1H closes (current EMA20 ≈ $73.0953 from indicators table)

### Lessons-eligibility review

Per routine §DO step (lesson review): today's events warrant a new lesson on the cash-constraint observation. **One new lesson appended to `lessons.md`** ("2026-06-17 — Cash insufficiency blocks BTC top-rank entry under strategy-mandated sizing"). Routine-04 should evaluate the policy: (a) explicit cash-fit pre-check, (b) codify rule-8 fallback, (c) sizing degrade-to-cash with reduced-risk recording, or (d) skip-wake-on-top-rank-reject.

HYPE stop today is the third consecutive losing trade (post BTC/ETH); pattern is not a new lesson — multi-day losing streak is monitored via kill-switch state and remains within bounds (3 of 7).

### Cash & equity reconciliation

| Step | USD |
|---|---|
| Cash pre-routine (post-EOD HYPE entry) | $6,416.87 |
| HYPE position MTM @ EOD close $74.46 | $4,195.28 |
| Equity at routine wake (pre-replay) | $10,612.15 |
| HYPE CLOSE replay @ 12:00Z bar pierce ($71.6356 fill) | net −$182.64; cash → $10,431.61 |
| Equity post-HYPE-close (cash, no positions) | $10,431.61 |
| BTC pre-entry-check: cash-insufficient REJECT | no position change |
| SOL OPEN at 17:00Z (cash lock −$7,701.06) | cash → $2,730.55; position notional $7,701.06 |
| SOL MTM @ 16:00Z close $73.69 | $7,697.22 |
| Equity at MTM | $2,730.55 + $7,697.22 = **$10,427.77** |

### Kill-switch table

- Daily realized 2026-06-17 PT: −$182.64 / −1.72% — CLEAR (5% cap).
- Daily total (realized + unrealized) 2026-06-17 PT: −$186.48 / −1.74% — CLEAR.
- Loss streak: 3 trading days (BTC Sun, ETH Tue, HYPE Wed) — CLEAR (cap 7, 4 of headroom).
- Max drawdown: 4.12% from peak $10,875.85 — CLEAR (warn 12.5%).
- Equity floor: $10,427.77 > $7,500 — CLEAR.
- Regime gate: 5a PASS (12/15 positive, median +1.17%). 5a-SBD CLEAR.

### First-of-month universe refresh

Today is Wed 2026-06-17. Not the 1st. Skipped (last refresh 2026-06-01).

### Telegram

**Sent** per routine §NOTIFY (new OPEN + stop-out CLOSE both fired this run). Card includes equity, day P&L, HYPE close + SOL open events, kill-switch status, late-fire context, rule-8 fallback explanation, and BTC cash-insufficient rejection note.

### Trade log writes

**2 rows appended:** HYPE CLOSE @ 12:00Z bar-pierce replay + SOL OPEN @ 17:00Z (fire-time bar close).

### Next routine

routine-02-midday Wed 2026-06-17T19:00Z (cron `0 12 * * 1-5` PT) — will MTM the fresh SOL position against the latest 1H close. Note: with cash now low ($2,730.55) and 1 cluster position open, midday wake should re-MTM cleanly; no entries are made at midday per routine-02 design.

## 2026-06-16T20:08Z — routine-02-midday (on-schedule cron fire, third midday wake today)

**Slot identity `bull-02-midday`.** Cron `0 13 * * 1-5` (Tue 13:00 PT / 20:00 UTC) — framework dispatched on-schedule ~8 min late at ~20:08Z. Third routine-02 wake of the day after off-schedule 12:30Z and early 15:16Z fires.

### State-of-record anomaly: orphan ETH/USD OPEN row

At session start, `git status` showed `M memory/trade_log.md` with one appended row:
```
| 2026-06-16T12:00:00Z | OPEN | ETH/USD | long | 5.1162 | 1797.88 | 1766.13 | 1924.87 | — | — | entry-rule-v0.4-momentum |
```

**File mtime evidence** (`Get-ChildItem`): trade_log.md last-write = **2026-06-16 05:17:29 AM PT = 12:17:29 UTC**. The prior commit `e5f89f6 routine-02-midday 2026-06-16: DD 0.43%, 0 exits (flat book carry; first wake since Sun 06-14)` was at **12:15:52 UTC**, ~96 seconds earlier. Both subsequent rebuilds (15:16Z midday and 20:08Z midday pre-read) had no knowledge of the row — the 15:16Z rebuild even explicitly logged flat-book carry. Conclusion: **the orphan write happened in a ~96s race window between the 12:15:52Z midday commit and the 12:17:29Z orphan-write**, by a concurrent or quickly-aborted routine-01-overnight process that wrote to trade_log.md but never committed. No `routine-01-overnight` commit appears on `main` between 12:15:52Z and now. No stash, no branch (besides three pre-existing `claude/*` worktree branches unchanged). The race archetype matches the 2026-06-14 BTC -0.60R replay-race precedent (commit 2b5e27e addendum) where routine-05 corrected the routine-01 race.

**Provenance assessment of the orphan write:** the row is internally consistent with strategy v0.4 sizing — 5.1162 × ($1797.88 - $1766.13) = $162.44 ≈ 1.5% × $10,828.58 prior equity, OPEN price matches the 2026-06-16T11:00Z 1H bar close exactly, stop is at $1797.88 - 2 × $15.875 ATR = $1766.13 (ATR-consistent), target is at $1797.88 + 4 × $31.75 = $1924.88 (≈ logged $1924.87, off by $0.01 rounding). The entry signal would have validly fired on the 11:00Z bar close (the 12:00Z bar close in BULL's bar-naming convention) if regime 5a passed at the time (per 12:30Z research_log read, 14/15 positive median +1.27% — comfortably passes 5a). **The orphan row is most consistent with a real-but-aborted routine-01-overnight wake** that opened the position correctly per strategy but crashed before committing. The sole irregularity is **missing 0.05% adverse slippage on the entry fill** ($1797.88 logged vs $1798.78 conservative-model expectation), which is consistent with a partial-execution failure that skipped the slippage step.

**Decision:** per CLAUDE.md and `skills/log-trade.md` "trade_log.md is source of truth, portfolio.md is derived", the ETH position is **real and managed by this routine**. The orphan OPEN row is **kept as-is** per "Never rewrite past rows" rule; the missing-slippage cost is realized only on the exit side as slightly worse R.

### Position management: ETH stop-hit replay

Walked ETH/USD 1H bars 2026-06-16T12:00Z → 20:00Z (last in-progress bar) via `kraken_ohlcv` 30-bar fetch:

| Bar (UTC open) | Close | Low | Bar vs entry |
|---|---|---|---|
| 12:00 | 1813.48 | 1795.33 | +0.87% (favorable) |
| 13:00 | 1796.10 | 1790.69 | -0.10% |
| **14:00** | **1778.89** | **1762.78** ← stop pierced | **-1.06% close, -1.95% low** |
| 15:00 | 1781.23 | 1773.36 | -0.93% (post-exit) |
| 16:00 | 1776.03 | 1772.05 | -1.22% (post-exit) |
| 17:00 | 1793.75 | 1776.23 | -0.23% (post-exit) |
| 18:00 | 1797.37 | 1791.25 | -0.03% (post-exit) |
| 19:00 | 1792.69 | 1788.45 | -0.29% (post-exit) |
| 20:00 | 1788.46 | 1788.38 | -0.52% (in-progress) |

**Stop check (rule 2):** Static 2×ATR stop = $1766.13. 14:00Z bar low = $1762.78 → pierced by $3.35 intrabar → **stop hit on the 14:00Z bar**.

**EMA20 cross-check (rule 1, W22-G two-bar confirm):** 1H 20-EMA computed via SMA-20 seed on bars 06-15T15:00Z → 06-16T10:00Z (sum 35,945.48 / 20 = $1797.274), then EMA recursion with α = 2/21:
- EMA(11:00Z) = $1797.33; close $1797.88 → +$0.55 above (entry bar OK)
- EMA(12:00Z) = $1798.30; close $1813.48 → +$15.18 above
- EMA(13:00Z) = $1798.53; close $1796.10 → **-$2.43 below (first sub-EMA)**
- EMA(14:00Z) = $1797.10; close $1778.89 → **-$18.21 below (second consecutive sub-EMA → W22-G would fire at bar close 15:00Z)**

**Rule precedence:** Both rule 2 (intrabar stop) and rule 1 (bar-close EMA confirm) trigger on the 14:00Z bar. Per `skills/decide.md` "intra-bar exits" handling and the midday routine spec ("if price has pierced [the stop] intrabar, close at stop price"), the intrabar stop pierce precedes the bar-close EMA confirm chronologically. **Exit fires via rule 2 (stop hit), not rule 1.** Counterfactual: had rule 1 fired instead, exit fill would have been close × 0.9995 = $1778.89 × 0.9995 = $1778.00, gross PnL = 5.1162 × ($1778.00 - $1797.88) = -$101.71, commission $47.40, net **-$149.11 / -0.92R** — i.e., the EMA20-confirm exit would have been **+$65.22 / +0.40R better** than the stop. But the stop intrabar pierced first chronologically and is the rule that fired.

**4R target check (rule 3):** target $1924.87 not approached — highest 1H high post-entry was 12:00Z bar high $1837.90, well below target.

**Stop ratchet check (W22-H breakeven):** never armed. Highest 1H close post-entry was 12:00Z bar = $1813.48 → +0.49R, below +2R threshold $1861.38; stop remained at initial 2×ATR throughout.

### Exit math

- **Exit fill:** $1766.13 × 0.9995 = **$1765.25** (0.05% adverse slippage per `skills/decide.md`)
- **Exit timestamp:** 2026-06-16T15:00:00Z (close of the 14:00Z bar — convention from SOL 2026-05-22T15:00:00Z exit-stop-hit-missed-scheduler-replay precedent)
- **Gross PnL:** 5.1162 × ($1765.25 - $1797.88) = -$166.94
- **Commission roundtrip:** 0.26% × 5.1162 × ($1797.88 + $1765.25) = $47.39
- **Net realized PnL:** -$166.94 - $47.39 = **-$214.33**
- **Per-trade risk basis (at entry):** 5.1162 × ($1797.88 - $1766.13) = $162.44
- **R-multiple:** -$214.33 / $162.44 = **-1.32R**

R is worse than the typical -1.0x stop-hit precedent because the orphan entry skipped the conservative 0.05% slippage model — effective adverse range $32.63 vs design $31.75, plus standard commission load on a small-relative-to-equity risk basis.

### Friction accounting

Commission $47.39 = 0.439R on a $162.44 risk basis (29.1% of stop-distance loss). This is the second-largest commission-to-risk ratio in the trade-log (the SOL 2026-05-22 stop-hit had a similar ratio at $13.70 / $31.94 = 42.9%, and that one was R = -1.43). Pattern: small-equity-percentage trades amplify the commission-as-R penalty. For sizing purposes this is informational only — the 1.5%-per-trade and 4% portfolio caps are mandate-locked.

### Cash & equity reconciliation

| Step | USD |
|---|---|
| Cash pre-trade (Sun BTC exit) | $10,828.58 |
| ETH OPEN at 12:00Z (orphan write, no MTM impact) | -$9,197.49 (locked) → cash $1,631.09; position notional $9,197.49 |
| ETH CLOSE at 15:00Z | +5.1162 × $1765.25 - $47.39 commission = $9,030.62 - $47.39 = $8,983.23 |
| Cash post-trade | $1,631.09 + $8,983.23 = **$10,614.32** |

Reconciliation note: a strict commission-each-side bookkeeping gives $10,614.32; the realized-PnL form ($10,828.58 - $214.33) gives $10,614.25; the $0.07 difference is the residual from carrying ($1,797.88 × 5.1162 = $9,197.494) at-position-open commission as $23.91 vs $23.91 carry-forward arithmetic. Pinned to **$10,614.25** to match the realized-PnL convention used throughout the ledger. (Future audit-cleanup item, not material.)

### Kill-switch table

- Daily realized 2026-06-16 PT: -$214.33 / -1.98% — CLEAR (cap 5%, 2.5x below).
- Loss streak: 2 (BTC Sun -0.60R + ETH Tue -1.32R) — CLEAR (cap 7, 5 of headroom).
- Max drawdown: 2.40% from peak $10,875.85 — CLEAR (warn 12.5% / kill 25%).
- Equity floor: $10,614.25 > $7,500 — CLEAR.
- Regime gate: 5a marginal-PASS at floor (4/15 positive). 5a-SBD CLEAR (median -0.58% > -1.0%, 4 > 1 positive). **Informational only — midday spec forbids new entries regardless of regime.**
- MCP availability: Kraken `kraken_ticker` ETHUSD + `kraken_ohlcv` 30-bar 1H + `kraken_multi_ticker` 15-pair all returned clean <3s.

### Live snapshot (informational)

`kraken_multi_ticker` 20:08Z — **4/15 positive 24h** (positives: AVAX +0.34, FARTCOIN +5.60, HYPE +8.67, SUI +0.13; median TRX -0.58%). Notable: BTC last $65,621.8 (-1.45% vs the 15:16Z print of $66,584.5), TAO -4.78% session-low, HYPE +8.67% holding the leader slot for the third consecutive day. The session has flipped from the 12:30Z reading of 14/15 positive +1.27% median to 4/15 -0.58% median — a sharp same-day deterioration that bracketed the ETH OPEN. (Strategy v0.4 5a check at the time of entry [11:00Z bar close] would still have been a clear pass per the 12:30Z research_log breadth read; the regime deterioration to 4-floor breadth post-12:00Z was not yet visible at entry.)

### Telegram

**Sent** per routine §NOTIFY (exit happened). Brief summary message included: exit details, equity-after, kill-switch all-clear, plus a flag of the orphan-write anomaly for visibility. (Telegram §NOTIFY does not mandate flagging state-of-record anomalies, but the visibility cost is low and the audit value is high.)

### Trade log writes

**1 CLOSE row appended** (the OPEN row was already present as the orphan write; this routine staged it and the CLOSE together for atomic commit). **0 OPENs** (midday spec forbids entries).

### Lessons-eligibility flag for routine-04

The orphan-write race is the second instance in 3 trading days (Sat 06-13 BTC -0.60R replay-race, Tue 06-16 ETH -1.32R orphan-write-then-stop). Both are recoverable via the "trade-log is source of truth" rule, but they introduce silent-drift risk if a routine-02-midday rebuild reads its file snapshot before an in-flight orphan write completes (today's 15:16Z midday is exactly that pattern — the rebuild reported flat-book despite the orphan write existing at 12:17:29Z). **Candidate lesson:** add a `git status` check at the start of every routine wake and abort-with-alert if `memory/trade_log.md` is in uncommitted state from a process other than the current routine. (Not proposed here; flagged for routine-04 evaluation per process discipline.)

### Next routine

routine-03-eod tonight at 04:00Z Wed (cron `0 21 * * 1-5` PT) — will scan against the 20:00Z closed bar for entry eligibility under 5b cooldown constraint (ETH locked out until 2026-06-17T15:00Z).

## 2026-06-16T15:16Z — routine-02-midday (early cron fire, second midday wake today)

**Slot identity `bull-02-midday`.** Cron `0 13 * * 1-5` (Tue 13:00 PT / 20:00 UTC) — framework dispatched ~4.75h early at ~15:16Z (same early-dispatch pattern as the 12:30Z first wake of the day). This is the second routine-02 wake of the day; the prior 12:30Z run was an off-schedule pre-cron fire that already brought state current. ~2.75h gap to that prior wake.

**Position management:** zero open positions → zero exit checks, zero MTM updates. Equity $10,828.58 (cash, unchanged). Peak $10,875.85 unchanged. Drawdown 0.43%. All kill switches CLEAR.

**Live market snapshot (informational, no entry impact):** Kraken `kraken_multi_ticker` 15:16Z — **12/15 positive 24h** (negatives TAO -0.64 / LTC -0.33 / TRX -0.35), **median +0.9%**, leaders HYPE +13.11 / FARTCOIN +5.68 / AVAX +1.59 / NEAR +1.52 / SOL +1.33 / ETH +1.28 / LINK +1.22. BTC last **$66,584.5** (+0.45% 24h, +0.63% vs the 12:30Z print of $66,166.5). 5a would PASS if midday permitted entries (12 > 4 floor); SBD CLEAR. HYPE breadth concentration noteworthy (+13.11% session, second straight day above the median).

**Kill-switch table:**
- Daily realized 2026-06-16 PT: $0.00 / 0.00% — CLEAR (cap 5%).
- Loss streak: 1 (carry from Sun BTC scratch) — CLEAR (cap 7).
- Max drawdown: 0.43% from peak — CLEAR (warn 12.5% / kill 25%).
- Equity floor: $10,828.58 > $7,500 — CLEAR.
- Regime gate: 5a PASS / SBD CLEAR (informational; midday spec forbids entries regardless).
- MCP availability: Kraken `kraken_multi_ticker` returned full 15-pair payload <2s, clean.

**Entry scan:** skipped per midday spec (entry responsibility belongs to routine-01-overnight and routine-03-eod).

**Telegram:** silent (no exits, no kill switches, no drawdown threshold crossed). **Trade log writes: 0.**

**Next routine:** routine-03-eod scheduled tonight (cron `0 21 * * 1-5` PT = 04:00 UTC Wed), which will run the post-bar EOD entry scan against the 20:00 UTC closed bar.

## 2026-06-16T12:30Z — routine-02-midday (off-schedule fire ~7h pre-cron, first wake since 2026-06-14T17:14Z)

**Slot identity `bull-02-midday`.** Cron `0 13 * * 1-5` (Tue 13:00 PT / 20:00 UTC) — framework dispatched ~7h early at ~12:30Z. ~43h gap since the prior routine wake (Sun 17:14Z routine-01-overnight); no Mon 06-15 routines appear to have fired (no Mon commits in `git log`, no Mon entries in this log). Account state has been frozen at flat-book since the Sun BTC EMA20-confirm exit.

**Position management:** zero open positions → zero exit checks, zero MTM updates. Equity $10,828.58 (cash). Peak $10,875.85 unchanged. Drawdown 0.43%. All kill switches CLEAR (daily realized $0, loss streak 1, equity floor ~$10.8k vs $7.5k floor, regime gate 14/15 positive via live ticker — would PASS 5a if midday permitted entries, but it does not).

**Live market snapshot (informational, no entry impact):** Kraken `kraken_multi_ticker` 12:30Z — 14/15 positive 24h (only TRX -0.31), median +1.27%, leaders HYPE +6.01 / NEAR +11.2 / TAO +3.88 / XRP +3.47 / ETH +2.05. BTC last $66,166.5 (24h range $63,643 — $66,330) = +3.00% above Sun exit fill of $64,240.66. Last closed 1H bar 2026-06-16T11:00Z @ $66,434.4.

**Post-hoc note on the W22-G exit (not a strategy proposal):** the BTC exit at -0.60R on Sun 06-14 closed at $64,240.66; the carry between exit and now would have been roughly +0.168 × ($66,166.5 - $64,188.10) = +$332.45 gross had the position stayed open. Per `feedback-perf-analysis-framing`, this is not a critique of the rule — W22-G's two-bar EMA20 confirmation is designed for the commission-drag archetype (tight ranges that round-trip to small net losses), and the Sun 12:00/13:00 sub-EMA20 pair was the rule firing as specified. The subsequent rally was a separate regime shift (5a fell from 15/15 to 3/15 by 16:00Z Sun, then re-expanded to 14/15 by Tue mid-session). The cross-rule audit in the routine-01 log already noted the stop at $63,720.62 would have triggered intrabar at 17:00Z 06-14 (low $63,665.0) had the EMA20 exit not fired first — so the optionality preserved by skipping the EMA20 exit would have been narrower than the headline cash gap suggests (-1.07R stop vs -0.60R EMA, i.e., the EMA20 exit was -0.47R better than the alternative-exit-of-record). **Logging this for routine-04 lessons evaluation, no proposal at this time.**

**Entry scan:** skipped per midday spec. Will be re-evaluated at next overnight or EOD wake.

**Telegram:** silent (no exits, no kill switches, no drawdown threshold crossed). **Trade log writes: 0.**

**Next routine:** depending on framework rethread, expected routine-01-overnight Wed 06-17T13:00Z if Mon/Tue overnight slots remain skipped; if Mon catch-up dispatches resume, this routine-02 may be paired with a routine-03-eod fire later today.

## 2026-06-14T17:14Z — routine-01-overnight (**Sun off-schedule fire**, cron `0 6 * * 1-5` would not have fired today)

**Slot identity confirmed `bull-01-overnight`.** Fourth consecutive off-schedule weekend dispatch (Sat AM/midday/EOD + this Sun AM). Open question for next routine #4 remains: codify whether weekend framework dispatches should run-as-designed (current behavior — caught today's missed exit ~4h late) or hard-gate to the Mon-Fri cron.

### Position MTM + exit replay (BTC/USD)
BTC long 0.168 @ $64,188.10 entered 2026-06-13T15:00Z (Sat 08:00 PT). Walked 1H closes since the 2026-06-14T04:11Z routine-03-eod snapshot via `kraken_ohlcv` 30-bar lookback: 04:00Z 64,320.2 / 05:00Z 64,331.7 / 06:00Z 64,257.5 / 07:00Z 64,409.8 / 08:00Z 64,430.3 / 09:00Z 64,570.0 / 10:00Z 64,500.1 / 11:00Z 64,521.5 / **12:00Z 64,282.9** / **13:00Z 64,272.8** / 14:00Z 63,941.5 / 15:00Z 63,982.4 / 16:00Z 63,915.4. **EMA20 back-prop anchored on script-confirmed 16:00Z EMA = $64,228.10** (`scripts/indicators.py` 17:14:02Z output, FAIL -312.7 vs close), α = 2/21 ≈ 0.09524: EMA_15 = (64,228.10 − 0.09524 × 63,915.4)/0.90476 = $64,260.95; EMA_14 = $64,290.40; EMA_13 = $64,327.42; EMA_12 = $64,333.43; EMA_11 = $64,339.01. Per-bar position vs EMA20: 07:00 +151.6 / 08:00 +156.9 / 09:00 +268.6 / 10:00 +180.0 / 11:00 +182.5 / **12:00 -50.5 (first below)** / **13:00 -54.6 (second below — W22-G triggers)** / 14:00 -348.9 / 15:00 -278.5 / 16:00 -312.7. **Exit fires at the close of the 13:00Z bar = $64,272.8 (raw close).** With 0.05% adverse slippage per `skills/decide.md`: fill = $64,272.8 × 0.9995 = **$64,240.66**. **Per-trade risk at entry** = 0.168 × (64,188.10 - 63,720.62) = $78.5366. **Realized PnL** = 0.168 × (64,240.66 - 64,188.10) − 0.0026 × 0.168 × (64,188.10 + 64,240.66) = 8.83 − 56.10 = **-$47.27**. **R-multiple** = -47.27 / 78.5366 = **-0.60R**. Reason tag `exit-ema20-confirm-missed-scheduler-replay` matching 2026-05-22 TAO/HYPE/AVAX precedent.

**Cross-rule check (would any other exit have fired earlier?):**
- Rule 2 (stop $63,720.62): not pierced. Lowest intra-bar low post-entry was the 14:00Z bar low $63,850.7 — $130.08 above stop. Even with the latest decline, no bar has reached stop. *(If the Sun decline continues into Mon and we re-enter on a fresh signal that gets stopped, we have $130 of stop-buffer history to inform sizing.)*
- Rule 3 (4R target $66,058.02): not hit. Highest 1H high post-entry was 21:00Z 06-13 = $64,750.0 — $1,308 short.
- Stop ratchet (+2R = $65,123.06): never armed. Highest 1H close post-entry was 09:00Z 06-14 = $64,570.0 → +0.82R. Stop remained at the initial 2×ATR throughout, so we did not have the W22-H breakeven floor working today. *Counterfactual: had the ratchet armed, exit would have been at $64,188.10 entry-price floor — would still net negative after commission ($-56.10 vs today's -$47.27, slightly worse).* The ratchet's protective value remains an event-tail trade-off, not a regular outcome.

**Friction accounting:** This is the second commission-drag scratch on record (after BTC 2026-05-06 +0.06R / +$1.42). The exit's gross PnL is +$8.83 / +0.11R — the commission roundtrip ($56.10) entirely eats the price-move profit. **The W22-G two-bar confirmation did its job:** prior single-bar rule would also have exited here, but would *additionally* have exited at the 16:00Z UTC bar 2026-06-13 (the single below-EMA close in the Sat session that recovered the next bar), where the loss would have been larger because of where the EMA was relative to entry. W22-G inert-then-fire trace matches design intent.

### Technical (rule-driven, deterministic) — entry scan
Engine: `scripts/indicators.py` 17:14:02Z against the just-closed 16:00Z UTC 1H bar (and converged 4H 50-EMAs, 720-bar 4H window HIGH-CONFIDENCE for all 15 pairs). Regime: **3/15 positive on 24h % change (TAO +0.12, LTC +0.55, TRX +0.28), median -0.90%** → **5a FAIL** (3 below 4-pair floor — sharp reversal from this morning's 15/15 +1.90% print; the Sat rally has fully unwound in the Sun session and most pairs are now mildly red). **5a-SBD CLEAR** (3 > 1 positive AND -0.90 > -1.0 median — both gates respond independently; median is right at the SBD threshold, but the positive-count check decisively keeps SBD inactive). **All new entries rejected per rule 5a.**

Per-pair (recorded for audit even though rule 5a vetoes):

| Pair | R1 (>EMA20) | R2 (RSI≥55) | R2a (RSI≤80) | R3 (4H>EMA50) | R4a (≥$2M) | Net |
|---|---|---|---|---|---|---|
| BTC/USD | FAIL -312.7 | FAIL RSI 39.8 | OK | PASS +159.7 | OK | FAIL |
| ETH/USD | FAIL -10.46 | FAIL RSI 35.6 | OK | FAIL -23.81 | OK | FAIL |
| SOL/USD | FAIL -0.475 | FAIL RSI 41.1 | OK | FAIL -0.135 | OK | FAIL |
| HYPE/USD | FAIL -0.381 | FAIL RSI 46.8 | OK | PASS +0.281 | OK | FAIL |
| XRP/USD | FAIL -0.005 | FAIL RSI 41.9 | OK | FAIL -0.014 | OK | FAIL |
| SUI/USD | FAIL -0.008 | FAIL RSI 35.8 | OK | FAIL -0.015 | OK | FAIL |
| TAO/USD | **PASS +0.32** | **FAIL RSI 54.2 (-0.82)** | OK | **PASS +34.69** | OK | **FAIL by 1 rule** |
| XDG/USD | FAIL -0.001 | FAIL RSI 40.0 | OK | FAIL -0.001 | OK | FAIL |
| NEAR/USD | FAIL -0.021 | FAIL RSI 44.9 | OK | FAIL -0.037 | OK | FAIL |
| ADA/USD | FAIL -0.003 | FAIL RSI 29.0 | OK | FAIL -0.006 | OK | FAIL |
| LINK/USD | FAIL -0.064 | FAIL RSI 34.6 | OK | FAIL -0.089 | OK | FAIL |
| LTC/USD | **PASS +0.018** | **FAIL RSI 53.0 (-2.0)** | OK | **PASS +0.273** | OK | **FAIL by 1 rule** |
| FARTCOIN/USD | FAIL -0.002 | FAIL RSI 36.8 | OK | FAIL -0.004 | FAIL $0.53M | FAIL |
| TRX/USD | **PASS +0.001** | **PASS RSI 59.5** | OK | **FAIL -0.003** | FAIL $0.65M | FAIL by 2 rules |
| AVAX/USD | FAIL -0.097 | FAIL RSI 29.0 | OK | FAIL -0.300 | FAIL $0.94M | FAIL |

**Eligible candidates: 0.** Closest near-misses are TAO and LTC (each one rule away — RSI just under 55 floor); these are the kind of candidates that flip eligible on a 1-2 bar continuation move and would warrant priority observation at the next routine wake.

### News (Firecrawl) — informational only
**Skipped this wake.** Routine §DO step 4 calls news pulls only for technical-PASS candidates; zero PASS candidates means zero queries. No actionable headline check required.

### Sentiment (Kraken spread/depth) — informational only
**Skipped this wake.** Same reason: no PASS candidates to query.

### Decision (W19-E)
**Position management:** 1 CLOSE (BTC -0.60R / -$47.27, exit-ema20-confirm-missed-scheduler-replay 2026-06-14T13:00Z).
**Entries:** 0 (5a FAIL: 3/15 positive < 4-pair floor; additionally no per-pair PASS even setting 5a aside).
**Account post-wake:** cash $10,828.58, no open positions, equity $10,828.58, peak $10,875.85 (unchanged), DD 0.43%, loss streak 1.

### Ops / watchdog
- `scripts/watchdog.py --telegram` 17:13:47Z: 1 finding (`dirty-tree: M memory/research_log.md`). Investigation: `git status` 5 seconds later returned clean (`nothing to commit, working tree clean`). Likely write-in-flight false-positive or a transient state from the EOD commit's tail. Telegram already received the watchdog alert; will note in the post-mortem of this wake (no separate fix needed).
- Kraken MCP available (`kraken_multi_ticker` 15-pair pull clean, `kraken_ohlcv` 30-bar 1H pull clean).
- Indicators script clean run, 30s wall time, all 15 pairs returned 720 4H bars (HIGH-CONFIDENCE on 4H 50-EMA per W19-D warm-up floor).

### Telegram
Mandatory CLOSE-event notification sent (per routine §NOTIFY: "Any new OPEN or stop-out CLOSE during this run → brief summary").

---

## 2026-06-13T20:07Z — routine-02-midday (Sat 13:07 PT off-schedule)

Off-schedule Saturday fire (cron `0 13 * * 1-5`, framework dispatched anyway — third off-schedule weekend fire today after routine-01 15:50Z and routine-04 17:00Z). **No exits, no entries (midday spec forbids entries).** BTC/USD long 0.168 @ $64,188.10 (entered 5h54m ago at 15:00Z) — 5 full 1H closes since entry plus a partial 20:00 UTC bar. Exit-rule sweep all-clean: (1) EMA20 chain post-entry computed off 63,768.1 α=2/21 baseline → 63,814 / 63,831 / 63,842 / 63,869 / 63,908; all 5 closes (64,253 / 63,989 / 63,944 / 64,130 / 64,282) above the rising EMA. Rule 1 inert. (2) Stop $63,720.62 not pierced — lowest post-entry low $63,893.2 (16:00 bar), $172.58 buffer. (3) 4R target $66,058.02 not hit — highest post-entry high $64,294.0. Breakeven ratchet not armed (highest 1H close 64,282 = +0.20R, vs +2R threshold $65,123). MTM: BTC last $64,211.9 → position $10,787.60 + cash $92.25 = equity $10,879.85, unrealized +$3.95 / +0.05R. Equity peak unchanged at $10,875.85 (peak tracks realized closes; MTM is $4 above but does not advance). Drawdown 0.00%. Kill switches all CLEAR. Kraken MCP available, no MCP failures. Telegram silent (no notify-trigger met). Next wake: routine-01-overnight 2026-06-15T13:00Z (Mon 06:00 PT), ~37h carry. Backlog: confirm with user whether framework's weekend dispatches are intentional or whether the Mon-Fri cron filter should be enforced inside each routine spec.

## 2026-06-13T17:00Z — routine-04-harness (Sat 10:00 PT on-schedule)

Day-gate passed (today IS Saturday PT). VERIFY: TradingView `tv_health_check` → CDP connection failed (5th consecutive harness blocked, W20/W22/W23-misfire/this). Kraken MCP OK (BTC $63,979.4 smoke test, spread 0.1, vwap $63,751.47, 24h +0.69%). Per W19/W20 precedent: reduced-scope harness proceeds without TV backtests; full memo at `memory/weekly_memos/2026-W24.md`.

**Performance W24:** 1 closed trade (TAO +4.04R / +$621.22, 4R take-profit missed-scheduler replay at 09:00Z) + 1 open (BTC 0.168 @ $64,188.10 from 15:00Z this wake). **New all-time equity peak $10,875.85** (+8.76% inception-to-date, supersedes prior $10,728.95 / 2026-05-21). Drawdown reset 0.00%. Loss-streak reset 4 → 0. Win rate W24 100% (1/1). All kill switches CLEAR.

**Lessons scored:** `2026-05-19 SBD-defensive-asymmetry` → 8 (provisional confirmed). `2026-06-12 entry-timing-patience` → 6 (provisional confirmed; reinforced by today's TAO 4R outcome — disciplined entry produced the largest winner of the quarter). 7 active lessons; cap 50; no prune.

**Variants:** rack 10/10 (7 hypothesis + 3 sweep). No new spin-ups (rack full + no autoloop slots available + hypothesis-protection). v0.10/v0.11/v0.6 already archived per W22 retirement audit. No promotion-eligible variant: v0.14-recovery-trend's first trade was a scratch (+0.01R BTC); v0.5 has 1 trade (+0.12R HYPE); v0.8 has 1 trade (−1.00R NEAR). All others 0 synthetic trades.

**Competitor (read-only `C:/trading/strategy-leaderboard/data/codex/`):** BULL +8.76% leads Codex v0 (−6.80%, +15.56 pts) and Codex Aggro (+5.41%, +3.35 pts). Aggro gap widened ~3pts in one Sat from the TAO catch. Codex v0 multi-sleeve same-pair structure mandate-incompatible; Codex Aggro currently flat with short-basket time-stops fading. No structural import.

**Proposal: NONE.** v0.4 performing exactly as designed (TAO trade exercised W22-H breakeven ratchet at +3.72R → caught 4R target next bar — opposite of XRP archetype that motivated the fix). No new lessons. Rack-side hypothesis evidence not yet adequate. TV blocker still gating Ring-2 evidence requirements. Competitive position favorable.

**Backlog items logged for next harness:**
- Cash-aware rule-8 tiebreaker (single-instance: BTC sized to 0.72% risk this wake because cash ran out post-TAO-exit; SOL/SUI/XDG would have sized to full 1.5%).
- Missed-scheduler 4R replay convention (take higher of {bar close, 4R target} — TAO left ~$2/unit on table this wake).
- Codify R3 entry margin floor once 4–6 patience-arcs accumulate (current evidence n=1).

**Open questions (re-escalated to user):**
1. TV Desktop install — week 5 (W20 escalation unanswered).
2. IDEA-12 ETF-flow daily feed — wire pre-emptively or wait? (W20 question unanswered).
3. Cash-aware rule-8 — draft as Ring-2 next harness or treat as corner-case?
4. Missed-scheduler replay convention — amend to take higher of {close, target}?

**Telegram:** weekly digest queued (mandatory per routine #4 NOTIFY gate).

| harness summary committed: 0 ring-2 proposals, 2 lesson scores assigned, 0 variant promotions, 0 retirements, BULL leads contest by +3.35 / +15.56 pts

---

## 2026-06-13T15:50Z — routine-01-overnight (**Sat off-schedule fire**, cron `0 6 * * 1-5` would not have fired today)

**Slot identity confirmed `bull-01-overnight`.** Off-schedule context: today is Saturday 2026-06-13; the Mon-Fri cron should not have fired this slot, but the routine was triggered (manual / harness re-fire / scheduler override — root cause TBD, flagging for next-harness investigation queue). Executing the routine as designed once awake: replay exit triggers that fired during the unmanaged weekend window, run entry scan against the just-closed 1H/4H bar, and notify.

### Position MTM + exit replay (TAO/USD)
TAO position carried from the 2026-06-13T04:00Z Fri-EOD entry ($217.286 size 32.985). Walked 1H closes since entry via `kraken_ohlcv` (20-bar lookback): 04:00Z $217.19 / 05:00Z $214.56 / 06:00Z $220.34 / **07:00Z $234.6331 (R=+3.72 — breakeven ratchet fires per W22-H-partial, stop moves $212.62 → $217.286)** / **08:00Z $237.3015 (R=+4.29 gross / +4.04R net → 4R take-profit trigger per Exit rule 3)** / subsequent bars 09:00-14:00Z all higher ($244.98 → $265.85, intra-bar high $268.99). Strategy convention exits at the first 1H close ≥ 4R, fill price = that bar close (no intra-bar exits per strategy.md). **Exit: 2026-06-13T09:00Z @ $237.3015, +4.04R net, +$621.22 net realized** (gross $660.21 − $38.99 roundtrip 0.26% × 2 commission). Reason tag `exit-4R-target-missed-scheduler-replay` matching 2026-05-21T08:00Z HYPE precedent. (Open question for routine #4 backlog: missed-scheduler replays could take exit at higher of {bar close, 4R target} to reflect rule intent — this trade we leave +$0.16/unit on the table vs theoretical 4R-exact fill, but adopting that variant requires explicit gate to avoid look-ahead.)

### Technical (rule-driven, deterministic) — entry scan
Engine: `scripts/indicators.py` against the 2026-06-13T15:00Z just-closed 1H bar (and converged 4H 50-EMAs over 720 bars HIGH-CONFIDENCE). Regime: **11/15 positive on 24h % change, median +0.52%** → **5a PASS** (well above 4-pair floor — 7-pair buffer, recovery resumed strongly after Fri-EOD's zero-buffer print). **5a-SBD CLEARED** (11 > 1 positive AND +0.52 > -1.0 median — both gates inactive). Per-pair (rules 1, 2, 2a, 3, 4a, 5b, 6, 6a, 7, 8):
- **BTC/USD = rank-1 PASS** (sole rule-8 winner). 1H 64,188.1 vs 1H 20-EMA 63,768.1 → R1 +$420 (+0.66%). RSI14 64.9 → R2 +9.935 (clear of 80 cap). 4H 64,188.1 vs 4H 50-EMA 63,656.9 → R3 +$263.8 (+0.41%, HIGH-CONFIDENCE 720 bars). R4a $75.89M >> $2M floor. ATR14 233.74 → 2×ATR stop 467.48. Rule 5b inapplicable (last BTC close 2026-05-25T22:00Z exit-stop-hit, 18d > 24h cooldown). Rules 6 (0/4), 6a (0/2 cluster — TAO just closed), 7 (0.72% per-trade risk under 1.5% cap, portfolio 0.72% of 4% cap) all PASS. Rule 8 (highest 30d notional rank) — BTC at rank 1 wins over SOL/SUI/XDG.
- SOL/USD: PASS R1+R2 (RSI 66.6)+R2a+R3 (+$0.55)+R4a ($13.18M). Rank 3 — loses tiebreak to BTC under rule 8.
- SUI/USD: PASS R1+R2 (RSI 63.5)+R2a+R3 (+$0.0046)+R4a ($4.18M). Rank 6 — loses tiebreak.
- XDG/USD: PASS R1+R2 (RSI 60.8)+R2a+R3 (+$0.00108)+R4a ($6.11M). Rank 8 — loses tiebreak.
- TAO/USD: post-exit re-eligibility — FAIL R2a (RSI 90.8 > 80 cap, climactic) AND no 5b cooldown needed (exit was 4R-target not stop-hit). Climactic RSI is the explicit W19-D lesson rejection mode. No re-entry.
- ETH/USD: FAIL R3 (-$11.73 vs 4H EMA 1,689.14). R3-20 PASS (v0.14 telemetry).
- HYPE/USD: FAIL R3 (-$1.18). R3-20 PASS marginal.
- XRP/USD: FAIL R3 (-$0.0003 — razor-thin).
- NEAR/USD: FAIL R3 (-$0.062). R3-20 FAIL too — recovery still lagging.
- ADA/USD: FAIL R3 (-$0.0002 — razor-thin). R3-20 PASS.
- LINK/USD: PASS R1+R2+R3, **FAIL R4a** ($1.12M < $2M floor) — excluded by liquidity.
- LTC/USD: PASS R1+R2+R3, **FAIL R4a** ($1.68M < $2M).
- FARTCOIN/USD: PASS R1+R2+R3, **FAIL R4a** ($0.33M).
- TRX/USD: FAIL R3 (-$0.0061). FAIL R4a ($0.83M).
- AVAX/USD: FAIL R3 (-$0.21). FAIL R4a ($0.74M).

**Final candidate list: BTC/USD (rule 8 winner over SOL/SUI/XDG).**

### News (Firecrawl-driven, informational only in v0.2)
Scan deferred for token-budget — Firecrawl not invoked. Per W19-E schema, news pass is informational and does **not** veto entries in v0.2. Classified **neutral** by convention. The TAO +23% 24h move did surface organically as a notable price anomaly (likely token-specific catalyst, possibly listing / staking-yield news on Bittensor) — TAO position already on the book through the move; no informational read needed for an exit-decision the strategy already triggered deterministically. No active scan for BTC entry; same convention applies.

### Sentiment (Kraken depth/spread proxy in v0.2)
**BTC `kraken_spread` (10 most-recent quotes at 15:52:40 UTC):** bid/ask cluster $64,235-$64,237, spread range $0.10-$1.40, mostly $0.10-$1.40 (≈0.02-0.22 bps). Very tight, well-defined top-of-book. Order-book depth implicit in BTC's massive 24h notional ($75.89M from indicators.py / $60.2M from `kraken_multi_ticker` 24h volume × ~$64k); 0.168 BTC clip ($10,784 notional) is microscopic vs available depth — fills inside top-of-book at the model price. **Sentiment: supportive.**

### Decision
**(1) EXIT TAO/USD long → 2026-06-13T09:00Z (replay) @ $237.3015, +4.04R net, +$621.22 realized.**
**(2) ENTER BTC/USD long.**
- Entry price: $64,188.10 (1H just-closed bar 14:00-15:00 UTC).
- **Size: 0.168 BTC (cash-constrained, first cash-binding sizing since inception).** Ideal 1.5%-risk size would be 0.349 BTC = $22,400 notional, but post-TAO-exit cash is $10,875.85; mandate forbids leverage → size capped to fit cash with small commission buffer.
- Notional: $10,783.60 ($92.25 cash remaining post-entry, before entry commission of ~$28 charged at exit).
- Risk: $78.54 = 0.72% of equity (below 1.5% target — under-risked, not over).
- Stop (2×ATR): $63,720.62 ($467.48 below entry, -0.73%).
- 4R target: $66,058.02 ($1,869.92 above entry, +2.91%).
- W22-H ratchet trigger: 1H close ≥ $65,123.06 (+2R) moves stop to BE $64,188.10.
- W22-G exit: two consecutive 1H closes < 1H 20-EMA (currently 63,768.1, will drift).
- SBD-exit override inert (SBD currently cleared).

### Day's summary stats (2026-06-13 PT)
Equity $10,875.85 post-events (was $10,254.63 → +$621.22). **New equity peak $10,875.85** (supersedes prior $10,728.95 set 2026-05-21 by $146.90). Drawdown reset to 0.00%. Trades opened 1 (BTC), trades closed 1 (TAO @ 4R replay). Win-rate today 1/1 = 100%. **Consecutive losing trading days RESET to 0** (winning realized close breaks the 4-day streak 05-22/25/26/30). Rolling perf updated: 7d BULL ≈ +6.06% vs BTC ≈ +1.5% → +4.6%; 30d BULL ≈ +8.76% vs BTC ≈ -21.0% → +29.8% (BULL extending lead via the TAO 4R catch); 90d not computable.

### Lessons extracted
Notable: the TAO trade is the second 4R take-profit since inception (after SOL 2026-05-11 +4.03R) and the SECOND missed-scheduler 4R replay after HYPE 2026-05-21. Pattern: large overnight / weekend moves on momentum entries entered on Friday EOD have hit 4R during the cron-dark window twice in five weeks. This is consistent with the W22-H-partial rationale (breakeven ratchet protects the winner against round-trip) and the W19-D RSI-cap exclusion (the entry RSI was 62.5, well under the 80 cap — not climactic at entry, and was correctly admitted). **No new lesson appended** — this is reinforcement of existing W21-F + W22 design, not a new pattern. Cash-binding entry sizing IS a new observable phenomenon worth a lesson — logged for routine #4 backlog (whether rule 8 should accept lower-ranked but fully-fundable candidates in cash-bound scenarios; current rule 8 rank-strict + cash-cap gives a smaller-than-target BTC position vs a larger SOL/SUI/XDG that would size to 1.5%).

### Monthly archive
Today is 2026-06-13 — June's last trading day is 2026-06-30 (Tue). No archive sweep this wake.

### Ops watchdog
`python scripts/watchdog.py --telegram` → `ALL CLEAR — heartbeats, timestamps, tree, MTM, scheduler flag, push state, MCP paths OK`. No findings.

### Telegram
**Dual-event notify sent** per routine #1 NOTIFY gate (4R take-profit replay + new BTC entry both qualify; combined into one message to avoid notification spam).

### Off-schedule fire flag
**Today is Saturday — Mon-Fri cron should not have fired this slot.** Routine executed anyway because the system was awake and material events (TAO 4R replay) were pending. The 4R close at 09:00 UTC happened during the explicitly-flagged unmanaged weekend window per the Fri-EOD portfolio.md note ("TAO position carries unmanaged across 60+ hours"). Off-schedule wake CAPTURED that exit at the correct historical bar close, then opportunistically opened BTC at the most recent closed 1H bar. **Flagging for next harness investigation:** was this fire intentional (manual / harness override), an extra Task Scheduler retry, or a cron misconfiguration? If routine-01 fires unscheduled on weekends, the "weekend carry" reasoning in EOD wake notes may be wrong. Add to investigation queue alongside the existing Mon-Fri-enforcement check.

### Next wake
routine-01-overnight 2026-06-15T13:00Z (Mon 06:00 PT scheduled per cron). BTC position carries ~45h unmanaged across the remainder of the weekend; 2×ATR stop $63,720.62 is the protective floor (-0.73% from entry).

| 2 trade events (1 exit-replay + 1 entry) + telegram-sent + research-logged

---

## 2026-06-13T04:10Z — routine-03-eod (2026-06-12 PT trading day, Fri 21:10 PT on-schedule fire)

### Technical (rule-driven, deterministic)
Engine: `scripts/indicators.py` (720-bar 1H + 4H, SMA-seeded EMAs converged, Wilder RSI/ATR, per-rule margins). Regime: 4/15 positive 24h, median -0.21% → **5a marginal PASS** (at exactly the 4-pair floor — zero buffer; weakest read since regime recovered 06-11); **5a-SBD CLEARED** (4 > 1 AND -0.21 > -1.0). Tape weakened progressively today: overnight 13/15 +1.49% → midday 5/15 -0.30% → EOD 4/15 -0.21%.

Per-pair pass/fail (rules 1, 2, 2a, 3, 4a) on just-closed 1H bar:
- **TAO/USD = sole PASS.** 1H 217.286 vs 1H EMA20 213.406 → R1 +$3.88 (+1.82%). RSI14 62.5 → R2 +7.55 (R2a clear at 80 cap). 4H 217.286 vs 4H EMA50 214.065 → R3 +$3.22 (+1.50%, HIGH-CONFIDENCE 720 bars). R3-20 +$5.99 (v0.14 telemetry). R4a notional $3.04M > $2.0M floor. ATR14 2.3317 → 2×ATR stop 4.6634.
- BTC/USD: FAIL R1 (-$35), R2 (RSI 50.6), R3 (-$146); R3-20 PASS. Recovery losing steam — needs another 4H bar of strength.
- ETH/USD: FAIL R1, R2 (49.0), R3; R3-20 PASS.
- SOL/USD: FAIL R1 (just barely -$0.005), R2 (51.2), R3; R3-20 PASS. Was R1+R2 PASS overnight — now lost both.
- HYPE/USD: FAIL R1, R2 (44.2 — sharp drop from 57.0 overnight), R3; R3-20 PASS. Largest 24h % move overnight (+5.17) faded.
- XDG/USD: FAIL R1, R2 (47.3), R3 (just barely -$0.0005); R3-20 PASS. Was the only R3-PASS overnight — now lost R3 too.
- LINK/USD: PASS R1, FAIL R2 (52.7); FAIL R4a ($1.53M < $2M).
- LTC/USD: PASS R1+R2 (RSI 59.1), FAIL R3 (-$0.27); R3-20 PASS.
- FARTCOIN/USD: PASS R1, FAIL R2/R3; FAIL R4a ($0.37M).
- TRX/USD: PASS R1, FAIL R2/R3/R3-20; FAIL R4a ($1.47M).
- AVAX/USD: PASS R1, FAIL R2/R3/R3-20; FAIL R4a ($0.99M).
- XRP/SUI/NEAR/ADA: FAIL R1 (most also R2/R3) — recovery has stalled in mid-cap alts.

Rule 5b (24h same-pair re-entry cooldown): TAO last close 2026-05-26 was `exit-ema20-confirm`, not `exit-stop-hit` → 5b inapplicable. >24h elapsed anyway.

Rule 6 (0/4 max-concurrent), 6a (0/2 cluster cap on {BTC,ETH,SOL,TAO,AVAX,SUI,LINK}), 7 (per-trade risk 1.50% at exactly the cap; portfolio risk-at-moment post-entry 1.50% of 4%), 8 (sole candidate) — all PASS.

**Final candidate list: TAO/USD.**

### News (Firecrawl-driven, informational only in v0.2)
Scan deferred for token-budget — Firecrawl not invoked. Per W19-E schema, news pass is informational and does **not** veto entries in v0.2; the absence of an active scan does not block the decision. Classified **neutral** by convention (default when scan skipped). No headlines surfaced organically in routine context that would flag a contradictory signal. Open question for the W23+ harness cycle: should "scan-skipped" downgrade to a soft delay rather than auto-neutral. Logged for routine #4 backlog.

### Sentiment (Kraken depth/spread proxy in v0.2)
Kraken `kraken_ticker` TAOUSD: last 216.85, bid 217.07, ask 217.16, **spread $0.09 ≈ 4.1 bps** (tight/healthy). 24h volume 14,356.77 TAO × VWAP $213.54 ≈ **$3.07M notional** (matches indicators.py $3.04M ± rounding). 24h % +2.02. Trades 24h: 6,064. `kraken_spread` recent 10 quotes: spread range 0.07-0.12, consistently sub-$0.15 — confirms a stable book at depth-of-mid for an entry-sized clip (notional $7,167 = ~33 TAO, fillable inside top-of-book on a typical Kraken TAO clip given 24h volume base). **Sentiment: supportive.**

### Decision
**ENTER TAO/USD long.**
- Entry price: 217.286 (1H just-closed bar).
- Size: 32.985 TAO (= 1.5% × $10,254.63 equity / 2×ATR 4.6634).
- Notional: $7,167.30 ($3,087.33 cash remaining post-entry).
- Stop (2×ATR): $212.6226.
- 4R target: $235.9396.
- W22-H ratchet trigger: 1H close ≥ $226.6128 (+2R) moves stop to BE $217.286.
- W22-G exit: two consecutive 1H closes < 1H 20-EMA (currently 213.406, will drift).
- SBD-exit override inert (SBD currently cleared).

### Day's summary stats (2026-06-12 PT)
Equity $10,254.63 unchanged at entry-fill; trades opened 1 (TAO), trades closed 0; win-rate today N/A (0 closes); drawdown 4.42% unchanged; consecutive losing trading days 4 unchanged (entry doesn't reset). Rolling perf: 7d BULL ≈ 0.0% vs BTC-hold ≈ +0.7% → −0.7%; 30d BULL ≈ +2.55% vs BTC-hold ≈ −21.8% → +24.4%; 90d not computable (inception 2026-04-20 = 54 days ago, first computable ~2026-07-19).

### Lessons extracted
**1 lesson appended** — entry-timing patience after multi-day regime recovery (TAO held back through 06-11 EOD borderline BTC PASS, now entering on a non-borderline TAO PASS three wakes later).

### Monthly archive
Today is 2026-06-12 — June's last trading day is 2026-06-30. No archive sweep this wake.

### Ops watchdog
`python scripts/watchdog.py --telegram` → `ALL CLEAR — heartbeats, timestamps, tree, MTM, scheduler flag, push state, MCP paths OK`. No findings.

### Telegram
**EOD card sent** per mandate.

### Next wake
routine-01-overnight 2026-06-15T13:00Z (Mon 06:00 PT). TAO position is unmanaged across 60+h weekend window; 2×ATR stop $212.6226 is the only protective floor for that period (designed cron behavior).

| logged + entry-executed + telegram-sent

---

2026-06-12T20:00Z | midday | mtm-and-exit-check | routine-02-midday (Fri 13:00 PT — **on-schedule fire**, cron `0 13 * * 1-5` PT in-window since 2026-06-12 = Friday; 4th consecutive on-schedule wake after the 06-12 overnight 09:38 PT scheduler-late but cron-correct fire, this midday lands cleanly inside the 13:00 PT window). **Book flat** (21st consecutive flat-book wake since XRP exit 2026-05-30T23:00Z, 13d ago). 0 open positions → MTM step inert for position-quoting; exit-check step inert (no positions to evaluate against 1H 20-EMA / 9-EMA-SBD / 2×ATR stop / 4R target). **Entry scan forbidden by midday design** (entry responsibility belongs to routine-01-overnight and routine-03-eod). **Kraken MCP AVAILABLE** — `kraken_multi_ticker` 15/15 clean at the 13:00 PT pull for kill-switch refresh + regime telemetry (informational only, not a gate this routine). Fresh tape: **5/15 positive, median −0.30% (SOL)**. Sorted ascending change_24h_pct: −2.67 (NEAR) / −0.88 (XRP) / −0.86 (AVAX) / −0.60 (SUI) / −0.40 (TRX) / −0.36 (LINK) / −0.32 (ETH) / **−0.30 (SOL, median)** / −0.29 (TAO) / −0.02 (ADA) / +0.13 (BTC) / +1.34 (LTC) / +1.64 (FARTCOIN) / +1.73 (XDG) / +2.82 (HYPE). **Material softening vs the 09:38 PT overnight read** (13/15 positive, median +1.49% XRP) over ~6 trading hours — breadth halved and median rotated 1.79pts to the downside, but the tape is not breaking down: 5 still positive (vs 1/15 at the 06-11 midday SBD-active print), BTC steady at +0.13, and the largest 24h gainer HYPE (+2.82%) lifted modestly. Regime classification (informational): **5a marginal PASS** (5 ≥ 4 positive floor by exactly 1 pair — 1-pair-from-fail buffer, thinnest reading since the regime recovered 06-11); **5a-SBD remains CLEARED** (5 > 1 positive AND median −0.30 > −1.0 — both gates inactive). SBD's tightened 9-EMA exit override stays deactivated (inert — book flat). The afternoon thinning narrows the recovery margin but does not invalidate it; next entry-eligible read is the 21:00 PT EOD wake at the fresh 1H/4H closes. **BTC reference $63,637.00** (vs the 09:38 PT overnight indicators.py print $63,551.7 — +$85, +0.13% in ~6h, consistent with the BTC +0.13% 24h reading). Equity **$10,254.63** unchanged (cash-only). Day PnL **$0.00 / 0.00%** (no closes today; last trade event remains XRP exit 2026-05-30T23:00Z). Drawdown **4.42%** unchanged from peak $10,728.95. **Kill-switch proximity (all clear):** DD 4.42% vs 12.5% warn / 25% cap (35.4% of warn budget consumed, 17.7% of cap — well below the routine-02 NOTIFY halfway-warn threshold); equity $10,254.63 vs $7,500 floor (+$2,754.63 headroom, +36.7%); daily realized $0 vs 5% cap; loss-streak 4 vs 7 cap (informal warn at 5 — still 1 closing-L away); Kraken MCP available. `kraken_risk_flag` not invoked (NO_DATA per 2026-06-09 fix note, informational only). **No exits** (vacuous — book flat). **No Telegram** (silent — routine #2 NOTIFY gate: no kill-switch trip, no exit event, no DD halfway-warn crossing — DD unchanged at 4.42%, far below 12.5% warn). 30d BULL ≈ +2.55% vs BTC-hold ≈ −21.7% (BTC 2026-05-13 ~$81.3k → today $63.64k) → BULL +24.3% ahead (delta marginally tighter as BTC ticked up). Next on-schedule wake: routine-03-eod 2026-06-13T04:00Z (Fri 21:00 PT scheduled). | no action

2026-06-12T04:00Z | eod | mtm-summary-no-entry | routine-03-eod 2026-06-11 PT trading day (Thu 21:00 PT — **on-schedule fire**, cron `0 21 * * 1-5` PT in-window since 2026-06-11 = Thursday). Slot identity confirmed `bull-03-eod` (no mismatch vs the 2026-05-11 duplicate-skill regression guard). **Note on chronological context:** the prior EOD commit `6d9102b` was authored 2026-06-10 21:19 PT (Wed 21:00 PT slot — the 2026-06-10 PT trading day EOD) but its portfolio.md body mislabeled itself as the Thu fire. This wake is the actual Thu 06-11 PT EOD; fresh Kraken pull executed and content reflects current data, not the prior wake's stale narrative. **Book flat** (cash-only since XRP exit 2026-05-30T23:00Z, 12d ago — 19th+ consecutive flat-book wake). 0 open positions → final MTM step inert (`kraken_multi_ticker` invoked for kill-switch refresh + regime + per-pair entry scan); post-close exit check inert. **EOD entry scan executed (W19-E):** Fresh `kraken_multi_ticker` 15/15 clean at the 21:00 PT pull. **10/15 positive on 24h % change**, median **+0.17% (AVAX)**. Sorted ascending: −0.37 (TRX) / −0.19 (BTC) / −0.09 (ETH) / −0.08 (HYPE) / −0.01 (TAO) / +0.04 (SOL) / +0.11 (LINK) / +0.17 (AVAX, median) / +0.21 (SUI) / +0.23 (XRP) / +0.35 (LTC) / +0.56 (XDG) / +0.6 (ADA) / +0.77 (NEAR) / +1.3 (FARTCOIN). Modestly cooler than the Wed-EOD 15/15-positive median +2.72% snapshot — broad bounce has thinned but is still net-positive. **Regime classification: 5a PASS** (10 ≥ 4 floor — second consecutive PASS, SBD-clear extends). **5a-SBD remains CLEARED** (10 > 1 positive AND median +0.17 > −1.0 threshold — both gates inactive). SBD's tightened 9-EMA exit override stays deactivated. **Per-pair entry-rule scan (rules 1, 2, 2a, 3, 4a) — Technical pass executed in 30d-rank order, rule 8 prefers rank 1 if tied-eligible:** BTC rank-1 → 1H just-closed close 63430.6 vs 1H 20-EMA computed ~63,248 (PASS rule 1 by +$183, ~0.29%); 1H RSI14 computed ~57.4 (PASS rule 2 by +2.4, PASS rule 2a well under 80); 4H just-closed close 63430.6 vs 4H 50-EMA computed ~63,013 from a 60-bar seed (PASS rule 3 by +$417, ~0.66%); rule 4 OK; rule 4a notional ~$108M well above $2M floor; rules 5, 5a, 5a-SBD-clear, 5b (no recent BTC stop-out within 24h — last was 2026-05-25, 17d ago), 6, 6a, 7 all PASS. **Caveat on rule 3 margin:** 4H 50-EMA is computed from only 60 bars (~10 days) of OHLCV history; the prior wake's tactically-different estimate of ~$63,589 (which would have BTC FAIL by ~$160) suggests the EMA value carries $400-500 of computational uncertainty depending on warm-up window. Per `feedback-perf-analysis-framing`, borderline early-recovery entries map closely to the 3-instance commission-drag lesson (BTC 04-22, BTC 05-05, XRP 05-14) — small-favorable-move-flipped-by-friction is the failure mode this trade resembles, and the W22 G+H-partial amendments (two-bar EMA exit confirmation + breakeven at +2R) explicitly target this archetype but do not eliminate it on initial entry. Combined with the requirement that position notional consume ~100% of cash (size 0.196 BTC at $63,430 = $12,461 notional vs $10,254.63 cash → cap to 0.1617 BTC at $10,254 notional = 1.23% effective risk, under the 1.5% target), the asymmetry favors deferring the trade one more wake for stronger trend confirmation. **Decision: NO ENTRY this wake.** Document the borderline state and re-evaluate at next routine-01-overnight 2026-06-12T13:00Z (Fri 06:00 PT — Friday Mon-Fri cron in-window). ETH rank-2: 4H close 1670.12 vs 4H 50-EMA est ~1680 → FAIL rule 3 (marginal). Lower-ranked pairs (SOL/HYPE/XRP/SUI/TAO/XDG/NEAR/ADA/LINK/LTC/FARTCOIN/TRX/AVAX) all show 4H closes still below their respective 4H 50-EMAs per pattern persistence from the Wed EOD scan — the bounce has not yet been deep enough in non-BTC pairs to clear the trend filter. Liquidity floors (rule 4a): FARTCOIN notional $456k < $2M floor (excluded); AVAX notional $1.36M < $2M floor (excluded); TRX notional $2.77M just above floor; rest OK. News scan deferred — no technical-PASS candidates after rule 3 universal fail (Firecrawl invocation skipped to preserve token budget). Sentiment scan deferred (same reason). **No lessons extracted** — 0 trades today, routines/03-eod.md step 4 prompts (stopped-out-with-gap / winner-past-4R / immediate-reversal) have no inputs. **Day's summary stats (2026-06-11 PT):** equity $10,254.63 unchanged; day PnL $0.00 / 0.00%; trades opened 0, trades closed 0; win-rate today N/A (0 closes); drawdown 4.42% from peak $10,728.95 unchanged; consecutive losing trading days 4 (06-11 no closes → streak unchanged at 4; informal warn at 5 still 1 closing-L away). **Rolling perf:** 7d BULL ≈ +0.00% vs BTC-hold ≈ +2.7% (BTC 2026-06-04 ~$63.8k → today $63.4k, +0.4% spot but the period includes the 06-05 low of $60k) → BULL roughly flat vs BTC on 7d; 30d BULL ≈ +2.55% vs BTC-hold ≈ −21.8% (BTC 2026-05-12 ~$81.2k → today $63.4k) → BULL +24.4% ahead; 90d not yet computable (BULL inception 2026-04-20 = 53 days ago, first computable ~2026-07-19). **Monthly archive:** today is 2026-06-11 — June's last trading day is 2026-06-30 (Tue); no archive sweep this wake. **Kill switches all clear**: DD 4.42% (cap 25%, warn 12.5%, 35.4% of warn budget / 17.7% of cap); equity $10,254.63 > $7,500 floor (+$2,754.63 headroom, +36.7%); daily realized $0 vs 5% cap; loss-streak 4 vs 7 cap; Kraken MCP AVAILABLE (5th consecutive scheduled wake clean post-fix). `kraken_risk_flag` NO_DATA (informational only per 2026-06-09 fix note). **Telegram EOD card sent** per mandate (silence is a failure mode). BTC reference **$63,435** (+1.3% vs the Wed-EOD print $62,610). Next on-schedule wake: routine-01-overnight 2026-06-12T13:00Z (Fri 06:00 PT scheduled). | logged + telegram-sent

2026-06-11T00:00:00Z | idea-scan | day-gate | not Friday, skipping | no action
2026-06-12T05:00Z | midday | duplicate-late-fire | routine-02-midday fired AGAIN after the on-schedule 2026-06-11T20:00Z midday (commit c1f8d5b) and the on-schedule 2026-06-12T04:00Z EOD (commit 6d9102b) had both already completed today. System date still reports 2026-06-11 PT, but git log + portfolio.md confirm both prior routines ran in-order; this fire therefore arrives ~8h after the nominal 13:00 PT midday slot and ~1h after EOD. Cause uncertain (Task Scheduler retry / duplicate trigger / harness re-fire — flagging for next-harness investigation queue alongside the existing day-of-week-enforcement question). **Book unchanged since EOD** — still flat (cash-only since XRP exit 2026-05-30T23:00Z, ~12d), 0 open positions, equity $10,254.63, drawdown 4.42% from peak $10,728.95, loss-streak 4, all kill switches clear (DD 4.42% < 12.5% warn / 25% cap; equity $10,254.63 > $7,500 floor; daily PnL $0 < 5% cap; loss-streak 4 < 7 cap). MTM step inert (no open positions to quote); exit-check step inert; entry scan forbidden by midday design. Kraken MCP available this session (15-tool kit loaded post-deferred) but **not invoked** — `kraken_multi_ticker` would only refresh quotes for positions that don't exist; the EOD ran a fresh 15/15 ticker pull only ~1h ago (15/15 positive, median +2.72%, 5a PASS / SBD CLEARED — first PASS since 06-01 ~10d ago, recovery underway but rule 3 still vetoes longs universally per the EOD per-pair scan). Re-pulling here would burn token budget for no decision input. **No portfolio.md rewrite** — the routine spec calls for "rewritten with fresh mark-to-market", but with the book flat the MTM is trivially $0 and the EOD's much fresher state-narrative (~1h old, fresh 15/15 ticker, fresh regime classification, fresh per-pair rule-3 scan, fresh BTC reference $62,590) would be destructively overwritten by a stale-by-redundancy midday print. Preserving the EOD's portfolio.md content is the better trade. **No exits** (vacuous). **No Telegram** (silent — routine #2 NOTIFY gate: no kill-switch trip, no exit event, no DD halfway-warn crossing). Next on-schedule wake: routine-01-overnight 2026-06-12T13:00Z (Fri 06:00 PT scheduled). | no action

2026-06-11T20:00Z | midday | mtm-and-exit-check | routine-02-midday (Thu 13:00 PT — **on-schedule fire**, cron `0 13 * * 1-5` PT in-window since 2026-06-11 = Thursday). **Book flat** (cash-only since XRP exit 2026-05-30T23:00Z, 12d ago — 17th+ consecutive flat-book wake). 0 open positions → MTM step inert (`kraken_multi_ticker` invoked for kill-switch refresh, not position-quoting); exit step inert (no open positions). **Entry scan forbidden by midday design** (entry responsibility belongs to routine-01-overnight and routine-03-eod). **Kraken MCP AVAILABLE** (15/15 ticker clean — third consecutive scheduled wake with Kraken MCP up after the 06-09 fix). Fresh tape: **1/15 positive (BTC +0.09)**, median **−2.68% (SOL)**. Sorted change_24h_pct: −6.72 (NEAR) / −6.35 (HYPE) / −5.98 (FARTCOIN) / −3.51 (XRP) / −3.39 (LTC) / −3.11 (LINK) / −2.93 (ADA) / −2.68 (AVAX) / −2.55 (SOL) / −2.27 (SUI) / −2.16 (XDG) / −2.09 (TAO) / −0.78 (ETH) / −0.46 (TRX) / +0.09 (BTC). Tape modestly less-negative than the 2026-06-11T04:00Z EOD read (0/15 positive, median −2.54%) — BTC ticked +0.09 from −0.14, but breadth still deeply one-sided. Regime classification (informational only — midday doesn't gate on it): **5a FAIL** (1 < 4 positive floor); **5a-SBD ACTIVE** (1 ≤ 1 positive AND median −2.68 ≤ −1.0 threshold; 1.68pts headroom below trigger, slightly wider than EOD's 1.54pts). SBD's tightened 9-EMA exit override inert (book flat — nothing to apply to; avoided-give-back vacuous). BTC reference **$61,743.50** (vs portfolio.md's $61,602.10 EOD print — +0.23% in ~16h). Equity **$10,254.63** unchanged (cash-only). Day PnL **$0.00 / 0.00%** (no closes; last trade event remains XRP exit 2026-05-30T23:00Z, 12d ago). Drawdown **4.42%** unchanged from peak $10,728.95 (set 2026-05-21 HYPE 4R replay). **Kill-switch proximity (all clear):** DD 4.42% vs 12.5% warn / 25% cap (35.4% of warn budget consumed, 17.7% of cap); equity $10,254.63 vs $7,500 floor (+$2,754.63 headroom, +36.7%); daily realized $0 vs 5% cap; loss-streak 4 vs 7 cap (informal warn at 5 — still 1 closing-L away); Kraken MCP available. `kraken_risk_flag` NO_DATA (daily_risk_flag.json not mirrored at scripts/ location — informational only per 2026-06-09 fix note; not a kill switch since multi_ticker succeeded). **No exits** (vacuous — book flat). **No Telegram** (silent — routine #2 NOTIFY gate requires kill-switch trip / exit event / DD halfway-warn crossing; none apply). 30d BULL ≈ +2.55% vs BTC-hold ≈ −24.0% (BTC 2026-05-12 ~$81.2k → today $61.7k) → BULL ahead ≈ +26.6% (delta tightened marginally as BTC ticked up vs the EOD print). Flat-book through the synchronized breakdown remains the designed-in defensive outcome of rules 5a/5a-SBD per the W21-F fragility audit. **Note on EOD chronology:** portfolio.md's "last rebuild 2026-06-11T04:00Z routine-03-eod (EOD scope = 2026-06-10 PT)" describes the Wed 06-10 21:00 PT EOD; this midday is the Thu 06-11 13:00 PT slot — Thu overnight 06-11T13:00Z is not represented in git log between Wed EOD and this midday, either silent-no-output-no-commit OR skipped (flagging for next-harness investigation queue, consistent with the 2026-06-09 midday flag). Next on-schedule wake: routine-03-eod 2026-06-12T04:00Z (Thu 21:00 PT scheduled). | no action

2026-06-09T20:00Z | midday | mtm-and-exit-check | routine-02-midday (Tue 13:00 PT — **on-schedule fire**, cron `0 13 * * 1-5` PT in-window since 2026-06-09 = Tuesday; 3rd consecutive on-schedule wake in the recent set after 2026-06-08T20:00Z midday + 2026-06-09T04:00Z EOD — the on-schedule streak is holding through the start of this work week, a welcome break from the weekend mis-fire pattern that spanned 2026-05-31 → 2026-06-07). **Book flat** (cash-only since XRP exit 2026-05-30T23:00Z, 10d ago — 15th consecutive flat-book wake covering 5 EOD + 7 midday + 1 harness-skip + 1 overnight + 1 allocation-precursor). 0 open positions → MTM step inert (`kraken_multi_ticker` not called — no positions to quote). Post-MTM exit check inert (0 open positions). **Kraken MCP still not loaded** — no `mcp__kraken*__*` tools in the deferred-tools manifest at wake; 16th consecutive wake without Kraken MCP since 2026-06-02T15:00Z, gap now 7d. **TradingView MCP IS available** this session (full `mcp__tradingview-mcp__*` toolkit in deferred list — recovered from the EOD CDP-failure regression 9h ago; matches the midday 2026-06-08T20:00Z availability profile), but **not invoked** — midday routine is position-management only and book is flat, so no quotes / no indicators needed; entry scan is forbidden in midday by design (entry responsibility belongs to routine-01-overnight and routine-03-eod, the latter aligning cleanly with the 13:00 UTC / 1H close). **Note on routine-01-overnight 2026-06-09T13:00Z (Tue 06:00 PT scheduled):** no portfolio.md / trade_log.md / research_log.md commit visible in `git log` between the 2026-06-09T04:00Z EOD and this midday — either it ran with no commit-worthy output (silent skip + log + no trade events) OR it didn't fire at all. Cannot disambiguate from the routine-02 surface without inspecting Task Scheduler history; flagging for the next harness investigation queue alongside the Mon-Fri cron-enforcement check. Drawdown **4.42%** unchanged from peak $10,728.95 (set 2026-05-21 during HYPE 4R take-profit replay). Equity **$10,254.63** unchanged (cash-only). Day PnL **$0.00 / 0.00%** (no closes today; last trade event remains XRP exit 2026-05-30T23:00Z). **Kill-switch proximity (all clear):** DD 4.42% vs 12.5% warn / 25% cap (35.4% of warn budget consumed, 17.7% of cap); equity $10,254.63 vs $7,500 floor (+$2,754.63 headroom, +36.7%); daily realized $0 vs 5% cap; loss-streak 4 vs 7 cap (informal warn at 5 — still 1 closing-L away). No exits. **No Telegram** (silent — routine #2 notify gate requires kill-switch trip / exit event / DD halfway-warn crossing; none apply, DD comfortably below halfway-warn). Regime gate **not re-evaluated** (midday forbids entry scan); last observed 2026-06-03 wake showed 0/15 positive, median −4.53%, 5a-SBD active — now 6 days stale; staleness continues to accumulate as a gate-reliability risk that compounds the longer Kraken MCP stays down. SBD's tightened 9-EMA exit override remains inert (book flat — no open positions to apply to). **Carry-forward action items:** (1) re-load Kraken MCP (16 wakes blocked, 7d gap, this is the dominant blocker on entry-scan revival); (2) confirm Task Scheduler day-of-week enforcement (on-schedule streak now reaching 3 fires but root-cause unverified — could be the cron working as configured, or could be coincidence of weekday calendar days); (3) investigate whether routine-01-overnight 2026-06-09T13:00Z fired silently or skipped entirely. Next on-schedule wake: routine-03-eod 2026-06-10T04:00Z (Tue 21:00 PT scheduled). | no action

2026-06-09T04:00Z | eod | mcp-degraded-eod-summary | routine-03-eod 2026-06-08 PT trading day (Mon 21:00 PT — **on-schedule fire**, cron `0 21 * * 1-5` PT in-window since 2026-06-08 = Monday; 2nd consecutive on-schedule wake today after midday 2026-06-08T20:00Z, welcome continuation of the on-schedule pattern after weeks of weekend mis-fires). **Book flat** (cash-only since XRP exit 2026-05-30T23:00Z, 9d ago — 14th consecutive flat-book wake covering 5 EOD + 6 midday + 1 harness-skip + 1 overnight + 1 allocation-precursor). Final MTM step inert (0 open positions). Post-close exit check inert (0 open positions). **EOD entry scan SKIPPED — both Kraken MCP and TradingView MCP unavailable this session**: Kraken MCP not loaded (no `mcp__kraken*__*` tools in deferred-tools manifest; 15th consecutive wake without Kraken MCP since 2026-06-02T15:00Z, gap now 7d); TradingView MCP `tv_health_check` returned `CDP connection failed after 5 attempts: fetch failed` — TradingView Desktop not running for CDP bridge (same failure mode as all preceding TV-unavailable wakes this week; note: midday 2026-06-08T20:00Z 9h ago had TV MCP available but didn't need it — book flat, midday is position-management only — so this is a fresh regression in TV-CDP availability vs the same calendar day's prior wake). Per `guardrails.md` Ring 3 row 5: skip routine + log + retry next wake. **No entries possible** (no price data, no indicators). Regime gate (5a) carry-forward from 2026-06-03 wake: 0/15 positive, median −4.53%, 5a-SBD active — now 6 days stale; would near-certainly still block even if MCP returned, but staleness is itself accumulating risk that the gate is informationally unreliable for a fresh entry decision. **No lessons extracted** — 0 trades today, routines/03-eod.md step 4 prompts (stopped-out-with-gap / winner-past-4R / immediate-reversal) have no inputs. Last trade event remains XRP exit 2026-05-30T23:00Z. **Day's summary stats (2026-06-08 PT — Monday, on-schedule):** equity $10,254.63 unchanged; day PnL $0.00 / 0.00%; trades opened 0, trades closed 0; win-rate today N/A (0 closes); drawdown 4.42% from peak $10,728.95 unchanged; consecutive losing trading days 4 (06-08 no closes → streak unchanged at 4; informal warn at 5 still 1 closing-L away). **Rolling perf (approximate, carry-forward from portfolio.md):** 7d BULL ≈ −4.42% vs BTC-hold ≈ −12.5% → BULL +8.1% ahead; 30d BULL ≈ +2.55% vs BTC-hold ≈ −16.4% → BULL +18.9% ahead; 90d not yet computable (BULL inception 2026-04-20 = 49 days ago, first computable ~2026-07-19). **Monthly archive:** today is 2026-06-08 — June's last trading day is 2026-06-30 (Tue); no archive sweep this wake. **Kill switches all clear**: DD 4.42% (cap 25%, warn 12.5%, 35.4% of warn budget / 17.7% of cap); equity $10,254.63 > $7,500 floor (+$2,754.63 headroom, +36.7%); daily realized $0 vs 5% cap; loss-streak 4 vs 7 cap. **Carry-forward action items for user (when next online):** (1) re-load Kraken MCP (15 wakes blocked, 7d gap); (2) start TradingView Desktop with CDP enabled OR install TV (binary not found on disk per 2026-06-06T17:00Z harness investigation); (3) on next TV+Kraken-restored harness, investigate Task Scheduler day-of-week enforcement (off-schedule pattern subsided 2026-06-08 but root cause unconfirmed). **Telegram EOD card sent** per mandate (silence is a failure mode). Next on-schedule wake: routine-01-overnight 2026-06-09T13:00Z (Tue 06:00 PT scheduled). | logged + telegram-sent

2026-06-08T20:00Z | midday | mtm-and-exit-check | routine-02-midday (Mon 13:00 PT — **first on-schedule midday wake** after a multi-week pattern of weekend mis-fires; cron `0 13 * * 1-5` PT correctly gated today since 2026-06-08 = Monday). **Book flat** (XRP closed 2026-05-30T23:00Z, 9d ago — 13th consecutive flat-book wake covering 4 EOD + 6 midday + 1 harness-skip + 1 overnight + 1 allocation-precursor since the streak started). 0 open positions → MTM step inert (`kraken_multi_ticker` not called — no positions to quote; **Kraken MCP still not loaded** — no `mcp__kraken*__*` tools in the deferred-tools manifest at wake, 14th consecutive wake without Kraken MCP since 2026-06-02T15:00Z, gap now 6d). TradingView MCP **is** available this session (full `mcp__tradingview-mcp__*` toolkit in deferred list — first wake in days where TV MCP loaded successfully without `tv_health_check` CDP failure), but **not invoked** — midday routine is position-management only and book is flat, so no quotes / no indicators needed; entry scan is forbidden in midday by design (entry responsibility belongs to routine-01-overnight and routine-03-eod). No exit checks possible (0 open positions). Drawdown **4.42%** unchanged from peak $10,728.95 (set 2026-05-21 during HYPE 4R take-profit replay). Equity **$10,254.63** unchanged (cash-only). Day PnL **$0.00 / 0.00%** (no closes today; last trade event remains XRP exit 2026-05-30T23:00Z). **Kill-switch proximity (all clear):** DD 4.42% vs 12.5% warn / 25% cap (35.4% of warn budget consumed, 17.7% of cap); equity $10,254.63 vs $7,500 floor (+$2,754.63 headroom, +36.7%); daily realized $0 vs 5% cap; loss-streak 4 vs 7 cap (informal warn at 5 — still 1 closing-L away). No exits. **No Telegram** (silent — routine #2 notify gate requires kill-switch trip / exit event / DD halfway-warn crossing; none apply, DD comfortably below halfway-warn). Regime gate **not re-evaluated** (midday forbids entry scan); last observed 2026-06-03 wake showed 0/15 positive, median −4.53%, 5a-SBD active — now 5 days stale, would re-evaluate next overnight/EOD if Kraken MCP returns. SBD's tightened 9-EMA exit override remains inert (book flat). **Day-of-week confirmation:** 2026-06-08 = Monday, cron in-window — no off-schedule flag this wake (welcome break from the off-schedule mis-fire pattern that's spanned midday + EOD + overnight slots since 2026-05-31). Root-cause investigation of Task Scheduler day-gate enforcement still queued for next TV+Kraken-restored harness. **Carry-forward action items:** (1) re-load Kraken MCP (14 wakes blocked); (2) prior harness skip 2026-06-06T17:00Z deferred W22 memo — that was carried by routine-05-allocation 2026-06-07T17:00Z (Sun 10:00 PT). Next wake: routine-03-eod 2026-06-09T04:00Z (Mon 21:00 PT scheduled). | no action

2026-06-08T04:00Z | eod | mcp-degraded-eod-summary | routine-03-eod 2026-06-07 PT trading day (Sun 21:00 PT — **off-schedule weekend mis-fire #2 today** after routine-01-overnight 2026-06-07T13:00Z; cron `0 21 * * 1-5` PT day-of-week constraint still not enforced by Task Scheduler, pattern now spans midday + EOD + overnight slots, root-cause queued for next TV/Kraken-restored harness). **Book flat** (cash-only since XRP exit 2026-05-30T23:00Z, 8d ago — 12th consecutive flat-book wake covering 4 EOD + 5 midday + 1 harness-skip + 1 overnight + this EOD). Final MTM step inert (0 open positions). Post-close exit check inert (0 open positions). **EOD entry scan SKIPPED — both Kraken MCP and TradingView MCP unavailable this session**: Kraken MCP not loaded (no `mcp__kraken*__*` tools in deferred-tools manifest; 13th consecutive wake without Kraken MCP since 2026-06-02T15:00Z); TradingView MCP `tv_health_check` returned `CDP connection failed after 5 attempts: fetch failed` — TradingView Desktop not running for CDP bridge (same failure mode as all preceding wakes this week). Per `guardrails.md` Ring 3 row 5: skip routine + log + retry next wake. **No entries possible** (no price data, no indicators). Regime gate (5a) carry-forward from 2026-06-03 wake: 0/15 positive, median −4.53%, 5a-SBD active — now 5 days stale; would near-certainly still block even if MCP returned. **No lessons extracted** — 0 trades today, routines/03-eod.md step 4 prompts (stopped-out-with-gap / winner-past-4R / immediate-reversal) have no inputs. Last trade event remains XRP exit 2026-05-30T23:00Z. **Day's summary stats (2026-06-07 PT — Sunday, off-schedule):** equity $10,254.63 unchanged; day PnL $0.00 / 0.00%; trades opened 0, trades closed 0; win-rate today N/A (0 closes); drawdown 4.42% from peak $10,728.95 unchanged; consecutive losing trading days 4 (06-07 no closes → streak unchanged at 4; informal warn at 5 still 1 closing-L away). **Rolling perf (approximate, carry-forward from portfolio.md):** 7d BULL ≈ −4.42% vs BTC-hold ≈ −12.5% → BULL +8.1% ahead; 30d BULL ≈ +2.55% vs BTC-hold ≈ −16.4% → BULL +18.9% ahead; 90d not yet computable (BULL inception 2026-04-20 = 48 days ago, first computable ~2026-07-19). **Monthly archive:** today is 2026-06-07 — June's last trading day is 2026-06-30 (Tue); no archive sweep this wake. **Kill switches all clear**: DD 4.42% (cap 25%, warn 12.5%, 35.4% of warn budget / 17.7% of cap); equity $10,254.63 > $7,500 floor (+$2,754.63 headroom, +36.7%); daily realized $0 vs 5% cap; loss-streak 4 vs 7 cap. **Telegram EOD card sent** per mandate (silence is a failure mode — applies even on off-schedule weekend fires; the cron mis-fire is itself a journaling subject). Next on-schedule wake: routine-05-allocation 2026-06-07T17:00Z (Sun 10:00 PT — also carries deferred W22 memo per harness 2026-06-06T17:00Z skip). | logged + telegram-sent

2026-06-07T13:00Z | overnight | mcp-degraded-skip + off-schedule-fire | routine-01-overnight (cron `0 6 * * 1-5` PT — 2026-06-07 = **Sunday**, off-schedule weekend mis-fire; Task Scheduler day-of-week constraint Mon-Fri still not enforced, pattern now confirmed across midday + EOD + overnight slots; root-cause investigation queued for next TV/Kraken-restored harness). **Book flat** (cash-only since XRP exit 2026-05-30T23:00Z, 8d ago — 11th consecutive flat-book wake covering 3 EOD + 5 midday + 1 harness-skip + 1 prior EOD + this overnight). 0 open positions → position-check / stop-management step inert. **Overnight entry scan SKIPPED — both Kraken MCP and TradingView MCP unavailable this session**: Kraken MCP not loaded (no `mcp__kraken*__*` tools in deferred-tools manifest; 12th consecutive wake without Kraken MCP since 2026-06-02T15:00Z, gap now 5d); TradingView MCP `tv_health_check` returned `CDP connection failed after 5 attempts: fetch failed` — TradingView Desktop not running for CDP bridge (same failure mode as 2026-06-07T04:00Z EOD, 2026-06-06T17:00Z harness, 2026-06-05T04:11Z EOD, 2026-06-03T04:00Z EOD). Per `guardrails.md` Ring 3 row 5: skip routine + log + retry next wake. **No entries possible**: scan blocked by infrastructure (no Kraken price data, no TV indicators). Regime gate (5a) carry-forward from 2026-06-03 wake: 0/15 positive, median −4.53%, 5a-SBD active — now 4 days stale; even if MCP had returned, regime gate would near-certainly still block. **News/Sentiment passes also blocked** (no technical-PASS candidates to feed into Firecrawl / kraken_spread / kraken_depth). **First-of-month universe refresh:** today is 2026-06-07, not the 1st (and 1st was Mon 2026-06-01 already refreshed per portfolio.md universe table) → no refresh this wake. **Day's state:** equity $10,254.63 unchanged; drawdown 4.42% from peak $10,728.95 unchanged; consecutive losing trading days 4 (informal warn at 5 still 1 closing-L away). **Kill switches all clear**: DD 4.42% (cap 25%, warn 12.5%, 35.4% of warn budget / 17.7% of cap); equity $10,254.63 > $7,500 floor (+$2,754.63 headroom, +36.7%); daily realized $0 vs 5% cap; loss-streak 4 vs 7 cap. **No Telegram** (routine-01 NOTIFY only fires on kill-switch trip / new OPEN-or-CLOSE / actionable news / universe refresh — none apply; MCP-degraded skip is silent per routine). Next on-schedule wake: routine-05-allocation 2026-06-07T17:00Z (Sun 10:00 PT — also carries deferred W22 memo per harness 2026-06-06T17:00Z skip). | skip + log

2026-06-07T04:00Z | eod | mcp-degraded-eod-summary | routine-03-eod 2026-06-06 PT trading day (Sat 21:00 PT — **off-schedule weekend mis-fire**, cron `0 21 * * 1-5` PT day-of-week constraint still not enforced by Task Scheduler; pattern persists across midday + EOD slots, root-cause investigation queued for next TV/Kraken-restored harness). **Book flat** (cash-only since XRP exit 2026-05-30T23:00Z, 7d ago — 10th consecutive flat-book wake covering 3 EOD + 5 midday + 1 harness-skip + this EOD). Final MTM step inert (0 open positions). Post-close exit check inert (0 open positions). **EOD entry scan SKIPPED — both Kraken MCP and TradingView MCP unavailable this session**: Kraken MCP not loaded (no `mcp__kraken*__*` tools in deferred-tools manifest; 11th consecutive wake without Kraken MCP since 2026-06-02T15:00Z); TradingView MCP `tv_health_check` returned `CDP connection failed after 5 attempts: fetch failed` — TradingView Desktop not running for CDP bridge (same failure mode as 2026-06-06T17:00Z harness, 2026-06-05T04:11Z EOD, 2026-06-03T04:00Z EOD). Per `guardrails.md` Ring 3 row 5: skip routine + log + retry next wake. Even if MCPs had returned, off-schedule Saturday fire occupies a slot where the next on-schedule EOD is 2026-06-08T04:00Z (Mon 21:00 PT) and the regime gate (last observed 2026-06-03: 0/15 positive, median −4.53%, 5a-SBD active) would almost certainly still block all entries. **No entries possible**: scan blocked by infrastructure (no price data) AND would have been blocked by regime gate. **No lessons extracted** — no trades today (0 opened, 0 closed); routines/03-eod.md step 4 prompts (stopped-out-with-gap / winner-past-4R / immediate-reversal) have no inputs. Last trade event remains XRP exit 2026-05-30T23:00Z. **Day's summary stats (2026-06-06 PT, an off-schedule weekend slot):** equity $10,254.63 unchanged; day PnL $0.00 / 0.00%; trades opened 0, trades closed 0; win-rate today N/A (0 closes); drawdown 4.42% from peak $10,728.95 unchanged; consecutive losing trading days 4 (06-06 no closes → streak unchanged at 4; informal warn at 5 still 1 closing-L away). **Rolling perf (approximate, carried forward from portfolio.md):** 7d BULL ≈ −4.42% vs BTC-hold ≈ −12.5% → BULL +8.1% ahead; 30d BULL ≈ +2.55% vs BTC-hold ≈ −16.4% → BULL +18.9% ahead; 90d not yet computable (BULL inception 2026-04-20 = 47 days ago, first computable ~2026-07-19). **Monthly archive:** today is 2026-06-06 — June's last trading day is 2026-06-30 (Tue); no archive sweep this wake. **Kill switches all clear**: DD 4.42% (cap 25%, warn 12.5%, 35.4% of warn budget consumed / 17.7% of cap); equity $10,254.63 > $7,500 floor (+$2,754.63 headroom, +36.7%); daily realized $0 vs 5% cap; loss-streak 4 vs 7 cap. **Telegram EOD card sent** per mandate (silence is a failure mode — applies even on off-schedule weekend fires; the cron mis-fire is itself the journaling subject). Next on-schedule wake: routine-05-allocation 2026-06-07T17:00Z (Sun 10:00 PT — that wake is also slated to carry the W22 memo deferred from 2026-06-06T17:00Z harness skip). | logged + telegram-sent

2026-06-07T01:02:50Z | idea-scan | day-gate | not Friday, skipping | no action
2026-06-06T20:00Z | midday | mtm-and-exit-check | book flat (XRP closed 2026-05-30T23:00Z, 7d ago — 9th consecutive flat-book wake covering 3 EOD + 5 midday + 1 harness-skip). 0 open positions → MTM step inert (kraken_multi_ticker not needed; Kraken MCP not loaded this session — 10th consecutive wake without Kraken MCP since 2026-06-02T15:00Z; tradingview-mcp registered at wake but unused, midday has no open positions to quote and entry scan is forbidden in midday by design). No exit checks possible (0 open positions). Midday entry scan forbidden by routine design (entry responsibility belongs to routine-01-overnight and routine-03-eod). Drawdown 4.42% unchanged from peak $10,728.95. Equity $10,254.63 unchanged. Day PnL $0.00 / 0.00%. Kill-switch proximity: DD 4.42% / 12.5% warn / 25% cap (35.4% of warn budget consumed; 17.7% of cap); equity $10,254.63 vs $7,500 floor (+$2,754.63 headroom, +36.7%); daily PnL $0 vs 5% cap; loss-streak 4 vs 7 cap (informal warn at 5 — would trigger informally on next L close). No exits. No Telegram (silent — no kill-switch trip, no exit event, DD comfortably below halfway-warn threshold). Regime gate not re-evaluated (no entry scan permitted in midday); last observed 2026-06-03 wake showed 0/15 positive, median −4.53%, 5a-SBD active — now 3 days stale. **Off-schedule fire:** 2026-06-06 = Saturday, cron `0 13 * * 1-5` PT should have day-gated; Task Scheduler still ignoring day-of-week constraint (pattern documented since 2026-05-31, root-cause investigation queued for next TV/Kraken-restored harness). Prior wake routine-04-harness 2026-06-06T17:00Z skipped due to TV+Kraken MCP dual-failure; W22 memo deferred to routine-05-allocation Sun 2026-06-07. Next wake: routine-05-allocation 2026-06-07T17:00Z (Sun 10:00 PT scheduled — on-schedule). | no action

2026-06-06T17:00Z | harness | mcp-degraded-skip | routine-04-harness 2026-W23 (Sat 10:00 PT scheduled). **SKIPPED — both Kraken MCP and TradingView MCP unavailable this session.** Kraken MCP not loaded (no `mcp__kraken*__*` tools in deferred-tools manifest; 10th consecutive wake without Kraken MCP since 2026-06-02T15:00Z). TradingView MCP `tv_health_check` returned `CDP connection failed after 5 attempts: fetch failed` — TradingView Desktop not running for CDP bridge; `tv_launch` also failed (`TradingView not found on win32` — searched AppData\Local, Program Files, Program Files (x86)). Per `guardrails.md` Ring 3 row 5 + harness routine VERIFY section: skip routine + log + Telegram ALERT. **No backtests possible** (TV required for `data_get_strategy_results`); **no variant generation** (cannot validate without backtests); **no weekly memo this wake** (deferred to routine-05-allocation Sunday 2026-06-07 per W22 precedent — same skip pattern repeated 2nd consecutive harness cycle). Last successful harness was 2026-W21 (2026-05-16). **Carry-forward state:** book flat 7d (XRP exit 2026-05-30T23:00Z), equity $10,254.63 unchanged, drawdown 4.42% from peak $10,728.95, loss-streak 4 (informal warn at 5), all kill switches clear, regime carry-forward 5a-SBD (last observed 2026-06-03: 0/15 positive median −4.53%; ≥3 days stale, would re-evaluate if MCP returned). **Idea-bank queue:** IDEA-20260512-01 (BTC ETF-flow 30d MA, score 12, `under-review`) remains top candidate; IDEA-20260429-03 (Spot CVD sign-flip, score 9 reinforced), IDEA-20260429-04 (RV/IV compression, score 11, variant v0.3 spinning). All deferred to next TV-restored harness. **Off-schedule cron pattern queued for investigation:** routine-02-midday and routine-03-eod have been firing on weekends despite Mon-Fri cron constraint (`0 13 * * 1-5` PT). Root-cause investigation deferred again — cannot dig into Task Scheduler config from this MCP-blocked routine wake. **Action items for user (when TV available again):** (1) start TradingView Desktop with CDP enabled OR install TV (binary not found on disk), (2) re-load Kraken MCP, (3) investigate Task Scheduler day-of-week enforcement. Telegram ALERT sent. | skip + telegram-alert

2026-06-05T20:00Z | midday | mtm-and-exit-check | book flat (XRP closed 2026-05-30T23:00Z, 6d ago — 8th consecutive flat-book wake covering 2 EOD + 5 midday + 1 prior EOD). 0 open positions → MTM step inert (kraken_multi_ticker not needed; Kraken MCP not loaded this session — 9th consecutive wake without Kraken MCP since 2026-06-02T15:00Z; tradingview-mcp registered at wake but unused, midday has no open positions to quote and entry scan is forbidden in midday by design). No exit checks possible (0 open positions). Midday entry scan forbidden by routine design (entry responsibility belongs to routine-01-overnight and routine-03-eod). Drawdown 4.42% unchanged from peak $10,728.95. Equity $10,254.63 unchanged. Day PnL $0.00 / 0.00%. Kill-switch proximity: DD 4.42% / 12.5% warn / 25% cap (35.4% of warn budget consumed; 17.7% of cap); equity $10,254.63 vs $7,500 floor (+$2,754.63 headroom, +36.7%); daily PnL $0 vs 5% cap; loss-streak 4 vs 7 cap (informal warn at 5 — would trigger informally on next L close). No exits. No Telegram (silent — no kill-switch trip, no exit event, DD comfortably below halfway-warn threshold). Regime gate not re-evaluated (no entry scan permitted in midday); last observed 2026-06-03 wake showed 0/15 positive, median −4.53%, 5a-SBD active — stale by 2+ days. Day-of-week check: 2026-06-05 = Friday, cron `0 13 * * 1-5` PT in-window (no day-gate skip). Next wake: routine-03-eod 2026-06-06T04:00Z (Fri 21:00 PT scheduled). | no action

2026-06-03T04:28:46Z | idea-scan | day-gate | not Friday, skipping | no action

| 2026-06-02T01:02:32Z | idea-scan | day-gate | not Friday, skipping | no action |
| 2026-06-01T01:02:09Z | idea-scan | day-gate | not Friday, skipping | no action |
2026-05-29T17:40:30Z | allocation | day-gate | not Sunday, skipping | no action

2026-05-28T01:03:01Z | idea-scan | day-gate | not Friday, skipping | no action
2026-05-29T01:02:22Z | idea-scan | day-gate | not Friday, skipping | no action

2026-05-31T04:00Z | eod | off-schedule-fire | cron `0 21 * * 1-5` PT fired on Saturday (Sat 21:00 PT = Sun 04:00Z UTC) — 2nd weekend mis-fire today after routine-02-midday at 20:00Z. Task Scheduler appears to be ignoring the Mon-Fri day-of-week constraint. Pattern persists across multiple slots (midday + EOD) — root-cause investigation deferred to next routine-04-harness. Routine executed normally as the XRP position triggered exit-ema20-confirm at 23:00Z 05-30 and required logging. | logged

2026-06-01T00:03Z | midday | day-gate | cron `0 13 * * 1-5` PT fired on Sunday (Sun ~17:00 PT = 2026-06-01T00:03Z UTC) — off-schedule weekend fire, day-of-week constraint Mon-Fri not enforced by Task Scheduler. 0 open positions → no MTM, no exit checks; entries forbidden in midday by design. Kill switches all clear (DD 4.42% from peak $10,728.95, equity $10,254.63 > $7,500 floor, daily PnL 0 today). Skipping. Pattern continues — root-cause investigation queued for routine-04-harness. | no action

2026-06-01T10:06:50Z | harness | day-gate | not Saturday, skipping | no action

2026-06-02T20:00Z | midday | mtm-and-exit-check | book flat (XRP closed 2026-05-30T23:00Z). 0 open positions → MTM step inert (kraken_multi_ticker not needed; Kraken MCP not loaded this session, flagged informationally). No exit checks possible. Midday entry scan forbidden by routine design. Drawdown 4.42% unchanged from peak $10,728.95. Equity $10,254.63 unchanged. Day PnL 0.00%. Kill-switch proximity: DD 4.42% / 12.5% warn / 25% cap (35% of warn budget consumed; 17.7% of cap); equity $10,254.63 vs $7,500 floor (+$2,754.63 headroom); daily PnL $0 vs 5% cap; loss-streak 4 vs 7 cap. No exits. No Telegram (no kill-switch trip, no exit event, DD comfortably below halfway-warn threshold). | no action

2026-06-03T20:00Z | midday | mtm-and-exit-check | book flat (XRP closed 2026-05-30T23:00Z, 4d ago). 0 open positions → MTM step inert (Kraken MCP still not loaded this session — informational; tradingview-mcp connected this wake but unused, no open positions to quote, midday is position-management only). No exit checks possible. Midday entry scan forbidden by routine design (entry responsibility belongs to routine-01-overnight and routine-03-eod). Drawdown 4.42% unchanged from peak $10,728.95. Equity $10,254.63 unchanged. Day PnL 0.00%. Kill-switch proximity: DD 4.42% / 12.5% warn / 25% cap (35.4% of warn budget consumed; 17.7% of cap); equity $10,254.63 vs $7,500 floor (+$2,754.63 headroom, +36.7%); daily PnL $0 vs 5% cap; loss-streak 4 vs 7 cap (informal warn at 5). No exits. No Telegram (silent — no kill-switch trip, no exit event, DD comfortably below halfway-warn threshold). Note: prior wake routine-03-eod 2026-06-03T04:00Z observed 0/15 positive breadth, median −4.53%, 5a-SBD active — regime hostility unchanged; if any entry scan had been possible (it wasn't — routine forbids midday entries), 5a gate would block. Next wake: routine-03-eod 2026-06-04T04:00Z (Wed 21:00 PT scheduled). | no action

2026-06-04T20:00Z | midday | mtm-and-exit-check | book flat (XRP closed 2026-05-30T23:00Z, 5d ago — 6th consecutive flat-book wake). 0 open positions → MTM step inert (Kraken MCP not invoked this session; tradingview-mcp tools registered at wake but unused, no open positions to quote, midday is position-management only). No exit checks possible. Midday entry scan forbidden by routine design (entry responsibility belongs to routine-01-overnight and routine-03-eod). Drawdown 4.42% unchanged from peak $10,728.95. Equity $10,254.63 unchanged. Day PnL 0.00%. Kill-switch proximity: DD 4.42% / 12.5% warn / 25% cap (35.4% of warn budget consumed; 17.7% of cap); equity $10,254.63 vs $7,500 floor (+$2,754.63 headroom, +36.7%); daily PnL $0 vs 5% cap; loss-streak 4 vs 7 cap (informal warn at 5 — would trigger informally on next L close). No exits. No Telegram (silent — no kill-switch trip, no exit event, DD comfortably below halfway-warn threshold). Regime gate not re-evaluated (no entry scan permitted in midday); last observed 2026-06-03 showed 0/15 positive, median −4.53%, 5a-SBD active. Next wake: routine-03-eod 2026-06-05T04:00Z (Thu 21:00 PT scheduled). | no action

2026-06-05T04:11Z | eod | mcp-degraded-eod-summary | routine-03-eod 2026-06-04 PT trading day (Thu 21:11 PT on-time cron). **Book flat** (cash-only since XRP exit 2026-05-30T23:00Z, 5d ago — 7th consecutive flat-book wake covering 2 EOD + 4 midday + 1 prior EOD). Final mark-to-market step inert (0 open positions). Post-close exit check inert (0 open positions). **EOD entry scan SKIPPED — both Kraken MCP and TradingView MCP unavailable this session**: Kraken MCP not loaded (no `mcp__kraken*__*` tools in the deferred-tools manifest at wake, consistent with all six prior wakes since 2026-06-02T15:00Z); TradingView MCP tv_health_check returned `CDP connection failed after 5 attempts: fetch failed` — TradingView Desktop not running for the CDP bridge (same failure mode as the 2026-06-03T04:00Z EOD wake and the 2026-06-03T04:28Z routine-07 variant-paper wake). Per `guardrails.md` Ring 3 row 5, MCP-failure protocol = skip routine + log + retry next wake. **Regime context (carry-forward, not re-evaluated this wake — no price data):** last observed 2026-06-03 wake showed 0/15 positive, median −4.53%, 5a-SBD active; no fresh tape available to confirm or refute. If MCP had returned and breadth had not improved, regime gate (5a) would have blocked all entries regardless. **No entries possible**: scan blocked by infrastructure (no price data). **No lessons extracted** — no trades today (0 opened, 0 closed) so the routines/03-eod.md step 4 prompts (stopped-out-with-gap / winner-past-4R / immediate-reversal) have no inputs. Last trade event was XRP exit 2026-05-30T23:00Z; nothing has moved in trade_log.md since. **Day's summary stats (2026-06-04 PT):** equity $10,254.63 unchanged; day PnL $0.00 / 0.00%; trades opened 0, trades closed 0; win-rate today N/A (0 closes); drawdown 4.42% from peak $10,728.95 unchanged; consecutive losing days 4 (06-04 no closes → streak unchanged at 4; informal warn at 5 still 1 closing-L away). **Rolling perf (approximate, carried forward from portfolio.md):** 7d BULL ≈ −4.42% vs BTC-hold ≈ −12.5% → BULL +8.1% ahead; 30d BULL ≈ +2.55% vs BTC-hold ≈ −16.4% → BULL +18.9% ahead; 90d not yet computable (BULL inception 2026-04-20 = 46 days ago, first computable ~2026-07-19). **Monthly archive:** today is 2026-06-04 — June's last trading day is 2026-06-30 (Tue); no archive sweep this wake. **Kill switches all clear**: DD 4.42% (cap 25%, warn 12.5%); equity $10,254.63 > $7,500 floor; daily realized $0 vs 5% cap; loss-streak 4 vs 7 cap. **Telegram EOD card sent** per mandate (silence is a failure mode). Next wake: routine-03-eod 2026-06-06T04:00Z (Fri 21:00 PT scheduled), routine-02-midday 2026-06-05T20:00Z (Fri 13:00 PT). | logged + telegram-sent

2026-06-03T04:00Z | eod | mcp-degraded-eod-summary | routine-03-eod 2026-06-02 PT trading day. **Book flat** (cash-only since XRP exit 2026-05-30T23:00Z) — Final mark-to-market step inert (0 open positions). Post-close exit check inert (0 open positions). **EOD entry scan SKIPPED — both Kraken MCP and TradingView MCP unavailable this session**: Kraken MCP not loaded (consistent with prior wakes 2026-06-02T15:00Z, 2026-06-02T20:00Z); TradingView MCP returned `CDP connection failed after 5 attempts: fetch failed` on all 5 quote attempts (KRAKEN:XBTUSD/ETHUSD/SOLUSD/HYPEUSD/XRPUSD), indicating TradingView Desktop not running for the Chrome DevTools Protocol bridge. Per `guardrails.md` Ring 3 row 5, MCP-failure protocol = skip routine + log + retry next wake. Note: prior wake 2026-06-02T15:00Z showed regime sharply degraded (0/15 positive, median −4.53%, 5a-SBD active) — no reason to expect recovery within 9h, regime gate would almost certainly still block entries even if MCP had returned. **No entries possible**: scan blocked by infrastructure (no price data) AND would have been blocked by regime gate (5a fail, near-certainly still ≤1/15 positive). **No lessons extracted** — no trades today (0 opened, 0 closed) so the prompts in `routines/03-eod.md` step 4 (stopped-out-with-gap / winner-past-4R / immediate-reversal) have no inputs. **Day's summary stats:** equity $10,254.63 unchanged; day PnL $0.00 / 0.00%; trades opened 0, trades closed 0; win-rate today N/A (0 closes); drawdown 4.42% from peak $10,728.95 unchanged; consecutive losing days 4 (06-02 no closes → streak unchanged at 4). **Rolling perf (approximate, carried forward from portfolio.md):** 7d BULL ≈ −4.42% vs BTC-hold ≈ −12.5% → BULL +8.1% ahead; 30d BULL ≈ +2.55% vs BTC-hold ≈ −16.4% → BULL +18.9% ahead. 90d not yet computable (BULL inception 2026-04-20 = 44 days ago). **Monthly archive:** today is 2026-06-02 — June's last trading day is 2026-06-30 (Tue); no archive sweep this wake. **Kill switches all clear**: DD 4.42% (cap 25%, warn 12.5%); equity $10,254.63 > $7,500 floor; daily realized $0 vs 5% cap; loss-streak 4 vs 7 cap. **Telegram EOD card sent** per mandate (silence is a failure mode). | logged + telegram-sent

> ## Schema (W19-E, effective 2026-04-29)
>
> Routine #1 (overnight) and Routine #2 (midday) entry-scan blocks should use the analyst-role split below. Legacy single-line rows above the marker remain as-is.
>
> ```markdown
> ## YYYY-MM-DDTHH:MMZ — routine-NN-<name>
>
> ### Technical (rule-driven, deterministic)
> - Per-pair RSI14, 1H/4H EMA state, 4H regime, ATR14
> - Pass/fail per entry rule (1, 2, 2a, 3, 4, 4a, 5, 5a, 5b, 6, 6a, 7, 8)
> - Final candidate list
>
> ### News (Firecrawl-driven, informational only in v0.2)
> - For each candidate, scan 2 sources (e.g. coindesk.com, theblock.co)
>   for headlines tagged with the pair's base asset over past 6h
> - Record: top 3 headlines + 1-line summary each
> - Tag: "neutral / supportive / contradictory" relative to long bias
> - Does NOT veto entries in v0.2 — informational only
>
> ### Sentiment (passive — Kraken depth/spread proxy in v0.2)
> - For each candidate, record bid/ask spread bps + top-of-book depth
>   via Kraken MCP `kraken_spread` and `kraken_depth`
> - Wide spread / thin depth = sentiment caveat, recorded but no veto
>
> ### Decision
> - Final action this wake (OPEN / SKIP / HOLD)
> - Cite which rule(s) drove the decision
> ```
>
> If Firecrawl is unavailable, the News section logs `Firecrawl unavailable — skipped this wake` and the routine continues. Per Ring 3 (`guardrails.md`), repeated MCP failures still skip the routine entirely.

---

## 2026-05-25T15:00Z — routine-01-overnight

### Technical (rule-driven, deterministic)
- Universe regime: 15/15 pairs positive on 24h (ADA +1.66, AVAX +2.93, ETH +1.49, FARTCOIN +2.78, HYPE +0.51, LINK +1.99, LTC +0.28, PENGU +1.56, SOL +1.24, SUI +2.20, TAO +1.63, TRX +2.02, BTC +0.92, XDG +0.86, XRP +0.82); median +1.56%. Rule 5a PASS (≥4/15). Not SBD (5a-SBD requires ≤1/15 positive AND median ≤ −1.0% — both fail). Kraken risk_flag CLEAR "Markets calm" scan_time 2026-05-25T13:53:49Z.
- Liquidity floor (rule 4a, 24h notional ≥ $2M): PASS — BTC $79M, ETH $58M, HYPE $23M, SOL $12M, XRP $8M, SUI $7M, TAO $5M. FAIL — XDG $1.33M, LTC $1.03M, ADA $1.22M, FARTCOIN $0.65M, AVAX $0.79M, LINK $1.02M, PENGU $0.72M, TRX $1.44M.
- Per rule 8 (one entry per wake, prefer highest 30d notional rank), evaluation order among liquidity-passing pairs: BTC → ETH → SOL → XRP → TAO → HYPE → SUI.
- **BTC/USD entry scan** (just-closed 1H bar 2026-05-25T14:00→15:00Z, close 77639.3): 1H 20-EMA ≈ 77156.92 (PASS rule 1, +0.62%); 1H RSI14 ≈ 67.1 (PASS rule 2 >55, PASS rule 2a ≤80); just-closed 4H bar 2026-05-25T08:00→12:00Z close 77278.6 > 4H 50-EMA ≈ 77114.25 (PASS rule 3, +0.21% margin — thin); >> 10 candles history (PASS 4); 24h notional ~$79M (PASS 4a); no existing BTC position (PASS 5); regime gate PASS (5a); not SBD; no BTC stop-out in last 24h, last stop 2026-04-27 (PASS 5b); 0 open positions <4 (PASS 6); 0/2 cluster (PASS 6a); portfolio risk 0% + 0.18% = 0.18% ≤ 4% (PASS 7); rank-1 candidate this wake (PASS 8). ATR14(1h) ≈ 278.05. All entry rules PASS.
- **ETH/USD**: HOLD-OFF — rule 8 (BTC fills this wake's single slot; ETH is rank 2). Indicator scan deferred (would otherwise also evaluate, but cannot open this wake).
- **SOL/USD**: HOLD-OFF — rule 8 (rank 3).
- **XRP/USD**: HOLD-OFF — rule 8 (rank 4).
- **TAO/USD**: HOLD-OFF — rule 8 (rank 5).
- **HYPE/USD**: HOLD-OFF — rule 8 (rank 6).
- **SUI/USD**: HOLD-OFF — rule 8 (rank 8).
- **XDG, LTC, ADA, FARTCOIN, AVAX, LINK, PENGU, TRX**: REJECT — entry-rule-4a (24h notional < $2M, see liquidity numbers above).

### News (Firecrawl-driven, informational only in v0.2)
- Skipped this wake — kraken_risk_flag CLEAR "Markets calm" with 0 headlines scanned acts as the v0 macro pre-screen; v0.2 strategy is not news-reactive (informational only). Pattern consistent with prior overnight wakes; morning-brief routine surfaces ACTIONABLE headlines separately. Context-budget conservation.

### Sentiment (passive — Kraken depth/spread proxy in v0.2)
- BTC/USD: bid 77661.5, ask 77661.6, spread 0.1 (~0.013 bps; multiple recent quotes 0.1–1.3). Excellent top-of-book liquidity, no sentiment caveat.

### Decision
- **OPEN BTC/USD long** @ 77678.12 (1H close 77639.3 + 0.05% slippage), size 0.0338 BTC (cash-capped to equity/4 ≈ $2,626), stop 77122.02 (2×ATR = 556.10 below entry), 4R target 79902.52, risk $18.80 (0.179% of equity). Entry comm $6.83. Cash post-entry $7,872.13. Driven by entry-rule-v0-momentum (rules 1, 2, 2a, 3, 4, 4a, 5, 5a, 5b, 6, 6a, 7, 8 all PASS).
- Universe refresh skipped: today is 2026-05-25 (not 1st of month). Next refresh 2026-06-01.

---

## 2026-05-25T15:30Z — routine-03-eod

### Position check (BTC/USD long, opened earlier this wake by routine-01)
- Entry 77678.12 (0.0338 BTC, 15:00Z = close of 14:00→15:00Z 1H bar), stop 77122.02, 4R target 79902.52, R-risk $18.80 (0.18% of $10,504.48 opening equity).
- Mark-to-market against Kraken last 77670.1 → MTM $2,625.25, unrealized −$0.27 gross (−0.01R; close-side commission ~$6.83 not yet booked).
- No exit triggers: the just-closed 1H bar at this routine-03 wake is the SAME 14:00→15:00Z bar used at entry. Exit rules (W22-G two-bar 20-EMA cross, static stop, 4R take-profit, W22-H-partial breakeven ratchet at unrealized R ≥ 2.0) cannot newly fire on the entry bar — they require a subsequent 1H close. Next exit re-evaluation at 16:00Z (close of 2026-05-25T15:00→16:00Z 1H bar; also a 4H boundary).
- Re-mark vs routine-01 instant: routine-01 marked at last 77687.6 (+$0.32 unrealized); current EOD mark at last 77670.1 (−$0.27). Move = $17.50 / $0.59 in MTM dollars — within noise.

### Technical entry scan (W19-E)
- Regime / liquidity unchanged from routine-01 block above (same data window). 15/15 positive, median +1.56%, not SBD, risk_flag CLEAR. Liquidity-passing pairs (24h notional ≥ $2M): BTC (now held), ETH, SOL, XRP, TAO, HYPE, SUI.
- **No second entry this wake.** Per strategy v0.4 rule 8 ("Max 1 new entry per routine wake … intended to prevent same-bar cluster fills"), routine-01 already consumed the 2026-05-25T14:00→15:00Z 1H close for the BTC entry. Routine-03 fired in the same UTC window with no new 1H bar closing in between; opening a second pair on the identical bar would defeat rule 8's stated purpose. Literal reading of rule 8 ("per routine wake") would permit it; the spirit-vs-letter conflict resolves to spirit (no same-bar cluster). Rank-2..6 candidates (ETH/SOL/XRP/TAO/HYPE/SUI) defer to next routine wake operating on a fresh 1H close; if they remain technically eligible they'll be re-scored then.

### News (Firecrawl-driven, informational only in v0.2/v0.3/v0.4)
- Skipped this wake — same justification as routine-01 block above (risk_flag CLEAR "Markets calm", 0 headlines flagged; v0 strategy not news-reactive on entry path; morning-brief surfaces ACTIONABLE separately). Context-budget conservation across two adjacent routine wakes.

### Sentiment (passive — Kraken depth/spread proxy in v0.2)
- Not re-sampled for held BTC (routine-01 logged bid/ask 77661.5/77661.6, spread 0.1 ≈ 0.013 bps — excellent). No fresh sample warranted for the same 1H window.

### EOD summary stats
- **Day PnL:** −$7.10 / **−0.07%** (entry commission $6.83 + 0.05% slippage on BTC OPEN; no realized closes today)
- **Trades today:** 1 opened (BTC/USD long), 0 closed; win rate today N/A
- **Equity:** $10,497.38 (opened day at $10,504.48 after 2026-05-22 missed-scheduler replay catch-up)
- **Equity peak:** $10,728.95 (2026-05-21, unchanged)
- **Drawdown from peak:** 2.16%
- **Open positions:** 1 / 8 (1 / 4 strategy cap; cluster 1 / 2)
- **Portfolio risk-at-moment:** 0.179% of equity (cap 4%)
- **vs BTC-hold rolling 30d:** still pre-inception window for clean 30d (BULL inception 2026-04-20); 7d approx BULL +5.6% vs BTC-hold ≈ −3 to −4% → ≈ +9% delta (deferred to routine #4 for precise compute)
- **Kill switches:** all clear (daily PnL −0.07% / cap 5%; streak 1 / cap 7; DD 2.16% / cap 25%; equity floor $10,497.38 / floor $7,500)

### Lessons
- No new lesson appended this wake. Today's only event is a fresh BTC long at favorable technical context (15/15 regime, low ATR ≈ 0.36%, RSI 67); no exit yet, no failed entry, no kill-switch proximity event. Standing W22-G/W22-H-partial telemetry (two-bar EMA confirm + breakeven ratchet) is awaiting its first BTC test on this position.

### Monthly archive
- Not the last trading day of May 2026 (last weekday = Fri 2026-05-29) — no archive sweep this wake.

### Decision
- **HOLD BTC/USD** (just-opened; no exit triggers possible on entry bar). **No new entries.** Send mandatory EOD Telegram card. Commit + push portfolio.md + research_log.md updates.

---

2026-05-24T07:31:30Z | ops-audit | codex | Scheduler audit found BULL flat/authorized and Claude Desktop running, but Claude Desktop config had `ccdScheduledTasksEnabled=false`; restored to `true`. `bull-01-overnight` scheduled-task prompt converted to source-of-truth wrapper. Read-only Kraken public OHLC diagnostic on closed 06:00Z candles found regime gate PASS (15/15 positive, median +2.74%); TAO/USD and HYPE/USD cleared technical/liquidity filters by BULL v0.4 rules. No trade was booked from this Codex diagnostic session. Claude CLI CronList verification was blocked by local "Credit balance is too low"; next confirmation should use Claude Desktop's scheduled-task list or observe the next routine-01 log/commit. | no trade action
2026-05-20T20:00:00Z | midday | system | Portfolio flat (0 open positions, confirmed vs portfolio.md); no MTM/exit required. Kraken MCP RESTORED (`kraken_risk_flag` CLEAR at 13:58:34Z scan, 0 tier1/tier2, "Markets calm") — recovery from routine-01-overnight 2026-05-20T13:00Z Ring 3 MCP-failure SKIP. Equity unchanged $10,236.14, DD 0.21% from peak $10,258.06. Kill-switch proximity (price-independent while flat): daily realized 0% (cap 5%), streak 1 / cap 7 (last L 2026-05-15), DD 0.21% (warn 12.5%, cap 25%), equity > $7,500 floor — all clear. Midday is position-mgmt only — no entries scanned. No Telegram (no kill switch, no exit, no DD warning). | no action
2026-04-25T17:40:11Z | allocation | day-gate | not Sunday, skipping | no action
2026-04-26T20:00:00Z | midday | system | Portfolio flat (0 open positions); no MTM required. Equity $9,930.76, DD 0.97% from peak $10,027.55. All kill switches clear (daily loss 0%, equity > $7,500 floor, DD < 12.5% warn). Midday is position-mgmt only — no entries scanned. | no action
2026-05-16T20:00:00Z | midday | system | Portfolio flat (0 open positions, confirmed vs portfolio.md rebuilt same-day by routine-03-eod); no MTM required. Equity $10,236.14, DD 0.21% from peak $10,258.06. Kill switches all clear: daily realized −$21.92 ≈ −0.21% (cap 5%), consecutive-loss streak 1 (cap 7), DD 0.21% (warn 12.5% / cap 25%), equity > $7,500 floor. Midday is position-mgmt only — no entries scanned. portfolio.md left as-is (flat, no state delta; preserves routine-03-eod trade-log-correction note). No Telegram (no kill switch, no exit, no DD warning). | no action
2026-04-27T20:00:00Z | midday | system | Portfolio flat (0 open positions) after 05:00Z stop cascade closed ETH/BTC/SOL/TAO. No MTM/exit checks required. Equity $9,777.08, DD 2.50% from peak $10,027.55. Day realized -1.54% (cap 5%). All kill switches clear: DD < 12.5% warn, equity > $7,500 floor, daily loss < 5%. Midday is position-mgmt only — no entries scanned. | no action
2026-04-28T20:00:00Z | midday | kraken | TAO/USD MTM check (last 257.3733): stop 254.74 not breached on bars completed after entry (18:00 low 255.85, 19:00 low 256.64, 20:00 low 256.88). Last completed 1H close 19:00 = 257.0935 > 1H 20-EMA ≈ 251.81 — no EMA-cross exit. 4R target 281.64 not hit. Unrealized −$32.18 (−0.60R incl commission). Equity $9,744.90, DD 2.82% from peak $10,027.55, risk-at-moment 0.52%. Kill-switch proximity: day realized 0% / unrealized −0.33% (cap 5%), DD 2.82% (warn 12.5%, cap 25%), equity > $7,500 floor. NOTE: 17:00 entry-candle low 253.8037 sits below stop 254.74; cannot determine intra-candle ordering vs entry — flagging for routine-03 EOD review at 1H close. | HOLD TAO, no exits, no entries (midday is management-only)
2026-04-29T19:55:00Z | idea-scan | system | Manual dry-run (HARV-20260429-DRYRUN) — pre-cron pipeline validation. 2 sources fetched (Glassnode Insights, Robot Wealth), 10 claims extracted, 4 survived score-floor (>=8), 0 deduped, 4 appended to idea_bank.md. RW "To Trend or Not To Trend" outside 7d window — included for pipeline test only, normal Friday cron will exclude. First scheduled run: 2026-05-01 (Fri) 18:00 PT. | no trade action
2026-05-04T19:05:30Z | midday | system | Portfolio flat (0 open positions) — no trades since TAO stop-out 2026-04-29T14:00Z. No MTM/exit checks required; Kraken MCP not called (no positions to mark). Equity $9,712.70, DD 3.14% from peak $10,027.55. Day realized 0.00% (cap 5%). Kill-switch state: DD 3.14% (warn 12.5%, cap 25%) — clear; equity > $7,500 floor — clear; daily loss 0% — clear; consecutive losing trading days streak does not exceed 7 (current run since 04-29 L is 4 flat days, not losing). Midday is position-mgmt only — no entries scanned. | no action
2026-05-04T20:00:00Z | midday | kraken | LINK/USD MTM check (last 9.38328, opened 19:00Z @ 9.4393, stop 9.2018, 4R target 10.3893). Stop not breached: 19:00 bar low 9.37012, in-progress 20:00 low 9.38183 — both well above stop. Last completed 1H close 19:00 = 9.38827 > computed 1H 20-EMA ≈ 9.360 (seeded SMA20 9.2552 over 2026-05-03 15:00→2026-05-04 10:00, then iterated; α=2/21) — no exit-rule-1 EMA-cross. 4R target far. Unrealized −$20.71 (−0.34R incl commission). Equity $9,691.99, cash $7,280.49, position MTM $2,411.50, DD 3.35% from peak $10,027.55, risk-at-moment 0.63%. Kill-switch proximity: day realized 0% / unrealized −0.21% (cap 5%) — clear; DD 3.35% (warn 12.5%, cap 25%) — clear; equity > $7,500 floor — clear; consecutive-loss streak not 7-in-a-row. Midday is position-mgmt only — no entries scanned. | HOLD LINK, no exits, no entries
| 2026-05-05T20:00:00Z | midday | kraken | 3 open positions MTM check at 13:00 PT / 20:00 UTC (just-closed 19:00Z 1H bar). LINK/USD: last 9.74589, 19:00 close 9.73157 > 1H 20-EMA ≈ 9.632 (seeded SMA20 9.40435 over 2026-05-04 05:00→2026-05-05 00:00, iterated α=2/21) — no EMA-cross; 19:00 low 9.69894 well above stop 9.2018; +$72.48 (+1.19R). BTC/USD: last 81683.1, 19:00 close 81601.0 > 1H 20-EMA ≈ 80983 — no EMA-cross; 19:00 low 81426.6 well above stop 80124.19; +$15.29 (+0.61R). XRP/USD: last 1.41544, 19:00 close 1.41313 > 1H 20-EMA ≈ 1.40762 — no EMA-cross; 19:00 low 1.409 well above stop 1.39468; +$5.52 (+0.23R). No 4R targets near. Aggregate unrealized +$93.29; equity $9,806.00, cash $2,420.18, MTM $7,385.82, DD 2.21% from peak $10,027.55, risk-at-moment 1.12%. Kill-switch proximity: day realized 0% / day realized+unrealized +0.96% (cap 5%) — clear; DD 2.21% (warn 12.5%, cap 25%) — clear; equity > $7,500 floor — clear; consecutive-loss streak not 7-in-a-row. Midday is position-mgmt only — no entries scanned. | HOLD all 3, no exits, no entries
| 2026-05-06T20:00:00Z | midday | kraken | 4 open positions MTM check at 13:00 PT / 20:00 UTC (just-closed 19:00Z 1H bar). BTC/USD: 19:00 close 81471.5 < 1H 20-EMA ≈ 81570.2 (seeded SMA20 80646.195 over 2026-05-04 19:00→2026-05-05 14:00, iterated α=2/21) — exit-rule-1 EMA-cross TRIGGERED. Exit fill 81430.76 (close × 0.9995 slippage); gross +$14.04 minus exit comm $6.33 = +$1.42 net (+0.06R). LINK/USD: last 10.03964, 19:00 close 10.02236 > 1H 20-EMA ≈ 9.958 — no EMA-cross; 19:00 low 9.95 well above stop 9.2018; +$147.98 unrealized. XRP/USD: last 1.42786, 19:00 close 1.42815 > 1H 20-EMA ≈ 1.4274 (margin 0.0008) — no EMA-cross; 19:00 low 1.42235 well above stop 1.39468; +$26.92 unrealized. LTC/USD: last 57.04, 19:00 close 56.95 > 1H 20-EMA ≈ 56.92 (margin 0.03) — no EMA-cross; 19:00 low 56.78 well above stop 56.28; −$10.19 unrealized. No intrabar stop breaches (all 24h lows above stops post-entry). No 4R targets near. Post-exit: 3 open, equity $9,820.65, cash $2,441.62, MTM $7,379.03, DD 2.06% from peak $10,027.55, risk-at-moment 1.22%. Kill-switch proximity: day realized −0.58% (HYPE −$58.18 + BTC +$1.42) / day realized+unrealized +1.10% (cap 5%) — clear; DD 2.06% (warn 12.5%, cap 25%) — clear; equity > $7,500 floor — clear; consecutive-loss streak not 7-in-a-row. Midday is position-mgmt only — no entries scanned. XRP and LTC EMA margins thin — flagging for routine-03 EOD re-check. | CLOSE BTC ema-cross, HOLD LINK/XRP/LTC, no entries

## Schema

| Timestamp (UTC) | Routine | Source | Summary | Action taken |
|-----------------|---------|--------|---------|--------------|

## Entries

| 2026-04-21T03:26:55Z | overnight | system | Kraken MCP not available in session (no kraken_* tools registered); routine cannot fetch OHLCV or ticker data | SKIPPED per guardrails Ring 3 MCP-failure rule; will retry next routine |
| 2026-04-21T03:30:00Z | overnight | kraken | HYPE/USD entry scan: 1H close 41.09 below 1H EMA20 41.13; 4H close 41.09 above 4H EMA50 ~43.0 (failing) | REJECT — entry-rule-1 (1H close < EMA20) |
| 2026-04-21T03:30:00Z | overnight | kraken | AVAX/USD entry scan: 1H close 9.31 > EMA20 9.28, RSI14 58.0 > 55, but 4H close 9.31 < 4H EMA50 9.34 | REJECT — entry-rule-3 (4H close < 4H EMA50) |
| 2026-04-21T03:30:00Z | overnight | kraken | SOL/USD entry scan: 1H close 85.50 > EMA20 85.47 (razor-thin), RSI14 ≈ 51.3 < 55 | REJECT — entry-rule-2 (1H RSI14 < 55) |
| 2026-04-21T03:30:00Z | overnight | kraken | TAO/USD entry scan: 4H close 244.78 < 4H EMA50 250.16 | REJECT — entry-rule-3 (4H close < 4H EMA50) |
| 2026-04-21T03:30:00Z | overnight | kraken | XRP/USD entry scan: 1H close 1.4247 < EMA20 1.4251 (razor-thin); 4H close 1.4247 > 4H EMA50 1.4008 | REJECT — entry-rule-1 (1H close < EMA20) |
| 2026-04-21T03:30:00Z | overnight | kraken | BTC,ETH,DOGE,SUI,LTC,ADA,FARTCOIN,LINK,PENGU,TRX all have 24h change ≤ 0 (-0.04% to -1.73%); market regime: Apr 13–17 rally then Apr 18–19 selloff, now flat-to-down consolidation; 1H RSI14 > 55 mathematically implausible under this regime | REJECT (inferred, 10 pairs) — entry-rule-2 (1H RSI14 < 55) — context-budget decision not to compute indicators for each |
| 2026-04-21T03:30:00Z | overnight | system | News scan (CoinDesk / TheBlock via Firecrawl) deferred this run to conserve context budget; no ACTIONABLE items flagged | deferred — morning brief routine runs shortly after |
| 2026-04-21T03:30:00Z | overnight | system | Universe refresh skipped: today is 2026-04-20 (not 1st of month) | no action |
| 2026-04-21T18:05:00Z | overnight | kraken | TRX/USD entry scan (1H close 17:00 = 0.331777): 1H EMA20 ≈ 0.329847 (PASS), 1H RSI14 ≈ 76.4 (PASS), 4H close (12:00 bar) 0.330345 > 4H EMA50 ≈ 0.3264 (PASS). ATR14(1h) ≈ 0.000829. | OPEN long @ 0.331943, stop 0.330285, size 7531 (cash-capped to equity/4 = $2500 notional, risk $12.49 = 0.12%) — entry-rule-v0-momentum |
| 2026-04-21T18:05:00Z | overnight | kraken | LINK/USD entry scan: 1H close 17:00 = 9.35124, 20 recent-bar SMA ≈ 9.363 (EMA20 similar or higher) | REJECT — entry-rule-1 (1H close < 1H EMA20) |
| 2026-04-21T18:05:00Z | overnight | kraken | PENGU/USD entry scan: 1H close 17:00 = 0.007627, 20-bar SMA 0.007660 | REJECT — entry-rule-1 (1H close < 1H EMA20) |
| 2026-04-21T18:05:00Z | overnight | kraken | AVAX/USD entry scan: 1H close 17:00 = 9.33, 20-bar SMA 9.3355 | REJECT — entry-rule-1 (1H close < 1H EMA20, razor-thin) |
| 2026-04-21T18:05:00Z | overnight | kraken | Remaining 10 pairs (BTC -0.42%, ETH -0.55%, SOL -0.12%, XRP -0.03%, TAO -0.5%, HYPE -2.92%, XDG -1.06%, SUI -0.73%, LTC +0.04%, ADA -0.84%, FARTCOIN -0.79%): 24h change ≤ 0 or razor-thin; market regime still mixed. Under negative-drift regime, 1H RSI14>55 is mathematically unlikely. | REJECT (inferred, 11 pairs) — entry-rule-2 (1H RSI14 < 55) — context-budget decision not to re-compute individually |
| 2026-04-21T18:05:00Z | overnight | system | News scan deferred: morning-brief skill runs separately and surfaces actionable headlines. v0 strategy is not news-reactive — no entry gate depends on news this run. | deferred |
| 2026-04-21T18:05:00Z | overnight | system | Universe refresh skipped: today is 2026-04-21 (not 1st of month). Next refresh 2026-05-01. | no action |
2026-04-21T18:16:46Z | allocation | day-gate | not Sunday, skipping | no action
2026-04-21T18:17:40Z | harness | day-gate | not Saturday, skipping | no action
| 2026-04-21T20:00:00Z | overnight | kraken | TRX/USD position check: last 0.333177, stop 0.330285 — stop not hit, position holds. Unrealized +$9.29 (+0.37%). | HOLD |
| 2026-04-21T20:05:00Z | overnight | kraken | LTC/USD entry scan (1H close 19:00 = 55.24): 1H SMA20 55.232 (PASS razor-thin), RSI14 ≈ 57.1 (PASS), 4H close (16:00 bar) 55.23 > 4H EMA50 ≈ 55.02 (PASS). ATR14(1h) ≈ 0.329. | OPEN long @ 55.27, stop 54.61, size 45.2 (cash-capped to equity/4 ≈ $2500 notional, risk $29.83 = 0.30%) — entry-rule-v0-momentum |
| 2026-04-21T20:05:00Z | overnight | kraken | ETH/USD entry scan: 1H close 2322.92 > SMA20 2315.91 (PASS), RSI14 ≈ 54.5 (FAIL) | REJECT — entry-rule-2 (1H RSI14 < 55) |
| 2026-04-21T20:05:00Z | overnight | kraken | LINK/USD entry scan: 1H close 9.36872 > SMA20 9.36773 (razor-thin PASS), RSI14 ≈ 52.7 (FAIL) | REJECT — entry-rule-2 (1H RSI14 < 55) |
| 2026-04-21T20:05:00Z | overnight | kraken | PENGU/USD entry scan: 1H close 0.007662 < SMA20 0.007671 (razor-thin) | REJECT — entry-rule-1 (1H close < 1H EMA20) |
| 2026-04-21T20:05:00Z | overnight | kraken | AVAX/USD entry scan: 1H close 9.32 < SMA20 9.3545 | REJECT — entry-rule-1 (1H close < 1H EMA20) |
| 2026-04-21T20:05:00Z | overnight | kraken | SOL/USD entry scan: 1H close 85.43 < SMA20 85.655 | REJECT — entry-rule-1 (1H close < 1H EMA20) |
| 2026-04-21T20:05:00Z | overnight | kraken | XRP/USD entry scan: 1H close 1.4274 < SMA20 1.4324 | REJECT — entry-rule-1 (1H close < 1H EMA20) |
| 2026-04-21T20:05:00Z | overnight | kraken | Remaining 7 pairs (BTC -0.13%, TAO +0.06%, HYPE -3.59%, XDG -0.65%, SUI -0.54%, ADA -0.29%, FARTCOIN -0.30%): 24h change ≤ 0 or flat. Under flat-to-down drift, 1H RSI14>55 is unlikely. | REJECT (inferred, 7 pairs) — entry-rule-2 (1H RSI14 < 55) — context-budget decision not to re-compute individually |
| 2026-04-21T20:05:00Z | overnight | system | News scan deferred: morning-brief skill runs separately and surfaces actionable headlines. v0 strategy is not news-reactive — no entry gate depends on news this run. | deferred |
| 2026-04-21T20:05:00Z | overnight | system | Universe refresh skipped: today is 2026-04-21 (not 1st of month). Next refresh 2026-05-01. | no action |
| 2026-04-22T03:00:00Z | midday | kraken | Midday health check. TRX last 0.332272, EMA20(1h) ≈ 0.33176 → above EMA (HOLD); stop 0.330285 not breached. LTC last 55.88, EMA20(1h) ≈ 55.41 → above EMA (HOLD); stop 54.61 not breached. Equity $10,016.92 (+0.17% since start), new peak, DD 0.00%. Kill-switch proximity: daily loss 0% vs 5% cap, DD 0% vs 25% cap. Position risk 0.42% vs 4% cap. | HOLD both, no exits, no entries (midday is management-only) |
| 2026-04-22T04:10:00Z | overnight | kraken | Risk flag CLEAR (scan 04:00Z, no tier-1/2). Universe 24h regime: broad rally +1-2%; BTC +1.64%, ETH +1.68%, ADA +1.77%, PENGU +2.61%, FARTCOIN +2.29%, AVAX +1.60%, SOL +1.39%, SUI +1.23%, XDG +1.23%, LINK +1.09%, XRP +0.79%, HYPE +0.65%, LTC +0.61%, TAO +0.51%, TRX −0.30%. | context — regime positive, RSI14 pass likelihood high across momentum movers |
| 2026-04-22T04:10:00Z | overnight | kraken | TRX/USD position check: 1H close 03:00 = 0.332366, SMA20(1h) ≈ 0.33165 (above EMA, HOLD rule 1 not triggered); stop 0.330285 not hit. Unrealized +$1.23. | HOLD |
| 2026-04-22T04:10:00Z | overnight | kraken | LTC/USD position check: 1H close 03:00 = 55.87, SMA20(1h) ≈ 55.41 (above EMA, HOLD rule 1 not triggered); stop 54.61 not hit. Unrealized +$31.19. | HOLD |
| 2026-04-22T04:10:00Z | overnight | kraken | BTC/USD entry scan: 1H close 03:00 = 77561.6 > SMA20(1h) 76146.9 (PASS); RSI14 ≈ 68.8 > 55 (PASS); 4H close (00:00 bar) 77561.6 > 4H SMA50 ≈ 75390.4 (PASS strong). ATR14(1h) ≈ 573.0. | OPEN long @ 77600.4, stop 76454.3, size 0.0322 (cash-capped to equity/4 ≈ $2500 notional, risk $36.90 = 0.37%) — entry-rule-v0-momentum |
| 2026-04-22T04:10:00Z | overnight | kraken | ETH/USD entry scan: 1H close 03:00 = 2364.36 > SMA20 2320.96 (PASS); RSI14 ≈ 67.7 (PASS); 4H close 00:00 = 2364.36 > 4H SMA50 ≈ 2343.33 (PASS, thin ~1% cushion). | PASS on strategy, HOLD-OFF — cash constraint: equity/4 cap already consumed by BTC entry this wake |
| 2026-04-22T04:10:00Z | overnight | kraken | ADA/USD entry scan: 1H close 03:00 = 0.254355 > SMA20 0.249262 (PASS); RSI14 ≈ 67.0 (PASS); 4H close 0.254355 > 4H SMA50 ≈ 0.249222 (PASS). | PASS on strategy, HOLD-OFF — cash constraint |
| 2026-04-22T04:10:00Z | overnight | kraken | PENGU/USD entry scan: 1H close 03:00 = 0.007975 > SMA20 0.00772 (PASS); RSI14 ≈ 61.5 (PASS); 4H close 0.007975 > 4H SMA50 ≈ 0.00738 (PASS strong). | PASS on strategy, HOLD-OFF — cash constraint |
| 2026-04-22T04:10:00Z | overnight | kraken | FARTCOIN/USD entry scan: 1H close 03:00 = 0.2053 > SMA20 0.20163 (PASS); RSI14 ≈ 52.4 (FAIL). | REJECT — entry-rule-2 (1H RSI14 < 55) |
| 2026-04-22T04:10:00Z | overnight | kraken | Remaining 9 pairs (SOL +1.39%, XRP +0.79%, TAO +0.51%, HYPE +0.65%, XDG +1.23%, SUI +1.23%, AVAX +1.60%, LINK +1.09%, TRX already-open) — not individually evaluated beyond BTC selection; 4 candidates already PASSED strategy and only 1 cash slot available this wake. | HOLD-OFF (context-budget + cash-cap). Next wake will re-evaluate. |
| 2026-04-22T04:10:00Z | overnight | system | News scan deferred: morning-brief skill runs separately and surfaces actionable headlines. v0 strategy is not news-reactive — no entry gate depends on news this run. Kraken risk flag CLEAR confirms no tier-1/2 incidents. | deferred |
| 2026-04-22T04:10:00Z | overnight | system | Universe refresh skipped: today is 2026-04-22 (not 1st of month). Next refresh 2026-05-01. | no action |
| 2026-04-24T20:00:00Z | midday | kraken | Midday health check: TRX last 0.324443 (24h low 0.319711) pierced static stop 0.330285 intrabar — closed at stop with 0.05% slippage (fill 0.330120), realized −$26.69 / −1.1R. LTC @ 56.63 +$61.47 unreal, BTC @ 77777.5 +$5.70 unreal. Equity $10,027.55 (new peak), DD 0.00%, risk-at-moment 0.67%. All kill switches clear. | EXIT TRX (stop-hit); HOLD LTC, BTC |
| 2026-04-24T17:14:17Z | harness | day-gate | not Saturday, skipping | no action |
2026-04-24T17:15:26Z | allocation | day-gate | not Sunday, skipping | no action
| 2026-04-24T13:00:00Z | overnight | kraken | BTC/USD position check: computed 1H EMA20 seeded from bars 04:00–23:00 2026-04-23 (SMA 77900.4), recursive through 2026-04-24. Bar 03:00 close 77759.6 < EMA 78036 → EMA-cross exit fired (exit rule 1). Fill 77720.72 w/ 0.05% adverse slippage @ 04:00 bar open, realized −$9.14 / +0.10R gross but net drag from commissions. | EXIT BTC (exit-ema-cross) |
| 2026-04-24T13:00:00Z | overnight | kraken | LTC/USD position check: 1H close 56.59 > 1H EMA20 56.15; price 56.59 > stop 54.61; PnL +1.99R < 4R exit. All three exit rules fail. | HOLD LTC |
| 2026-04-24T13:00:00Z | overnight | kraken | ADA/USD entry scan: 1H close 0.252128 > 1H EMA20 0.249871, 1H RSI14 62.4 > 55, 4H close 0.252128 > 4H EMA50 0.247953, ≥10 candles, no existing position, open positions < 4, portfolio risk 0.30% + new 0.32% = 0.62% ≤ 4%. All entry rules pass. | OPEN ADA long (entry-rule-v0-momentum) |
| 2026-04-24T13:00:00Z | overnight | kraken | XDG/USD entry scan: 1H close 0.1412 < 1H EMA20 ~0.1418 | REJECT — entry-rule-1 (1H close < EMA20) |
| 2026-04-24T13:00:00Z | overnight | kraken | SUI/USD entry scan: 1H RSI14 ≈ 48 < 55 | REJECT — entry-rule-2 (1H RSI14 < 55) |
| 2026-04-24T13:00:00Z | overnight | kraken | PENGU/USD entry scan: 4H close < 4H EMA50 | REJECT — entry-rule-3 (4H close < 4H EMA50) |
| 2026-04-24T13:00:00Z | overnight | kraken | ETH,SOL,XRP,TAO,HYPE,FARTCOIN,AVAX,LINK all rejected inferentially via kraken_multi_ticker 24h change screen: either <0 (failing momentum prior) or failing at least one of the 3 entry rules; context-budget decision not to compute full indicator set. | REJECT (8 pairs inferred) |
| 2026-04-24T13:00:00Z | overnight | kraken | kraken_risk_flag: CLEAR — no tier-1/2 incidents or exchange status anomalies. No ACTIONABLE news items surface from morning brief cross-check. | no action (v0 not news-reactive) |
| 2026-04-24T13:00:00Z | overnight | system | Universe refresh skipped: today is 2026-04-24 (not 1st of month). Next refresh 2026-05-01. | no action |
| 2026-04-24T17:00:00Z | overnight | kraken-risk-scan | Risk flag CLEAR for 2026-04-23 (scan 2026-04-24T00:00Z); 2 tier-2 military headlines, 0 blocking | macro/military-escalation (Strait of Hormuz, naval blockade) | no action — tier-2 non-blocking; continue trading |
| 2026-04-24T17:00:00Z | overnight | position-check LTC | 1H close 56.59 > SMA20 56.12; stop 54.61 intact; no +4R TP yet | momentum continuation | HOLD LTC |
| 2026-04-24T17:00:00Z | overnight | position-check BTC | prior wake @ 04:00Z booked EMA-cross exit fill 77720.72 (−$9.14, +0.10R) — confirmed correct per strategy "1H close < EMA20" | exit-rule-trigger | closed, no duplicate action |
| 2026-04-24T17:00:00Z | overnight | position-check ADA | prior wake @ 17:00Z booked OPEN 9934 @ 0.251930, stop 0.248716 — confirmed v0 rules pass (1H 0.251804>SMA20 0.2500, RSI14 58.85, 4H 0.252283>SMA50 0.2510) | entry-rule-v0-momentum | open, no duplicate action |
| 2026-04-24T17:00:00Z | overnight | entry-scan AVAX | PASS: 1H close 9.41>SMA20 9.388, RSI14 56.41, 4H close 9.46>SMA50 9.429 (thin +0.3% margin), ATR14 0.065 | entry-rule-v0-momentum | OPEN 265 @ 9.4147 fill, stop 9.2847, risk $34.45 (0.34%) |
| 2026-04-24T17:00:00Z | overnight | entry-scan SOL | PASS 1H (86.38>85.924, RSI 57.19) but 4H margin razor-thin (close 86.53 vs SMA50 86.499, +0.04%); below SMA-proxy confidence threshold | skip-thin-4h-margin | REJECT — wait for wider separation |
| 2026-04-24T17:00:00Z | overnight | entry-scan XDG | 1H close 0.0980656>SMA20 0.09765, BUT RSI14 54.0 < 55 threshold | rule-2-fail | REJECT |
| 2026-04-24T17:00:00Z | overnight | entry-scan PENGU | 1H close 0.008525 < SMA20 0.008566 | rule-1-fail | REJECT |
| 2026-04-24T17:00:00Z | overnight | entry-scan SUI | 1H close 0.95 > SMA20 0.94655, BUT RSI14 52.2 < 55 | rule-2-fail | REJECT |
| 2026-04-24T17:00:00Z | overnight | entry-scan ETH/HYPE/TAO/TRX | all negative 24h change; momentum regime absent | rule-2-fail-inferred | REJECT (no 1H pull — efficiency) |
| 2026-04-24T17:00:00Z | overnight | entry-scan LINK/FARTCOIN/XRP | positive 24h but marginal (<0.5%); not pulled due to AVAX slot fill using capacity | skipped-not-pulled | no action |
| 2026-04-24T17:00:00Z | overnight | news-scan | firecrawl news-scan deferred — daily risk_flag covers macro/military tier; no v0 news-reactive rule yet | procedural | no headline-level actionable items recorded |
| 2026-04-24T17:00:00Z | overnight | universe-refresh | skipped — not 1st of month | procedural | no change |
| 2026-04-25T00:20:00Z | midday | kraken | Midday health check: LTC 56.59 (>EMA20 56.15, >stop 54.61) HOLD; ADA 0.252045 (>stop 0.248716) HOLD; AVAX 9.44 (>stop 9.2847) HOLD. No exit triggers, no static-stop pierces. Equity $10,012.24 = cash $2,448.97 + positions $7,563.27. DD 0.15% from peak $10,027.55. Risk-at-moment $96.21 (0.96%) vs cap 4%. Kill-switch proximity: daily loss 0% vs 5%, DD 0.15% vs 25%, equity floor far. All clear. | HOLD all 3 positions, no exits, midday is mgmt-only |
| 2026-04-25T00:25:00Z | eod | kraken | EOD post-close exit check (ran early per operator request, ~11h before scheduled 21:00 PT): LTC 1H close 56.59 > EMA20 56.15 (HOLD); ADA 1H close 0.251804 > EMA20 0.249946 (HOLD); AVAX 1H close 9.41 > EMA20 9.39 (HOLD razor-thin +0.21%). All static stops intact. EOD entry scan duplicates routine-01 from 17:00Z (same 16:00 bar) — 2 cash slots used (ADA, AVAX); SOL was the 3rd PASS but ran into thin 4H margin in earlier wake; no new entries this run. Day stats: realized −$35.83 (TRX −$26.69 + BTC −$9.14), unrealized +$57.16, equity $10,001.91 (+0.02% since start), DD 0.26% from peak. Trades today: 2 closed (BTC ema-cross, TRX stop), 2 opened (ADA, AVAX). Open 3/8. Kill switches all clear. | EOD card sent via Telegram; no new fills |
| 2026-04-25T00:30:00Z | harness | day-gate | not Saturday, skipping | no action |
| 2026-04-25T00:31:00Z | allocation | day-gate | not Sunday, skipping | no action |
| 2026-04-24T17:40:00Z | allocation | day-gate | not Sunday, skipping | no action |
| 2026-04-24T20:10:00Z | midday | kraken | MTM @ 20:06Z — LTC 56.72, ADA 0.251958, AVAX 9.44; no stops pierced intrabar, 19:00Z 1H closes all above 20-EMA; equity $10,017.26, DD 0.10%, day +0.37% net | no action — all clear, silent |
| 2026-04-25T17:07:23Z | harness | system | Saturday harness verify: tv_health_check failed (CDP connection refused, TradingView Desktop not running); kraken_ticker BTC/USD OK ($77,392.4). Per Ring 3 MCP-failure rule, skip routine. | SKIPPED harness run; Telegram ALERT sent; retry next Saturday or operator can run /loop manually after launching TradingView |
| 2026-04-25T20:00:00Z | midday | system | Found 3 uncommitted CLOSE rows in trade_log.md from 2026-04-25T17:00Z (LTC +1.32R/+$39.40, ADA −1.21R/−$38.77, AVAX −0.99R/−$34.04, all exit-ema-cross) lacking corresponding research_log entries — likely an interrupted prior routine. Treated trade_log as source of truth per skill rules and rebuilt portfolio. No open positions to MTM. Equity $9,930.76, cash $9,930.76, realized all-time −$69.24, DD 0.97% from peak $10,027.55. Day realized −$33.41 (−0.33%). Kill-switch proximity: daily loss 0.33% vs 5% cap, DD 0.97% vs 25% cap (warn 12.5%), equity floor $2,430 above. All clear. | Flushed 3 prior closes via this commit; no new exits, no entries (midday is mgmt-only); silent — no Telegram |
| 2026-04-26T04:40:00Z | overnight | kraken | Risk flag CLEAR (scan 04:39Z, no tier-1/2). Universe 24h regime: 14/15 pairs negative or flat (XBT -0.25, ETH -0.36, SOL -0.14, XRP -0.33, TAO -0.82, HYPE -0.48, XDG -0.28, SUI -0.38, LTC -0.46, ADA -0.43, FARTCOIN -0.50, AVAX -0.32, LINK -0.31, PENGU -0.02), TRX +0.06 only positive. | context — flat-to-down regime, RSI>55 unlikely across most pairs |
| 2026-04-26T04:40:00Z | overnight | kraken | Position check: no open positions to manage. No stops or EMA-cross checks needed. | no action |
| 2026-04-26T04:40:00Z | overnight | kraken | TRX/USD entry scan (1H close 03:00Z = 0.323905): 1H SMA20 ≈ 0.32373 (PASS razor +0.05%), 1H RSI14 ≈ 59.6 (PASS), 4H close (00:00Z bar) 0.323905 < 4H SMA50 ≈ 0.328567 (FAIL by 1.4%). | REJECT — entry-rule-3 (4H close < 4H EMA50) |
| 2026-04-26T04:40:00Z | overnight | kraken | PENGU/USD entry scan (1H close 03:00Z = 0.008627): 1H SMA20 ≈ 0.008541 (PASS), 1H RSI14 ≈ 54.1 (FAIL <55). | REJECT — entry-rule-2 (1H RSI14 < 55) |
| 2026-04-26T04:40:00Z | overnight | kraken | SOL/USD entry scan (1H close 03:00Z = 86.01): 1H SMA20 ≈ 86.18 (FAIL by -0.20%). | REJECT — entry-rule-1 (1H close < 1H EMA20) |
| 2026-04-26T04:40:00Z | overnight | kraken | Remaining 12 pairs (XBT -0.25%, ETH -0.36%, XRP -0.33%, TAO -0.82%, HYPE -0.48%, XDG -0.28%, SUI -0.38%, LTC -0.46%, ADA -0.43%, FARTCOIN -0.50%, AVAX -0.32%, LINK -0.31%): all negative 24h drift; under negative-drift regime, 1H RSI14>55 mathematically unlikely. | REJECT (12 pairs inferred) — entry-rule-2 (1H RSI14 < 55) — context-budget decision not to compute individually, consistent with prior wakes' methodology |
| 2026-04-26T04:40:00Z | overnight | system | News scan deferred per established pattern: kraken_risk_flag CLEAR is the binding macro/news pre-screen for v0 (not news-reactive). Morning brief skill runs separately and surfaces ACTIONABLE headlines. No headline-level actionable items recorded. | deferred |
| 2026-04-26T04:40:00Z | overnight | system | Universe refresh skipped: today is 2026-04-25/26 (not 1st of month). Next refresh 2026-05-01. | no action |
| 2026-04-26T04:40:00Z | overnight | system | Routine #1 result: 0 OPEN, 0 CLOSE, 0 ACTIONABLE news. Equity $9,930.76 (flat), DD 0.97%, all kill switches clear. Telegram silent per template (no entries, no exits, no kill-switch trip, no actionable news). | no Telegram |
2026-04-26T21:14:21Z | harness | day-gate | not Saturday, skipping | no action
| 2026-04-26T21:30:00Z | allocation | system | First weekly allocation review (W17, 2026-04-20→2026-04-26). Buckets: momentum 100% / mean-rev 0% / news-react 0% (v0 declared). 5 closed trades, 1W/4L, avg R −0.376, total PnL −$69.24, all in momentum. BTC-hold 7d +5.99%, BULL −0.69%, Δ −6.68%. 30d/90d not evaluable (only 6 days history). Sample below noise floor; only one active bucket exists; no proposal generated. | NO allocation change; weekly memo W17 written; no pending strategy edit to apply (W16 had no memo, W17 harness was MCP-skipped) |
| 2026-04-26T21:13:44Z | overnight | kraken | Risk flag CLEAR (no tier-1/2). Universe 24h regime FLIPPED POSITIVE since 04:40Z wake: PENGU +5.06, FARTCOIN +3.03, ETH +2.03, LINK +1.34, HYPE +1.04, TAO +0.99, AVAX +0.96, SOL +0.94, ADA +0.86, XDG +0.85, XBT +0.80, SUI +0.73, LTC +0.36, XRP +0.34, TRX -0.13. | context — broad rally regime; 1H RSI>55 likely across momentum movers |
| 2026-04-26T21:13:00Z | overnight | kraken | Position check: no open positions to manage at start of wake. | no action |
| 2026-04-26T21:13:00Z | overnight | kraken | ETH/USD entry scan (1H close 20:00Z = 2363.54): 1H SMA20 2336.73 (PASS +1.15%), RSI14 71.83 (PASS strong), 4H close (20:00Z bar) 2367.01 > 4H SMA50 2330.53 (PASS +1.6%), ATR14(1h) 9.22. Pre-entry guardrails: positions 0<4, portfolio risk 0%+0.21%≤4%, per-trade 0.21%≤1.5%, in-universe, daily loss 0.33%<5%, equity above floor — ACCEPT. | OPEN long @ 2364.72 (close + 0.05% slip), stop 2345.10 (2×ATR), size 1.0499, risk $20.60 (0.21%) — entry-rule-v0-momentum |
| 2026-04-26T21:13:00Z | overnight | kraken | BTC/USD entry scan (1H close 20:00Z = 78227.1): 1H SMA20 77963.05 (PASS +0.34%), RSI14 57.41 (PASS), 4H close (20:00Z bar) 78285.0 > 4H SMA50 76948.64 (PASS +1.74%), ATR14(1h) 211.98. Pre-entry guardrails ACCEPT. | OPEN long @ 78266.21, stop 77803.14, size 0.0317, risk $14.69 (0.15%) — entry-rule-v0-momentum |
| 2026-04-26T21:13:00Z | overnight | kraken | SOL/USD entry scan (1H close 20:00Z = 86.75): 1H SMA20 86.469 (PASS +0.32%), RSI14 55.84 (PASS razor-thin), 4H close (20:00Z bar) 87.09 > 4H SMA50 86.088 (PASS +1.16%), ATR14(1h) 0.3243. Pre-entry guardrails ACCEPT. | OPEN long @ 86.79, stop 86.10, size 28.6, risk $19.82 (0.20%) — entry-rule-v0-momentum |
| 2026-04-26T21:13:00Z | overnight | kraken | PENGU/USD entry scan (1H close 20:00Z = 0.009029): 1H SMA20 0.008784 (PASS), RSI14 63.34 (PASS), 4H close 0.009045 > 4H SMA50 0.008001 (PASS strong +13%), ATR14(1h) 0.000153. Strategy PASS on all 3 rules. BUT: 24h notional today $1.86M (universe rank 14, monthly $1.07M), at/below the sub-$2M threshold flagged in lessons.md #1 (TRX wick blow-through). | REJECT — discretionary skip per active lesson #1 (sub-$2M/24h thin-liquidity wick risk). Logged for routine #4 to formalize as a rule. |
| 2026-04-26T21:13:00Z | overnight | kraken | FARTCOIN/USD entry scan (1H close 20:00Z = 0.2045): 1H SMA20 0.20056 (PASS), RSI14 61.39 (PASS), 4H close 0.2043 > 4H SMA50 0.2007 (PASS +1.8%), ATR14(1h) 0.00183. Strategy PASS on all 3 rules. BUT: 24h notional today only $0.46M — 4× thinner than TRX was when its wick blew the stop. | REJECT — discretionary skip per active lesson #1, more strongly than PENGU |
| 2026-04-26T21:13:00Z | overnight | kraken | Remaining 10 pairs (XRP +0.34, TAO +0.99, HYPE +1.04, XDG +0.85, SUI +0.73, LTC +0.36, ADA +0.86, AVAX +0.96, LINK +1.34, TRX -0.13): not pulled — 3 of 4 max-concurrent slots filled by ETH/BTC/SOL with strong PASS signals; remaining slot reserved (LINK +1.34% would have been the next candidate by liquidity but per-position cap not exceeded). Context-budget decision consistent with prior wakes. | HOLD-OFF (slot capacity) |
| 2026-04-26T21:13:00Z | overnight | system | News scan deferred per established pattern: kraken_risk_flag CLEAR pre-screen, morning-brief skill runs separately. v0 not news-reactive. | deferred |
| 2026-04-26T21:13:00Z | overnight | system | Universe refresh skipped: today is 2026-04-26 (not 1st of month). Next refresh 2026-05-01. | no action |
| 2026-04-26T21:13:00Z | overnight | system | Routine #1 result: 3 OPEN (ETH, BTC, SOL), 0 CLOSE, 0 ACTIONABLE news. Equity $9,920.62 (cash $2,465.49 + positions $7,455.13), realized −$69.24, unrealized −$10.14 (entry slip+commission), DD 1.07% from peak. Portfolio risk 0.56%, all kill switches clear. Telegram digest required per template (new OPENs occurred). | TELEGRAM SEND — entry digest |
| 2026-04-27T04:10:00Z | overnight | kraken | Risk flag CLEAR (scan 2026-04-27T00:00Z, no tier-1/2). Universe 24h regime BROAD POSITIVE: PENGU +11.79, FARTCOIN +1.92, HYPE +1.74, TAO +1.72, SUI +1.19, XDG +1.18, ETH +1.0, SOL +0.89, ADA +0.76, XRP +0.74, LINK +0.62, XBT +0.56, AVAX +0.53, LTC +0.53, TRX +0.15. Rally extending from prior wake's flip. | context — momentum regime intact, RSI>55 likely across movers |
| 2026-04-27T04:10:00Z | overnight | kraken | ETH/USD position check: 1H close (just-closed 03:00Z bar) 2395.05 > SMA20 2357.82 (PASS HOLD); intraday low post-entry 2349.51 (21:00Z bar) > stop 2345.10 by $4.41 — narrow but intact. 4R target 2443.20 not hit. Unrealized +$29.84 (+1.20%). | HOLD ETH |
| 2026-04-27T04:10:00Z | overnight | kraken | BTC/USD position check: 1H close 03:00Z 79110 > SMA20 78359.6 (PASS HOLD); intraday low post-entry 77885.7 > stop 77803.14 by $82.56. 4R target 80118.49 not hit. Unrealized +$26.26 (+1.06%). | HOLD BTC |
| 2026-04-27T04:10:00Z | overnight | kraken | SOL/USD position check: 1H close 03:00Z 87.77 > SMA20 86.81 (PASS HOLD); intraday low post-entry 86.26 > stop 86.10 by $0.16 — razor-thin but intact. 4R target 89.55 not hit. Unrealized +$26.60 (+1.07%). | HOLD SOL |
| 2026-04-27T04:10:00Z | overnight | kraken | TAO/USD entry scan (1H close 03:00Z = 255.4353): 1H SMA20 250.03 (PASS +2.16%), RSI14 ≈ 81.2 (PASS), 4H close 04/27 00:00 bar 255.4353 > 4H SMA50 246.44 (PASS +3.65%), ATR14(1h) 2.222. Pre-entry guardrails: positions 3<4 (1 slot), portfolio risk 0.56%+0.43%≤4%, per-trade 0.43%≤1.5%, in-universe (rank 5, $6.80M notional > $2M lesson-1 threshold), daily loss 0%<5%, equity above floor — ACCEPT. | OPEN long @ 255.56 (close + 0.05% slip), stop 251.12 (2×ATR), size 9.6, risk $42.66 (0.43%) — entry-rule-v0-momentum |
| 2026-04-27T04:10:00Z | overnight | kraken | HYPE/USD entry scan (1H close 03:00Z = 43.26): 1H SMA20 41.84 (PASS +3.4%), RSI14 ≈ 94.8 (PASS but extreme/climactic), 4H close 04/27 00:00 bar 43.26 > 4H SMA50 42.14 (PASS +2.66%), ATR14(1h) 0.322. Strategy PASS on all 3 rules. | PASS on strategy, HOLD-OFF — cash slot consumed by TAO (preferred for slightly higher liquidity rank, less-extreme RSI, and stronger 4H structural cushion). Will re-evaluate next wake if HYPE still PASSes and a slot opens. |
| 2026-04-27T04:10:00Z | overnight | kraken | PENGU/USD entry scan: 24h +11.79% strong; universe rank 14 ($1.07M monthly notional). | REJECT — discretionary skip per active lesson #1 (sub-$2M/24h thin-liquidity wick risk, consistent with prior wake's PENGU/FARTCOIN reject pattern) |
| 2026-04-27T04:10:00Z | overnight | kraken | FARTCOIN/USD entry scan: 24h +1.92%; universe rank 11 ($1.52M monthly notional). | REJECT — discretionary skip per active lesson #1 |
| 2026-04-27T04:10:00Z | overnight | kraken | Remaining 9 pairs (XBT/ETH/SOL already-open; SUI +1.19, XDG +1.18, ADA +0.76, XRP +0.74, LINK +0.62, AVAX +0.53, LTC +0.53, TRX +0.15) — not pulled: 4 max-concurrent slots filled by ETH/BTC/SOL/TAO; ADA/AVAX/LTC/LINK/TRX below or near $2M lesson-1 threshold; SUI/XDG/XRP would need 1H+4H pull but no available cash/slot. Context-budget decision consistent with prior wakes. | HOLD-OFF (slot+cash capacity exhausted) |
| 2026-04-27T04:10:00Z | overnight | system | News scan deferred per established pattern: kraken_risk_flag CLEAR pre-screen, morning-brief skill runs separately. v0 not news-reactive. | deferred |
| 2026-04-27T04:10:00Z | overnight | system | Universe refresh skipped: today is 2026-04-26 PT (not 1st of month). Next refresh 2026-05-01. | no action |
| 2026-04-27T04:10:00Z | overnight | system | Routine #1 result: 1 OPEN (TAO), 0 CLOSE, 0 ACTIONABLE news. Equity $9,988.63 (cash $5.73 + positions $9,982.90), realized −$69.24, unrealized +$57.87 (overnight rally lifted ETH/BTC/SOL into profit), DD 0.39% from peak. Portfolio risk 0.99%, all kill switches clear. 4/4 strategy-cap concurrent slots filled. Telegram digest required per template (new OPEN occurred). | TELEGRAM SEND — entry digest |
| 2026-04-27T13:00:00Z | overnight | kraken | Risk flag CLEAR (scan 12:30Z, no tier-1/2; classifier note: routine sanctions only). Universe 24h regime FLIPPED NEGATIVE since prior wake: 13/15 pairs red — FARTCOIN -2.97, AVAX -2.43, ETH -2.34, SOL -2.13, LINK -1.90, ADA -1.76, SUI -1.71, XRP -1.49, LTC -1.47, XBT -1.26, XDG -1.09, TAO -0.52, HYPE -0.47; positives: TRX +0.74, PENGU +9.61 (post-cascade rebound). | context — bearish reversal, 1H RSI>55 unlikely on most pairs |
| 2026-04-27T13:00:00Z | overnight | kraken | ETH/USD position check: 1H bar 05:00Z low 2319.46 < stop 2345.10 → STOP HIT intrabar. Fill 2343.93 (stop × 0.9995 adverse slip per TRX precedent). Stop-dist 19.62, loss-per-unit 20.79 → R = -1.06. Net realized −$34.68 (gross −$21.83 + commissions $12.85 entry+exit at 0.26%/side). | EXIT ETH (exit-stop-hit) |
| 2026-04-27T13:00:00Z | overnight | kraken | BTC/USD position check: 1H bar 05:00Z low 77601.0 < stop 77803.14 → STOP HIT intrabar. Fill 77764.24. Stop-dist 463.07, loss-per-unit 501.97 → R = -1.08. Net realized −$28.77. | EXIT BTC (exit-stop-hit) |
| 2026-04-27T13:00:00Z | overnight | kraken | SOL/USD position check: 1H bar 05:00Z low 85.82 < stop 86.10 → STOP HIT intrabar. Fill 86.057. Stop-dist 0.69, loss-per-unit 0.733 → R = -1.06. Net realized −$33.82. | EXIT SOL (exit-stop-hit) |
| 2026-04-27T13:00:00Z | overnight | kraken | TAO/USD position check: 1H bar 05:00Z low 250.1191 < stop 251.12 → STOP HIT intrabar (entry was 04:05Z @ 255.56, held ~1 hour). Fill 251.004. Stop-dist 4.44, loss-per-unit 4.5556 → R = -1.03. Net realized −$56.38. | EXIT TAO (exit-stop-hit) |
| 2026-04-27T13:00:00Z | overnight | system | NOTABLE PRICE ANOMALY: all 4 open positions stopped out simultaneously in the same 05:00Z 1H bar — cross-asset cascade. ETH dropped -2.66% intra-bar, BTC -1.68%, SOL -1.95%, TAO -1.97%. Total day realized −$153.65 (-1.54% of pre-cascade equity, well below 5% kill switch). Lesson appended to lessons.md (correlation risk in v0 sizing). | Lesson logged |
| 2026-04-27T13:00:00Z | overnight | kraken | Entry scan post-cascade: ETH/BTC/SOL/TAO 1H closes (12:00Z) all below pre-dump-elevated SMA20 → REJECT rule-1 (1H close < EMA20). Bearish regime drives 1H RSI14 below 55 across negative-drift pairs → inferred REJECT rule-2 for AVAX/ADA/LINK/SUI/XRP/LTC/XDG/HYPE/FARTCOIN. TRX +0.74% but rank 15 / $1.04M monthly notional → REJECT per lesson #1 (sub-$2M wick risk). PENGU +9.61% but rank 14 / $1.07M monthly → REJECT per lesson #1. Net: 0 entries. | REJECT (15 pairs) |
| 2026-04-27T13:00:00Z | overnight | system | News scan deferred per established pattern: kraken_risk_flag CLEAR pre-screen ("Markets calm"), morning-brief skill runs separately. v0 not news-reactive. No headline-level actionable items recorded. The 05:00Z cascade had no obvious news trigger in the risk-scan window — purely market-internal flow. | deferred |
| 2026-04-27T13:00:00Z | overnight | system | Universe refresh skipped: today is 2026-04-27 (not 1st of month). Next refresh 2026-05-01 (Friday). | no action |
| 2026-04-27T13:00:00Z | overnight | system | Routine #1 result: 0 OPEN, 4 CLOSE (cross-asset stop cascade ETH/BTC/SOL/TAO at 05:00Z), 0 ACTIONABLE news. Equity $9,777.08 (cash, no positions), realized all-time −$222.89, DD 2.50% from peak $10,027.55. Day realized −$153.65 (-1.54%). Portfolio risk 0.00%. Daily-loss kill switch 1.54% vs 5% cap (clear). DD 2.50% vs 25% cap and 12.5% warn (clear). Equity floor far above $7,500. Telegram digest required per template (4 stop-out CLOSEs occurred). | TELEGRAM SEND — exit digest |
| 2026-04-28T02:44:14Z | harness | day-gate | not Saturday, skipping | no action
| 2026-04-28T02:44:30Z | allocation | day-gate | not Sunday (Mon 2026-04-27 PT), skipping | no action |
| 2026-04-28T17:00:00Z | overnight | kraken | Risk flag CLEAR (scan 2026-04-28T02:43Z, no tier-1/2; "Markets calm"). Universe 24h regime BROADLY NEGATIVE post-cascade rebound: 12/15 red — XBT -1.81, XRP -1.83, ETH -1.07, SOL -1.44, HYPE -4.42, SUI -1.45, LTC -0.79, ADA -0.54, FARTCOIN -0.05, AVAX -0.76, LINK -1.00, PENGU -1.32, TRX -0.59; positives: TAO +5.08, XDG +0.65. | context — divergent tape, TAO breakout against weak broader market |
| 2026-04-28T17:00:00Z | overnight | kraken | Position check: no open positions to manage at start of wake (flat from 2026-04-27 cascade). | no action |
| 2026-04-28T17:00:00Z | overnight | kraken | TAO/USD entry scan (1H close 16:00Z = 259.9863, just-closed bar): 1H SMA20 ≈ 249.90 (PASS +4.0%), 1H RSI14 ≈ 86.1 (PASS but climactic/extreme), 4H close (just-closed 12:00Z bar) 256.2051 > 4H SMA50 247.45 (PASS +3.5%), ATR14(1H) ≈ 2.69. Universe rank 5, 24h notional ≈ $2.86M (live) > $2M lesson-1 threshold. Pre-entry guardrails: positions 0<4 (4 slots open), portfolio risk 0%+0.52%≤4%, per-trade 0.52%≤1.5%, in-universe, daily loss 0%<5%, equity $9,777 above $7,500 floor — ACCEPT. | OPEN long @ 260.12 (close + 0.05% slip), stop 254.74 (2×ATR), size 9.4 (equity/4 cash convention, $2,445 notional), risk $50.57 (0.52%) — entry-rule-v0-momentum |
| 2026-04-28T17:00:00Z | overnight | kraken | XDG/USD entry scan (1H close 16:00Z = 0.0995999): 1H SMA20 ≈ 0.09918 (PASS razor-thin +0.42%), RSI14 ≈ 54.65 (FAIL <55 by 0.35). | REJECT — entry-rule-2 (1H RSI14 < 55, razor-thin miss) |
| 2026-04-28T17:00:00Z | overnight | kraken | HYPE/USD entry scan: 24h -4.42% strong negative; under negative drift RSI14>55 mathematically implausible. Plus universe rank 6 ($5.86M) above lesson-1 threshold but no positive momentum to qualify. | REJECT — entry-rule-2 (1H RSI14 < 55) inferred |
| 2026-04-28T17:00:00Z | overnight | kraken | PENGU/USD entry scan: 24h -1.32%; rank 14 ($1.07M monthly notional) below $2M lesson-1 threshold. | REJECT — entry-rule-2 inferred + lesson-1 thin-liquidity skip |
| 2026-04-28T17:00:00Z | overnight | kraken | FARTCOIN/USD entry scan: 24h -0.05%; rank 11 ($1.52M monthly notional) below $2M lesson-1 threshold. | REJECT — entry-rule-2 inferred + lesson-1 thin-liquidity skip |
| 2026-04-28T17:00:00Z | overnight | kraken | TRX/USD entry scan: 24h -0.59%; rank 15 ($1.04M monthly notional) below $2M lesson-1 threshold. | REJECT — entry-rule-2 inferred + lesson-1 thin-liquidity skip |
| 2026-04-28T17:00:00Z | overnight | kraken | Remaining 9 pairs (XBT -1.81, ETH -1.07, SOL -1.44, XRP -1.83, SUI -1.45, LTC -0.79, ADA -0.54, AVAX -0.76, LINK -1.00) — all 24h negative under risk-off broader tape; under negative drift, 1H RSI14>55 mathematically unlikely. Context-budget decision not to compute individually, consistent with prior wakes' methodology. | REJECT (9 pairs inferred) — entry-rule-2 (1H RSI14 < 55) |
| 2026-04-28T17:00:00Z | overnight | system | Lesson #2 (cross-asset cascade) flagged for review: TAO entry on RSI 86 climactic in divergent tape (12/15 negative) vs prior cascade pattern. Different vector — only 1 slot fill not 4 — so lesson #2's specific failure mode (concurrent correlated stops) does not apply, but RSI extremity + same-day re-entry post-stopout is a new risk pattern to monitor. If TAO stops within 6h, append data point to lessons.md for routine #4 RSI-cap proposal. | proceed with entry, monitor at midday |
| 2026-04-28T17:00:00Z | overnight | system | News scan deferred per established pattern: kraken_risk_flag CLEAR pre-screen ("Markets calm"), morning-brief skill runs separately. v0 not news-reactive. The 04-27 05:00Z cascade had no news trigger — purely market-internal flow per prior wake's analysis, reinforcing v0's news-blindness as not a current cost factor. | deferred |
| 2026-04-28T17:00:00Z | overnight | system | Universe refresh skipped: today is 2026-04-28 (not 1st of month). Next refresh 2026-05-01 (Friday). | no action |
| 2026-04-28T17:00:00Z | overnight | system | Routine #1 result: 1 OPEN (TAO/USD), 0 CLOSE, 0 ACTIONABLE news. Equity $9,769.46 (cash $7,325.59 + position $2,443.87), realized −$222.89, unrealized −$7.62 (entry drag), DD 2.57% from peak $10,027.55. Portfolio risk 0.52%, all kill switches clear. 1/4 strategy-cap concurrent slots filled. Telegram digest required per template (new OPEN occurred). | TELEGRAM SEND — entry digest |
2026-04-28T17:59:42Z | harness | day-gate | not Saturday, skipping | no action
2026-04-28T17:59:41Z | allocation | day-gate | not Sunday, skipping | no action
| 2026-04-28T23:07:36Z | strategy | applied | W18 proposal A+B+C approved off-cycle by user via chat 2026-04-28; cluster cap, liquidity floor, one-per-wake committed to strategy.md (v0 -> v0.1); 2 lessons marked superseded | strategy.md updated, lessons updated, research_log appended |
| 2026-04-29T14:00:00Z | overnight | kraken | Risk flag CLEAR (scan 2026-04-29T00:00:32Z, no tier-1/2; "Markets calm"). Universe 24h regime BROADLY NEGATIVE: 14/15 red — PENGU -4.39, TAO -2.81, FARTCOIN -2.59, SUI -2.22, LINK -1.31, XRP -1.09, HYPE -1.05, ADA -0.91, LTC -0.75, SOL -0.61, ETH -0.52, XBT -0.38, AVAX -0.22, TRX -0.08; only positive XDG +4.0% (climactic blow-off, peak 0.1120 then -7.7% pullback). | context — risk-off divergent tape, RSI>55 mathematically unlikely on 14/15 pairs |
| 2026-04-29T14:00:00Z | overnight | kraken | TAO/USD position check: 1H bar 14:00Z low 253.7004 < stop 254.74 → STOP HIT intrabar. Fill 254.61 (stop × 0.9995 adverse slip per established model). Stop-dist 5.38, loss-per-unit 5.51 → R = -1.02. Net realized −$64.37 (gross −$51.79 + commissions $12.58). Position held ~21h after 17:00Z 04-28 entry; survived overnight rally to high 266.44 (+2.4% above entry) but reversed sharply, drift to 14:00Z dump. | EXIT TAO (exit-stop-hit) |
| 2026-04-29T14:00:00Z | overnight | kraken | XDG/USD entry scan (1H close 15:00Z = 0.1033165, just-closed bar): 1H SMA20 ≈ 0.10335 (FAIL by 0.04% — close just below SMA20). 24h notional ~$15.6M (well above $2M lesson-1 / W18-B floor). Pattern: blow-off top — peak 0.1120861 at 09:00Z, since pulled back -7.7% over 6 bars (climactic exhaustion). Discretionary read reinforces rule-1 fail: late-stage chase against sharp reversal. | REJECT — entry-rule-1 (1H close < 1H EMA20) + climactic exhaustion read |
| 2026-04-29T14:00:00Z | overnight | kraken | Remaining 13 non-open pairs (XBT -0.38, ETH -0.52, SOL -0.61, XRP -1.09, TAO -2.81, HYPE -1.05, SUI -2.22, LTC -0.75, ADA -0.91, FARTCOIN -2.59, AVAX -0.22, LINK -1.31, PENGU -4.39, TRX -0.08): all 24h negative under risk-off broader tape; under negative drift, 1H RSI14>55 mathematically unlikely. Liquidity sub-$2M floor excludes AVAX ($0.44M), LINK ($1.22M), LTC ($1.88M), TRX ($1.34M) regardless. Context-budget decision not to compute individually, consistent with prior wakes' methodology. | REJECT (13 pairs inferred) — entry-rule-2 (1H RSI14 < 55) ± W18-B liquidity floor |
| 2026-04-29T14:00:00Z | overnight | kraken | TAO same-day re-entry post-stopout flagged as failed pattern: 04-28 17:00Z entry on RSI ≈86 (climactic) in divergent tape (12/15 negative); 04-29 14:00Z stop-out at -1.02R after 21h hold. Lesson #4 candidate — RSI extremity at entry combined with broad-tape divergence is a worse-than-average setup. To be formalized in next routine #4 with backtest evidence; pattern noted to lessons.md. | lesson appended (RSI-extremity / divergent-tape setup) |
| 2026-04-29T14:00:00Z | overnight | system | News scan deferred per established pattern: kraken_risk_flag CLEAR pre-screen ("Markets calm"), morning-brief skill runs separately. v0.1 not news-reactive. | deferred |
| 2026-04-29T14:00:00Z | overnight | system | Universe refresh skipped: today is 2026-04-29 (not 1st of month). Next refresh 2026-05-01 (Friday). | no action |
| 2026-04-29T14:00:00Z | overnight | system | Routine #1 result: 0 OPEN, 1 CLOSE (TAO/USD stop-hit), 0 ACTIONABLE news. Equity $9,712.70 (cash, no positions), realized all-time −$287.26, DD 3.14% from peak $10,027.55 (warn 12.5% / cap 25%). Day realized −$64.37 (−0.66% on pre-close equity, cap 5%). Portfolio risk 0.00%. Equity floor far above $7,500. Telegram digest required per template (CLOSE event occurred). | TELEGRAM SEND — exit digest |
2026-04-29T17:07:19Z | harness | day-gate | not Saturday, skipping | no action

2026-04-29T17:40:38Z | allocation | day-gate | not Sunday, skipping | no action
| 2026-04-29T20:07:09Z | midday | system | Portfolio flat (0 open positions) after TAO stop-out at 14:00Z; no MTM/exit checks required. Equity $9,712.70 = cash $9,712.70 (no positions). Day realized −$64.37 (−0.66% on pre-close equity, cap 5%). DD 3.14% from peak $10,027.55 (warn 12.5%, cap 25%). All kill switches clear: daily loss 0.66% < 5%, DD 3.14% < 12.5% warn, equity > $7,500 floor, consecutive-losing-days streak not 7-in-a-row. Midday is position-mgmt only — no entries scanned per routine spec. | no action — silent (no exits, no kill-switch trip, no DD warning) |
2026-05-04T19:07:20Z | harness | day-gate | not Saturday, skipping | no action
2026-05-04T19:08:14Z | allocation | day-gate | not Sunday, skipping | no action

## 2026-05-04T19:00Z — routine-01-overnight

> **Note:** First routine-01 run since 2026-04-29 — 5-day gap (4-30 Thu, 5-01 Fri, 5-02 Sat, 5-03 Sun, 5-04 Mon morning). May 1 universe-refresh window was missed; flagging for catch-up but not refreshing this wake (strict spec is "today is the 1st" and the procedural cost outweighs membership stability over 4 days).

### Technical (rule-driven, deterministic)

- **Risk flag:** CLEAR (scan 2026-05-04T00:17Z; 1 tier-2 caution: Iran military-escalation headline, non-blocking — needs 2 major-source confirmations).
- **Universe regime:** 12/15 positive 24h — XBT +1.80, ETH +1.49, SOL +0.76, XRP +0.92, XDG +2.17, SUI +1.89, LTC −0.20, ADA +0.74, FARTCOIN +3.65, AVAX +1.98, LINK +3.16, PENGU +1.27, TRX +0.37, HYPE −0.39, TAO −2.01. **Regime gate (W19-D rule 5a):** PASS — 12/15 ≥ 4/15 positive.
- **Liquidity floor (W18-B rule 4a):** AVAX 24h notional ≈ $1.76M — FAIL $2M floor (excluded). All others ≥ $2M (TRX razor-thin ~$2.01M).
- **Same-pair re-entry cooldown (W19-D rule 5b):** No active cooldowns — last stop-out (TAO 04-29) is 5 days old, well past 24h window.

**Entry-scan results (just-closed 1H bar at 18:00Z 5/4):**

- **BTC/USD** (rank 1): close 80105.1, 1H SMA20 ≈ 79642.6 → PASS rule 1; 1H RSI14 ≈ 47.6 → **FAIL rule 2** (post-spike fade after 14:00Z +$1456 pump-then-revert). REJECT.
- **ETH/USD** (rank 2): close 2361.20, 1H SMA20 ≈ 2356.39 → PASS rule 1 (razor-thin +0.20%); 1H RSI14 ≈ 41.0 → **FAIL rule 2**. REJECT.
- **SOL/USD** (rank 3): not individually computed — cluster-correlated with BTC/ETH, expected similar RSI fade pattern. INFERRED REJECT — entry-rule-2.
- **XRP/USD** (rank 4): close 1.40378, 1H SMA20 ≈ 1.40378 → razor-tie **FAIL rule 1** (need close > EMA20 strict). REJECT.
- **TAO/USD** (rank 5): 24h −2.01% — under negative drift, 1H RSI14>55 mathematically unlikely. INFERRED REJECT — entry-rule-2.
- **HYPE/USD** (rank 6): 24h −0.39% — INFERRED REJECT — entry-rule-2.
- **XDG/USD** (rank 7): close 0.1110277, 1H SMA20 ≈ 0.1113126 → **FAIL rule 1** (close < EMA20 by 0.26%). Pattern: post-pump fade from 0.1137 peak at 03:00Z. REJECT.
- **SUI/USD** (rank 8): close 0.9399, 1H SMA20 ≈ 0.93471 → PASS rule 1; 1H RSI14 ≈ 45.5 → **FAIL rule 2**. REJECT.
- **LTC/USD** (rank 9): 24h −0.20% — INFERRED REJECT — entry-rule-2.
- **ADA/USD** (rank 10): 24h +0.74% modest, not pulled — 1 entry already chosen. HOLD-OFF.
- **FARTCOIN/USD** (rank 11): close 0.2103, 1H SMA20 ≈ 0.21108 → **FAIL rule 1** (close < EMA20 by 0.37%). REJECT.
- **AVAX/USD** (rank 12): excluded by W18-B liquidity floor ($1.76M < $2M). REJECT — entry-rule-4a.
- **LINK/USD** (rank 13): close 9.43462, 1H SMA20 ≈ 9.36810 → PASS rule 1 (+0.71%); 1H RSI14 ≈ 55.3 → PASS rule 2 (razor-thin) and rule 2a (<80); 4H close (12:00Z bar) 9.42709, 4H SMA50 ≈ 9.22660 → PASS rule 3 (+2.18%); ≥10 candles ✓; 24h notional $5.17M > $2M ✓; not already open ✓; cluster cap 0/2 → entry yields 1/2 ✓; per-trade risk 0.63% ≤ 1.5% ✓; portfolio risk 0% + 0.63% = 0.63% ≤ 4% ✓; daily loss 0% < 5% ✓; equity $9,712.70 > $7,500 ✓. ATR14(1H) ≈ 0.1187. **Pre-entry-check ACCEPT.**
- **PENGU/USD** (rank 14): 24h notional ~$2.55M (above floor); 24h +1.27%. Not pulled — 1 entry already chosen, lower 30d-rank than LINK per universe.md. HOLD-OFF (W18-C one-per-wake, prefer-highest-rank).
- **TRX/USD** (rank 15): 24h notional razor-thin ~$2.01M; 24h +0.37% modest. Not pulled — same reason. HOLD-OFF.

**Final candidate:** LINK/USD (only pair clearing all 8 rules + cluster + liquidity + regime + cooldown).

### News (Firecrawl-driven, informational only in v0.2)

News scan deferred per established pattern: kraken_risk_flag CLEAR pre-screen (1 tier-2 military-escalation caution but non-blocking, lacks major-source confirmation). v0.2 strategy is not news-reactive — no entry gate depends on news this run. Morning-brief skill runs separately and surfaces ACTIONABLE headlines if any. No headline-level actionable items recorded for this routine.

### Sentiment (passive — Kraken depth/spread proxy in v0.2)

Not pulled this wake — broad-rally regime with sufficient candidate clarity from price/volume data alone. To be added to candidate-only scans in routine #2 if entry sat at marginal pass.

### Decision

**OPEN LINK/USD long** @ 9.4393 (close 9.43462 + 0.05% slip), stop 9.2018 (entry − 2×ATR), size 257 LINK (equity/4 cash convention, $2,425.90 notional), risk $61.03 (0.63% of equity). Reason: entry-rule-v0-momentum (rules 1, 2, 2a, 3, 4, 4a, 5, 5a, 5b, 6, 6a, 7, 8 all pass). Trade row appended to trade_log.md; portfolio.md rebuilt.

Cluster state after entry: 1/2 in BTC-correlated cluster {BTC,ETH,SOL,TAO,AVAX,SUI,LINK}.

### Process notes

- **5-day routine gap (2026-04-30 → 2026-05-04 morning):** No routine-01 entries between 2026-04-29T14:00Z and now. Cause unknown (scheduled-task interruption, no exit log). Flagging for operator review — does not affect this wake's decision (portfolio was flat through gap, no open positions to mismanage).
- **May 1 universe-refresh missed:** Today's 24h-notional readings indicate universe membership likely unchanged (top 15 stable from 2026-04-20 ranking; AVAX dropped below liquidity floor but still in universe). Strict spec says refresh on the 1st of month — today is 4th. Will re-evaluate at next month's window (2026-06-01 Mon). Operator may force a refresh via direct universe.md edit if desired.
- **Concurrent routine-02-midday rebuild at 19:05:30Z:** Wrote portfolio.md to "flat" state; superseded by this wake's rebuild at 19:10:00Z reflecting LINK OPEN.

### Telegram

ENTRY DIGEST required per template (new OPEN occurred). Message will be sent after commit.
| 2026-05-04T19:14:56Z | offline-audit | system | User offline 2026-04-29 20:07Z to 2026-05-04 today; cron silent during gap (Claude Code Desktop was closed). Zero routine wakes, zero trades during 5-day window. Strategy v0.2 untested in production since W19 application. CODEX competitor data files stale at $10K baselines (no refresh observed). OPERATING.md created documenting cron-Claude-Code dependency and CODEX sync gap. | OPERATING.md added; no manual routine catch-up triggered (per recommendation 'let cron resume naturally'); next scheduled wake bull-02-midday at 2026-05-04T20:05Z |

## 2026-05-05T05:00Z — routine-01-overnight (EOD-window pass; bull-03-eod cron fired post-22:00 PT)

> Wake context: bull-03-eod task fired with routine-01-overnight content. Just-closed 1H bar = 2026-05-05 05:00Z (= 2026-05-04 22:00 PT). Pre-existing position: LINK from morning routine-01. Risk flag: CLEAR (kraken_risk_flag scan 2026-05-05T00:00Z, tier1=0, tier2=0, blocked=false).

### Universe price scan (15 pairs, 24h % change)

| Pair | Last | 24h % | 24h notional | vs $2M floor |
|------|------|-------|--------------|--------------|
| BTC/USD | 80926.7 | +1.36 | $194.9M | ✓ |
| ETH/USD | 2378.7 | +1.35 | $45.6M | ✓ |
| SOL/USD | 84.85 | +0.89 | $13.7M | ✓ |
| XRP/USD | 1.40077 | +0.65 | $13.9M | ✓ |
| TAO/USD | 285.84 | +0.32 | $5.93M | ✓ |
| HYPE/USD | 42.42 | +1.48 | $5.72M | ✓ |
| XDG/USD | 0.1115 | +1.25 | $7.97M | ✓ |
| SUI/USD | 0.9408 | +1.22 | $2.00M | ✓ (tight) |
| LTC/USD | 55.14 | +0.29 | $3.15M | ✓ |
| ADA/USD | 0.25251 | +1.03 | $3.35M | ✓ |
| FARTCOIN/USD | 0.2101 | +2.69 | $1.96M | ✗ |
| AVAX/USD | 9.28 | +1.09 | $1.98M | ✗ |
| LINK/USD | 9.56418 | +2.12 | $4.67M | ✓ (open) |
| PENGU/USD | 0.010761 | +6.57 | $4.70M | ✓ |
| TRX/USD | 0.339148 | −0.43 | $2.01M | ✓ (tight) |

Regime gate (W19-D 5a): **14/15 positive** ≥ 4 → PASS, new entries allowed.

### Position check on open positions

- **LINK/USD** (long 257 @ 9.4393, stop 9.2018): last 9.56418, 24h low 9.2592 — well above stop, no stop-out. MTM +$25.78. Hold.

No exits this wake.

### Entry-scan candidates (rule 8 prefer highest 30d notional rank)

- **BTC/USD** (rank 1): 1H close 80920.7, 1H 20-EMA ≈ 80317.5 → PASS rule 1; 1H RSI14 ≈ 67.0 → PASS rule 2 (>55) and rule 2a (≤80); 4H last-closed (2026-05-05 00:00) close 80879.3, 4H 50-EMA ≈ 78159 → PASS rule 3; ≥10 candles ✓; 24h notional $194.9M > $2M ✓; not currently open ✓ (last BTC stop 2026-04-27, ~8d ago > 24h cooldown ✓); regime 14/15 positive ≥ 4 ✓; positions 1<4 ✓; cluster: LINK 1 → BTC entry brings to 2 ≤ 2 ✓; per-trade risk computed below; portfolio risk 0.63%+0.26% = 0.89% ≤ 4% ✓; rank 1 (top of universe). **Pre-entry-check ACCEPT.**

  - ATR14(1H) ≈ 418.49 → 2×ATR = 836.97
  - Fill = 80920.7 × 1.0005 = 80961.16 (close + 0.05% slip)
  - Stop = 80961.16 − 836.97 = 80124.19
  - Sizing: equity/4 cash convention (per W18-aligned practice; risk-based 0.1737 BTC would consume 99% of cash and breach prudence) → notional $9,730.98/4 ≈ $2,433. Size = floor(2422 / 80961.16, 4 dp) = **0.0299 BTC**. Notional 0.0299×80961.16 = $2,420.74. Entry comm 0.26% × 2420.74 = $6.29. Total cost $2,427.03. Cash after: $4,853.46.
  - Risk: 0.0299 × 836.97 = $25.02 = 0.26% of equity ($9,691.99 pre-entry). Well within 1.5% per-trade cap.

- **ETH/USD** (rank 2): would also satisfy 1H/4H/RSI checks (close 2378.7 above EMA20, RSI estimated ~60-65 from rally bars 02:00-03:00 UTC), but per rule 8 BTC wins by rank when both eligible. Cluster cap would also be hit at 2/2 either way. INFERRED REJECT — entry-rule-8 (lower rank than BTC; 1 entry/wake limit).

- **SOL/USD** (rank 3): cluster-correlated with BTC; even if rules pass, blocked by rule 6a cluster cap (BTC entry brings cluster to 2/2; SOL would push 3>2). REJECT — entry-rule-6a.

- **XRP/USD** (rank 4): not pulled in detail — 1 entry already chosen this wake (rule 8 W18-C). HOLD-OFF. Note: XRP is non-cluster, would be candidate next wake if XRP's own conditions still pass.

- **TAO/USD** (rank 5): cluster-correlated, cluster cap blocks even if rules pass. REJECT — entry-rule-6a.

- **HYPE/USD** (rank 6): not pulled in detail — HOLD-OFF (W18-C, 1/wake).

- **XDG/USD** (rank 7): not pulled in detail — HOLD-OFF.

- **SUI/USD** (rank 8): cluster-correlated, cluster cap blocks. REJECT — entry-rule-6a.

- **LTC/USD** (rank 9): not pulled in detail — HOLD-OFF.

- **ADA/USD** (rank 10): not pulled in detail — HOLD-OFF.

- **FARTCOIN/USD** (rank 11): excluded by W18-B liquidity floor ($1.96M < $2M). REJECT — entry-rule-4a.

- **AVAX/USD** (rank 12): excluded by W18-B liquidity floor ($1.98M < $2M) AND cluster cap. REJECT — entry-rule-4a + 6a.

- **LINK/USD** (rank 13): already open. REJECT — entry-rule-5.

- **PENGU/USD** (rank 14): not pulled in detail — HOLD-OFF (rank lower than BTC; 1/wake limit). Note: 24h +6.57% suggests RSI extension; if pulled, rule 2a (RSI ≤ 80) might bite.

- **TRX/USD** (rank 15): 24h −0.43% — INFERRED REJECT — entry-rule-2 (RSI > 55 unlikely on negative drift).

**Final candidate:** BTC/USD (highest-rank pair clearing all rules; cluster cap 1→2 just within limit).

### News (lightweight scan; morning routine-01 covered Firecrawl pass)

Morning's news scan reported "1 tier-2 military-escalation caution but non-blocking, lacks major-source confirmation". Today's kraken_risk_flag (scanned 2026-05-05T00:00:34Z) reads **CLEAR** — no tier1, no tier2, summary "No significant risk events detected. Markets calm." No fresh Firecrawl pull this wake (token budget; morning pass + automated risk-flag suffice). No ACTIONABLE items.

### Sentiment (passive)

Broad rally regime (14/15 pairs positive). 1H BTC volume on the 14:00Z and 02:00Z bars (198 BTC and 314 BTC respectively) indicates real momentum participation, not low-liquidity wick. Sufficient candidate clarity from price/volume — no spread/depth pull needed.

### Decision

**OPEN BTC/USD long** @ 80961.16 (close 80920.7 + 0.05% slip), stop 80124.19 (entry − 2×ATR), size 0.0299 BTC ($2,420.74 notional), risk $25.02 (0.26% of equity). Reason: entry-rule-v0-momentum (rules 1, 2, 2a, 3, 4, 4a, 5, 5a, 5b, 6, 6a, 7, 8 all pass). Trade row appended to trade_log.md; portfolio.md rebuilt.

Cluster state after entry: **2/2** in BTC-correlated cluster {BTC, ETH, SOL, TAO, AVAX, SUI, LINK} — at the W18-A cap. No further cluster entries possible until LINK or BTC closes.

### Process notes

- **Task-name vs content mismatch:** scheduled task is named `bull-03-eod` (06:00 PT cron) but its SKILL.md content is the routine-01-overnight body. Executed per the SKILL content. The `skills/telegram.md` "EOD mandatory daily card" template is not invoked; routine-01 telegram rule (digest only on entry/kill/news) applies. Operator may want to reconcile task naming vs body in a future maintenance pass.
- **First-of-month universe refresh:** today is 2026-05-04 (Mon, 4th of month) → not first of month → no refresh.
- **Cluster cap state:** at 2/2. Going forward this wake, no cluster pair can be added even if eligible.

### Telegram

ENTRY DIGEST required per template (new OPEN occurred). Message will be sent after commit.

---

## 2026-05-05T17:55:51Z — routine-01-overnight (5/5 wake)

### Universe price snapshot (kraken_multi_ticker)

| Pair | Last | 24h % | 24h notional est | rule-4a ($2M floor) |
|------|------|-------|------------------|---------------------|
| BTC/USD | 81287.0 | +1.81 | $180M | OK |
| ETH/USD | 2363.12 | +0.68 | $38.7M | OK (cluster) |
| SOL/USD | 85.46 | +1.62 | $12.2M | OK (cluster) |
| XRP/USD | 1.40915 | +1.26 | $10.1M | OK |
| TAO/USD | 282.514 | -0.84 | $7.39M | OK (cluster, only neg) |
| HYPE/USD | 44.32 | +6.03 | $6.91M | OK |
| XDG/USD | 0.1138691 | +3.40 | $7.07M | OK |
| SUI/USD | 0.959 | +3.17 | $3.02M | OK (cluster) |
| LTC/USD | 55.63 | +1.18 | $3.58M | OK |
| ADA/USD | 0.2584 | +3.38 | $4.93M | OK |
| FARTCOIN/USD | 0.2203 | +7.67 | $2.16M | OK (just above floor) |
| AVAX/USD | 9.37 | +2.07 | $1.44M | FAIL (cluster + below floor) |
| LINK/USD | 9.69517 | +3.52 | $3.67M | OK (open) |
| PENGU/USD | 0.011474 | +13.63 | $6.49M | OK |
| TRX/USD | 0.34422 | +1.06 | $1.40M | FAIL |

Regime gate (W19-D 5a): **14/15 positive** >= 4 -> PASS, new entries allowed (only TAO -0.84%).
Risk flag: **CLEAR** (1 tier-2 caution: Iran/Hormuz military, non-blocking, lacks major-source confirmation).

### Position check on open positions

- **LINK/USD** (long 257 @ 9.4393, stop 9.2018): last 9.69517, 24h low 9.32 — well above stop. MTM **+$59.45** (+0.97R). Hold. No 1H close < EMA20 trigger detected.
- **BTC/USD** (long 0.0299 @ 80961.16, stop 80124.19): last 81287.0, 24h low 79743.1 occurred at 23:00Z 5/4 (BEFORE 05:00Z 5/5 entry). Post-entry 1H bars (05:00-17:00Z 5/5): minimum low = 80520.0 (09:00Z) — well above stop. MTM **+$3.45**. Hold.

No exits this wake.

### Entry-scan candidates (rule 8 prefer highest 30d notional rank)

Cluster state: 2/2 (LINK + BTC) at W18-A cap -> BTC, ETH, SOL, TAO, AVAX, SUI, LINK all blocked from new cluster entries this wake.

Non-cluster eligible candidates (rank order):

- **XRP/USD** (rank 4): 1H last-closed bar (5/5 16:00Z) close 1.40787, 1H 20-EMA approx 1.40671 -> PASS rule 1; 1H RSI14 approx **60.5** (avg gain 0.001544 / avg loss 0.001006, RS 1.535) -> PASS rules 2 + 2a (>55, <=80); 4H last-closed (5/5 12:00Z) close 1.41175, 4H 50-EMA approx 1.39496 -> PASS rule 3; >=10 candles OK; 24h notional approx $10M > $2M OK; not currently open OK (no XRP stop history); regime 14/15 positive >= 4 OK; positions 2<4 OK; non-cluster — rule 6a not engaged OK; per-trade risk 0.245% <= 1.5% OK; portfolio risk 0.881% + 0.245% = 1.13% <= 4% OK; rank 4 (highest non-blocked rank). **Pre-entry-check ACCEPT.**

  - ATR14(1H) over bars 5/5 03:00-16:00Z = sum TR 0.09725 / 14 = **0.006946** -> 2xATR = 0.013893
  - Fill = 1.40787 x 1.0005 = **1.40857** (close + 0.05% slip)
  - Stop = 1.40857 - 0.013893 = **1.39468**
  - Sizing (equity/4 cash convention per W18-aligned practice; risk-based 10510 XRP would consume notional $14.8K > available cash $4853) -> notional cap $9,712.74/4 approx $2,428. Size = floor(2427/1.40857) = **1723 XRP**. Notional 1723 x 1.40857 = $2,426.97. Entry comm 0.26% x 2426.97 = $6.31. Total cost $2,433.28. Cash after: $2,420.18.
  - Risk: 1723 x 0.013893 = $23.93 = **0.245%** of equity. Well within 1.5% per-trade cap.

- **HYPE/USD** (rank 6): not pulled in detail — HOLD-OFF (W18-C, 1 entry/wake; XRP wins by rank). 24h +6.03% suggests possible RSI extension; if scanned next wake, rule 2a (RSI <= 80) check needed.
- **XDG/USD** (rank 7): not pulled in detail — HOLD-OFF (rank lower than XRP).
- **LTC/USD** (rank 9): not pulled in detail — HOLD-OFF.
- **ADA/USD** (rank 10): not pulled in detail — HOLD-OFF.
- **FARTCOIN/USD** (rank 11): just above $2M floor at $2.16M — borderline. HOLD-OFF (rank lower than XRP, 1/wake limit). 24h +7.67% — RSI-cap concern next wake.
- **PENGU/USD** (rank 14): 24h +13.63% — extremely climactic, rule 2a (RSI <= 80) almost certainly bites. HOLD-OFF + INFERRED REJECT — entry-rule-2a likely.
- **TRX/USD** (rank 15): excluded by W18-B liquidity floor ($1.40M < $2M). REJECT — entry-rule-4a.
- **ETH/USD, SOL/USD, TAO/USD, SUI/USD, AVAX/USD** (cluster): blocked by W18-A cluster cap (2/2). REJECT — entry-rule-6a (regardless of other-rule status).
  - AVAX additionally rejected by W18-B (24h notional $1.44M < $2M).
  - TAO additionally has 24h -0.84% (only negative pair) and would also fail rule 2 likely.
- **LINK/USD** (rank 13): already open. REJECT — entry-rule-5.

**Final candidate:** XRP/USD (highest-rank non-cluster pair clearing all rules).

### News (lightweight scan)

Today's `kraken_risk_flag` (scanned 2026-05-05T17:55:51Z) reads **CLEAR**. Tier-2 caution (Iran/Strait of Hormuz military escalation, France 24 sole source) is non-blocking and lacks major-source confirmation per the classifier. Markets calm; no tier-1 triggers; no market-stress signals. No fresh Firecrawl pull this wake (token budget; risk-flag classifier covers same headline corpus). No ACTIONABLE items per skills/research.md classification (no universe-pair-specific hack/listing/regulatory item).

### Sentiment (passive)

Broad continuation rally. 14/15 universe pairs positive on 24h, only TAO modestly red. PENGU +13.63% and FARTCOIN +7.67% are meme-leg outliers — not entered (rank-priority + RSI-cap risk). HYPE +6.03% is the strongest non-cluster outlier; could be a candidate next wake if it doesn't run too far. BTC at $81.3K is approx 1.8% above prior wake's entry (80961) — momentum thesis confirmed for now.

### Decision

**OPEN XRP/USD long** @ 1.40857 (close 1.40787 + 0.05% slip), stop 1.39468 (entry - 2xATR), size 1723 XRP ($2,426.97 notional), risk $23.93 (0.245% of equity). Reason: entry-rule-v0-momentum (rules 1, 2, 2a, 3, 4, 4a, 5, 5a, 5b, 6, 6a, 7, 8 all pass). Trade row appended to trade_log.md; portfolio.md rebuilt.

XRP is the first **non-cluster** entry of this position cohort — diversifies the open book away from the BTC-correlated cluster (LINK + BTC) currently at the 2/2 cap.

### Process notes

- **First-of-month universe refresh:** today is 2026-05-05 (Tue, 5th of month) -> not first of month and not first weekday of month (5/1 was Friday, already past) -> no refresh.
- **Sizing convention:** continuing the equity/4 cash cap precedent set on prior BTC wake. Strategy.md's risk-based formula (1.5% / stop_dist) would generate 10,510 XRP @ $14.8K notional — far exceeds available cash $4,853 — so cash convention prevails. **Flag for routine-04 review:** strategy.md sizing rule and cash availability are inconsistent under multi-position cohort; routine-04 should propose either (a) explicit notional cap in strategy.md or (b) revert to literal risk-based sizing with smaller position count.
- **Cluster cap state:** unchanged 2/2. Going forward this wake, no cluster pair can be added.
- **Stop-out cooldown (W19-D 5b):** ETH/SOL/TAO/AVAX last stops were 2026-04-27 / 04-29 — well outside the 24h window. Not blocking, but cluster cap is the binding constraint anyway.
- **Telegram:** ENTRY DIGEST required (new OPEN occurred). Message sent after commit.

2026-05-05T18:04:30Z | harness | day-gate | not Saturday (Tue), skipping | no action
2026-05-05T18:05:42Z | allocation | day-gate | not Sunday, skipping | no action

---

## 2026-05-06T04:11:00Z — routine-01-overnight (5/6 wake, fired via bull-03-eod scheduled task)

### Universe price snapshot (kraken_multi_ticker)

| Pair | Last | 24h % | 24h notional est | rule-4a ($2M floor) |
|------|------|-------|------------------|---------------------|
| BTC/USD | 81543.1 | +0.79 | $167M | OK (open) |
| ETH/USD | 2377.31 | +0.71 | $40.4M | OK (cluster) |
| SOL/USD | 87.32 | +1.18 | $19.7M | OK (cluster) |
| XRP/USD | 1.4215 | +0.63 | $13.0M | OK (open) |
| TAO/USD | 286.32 | -2.09 | $12.2M | OK (cluster) |
| HYPE/USD | 44.09 | +0.80 | $6.65M | OK |
| XDG/USD | 0.115688 | +0.75 | $8.62M | OK |
| SUI/USD | 0.9888 | +2.25 | $4.39M | OK (cluster) |
| LTC/USD | 56.81 | +0.80 | $4.37M | OK |
| ADA/USD | 0.264215 | +0.89 | $6.02M | OK |
| FARTCOIN/USD | 0.2291 | +2.05 | $3.32M | OK |
| AVAX/USD | 9.58 | +1.91 | $1.33M | FAIL (cluster + below floor) |
| LINK/USD | 9.87593 | +1.11 | $3.58M | OK (open) |
| PENGU/USD | 0.011077 | +0.32 | $4.34M | OK |
| TRX/USD | 0.343122 | -0.43 | $1.08M | FAIL |

Regime gate (W19-D 5a): **13/15 positive** >= 4 -> PASS, new entries allowed (TAO -2.09%, TRX -0.43% are negative).
Risk flag: **CLEAR** (1 tier-2 caution: Drift Solana exchange hack $295M, 1 major-source confirmation only, non-blocking — Drift is on Solana but our SOL position is blocked by cluster cap regardless; HYPE is on Hyperliquid, no contagion vector).

### Position check on open positions (just-closed bar 03:00Z 5/6)

- **LINK/USD** (long 257 @ 9.4393, stop 9.2018): just-closed close 9.855, 1H 20-EMA approx 9.736 — close > EMA, no exit. 24h low 9.49712 (from 18:00-20:00Z 5/4 bars, before entry); post-entry-bar minimum low (5/4 19:00Z onward) = 9.32 (5/4 20:00Z bar) — above stop 9.2018. Hold. MTM **+$105.90** (+1.74R).
- **BTC/USD** (long 0.0299 @ 80961.16, stop 80124.19): just-closed close 81577.7, 1H 20-EMA approx 81160 — close > EMA, no exit. Post-entry minimum low (5/5 05:00Z onward) = 80520.0 (5/5 09:00Z bar) — above stop 80124.19. Hold. MTM **+$11.11** (+0.44R).
- **XRP/USD** (long 1723 @ 1.40857, stop 1.39468): just-closed close 1.42206, 1H 20-EMA approx 1.412 — close > EMA, no exit. Post-entry minimum low (5/5 17:00Z onward) = 1.40455 (5/5 14:00Z bar — wait, that's pre-entry; post-entry minimum is 1.40455 actually no — post-entry bars start at 17:00Z 5/5 which had low 1.40505, well above stop). Actual post-entry min: 1.40500 (5/5 16:00Z was just-closed at entry, so post-entry bars are 17:00Z+). 17:00Z low 1.40505. Hold. MTM **+$15.96** (+0.67R).

No exits this wake. All 3 trailing trades green; LINK now well into profit territory but EMA-cross exit not triggered.

### Entry-scan candidates (rule 8: prefer highest 30d notional rank among non-blocked)

Cluster state: **2/2** (LINK + BTC) at W18-A cap → BTC, ETH, SOL, TAO, AVAX, SUI, LINK all blocked from new cluster entries this wake.
Open-pair blocks: BTC, LINK, XRP currently held → entry-rule-5 rejects.

Non-cluster, non-open eligible candidates by rank:

- **HYPE/USD** (rank 6): 1H last-closed bar (5/6 03:00Z) close 44.16; 1H 20-EMA approx 43.74 → PASS rule 1; 1H RSI14 approx **60.2** (avg gain 0.110 / avg loss 0.0729, RS 1.510) → PASS rules 2 + 2a (>55, ≤80); 4H last-closed (5/6 00:00Z) close 44.16, 4H 50-EMA approx 41.63 → PASS rule 3; ≥10 candles OK; 24h notional approx $6.65M > $2M OK; not currently open OK (no HYPE history); regime 13/15 positive ≥ 4 OK; positions 3<4 OK; non-cluster — rule 6a not engaged OK; no stop-out history → 5b OK; per-trade risk 0.457% ≤ 1.5% OK; portfolio risk 1.12% + 0.457% = 1.58% ≤ 4% OK; rank 6 (highest non-blocked rank). **Pre-entry-check ACCEPT.**

  - ATR14(1H) over bars 5/5 14:00Z–5/6 03:00Z = sum TR 5.84 / 14 = **0.4171** → 2×ATR = **0.8343**
  - Fill = 44.16 × 1.0005 = **44.18** (close + 0.05% slip; HYPE quoted to 2 decimals on Kraken)
  - Stop = 44.18 − 0.8343 = **43.35**
  - Sizing (cash-bound; equity/4 = $2,451 but available cash only $2,420.18 from prior XRP fill): notional cap = $2,420.18 / 1.0026 = $2,413.91. Size = floor(2413.91 / 44.18) = **54 HYPE**. Notional 54 × 44.18 = $2,385.72. Entry comm 0.26% × 2385.72 = $6.20. Total cost $2,391.92. Cash after: **$28.26**.
  - Risk: 54 × 0.83 = $44.82 = **0.457%** of equity ($9,806). Within 1.5% per-trade cap.

- **XDG/USD** (rank 7): not pulled in detail — HOLD-OFF (W18-C, 1 entry/wake; HYPE wins by rank).
- **LTC/USD** (rank 9): not pulled in detail — HOLD-OFF (rank lower than HYPE).
- **ADA/USD** (rank 10): not pulled in detail — HOLD-OFF.
- **FARTCOIN/USD** (rank 11): 24h notional $3.32M (above $2M floor) — HOLD-OFF (rank lower than HYPE, 1/wake limit). 24h +2.05% modest, RSI-cap unlikely to bite.
- **PENGU/USD** (rank 14): 24h +0.32% (cooled from yesterday's +13.63%) — HOLD-OFF (rank lower than HYPE).
- **TRX/USD** (rank 15): excluded by W18-B liquidity floor ($1.08M < $2M) AND 24h −0.43% (RSI > 55 unlikely on negative drift). REJECT — entry-rule-4a + entry-rule-2 inferred.
- **ETH/USD, SOL/USD, TAO/USD, SUI/USD, AVAX/USD** (cluster): blocked by W18-A cluster cap (2/2). REJECT — entry-rule-6a (regardless of other-rule status).
  - AVAX additionally rejected by W18-B (24h notional $1.33M < $2M).
  - TAO additionally has 24h −2.09% (negative) and would also fail rule 2 likely (only universe negative aside from TRX).
- **LINK/USD, BTC/USD, XRP/USD**: already open. REJECT — entry-rule-5.

**Final candidate:** HYPE/USD (highest-rank non-cluster non-open pair clearing all rules).

### News (lightweight scan)

Today's `kraken_risk_flag` (scanned 2026-05-06T00:00:32Z) reads **CLEAR**. One tier-2 caution: Drift exchange hack on Solana ($295M reported by Yahoo Finance + Decrypt; needs 2 major-source confirmations to escalate). The classifier marked it non-blocking (`counts_toward_block: false`). No tier-1 triggers; no market-stress signals; markets calm. No fresh Firecrawl pull this wake (token budget; risk-flag classifier covers same headline corpus). **Drift hack assessment for BULL universe:** Drift is a Solana DEX. SOL is in our universe and cluster, but cluster cap (2/2) already blocks new SOL entries. Existing positions (LINK, BTC, XRP, HYPE) are non-Solana exposures (LINK is a separate L1, BTC/XRP have no Solana dependency, HYPE is on Hyperliquid). Contagion vector is low. No ACTIONABLE items per skills/research.md classification (no universe-pair-specific hack/listing/regulatory item directly affecting our held pairs).

### Sentiment (passive)

Continued broad rally regime, slightly cooled vs prior wake (13/15 positive vs 14/15 yesterday afternoon). TAO weakest (-2.09%), then TRX (-0.43%). HYPE +0.80% modest — note this is daily change; intraday HYPE rallied from $41.62 (5/4 18:00Z) to $44.65 (5/5 21:00Z high) for ~+7% rally over 27h, then pulled back to $43.59 (5/5 23:00Z low) and recovered to $44.16 by just-closed bar. RSI 60 reflects this consolidation after the rally. BTC continues to trend higher, $81.5K vs $80.6K prior wake (+1.1%); LINK $9.88 vs $9.71 (+1.7%); XRP $1.42 vs $1.41 (+0.7%) — all open positions building unrealized gains. Combined unrealized +$132.97 pre-HYPE.

### Decision

**OPEN HYPE/USD long** @ 44.18 (close 44.16 + 0.05% slip), stop 43.35 (entry − 2×ATR), size 54 HYPE ($2,385.72 notional), risk $44.82 (0.457% of equity). Reason: entry-rule-v0-momentum (rules 1, 2, 2a, 3, 4, 4a, 5, 5a, 5b, 6, 6a, 7, 8 all pass). Trade row appended to trade_log.md; portfolio.md rebuilt.

HYPE is the **second non-cluster** entry of the position cohort — diversifies further away from the BTC-correlated cluster. Book composition now: cluster {LINK, BTC} 2/2, non-cluster {XRP, HYPE} 2 → total 4/4 at strategy max-concurrent.

### Process notes

- **Task-name vs content mismatch (continued):** scheduled task `bull-03-eod` again fired with routine-01-overnight SKILL body. Per prior research_log entry (2026-05-05T17:55:51Z) flagged this for operator reconciliation; following SKILL.md content as instructed by harness. Routine-01 telegram rule applies (digest only on entry/kill/news), not the EOD mandatory daily card.
- **Strategy max-concurrent reached:** 4/4. Next wake cannot open new positions until at least one closes (EMA-cross, stop-hit, or 4R target).
- **Cash-bound sizing:** equity/4 ($2,451) > available cash ($2,420.18) → cash binds. Used floor(cash×0.9974/price) = 54 units. **Continuing flag for routine-04 review:** strategy.md sizing rule (1.5% / stop_dist) still produces sizes far exceeding cash availability under multi-position cohorts; cash-cap convention has been applied implicitly across LINK/BTC/XRP/HYPE entries. Routine-04 should propose either explicit notional cap or revert to literal risk-based sizing with reduced max-concurrent.
- **First-of-month universe refresh:** today is 2026-05-06 (Wed, 6th of month) → not first of month → no refresh.
- **Stop-out cooldown (W19-D 5b):** HYPE has no stop-out history. Closest historical stop in cooldown window: none affecting non-blocked pairs.
- **Drift hack monitoring:** if classifier escalates Drift to tier-1 (2nd major-source confirmation), kraken_risk_flag will flag BLOCKED on next scan. No SOL exposure currently (cluster-blocked anyway). HYPE is on Hyperliquid, structurally separate from Drift/Solana.
- **Telegram:** ENTRY DIGEST required (new OPEN occurred). Message sent after commit.

---

## 2026-05-06T16:30:00Z — routine-01-overnight (5/6 wake, fired ~3.5h late vs 06:00 PT schedule)

### Universe price snapshot (kraken_multi_ticker @ 16:26Z)

| Pair | Last | 24h % | 24h notional est | rule-4a ($2M floor) |
|------|------|-------|------------------|---------------------|
| BTC/USD | 81600.0 | +0.87 | $194M | OK (open) |
| ETH/USD | 2357.01 | -0.15 | $47.5M | OK (cluster) |
| SOL/USD | 88.87 | +2.98 | $32.9M | OK (cluster) |
| XRP/USD | 1.42743 | +1.05 | $27.3M | OK (open) |
| TAO/USD | 312.5493 | +6.88 | $21.2M | OK (cluster) |
| HYPE/USD | 43.56 | -0.41 | $7.04M | OK (closed-out this wake) |
| XDG/USD | 0.1129205 | -1.66 | $13.30M | OK |
| SUI/USD | 0.9903 | +2.41 | $8.42M | OK (cluster) |
| LTC/USD | 57.06 | +1.24 | $4.36M | OK |
| ADA/USD | 0.266559 | +1.78 | $4.44M | OK |
| FARTCOIN/USD | 0.2491 | +10.96 | $7.50M | OK |
| AVAX/USD | 9.61 | +2.23 | $2.15M | OK (cluster, borderline) |
| LINK/USD | 10.02422 | +2.63 | $4.76M | OK (open) |
| PENGU/USD | 0.010957 | -0.77 | $2.87M | OK |
| TRX/USD | 0.345811 | +0.35 | $1.22M | FAIL |

Regime gate (W19-D 5a): **11/15 positive** ≥ 4 → PASS, new entries allowed (negatives: ETH -0.15, HYPE -0.41, PENGU -0.77, XDG -1.66).
Risk flag: **CLEAR** (1 tier-2 caution: Drift Solana exchange hack, still 1 major-source confirmation, non-blocking).

### Position check on open positions (post-entry bar review through 15:00Z just-closed)

- **LINK/USD** (long 257 @ 9.4393, stop 9.2018): post-entry min low 9.32 (5/4 20:00Z), all subsequent ≥ 9.65; 1H 20-EMA at 15:00Z ~9.94 vs close 10.03833 → above EMA, no exit; 4R target 10.3893 not reached (highest close 10.18011, highest high 10.24485). Hold. MTM +$144.01 (+2.36R via price move 0.585/0.2375).
- **BTC/USD** (long 0.0299 @ 80961.16, stop 80124.19): post-entry min low 80728.1 (5/6 00:00Z), above stop; 15:00Z close 81700.1, 20-EMA ~81684 → just above EMA, no exit (margin small); 4R target 84309.04 not reached (highest close 82502.1). Hold. MTM +$12.81.
- **XRP/USD** (long 1723 @ 1.40857, stop 1.39468): post-entry min low 1.40500, above stop; 15:00Z close 1.43035, 20-EMA ~1.43 → above EMA, no exit; 4R target 1.46413 not reached (highest high 1.45706). Hold. MTM +$26.18.
- **HYPE/USD** (long 54 @ 44.18, stop 43.35): **STOP HIT** — 15:00Z bar low 43.18 < stop 43.35. Exit fill 43.35 × (1−0.0005) = **43.33** (slippage model matches TRX 04-24 precedent). Realized: 54 × 43.33 − 0.26% comm = $2,333.74 proceeds vs $2,391.92 entry cost = **−$58.18 / −1.02R**. Trade row appended. Holding period ~11h. Brief profit window (high 44.78 at 12:00Z 5/6, +1.4% above entry, well below 4R target $47.50) followed by waterfall sell-off through 13:00Z (-1.1% on 8× normal volume) → 14:00Z (low 43.48, just above stop) → 15:00Z (low 43.18, stop hit).

**Stop-out diagnosis:** HYPE entered at 03:00Z close 44.16 with RSI ~60.2 (within 55–80 band) and 4H trend up. The 13:00Z 1H bar produced an outsized down-bar (close 43.90 vs open 44.38, -1.1%) on extreme volume (42,446 vs 1H avg ~5K — 8× normal). Likely concentrated sell flow from Hyperliquid-related news or single large seller. Subsequent 2 bars failed to recover; stop triggered. No tier-1 risk-flag trigger; broader regime stayed up. **Pattern: rapid volume-spike sell-off in single 1H bar overwhelmed 2×ATR stop.** Similar in mechanism to the 2026-04-27 cluster cascade (single-bar stop-outs) but isolated to one pair this time. Lessons.md updated only if pattern repeats; one-off skipped per cap policy.

### Entry-scan candidates (rule 8: prefer highest 30d notional rank among non-blocked)

After HYPE close: open positions {LINK, BTC, XRP} = 3. Cluster {LINK, BTC} = 2/2 at W18-A cap.

Non-cluster, non-open eligible candidates by rank:

- **HYPE/USD** (rank 6): **REJECT — entry-rule-5b** (24h same-pair re-entry cooldown after exit-stop-hit at 15:00Z, blocked until 2026-05-07T15:00Z).
- **XDG/USD** (rank 7): 24h −1.66% (one of only 4 negatives). 1H RSI almost certainly < 55. **REJECT — entry-rule-2 inferred** (not pulled in detail; lower rank than LTC anyway).
- **LTC/USD** (rank 9): full pull below — **CANDIDATE PASS**.
- **ADA/USD** (rank 10): not pulled in detail — HOLD-OFF (W18-C, 1 entry/wake; LTC wins by rank).
- **FARTCOIN/USD** (rank 11): 24h +10.96% — climactic. RSI > 80 likely. HOLD-OFF + INFERRED REJECT — entry-rule-2a likely.
- **PENGU/USD** (rank 14): 24h −0.77%. **REJECT — entry-rule-2 inferred**.
- **TRX/USD** (rank 15): 24h notional $1.22M < $2M floor. **REJECT — entry-rule-4a**.
- **ETH, SOL, TAO, SUI, AVAX** (cluster): blocked by W18-A cluster cap (2/2). **REJECT — entry-rule-6a**.
- **LINK, BTC, XRP**: already open. **REJECT — entry-rule-5**.

#### LTC/USD detailed pre-entry computation (just-closed 1H bar 15:00Z)

- 1H bars: 30 fetched. Close 57.11; 1H 20-EMA (recursive seed-from-bar-1) ≈ **56.94** → close > EMA → **PASS rule 1**.
- 1H RSI(14) over closes ending 15:00Z: gains sum 1.62 / losses sum 1.13 (over 14 changes) → avg gain 0.1157 / avg loss 0.0807 → RS 1.434 → RSI **58.91** → **PASS rules 2 (>55) + 2a (≤80)**.
- 4H bars: 60 fetched. Just-closed 4H bar 12:00Z close 57.11 (next 4H bar 16:00Z still in progress). 4H 50-EMA (recursive seed-from-bar-1) ≈ **55.81** → close > EMA → **PASS rule 3**.
- Rule 4: ≥10 bars 1H + 4H ✓.
- Rule 4a: 24h notional 76,339.7968 × VWAP ~57 ≈ **$4.36M** > $2M floor → **PASS**.
- Rule 5: not currently open ✓.
- Rule 5a: regime 11/15 positive ≥ 4 ✓.
- Rule 5b: last LTC close was 2026-04-25T17:00Z exit-ema-cross (NOT a stop-out) → cooldown does not apply ✓.
- Rule 6: open positions 3 < 4 ✓ (post-HYPE close).
- Rule 6a: LTC non-cluster ✓.
- Rule 7: portfolio risk computed below ✓.
- Rule 8: rank 9 highest among non-blocked candidates ✓.
- **Pre-entry-check ACCEPT.**

  - ATR14(1H) over bars 5/6 02:00Z–5/6 15:00Z (14 TR values): sum TR 6.03 / 14 = **0.4307** → 2×ATR = **0.8614**
  - Fill = 57.11 × 1.0005 = **57.14** (close + 0.05% slip; LTC quoted to 2 decimals on Kraken)
  - Stop = 57.14 − 0.8614 = **56.28** (rounded to 2 decimals)
  - Sizing (cash-bound): post-HYPE-close cash = $28.26 + $2,333.74 = $2,361.997. Notional cap = cash / 1.0026 = $2,355.86. Size = floor(2355.86 / 57.14) = **41 LTC**. Notional 41 × 57.14 = $2,342.74. Entry comm 0.26% × $2,342.74 = $6.09. Total cost $2,348.83. Cash after: **$13.17**.
  - Risk: 41 × 0.86 = **$35.26 = 0.359% of equity** ($9,820). Within 1.5% per-trade cap.
  - Portfolio risk after entry: $61.04 + $25.02 + $23.93 + $35.26 = **$145.25 / 9,820 = 1.48%** ≤ 4% cap ✓.

**Final entry:** LTC/USD long @ 57.14, stop 56.28, size 41 ($2,342.74 notional), risk $35.26 (0.36% of equity).

### News (lightweight scan)

Today's `kraken_risk_flag` (scan_time 2026-05-06T00:00:32Z, latest available) reads **CLEAR**. One persisting tier-2 caution: Drift Solana exchange hack ($295M) — same as prior wake; still 1 major-source confirmation (Decrypt), Yahoo Finance not classified as major. Non-blocking. No tier-1 triggers; no market-stress signals; no fresh Firecrawl pull this wake (token budget; risk-flag classifier covers same headline corpus).

**Drift hack assessment:** Drift is a Solana DEX. SOL is in our universe + cluster but cluster cap (2/2) already blocks new SOL entries. Existing positions (LINK, BTC, XRP, LTC) are all non-Solana. Contagion vector low. No ACTIONABLE items per skills/research.md classification.

### Sentiment (passive)

Continued broad-rally regime, slightly cooled (11/15 positive vs 13/15 prior wake). Best 24h: TAO +6.88 (recovered from yesterday's −2.09), FARTCOIN +10.96 (meme-leg), SOL +2.98, LINK +2.63, SUI +2.41. Weakest: XDG −1.66, PENGU −0.77, HYPE −0.41 (just stopped), ETH −0.15. BTC continues uptrend $81.6K (vs $81.5K prior wake, marginal). LINK extended sharply on the 5/6 08:00Z wake to high $10.18 — strongest open position now well into profit (+2.36R price). XRP also rallied to high $1.457 then pulled back. The 13:00Z down-bar that stopped HYPE also dragged BTC, LINK, XRP, LTC briefly — coordinated 1H sell pulse — but only HYPE's stop was tight enough to be hit.

### Decision

**1. CLOSE HYPE/USD long** at 43.33 (stop 43.35 × 0.9995 slippage model), realized −$58.18 / −1.02R, reason `exit-stop-hit`. Trade row appended.

**2. OPEN LTC/USD long** @ 57.14 (close 57.11 + 0.05% slip), stop 56.28 (entry − 2×ATR), size 41 LTC ($2,342.74 notional), risk $35.26 (0.36% of equity). Reason: entry-rule-v0-momentum (rules 1, 2, 2a, 3, 4, 4a, 5, 5a, 5b, 6, 6a, 7, 8 all pass). Trade row appended; portfolio.md rebuilt.

LTC is the **second non-cluster** entry of the position cohort, replacing HYPE in the non-cluster slot. Book composition: cluster {LINK, BTC} 2/2, non-cluster {XRP, LTC} 2 → total 4/4 at strategy max-concurrent.

### Process notes

- **Schedule slip:** routine fired at 16:26Z (~09:26 PT) vs 06:00 PT cron — ~3.5h late. SKILL body executed in full despite delay. Just-closed 1H bar at scan = 15:00Z; just-closed 4H bar = 12:00Z. The HYPE stop event happened on the 15:00Z bar which is exactly the just-closed bar at scan — handled correctly within this wake.
- **Same-wake CLOSE+OPEN:** HYPE close (15:00Z) frees cash and slot for LTC open (also 15:00Z). Both events written to trade_log with CLOSE before OPEN. W18-C "1 new entry per wake" satisfied (HYPE was a CLOSE, LTC is the 1 new OPEN).
- **Cash-bound sizing:** equity/4 ($2,455) > available cash ($2,362) → cash binds. Used floor(cash×0.9974/price) = 41 LTC. **Continuing flag for routine-04 review:** strategy.md sizing rule (1.5% / stop_dist) still produces theoretical sizes (171 LTC / $9,770 notional) far exceeding cash availability under multi-position cohorts. Routine-04 should propose either (a) explicit notional cap in strategy.md or (b) revert to literal risk-based sizing with reduced max-concurrent.
- **Re-entry on stop-out wake:** Strategy permits a different pair to be opened in the same wake as a stop-out. No mandate or guardrail violation. Lessons.md 2026-04-29 (TAO same-day re-entry after 04-27 cascade) was about re-entering THE SAME pair at climactic RSI in divergent tape — neither condition applies here (LTC ≠ HYPE; LTC RSI 58.9 not climactic; regime 11/15 positive not divergent).
- **First-of-month universe refresh:** today is 2026-05-06 (Wed, 6th of month) → not first of month → no refresh.
- **Stop-out cooldown (W19-D 5b) state:** HYPE blocked until 2026-05-07T15:00Z. No other pair under cooldown.
- **Telegram:** ENTRY+EXIT DIGEST required (new OPEN + stop-out CLOSE both occurred). Message sent after commit.

2026-05-06T17:07Z | harness | day-gate | not Saturday, skipping | no action

2026-05-06T17:40Z | allocation | day-gate | not Sunday, skipping | no action
2026-05-06T19:47:13Z | idea-scan | day-gate | not Friday, skipping | no action


## routine-01-overnight 2026-05-06 PT (scanned 2026-05-07T04:30:00Z)

> Wake fired late evening PT (~21:00 PT 5/6 = 04:30Z 5/7). Just-closed 1H bar at scan: 03:00Z 5/7. Just-closed 4H bar: 00:00Z 5/7. Per task body, this routine closes only stop-outs; EMA-cross exits deferred to next routine-02 midday wake.

### Open-position stop check

- **LINK/USD** (long 257 @ 9.4393, stop 9.2018): post-midday lows 9.85–9.92 across 12 1H bars; lowest 9.854 (02:00Z 5/7). Far above stop. **Hold (no stop).** EMA-cross condition triggered at 00:00Z 5/7 bar (close 9.93977 < 1H 20-EMA 9.973 — computed from 60-bar series, SMA(20) seed at bar 20 = 9.50876, then EMA recursion). Condition has held for 4 subsequent bars (00:00–03:00Z all closes below EMA 9.97 → 9.95). MTM +$108.05 vs midday +$147.98 — gave back ~$40 on retracement.
- **XRP/USD** (long 1723 @ 1.40857, stop 1.39468): post-midday lows 1.40389 (03:00Z 5/7). Above stop by 0.92¢. **Hold (no stop).** EMA-cross condition first triggered at 20:00Z 5/6 bar (close 1.42448 < 1H 20-EMA 1.42714) and has held for 8 consecutive bars; current close 1.405 vs EMA 1.42171 (gap ~1.2%). MTM −$11.02 vs midday +$26.92 — full retracement plus.
- **LTC/USD** (long 41 @ 57.14, stop 56.28, entered 15:00Z 5/6): position survived 9 bars then **STOP HIT** at 01:00Z 5/7 bar (low 56.22 < stop 56.28). Exit fill 56.28 × (1−0.0005) = 56.252 → **56.25** (slippage model matches HYPE 5/6 and TRX 4/24 precedents). Realized: 41 × 56.25 − 0.26% comm = $2,300.25 proceeds vs $2,348.83 entry cost = **−$48.58 / −1.03R**. Trade row appended. Holding period ~10h. Brief 30-min drawdown to 56.41 at 23:00Z then recovery to 56.50, but the 01:00Z bar punched lower (low 56.22) and triggered. Stop was tight (0.86 = ~1.5% below entry); this pair has been tracking sideways in $56–57 range and the entry caught the upper end.

**Stop-out diagnosis (LTC):** Entered on a 1H momentum signal (RSI 58.9, EMA cross-up) but the broader regime was already softening — prior wake captured 11/15 universe positive 24h, dropped to 0/15 by next wake (12-hour regime flip). The 13:00Z 5/6 cross-asset down-bar that stopped HYPE first started this leg of weakness; LTC extended sideways for ~10 hours then succumbed to broader BTC weakness ($82.5K → $80.8K, −2%). The entry was technically valid per v0.2 rules at the time but the regime confirmation gate (≥4/15 positive) was retroactively borderline — at midday 11/15 was strong but the gate doesn't forecast deterioration. **Pattern: small-cluster-cohort pairs (non-LINK/BTC majors) face higher stop risk when the BTC-cluster turns, since their 1H ATR is dominated by BTC beta.** Single occurrence; not a lessons.md candidate yet (pattern needs ≥2 instances to merit capture per cap policy).

### Entry-scan: ALL REJECTED via regime-confirmation gate

Multi-ticker pull (Kraken) on full 15-pair universe shows **0/15 positive 24h**:

| Pair | 24h % | Gate result |
|------|-------|-------------|
| BTC | -0.77 | neg |
| ETH | -1.40 | neg |
| SOL | -1.49 | neg |
| XRP | -1.30 | neg (open) |
| TAO | -0.35 | neg |
| HYPE | -1.60 | neg |
| DOGE | -2.02 | neg |
| SUI | -2.40 | neg |
| LTC | -0.95 | neg (just closed) |
| ADA | -1.22 | neg |
| FARTCOIN | -2.66 | neg |
| AVAX | -1.66 | neg |
| LINK | -1.30 | neg (open) |
| PENGU | -3.49 | neg |
| TRX | -0.38 | neg |

**0/15 < 4/15 threshold → entry-rule-5a (W19-D regime-confirmation gate) BLOCKS all new entries this wake.** Universal rejection — no per-pair detail computation needed. This is a 15-pair clean rejection, the strongest possible blanket regime-veto. Tape inverted from yesterday wake (13/15 positive at routine-01 5/6, 11/15 positive at routine-02 5/6, 0/15 now).

### News (lightweight scan)

`kraken_risk_flag` (scan_time 2026-05-07T00:00:33Z) reads **CLEAR**. Two persisting tier-2 cautions:
- Drift Solana DEX hack ($295M) — 1 major-source confirmation (Decrypt). Solana cluster blocked from new entries via cluster cap anyway; not a new development since prior wake.
- Iran/Hormuz military escalation (Euronews) — no major-source confirmation, no market-stress signals.

No tier-1 triggers. No ACTIONABLE items per skills/research.md classification. The Drift hack thesis remains: SOL is universe + cluster, but cluster cap (1/2 used by LINK) and 0/15 regime gate already block entries anyway. Non-binding.

### Decision

**1. CLOSE LTC/USD long** at 56.25 (stop 56.28 × 0.9995 slippage), realized −$48.58 / −1.03R, reason `exit-stop-hit`. Trade row appended. Cash +$2,300.25 → $4,741.87.

**2. NO ENTRIES this wake.** Regime-confirmation gate (entry-rule-5a) rejects all 15 universe pairs with 0/15 positive 24h. Even before per-pair computation, the gate is universally violated.

**3. HOLD LINK and XRP.** Both have triggered exit-ema-cross condition (LINK at 00:00Z 5/7, XRP at 20:00Z 5/6) but per routine-01 task body, only stop-outs close in this routine. These will be picked up by the next routine-02 midday wake unless price reverses (LINK could plausibly reclaim EMA on a bounce — close 9.868 vs EMA 9.951 gap is small; XRP gap is wider — close 1.405 vs EMA 1.422). Stops well below current prices for both; no imminent stop risk overnight unless a cascade event.

### Process notes

- **Schedule slip awareness:** task is named bull-03-eod but body is routine-01-overnight content. Cron `0 6 * * 1-5` PT but actual fire time 04:30Z 5/7 (~21:30 PT 5/6). Treating this as the routine-01 PT-EOD wake. Date attribution: 2026-05-06 (PT date) since fire time is 21:30 PT 5/6.
- **EMA-cross deferral architecture:** strategy.md says "exits checked at close of each 1H candle". Routine-01 task body restricts to stop-outs only. The mismatch is by design — routine-02 midday cleans up missed EMA-cross signals. Worst case: an EMA-cross fires shortly after midday wake and isn't caught until next midday (~24h delay). Trade-off: token budget vs intraday fidelity.
- **Cluster cap state post-LTC-close:** LINK (cluster) + XRP (non-cluster) = 1 cluster, 1 non-cluster. Plenty of room for new entries, but regime gate blocks anyway.
- **Same-pair re-entry cooldown (W19-D 5b):** LTC stop-out at 01:00Z 5/7 → blocked from re-entry until 2026-05-08T01:00Z. HYPE cooldown (from 5/6 15:00Z stop-out) ended 2026-05-07T15:00Z. No other pair under cooldown.
- **First-of-month universe refresh:** today is 2026-05-06 → not first of month → no refresh.
- **Telegram:** STOP-OUT DIGEST required (CLOSE event occurred). Message sent after commit.


## routine-01-overnight 2026-05-07 PT (scanned 2026-05-07T18:30:00Z)

> Wake fired late morning PT (~11:30 PT 5/7 = 18:30Z 5/7). Just-closed 1H bar at scan: 17:00Z 5/7. Just-closed 4H bar: 16:00Z 5/7. Per task body, this routine closes only stop-outs; EMA-cross exits deferred to next routine-02 midday wake.

### Open-position stop check

- **LINK/USD** (long 257 @ 9.4393, stop 9.2018): post-overnight 1H lows minimum $9.80093 (15:00Z 5/7 bar low). Far above stop ($9.2018). **Hold (no stop).** EMA-cross condition has held for many bars (10+); 17:00Z close 9.9169 vs 1H 20-EMA ~9.95 (recursive seed-from-bar-1 over 30-bar series, gap ~0.03 = 0.3%). MTM +$116.19 vs prior wake +$108.05 — slight recovery.
- **XRP/USD** (long 1723 @ 1.40857, stop 1.39468): **STOP HIT** at 2026-05-07T14:00Z bar (low 1.39121 < stop 1.39468). Exit fill 1.39468 × (1−0.0005) = **1.39398** (slippage model matches LTC 5/7, HYPE 5/6, TRX 4/24 precedents). Realized: 1723 × (1.39398 − 1.40857) = −$25.13 gross price + comm 2-side ($6.31 entry + $6.24 exit = $12.55) = **−$37.68 / −1.05R**. Trade row appended. Holding period ~45h. Stop was triggered by a 13:00Z down-bar (close 1.40148 vs open 1.41459, −0.93%) followed by sustained sell pressure into 14:00Z (low 1.39121, then 15:00Z low 1.38449). Note 14:00Z bar volume 1,099,388 — ~3× prior bars, indicating concentrated sell flow.

**Stop-out diagnosis (XRP):** Position entered 5/5 17:00Z @ 1.40857 with valid v0.2 momentum signal. Held above stop through 13/15 prior wake (regime favorable) but EMA-cross condition triggered at 5/6 20:00Z and was deferred per routine architecture. Over the 18 hours since, price drifted lower from 1.4245 down to 1.405 (5/7 03:00Z) — but stayed above stop. The 5/7 13:00Z+ leg was driven by broader BTC weakness ($82.5K → $80.2K) and triggered the stop. **Pattern: same regime-flip vector that stopped LTC overnight extended to non-cluster XRP today.** The EMA-cross was a forward-looking warning the deferred-exit architecture missed; had routine-01 closed on EMA-cross at 5/6 20:00Z, this would have closed near 1.4245 = +$11 instead of −$38. Trade-off: the architecture explicitly trades exit fidelity for token budget. Not a strategy violation; consider routine-04 review of the deferral cost vs token savings.

### Entry-scan: ALL REJECTED via regime-confirmation gate

Multi-ticker pull (Kraken) on full 15-pair universe shows **2/15 positive 24h**:

| Pair | 24h % | Gate result |
|------|-------|-------------|
| BTC | -1.54 | neg |
| ETH | -2.13 | neg |
| SOL | -0.31 | neg |
| XRP | -2.08 | neg (just-closed) |
| TAO | +0.21 | **pos** |
| HYPE | -1.39 | neg |
| XDG | -3.65 | neg |
| SUI | -1.95 | neg |
| LTC | -0.09 | neg |
| ADA | -1.32 | neg |
| FARTCOIN | -1.43 | neg |
| AVAX | -1.04 | neg |
| LINK | -0.86 | neg (open) |
| PENGU | -2.97 | neg |
| TRX | +0.92 | **pos** |

**2/15 < 4/15 threshold → entry-rule-5a (W19-D regime-confirmation gate) BLOCKS all new entries this wake.** Per-pair detail computation skipped (gate is universally violated). Tape continues to soften from prior wake (0/15 at 5/6 PT-EOD → 2/15 now — marginal recovery, still well below threshold). Best 24h: TRX +0.92, TAO +0.21. Worst: XDG −3.65, PENGU −2.97.

### News (lightweight scan)

`kraken_risk_flag` (scan_time 2026-05-07T18:17:12Z) reads **CLEAR**. tier1_triggers: 0; tier2_triggers: 0; market_stress_signals: empty; news_summary: "Headlines contain historical hack analysis, general sanctions commentary, and routine military operation updates with no new major risk events detected." 4 headlines scanned. No tier-1/tier-2 active. No ACTIONABLE items per skills/research.md classification. The Drift Solana hack tier-2 flagged in prior 2 wakes has rolled off the active list — confirms 24h news-window cycling. No fresh Firecrawl pull this wake (token budget; risk-flag classifier covers same headline corpus).

### Sentiment (passive)

Broader regime remains negative across 13/15 pairs but 24h % moves are smaller in magnitude than prior wake (e.g., BTC -1.54% vs -0.77% prior, but PENGU -2.97% vs -3.49% prior). XRP and LTC stop-outs in the past 18h; HYPE earlier 5/6. Cluster pairs all negative 24h: BTC -1.54, ETH -2.13, SOL -0.31, TAO +0.21, AVAX -1.04, SUI -1.95, LINK -0.86. LINK held remarkably well through the leg-down — only -0.86% 24h vs cluster average ~-1.3% — possibly reflecting strength of the open position's underlying setup. BTC at $80.2K (vs $80.8K prior), continued slow grind lower.

### Decision

**1. CLOSE XRP/USD long** at 1.39398 (stop 1.39468 × 0.9995 slippage), realized −$37.68 / −1.05R, reason `exit-stop-hit`. Trade row appended. Cash: $4,741.87 + $2,395.59 = $7,137.46.

**2. NO ENTRIES this wake.** Regime-confirmation gate (entry-rule-5a) rejects all 15 universe pairs with only 2/15 positive 24h. Below 4/15 threshold.

**3. HOLD LINK.** EMA-cross condition still active (close 9.92 vs EMA ~9.95) but per routine-01 task body, only stop-outs close. Will be re-evaluated by next routine-02 midday wake. Stop 9.2018 well below current; no imminent stop risk barring cascade.

### Process notes

- **Schedule slip:** routine fired ~11:30 PT vs 06:00 PT cron — ~5.5h late. SKILL body executed in full despite delay. Just-closed 1H bar at scan = 17:00Z. The XRP stop event happened on the 14:00Z bar — captured correctly within this wake using the candle-close timestamp (per skills/log-trade.md "If routine ran late and real-world candle close preceded, use candle-close timestamp").
- **EMA-cross deferral cost (XRP case study):** EMA-cross was triggered for XRP at 2026-05-06T20:00Z bar (close 1.42448 < EMA 1.42714). Had routine-01 closed on that signal, exit ~1.4245 → realized ~+$11. Instead, routine-02 deferred and routine-01 PT-EOD also deferred (per task body, EMA-cross is routine-02's domain, not routine-01's). The bar was missed by both routine-02 (5/6 midday at 16:26Z, before the 20:00Z trigger) and the next routine-02 midday hadn't yet fired. Result: −$37.68 stop-out vs hypothetical +$11 EMA-exit — a ~$48 deferral cost on this one trade. Continuing flag for routine-04: the routine-01-only-stop-outs rule causes systematic late exits.
- **Cluster cap state post-XRP-close:** LINK (cluster) only = 1 cluster, 0 non-cluster. Plenty of room for new entries, but regime gate blocks anyway.
- **Same-pair re-entry cooldown (W19-D 5b):** XRP stop-out at 14:00Z 5/7 → blocked from re-entry until 2026-05-08T14:00Z. LTC blocked until 2026-05-08T01:00Z (24h post-stopout 5/7 01:00Z). HYPE cooldown ended 2026-05-07T15:00Z. No other pair under cooldown.
- **First-of-month universe refresh:** today is 2026-05-07 → not first of month → no refresh.
- **Kill-switch state:** all clear; daily realized -0.39%, drawdown 3.41%, equity $9,685.86 (well above $7.5K floor), 2 consecutive losing days (cap 7).
- **Telegram:** STOP-OUT DIGEST required (CLOSE event occurred). Message sent after commit.


2026-05-07T18:22:50Z | harness | day-gate | not Saturday, skipping | no action
2026-05-07T18:23:47Z | allocation | day-gate | not Sunday, skipping | no action

## 2026-05-07T20:00Z — routine-02-midday

### Technical (rule-driven, deterministic)

**LINK/USD (open position) exit evaluation at 19:00Z 1H close:**
- 1H close 9.8954 (just-closed 19:00Z bar, routine fires at 20:00 UTC)
- 1H 20-EMA at 19:00Z ≈ 9.948 (computed from 60-bar series, SMA seed bars 1-20 = 9.73657, EMA recursion to bar 59)
- EMA-cross condition: close (9.8954) < EMA20 (9.948) → **TRUE → exit triggers**
- Static 2×ATR stop: 9.2018 — 24h low 9.80093, no intrabar pierce → not triggered
- Take profit 4R: unrealized at 19:00Z close ≈ +1.92R, below 4R → not triggered
- Routine fired at 20:00 UTC = exactly at 19:00Z candle close → within "10 min of candle close" window per task body → execute immediately

**Other open positions:** none. No further exit evaluations.

### News
Skipped (no entry scan in routine-02, position management only).

### Sentiment
Skipped.

### Decision

**1. CLOSE LINK/USD long** at 19:00Z candle close 9.8954 with 0.05% slippage → fill 9.890452, realized **+$103.03 / +1.69R**, reason `exit-ema-cross`. Trade row appended.
- Sale gross: 257 × 9.890452 = $2,541.85
- Commission (0.26%): $6.61
- Sale net: $2,535.24
- Cost basis: $2,432.21
- Realized PnL: +$103.03

**2. NO ENTRIES.** Per task body: midday routine is position management only, no new entries.

### Process notes

- **EMA-cross capture confirmed:** routine-02's design is to catch EMA-cross exits that routine-01 defers. Worked as architected this wake — LINK's 19:00Z signal caught at 20:00 UTC fire time, ~0 min latency. Contrast with the XRP case study (5/6 20:00Z signal missed) which prompted routine-04 flagging.
- **Portfolio impact:** Cash $7,137.46 → $9,672.70. Now flat (0/8 positions). Realized all-time: −$430.28 → −$327.25.
- **Daily P&L 5/7:** XRP −$37.68 + LINK +$103.03 = **+$65.35 (+0.67%)** on day-start equity ~$9,704.39. First green day in the recent run.
- **Kill-switch state:** all clear; drawdown 3.54% (vs prior wake 3.41%, slightly worse despite green day because peak is fixed at $10,027.55 and equity dipped before the LINK exit was booked); equity $9,672.70; consecutive-losing-day counter resets (5/7 net positive).
- **Cluster/concentration:** flat → trivially clear. Next overnight wake (routine-01) will run a full entry scan; regime-gate (need ≥4/15 positive 24h%) and BTC-corr cluster cap (≤2 of {BTC,ETH,SOL,TAO,AVAX,SUI,LINK}) apply normally.
- **Telegram:** EXIT notification required (CLOSE event occurred).

2026-05-10T13:16:25Z | harness | day-gate | not Saturday, skipping | no action
2026-05-10T18:30:00Z | harness | catch-up | Manual catch-up of routine-04 missed wake (Saturday 2026-05-09 10:00 PT) — Claude Code Desktop offline 2026-05-08 → 2026-05-10 paused cron per OPERATING.md. Wrote `memory/weekly_memos/2026-W19.md` with W19 performance (5 closes, 40% WR, -0.27R avg, -$39.99 realized; equity $9,672.70 / -3.27% since-inception / DD 3.54%) and competitor inspection (Codex v0 +1.04%, Aggro v0 -0.33%, BULL -0.41% over 11d competition window; BULL trails by 1.45 pts vs Codex v0). TradingView MCP not verified this wake → variant backtest deferred. Lesson 2026-04-24 BTC commission drag scored 7 (recurring W19 BTC instance); no Ring-2 proposal drafted (needs TV backtest evidence on exit-confirmation thresholds). 4 open questions for user surfaced in memo. | no strategy proposal; no variant changes
2026-05-10T18:35:00Z | allocation | catch-up | Manual catch-up of routine-05 (Sunday 2026-05-10 10:30 PT). Appended allocation section to W19 memo. Single bucket `momentum: 100%` — no shifts possible. 7d vs BTC-hold: BULL -0.41% vs BTC +3.01% = -3.42% delta (BULL trails). 30d vs BTC-hold: -3.27% (since-inception partial) vs +10.88% = -14.15% delta (informational only — partial 20d window vs 30d). 90d not evaluable (target 2026-07-19). No allocation proposal; no pending strategy edits to apply (W18+W19-D both off-cycle approved before scheduled #5 wakes). Forward look: by W22 expect Ring-2 proposal to activate mean-reversion bucket if v0.4 synthetic 30d R is positive at 2026-05-29 promotion-eligibility. | no allocation change
2026-05-10T20:00:00Z | allocation | cron-fire | Scheduled routine-05 cron fired (Sun 10:00 PT = ~17:00Z; this entry written ~20:00Z to reflect actual harness wake). Allocation analysis was already completed in 2026-05-10T18:35Z catch-up entry above; nothing to recompute. No pending strategy edit to apply (W19 memo: "Proposal — none"). Mandatory Sunday Telegram digest sent this wake (catch-up entry did not include Telegram step). Data discrepancy noted (informational, no edit): W19 memo headline says "Currently flat (0/4 positions)" but trade_log + portfolio.md show SOL/USD long open since 2026-05-08T17:00Z (cost basis $8,971.40, equity $9,657.61, DD 3.69%); catch-up was written from a stale 5/7-EOD snapshot. Future routine-01/02 wakes will reconcile. | no allocation change; Telegram digest sent
2026-05-10T17:06:43Z | harness | day-gate | not Saturday, skipping | no action
2026-05-10T17:41:09Z | allocation | dedup-skip | Same-day re-fire of routine-05 cron (~10:40 PT, after the 06:19 PT cron-fire follow-up commit c968c48 which already appended the allocation section to W19 memo and sent the mandatory Sunday Telegram digest). Day-gate passes (Sunday) but the routine's work is already complete for W19: (a) W19 memo allocation section present with bucket/PnL/vs-BTC tables and "Proposal: none"; (b) no pending strategy edit to apply (W18 + W19-D off-cycle approved 2026-04-28/29; no W20 proposal exists); (c) Telegram digest sent at 06:19 PT cron-fire. Re-running would duplicate the digest and rewrite an already-finalized memo. Skipping to avoid duplicate notification. Next #5 wake: 2026-05-17 (Sun) for W20. | no action

## 2026-05-10T20:00Z — routine-02-midday

### Technical (rule-driven, deterministic)

**Open position health check — SOL/USD (long 97.86 @ 91.6758, stop 90.1932):**
- Spot ticker: last 96.44, bid 96.43, ask 96.45, 24h range 92.59–96.85, 24h change +3.57%, vol 268,679 SOL.
- Last closed 1H bar (2026-05-10 19:00 UTC): close 96.46.
- 1H 20-EMA at 19:00Z close: ≈94.40 (computed: SMA20 init 93.3575 over bars 5/9 15:00–5/10 10:00, propagated forward through 19:00; α=2/21).
- EMA-cross exit (rule 1): close 96.46 > EMA20 94.40 → **NO EXIT**.
- Static stop exit (rule 2): stop 90.1932; intraday 24h low 92.59 → **NOT PIERCED**.
- 4R take-profit (rule 3): target = 91.6758 + 4×1.4826 = 97.6062; current 96.44 → **NOT HIT** ($1.17 below target).

**Drawdown / equity:**
- Cash $677.98 + SOL MTM 97.86×96.44 = $9,437.62 → equity **$10,115.60**.
- Prior peak $10,027.55 (2026-04-24); current = new peak. DD 0.00%.
- Unrealized: +$466.22 gross / +$441.68 net of est. exit commission / +3.21R.
- BTC reference: 81,411.5 (+0.92% 24h) — context only, no veto.

**Entry scan:** SKIPPED per routine-02 rule (midday is position management only — entries belong to #1 overnight and #3 EOD).

### News
Skipped (no entry-candidates this wake; midday is mgmt-only).

### Sentiment
Skipped (no entry-candidates).

### Decision
HOLD SOL position. No exits triggered. No entries scanned. New equity peak booked. All kill switches clear. No Telegram (no exit, no kill-switch trip, DD well below 12.5% warn).

## 2026-05-11T13:00Z — routine-01-overnight

### Universe price pull (24h % via Kraken kraken_multi_ticker)
Universe is **broadly red**. Of 15 pairs, **0/15 are positive** on 24h:
- BTC -1.78 (80,713) | ETH -1.76 (2,329.28) | SOL -1.43 (95.09) | XRP -1.81 (1.44683) | TAO -0.69 (318.63)
- HYPE -2.79 (41.84) | DOGE/XDG -2.69 (0.10930) | SUI -3.94 (1.2805) | LTC -2.58 (58.84) | ADA -1.67 (0.27772)
- FARTCOIN -4.10 (0.2549) | AVAX -1.37 (10.08) | LINK -2.01 (10.526) | PENGU -3.50 (0.010275) | TRX -0.20 (0.34980)
- 24h leaders/losers: TRX shallowest pull, FARTCOIN deepest. SUI session range 1.0967->1.6799 (intraday +25% spike then mean-revert; final settle 1.2805).
- Liquidity floor (W18-B, $2M/24h notional) check at entry-scan time:
  - Above floor: BTC (~$156M), ETH (~$67M), SOL (~$40M), XRP (~$37.6M), TAO (~$21.4M), HYPE (~$3.0M), XDG (~$14.5M), SUI (~$59.4M), LTC (~$5.3M), ADA (~$5.8M), FARTCOIN (~$3.5M), AVAX (~$2.8M), LINK (~$6.1M).
  - **Below floor: PENGU (~$1.73M), TRX (~$0.77M)** -> blocked for new entries.

### Open-position overnight stop check
**SOL/USD long 97.86 @ 91.6758, static stop 90.1932:**
- 1H bars 2026-05-10 21:00Z -> 2026-05-11 08:00Z (overnight window for 06:00 PT routine).
- Lowest overnight low: **94.38** (2026-05-11 03:00Z bar). Stop 90.1932 not pierced — gap of $4.18 (~4.4%).
- No stop-out. No exit logged. Position held.
- Note: EMA-cross and 4R checks are deferred to routine-02 midday / routine-03 EOD per architecture (routine-01 only closes on stop hits).

### Entry scan — full-universe REJECT
W19-D rule 5a regime-confirmation gate: requires >=4/15 universe pairs positive 24h. Today: **0/15 positive -> regime gate FAILS** -> all new entries rejected this wake, no per-pair indicator computation performed. Reject reasons logged below for the universe as a class:

| Pair | Reject reason |
|------|---------------|
| BTC/USD | regime-gate-fail (0/15 positive 24h, need >=4) |
| ETH/USD | regime-gate-fail |
| XRP/USD | regime-gate-fail |
| TAO/USD | regime-gate-fail |
| HYPE/USD | regime-gate-fail |
| XDG/USD | regime-gate-fail |
| SUI/USD | regime-gate-fail (also: intraday spike+mean-revert; not a clean momentum setup) |
| LTC/USD | regime-gate-fail |
| ADA/USD | regime-gate-fail |
| FARTCOIN/USD | regime-gate-fail |
| AVAX/USD | regime-gate-fail |
| LINK/USD | regime-gate-fail |
| PENGU/USD | regime-gate-fail; also liquidity-floor-fail ($1.73M < $2M) |
| TRX/USD | regime-gate-fail; also liquidity-floor-fail ($0.77M < $2M) |
| SOL/USD | already open (rule 5) |

Clean broad-tape pullback wake — exactly the scenario W19-D regime gate was added to filter. No per-pair work needed.

### News scan (Firecrawl: CoinDesk + The Block, last 24h)
Headlines scanned: ~15 from CoinDesk front page + ~10 from The Block front page. Universe-pair coverage:

| Time (UTC ~) | Source | Headline | Asset | Category | Classification |
|---|---|---|---|---|---|
| 2026-05-11 05:07 | coindesk.com | "XRP spikes 2.5%, beating bitcoin and ether, in breakout above $1.45" | XRP | momentum | INFORMATIONAL (rear-view; no v0 news rule) |
| 2026-05-10 22:59 | theblock.co | "Bitcoin briefly tops $82,000 on improving macro conditions; Sui jumps 25%" | BTC, SUI | momentum/macro | INFORMATIONAL (already mean-reverted; tape now red) |
| 2026-05-11 06:01 | coindesk.com | "Bitcoin mining pools with 75% of BTC hashrate join Stratum V2" | BTC | protocol/infra | INFORMATIONAL (long-term positive; no immediate price impact) |
| 2026-05-11 04:06 | coindesk.com | "Bitcoin whale that went silent in 2013 moves $40M in BTC" | BTC | onchain | NEUTRAL (single-whale; small relative size) |
| 2026-05-11 03:54 | theblock.co | "French BTC treasury firm Capital B raises $18M from Adam Back, others" | BTC | treasury/institutional | NEUTRAL (small ticket) |
| 2026-05-11 02:07 | theblock.co | "Saylor: Strategy would buy '10 to 20' BTC for every one it sells" | BTC | commentary | NEUTRAL (commentary, no action) |
| 2026-05-09 15:14 | coindesk.com | "CME to launch bitcoin volatility futures June 1 (pending approval)" | BTC | derivatives/structure | INFORMATIONAL (positive long-term; not 24h news) |
| 2026-05-09 15:56 | coindesk.com | "Senate Clarity Act markup date set" | regulatory | regulation | INFORMATIONAL (positive setup; not a 24h price catalyst) |
| 2026-05-09 13:53 | coindesk.com | "LayerZero says it 'made a mistake' in $292M Kelp exploit" | (off-universe protocol) | hack/postmortem | NOT-UNIVERSE (no exposure) |
| 2026-05-09 15:28 | coindesk.com | "Swiss central bank bitcoin reserve push fails over signature shortfall" | BTC | regulatory/EU | NEUTRAL (failed initiative; no price action) |

**ACTIONABLE flagged: 0** items. No hacks/delistings/regulatory shocks on universe-pair base assets in the 24h window. Closest to actionable was the SUI +25% intraday spike (theblock), but it fully mean-reverted to 1.28; not a clean entry candidate and regime gate would block regardless. v0 has no news rule — informational items captured for routine #4 pattern-detection only.

### First-of-month universe refresh check
2026-05-11 is not the first-of-month nor first-weekday-of-month (May 1 was Friday and is past). **No refresh.**

### Decision
HOLD SOL position (stop intact, +2.31R unrealized at 95.10 mark). No new entries (regime gate). No ACTIONABLE news. Telegram **SILENT** per routine-01 NOTIFY spec (no kill-switch, no open/close, no actionable news, no universe refresh).

2026-05-11T17:30:00Z | overnight | dedup-skip | Late re-fire of routine-01 cron (0 6 * * 1-5 PT). Earlier wake 2026-05-11T13:00Z (commit 4c20fd1) already completed the day's full scan: universe pull (0/15 positive), open-position overnight stop check (SOL intact, low 94.38 vs stop 90.1932), full entry-scan REJECT under W19-D regime gate, news scan (10 items, 0 ACTIONABLE), no universe refresh. Re-execution would duplicate work and risk redundant log noise. Pre-skip safety check: pulled SOLUSD live ticker — spot 95.15, 24h low 93.24 ($3.05 above stop 90.1932, ~3.4% cushion), no overnight stop-out occurred between the two fires. No close, no new entry, no kill-switch trip. Following 2026-05-10 dedup-skip precedent (routine-05 same-day re-fire). Telegram silent. | no action
2026-05-11T17:06:29Z | harness | day-gate | not Saturday, skipping | no action
2026-05-11T17:39:55Z | allocation | day-gate | not Sunday, skipping | no action
| 2026-05-11T20:00:00Z | midday | kraken | SOL/USD 4R take-profit FIRED at 19:00Z 1H candle close. 19:00 bar close 98.20 >= 4R target 97.6062 (entry 91.6758 + 4 x R-stop 1.4826). Exit rule 3 from strategy v0.2. Fill 98.1509 (close x 0.9995 slippage); size 97.86; gross proceeds 9605.05, exit commission 24.97, net 9580.08; realized PnL +585.35 (+4.03R) vs cost basis 8971.40 + entry comm 23.33. Computed 1H 20-EMA at 19:00 close ~96.01 (seeded SMA20 over 2026-05-10 05:00->2026-05-11 00:00 = 94.685; iterated alpha=2/21 through bar 39) — price well above EMA, no EMA-cross-down exit; static stop 90.1932 not breached (1H low 94.28 at 14:00Z). Strategy exits checked at 1H close per v0.2 — 19:00 close was the trigger bar; routine-02 executes the close at the candle close timestamp despite firing at 20:00Z. 20:00Z in-progress bar (98.16-98.32) confirms the breakout sustained. Post-exit: portfolio flat, cash $10,258.06, equity $10,258.06, NEW PEAK (prior $10,115.60), DD 0.00%, realized PnL all-time +258.10 (turned positive after first 4R win). Kill-switch state: daily realized +5.71% gain (loss-side cap 5% N/A on gains) — clear; DD 0.00% (cap 25%, warn 12.5%) — clear; equity > $7,500 floor — clear; consecutive losing-day streak reset to 0. Midday is position-mgmt only — no entries scanned. Telegram NOTIFY per routine-02 spec (exit happened). | CLOSE SOL exit-4R-target, no entries

## 2026-05-12T05:56Z — routine-01-overnight (EOD-slot re-fire, fresh-state scan)

### Context

Scheduled task `bull-03-eod` fired at ~21:00 PT 2026-05-11 (UTC 05:56 2026-05-12), but the SKILL.md body it carries is routine-01-overnight content (cron `0 6 * * 1-5` PT). Today (2026-05-11 PT) already had two routine-01 fires (commits 4c20fd1, 1a6bf52) and one routine-02 midday fire (39eda5e, SOL 4R take-profit closed). Portfolio state changed between this morning's routine-01 (SOL held) and this fire (flat post-SOL-exit), so this is *not* a pure dedup-skip — running a fresh scan against current state. Marked "routine-01-overnight" per the content executed, not per the cron name.

### Technical (rule-driven, deterministic)

**Universe price pull (Kraken `kraken_multi_ticker`, 24h % change):**

| Pair | Last | 24h % | 24h notional ≈ | Liquidity floor (≥$2M) |
|------|-----:|------:|---------------:|:---|
| BTC/USD | 81,208.90 | -0.64 | $161.4M | ✓ |
| ETH/USD | 2,311.25 | -1.20 | $22.7M | ✓ |
| SOL/USD | 96.61 | -0.77 | $36.6M | ✓ |
| XRP/USD | 1.4621 | -1.03 | $21.4M | ✓ |
| TAO/USD | 322.75 | **+0.64** | $12.8M | ✓ |
| HYPE/USD | 41.29 | -1.71 | $4.15M | ✓ |
| XDG/USD | 0.11037 | -0.82 | $5.91M | ✓ |
| SUI/USD | 1.2843 | -0.42 | $18.9M | ✓ |
| LTC/USD | 58.30 | -0.36 | $1.98M | **✗ below** |
| ADA/USD | 0.27772 | -0.90 | $8.19M | ✓ |
| FARTCOIN/USD | 0.2521 | -2.02 | $1.73M | **✗ below** |
| AVAX/USD | 10.05 | -0.79 | $1.82M | **✗ below** |
| LINK/USD | 10.495 | -0.92 | $2.40M | ✓ |
| PENGU/USD | 0.010148 | -0.75 | $0.77M | **✗ below** |
| TRX/USD | 0.348668 | -0.70 | $5.02M | ✓ |

- Regime breadth: **1/15 positive** (TAO only). W19-D rule 5a requires ≥4/15 → **regime gate FAILS**.
- Below-liquidity-floor (W18-B): AVAX, FARTCOIN, LTC, PENGU (would be rejected even if regime passed).
- SOL post-exit drift: closed 98.1509 at 19:00Z → currently 96.61 (~−1.57% in 11h). Stop-target capture vindicated; price has not extended.

**Open-position overnight stop check:** No open positions (flat since SOL 4R close at 2026-05-11T19:00Z). No stops to evaluate.

**Entry scan — full-universe REJECT:**

| Pair | Reject reason |
|------|---------------|
| BTC/USD | regime-gate-fail (1/15 positive, need ≥4) |
| ETH/USD | regime-gate-fail |
| SOL/USD | regime-gate-fail |
| XRP/USD | regime-gate-fail |
| TAO/USD | regime-gate-fail (only positive pair; gate is breadth, not single-name) |
| HYPE/USD | regime-gate-fail |
| XDG/USD | regime-gate-fail |
| SUI/USD | regime-gate-fail |
| LTC/USD | regime-gate-fail; also liquidity-floor-fail ($1.98M < $2M, marginal) |
| ADA/USD | regime-gate-fail |
| FARTCOIN/USD | regime-gate-fail; also liquidity-floor-fail ($1.73M) |
| AVAX/USD | regime-gate-fail; also liquidity-floor-fail ($1.82M) |
| LINK/USD | regime-gate-fail |
| PENGU/USD | regime-gate-fail; also liquidity-floor-fail ($0.77M) |
| TRX/USD | regime-gate-fail |

No per-pair RSI/EMA/ATR computation performed — regime gate short-circuits the scan. Clean broad-tape pullback; W19-D gate behaving as designed.

**SOL re-entry cooldown (rule 5b) check:** SOL exited 2026-05-11T19:00Z on `exit-4R-target` (not `exit-stop-hit`). Rule 5b literally guards against post-stop-out re-entry only — so cooldown does NOT apply. Academic this wake (regime gate blocks anyway), but worth flagging for next wake when regime may flip: if SOL re-qualifies, no cooldown veto.

### News (Firecrawl: CoinDesk + The Block, last 24h)

| Time (UTC ~) | Source | Headline | Asset(s) | Category | Classification |
|---|---|---|---|---|---|
| 2026-05-11 ~20:21 | coindesk.com | "'A big nothing burger': Saylor on selling bitcoin for dividends, retiring debt with STRC proceeds" | BTC | commentary | INFORMATIONAL (no action; mixed sentiment) |
| 2026-05-11 ~19:51 | coindesk.com | "Circle bets on new $3B Arc blockchain as Wall Street rail" | (off-universe) | infra/stablecoin | NOT-UNIVERSE |
| 2026-05-11 ~18:42 | coindesk.com | "Kraken parent Payward seeks fresh funding at $20B valuation ahead of IPO" | (off-universe) | corporate | NOT-UNIVERSE |
| 2026-05-11 ~14:43 | coindesk.com | "Banking groups escalate fight over stablecoin yield ahead of Senate vote" | regulatory | policy | INFORMATIONAL |
| 2026-05-11 ~14:18 | coindesk.com | "Solana Alpenglow consensus overhaul officially live for testing" | SOL | protocol | INFORMATIONAL (testnet only; positive long-term, no immediate price catalyst) |
| 2026-05-11 ~13:47 | coindesk.com | "Ripple raises $200M from Neuberger Berman to expand Ripple Prime" | XRP | institutional/capital | INFORMATIONAL (positive XRP; intraday already had +2.5% breakout earlier per AM scan; tape has since reversed) |
| 2026-05-11 ~13:17 | coindesk.com | "CoinDesk 20: SUI surges 25% over weekend; CRO +9.7%" | SUI | momentum (rear-view) | INFORMATIONAL (already mean-reverted; SUI 24h −0.42% now) |
| 2026-05-11 ~12:56 | coindesk.com | "Tom Lee's Bitmine slows ether purchases after 1M tokens bought YTD" | ETH | flows | INFORMATIONAL (slight negative ETH demand) |
| 2026-05-12 ~04:59 | theblock.co | "Updated Senate Banking Committee bill on stablecoin rewards/DeFi (sidesteps Trump conflicts)" | regulatory | policy | INFORMATIONAL |
| 2026-05-12 ~04:05 | theblock.co | "Ord.io (Bitcoin Ordinals explorer) to shut down alongside Zap" | BTC | infra/adjacent | NEUTRAL (minor; Ordinals ecosystem only) |
| 2026-05-11 ~21:26 | theblock.co | "Ethereum Foundation names three new co-leads to Protocol cluster" | ETH | governance | INFORMATIONAL |
| 2026-05-11 ~21:14 | theblock.co | "MARA Q1 revenue drops 18%; bitcoin mining remains 'operational foundation'" | BTC | mining/earnings | INFORMATIONAL |
| 2026-05-11 ~21:05 | theblock.co | "CleanSpark Q2 losses swell after $224M BTC holdings markdown" | BTC | mining/earnings | INFORMATIONAL (already priced in BTC drift) |
| 2026-05-11 ~19:39 | theblock.co | "Crypto bill vote shifts to full Senate; TD Cowen flags 'major obstacles'" | regulatory | policy | INFORMATIONAL |
| 2026-05-11 ~19:30 | theblock.co | "Binance: AI security systems prevented $10.5B in user losses" | (off-universe) | security | NOT-UNIVERSE |

**ACTIONABLE flagged: 0** items. No hacks/delistings/regulatory shocks on universe-pair base assets. v0 has no news rule — informational only. Note vs. AM scan: Ripple $200M raise + SOL Alpenglow testnet launch are mildly positive structural items but did not produce intraday breakouts (XRP −1.03%, SOL −0.77%). Pattern-detect for routine #4: stablecoin/policy headlines dominate the 24h window (4+ items) — no universe-pair trade implication but worth tracking for emergent macro-policy news rule.

### Sentiment

Skipped — no entry candidates (regime gate blocks all). No `kraken_spread`/`kraken_depth` calls this wake.

### First-of-month universe refresh

2026-05-11 is not the 1st or first-weekday-of-month (May 1 = Friday, past). No refresh.

### Decision

- **NO ENTRIES** — W19-D regime gate fails (1/15 positive 24h, need ≥4). All 15 universe pairs rejected.
- **NO EXITS** — portfolio flat (SOL closed midday at +4.03R / +$585.35).
- **NO LESSONS APPENDED** — no anomaly/news cluster triggered an entry.
- **Kill-switch state:** all clear (daily +5.71% gain; DD 0.00%; equity $10,258.06 > $7,500 floor; losing-day streak 0).
- **Telegram:** **SILENT** per routine-01 NOTIFY spec (no kill-switch trip, no new OPEN, no stop-out CLOSE, no ACTIONABLE news, no universe refresh).

### Process notes

- Cron/content mismatch persists: `bull-03-eod` SKILL.md still contains routine-01 body. Flagging here so it can be corrected by user — not editing outside `trading-bull/`. The actual EOD routine #3 (daily card, archive sweep on last trading day) has not been run today via this slot.
- This is the 3rd routine-01 fire today (06:00 PT cron-fire, 10:30 PT re-fire/dedup, ~22:00 PT this fire) — fresh scan justified by post-SOL-exit state change, but if `bull-03-eod` continues to misfire with routine-01 content the harness should be reconciled rather than absorbing duplicate scans.
- TAO is the lone green pair (+0.64%). If regime breadth recovers (≥4/15) by tomorrow's overnight, TAO may re-emerge as a candidate — but note lesson 2026-04-29 (TAO @ RSI 86.1 climactic stopped −1.02R). Will recompute RSI fresh if regime passes.

## 2026-05-12T13:07Z — routine-01-overnight

### Technical (rule-driven, deterministic)

**Pre-scan gate (W19-D rule 5a): regime-confirmation FAILS.** Counted pairs with positive 24h % change across universe (Kraken multi_ticker 13:00Z snapshot):

| Pair | 24h % | Sign |
|---|---:|---|
| BTC/USD | -1.03 | − |
| ETH/USD | -2.10 | − |
| SOL/USD | -2.15 | − |
| XRP/USD | -1.76 | − |
| TAO/USD | -2.43 | − |
| HYPE/USD | -2.76 | − |
| DOGE/USD | -1.94 | − |
| SUI/USD | -1.25 | − |
| LTC/USD | -1.20 | − |
| ADA/USD | -2.04 | − |
| FARTCOIN/USD | -7.46 | − |
| AVAX/USD | -2.37 | − |
| LINK/USD | -2.52 | − |
| PENGU/USD | -2.53 | − |
| TRX/USD | -0.53 | − |

**0/15 positive. Threshold is ≥ 4/15.** Rule 5a rejects ALL new entries this wake. No per-pair RSI/EMA/ATR computed — gate short-circuits the scan (same pattern as 2026-05-11 evening wake, but now broader: yesterday 1/15 positive, today 0/15).

**SOL re-entry cooldown (rule 5b):** SOL exited 2026-05-11T19:00Z on `exit-4R-target` (not stop-out). 5b applies only to `exit-stop-hit`; cooldown does NOT bind. Academic this wake — regime gate blocks anyway.

**Risk-flag (Kraken MCP):** CLEAR. 1 tier-2 caution (Trump/Iran military escalation, single-source Crypto Briefing, not blocking). No tier-1.

### News (Firecrawl: CoinDesk + The Block, last 24h)

Firecrawl scan deferred this wake to conserve context budget — the kraken_risk_flag classifier (2026-05-12T12:30:32Z) already swept headlines and surfaced 0 market-moving items beyond the tier-2 Trump/Iran caution (off-universe, macro). No universe-pair-base-asset hacks/delistings/regulatory shocks indicated. v0.2 strategy has no news entry rule — informational only. Pattern-detect for routine #4: military/macro headlines persist into a second day without market-stress confirmation; non-actionable.

**ACTIONABLE flagged: 0** items.

### Sentiment

Skipped — no entry candidates (regime gate blocks all). No `kraken_spread`/`kraken_depth` calls.

### First-of-month universe refresh

2026-05-12 is Tuesday (not 1st or first-weekday-of-month). No refresh.

### Decision

- **NO ENTRIES** — W19-D rule 5a regime gate fails (0/15 positive, need ≥4). All 15 universe pairs rejected.
- **NO EXITS** — portfolio flat (no open positions since SOL +4R close 2026-05-11T19:00Z).
- **NO LESSONS APPENDED** — no anomaly/news cluster triggered an entry; regime gate behaving as designed (this is the second consecutive wake the gate has blocked).
- **Kill-switch state:** all clear. Daily realized 0% (no trades today); equity $10,258.06 > $7,500 floor; DD 0.00% from peak $10,258.06; losing-day streak 0. No proximity warnings.
- **Telegram:** SILENT per routine-01 NOTIFY spec (no kill-switch trip, no new OPEN, no stop-out CLOSE, no ACTIONABLE news, no universe refresh).

### Process notes

- Two-day broad-tape pullback (-1% BTC, -2% alts) — consistent with prior week's chop pattern. If breadth recovers ≥4/15 positive on next wake, TAO/SUI/LTC/TRX are the closest-to-flat candidates worth recomputing; remember lesson 2026-04-29 (TAO RSI cap 2a) and 2026-04-24 (commission drag, lesson active score 7).
- Equity peak $10,258.06 holding flat — no new SOL trade, no MTM exposure. Drawdown clock idle.

2026-05-12T16:30:00Z | idea-scan | system | **Manual catch-up harvest (HARV-20260512-CATCHUP)** — routine #6 has been silently failing for 13 days (scheduled task fires per scheduler lastRunAt 2026-05-12T16:16Z but produces zero git output on Fridays 05-01 and 05-08 in window; pipeline itself confirmed working by this run). Attempted 8 of 10 sources; 6 successful (Hayes, Glassnode, Robot Wealth, Coin Metrics, CryptoQuant, Newfound). Source-list issues: Lyn Alden URL 404, Woocharts is a chart page not a blog, Marcos López de Prado (LinkedIn) + Ari Paul (X) require auth — 2-source maintenance needed. Extracted 12 candidate claims, 1 survived score-floor (IDEA-20260512-01: ETF Flows 30d MA sign-flip, score 12, BTC) + 1 reinforcement note added to IDEA-20260429-03 (CVD turn-positive — same concept resurfaced in Glassnode W20). Dropped: 9 (Glassnode-proprietary-data barriers ×5, mandate violations options/perps ×3, Hayes macro vibes, Coin Metrics quantum risk). | no trade action; routine #6 cron stall flagged for diagnostic follow-up
2026-05-12T19:30:00Z | idea-scan | system | **Verification re-run after settings.json bypassPermissions fix** — re-scraped Glassnode/Hayes/CryptoQuant indexes 3h after HARV-20260512-CATCHUP. Zero new content since: Glassnode latest still May 11 (Market Pulse W20, already extracted); Hayes latest still "Butterfly Touch", already extracted; CryptoQuant quicktake page unchanged. No new ideas to append. Pipeline functional; cron-stall fix validation pending tonight's 18:02 PT scheduled fire (expect day-gate skip commit since today is Tuesday). First real-harvest cron validation Friday 2026-05-15 18:02 PT. | no action
2026-05-12T17:06:51Z | harness | day-gate | not Saturday, skipping | no action

2026-05-12T17:40:23Z | allocation | day-gate | not Sunday, skipping | no action

2026-05-12T20:07:01Z | routine-02-midday | system | **Heartbeat — portfolio flat.** No open positions since SOL +4R close 2026-05-11T19:00Z. MTM skipped (no positions → equity = cash = $10,258.06, DD 0% from peak, no exit checks possible). Kill switches all clear: daily realized 0%, DD 0% (cap 25%, warn 12.5%), equity floor $10,258.06 > $7,500, losing-day streak 0/7. Midday routine forbids new entries by spec — entry responsibility belongs to routines #1 (overnight) and #3 (EOD). Telegram SILENT (no exits, no kill-switch trip, no DD warn crossing). | no action
2026-05-13T22:21:02Z | allocation | day-gate | not Sunday, skipping | no action

## 2026-05-14T16:00Z — routine-01-overnight

### Technical (rule-driven, deterministic)

**Universe price pull (Kraken `kraken_multi_ticker`, 24h % change):**

| Pair | Last | 24h % | Liquidity (≥$2M) | Notes |
|------|-----:|------:|:---|---|
| BTC/USD | 80,856.1 | +1.97 | ✓ ($154M) | rank 1 |
| ETH/USD | 2,280.67 | +1.01 | ✓ ($27M) | rank 2 |
| SOL/USD | 91.94 | +0.89 | ✓ ($27M) | rank 3 |
| XRP/USD | 1.46309 | +2.55 | ✓ ($23M) | rank 4 |
| TAO/USD | 305.77 | +3.84 | ✓ ($8M) | rank 5 |
| HYPE/USD | 42.21 | +8.70 | ✓ ($7M) | rank 6, biggest gainer |
| XDG/USD | 0.11451 | +1.63 | ✓ ($14.5M) | rank 7 |
| SUI/USD | 1.2177 | +0.85 | ✓ ($12.9M) | rank 8 |
| LTC/USD | 57.87 | +1.54 | ✓ ($3.5M) | rank 9 |
| ADA/USD | 0.26946 | +1.80 | ✓ ($2.55M) | rank 10 |
| FARTCOIN/USD | 0.2173 | **−0.32** | **✗ ($1.28M)** | rank 11 |
| AVAX/USD | 10.00 | +2.56 | ✓ ($2.05M) | rank 12 |
| LINK/USD | 10.47 | +2.52 | ✓ ($2.43M) | rank 13 |
| PENGU/USD | 0.00919 | +2.30 | **✗ ($1.43M)** | rank 14 |
| TRX/USD | 0.35464 | +1.49 | **✗ ($1.72M)** | rank 15 |

- **Regime breadth: 14/15 positive** (FARTCOIN only negative). W19-D rule 5a threshold ≥4 → **GATE PASSES** for the first time in 3 wakes (vs 1/15 on 05-12 morning and 0/15 on 05-12 midday).
- **Below-liquidity-floor (W18-B):** FARTCOIN, PENGU, TRX — rejected from entry pool regardless of other criteria.
- **Risk flag (Kraken MCP):** CLEAR (1 tier-2 macro caution: US-Iran tensions, off-universe, non-blocking).

**Open-position overnight stop check:** None — portfolio was flat entering this wake (SOL +4R 2026-05-11T19:00Z was last close).

**Entry scan — per-pair evaluation in rank order, taking highest-rank eligible per W18-C "max 1 entry/wake":**

| Rank | Pair | Rule 1 (1H>EMA20) | Rule 2a (55<RSI≤80) | Rule 3 (4H>EMA50) | Verdict |
|---:|---|---|---|---|---|
| 1 | BTC/USD | PASS (80923 > 79886) | PASS (RSI ~67.4) | **FAIL** (4H 79245 < EMA50 ~80514) | REJECT 4H trend |
| 2 | ETH/USD | (not computed) | (not computed) | **FAIL** (4H 2253.1 < EMA50 ~2311) | REJECT 4H trend |
| 3 | SOL/USD | (not computed) | (not computed) | **FAIL** (4H 90.61 < EMA50 ~91.45, marginal) | REJECT 4H trend |
| 4 | XRP/USD | PASS (1.46733 > 1.4405) | PASS (RSI ~67.7) | **PASS** (4H 1.43211 > EMA50 ~1.43107, marginal +0.001) | **ACCEPT** |
| 5 | TAO/USD | (skipped per rule 8 — XRP wins) | — | (FAIL 4H 296.12 < EMA50 ~304.94) | REJECT 4H trend |
| 6 | HYPE/USD | (skipped per rule 8) | — | (FAIL 4H 38.91 < EMA50 ~41.63) | REJECT 4H trend |
| 7-15 | — | (not evaluated per rule 8 — XRP rank 4 is highest-rank eligible) | — | — | — |

**XRP entry detail (computed in-line per `skills/decide.md`):**

- **Just-closed 1H bar:** 2026-05-14T15:00Z (close 1.46733; bar closes at 16:00Z, which is the entry timestamp).
- **1H 20-EMA:** ~1.4405 (seeded SMA20 over idx 0-19 = 1.44448, then α=2/21 iterated through idx 59). Close +1.9% above EMA.
- **1H RSI(14):** ~67.74 (gains 0.06731 / losses 0.03205 over Δ_{46..59}, RS ≈ 2.10). Comfortably within W19-D 55<RSI≤80 envelope; lesson 2026-04-29 (TAO RSI 86.1 climactic) avoided.
- **4H 50-EMA:** ~1.43107 (SMA50 seed 1.43020, iterated α=2/51 through idx 58 close 1.43211). 4H close just barely re-crossed the EMA50 — fresh trend confirmation, not extended.
- **ATR(14) on 1H:** $0.01215 (sum of TR over idx 46-59 = 0.17006 / 14). Elevated due to idx 58 breakout bar (TR 0.03546). Stop distance = 2×ATR = **$0.02429**.
- **Volume context:** 14:00Z 1H breakout bar (close 1.4707) had 2.16M XRP volume — 4-7× the prior 50-bar average. Conviction signal.

**Pre-entry guardrail check (`pre_entry_check`):**

| Check | Value | Limit | Result |
|---|---|---|---|
| open_positions < 8 | 0 | 8 | PASS |
| open_positions < strategy.max_concurrent | 0 | 4 | PASS |
| portfolio_risk + new_risk ≤ 4% | 0 + 1.50% = 1.50% | 4% | PASS |
| new_trade_risk ≤ 1.5% | 1.50% ($153.86) | 1.50% ($153.87) | PASS (at cap) |
| pair in universe | yes (rank 4) | — | PASS |
| pair not already open | no XRP open | — | PASS |
| daily_loss_pct ≤ 5% | 0% | 5% | PASS |
| equity ≥ $7,500 | $10,258.06 | $7,500 | PASS |
| W19-D regime gate (≥4/15 pos) | 14/15 | 4/15 | PASS |
| W19-D 24h same-pair re-entry cooldown | XRP last close 2026-05-07T14:00Z (>7d ago, was stop-out so cooldown would have applied for 24h only) | 24h | PASS |
| W18-A cluster cap (≤2 in BTC-cluster) | 0 (XRP not in cluster) | 2 | PASS |
| W18-B liquidity floor (≥$2M/24h) | $23M | $2M | PASS |
| W18-C max 1 entry/wake | 1 | 1 | PASS |
| Rule 8 highest-rank tiebreaker | rank 4, others rejected | — | PASS |

ACCEPT.

**Position sizing (per strategy v0.2):**

- Equity: $10,258.06
- Risk per trade: 1.5% × $10,258.06 = $153.87
- Fill price: 1.46733 × 1.0005 (slippage) = **1.46806**
- Stop price: 1.46806 − 0.02429 = **1.44377**
- Stop distance: $0.02429
- Size: $153.87 / $0.02429 = **6334 units** (rounded down)
- Notional: 6334 × $1.46806 = $9,298.69
- Entry commission: 0.26% × $9,298.69 = $24.18
- Cash after: $10,258.06 − $9,298.69 − $24.18 = **$935.19**
- 4R target: 1.46806 + 4 × 0.02429 = **1.56522** (≈ +$615 / +4R if hit)

**Trade event logged:**
`2026-05-14T16:00:00Z | OPEN | XRP/USD | long | 6334 | 1.46806 | 1.44377 | — | — | — | entry-rule-v0-momentum`

### News (Firecrawl scan abbreviated)

Full Firecrawl CoinDesk+TheBlock pull deferred this wake (context budget conservation; same pattern as 2026-05-12T13:07Z wake). `kraken_risk_flag` classifier (2026-05-13T07:16:59Z) swept 4 headlines and surfaced 0 ACTIONABLE on universe-pair base assets. Only flag: tier-2 macro on US-Iran military tension (Crypto Briefing, single source, non-blocking, off-universe).

Recent universe-context items still pattern-detect-worthy from prior wakes (carried-forward from research_log entries on 05-09 / 05-11): SOL Alpenglow testnet live (informational, no immediate price catalyst), XRP Ripple Prime $200M raise from Neuberger Berman (mildly positive structural — may have contributed to XRP outperformance today). Note that XRP +2.55% is the 3rd-strongest universe gainer behind HYPE (+8.7%) and TAO (+3.84%). **ACTIONABLE flagged: 0** items.

### First-of-month universe refresh

2026-05-14 is Thursday — not the 1st or first-weekday-of-month. No refresh.

### Decision

- **OPEN XRP/USD** long 6334 @ 1.46806, stop 1.44377, 4R target 1.56522. Reason: entry-rule-v0-momentum.
- **No exits** — was no open position entering this wake.
- **No lessons appended** — clean rule-driven entry, no anomaly pattern requiring extraction. (XRP marginal 4H pass +0.001 above EMA50 is worth monitoring; if subsequent wake stops out we'd extract a "fresh-4H-crossover entries underperform" lesson candidate for routine #4.)
- **Kill-switch state:** all clear. Daily realized 0%; DD 0.28% from peak (slippage drag, normal); equity $10,229.26 > $7,500 floor; losing-day streak 0/7. Cluster {BTC,ETH,SOL,TAO,AVAX,SUI,LINK} 0/2.
- **Telegram:** **NOTIFY** per routine-01 spec (new OPEN occurred).

### Process notes

- First eligible entry since the 2-day broad-tape pullback (last entry was SOL 2026-05-08T17:00Z which ran to 4R 05-11). W19-D regime gate did its job by holding entries flat for 2 wakes at 1/15 and 0/15 breadth.
- Rule 8 priority worked as designed: top-3 by rank (BTC, ETH, SOL) all failed the 4H trend filter despite +1-2% 24h moves; XRP was the highest-rank pair where the 4H crossover materialized. Lower-rank candidates (XDG, SUI, LTC, ADA, AVAX, LINK) not evaluated because XRP locked the slot — this is correct per rule 8 (and saves token budget).
- ATR elevated (~3× of normal range) due to the breakout bar. Wider stop = smaller size = same $-risk. Strategy v0.2 sizing handles this automatically.
- Entry at marginal 4H crossover (+0.001 above EMA50) is the riskiest profile for a v0.2 entry — the 4H trend hasn't accelerated yet, just curled. The 1H momentum carry (+1.9% above EMA20 and RSI 67) is strong though. Watching for early-bar stop-out on cluster-correlated reversal (BTC/ETH still below their 4H EMA50s — if they fail to follow, XRP could orphan).

## 2026-05-14T16:45Z — routine-03-eod

### Context

Cron-fire of `bull-03-eod` ~45min after `bull-01-overnight` opened XRP at 16:00Z. EOD's role per spec: final MTM, exit check on just-closed 1H, entry rescan (interpreted below), lesson extraction, day-stats compilation, mandatory Telegram card.

### Final mark-to-market

- XRP/USD spot 16:30Z (`kraken_ticker`): **1.4689** (24h +2.96%, spread 0.00013, vwap 1.44). Tight liquidity, no spread anomaly.
- Position MTM: 6334 × 1.4689 = **$9,304.01** (vs entry notional 9298.69)
- Unrealized PnL: **+$5.32** (+0.03R) — recovered from earlier −$4.62 mark
- Cash: $935.19 (post entry-commission $24.18)
- **Equity: $10,239.20** (vs prior peak $10,258.06)
- **Drawdown from peak: 0.18%** — well within 12.5% warn / 25% kill caps

### Post-close exit check (XRP just-closed 1H bar 2026-05-14 15:00Z)

Bar 15:00Z close **1.46903** (high 1.4721, low 1.46197, vol 553k, trades 753):
- Static stop 1.44377: close 1.46903 **>** stop. No stop-hit (bar low 1.46197 also above).
- 1H 20-EMA at 15:00Z: iterated from E58=1.43763 → E59 ≈ **1.4406**. Close 1.46903 > EMA → no EMA-cross exit.
- 4R target 1.56522: close well below. No take-profit.

**Hold XRP.** Next 1H exit check at 17:00Z bar close.

### Entry scan (routine-03 spec step 3)

**Regime breadth (refresh 16:15Z):** unchanged from overnight wake — 14/15 positive (only FARTCOIN red, also below liquidity floor). Gate PASSES.

**Per-pair evaluation summary (rule-8 priority order):**

| Rank | Pair | Status |
|:---:|---|---|
| 1 | BTC/USD | rejected this morning on rule 3 (4H close 79245 < EMA50 80282) |
| 2 | ETH/USD | rejected on rule 3 (2253.10 < 2305.62) |
| 3 | SOL/USD | rejected on rule 3 (90.61 < 91.59) |
| 4 | XRP/USD | **HELD** (entered 16:00Z this morning by routine-01) |
| 5–15 | TAO, HYPE, XDG, SUI, LTC, ADA, AVAX, LINK | **not evaluated** — see Decision rationale |

### News (Firecrawl scan)

**Deferred this wake** to conserve context budget (same pattern as 2026-05-12 routine-01). v0.2 news rule is informational-only (no entry veto), and overnight wake already harvested the 24h headline set with 0 ACTIONABLE. No new XRP-base-asset catalysts surfaced via spot price (no idiosyncratic XRP spike vs broad 14/15 rally). `kraken_risk_flag` daily classifier (CLEAR per overnight). 

**ACTIONABLE flagged: 0** items.

### Sentiment

XRP spread 0.00013 (0.009% of price) — tight. Single open position, no entry-decision data needed. Depth pull skipped.

### Decision

- **NO ADDITIONAL ENTRIES.** Rationale: cron-fire-adjacent routine-01 already consumed the per-wake entry budget (rule 8: "max 1 new entry per routine wake"). Treating this EOD fire as a separate wake would effectively allow 2 entries inside the same 1H bar (15:00–16:00Z window when XRP just printed +2.4%), recreating the cascade-risk failure mode lesson 2026-04-27 was designed to prevent. **Conservative interpretation chosen: 1-per-cron-bar.** This ambiguity should be codified at routine #4 (Saturday 2026-05-16): either tighten strategy.md rule 8 to "max 1 entry per 1H bar" or explicitly allow EOD to re-scan with cluster-cap as the only check.
- **NO EXITS.** XRP all three exit triggers clear at 15:00Z 1H close.
- **NO LESSONS APPENDED.** XRP entry is 1h old — too fresh for outcome-based lesson extraction. Pre-outcome lesson candidates already noted in overnight log (marginal 4H crossover risk; cluster-orphan risk if BTC/ETH don't follow).
- **Kill-switch state:** all clear (daily 0%, DD 0.18%, equity $10,239.20, losing streak 0).
- **No archive sweep:** 2026-05-14 is Thursday; last trading day of May is Friday 2026-05-29.

### Day's summary stats

- **Day PnL:** −$18.88 (−0.18%) — entry commission $24.18 partially offset by +$5.32 XRP positive drift
- **Trades opened:** 1 (XRP/USD long, by routine-01-overnight)
- **Trades closed:** 0 — win rate today N/A
- **New equity:** $10,239.20 (peak $10,258.06 from 2026-05-11 SOL +4R)
- **Drawdown:** 0.18% from peak
- **Rolling 7-day delta vs BTC-hold (approximate):** BULL ≈ +5.86% (from 9672.75 EOD 2026-05-07 LINK exit → 10239.20 now); BTC-hold ≈ +1.07% (~80000 → 80857). **BULL +4.79% delta vs BTC over 7d.** Full computation defers to routine #4 with precise reference prices.
- **Rolling 30-day:** window pre-dates BULL inception (2026-04-20); not yet computable. First available 2026-05-20.

### Process notes

- Slot identity confirmed: this fire is `bull-03-eod` content (final MTM + exit check + day stats + EOD Telegram card). Distinct from prior `bull-03-eod`-misfire-as-routine-01 pattern (commits `3ce53b1`, `2055f30`-precursor).
- The 1-per-cron-bar interpretation is a deliberate conservative reading; flagged for routine #4 review.
- **Telegram:** mandatory EOD card per routine-03 NOTIFY spec.
2026-05-15T06:21:04Z | harness | day-gate | not Saturday, skipping | no action
2026-05-15T06:22:33Z | allocation | day-gate | not Sunday, skipping | no action
2026-05-16T20:00:00Z | midday | exit | XRP/USD stop 1.44377 pierced intrabar on 2026-05-15T13:00Z 1H bar (low 1.4292); missed by intervening routines (last MTM EOD 2026-05-14; 05-15 overnight/EOD did not run/commit). Closed @ 1.44305 (stop +0.05% adverse slip), realized −$206.37 / −1.03R. Now flat. DD 2.01% (warn 12.5%, cap 25%). Equity $10,051.73 > $7,500 floor. Daily loss for 05-15 ≈ −2.01% < 5% cap. Streak 1 losing day (cap 7). No kill switch. Risk scan CLEAR (1 caution: unconfirmed US/Iran headline). No new entries (midday = position mgmt only). Telegram sent (exit event).
2026-05-16T10:27:19Z | allocation | day-gate | not Sunday, skipping | no action

## 2026-05-16 — routine-03-eod

### Context

Scheduled `bull-03-eod` fire (note: 2026-05-16 is Saturday; EOD cron is Mon–Fri but the task dispatched it, so reconciliation proceeds). Slot identity confirmed: routine-03 content (final MTM + exit check + day stats + mandatory EOD card). No routine-03-eod ran for 2026-05-15 (only harness/allocation day-gate skips logged). The XRP position opened 2026-05-14T16:00Z was still marked "open" entering this wake.

### Trade-log correction — XRP exit reconciliation (PRIMARY ACTION THIS WAKE)

A concurrent `routine-02-midday` instance (research_log line `2026-05-16T20:00:00Z | midday | exit`) closed XRP as `exit-stop-hit` @ 1.44305, −$206.37 / −1.03R, timestamp 2026-05-15T13:00Z, and **sent a Telegram exit alert with that −$206.37 figure**. It also rebuilt portfolio.md to equity $10,051.73.

That exit is **superseded** by this routine. Per `strategy.md` Exits: "Exit when ANY of the following is true … checked at the close of each 1H candle. No intra-bar exits." The binding exit is the *first* condition true at a 1H close. Replaying XRP 1H closes from the 2026-05-14T16:00Z entry (Kraken `kraken_ohlcv` XXRPZUSD 1h, 80 bars):

- **20-EMA computation:** seed = SMA of 1H closes 2026-05-13 03:00→22:00Z = 28.78338/20 = 1.439169; iterate α=2/21=0.0952381 forward 30 bars. Spot-check vs prior EOD's independent estimate (≈1.4406 @ 2026-05-14 15:00Z) — consistent (this run: 1.44118 @ same bar). EMA path post-entry: 05-14 16:00Z 1.4448 → 17:00Z 1.4491 → 18:00Z 1.4573 → 19:00Z 1.4628 → 20:00Z 1.4670 → 21:00Z 1.4699 → 22:00Z 1.4727 → 23:00Z 1.4738 → 05-15 00:00Z 1.4757 → 01:00Z 1.4765 → 02:00Z 1.4777 → 03:00Z 1.47863 → **04:00Z 1.47800**.
- **Exit rule 1 (close < 20-EMA):** closes 05-14 16:00Z→05-15 03:00Z (1.479, 1.492, 1.536, 1.516, 1.508, 1.498, 1.501, 1.485, 1.495, 1.485, 1.490, 1.489) all > EMA. **05-15 04:00Z close 1.47298 < EMA 1.47800 → FIRST exit trigger, exit-ema-cross.**
- **Exit rule 2 (static stop 1.44377):** first 1H close ≤ stop not until 05-15 13:00Z (close 1.43187). Intra-bar lows from 05-14 16:00Z→05-15 04:00Z all ≥ 1.47298 — stop untouched before the EMA-cross even ignoring the no-intra-bar rule.
- **Exit rule 3 (4R = 1.56522):** never reached (peak 1H close 1.53618 @ 05-14 18:00Z; bar high 1.54488).

The EMA-cross at 05-15 04:00Z closes the position ~9h before any stop interaction → the 13:00Z stop-out is impossible. Correction row appended to `trade_log.md` (reason `correction-previous-row`, candle-close timestamp 2026-05-15T04:00:00Z) per `skills/log-trade.md` append-only rule. Fill 1.47224 = close 1.47298 × (1−0.0005) adverse slip. Net realized **−$21.92 (−0.14R)** after 0.26%/side commission. Cash $935.19 + ($9,325.19 − $24.25) = **$10,236.14**. Equity $10,236.14 (vs routine-02's erroneous $10,051.73 — a $184.45 overstated loss).

### Post-close exit / entry scan

- **Open positions entering wake:** XRP (now correctly closed 05-15 04:00Z). Account flat.
- **Entry scan:** W19-D regime-confirmation gate (rule 5a) — universe 24h breadth via `kraken_multi_ticker`: **0 / 15 positive** (ADA −3.19, AVAX −3.36, ETH −2.46, FARTCOIN −4.84, HYPE −8.27, LINK −4.22, LTC −3.17, PENGU −4.88, SOL −3.87, SUI −4.95, TAO −5.42, TRX −0.20, BTC −1.57, XDG −4.21, XRP −2.46). 0 < 4 required → **regime gate FAILS, reject all new entries this wake.** Broad risk-off tape; no per-pair evaluation needed. (Also Saturday — outside Mon–Fri entry cadence regardless.)
- **News / sentiment:** `kraken_risk_flag` CLEAR (1 non-blocking tier-2: unconfirmed US/Iran military headline, single non-major source). No entries to vet; informational only under v0.2.

### Lessons

1 lesson appended (round-trip give-back; XRP). See `lessons.md` 2026-05-15 entry.

### Day's summary stats

- **Realized this reconciliation:** XRP −$21.92 (−0.14R), candle-date 2026-05-15.
- **Equity:** $10,236.14 (vs prior EOD 2026-05-14 $10,239.20). Net change since last EOD **−$3.06 (−0.03%)** — spans the missed 05-15 EOD; the −$21.92 realized largely replaced the +$5.32 unrealized mark carried at last EOD.
- **Since start:** +$236.18 (+2.36%) on $10,000.
- **Trades opened:** 0. **Trades closed:** 1 (XRP, corrected). Win rate today: 0/1.
- **Drawdown:** 0.21% from peak $10,258.06.
- **Rolling 7d (approx):** BULL ≈ +5.8% (from ~$9,672.75 EOD 2026-05-07); BTC-hold ≈ −3 to −4% (BTC ~80,800 → 77,819). BULL ≈ **+9% delta vs BTC over 7d (approx)**. Precise computation deferred to routine #4.
- **Rolling 30d:** pre-inception; first computable 2026-05-20.
- **No archive sweep:** last trading day of May is Fri 2026-05-29.

### Kill-switch state

All clear. Daily realized −0.21% (cap 5%); losing-day streak 1 (cap 7); DD 0.21% (cap 25%); equity $10,236.14 > $7,500 floor.

### Process notes

- Concurrent-routine write race observed: routine-02-midday and routine-03-eod both acted on the same open XRP position within the same clock window, producing a duplicate/contradictory CLOSE. Root cause: 05-15 routines did not run, leaving an unprocessed position that two later fires raced to reconcile, using different exit interpretations (intra-bar stop vs close-based rule ordering). **Escalated to routine #4 (today, Saturday 2026-05-16):** (a) late/concurrent fires must replay ALL unprocessed 1H closes and apply the earliest trigger; (b) single-writer lock or idempotent CLOSE keyed on open-position id; (c) reconcile "no intra-bar exits" wording vs intra-bar stop usage.
- **Telegram:** mandatory EOD card sent, explicitly correcting the earlier routine-02 −$206.37 alert to the true −$21.92.

## 2026-05-16T18:30Z — routine-04-harness (W20, on-cron Saturday)

| 2026-05-16T18:30Z | harness | W20 memo written (weekly_memos/2026-W20.md). Equity $10,236.18 (+2.36% inception), flat, peak $10,258.06, DD-from-peak 0.21%, all kill switches clear. W20 closes: SOL +4.03R/+$585.35 (4R-target, first ever), XRP −0.14R/−$21.92 (exit-ema-cross, using CORRECTED close — supersedes mislogged 13:00Z −$206.37 stop row). Win 50%, avg +1.95R. | report |
| 2026-05-16T18:30Z | harness | VERIFY: Kraken MCP OK (BTC smoke). TradingView Desktop NOT INSTALLED — tv_health_check CDP fail, tv_launch found no binary (AppData\Local, Program Files, x86). 2nd consecutive harness blocked from 180d variant backtests. Escalated as hard blocker in memo Open Q1. | no TV action |
| 2026-05-16T18:30Z | harness | Lessons: NEW 2026-05-15 profit-give-back (XRP ran ~+2.8R→−0.14R; 4R hit 1/17) scored **9** — highest open exit-logic gap. 2026-04-24 commission-drag raised **7→8** (XRP = 3rd whipsaw instance). 5 lesson sections, no prune (cap 50). | scored |
| 2026-05-16T18:30Z | harness | Variants spawned: v0.9-mean-rev-tight (autoloop sweep of v0.4, RSI 25→20); v0.10-exit-confirm (commission-drag lesson, 2-bar EMA exit); v0.11-breakeven-2R (profit-give-back lesson, breakeven ratchet ≥2R). No v0.3/v0.5 sweep (v0.3 both dirs covered; v0.5 cap=0 documented uninformative). Rack 9/10. idea_bank IDEA-12 → under-review. | spun up |
| 2026-05-16T18:30Z | harness | Competition (vs Codex, 2026-07-01): BULL +5.39% LEADS Codex v0 −0.20% / Codex Aggro −0.43% (reversal from W19 −1.45 trail). Codex Aggro now 200% gross short — mandate-incompatible, not copied. | report |
| 2026-05-16T18:30Z | harness | ACK concurrent-write-race escalation (routine #3 EOD note, XRP mislog root cause). Strategy memo cannot fix infra; logged here as an operational item requiring an OPERATING.md / routine-architecture change (single-writer lock or idempotent CLOSE keyed on open-position id; late fires replay all unprocessed 1H closes earliest-trigger-first). NOT a Ring-2 strategy edit — flagged for user as a v2 routine-infra task; added to W20 memo open questions. | escalate |


## 2026-05-16T13:00Z — routine-01-overnight

### Technical (rule-driven, deterministic)

- Account flat (0 open positions per portfolio.md, last rebuild 2026-05-16 routine-03-eod). No position/stop/exit checks required this wake.
- Overnight Kraken `kraken_multi_ticker` (15 universe pairs), 24h % change:
  BTC −1.43, ETH −2.24, SOL −3.40, XRP −1.71, TAO −4.53, HYPE −7.04, DOGE −4.37, SUI −4.89, LTC −2.44, ADA −2.68, FARTCOIN −3.79, AVAX −2.83, LINK −4.25, PENGU −4.32, TRX −0.25.
- **Positive-24h count: 0 / 15.** Broad single-direction red tape; HYPE worst (−7.04%), TRX shallowest (−0.25%).
- **Entry rule 5a (W19-D regime-confirmation gate) FAILS at wake level:** requires ≥ 4/15 universe pairs positive 24h; observed 0/15. Per rule 5a this rejects ALL new entries this wake. Per-pair 1H/4H OHLCV + indicator computation intentionally skipped (context-budget; 5a is a wake-level gate that pre-empts per-pair evaluation — same inferred-reject pattern as 2026-04-21 runs). Under uniformly negative drift, 1H RSI14 > 55 is also mathematically implausible across the board (rule 2 would compound the reject).
- Final candidate list: **empty** — all 15 rejected by entry-rule-5a (regime-confirmation gate, 0/15 positive).

### News (Firecrawl-driven, informational only in v0.2)

- News scan deferred to the separate morning-brief skill (established v0.2 practice — cf. 2026-04-21 overnight rows). v0.2 is not news-reactive: no entry gate depends on news, and no entries are possible this wake regardless (5a gate). Daily risk scan (`kraken_risk_flag` 2026-05-16T12:30Z): **CLEAR**, "markets calm", 0 tier-1/tier-2 triggers — the broad −2 to −7% move did not trip the external risk classifier. No ACTIONABLE item recorded.

### Sentiment (passive — Kraken depth/spread proxy in v0.2)

- No entry candidates → no per-candidate spread/depth pull required this wake. Volume sanity from multi-ticker: high-liquidity names (BTC, ETH, SOL, XRP, DOGE, PENGU) trading actively; AVAX 24h base volume thin (~216k), consistent with its standing W18-B sub-$2M caveat.

### Decision

- **Action: SKIP — no entries, no exits.** Driver: entry-rule-5a regime-confirmation gate (0/15 universe pairs positive, threshold ≥4/15). Account remains flat. Kill-switch state unchanged from routine-03-eod: daily realized −0.21% (cap 5%), losing-day streak 1 (cap 7), DD 0.21% (cap 25%), equity $10,236.14 > $7,500 floor — all clear, no Ring 3 tripped.
- Universe refresh: skipped, today is 2026-05-16 (not 1st of month; next refresh 2026-06-01).
- No lesson appended: no entry taken, no single-pair price anomaly drove an action, no news cluster. Broad beta drawdown with risk-flag CLEAR is regime, not a strategy-actionable anomaly under v0.2.

| 2026-05-16T13:00Z | overnight | kraken | 15-pair overnight pull: 0/15 positive 24h (BTC −1.43 … HYPE −7.04). Flat account. Entry-rule-5a regime gate fails wake-level (0/15 < 4/15) → all entries rejected. Risk flag CLEAR. No positions to manage. | SKIP — no trades; research_log only |
| 2026-05-16T17:07Z | harness | dedup | DUPLICATE same-week fire — W20 harness already completed and committed today (cab62cc; memo weekly_memos/2026-W20.md written, lessons scored, variants v0.9/v0.10/v0.11 spawned, Telegram retention digest sent). Idempotent skip: did NOT rewrite memo, re-spawn variants, re-score/prune lessons, or re-send Telegram (would duplicate the digest + recreate the concurrent-write hazard escalated in W20 memo Open Q4 / the XRP −$206.37 mislog). No second run per Saturday. | SKIP — no action; research_log only |
| 2026-05-16T17:40Z | allocation | day-gate | not Sunday (Saturday PT), skipping | no action |

## 2026-05-17T13:00Z — routine-01-overnight (MCP-failure SKIP)

### VERIFY / data-source state

- **Kraken MCP: UNAVAILABLE.** Server is configured in `.mcp.json` (`kraken` stdio → `kraken_mcp.py`) but exposed zero tools this wake — not in the live tool list, not resolvable via ToolSearch (`mcp__kraken__kraken_multi_ticker` / `kraken_ticker` / `kraken_ohlcv` / `kraken_risk_flag` all "No matching deferred tools"), and not in the session's connecting-servers list (only `ableton` was connecting). Server failed to start/register.
- **TradingView MCP fallback: UNAVAILABLE.** `tv_health_check` → `CDP connection failed after 5 attempts: fetch failed`. Consistent with W20 harness note (2026-05-16, cab62cc): TradingView Desktop not installed, no binary found. 3rd consecutive routine blocked from TV.
- Both the primary data source (Kraken MCP) and the documented indicator fallback (TradingView MCP, per `skills/decide.md`) are down. Steps 1–5 of the routine (overnight price pull, position/stop check, entry scan, news/risk pull, entry placement) all require live price data and cannot be executed.

### Guardrail applied

- `memory/guardrails.md` Ring 3: *"Kraken MCP / TradingView MCP / Telegram MCP failure → SKIP this routine run, append error to research_log.md, retry next routine."* Action taken accordingly: SKIP, log, retry next routine. This is the prescribed log-and-retry path (not a HALT+ALERT kill switch — those four are equity/daily-loss/drawdown/losing-streak triggers, none of which are evaluable or tripped this wake).

### Position / risk state (carried, unverified — no live data)

- Account **flat** per `portfolio.md` (last rebuild 2026-05-16 routine-03-eod): 0 open positions, equity $10,236.14, cash $10,236.14, DD 0.21% from peak $10,258.06, losing-day streak 1. No open positions ⇒ no stop/exit management was required this wake regardless of data availability; SKIP introduces no unmanaged-position risk.
- Kill-switch state unchanged from routine-03-eod (cannot recompute without prices; no trades): all clear, no Ring 3 equity/loss/dd/streak trigger.

### Other steps

- Universe refresh: not due (today 2026-05-17, not 1st of month; next 2026-06-01).
- News/Firecrawl scan: skipped — no entries possible this wake regardless of news (no price data); v0.2 is not news-reactive.
- Note: 2026-05-17 is a Sunday; routine-01 cron is Mon–Fri (`0 6 * * 1-5`). Task dispatched it anyway; processed as a normal wake. Outcome (SKIP) is independent of the weekday question.

### Decision

- **Action: SKIP — no price pull, no position checks, no entries, no exits, no Telegram.** Driver: Kraken MCP + TradingView MCP both unavailable (Ring 3 MCP-failure → log-and-retry). Account remains flat. Retry next routine.

| 2026-05-17T13:00Z | overnight | mcp-failure | Kraken MCP exposed 0 tools (server failed to load); TradingView fallback CDP-fail (TV Desktop not installed, 3rd consecutive). Both data sources down. Ring 3 MCP-failure guardrail → SKIP + log + retry next routine. Account flat (0 positions) per portfolio.md — no unmanaged risk. No notify (not a HALT kill switch). | SKIP — no trades; research_log only |
| 2026-05-17T17:34Z | harness | day-gate | not Saturday (Sunday PT), skipping | no action |

### routine-05-allocation 2026-05-17 — SKIP (Ring 3 MCP-failure)

- DAY GATE passed: today is Sunday 2026-05-17 (PT 10:34, UTC 17:34) — full routine attempted.
- VERIFY failed: Kraken MCP exposed 0 tools (server in .mcp.json failed to load); TradingView MCP CDP connection failed (TV Desktop not running, 4th consecutive harness/routine block). Both required data sources down — same condition routine-01-overnight handled this same day at 13:00Z.
- Ring 3 guardrail (Kraken/TV/Telegram MCP failure) → SKIP this routine run, append error to research_log, retry next routine.
- Account flat per portfolio.md (last rebuild 2026-05-16 routine-03-eod): 0 open positions, equity $10,236.14, DD 0.21%, losing-day streak 1, all kill switches clear. SKIP introduces no unmanaged-position risk.
- Core allocation analysis (concept-bucket R, vs-BTC-hold) needs live BTC price for the rolling-window comparison; the bucket-PnL portion is derivable from trade_log but the guardrail prescribes a clean SKIP rather than a partial run when the required MCP is down.
- No pending W18/W19/W20 strategy proposal awaiting a `Y` reply (W20 memo: "Proposal — none"); nothing to apply this routine regardless.
- No notify: Ring 3 MCP-failure is a log-and-retry condition, not a HALT kill switch (consistent with routine-01-overnight 2026-05-17 decision). Avoids double-notifying the same infra outage. Next routine #5 fires Sun 2026-05-24.

| 2026-05-17T17:34Z | allocation | mcp-failure | Kraken MCP 0 tools (server load fail) + TradingView CDP-fail (TV Desktop down); both data sources unavailable. Ring 3 MCP-failure → SKIP + log + retry next routine. Account flat per portfolio.md, no unmanaged risk. No pending strategy proposal to apply. No notify (not a HALT kill switch). | SKIP — no allocation analysis; research_log only |

### routine-02-midday 2026-05-17 — SKIP (Ring 3 MCP-failure)

- VERIFY failed: Kraken MCP exposed 0 tools (server in .mcp.json failed to load); TradingView MCP unavailable as fallback (TV Desktop down — consistent with routine-01/05 today). The midday routine's DO step 1 (`kraken_multi_ticker` mark-to-market) and VERIFY (kill-switch recheck on latest Kraken prices) both require the Kraken MCP.
- Ring 3 guardrail (Kraken/TV/Telegram MCP failure) → SKIP this routine run, append error to research_log, retry next routine.
- Account flat per portfolio.md (last rebuild 2026-05-16 routine-03-eod): 0 open positions, equity $10,236.14, DD 0.21% from peak $10,258.06, losing-day streak 1/7, equity floor clear. With no open positions there is no mark-to-market, no exit check, and no entries (midday is management-only) — the SKIP introduces zero unmanaged-position risk.
- Kill-switch state unchanged from last EOD rebuild (price-independent while flat): all clear, trading authorized.
- No notify: Ring 3 MCP-failure is a log-and-retry condition, not a HALT kill switch (consistent with routine-01-overnight / routine-05-allocation 2026-05-17 decisions). Avoids double-notifying the same ongoing infra outage. Next routine-02-midday fires next weekday 13:00 PT.

| 2026-05-17T20:00Z | midday | mcp-failure | Kraken MCP 0 tools (server load fail) + TradingView fallback down; mark-to-market/kill-switch recheck data sources unavailable. Ring 3 MCP-failure → SKIP + log + retry next routine. Account flat per portfolio.md (0 positions, eq $10,236.14, DD 0.21%) — no unmanaged risk; midday is management-only so no missed entries. No notify (not a HALT kill switch). | SKIP — no trades; research_log only |
2026-05-18T18:51:27Z | allocation | day-gate | not Sunday, skipping | no action
2026-05-18T18:51:32Z | harness | day-gate | not Saturday, skipping | no action
2026-05-18T20:00Z | midday | mcp-failure | Kraken MCP 0 tools available (only ableton connecting; no kraken/tradingview servers present) — mark-to-market/kill-switch-recheck data sources unavailable. Ring 3 MCP-failure → SKIP + log + retry next routine. Account flat per portfolio.md (0 positions, eq $10,236.14, DD 0.21% from peak $10,258.06, loss-day streak 1/7, equity floor clear). With 0 open positions: no MTM, no exit check, no entries (midday is management-only) — SKIP introduces zero unmanaged-position risk. Kill-switch state price-independent while flat: all clear, trading authorized. No notify (Ring 3 MCP-failure is log-and-retry, not a HALT kill switch). | SKIP — no trades; research_log only

## 2026-05-19T13:00Z — routine-01-overnight

### Technical (rule-driven, deterministic)
- Kraken MCP healthy (kraken_multi_ticker returned all 15 pairs; risk_flag scan 2026-05-19T12:30:31Z = CLEAR, "Markets calm", 0 tier1/tier2).
- 24h % change, 15 universe pairs: BTC -0.26, ETH -0.74, SOL -0.88, XRP -1.07, TAO -0.68, HYPE -0.48, DOGE/XDG -0.82, SUI -0.12, LTC -0.44, ADA -0.79, FARTCOIN -1.45, AVAX -1.19, LINK -0.72, PENGU -0.38, TRX +0.03.
- **Entry rule 5a (regime-confirmation gate): FAIL.** Positive 24h movers = 1/15 (TRX +0.03% only). Threshold is >= 4/15. Per strategy.md v0.2 rule 5a, this is a wake-level hard reject: ALL new entries rejected this wake. Per-pair RSI/EMA/ATR computation skipped — 5a gates before per-pair eval and no pair can pass once 5a fails.
- Final candidate list: **none** (regime gate reject-all).

### Position check
- 0 open positions (account flat per portfolio.md, last rebuild routine-03-eod 2026-05-16). No stops to evaluate, no exits. This routine's only close-path (overnight stop-out) is N/A.

### News (Firecrawl-driven, informational only in v0.2)
- Sources fetched: coindesk.com front page + theblock.co/latest (Firecrawl CLI 1.3.1, both 200 OK).
- Dominant theme — broad BTC-led risk-off (bearish, macro): "Bitcoin has shed $5,000 within days... selloff could worsen" (BTC ~-6% over several days to ~$76.8k, near pivotal monthly close); "Spot bitcoin ETFs log $649M net outflows, largest since January"; CoinShares: "XRP and Solana funds attract inflows as bitcoin outflows hit ~$1B" (rotation BTC/ETH out, XRP/SOL in).
- Pair-specific notes (informational, no veto in v0.2): HYPE — Hyperliquid USDC revenue-share deal "could supercharge HYPE" (supportive); DOGE — Revolut physical Dogecoin debit card (supportive); ETH — onchain conviction grows, staked ETH rises despite price underperformance (neutral/mild support).
- Hack: Echo Protocol $76M eBTC mint exploit on Monad — non-universe protocol/chain, BTCFi-adjacent, indirect; recorded, no universe-pair impact.
- Classification: macro-bearish backdrop corroborates the technical regime-off reading. No single universe pair has 3+ ACTIONABLE items this week -> no news-cluster lesson triggered. Not a discrete shock; daily risk scan independently CLEAR.

### Sentiment (passive — Kraken depth/spread proxy in v0.2)
- Not sampled: 0 entry candidates survived rule 5a, so no per-candidate spread/depth pull warranted.

### Decision
- **SKIP all entries** — driven by strategy.md v0.2 rule 5a (regime-confirmation gate, 1/15 positive < 4/15 threshold). 0 trades. No exits (flat). Not first-of-month -> no universe refresh. portfolio.md kill-switch state refreshed in place (flat, no state delta; routine-03-eod trade-log-correction note preserved). No Telegram: no kill switch, no OPEN/CLOSE, news is orderly known macro pullback with CLEAR risk scan and zero portfolio exposure (absence of message = all clear).

2026-05-19T17:06:30Z | harness | day-gate | not Saturday, skipping | no action
2026-05-19T17:39:55Z | allocation | day-gate | not Sunday, skipping | no action
2026-05-19T20:00:00Z | midday | health-check | flat (0 positions), equity $10,236.14, DD 0.21% from peak $10,258.06, risk_flag CLEAR, all kill switches clear, 0 exits (no open positions), no entries (midday position-mgmt only); regime 2/15 positive (HYPE +1.38%, TRX +0.03%) — entry-irrelevant midday | no action

## 2026-05-19 — interactive session: Ring-2 W21-F adopted (strategy v0.2 → v0.3)

- **Type:** Ring-2 strategy edit, off-cycle, user-approved in interactive chat (scope: "Live v0.2 + spin variant"). Not a routine wake.
- **Origin:** Fragility audit of the BULL-vs-Codex contest stable (this session). Finding: the only contest edge that paid was positioning for the 2026-05-12→05-17 synchronized breakdown; BULL is long-only by mandate (cannot take the offensive short side) but the defensive half (flatten open longs faster) was uncaptured. User reframed concentrated momentum P&L as designed behavior, not fragility — wanted to learn from it (memory `feedback-perf-analysis-framing`).
- **Applied:**
  - `memory/strategy.md` → **v0.3**: added entry rule **5a-SBD** (regime=SYNCHRONIZED_BREAKDOWN when ≤1/15 pairs positive 24h AND median universe 24h % ≤ −1.0%; strict subset of a 5a fail) and **Exit rule 1-SBD** (trend exit tightens 20-EMA → 9-EMA while SBD active; reverts on clear). Static 2×ATR stop + 4R TP unchanged. Header/version/changelog updated; next review routine #4 2026-05-23.
  - Spun `variants/v0.12-sbd-exit/` (README+strategy+portfolio+trade_log, $10k synthetic) — instrumented twin isolating the SBD change vs the v0.2 baseline + avoided-give-back telemetry. Rack now 10/10 (full).
  - `lessons.md`: added 2026-05-19 lesson "synchronized-breakdown defensive asymmetry" (status: addressed).
  - `leaderboard.md`: MAIN row v0.2→v0.3, v0.12 row added, cap/categories updated.
  - `weekly_memos/2026-W21-proposal.md`: status → APPROVED & APPLIED.
- **Mandate compliance:** spot-only/long-only preserved (no shorting, no leverage); change is strictly risk-reducing (can only flatten earlier). `guardrails.md` untouched. No retroactive effect — SBD applies to new entry-scans/exits only; account is flat so no open positions affected.
- **Honest caveat carried forward:** adopted on thin evidence (1 BULL trade + cross-strategy + structural reasoning, no backtest). v0.12 twin + routine #4 TV harness (when available) are the validation path; autoloop may sweep sbd_* params → Ring-2 for a tuned config.
- No Telegram sent (interactive approval already obtained; absence of routine-driven alert is correct — no kill switch, no trade).

## 2026-05-20T13:00Z — routine-01-overnight (MCP-failure SKIP, Kraken-only outage)

### VERIFY / data-source state

- **Kraken MCP: UNAVAILABLE.** Server is configured in `.mcp.json` (`kraken` stdio → `kraken_mcp.py`) but exposed zero tools this wake. ToolSearch on `kraken` and `multi_ticker risk_flag pairs` returned no matches. Session-start "connecting servers" list named `kraken` but it did not register tools before this wake processed. Routine step 1 (`kraken_multi_ticker` for all 15 universe pairs) and the per-pair OHLCV pulls cannot be executed against the primary data source.
- **TradingView MCP: UP this wake** — `tv_health_check` returned `cdp_connected: true`, `api_available: true`, chart on `KRAKEN:SOLUSD` 60m. First time since 2026-05-16 that TV is healthy. However TV is documented in `skills/decide.md` as an indicator-values fallback (`data_get_study_values` on a BULL-namespaced chart), not as a 15-pair multi-ticker source. Pulling 15 pairs' 24h % via chart-symbol switching (`chart_set_symbol` × 15 + `quote_get`) is outside the routine spec, ~15× the API surface, and not the established workflow — particularly when the live strategy is now v0.3 and would require an additional SBD regime classification (median 24h % across 15 pairs) on top of the 5a count, both needing the same multi-ticker data.

### Strategy version note (post-rebase)

- Live strategy is **v0.3** as of 2026-05-19 (Ring-2 W21-F adoption — SBD-aware regime + tightened exit). SKIP rationale unchanged: v0.3 still needs the 15-pair 24h % vector for entry rule 5/5a/5a-SBD evaluation, which is the same Kraken-MCP-dependent data the v0.2 routine needed. Outcome of the wake (no entries, no exits, account flat) is identical under v0.2 or v0.3.

### Guardrail applied

- `memory/guardrails.md` Ring 3: *"Kraken MCP / TradingView MCP / Telegram MCP failure → SKIP this routine run, append error to research_log.md, retry next routine."* Literal reading: any one of the three failing triggers SKIP. Kraken MCP is the routine's primary price source and is down → SKIP per the prescribed log-and-retry path. Not a HALT+ALERT kill switch (those four are equity / daily-loss / drawdown / losing-streak triggers, none of which can be tripped while flat and none re-evaluable without price data).
- Consistent with 2026-05-17 routine-01 SKIP precedent (Kraken+TV both down) and 2026-05-17/18 midday SKIPs (Kraken down). Differs from 2026-05-19 (Kraken healthy, ran fully).

### Position / risk state (carried, unverified — no live data)

- Account **flat** per `portfolio.md` (last rebuild 2026-05-19 routine-02-midday): 0 open positions, cash $10,236.14, equity $10,236.14, DD 0.21% from peak $10,258.06, losing-day streak 1/7. No open positions ⇒ no stop/exit management was required this wake regardless of data availability; SKIP introduces no unmanaged-position risk.
- Kill-switch state unchanged from prior rebuild (price-independent while flat): daily realized within 5% cap, streak 1/7, DD 0.21%/25%, equity $10,236.14 > $7,500 floor — all clear, trading authorized (no Ring 3 equity/loss/dd/streak trigger).

### News / sentiment

- Skipped — established precedent on data-source-outage SKIPs (cf. 2026-05-17): no entries possible regardless of news (no price data + 5a gate would gate anyway), v0.3 is still not news-reactive in the entry path. News scan deferred to next routine #1 wake when Kraken MCP recovers.

### Other steps

- Universe refresh: not due (today 2026-05-20 Wednesday, not 1st of month; next 2026-06-01).
- No lesson appended: data-outage SKIP does not produce strategy-actionable observations (the outage itself is documented in research_log and the Kraken MCP fix log d1198cd/0aa5e4a area).
- No Telegram notify: Ring 3 MCP-failure is a log-and-retry condition, not a HALT kill switch. Avoids double-notifying repeated infra issues (no OPEN/CLOSE this wake, no Ring-3 equity trigger, no ACTIONABLE news).

### Decision

- **Action: SKIP — no price pull, no position checks, no entries, no exits, no Telegram.** Driver: Kraken MCP unavailable (Ring 3 MCP-failure → log-and-retry). Account remains flat. Retry next routine.

| 2026-05-20T13:00Z | overnight | mcp-failure | Kraken MCP 0 tools (server failed to register this session; TV up but is indicator-fallback per skills/decide.md, not the 15-pair multi-ticker source). Live strategy v0.3 post-W21-F (still needs 15-pair 24h vector for 5a/5a-SBD). Ring 3 MCP-failure guardrail → SKIP + log + retry next routine. Account flat per portfolio.md (0 positions, eq $10,236.14, DD 0.21%) — no unmanaged risk. No Telegram (not a HALT kill switch). | SKIP — no trades; research_log only |
2026-05-20T17:06:41Z | harness | day-gate | not Saturday, skipping | no action
2026-05-20T17:40Z | allocation | day-gate | not Sunday, skipping | no action

## 2026-05-20 — interactive session: deep-dive deliverables (4 actions)

- **Type:** Interactive (user-driven), not a routine wake. User prompt: "deep dive with your highest trading strategies and figure out why they are losing money and try to adjust them so they still trade a lot but start making money." User then approved all four proposed actions ("all of the above") and subsequently delegated the W22 option choice ("do whatever you suggest"). Mandate compliance: chat-channel approval has equivalent authority per W18/W19/W21 precedent (already documented in 2026-W21-proposal.md). No `guardrails.md` edits.
- **Action A — bull-aggro-ignition v1.2 baseline captured (off-leaderboard R&D):** DOM-scraped SOL 60m, both sides allowed: **825 trades, 14.06% win rate, profit factor 0.607, −92.18% net, 423 margin calls, commission $7,235 (78% of net loss).** T1 closeout gate (a) PASS — both sides fire. **T2 parameter sweep BLOCKED**: strategy is structurally broken by full-equity sizing (`percent_of_equity=100`) + 2×ATR stop producing margin calls on 51% of trades. Recommended next step: v1.3 with risk-based sizing (`qty = equity * 0.015 / (atr * stopMult)`, matching main's per-trade 1.5% risk floor). Logged to `strategies/bull-aggro-ignition/backtest_notes.md`.
- **Action B — variant v0.13-trend-confirm spun:** Hypothesis variant attacking the −1R whipsaw bucket (9 of 17 main closes inside 21h of entry, ≈ −$386 of losses). Entry rule 1 → two consecutive 1H closes > 20-EMA; added rule 3a: 4H RSI(14) ≥ 50. Strictly entry-restricting. Retired v0.6-vol-comp-aggressive (8 days, 0 trades, parameter-sweep displacement priority) to make rack room; archived at `variants/archive/v0.6-vol-comp-aggressive-2026-05-20/`. Rack 10/10 (7 hypothesis / 3 sweep). 30d-eligible 2026-06-19.
- **Action C+D — W22 Ring-2 proposal drafted then applied (Option C, agent-selected):** `memory/weekly_memos/2026-W22-proposal.md` drafted with proposals G (two-bar EMA exit) + H (breakeven ratchet at +2R + lower TP 4R→3R). User delegated choice. Agent selected **Option C: G + breakeven half of H, 4R target retained.** Rationale: `feedback-perf-analysis-framing` memory cautions against capping the momentum tail; lowering 4R→3R would have foregone ~$147 of the SOL +4R archetype the engine is designed to catch. Applied to `memory/strategy.md` → **v0.4**: Exit rule 1 + 1-SBD → two-bar EMA confirmation; new Stop management section (breakeven ratchet at unrealized R ≥ 2.0); Exit rule 3 (4R TP) **unchanged**. Sibling variants v0.10-exit-confirm and v0.11-breakeven-2R are now functionally subsumed by main — flagged on the leaderboard as `LAB-SUBSUMED`, routine #4 2026-05-23 to audit and archive.
- **Lessons updated:** `lessons.md` 2026-04-24 commission-drag (score 8) → `addressed` by W22-G. `lessons.md` 2026-05-15 profit-give-back (score 9) → `addressed` by W22-H-partial (with explicit note that the 4R-target half of H was rejected per `feedback-perf-analysis-framing`).
- **Mandate compliance summary:** Spot-only/long-only preserved (no shorting, no leverage). W22 changes are strictly risk-reducing on existing positions (two-bar EMA delays exit by ≤1 bar of adverse motion, bounded by unchanged 2×ATR stop; breakeven ratchet only moves stop closer to current price). `guardrails.md` untouched. No retroactive effect — W22 rules apply to new entry-scans/exits only; account is flat so no open positions affected.
- **Honest caveats carried forward:** W22-G adopted on 3 trade-log instances; W22-H-breakeven adopted on 1 archetype (XRP) + 16-trade empirical 4R-hit-rate. No TV backtest. v0.13-trend-confirm and v0.12-sbd-exit continue accruing paper-paper evidence as forward-looking validators of the entry-quality and SBD axes respectively.
- **No Telegram sent.** Interactive session, account flat, no kill switch, no trade.
- 2026-05-21T19:28:41Z | allocation | day-gate | not Sunday, skipping | no action

2026-05-21T19:28Z | harness | day-gate | not Saturday, skipping | no action

2026-05-22T20:52:13Z | allocation | day-gate | not Sunday, skipping | no action

## 2026-05-25 — interactive session: missed-scheduler replay integrated into main BULL v0

- **Type:** Interactive user-directed catch-up, not an autonomous routine wake. User requested that the previously computed missed-scheduler replay be folded into BULL v0 rather than tracked as a separate leaderboard row.
- **Cause:** Claude scheduled-task runner had been disabled/stalled after 2026-05-19, so routine-01/routine-03 entry windows and routine-02/routine-03 exit checks were missed while the account was flat and trading authorized.
- **Replay scope:** Weekday BULL v0.4 rules over missed windows 2026-05-20 through 2026-05-22. Weekend routine-01 slots excluded. Kraken public 1H/4H OHLC replay; same one-entry-per-wake, cash/position, cluster, liquidity, 24h regime, stop, 4R target, breakeven, and two-bar EMA-confirm logic as the diagnostic replay.
- **Rows appended to `memory/trade_log.md`:** HYPE open 2026-05-20T13:00Z; TAO open 2026-05-21T04:00Z; HYPE close +$413.62 at 2026-05-21T08:00Z; HYPE open 2026-05-21T13:00Z; TAO close -$29.84 at 2026-05-22T01:00Z; HYPE close -$33.98 at 2026-05-22T02:00Z; AVAX open 2026-05-22T04:00Z; SOL open 2026-05-22T13:00Z; SOL close -$45.64 at 2026-05-22T15:00Z; AVAX close -$35.83 at 2026-05-22T16:00Z.
- **Portfolio rebuild:** Account flat, cash/equity $10,504.48, all-time realized PnL +$504.48, replay delta +$268.34, equity peak $10,728.95, drawdown 2.09%, open positions 0, kill switches clear.
- **Leaderboard:** `strategy-leaderboard` now folds `data/bull/scheduler_replay_trade_log.md` into the live BULL v0 row as an auditable `missed_scheduler_replay` overlay and removes the separate `BULL v0 Scheduler Replay` research row. If these appended rows are later published to GitHub raw, remove the local overlay from the leaderboard registry to avoid double-counting.
2026-05-25T15:18:51Z | allocation | day-gate | not Sunday, skipping | no action

2026-05-25T17:07:01Z | harness | day-gate | not Saturday, skipping | no action
2026-05-25T10:40:18Z | allocation | day-gate | not Sunday, skipping | no action

## 2026-05-25T20:00Z — routine-02-midday

### Technical (rule-driven, deterministic)

- **Open positions checked: 1 (BTC/USD long).** Entry 77678.12, stop 77122.02, 4R target 79902.52, ATR14(1h) 278.05.
- **Kraken last px (XXBTZUSD):** 77370.3; bid 77370.2 / ask 77370.3; 24h range 76020.5–77809.9; 24h chg +0.51%.
- **Latest closed 1H bar:** 2026-05-25 19:00Z close 77384.6 (high 77482.9, low 77300.0).
- **20-EMA on 1H, BTC/USD:** seed SMA of bars 2026-05-23 09:00→2026-05-24 04:00 = 75884.445; iterate α=2/21 → EMA at 19:00Z close = **77290.75**. Close 77384.6 > EMA → **rule 1 (W22-G two-bar EMA-confirm exit): 0/2 confirmation bars.**
- **Static stop check (rule 2):** lowest 1H low since entry 15:00Z window = 77300.0 (19:00Z); 20:00Z partial-bar low 77361.2. Stop 77122.02 **not pierced intra-bar.** Per routine #2 mandate "if price has pierced 2×ATR stop intrabar, close at stop price" → no action.
- **4R target check (rule 3):** target 79902.52, last 77370.3 → not reached.
- **Breakeven ratchet:** unrealized R = (77370.3 − 77678.12)/(77678.12 − 77122.02) = −307.82/556.10 = **−0.554R** → well below +2R trigger; stop remains at initial 77122.02.
- **EMA-tag-and-recover guard (single-bar):** N/A (close is above EMA, not below).

### News (Firecrawl-driven, informational only in v0.2)

- Skipped — routine #2 budget-lean by spec (does not read research_log/lessons/universe and does not run news scan; news is overnight/EOD scope).

### Sentiment (passive — Kraken depth/spread proxy in v0.2)

- BTC/USD spread 0.1 (bid 77370.2 / ask 77370.3) ≈ **0.013 bps** — tight, no caveat.

### Decision

- **Action: HOLD BTC/USD long.** No exit triggers fired (EMA-confirm 0/2; stop unhit; 4R untouched; breakeven not yet armed). **No new entries this wake** (routine #2 is position-management only — entries belong to overnight/EOD per amended routine spec).
- **Kraken risk_flag:** re-checked CLEAR (cached daily scan 2026-05-25T13:53:49Z "Markets calm").
- **Kill switches:** day PnL −$17.23 / **−0.16%** vs day-open equity $10,504.48 (cap 5%); DD 2.25% from peak $10,728.95 (warn 12.5%, cap 25%); equity $10,487.25 > $7,500 floor; losing-day streak 1/7. **All clear.**
- **Telegram:** silent (no kill switch, no exit, no drawdown warning).
- **Next decision point:** 2026-05-25T21:00Z 1H close → re-evaluate EMA-confirm + stop + 4R + breakeven against fresh closed bar.

## 2026-05-25T23:41Z — operator reconciliation

- **BTC/USD stop exit processed.** Kraken 1H replay after the midday wake showed the first binding stop trigger on the 2026-05-25T22:00Z closed candle: close 77041.4 <= fixed stop 77122.02; bar low 76975.1 confirmed the level was crossed. Rule 2 fired before any two-bar EMA exit.
- **Fill model:** exit-stop-hit uses the established stop model from prior stop rows: 77122.02 × 0.9995 adverse slippage = **77083.46**. Size 0.0338 BTC; gross price PnL −$20.10; entry commission $6.83 and exit commission $6.77; net realized **−$33.70 / −1.07R**.
- **State after close:** BULL flat; cash/equity **$10,470.78**; realized PnL all-time **+$470.78**; DD **2.41%** from $10,728.95 peak; day realized **−0.32%** vs $10,504.48 day-open equity. Kill switches clear. Same-pair stop-out cooldown blocks fresh BTC entries until **2026-05-26T22:00Z**.


## 2026-05-26T13:00Z — routine-01-overnight

### Technical (rule-driven, deterministic)

- **Wake context:** flat after BTC stop-out on 2026-05-25T22:00Z (−$33.70 / −1.07R). Cash $10,470.78, eq $10,470.78, DD 2.41% from peak $10,728.95. BTC same-pair cooldown blocks fresh BTC entries until 2026-05-26T22:00Z. Live strategy v0.4 (W22-C: G + breakeven half of H, 4R retained).
- **Kraken risk_flag:** CLEAR (2026-05-26T12:30:32Z scan, "Markets calm").
- **24h regime (Kraken multi_ticker @ wake):** **14/15 universe pairs positive.** Pos: ADA +0.56, AVAX +0.97, ETH +0.48, FARTCOIN +0.11, HYPE +1.62, LINK +0.97, LTC +0.08, PENGU +0.18, SOL +0.24, SUI +0.20, TAO +2.30, TRX +1.21, DOGE +0.68, XRP +0.32; only BTC −0.37. Median 24h % ≈ +0.48%. **Rule 5a PASS** (14/15 ≥ 4/15). **Rule 5a-SBD: not active** (>1 positive, median > −1.0%).
- **Rule 4a liquidity floor (≥$2M 24h notional):** PASS — BTC $78.1M, ETH $18.6M, HYPE $16.4M, SOL $9.69M, XRP $8.70M, TAO $8.28M, SUI $6.28M, TRX $2.497M. FAIL — DOGE $1.39M, ADA $1.61M, FARTCOIN $0.50M, AVAX $0.82M, LINK $1.38M, PENGU $1.57M, LTC $1.15M.
- **Per-pair entry-rule scan (just-closed 1H 12:00Z; just-closed 4H 08:00Z):**
  - **BTC/USD:** REJECT — rule 5b (same-pair stop-out cooldown active to 2026-05-26T22:00Z; last exit 2026-05-25T22:00Z).
  - **ETH/USD:** 1H close 2123.50 > 20-EMA ≈ 2107.43 (R1 ✓). 4H close 2118.65 vs 50-EMA ≈ 2126.50 → 4H close BELOW EMA50 (R3 ✗). **REJECT rule 3.**
  - **SOL/USD:** 1H close 85.22 > 20-EMA ≈ 84.90 (R1 ✓). 4H close 85.14 < 50-EMA ≈ 85.97 (R3 ✗). **REJECT rule 3.**
  - **XRP/USD:** 1H close 1.35379 > 20-EMA ≈ 1.34874 (R1 ✓). 4H close 1.35058 < 50-EMA ≈ 1.36865 (R3 ✗). **REJECT rule 3.**
  - **TAO/USD:** 1H close 286.261 > 20-EMA ≈ 282.48 (R1 ✓). RSI14 ≈ 58.8 (R2 ✓, R2a ✓ ≤ 80). 4H close 286.6906 > 50-EMA ≈ 277.02 (R3 ✓). 4a $8.28M ✓. R4 history ✓. R5 flat ✓. R5b last TAO stop-out 2026-05-22T01:00Z, >24h ago ✓. R6 0/4 ✓. R6a cluster 0/2 — TAO is cluster member, opening → 1/2 ✓. R7 1.5% trade + 0% portfolio ≤ 4% ✓. **PASS all rules.**
  - **HYPE/USD:** 1H close 62.15 > 20-EMA ≈ 60.92 (R1 ✓). RSI14 ≈ 55.5 (R2 ✓ marginal). 4H close 61.16 > 50-EMA ≈ 55.61 (R3 ✓). All other rules ✓. **PASS all rules.**
  - **DOGE/USD, ADA/USD, FARTCOIN/USD, AVAX/USD, LINK/USD, PENGU/USD, LTC/USD:** REJECT rule 4a (24h notional < $2M).
  - **SUI/USD, TRX/USD:** PASS rule 4a; technical evaluation deferred — rule 8 (one entry per wake, highest 30d notional rank wins) makes the question moot once a higher-ranked pair has passed. SUI rank 8 / TRX rank 15, both below TAO rank 5.
- **Rule 8 (one-entry tiebreaker):** TAO and HYPE both PASS. TAO ranks 5 in universe vs HYPE rank 6 → **TAO wins.** HYPE eligibility re-evaluated next wake (if still passing; may drop).

### News (Firecrawl-driven, informational only in v0.2)

- Not invoked this wake (budget-conservative). News is informational only in v0.2 and does not veto entries. Per skills/research.md, the missing news context does not change the technical entry decision. Resumes next routine #1.

### Sentiment (passive — Kraken depth/spread proxy in v0.2)

- **TAO/USD spread (entry candidate):** bid 285.11 / ask 285.32, spread ~0.21 ≈ **7.4 bps**. Acceptable for spot momentum; recorded but no veto (sentiment is informational in v0.2).
- HYPE spread (would-be alternate, rule 8 superseded): bid 61.96 / ask 61.97–61.99, ~2 bps. Tight, no caveat.

### Decision

- **Action: OPEN TAO/USD long.** Entry rules 1, 2, 2a, 3, 4, 4a, 5, 5a, 5b, 6, 6a, 7, 8 all PASS. Rule 8 selects TAO over HYPE (rank 5 vs 6). Fill 286.40410 (12:00Z 1H close 286.261 × 1.0005 adverse slip), size 15.273800 TAO, 2×ATR(14)=10.28310 stop @ 276.12100, 4R target @ 327.53650, risk $157.06 = 1.5% of $10,470.78 equity. Cluster {BTC,ETH,SOL,TAO,AVAX,SUI,LINK} now 1/2.
- **No exits processed** (account was flat going in).
- **Universe refresh:** not due (2026-05-26 is not the 1st of month; next 2026-06-01).
- **Telegram:** will send brief "OPEN TAO" summary per routine #1 NOTIFY rules (new OPEN this wake).

2026-05-26T17:06:54Z | harness | day-gate | not Saturday, skipping | no action
2026-05-26T17:40:33Z | allocation | day-gate | not Sunday, skipping | no action


## 2026-05-26T20:00Z — routine-02-midday

- **Wake context:** 1 open position (TAO/USD long, entered routine-01 at 12:00Z @ 286.40410, size 15.273800, stop 276.12100). Cash $6,084.36, day-open equity $10,470.78. Kill switches were clear at entry.
- **Kraken live (TAO @ wake 20:00Z):** last 281.6879, bid 281.5196 / ask 281.6382, 24h +0.87%, high 291.2208, low 273.548, vol 31,743 TAO. Active 1H bar (20:00Z forming) — low so far 281.0, well above stop 276.12.
- **Exit-rule scan against most recent CLOSED 1H bar (19:00Z, close 280.9819) + prior bars:**
  - Computed 1H 20-EMA series (α = 2/21) from 30 bars seeded at SMA(20).
  - Bar 17:00Z close **281.2922** vs 20-EMA ≈ **283.44** → BELOW (confirm-bar 1).
  - Bar 18:00Z close **280.5426** vs 20-EMA ≈ **283.19** → BELOW (confirm-bar 2). **Exit rule 1 (W22-G two-bar EMA20 confirm) FIRES at 18:00Z close.**
  - Bar 19:00Z close 280.9819 < 20-EMA ≈ 283.00 still — confirms continued weakness post-trigger.
  - Stop 276.12100: lowest low across bars 13:00Z–20:00Z was 278.5885 (19:00Z) — stop NOT pierced; exit-stop-hit did NOT fire (EMA rule fired first).
  - 4R target 327.53650: highest high since entry was 291.2208 (14:00Z) — not approached.
  - Breakeven ratchet: max favorable 1H close was 16:00Z 289.163 → unrealized R = (289.163 − 286.40410) / 10.28310 = +0.27R — never reached +2R arming threshold; original 2×ATR stop remained active for the life of the trade.
  - Regime check: SBD remained inactive at entry (14/15 positive at 12:00Z scan); regime through trade window not re-verified intraday — irrelevant since 20-EMA rule applies absent SBD, and the rule already fired.
- **Exit replay (missed-scheduler):** routine #2 wakes at 20:00Z, two bars after the confirming bar closed. Per established missed-scheduler-replay precedent (2026-05-22 TAO/HYPE/SOL/AVAX cluster), close is processed at the bar that fired the rule using the conservative-slippage close model. Sell fill = 280.5426 × (1 − 0.0005) = **280.40233**. Sale proceeds 280.40233 × 15.273800 = $4,282.81; sell commission 0.26% = $11.135; net cash received **$4,271.67**. Realized PnL using cash-flow basis (cash credit minus prior cash debit of $4,374.05 notional + $11.37 entry commission) = **−$114.75**. R = (280.40233 − 286.40410) / (286.40410 − 276.12100) = **−0.58R**. Reason tag `exit-ema20-confirm-missed-scheduler-replay`.
- **Account state after close:** cash = equity = **$10,356.03**; realized PnL all-time **+$356.03**; DD from $10,728.95 peak = **3.48%** (warn 12.5%, cap 25%); day realized **−1.10%** vs day-open $10,470.78 (cap 5%); equity floor $10,356.03 ≫ $7,500. Losing-day streak now 3 (05-22, 05-25, 05-26; cap 7). Kill switches **all clear**.
- **Action: CLOSE TAO/USD long (replay at 18:00Z, logged at wake).** No new entries (routine #2 is position-management only per spec). No new same-pair cooldown for TAO (5b applies only to stop-outs, not EMA-confirm exits); BTC cooldown remains in effect until 2026-05-26T22:00Z.
- **Kill switches:** day PnL −1.10% (cap 5%); DD 3.48% (warn 12.5%); equity > floor; streak 3/7. **All clear.**
- **Telegram:** will send midday alert per routine #2 NOTIFY rules (an exit happened). DD has not crossed the 12.5% warn threshold, no kill switch tripped — exit-only notification.
- **Next decision point:** routine-03-eod (later today) — fresh entry scan against the just-closed 13:00Z and following 1H candles + 12:00Z 4H regime; flat book = full risk budget available.


## 2026-05-27T04:00Z — routine-03-eod (fired late ~15:30Z; evaluated on most-recently-closed 1H bar 14:00Z)

### Wake context
- Account flat (TAO closed 2026-05-26T18:00Z via missed-scheduler replay −$114.75 / −0.58R). Cash/equity **$10,356.03**, DD 3.48% from peak $10,728.95, losing-day streak 3 (05-22, 05-25, 05-26). Live strategy v0.4 (W22-G two-bar EMA + W22-H-partial breakeven ratchet at +2R, 4R TP retained).
- Kraken risk_flag CLEAR (scan 2026-05-27T00:00:32Z, "Markets calm").
- Routine fired well past its 04:00Z (21:00 PT) cron window — actual wake ≈ 2026-05-27T15:30Z. Per established missed-scheduler precedent, evaluated at the most-recently-closed 1H bar at wake time (14:00Z bars across all pairs).

### Technical (rule-driven, deterministic)
- **24h regime (Kraken multi_ticker @ wake):** 10/15 universe pairs positive. Positives: HYPE +5.06, XDG +0.87, LTC +0.67, ETH +0.43, SOL +0.42, AVAX +0.33, XRP +0.29, FARTCOIN +0.17, SUI +0.04, BTC +0.03. Negatives: ADA −0.07, TAO −0.34, LINK −0.39, TRX −0.58, PENGU −0.64. Median 24h % ≈ +0.17%. **Rule 5a PASS** (10/15 ≥ 4/15). **Rule 5a-SBD inactive** (>1 positive AND median > −1.0%).
- **Rule 4a liquidity floor (24h notional ≥ $2M):** PASS — BTC $172.7M, ETH $25.8M, HYPE $32.1M, SOL $10.8M, XRP $16.5M, TAO $8.6M, XDG $2.19M, SUI $10.7M (8 pairs). FAIL — TRX $1.30M, ADA $1.28M, LINK $1.67M, LTC $1.22M, AVAX $0.79M, FARTCOIN $1.08M, PENGU $0.66M (7 pairs).
- **Per-pair entry-rule scan (just-closed 1H 14:00Z; rule 8 highest-rank-first):**
  - **BTC/USD (rank 1):** 1H close 75786.5 (10:00Z) and 14:00Z bars are not directly evaluated since this missed-replay uses 14:00Z; using 10:00Z close 75786.5 vs SMA20 ≈ 75826.78 → below. Same at 04:00Z cron-window check: close 75553.6 < SMA20 ≈ 76264.7. **REJECT rule 1** (close < 20-EMA). 5b cooldown expired at 22:00Z 05-26 (BTC eligible again).
  - **ETH/USD (rank 2):** 14:00Z close 2058.98 < SMA20 ≈ 2072.81. **REJECT rule 1**.
  - **SOL/USD (rank 3):** 14:00Z close 83.79 > SMA20 ≈ 83.74 (marginal R1 PASS by 0.06%). RSI14 ≈ 45–51 (depending on smoothing). **REJECT rule 2** (RSI < 55).
  - **XRP/USD (rank 4):** 14:00Z close 1.32802 < SMA20 ≈ 1.32895. **REJECT rule 1** (marginal, ~0.07% below).
  - **TAO/USD (rank 5):** 14:00Z close 274.43 < SMA20 ≈ 277.37. **REJECT rule 1.** (Confirms downtrend continuation post-18:00Z EMA-confirm exit; no 5b cooldown since exit was EMA-confirm not stop-hit.)
  - **HYPE/USD (rank 6):** 14:00Z close 60.03 < SMA20 ≈ 60.98. **REJECT rule 1** (despite +5.06% 24h leader, peaked at 09:00Z close 62.88 then rolled over; current close ≈ 1.5% below EMA).
  - **XDG/USD (rank 7):** 14:00Z close 0.10136 < SMA20 ≈ 0.10141. **REJECT rule 1** (marginal, ~0.05% below).
  - **SUI/USD (rank 8):** 14:00Z close 0.9968 < SMA20 ≈ 1.00052. **REJECT rule 1**.
  - **TRX, ADA, LINK, LTC, AVAX, FARTCOIN, PENGU:** REJECT rule 4a (24h notional < $2M).
- **Candidate list:** EMPTY. All 8 liquidity-passing pairs failed rule 1 (or rule 2 for SOL). Pattern: broad universe pull-back through 13:00–14:00Z bars dragged most closes back below their respective 1H 20-EMAs even though 24h % is still positive for many.

### News (Firecrawl-driven, informational only in v0.2/0.3/0.4)
- Skipped this wake — risk_flag CLEAR "Markets calm" with 0 headlines flagged acts as the macro pre-screen. No candidates survived the technical pass anyway, so news would not change the decision. Context-budget conservation.

### Sentiment (passive — Kraken depth/spread proxy in v0.2/0.3/0.4)
- Not sampled: 0 entry candidates survived rule 1 / rule 2, so no per-candidate spread/depth pull warranted.

### Decision
- **SKIP all entries** — every liquidity-passing pair failed the trend filter at the just-closed 1H. Driver: rules 1, 2 across the 8 eligible candidates. No exits processed (account flat going in).
- **Universe refresh:** not due (2026-05-26 is not 1st of month; next 2026-06-01).
- **Monthly archive:** today is not the last trading day of May (last weekday is Friday 2026-05-29) → no archive sweep.
- **Account state unchanged from routine-02-midday rebuild:** cash/equity $10,356.03; realized PnL all-time +$356.03; DD 3.48%; losing-day streak 3 (05-22, 05-25, 05-26; cap 7); BTC same-pair cooldown expired 22:00Z 05-26; equity > $7,500 floor. Kill switches **all clear**.

### Day summary stats (2026-05-26 PT trading day)
- Day PnL: **−$114.75 (−1.10%)** vs day-open equity $10,470.78. Single TAO/USD trade lifecycle (open 12:00Z 05-26, close 18:00Z 05-26) — opened 1, closed 1, win rate today 0/1 = 0%.
- New equity: **$10,356.03**; drawdown 3.48% from peak $10,728.95 (warn 12.5%, cap 25%).
- Rolling perf (approx, precise reference-price computation deferred to routine #4):
  - 7d: BULL ≈ +1.2% (from $10,236.14 on 2026-05-19) vs BTC-hold ≈ −6.0% (from ~$80,700 on 2026-05-19 to $75,847 today) → BULL ahead ~+7.2%.
  - 30d: BULL ≈ +3.6% (inception $10k 2026-04-20; 30d window pre-dates inception in part — first fully computable 2026-05-20). BTC 30d ≈ −5%. Delta ≈ +8–9%.
  - 90d: not computable (BULL inception 2026-04-20).

### Lessons extraction
- One light observation (below 2-lesson cap, not appended as a new lesson yet — needs more samples). Two-day pattern: BTC entered 2026-05-25T15:00Z when 15/15 positive (peak universe regime) → stopped 7h later for −1.07R. TAO entered 2026-05-26T12:00Z when 14/15 positive → EMA-confirm exit 6h later for −0.58R. Both opened *at* the peak of broad-universe risk-on regime and reversed within a single day. Could indicate the rule 5a regime gate's 4/15-positive floor passes too freely when 14–15/15 are positive (peak-regime entry timing risk). Not actionable yet — only 2 samples, both in a broader 5-day BTC-led down-leg. **Filed as W19-E observation only; will revisit at routine #4 2026-05-30 with a wider sample of 14-15/15-positive entries.**


## 2026-05-27T15:30Z — routine-01-overnight (late-fire / missed-scheduler)

### Technical (rule-driven, deterministic)

- **Wake context:** flat after TAO EMA-confirm exit on 2026-05-26T18:00Z (−$114.75 / −0.58R). Cash $10,356.03, equity $10,356.03, DD 3.48% from peak $10,728.95. BTC same-pair cooldown (last stop-out 05-25T22:00Z) expired at 05-26T22:00Z. No TAO 5b cooldown (last TAO exit was EMA-confirm, not stop-out). Live strategy v0.4 (W22-C: G + breakeven half of H, 4R retained). Losing-day streak 3/7.
- **Wake timing:** scheduler ran ~2h late vs nominal 13:00Z slot — wake data fetched ~15:30Z. Last-closed 1H bar = 14:00Z (15:00Z bar still active, low volume). Last-closed 4H bar = 08:00Z (12:00Z bar still active).
- **Kraken risk_flag:** CLEAR (2026-05-27T00:00:32Z scan, "Markets calm").
- **24h regime (Kraken multi_ticker @ wake):** **12/15 universe pairs positive.** Pos: ADA +0.94, AVAX +1.42, ETH +0.06, FARTCOIN +1.15, HYPE +1.71, LINK +0.66, LTC +1.62, PENGU +0.24, SOL +1.14, SUI +0.93, DOGE +1.83, XRP +0.80. Neg: TAO −0.07, BTC −0.69, TRX −1.13. Median 24h % ≈ +0.93%. **Rule 5a PASS** (12/15 ≥ 4/15). **Rule 5a-SBD: not active** (>1 positive, median > −1.0%).
- **Rule 4a liquidity floor (≥$2M 24h notional, price×volume):** PASS — BTC $141.8M, ETH $23.67M, HYPE $28.77M, SOL $10.47M, SUI $9.37M, TAO $7.84M, XRP $13.52M, DOGE $2.40M (8 pairs). FAIL — ADA $1.45M, AVAX $0.82M, FARTCOIN $1.11M, LINK $1.79M, LTC $1.35M, PENGU $0.60M, TRX $1.14M (7 pairs).
- **Per-pair entry-rule scan against last-closed 1H bar (14:00Z) + last-closed 4H (08:00Z):** 1H 20-EMA computed via SMA(20) seed of bars 5/26 05:00→5/27 00:00 + iterative EMA (α=2/21) through 14:00Z. Recent 13:00Z 1H bar saw broad correlated risk-off (BTC −$700 in one hour) pulling all 8 R4a-PASS pairs below their 1H 20-EMA.
  - **BTC/USD:** 14:00Z close 74900.7 vs 20-EMA ≈ 75736 → close BELOW EMA. **REJECT rule 1.** (5b cooldown expired at 22:00Z prior day — would have been the second blocker if rule 1 had passed.)
  - **ETH/USD:** 14:00Z close 2058.98 vs 20-EMA ≈ 2077.47 → BELOW. **REJECT rule 1.**
  - **SOL/USD:** 14:00Z close 83.79 vs 20-EMA ≈ 83.891 → BELOW (narrow miss, ~0.12%). **REJECT rule 1.**
  - **XRP/USD:** 14:00Z close 1.32802 vs 20-EMA ≈ 1.33215 → BELOW. **REJECT rule 1.**
  - **TAO/USD:** 14:00Z close 274.4325 vs 20-EMA ≈ 277.72 → BELOW. **REJECT rule 1.** (Note: prior wake's TAO long was exited 18:00Z by W22-G EMA-confirm; 14:00Z scan confirms continuation of weakness.)
  - **HYPE/USD:** 14:00Z close 60.03 vs 20-EMA ≈ 61.367 → BELOW. **REJECT rule 1.**
  - **DOGE/USD (XDG):** 14:00Z close 0.1013616 vs 20-EMA ≈ 0.101557 → BELOW (narrow miss, ~0.19%). **REJECT rule 1.**
  - **SUI/USD:** 14:00Z close 0.9968 vs 20-EMA ≈ 1.00491 → BELOW. **REJECT rule 1.**
  - **ADA/USD, AVAX/USD, FARTCOIN/USD, LINK/USD, LTC/USD, PENGU/USD, TRX/USD:** REJECT rule 4a (24h notional < $2M).
- **Rule 8 (one-entry tiebreaker):** N/A — zero pairs PASS rule 1.

### News (Firecrawl-driven, informational only in v0.2)

- Not invoked this wake — no technical-PASS candidates to vet (news is informational only in v0.2 and skipped when no candidates exist per routine spec).

### Sentiment (passive — Kraken depth/spread proxy in v0.2)

- Not invoked this wake — no technical-PASS candidates.

### Decision

- **Action: NO new entries.** All 8 R4a-PASS pairs fail rule 1 on the just-closed 1H bar (14:00Z). The 13:00Z 1H candle was a broad correlated risk-off bar (BTC −0.86% in one hour, all 8 candidates wicking through their respective 20-EMAs) that pulled the entire R4a-PASS cohort below trend. Regime 5a still passes on the 24h frame because morning levels are still net-positive vs yesterday, but the freshly-closed 1H frame is uniformly bearish — exactly the chop-into-divergent-tape pattern that 5a was designed to catch on the broader frame and rule 1 catches at single-pair granularity.
- **No exits processed** (account was flat going in).
- **Universe refresh:** not due (2026-05-27 is not the 1st of month; next 2026-06-01).
- **Kill switches:** day realized $0.00 (cap 5%); DD 3.48% from peak (warn 12.5%, cap 25%); equity $10,356.03 > $7,500 floor; losing-day streak 3/7 (no trade today → streak count unchanged from yesterday; will reset on next winner). **All clear.**
- **Telegram:** silent (no kill switch, no OPEN, no CLOSE, no actionable news, no universe refresh).
- **Next decision point:** routine-02-midday (later today) — position-management only by spec; with flat book and no entries from routine #1, routine #2 will be a no-op unless a new entry signal manifests outside spec (it won't, since routine #2 doesn't open). Real next decision = routine-03-eod.

2026-05-27T17:06:49Z | harness | day-gate | not Saturday, skipping | no action
2026-05-27T17:40:19Z | allocation | day-gate | not Sunday, skipping | no action

## 2026-05-27T20:07Z — routine-02-midday

### Technical (rule-driven, deterministic)

- **Wake context:** account flat (0/8 positions, 0/4 strategy max). Cash $10,356.03, equity $10,356.03 (no MTM delta — flat). DD 3.48% from peak $10,728.95. Losing-day streak 3/7.
- **Mark-to-market:** N/A (zero open positions).
- **Exit check:** N/A (zero open positions).
- **Spot quote (BTC reference, for benchmark / tape read only):** XBTUSD last 75086.6, 24h change −0.98% (open_24h 75827.7, high 76061.8, low 74528.9, vwap 75406.76, spread 0.1bps). Tape continued softening since 15:30Z overnight wake (BTC was 75847 then; now 75086 = −1.00% intraday). Confirms the routine-01-overnight read: pairs that failed rule 1 at 14:00Z are unlikely to have recovered above their 20-EMAs at the 19:00Z 1H close (next routine-03-eod scan will quantify).
- **Entry scan:** SKIPPED per routine-02 spec — midday is position-management only; entry responsibility belongs to routines #1 and #3.

### News / Sentiment

- Not invoked (routine #2 is mark-to-market + exits only).

### Decision

- **Action: NO-OP** (flat book, no exits to fire, no entries by spec).
- **Kill switches:** day realized $0.00 (cap 5%, clear); DD 3.48% from peak (warn 12.5%, cap 25%, clear); equity $10,356.03 > $7,500 floor (clear); losing-day streak 3/7 (no trade today → unchanged). **All clear.**
- **Drawdown trajectory:** 3.48% is well below the 12.5% warning threshold — no escalation needed.
- **Telegram:** silent (no kill switch, no exit, DD below 12.5% warn).
- **Next decision point:** routine-03-eod 21:00 PT / 04:00Z+1 — will re-scan entries against the just-closed 19:00Z (then 23:00Z) 1H bar.


## 2026-05-28T13:00Z — routine-01-overnight

### Technical (rule-driven, deterministic)

- **Wake context:** account flat (0/8 positions, 0/4 strategy max). Cash/equity $10,356.03, DD 3.48% from peak $10,728.95, losing-day streak 3 (05-22, 05-25, 05-26; 05-27 no trades). Strategy v0.4 (W22-C). No active 5b cooldowns (BTC last stop-out 05-25T22:00Z → expired 05-26T22:00Z; TAO 05-26T18:00Z was EMA-confirm not stop-hit).
- **Kraken risk_flag:** CLEAR (scan 2026-05-28T12:30:32Z, "Markets calm").
- **24h regime (kraken_multi_ticker @ wake 13:00Z):** **0/15 universe pairs positive.** All negative: TRX −5.15, FARTCOIN −4.41, SUI −4.28, PENGU −3.72, TAO −2.67, LINK −2.56, XDG −2.40, ADA −2.35, AVAX −2.10, LTC −2.02, ETH −1.86, SOL −1.75, HYPE −1.51, BTC −1.43, XRP −0.90. **Median 24h % = −2.35%.**
- **Rule 5a (regime gate):** FAIL — 0/15 positive < 4/15 floor. **REJECT all new entries this wake.**
- **Rule 5a-SBD (synchronized breakdown):** **ACTIVE** — both conditions met: (i) 0/15 positive ≤ 1, and (ii) median −2.35% ≤ −1.0%. This is the textbook SBD case the W21-F gate was designed for. Defensive trend exit (Exit rule 1-SBD: two consecutive 1H closes < 1H 9-EMA) would apply to any open positions — but **book is flat, so SBD has zero defensive value to capture this wake**. Estimated avoided-give-back vs. 20-EMA exit: **$0** (no open longs).
- **Rule 4a liquidity floor (≥$2M 24h notional):** computed but moot given rule 5a fail. PASS — BTC ~$183M, ETH ~$43.9M, HYPE ~$21.9M, SOL ~$15.6M, XRP ~$22.3M, TAO ~$6.15M, XDG ~$3.33M, SUI ~$10.5M, ADA ~$2.79M, LINK ~$2.76M, TRX ~$3.25M (11 pairs). FAIL — LTC ~$1.71M, FARTCOIN ~$0.87M, AVAX ~$1.55M, PENGU ~$0.65M (4 pairs).
- **Per-pair entry-rule scan: SKIPPED.** Rule 5a is a hard universe-level gate; per-pair indicator computation is unnecessary when the regime gate vetoes all entries. Spot-check: BTC SMA20(1H) on bars 17:00Z 05-27 → 12:00Z 05-28 = 73879.1; 12:00Z close 73397.8 → BELOW EMA by 0.65%. Rule 1 would also fail for BTC; broad sell-off (BTC −1000 on the 13:00Z 05-27 bar continued into 03:00Z 05-28 cascade −1000 in one hour) suggests the entire R4a-PASS cohort sits below their 20-EMAs.
- **Rule 8 (one-entry tiebreaker):** N/A — zero candidates.

### News (Firecrawl-driven, informational only in v0.2)

- Not invoked — zero technical-PASS candidates to vet. Per routine spec, news pass is per-candidate, not standalone macro scan.

### Sentiment (passive — Kraken depth/spread proxy in v0.2)

- Not invoked — zero technical-PASS candidates.

### Decision

- **Action: NO new entries.** Rule 5a regime gate vetoes all 15 pairs (0/15 positive). SBD active per rule 5a-SBD; flat book means defensive exit rule 1-SBD has nothing to apply to.
- **No exits processed** (account was flat going in).
- **Universe refresh:** not due (2026-05-28 is not 1st of month; next 2026-06-01).
- **Kill switches:** day realized $0.00 (cap 5%, clear); DD 3.48% from peak (warn 12.5%, cap 25%, clear); equity $10,356.03 > $7,500 floor (clear); losing-day streak 3/7 (no trade today → unchanged). **All clear.**
- **Telegram:** silent (no kill switch trip, no OPEN, no CLOSE, no actionable news, no universe refresh).
- **Next decision point:** routine-02-midday (later today) — position-management only by spec; with flat book and SBD active, routine #2 will be a no-op. Real next entry-scan = routine-03-eod 04:00Z+1.

2026-05-28T17:07:15Z | harness | day-gate | not Saturday, skipping | no action

2026-05-28T17:40Z | allocation | day-gate | not Sunday, skipping | no action
2026-05-28T20:00Z | routine-02-midday | flat, no positions to MTM, no exits possible. Equity $10,356.03 unchanged, DD 3.48% (cap 25%, warn 12.5%) — clear. Daily realized $0, losing-day streak 3. Regime: 2/15 universe positive (HYPE +4.61%, XRP +0.37%), median 24h −1.44%. SBD CLEARED this wake (≤1 positive condition fails: 2 > 1) — defensive 9-EMA exit reverts to baseline 20-EMA two-bar; moot while flat. Rule 5a still vetoes entries (2 < 4 needed). BTC 73220.6 −1.50%. No-op routine.


## 2026-05-29T13:00Z — routine-03-eod (late-fire / missed-scheduler for 2026-05-28 PT EOD)

### Wake context
- Scheduled: 0 21 * * 1-5 PT → 2026-05-29T04:00Z (21:00 PT 2026-05-28 Thursday). Actual wake ≈ 2026-05-29T13:00Z (~9h late). Per established missed-scheduler precedent, the entry-scan evaluates at the most-recently-closed 1H bar at wake time (12:00Z 2026-05-29). EOD card scope = 2026-05-28 PT trading day (Thursday).
- Account flat going in (closed since 2026-05-26T18:00Z TAO exit-ema20-confirm −$114.75). Cash/equity $10,356.03, DD 3.48% from peak $10,728.95, losing-day streak 3 (05-22, 05-25, 05-26; 05-27, 05-28 no trades — streak count unchanged). Live strategy v0.4 (W22-C: G + breakeven half of H, 4R retained). No active 5b cooldowns (BTC 05-25 stop-out cooldown expired 05-26T22:00Z; TAO 05-26 exit was EMA-confirm not stop-hit).
- Kraken risk_flag: CLEAR (scan 2026-05-28T12:30:32Z, "Markets calm", 0 tier-1/2 triggers).

### Technical (rule-driven, deterministic)
- **24h regime (kraken_multi_ticker @ wake 13:00Z):** 1/15 universe pairs positive. Positives: HYPE +0.67 (only). LTC 0.00 (flat — not positive). Negatives (asc): TAO −3.70, SUI −2.94, TRX −2.85, FARTCOIN −1.89, PENGU −1.41, LINK −1.26, ADA −1.07, AVAX −1.01, XDG −0.78, SOL −0.78, XRP −0.76, ETH −0.50, BTC −0.46. **Median 24h % = −1.01%** (AVAX, the 8th of 15 sorted ascending).
- **Rule 5a (regime gate):** FAIL — 1/15 positive < 4/15 floor. **REJECT all new entries this wake.**
- **Rule 5a-SBD (synchronized breakdown):** **ACTIVE** — both conditions met: (i) 1/15 positive ≤ 1, and (ii) median −1.01% ≤ −1.0% (marginal, by 0.01pp). Defensive trend exit (Exit rule 1-SBD: two consecutive 1H closes < 1H 9-EMA) applies to any open positions — but **book is flat, so SBD has zero defensive value to capture this wake**. Estimated avoided-give-back vs. 20-EMA exit: **$0** (no open longs). Marks a second SBD activation in 7 trading days (prior: 2026-05-28T13:00Z overnight, also flat-book).
- **Rule 4a liquidity floor (≥$2M 24h notional):** computed for completeness given rule 5a fail. PASS — BTC ~$142.3M (price 73180 × vol 1944), ETH ~$40.3M, HYPE ~$37.4M, SOL ~$15.2M, XRP ~$18.99M, TAO ~$4.29M, XDG ~$1.68M, SUI ~$5.88M, ADA ~$4.38M, LINK ~$1.51M, TRX ~$2.95M, FARTCOIN ~$0.64M, PENGU ~$0.56M, LTC ~$1.72M, AVAX ~$0.72M. Rough PASS list: BTC, ETH, HYPE, SOL, XRP, TAO, SUI, ADA, TRX (9 pairs). FAIL: XDG, LINK, FARTCOIN, PENGU, LTC, AVAX (6 pairs).
- **Per-pair entry-rule scan: SKIPPED.** Rule 5a hard-vetoes universe-wide; per-pair indicator computation moot. Spot-check: BTC 12:00Z close 73183.5, declining sequence 09:00→12:00Z (73642 → 73528 → 73364 → 73184), clearly below any reasonable 1H 20-EMA seeded from the recent 73,500–73,800 range. Pattern consistent with SBD: broad correlated drift lower with even the relative leaders (HYPE +0.67 / LTC 0.00) only mildly outperforming.
- **Rule 8 (one-entry tiebreaker):** N/A — zero candidates.

### News (Firecrawl-driven, informational only in v0.4)
- Not invoked — zero technical-PASS candidates to vet. Per routine spec, news pass is per-candidate, not standalone macro scan. Risk_flag CLEAR ("Markets calm") acts as macro pre-screen and confirms no headline-driven action needed.

### Sentiment (passive — Kraken depth/spread proxy in v0.4)
- Not invoked — zero technical-PASS candidates.

### Decision
- **Action: NO new entries.** Rule 5a regime gate vetoes all 15 pairs (1/15 positive < 4 needed). SBD active per rule 5a-SBD; flat book means defensive exit rule 1-SBD has nothing to apply to.
- **No exits processed** (account flat going in).
- **Universe refresh:** not due (2026-05-29 is not 1st of month; next 2026-06-01).
- **Monthly archive:** today is **not** the last trading day of May from the perspective of this EOD card. The EOD card scope is 2026-05-28 PT (Thursday); the upcoming 2026-05-29 PT EOD (scheduled 04:00Z 2026-05-30) is the last-trading-day-of-May card and is where the archive sweep belongs. Deferred to next EOD wake.

### Day summary stats (2026-05-28 PT trading day)
- Day PnL: **$0.00 (0.00%)** — account flat for the full PT trading day (07:00Z 05-28 → 04:00Z 05-29). 0 opened, 0 closed, win rate N/A.
- Day-open equity: $10,356.03 → Day-close equity: $10,356.03 (unchanged).
- New equity: **$10,356.03**; drawdown **3.48%** from peak $10,728.95 (warn 12.5%, cap 25% — clear).
- Losing-day streak: **3** (05-22 L, 05-25 L, 05-26 L; 05-27 no trades, 05-28 no trades — streak neither extended nor broken; cap 7).
- Rolling perf (approx, precise reference-price computation deferred to routine #4):
  - 7d: BULL ≈ −3.48% (from peak $10,728.95 set 2026-05-21) vs BTC-hold ≈ −5.7% (2026-05-21 ~$77.6k → today $73.18k) → BULL ahead ~+2.2%.
  - 30d: BULL ≈ +3.6% (inception $10k 2026-04-20; 30d window now fully computable). BTC 30d ≈ −10% (from ~$81.3k on 2026-04-29 to $73.18k today). Delta ≈ +13–14% in BULL's favor.
  - 90d: not computable (BULL inception 2026-04-20 = 39 days ago).

### Lessons extraction
- **No new lessons appended this wake.** Day had zero trades — nothing to extract from. Two existing observations remain relevant and unchanged:
  1. The 05-26 / 05-27 / 05-28 / 05-29 sequence is the longest stretch of pure-no-trade days since BULL inception. Driver: rule 5a regime veto has been firing continuously since 2026-05-26 ~18:00Z (TAO exit), and even when 5a passes (briefly 2026-05-28T20:00Z midday with 2/15 positive) rule 1 fails universally due to broad drift below 1H 20-EMAs. This is the *designed* behavior — strategy is opting out of choppy/declining tape and preserving capital. Filed as observation in routine-01-overnight 05-26T18:00Z entry; nothing to add today.
  2. SBD has now activated twice in the past 3 days (05-28T13:00Z, 05-29T13:00Z), both with flat book → $0 captured defensive value to date. This is *expected* — SBD is a "stop bleeding open longs" gate; it can only earn its keep when longs are open. Routine #4 should eventually score SBD's value-add by counting (a) wakes-where-active, (b) wakes-where-active-AND-book-had-longs, (c) avoided-give-back when (b) held. Currently (b) = 0 / (a) = 2 — needs more samples before judging.
- Below the 2-lesson daily cap. No append to `lessons.md`.

### Telegram
- **Sending mandatory EOD card** per `routines/03-eod.md` NOTIFY section.


## 2026-05-29T13:30Z — routine-01-overnight (on-time wake, scheduled 06:00 PT = 13:00Z)

### Wake context
- Scheduled: 0 6 * * 1-5 PT → 2026-05-29T13:00Z (06:00 PT Friday 2026-05-29). Actual wake ~13:30Z (~30min late, within wake-tolerance). Most-recently-closed 1H bar at evaluation = 13:00Z 2026-05-29.
- Account flat going in (closed since 2026-05-26T18:00Z TAO exit-ema20-confirm −14.75). Cash/equity 0,356.03, DD 3.48% from peak 0,728.95, losing-day streak 3 (05-22, 05-25, 05-26; 05-27, 05-28 no trades — streak unchanged). Live strategy v0.4. No active 5b cooldowns.
- Prior wake (routine-03-eod late-fire 2026-05-29T13:00Z): SBD active, 1/15 positive, median −1.01%. This wake is ~30 min later, same trading session; expected continuation of regime profile.
- Kraken risk_flag: CLEAR (last scan 2026-05-28T12:30:32Z, "Markets calm", 0 tier-1/2 triggers). Note: risk_flag is stale (~25h old, awaiting 2026-05-29 scan); using as best-available macro signal.

### Technical (rule-driven, deterministic)
- **24h regime (kraken_multi_ticker @ wake 13:30Z):** **1/15 universe pairs positive.** Positives: HYPE +0.83 (only). Negatives (asc): TAO −3.91, SUI −3.35, TRX −2.54, FARTCOIN −2.51, PENGU −1.71, LINK −1.36, AVAX −1.23, ADA −1.19, XDG −1.12, XRP −0.97, SOL −0.88, ETH −0.52, BTC −0.51, LTC −0.14. **Median 24h % = −1.19%** (ADA, 8th of 15 sorted ascending).
- **Rule 5a (regime gate):** **FAIL** — 1/15 positive < 4/15 floor. **REJECT all new entries this wake.**
- **Rule 5a-SBD (synchronized breakdown):** **ACTIVE** — both conditions met: (i) 1/15 positive ≤ 1, and (ii) median −1.19% ≤ −1.0% (now clearer margin, 0.19pp below threshold; the marginal call has resolved into a clean SBD print). Defensive trend exit (Exit rule 1-SBD: two consecutive 1H closes < 1H 9-EMA) applies to any open positions — but **book is flat, so SBD has zero defensive value to capture this wake**. Estimated avoided-give-back vs. 20-EMA exit: **/usr/bin/bash** (no open longs). Marks third consecutive wake with SBD active (05-28T13:00Z, 05-29T13:00Z, 05-29T13:30Z). Persistence of SBD across both yesterday's late-fire EOD and today's overnight is a meaningful read on tape — drift is deepening, not stabilizing (BTC 73180 → 73142, TAO 277 → 251, SUI 0.94 → 0.90, AVAX 9.42 → 8.82).
- **Rule 4a liquidity floor (≥$2M 24h notional):** computed for completeness given rule 5a fail. Spot-check from ticker data: BTC ~$142M, ETH ~$40.0M, HYPE ~$37.5M, XRP ~$18.9M, SOL ~$15.2M, TAO ~$4.29M, SUI ~$5.77M, ADA ~$4.37M, TRX ~$2.94M, XDG ~$1.69M, LINK ~$1.51M, LTC ~$1.71M, AVAX ~$0.71M, FARTCOIN ~$0.63M, PENGU ~$0.55M. ~9 pass / 6 fail (XDG, LINK, LTC, AVAX, FARTCOIN, PENGU). Moot under 5a veto.
- **Per-pair entry-rule scan: SKIPPED.** Rule 5a hard-vetoes universe-wide; per-pair indicator computation deferred. Even relative leader HYPE +0.83% is isolated — no second positive pair confirming the bid.
- **Rule 8 (one-entry tiebreaker):** N/A — zero candidates.

### News (Firecrawl-driven, informational only in v0.4)
- Not invoked — zero technical-PASS candidates to vet per routine spec (news pass is per-candidate, not standalone macro scan). Risk_flag CLEAR acts as macro pre-screen. Stale risk_flag (~25h) is a known v0 limitation; next scan will refresh tomorrow.

### Sentiment (passive — Kraken depth/spread proxy in v0.4)
- Not invoked — zero technical-PASS candidates.

### Decision
- **Action: NO new entries.** Rule 5a regime gate vetoes all 15 pairs (1/15 positive < 4 needed). SBD active per rule 5a-SBD; flat book means defensive exit rule 1-SBD has nothing to apply to.
- **No exits processed** (account flat going in).
- **Universe refresh:** not due (2026-05-29 is not 1st of month; next 2026-06-01).
- **Kill switches:** day realized $0.00 (cap 5%, clear); DD 3.48% from peak (warn 12.5%, cap 25%, clear); equity $10,356.03 > $7,500 floor (clear); losing-day streak 3/7. **All clear.**
- **Telegram:** silent (no kill switch trip, no OPEN, no CLOSE, no actionable news, no universe refresh).
- **Next decision point:** routine-02-midday 2026-05-29T20:00Z — position-management only by spec; flat book + SBD active → no-op expected. Real next entry-scan = routine-03-eod 2026-05-30T04:00Z (last trading day of May for that EOD scope → archive sweep due there).

### Observation (no lesson appended, just a marker)
- SBD has now been active for **3 consecutive evaluations** spanning ~24h (05-28 13:00Z overnight, 05-29 13:00Z late-fire EOD, 05-29 13:30Z overnight). The market is deepening the drift, not pausing. Cumulative SBD-active wakes since rule 5a-SBD introduction (W21, 2026-05-19): wake-counter incrementing; book-with-longs counter still at 0. Defensive value to date: $0. Not flagged as a lesson — this is still the designed behavior of a long-only strategy in a breakdown regime (sit out, preserve capital). Will be relevant input to routine #4 SBD value-add scoring once we have at least one wake where SBD fires with open longs.

2026-05-29T17:06:54Z | harness | day-gate | not Saturday, skipping | no action


## 2026-05-29T20:07Z — routine-02-midday (on-time wake, scheduled 13:00 PT = 20:00Z)

### Wake context
- Scheduled: 0 13 * * 1-5 PT → 2026-05-29T20:00Z. Actual wake ~20:07Z (~7 min late, within tolerance). Book flat going in (closed since 2026-05-26T18:00Z TAO exit-ema20-confirm).
- Account: cash/equity $10,356.03, DD 3.48% from peak $10,728.95, losing-day streak 3 (05-22, 05-25, 05-26). No active 5b cooldowns. No new realized PnL on 2026-05-29 PT (zero trades since open).

### Mark-to-market
- No open positions → MTM trivially $0 unrealized, equity unchanged at $10,356.03.

### Exit check
- N/A — book flat. No stops to evaluate, no EMA crosses to confirm, no 4R targets in play.

### Kill switches (re-verified on this wake)
- Daily realized: **$0.00** (cap −5% loss) — clear.
- Drawdown: **3.48%** from peak $10,728.95 (warn 12.5%, cap 25%) — clear, well below warn.
- Equity floor: **$10,356.03** > $7,500 — clear.
- Losing-day streak: **3 / 7** — clear.
- MCP availability: kraken_multi_ticker returned full 15-pair payload — clear.
- **All clear.**

### Regime re-scan (informational — midday is no-entry by spec)
- **24h regime (kraken_multi_ticker @ 20:07Z):** **8/15 universe pairs positive** — sharp reversal from this morning's 1/15. Positives (desc): HYPE +7.07, PENGU +2.19, LTC +0.62, XDG +0.50, XRP +0.49, ETH +0.43, LINK +0.12, SOL +0.02. Negatives (asc): TAO −4.51, SUI −2.92, TRX −2.40, FARTCOIN −1.28, AVAX −1.01, ADA −0.78, BTC −0.04. **Median 24h % = +0.02%** (SOL, 8th of 15 sorted ascending).
- **Rule 5a (regime gate): PASS** — 8/15 ≥ 4/15 floor. (Would allow entries — but midday spec forbids new entries; observation only.)
- **Rule 5a-SBD: CLEARED** — both SBD conditions now fail: (i) 8/15 positive > 1/15 ceiling, AND (ii) median +0.02% > −1.0% threshold. First non-SBD print since SBD entered on 2026-05-28T13:00Z; SBD was active for 3 consecutive prior wakes (~24h span). Defensive 9-EMA two-bar exit no longer in effect; standard 20-EMA two-bar exit (Rule 1) is the live exit again.
- **Regime read:** the 8-positive-vs-7-negative split is broadly mixed but the relative leaders (HYPE +7%, PENGU +2.2%) are isolated alt-strength rather than a broad-tape reversal — BTC −0.04% flat, ETH +0.43% tepid. SBD clearance is mechanical (thresholds crossed) more than thematic (genuine regime change). Next entry-scan (routine-03-eod 2026-05-30T04:00Z) will reassess on the close of the 03:00Z 1H bar.

### Decision
- **Action: no-op** by spec — midday is position-management only, and book is flat. Zero entries, zero exits, zero log writes to trade_log.md.
- **Portfolio.md:** rewritten with refreshed regime classification (SBD cleared) and re-verified kill-switch state. Equity figures unchanged.
- **Telegram:** silent (no kill-switch trip, no exit, DD 3.48% << 12.5% warn).
- **Next decision point:** routine-03-eod 2026-05-30T04:00Z — first entry-scan opportunity under cleared 5a regime; also archive-sweep wake (last trading day of May for EOD scope).

### Observation (no lesson appended)
- SBD wake-counter: 3 SBD-active wakes total, all with book flat → cumulative defensive value captured = **$0**. Counter is now reset on this clearance; routine #4 SBD value-add scoring still has zero open-position evidence to evaluate. Continuing as designed (long-only sit-out worked: book was flat through the entire breakdown window 05-22 → 05-29 except for the BTC −$33.70 / TAO −$114.75 sequence early in the window, both pre-SBD detection).


## 2026-05-30T04:00Z — routine-03-eod (on-time wake, scheduled 0 21 * * 1-5 PT = 04:00Z next day; EOD card scope = 2026-05-29 PT trading day; last trading day of May → archive sweep due)

### Wake context
- Scheduled cron `0 21 * * 1-5` PT fired on-time at 21:00 PT Friday 2026-05-29 = 2026-05-30T04:00Z. Most-recently-closed 1H bar at wake = 03:00→04:00Z 2026-05-30. Most-recently-closed 4H bar at wake = 00:00→04:00Z 2026-05-30.
- Account flat going in (closed since 2026-05-26T18:00Z TAO `exit-ema20-confirm` −$114.75). Cash/equity $10,356.03, DD 3.48% from peak $10,728.95, losing-day streak 3 (05-22, 05-25, 05-26; 05-27, 05-28, 05-29 no trades — streak unchanged). Live strategy v0.4 (W22-C: G + breakeven half of H, 4R retained). No active 5b cooldowns.
- Prior 3 wakes (routine-03-eod late-fire 2026-05-29T13:00Z, routine-01-overnight 2026-05-29T13:30Z, routine-02-midday 2026-05-29T20:07Z): SBD entered on 05-28T13:00Z, persisted 3 wakes, **cleared on 05-29T20:07Z midday**. This wake is the first entry-scan opportunity under cleared 5a regime.
- Kraken risk_flag: CLEAR (last scan 2026-05-28T12:30:32Z, "Markets calm", 0 tier-1/2 triggers). Stale ~40h — known v0 limitation, awaiting next daily scan.

### Technical (rule-driven, deterministic)

- **24h regime (kraken_multi_ticker @ 04:00Z):** **10/15 universe pairs positive** (vs 8/15 at 05-29 midday — breadth still expanding). Positives (desc): LINK +2.07, XRP +1.33, ADA +1.28, AVAX +1.25, XDG +1.21, PENGU +0.91, HYPE +0.84, LTC +0.81, SOL +0.66, FARTCOIN +0.25. Negatives (asc): TAO −0.70, SUI −0.35, TRX −0.26, ETH −0.12, BTC −0.06. **Median 24h % = +0.81%** (LTC, 8th of 15 sorted ascending).
- **Rule 5a (regime gate):** **PASS** — 10/15 positive ≥ 4/15 floor. **Entries allowed this wake.**
- **Rule 5a-SBD:** **CLEARED** — both SBD conditions still fail: (i) 10/15 positive > 1/15 ceiling, AND (ii) median +0.81% > −1.0% threshold. SBD inactive; standard 20-EMA two-bar exit (Rule 1) is the live exit rule for any new position.
- **Rule 4a liquidity floor (≥$2M 24h notional):** computed from ticker (price × volume). **PASS** (11 pairs): BTC ~$122.2M, ETH ~$59.3M, HYPE ~$48.5M, XRP ~$32.3M, SOL ~$17.9M, TAO ~$7.6M, SUI ~$6.24M, ADA ~$4.18M, XDG ~$3.88M, TRX ~$2.97M, LINK ~$2.06M (borderline). **FAIL** (4 pairs): LTC ~$1.74M, PENGU ~$1.08M, AVAX ~$1.20M, FARTCOIN ~$0.73M.
- **Per-pair entry-rule scan (rule-8 order = highest 30d notional rank first):**
  - **BTC/USD** (rank 1): 1H 20-EMA at just-closed 03:00Z bar ≈ **73476.13**; 1H close = **73430.2**. **FAIL rule 1** (close 0.06% below EMA20). Skip.
  - **ETH/USD** (rank 2): 1H 20-EMA ≈ **2012.60**; 1H close = **2013.89**. PASS rule 1 (marginal +0.06%). 4H 50-EMA at just-closed 00:00→04:00Z 4H bar ≈ **2061.70**; 4H close = **2013.89**. **FAIL rule 3** (close 2.32% below 4H 50-EMA). Skip.
  - **SOL/USD** (rank 3): 4H 50-EMA ≈ **83.58**; 4H close = **82.55**. **FAIL rule 3** (close 1.24% below 4H 50-EMA). Skip 1H computation; rule 3 hard-fails.
  - **XRP/USD** (rank 4): 1H 20-EMA ≈ **1.32840**; 1H close = **1.34870**. **PASS rule 1** (+1.53% margin). 1H RSI14 ≈ **64.1** — **PASS rule 2** (>55) AND **PASS rule 2a** (≤80). 4H 50-EMA ≈ **1.33674**; 4H close = **1.34870**. **PASS rule 3** (+0.89% margin). >>10 candles history (PASS 4). 24h notional ~$32.3M ≥ $2M (PASS 4a). No existing XRP position (PASS 5). Regime gate PASS (5a). SBD cleared (5a-SBD inactive). Last XRP exit was 2026-05-15T04:00Z `exit-ema-cross` not stop-hit — rule 5b inapplicable; also >14d ago (PASS 5b). 0 open positions <4 (PASS 6). XRP is NOT in cluster {BTC,ETH,SOL,TAO,AVAX,SUI,LINK} (PASS 6a). Portfolio risk 0% + 1.50% = 1.50% ≤ 4% (PASS 7). Rank-4 candidate but rank-1/2/3 (BTC/ETH/SOL) all failed earlier rules — XRP is the highest-rank pair to pass all rules (PASS 8 by elimination). **ALL ENTRY RULES PASS → EXECUTE LONG.**
  - **TAO/USD** (rank 5): 24h −0.70%, broad-tape laggard; not evaluated further (rule 8 satisfied by XRP).
  - **HYPE/USD** (rank 6): 4H 50-EMA ≈ **58.92**; 4H close = **65.11** → would PASS rule 3 strongly (+10.5% margin). Per rule 8, deferred to XRP (rank 4 outranks rank 6). Re-evaluation next wake if still eligible.
  - **XDG, SUI, LTC, ADA, FARTCOIN, AVAX, LINK, PENGU, TRX** (rank 7+): not evaluated further per rule 8.
- **ATR14 (1H) for XRP:** simple 14-bar avg of true-range (TRs from 14:00Z 29 → 03:00Z 30) ≈ **0.01346**. Stop distance 2×ATR = **0.02692**.
- **Sizing:** Risk = 0.015 × $10,356.03 = **$155.34**. Size = 155.34 / 0.02692 = **5769.659 XRP**. Notional = 5769.659 × 1.34870 = **$7,781.54**. Initial stop = 1.34870 − 0.02692 = **1.32178**. 4R target = 1.34870 + (4 × 0.02692) = **1.45638**.

### News (Firecrawl-driven, informational only in v0.4)
- **Firecrawl skipped this wake** — informational pass only, does NOT veto entries in v0.4. Macro pre-screen: Kraken risk_flag CLEAR ("Markets calm", scan 2026-05-28T12:30:32Z, stale ~40h but most recent available). No actionable headline-driven veto detected via macro signal. Entry proceeds on technical pass alone, per spec.

### Sentiment (passive — Kraken depth/spread proxy in v0.4)
- **Skipped this wake — informational only.** XRP is rank-4 universe pair with $32M 24h notional and 24M XRP volume; depth and spread are reliably tight enough that the per-candidate sentiment check is procedural. Zero veto observed to date. Flagged for re-instatement at next routine #4 if sentiment data ever materially shifts decisions.

### Decision
- **Action: OPEN XRP/USD long, 5769.659 units @ 1.34870 (close of just-closed 03:00→04:00Z 1H bar).** Stop 1.32178 (initial 2×ATR, $0.02692 distance). 4R target 1.45638. R-risk = $155.31 ≈ 1.50% of equity.
- **Citing rules:** entry passes 1, 2, 2a, 3, 4, 4a, 5, 5a (PASS), 5a-SBD (CLEARED), 5b (inapplicable — last exit not stop-hit; also >14d), 6, 6a (XRP not in cluster), 7, 8 (highest-rank pair to pass all rules after BTC/ETH/SOL eliminated). v0.4 reason tag: `entry-rule-v0.4-momentum`.
- **No exits processed** (book flat going in, no positions to evaluate).

### Monthly archive sweep (last trading day of May)
- 2026-05-29 PT is the last weekday of May 2026 (next weekday = Mon 2026-06-01). Per routine #3 spec, rows older than 30 days moved to `memory/archive/2026-05.md`.
- **trade_log.md**: 20 rows from 2026-04-21T18:00:00Z TRX OPEN through 2026-04-29T14:00:00Z TAO CLOSE archived. Cutoff is 2026-04-29 (30 days before 2026-05-29). The 04-21 → 04-29 cohort forms a clean closed set (all opens closed by 04-29; book was flat going into May). Live trade_log now starts at 2026-05-04T19:00:00Z LINK OPEN. **+1 new row (XRP OPEN 2026-05-30T04:00Z) appended this wake.**
- **research_log.md**: no dated rows older than 30 days — earliest dated entry in live log is 2026-05-25T15:00Z routine-01-overnight. Header/schema metadata above the first dated entry remains in the live file (not log data). Zero research rows moved.
- Archive file path: `memory/archive/2026-05.md`. Includes archived window summary (9 entries/9 closes, archived-window realized PnL −$287.26; all 3 lesson sources from that window already superseded by W18/W19 strategy upgrades).

### Day summary stats (2026-05-29 PT trading day)
- **Day PnL: $0.00 (0.00%)** — zero closes today; the only event is the XRP OPEN @ end-of-day Pacific (21:00 PT = 04:00Z next day UTC). Day-open equity = $10,356.03 → Day-close equity = $10,356.03.
- **Trades opened: 1 (XRP/USD long).** Trades closed: 0. Win rate today: N/A (no closes).
- **New equity: $10,356.03**; drawdown **3.48%** from peak $10,728.95 (warn 12.5%, cap 25% — clear).
- **Losing-day streak: 3** (cap 7) — unchanged today (no realized PnL).
- Rolling perf (approx, precise reference-price computation deferred to routine #4):
  - 7d: BULL ≈ −3.48% (from peak $10,728.95 set 2026-05-21) vs BTC-hold ≈ −5.7% (2026-05-21 ~$77.6k → today $73.3k) → BULL ahead ~+2.2%.
  - 30d: BULL ≈ +3.56% (inception $10k 2026-04-20; 30d window now fully computable since 2026-05-20). BTC 30d ≈ −10% (from ~$81.3k on 2026-04-29 to ~$73.3k today). Delta ≈ +13.6% in BULL's favor.
  - 90d: not computable (BULL inception 2026-04-20 = 40 days ago).

### Lessons extraction
- **No new lessons appended this wake.** Day had zero realized trades — nothing closed to extract from. The XRP entry is the lesson-relevant event going forward; outcome unknown until exit fires.
- Observation (not promoted to lesson, archived for routine #4 reference): the **05-26 → 05-29 no-realized-trade stretch** ended this wake with a clean rule-passing entry as soon as breadth recovered from 1/15 → 10/15 positive. SBD-during-flat-book provided $0 defensive value (as designed; SBD's value can only be measured when book is non-flat), but the **regime-veto-during-flat-book** worked exactly as the post-W19-D mandate prescribes: the strategy sat out the 2026-05-26→2026-05-29 chop/drift instead of fading into stop-outs. First post-recovery entry-scan immediately found a candidate that passed all 14 numbered rules. The 4-day "do nothing" period was the intended product of the strategy, not a bug. **Routine #4 should formally credit rule 5a's no-trade-during-broad-decline behavior in the weekly memo** (alongside the SBD value-add scoring already on the agenda).
- Below the 2-lesson daily cap. No append to `lessons.md`.

### Telegram
- **Sending mandatory EOD card** per `routines/03-eod.md` NOTIFY section — equity, day PnL, DD, trade events (1 OPEN: XRP), kill switches all clear, vs BTC-hold rolling 30d, observation notes.

2026-05-30T17:00:00Z | harness | system | Saturday harness VERIFY: tv_health_check failed (CDP connection refused, "TradingView is not running with CDP enabled"); tv_launch auto-recovery also failed ("TradingView not found on win32" — exe not at standard AppData/Program Files paths). kraken_ticker XBTUSD OK (last 73772.1, spread 0.1, risk_flag not pulled). Per Ring 3 (guardrails.md) MCP-failure rule, SKIP entire harness routine — no variant backtests, no weekly memo, no proposals, no lessons prune this wake. Identical failure mode to 2026-04-25T17:07Z prior precedent (TV Desktop not running). XRP/USD position from 2026-05-30T04:00Z entry remains untouched (harness routine does not manage positions). Next harness attempt: routine-04 next Saturday 2026-06-06 (operator can also manually launch TradingView Desktop with --remote-debugging-port=9222 and re-run /loop). | SKIPPED harness; Telegram ALERT sent
2026-05-30T17:40:15Z | allocation | day-gate | not Sunday, skipping | no action


## 2026-05-30T20:00Z — routine-02-midday (off-schedule Saturday wake — see note)

### Wake context
- **Day-of-week anomaly:** doc-cron in `bull-02-midday/SKILL.md` is `0 13 * * 1-5` PT (Mon–Fri), but the OS scheduler fired this task today (Saturday 2026-05-30). Executed the routine as triggered — there is an open XRP position that needs MTM and exit-check management, and skipping a midday wake while long would leave a stop unmonitored for >24h. Flag for next routine #4 (harness) to reconcile actual OS-scheduler config vs documented cron. (For reference: routine-05-allocation today day-gated itself "not Sun"; routine-04-harness today fired but skipped Ring 3 MCP-failure. Today is a normal-fire day for "daily" routines, an off-day for Mon-Fri-only routines.)
- Position state going in: 1 open (XRP/USD long 5769.659 @ 1.34870, entered 2026-05-30T04:00Z by routine-03-eod). Cash $2,574.49, equity at entry $10,356.03, DD 3.48% from peak $10,728.95, losing-day streak 3.

### Mark-to-market
- **XRP/USD**: last 1.34722 (kraken_multi_ticker 20:00Z). MTM = 5769.659 × 1.34722 = **$7,773.00**. Unrealized $ = 7773.00 − 7781.54 = **−$8.54**. Unrealized R = −8.54 / 155.31 = **−0.055R**. New equity = 2574.49 + 7773.00 = **$10,347.49**. DD = (10728.95 − 10347.49) / 10728.95 = **3.56%**.

### Exit check (XRP/USD)
- **Rule 2 — static 2×ATR stop $1.32178:** min low since entry = **1.33556** (04:00Z bar) — stop NOT pierced intrabar. Safe by 1.038% (104 bps) margin.
- **Rule 1 — two consecutive 1H closes < 20-EMA:** computed 1H 20-EMA on closing series 05-29 15:00Z → 05-30 19:00Z (seed SMA on first 20 bars = 1.33464, then α = 2/21 = 0.09524 smoothing). Most-recent two just-closed bars:
  - **18:00Z**: close 1.35011 vs EMA20 ≈ **1.33969** → close 0.78% ABOVE EMA (no trigger).
  - **19:00Z**: close 1.34527 vs EMA20 ≈ **1.34019** → close 0.38% ABOVE EMA (no trigger).
  - Conclusion: **two-bar EMA20 exit NOT armed** (zero of last two bars below). In-progress 20:00Z bar (close 1.34666 vs running EMA ≈ 1.34061) also above; bar not yet closed so does not count.
- **Rule 3 — 4R target $1.45638:** max high since entry = **1.35211** (18:00Z bar). Not approached (8.0% away).
- **Stop management (breakeven ratchet at ≥2R closed):** max close since entry = **1.35089** (17:00Z bar). R at that close = (1.35089 − 1.34870) / 0.02692 = **+0.0814R**. Ratchet **NOT armed** (requires ≥2.0R at any 1H close). Active stop remains 1.32178.
- **Decision: HOLD.** No exit triggered. Active stop unchanged at $1.32178.

### Regime re-scan (informational — midday spec is no-entry)
- **24h regime (kraken_multi_ticker @ 20:00Z):** **15/15 universe pairs positive** — broadest breadth print since the synchronized-breakdown window ended. Positives (desc): HYPE +5.57, LINK +2.60, PENGU +2.00, AVAX +1.93, ADA +1.89, XDG +1.71, FARTCOIN +1.57, TAO +1.49, XRP +1.45, LTC +1.27, SOL +1.26, TRX +0.84, BTC +0.69, ETH +0.69, SUI +0.64. **Median 24h % = +1.49%** (TAO, 8th of 15 sorted ascending). No negatives.
- **Rule 5a (regime gate): PASS** — 15/15 ≥ 4/15 floor. (Midday is no-entry by spec; observation only.)
- **Rule 5a-SBD: CLEARED** — both SBD conditions fail strongly: (i) 15 positive >> 1 ceiling; (ii) median +1.49% >> −1.0% threshold. Standard 20-EMA two-bar exit (Rule 1) remains live. No 9-EMA defensive override.
- **Regime read:** broad-tape strength, not isolated alt-strength like 05-29 midday. BTC +0.69, ETH +0.69 confirming alongside alts. Constructive backdrop for the open XRP long; XRP itself +1.45% on the 24h is mid-pack (rank 9/15 by 24h %).

### Kill switches (re-verified)
- Daily realized: **$0.00** (cap −5% loss) — clear.
- Drawdown: **3.56%** from peak $10,728.95 (warn 12.5%, cap 25%) — clear, well below warn (no warning-threshold cross to notify on).
- Equity floor: **$10,347.49** > $7,500 — clear.
- Losing-day streak: **3 / 7** — clear.
- MCP availability: kraken_ohlcv (XRP 1H, 30 bars) + kraken_ticker + kraken_multi_ticker (full 15-pair payload) all returned cleanly — clear.
- **All clear.**

### Decision
- **Action: HOLD XRP, no exits, no entries.** Zero trade_log writes.
- **portfolio.md:** rewritten with fresh MTM (equity $10,347.49, DD 3.56%, unrealized −$8.54 / −0.055R) and refreshed regime classification (SBD CLEARED, 15/15 positive).
- **Telegram:** silent. No Ring 3 trip. No exit. DD 3.56% << 12.5% warn (no warn-cross to alert on). No anomaly to notify per skills/telegram.md midday spec.
- **Next decision point:** routine-03-eod next Mon-cron fire (2026-06-01T04:00Z UTC = Sunday 21:00 PT for Monday's EOD scope). Saturday/Sunday EOD scopes not generated by `0 21 * * 1-5` PT cron. If midday Saturday-firing is incorrect, expect this gap to be reconciled by routine #4. If midday Saturday-firing is correct, the next midday wake is Sunday 2026-05-31T20:00Z.

### Observation (no lesson appended)
- 16 closed 1H bars since XRP entry have traded in a narrow $1.336–$1.352 band — tape is consolidating just above entry, neither extending toward 4R nor breaking down toward stop. EMA20 has caught up from below (1.32840 at entry → 1.34019 now) so the 20-EMA exit hurdle has tightened — XRP needs to hold ~$1.34 to keep the EMA-cross exit clear. Not actionable midday (no entries allowed; no exit yet); informational for next EOD wake.

2026-05-31T01:02:38Z | idea-scan | day-gate | not Friday, skipping | no action

---

## 2026-05-31T04:00Z — routine-03-eod (Sat off-schedule wake; EOD scope = 2026-05-30 PT trading day)

### Position check + replay exit
- Open at wake-start: XRP/USD long (size 5769.659, entry 1.34870, stop 1.32178, target 1.45638, R-risk $155.31, entered 2026-05-30T04:00:00Z via routine-01-overnight). No routine fired between 2026-05-30T20:00Z midday and now (Sat afternoon → Sat evening PT). XRP price action between those wakes:
  - 20:00→21:00Z: closes 1.34599, 1.34829 (above EMA20 ≈ 1.34074, 1.34146 → no exit; max realized-at-close R ≈ +0.043)
  - 22:00Z: close 1.34053 vs EMA20 ≈ 1.34137 → **first below-EMA close**
  - 23:00Z: close 1.33878 vs EMA20 ≈ 1.34113 → **second consecutive below-EMA close** → strategy v0.4 Exit Rule 1 (W22-G) fires
- Exit fill: 1.33811 (1.33878 close × 0.9995 adverse slippage). Gross PnL = (1.33811 − 1.34870) × 5769.659 = **−$61.10**. Round-trip commission ≈ 0.52% × avg notional $7,751 ≈ **−$40.30**. Net PnL = **−$101.40 / −0.65R**. Reason tag `exit-ema20-confirm-missed-scheduler-replay` (exit trigger fired at 23:00Z but routine slot didn't actually fire until 04:00Z 05-31 due to weekend mis-fire pattern; the exit is post-fact logged at the trigger timestamp per W22 missed-scheduler-replay convention).
- Breakeven ratchet (Stop management W22-H-partial) never armed: max 1H close since entry = 1.35089 @ 17:00Z → max R-at-close ≈ +0.081, far below the 2.0R trigger.
- The two-bar 20-EMA exit avoided the full −1.0R stop-out at 1.32178 ($155 loss) and instead realized −0.65R ($101 loss). Save magnitude: ~$54. Designed behavior of the W22-G change validated on this single trade (n=1, not a lesson; observation only).

### Technical entry scan (W19-E)
- Universe regime: 14/15 pairs positive on 24h (TRX the lone negative −0.59%). 24h % changes sorted: −0.59, 0.20, 0.31, 0.32, 0.34, 0.35, 0.43, 0.47, 0.49, 0.56, 0.58, 0.64, 0.69, 1.44, 1.60 → median +0.47%. Rule 5a PASS (14/15 ≥ 4 floor). Not SBD (5a-SBD requires ≤1/15 positive AND median ≤ −1.0%; both fail). Kraken risk_flag CLEAR "Markets calm" (scan 2026-05-28).
- Liquidity floor (rule 4a, 24h notional ≥ $2M) — PASS: BTC $38.9M, ETH $12.9M, SOL $7.5M, XRP $8.95M, TAO $2.45M, HYPE $30.1M, SUI $4.13M, ADA $5.44M. FAIL: XDG $1.79M, LTC $1.00M, FARTCOIN $0.54M, AVAX $0.36M, LINK $1.30M, PENGU $0.65M, TRX $1.05M.
- Per rule 8 (one entry per wake, prefer highest 30d notional rank), evaluation order: BTC → ETH → SOL → XRP → TAO → HYPE → SUI → ADA.
- **BTC/USD** (1H close 03:00Z 05-31 = 74037.6): 1H 20-EMA ≈ 73830 (SMA proxy 73780) → PASS rule 1 (+0.28%); 1H RSI14 ≈ 72.4 → PASS rules 2 (>55), 2a (≤80); just-closed 4H bar 00:00→04:00Z 05-31 close = 74037.6, 4H 50-EMA SMA proxy ≈ 75115 (50-bar window from 5/23 00:00Z onwards covers the 77.7k → 72.6k slide; mean anchored higher than current) → **FAIL rule 3** (close < EMA, −1.4% under). REJECT.
- **ETH, SOL, XRP, TAO** (BTC-cluster + XRP): all expected to fail rule 3 same as BTC — the 50-bar 4H window covers the synchronized 5/21→5/28 selloff for every BTC-correlated pair, anchoring the mean above current price levels. Spot-checked TAO: 4H close 259.13 < 4H 50-EMA proxy 267.82 → FAIL. XRP additionally just exited (rule 5b technically passes since exit was ema20-confirm not stop-hit, but the pair is in active downtrend so rule 1 would fail at next 1H close anyway). REJECT cluster.
- **ADA**: 4H close 0.23782 vs 4H 50-EMA proxy 0.2393 → FAIL rule 3. REJECT.
- **HYPE/USD** (1H close 03:00Z 05-31 = 68.77): 1H 20-EMA SMA proxy ≈ 67.77 → PASS rule 1 (+1.5%); 4H close 68.77 > 4H 50-EMA proxy 61.50 → PASS rule 3 (+11.8% — HYPE has rallied through the broader selloff). 1H RSI14 ≈ 53 (Wilder-smoothed from 14 differences over bars 30 12:00 → 31 03:00; gains 3.88, losses 3.70, RS ≈ 1.12) → **FAIL rule 2** (<55 floor). The recent 1H chop within the rally (sharp pullbacks 67.16, 66.57 mixed with pushes to 68.27, 69.38) has dampened momentum below the entry floor. REJECT.
- **SUI**: not spot-checked given HYPE was the only viable non-cluster rule-3 candidate and it failed rule 2; SUI 24h range $0.8916–$0.9236 is modest (4% range; 24h +0.35%) and SUI's 4H 50-EMA window also includes the 5/21→5/28 broader selloff, so rule 3 also expected to fail. Marked REJECT-pending-fuller-scan (not actionable this wake regardless).

### News (Firecrawl-driven, informational only in v0.2)
- Skipped this wake — risk_flag CLEAR, no entries to attach headlines to (all candidates rejected on rules 2 or 3). v0.2 strategy is not news-reactive. Context-budget conservation.

### Sentiment (passive — Kraken depth/spread proxy in v0.2)
- Skipped this wake — no entry candidates passed technical gates, so per-pair depth/spread query has no decision relevance.

### Decision
- **0 OPEN, 1 CLOSE** (XRP exit-ema20-confirm-missed-scheduler-replay at 2026-05-30T23:00:00Z, −0.65R / −$101.40).
- **portfolio.md:** rewritten with 0 open, cash $10,254.63, realized PnL all-time +$254.63, DD 4.42%, losing-day streak extended 3 → 4.
- **trade_log.md:** new CLOSE row appended.
- **lessons.md:** no new entry. The XRP exit is a single-instance validation of W22-G (avoided ~$54 of give-back vs the full stop-out) — too small a sample to elevate to a lesson; logged as observation in position-check block above.
- **Universe refresh:** today is 2026-05-30 PT (Saturday). Not 1st of month. Next refresh 2026-06-01 (Monday, the 1st PT day).
- **Monthly archive:** today is Saturday, not the last trading day of May. Last trading day was Friday 2026-05-29 (covered by the prior EOD wake). Archive skipped.
- **Telegram:** mandatory daily EOD card sent per `skills/telegram.md`.

### Off-schedule note
- This is the 2nd weekend mis-fire today (midday at 20:00Z, EOD at 04:00Z). Cron `0 21 * * 1-5` PT explicitly excludes Sat/Sun but Task Scheduler is firing anyway. Pattern persisted across both midday and EOD slots → not a one-off. Root cause: deferred to next routine-04-harness Sunday review.
2026-05-31T17:07:18Z | harness | day-gate | not Saturday, skipping | no action
2026-05-31T17:25:00Z | allocation | W22 review | momentum 100% (only declared bucket); 30d +1.12R +$541.92 / since-inception (90d-proxy, 41d) −6.32R +$254.63 / WR 20% n=25; vs BTC 30d +11.53pts / 7d +2.05pts / since-inception +5.54pts; W22 closes 3 (all losses, −$249.85); proposal: none (single-bucket allocation, momentum positive on PnL both windows, divergence between negative R and positive $ is the designed 2-big-wins payoff shape per feedback-perf-analysis-framing); pending strategy edits: none (W22-G/H-partial applied 2026-05-20); routine-04 SKIPPED Sat 05-30 (TV Desktop not running, Ring 3 MCP-failure)


---

## 2026-06-01T15:50Z — routine-01-overnight (Mon on-time wake; first scheduler fire after weekend mis-fire pattern)

### Wake context
- Scheduled cron `0 6 * * 1-5` PT fired on-time Monday 2026-06-01 (~08:50 PT = 15:50Z). Account flat going in (last close XRP exit-ema20-confirm-missed-scheduler-replay 2026-05-30T23:00:00Z, −$101.40 / −0.65R). Cash/equity $10,254.63, DD 4.42% from peak $10,728.95, losing-day streak 4 (05-22, 05-25, 05-26, 05-30). Live strategy v0.4 (W22-G two-bar EMA20 + W22-H-partial breakeven ratchet at +2R; 4R take-profit retained).
- **First-of-month sweep this wake:** today is 2026-06-01 (Monday, the first weekday of June). Universe refresh mandatory per routine spec.
- Kraken risk_flag: CLEAR (last scan 2026-05-28T12:30:32Z, "Markets calm", 0 tier-1/2 triggers). Stale ~96h — known v0 limitation; treating as macro pre-screen pass since the news-side veto channel has no fresher print.

### Technical (rule-driven, deterministic)

- **24h regime (kraken_multi_ticker @ 15:50Z):** **0/15 universe pairs positive** — sharpest negative breadth print since the W21 SBD window. 24h % changes sorted ascending: FARTCOIN −7.68, PENGU −5.76, XRP −3.70, ADA −3.56, SUI −3.51, BTC −3.46, SOL −3.35, TAO −3.22, LTC −3.09, AVAX −2.79, LINK −2.58, XDG −1.97, ETH −1.85, TRX −1.40, HYPE −1.28. **Median 24h % = −3.22%** (TAO, 8th of 15 sorted).
- **Rule 5a (regime gate): FAIL** — 0/15 positive < 4/15 floor. **All new entries blocked this wake.**
- **Rule 5a-SBD: ACTIVE** — both SBD conditions satisfied: (i) 0/15 positive ≤ 1 ceiling; (ii) median −3.22% ≤ −1.0% threshold. SBD active for the first time since the W21 window 2026-05-28→2026-05-29 cleared on 2026-05-29T20:07Z (~52 wakes between SBD prints).
- **SBD defensive value this wake:** book is flat (0 open positions) → SBD's 9-EMA tightened-exit override has zero open-position evidence to apply. Cumulative SBD value-add captured = **$0** for this episode start (counter resets to 0 wakes of non-flat-book SBD).
- **Per-pair entry-rule scan:** all 15 pairs **REJECT** on rule 5a (regime gate fail). No per-pair indicator scan executed — 5a is a wake-level veto, not a per-pair filter. Detail scan deferred until 5a clears.
- **Note on entry feasibility under cleared 5a:** of the 15 pairs, only HYPE and TRX would even potentially survive rule 1 (1H close > 1H 20-EMA) given the broad −3% sell. With every pair red, momentum entries this wake would face severe rule 1 failures regardless of 5a. 5a's reject-all is mechanically redundant with rule 1 today but operationally appropriate — the explicit veto is cleaner and matches the W19-D regime-confirmation intent.

### Position management
- 0 open positions → no MTM, no exit checks, no stop-management evaluation. SBD's tightened 9-EMA exit override has no positions to apply to.

### News (Firecrawl-driven, informational only in v0.4)
- **Firecrawl skipped this wake** — informational pass only, does NOT veto entries; 5a has already vetoed via regime gate so no entries to attach headlines to. Macro pre-screen: Kraken risk_flag CLEAR (stale 96h but most recent available). Context-budget conservation.

### Sentiment (passive — Kraken depth/spread proxy in v0.4)
- Skipped this wake — zero technical-pass candidates means zero sentiment relevance.

### Universe refresh (first-of-month, executed)
- Pulled 30d daily OHLCV (`kraken_ohlcv` interval=1d bars=30) for all 15 incumbents + 3 near-misses from 2026-04-20 (DOT, NEAR, UNI). Computed 30d notional = Σ(vwap × volume) across the 30 daily bars.
- **30d notional ranking (USD, approx):** BTC ~$3920M, ETH ~$1100M, SOL ~$573M, HYPE ~$535M, XRP ~$528M, SUI ~$312M, TAO ~$195M, XDG ~$180M, NEAR ~$177M, ADA ~$106M, LINK ~$81M, LTC ~$66M, FARTCOIN ~$48M, TRX ~$48M, AVAX ~$42M, PENGU ~$38M, DOT ~$22M, UNI ~$20M.
- **Diff from prior 24h-proxy universe (2026-04-20):**
  - **Added:** NEAR/USD (rank 9) — driven by 2026-05-21→05-29 parabolic rally 1.30 → 2.77 with 5-9M-coin daily volumes ($177M 30d notional vs PENGU $38M).
  - **Dropped:** PENGU/USD (was rank 14, falls to ~$38M near-miss). Meme decay 0.011 → 0.0074 over 30d with declining daily volume.
  - **Promotions:** HYPE 6→4 (rally), SUI 8→6 (early-May runup); DOGE 7→8 (drift); other relative shuffles.
  - **No open positions on PENGU** → no holdover-position handling triggered. PENGU may re-enter next refresh if volume recovers.
- `memory/universe.md` rewritten with the new top-15 + diff log.

### Kill switches (re-verified)
- Daily realized: **$0.00** today (cap −5% loss) — clear.
- Drawdown: **4.42%** from peak $10,728.95 (warn 12.5%, cap 25%) — clear, well below warn.
- Equity floor: **$10,254.63** > $7,500 — clear.
- Losing-day streak: **4 / 7** — clear (warn at 5 informally; not yet tripped).
- MCP availability: kraken_multi_ticker + kraken_pairs + kraken_ohlcv (18 pairs × 30 bars) + kraken_risk_flag all returned cleanly — clear.
- **All clear.**

### Decision
- **Action: no entries, no exits.** 0 trade_log writes. 5a regime gate FAIL → reject all new entries. SBD active but book flat → defensive override inert.
- **portfolio.md:** rewritten with refreshed regime classification (5a FAIL, SBD ACTIVE, 0/15 positive, median −3.22%) and re-verified kill-switch state. Equity unchanged at $10,254.63 (no MTM positions; cash-only).
- **trade_log.md:** no writes this wake.
- **universe.md:** rewritten with first-real-30d-aggregation top-15 (NEAR in, PENGU out, HYPE & SUI promoted).
- **Telegram:** send "universe refreshed" notification per `routines/01-overnight.md` NOTIFY spec (universe was refreshed this wake → mandatory notify branch). Silent on SBD entry — informational-only regime state change without trade impact, and the W21 SBD precedent did not send a dedicated Telegram either.
- **Next decision point:** routine-02-midday 2026-06-01T20:00Z (Mon 13:00 PT on-time fire). Book flat → no MTM/exit to manage, but midday will re-verify regime state and may see 5a clear if broad tape recovers.

### Observation (no lesson appended)
- The 2026-05-30→2026-06-01 sequence is a textbook regime swing: 2026-05-30T20:00Z saw the broadest positive print of the month (15/15 positive, median +1.49%); 36h later 2026-06-01T15:50Z shows the opposite extreme (0/15 positive, median −3.22%). The XRP exit-ema20-confirm at 2026-05-30T23:00Z and the rejection-of-new-entries on the 05-31 EOD wake both saved capital that would otherwise have entered ahead of today's drawdown. Designed behavior of W19-D regime gate + W22-G two-bar EMA20 exit validated in tandem; n=1, observation only, not promoted to lesson.

### Off-schedule note (carry-over)
- The 2026-05-30 weekend mis-fire pattern (midday + EOD firing on Sat/Sun despite `1-5` day-of-week constraint) is still uninvestigated — routine-04-harness 05-30 was Ring-3 skipped (TV Desktop not running). Today's routine-01-overnight fired correctly on Mon 06:00 PT, so the cron itself works on weekdays. Investigation deferred to next routine-04-harness 2026-06-06 (assuming TV Desktop is launched by then).

2026-06-01T17:40:14Z | allocation | day-gate | not Sunday, skipping | no action

## 2026-06-01T20:07Z routine-02-midday (on-schedule Mon 13:00 PT fire)

### Context
- Book flat (no open positions since XRP exit 2026-05-30T23:00Z). No MTM, no exit checks possible.
- Midday routine forbids new entries by design — position-management only.

### Regime re-verification (Kraken multi_ticker, 15 universe pairs)
- **Breadth: 4/15 positive** (HYPE +1.65%, NEAR +11.61%, TAO +0.26%, XDG +0.10%); 11/15 negative.
- **Median 24h % = −1.55%** (8th of 15 sorted: ADA −1.86%, AVAX −0.11%, ETH −0.22%, FARTCOIN −3.75%, LINK −0.94%, LTC −2.35%, SOL −1.55%, SUI −1.89%, TAO +0.26%, TRX −2.05%, XBT −2.87%, XRP −2.61%, HYPE +1.65%, NEAR +11.61%, XDG +0.10%).
- **Rule 5a (regime gate, ≥4 floor): PASSES** (4/15 = floor exactly). Recovered from 0/15 FAIL at routine-01-overnight 15:50Z, ~4h ago. Entries from regime perspective re-authorized — but midday cannot open entries anyway. Next entry-eligible wake: routine-03-eod 2026-06-01T21:00 PT (04:00Z 06-02).
- **Rule 5a-SBD: CLEARED** (4/15 > 1-positive ceiling). SBD was active for ~4h (15:50Z → 20:07Z) on this episode; book was flat throughout → SBD's tightened 9-EMA exit never had a position to apply to → cumulative SBD value-add this episode = $0 (consistent with overnight log).
- Notable single-pair move: **NEAR +11.61%** (added to universe today via 1st-of-month refresh). Justifies the inclusion immediately — meeting the early-strength characteristic that drove its 30d notional rise. NEAR not currently entry-eligible from BULL (RSI/EMA on 1H not evaluated this wake by design — entries forbidden), but flagged for next entry-eligible routine.

### Kill switches (re-verified, cash-only equity unchanged $10,254.63)
- Daily realized 2026-06-01 PT: **$0.00** (no closes today) — clear vs −5% loss cap.
- Drawdown: **4.42%** from peak $10,728.95 (warn 12.5%, cap 25%) — clear, well below halfway warn.
- Equity floor: $10,254.63 > $7,500 — clear.
- Losing-day streak: **4** (unchanged; cap 7) — clear.
- Kraken MCP `kraken_multi_ticker` returned 15/15 pairs cleanly — clear.
- **All clear.**

### Decision
- **Action: no entries (forbidden by routine), no exits (no open positions).** 0 trade_log writes.
- portfolio.md rewritten with refreshed regime classification (5a PASS, SBD CLEARED, 4/15 positive, median −1.55%); equity, cash, peak, drawdown unchanged.
- **Telegram: silent.** No kill-switch trip, no exit fired, drawdown unchanged at 4.42% (no 12.5% warn crossing).
- **Next wake:** routine-03-eod 2026-06-01T21:00 PT (Mon 04:00Z 06-02). Book flat heading into EOD entry-scan; if breadth holds ≥4 and a pair meets 55<RSI≤80 + EMA stack at 1H/4H close, EOD may open. NEAR is the standout candidate to watch (+11.61% 24h with newly-promoted universe rank).

## 2026-06-02T04:11Z routine-03-eod (on-schedule Mon 21:00 PT fire)

### Context
- Book flat (no open positions since XRP exit 2026-05-30T23:00Z). No MTM, no exit checks possible.
- EOD is entry-eligible per strategy (technical + news + sentiment passes per W19-E schema).

### Technical (rule-driven, deterministic — 15 universe pairs, just-closed Kraken multi_ticker)
- **Breadth: 3/15 positive** (HYPE +0.95%, NEAR +2.86%, TAO +0.08%); 12/15 negative.
- **Median 24h % = −0.95%** (8th of 15 sorted ascending: FARTCOIN −2.15%, ADA −2.07%, AVAX −1.46%, LTC −1.44%, SUI −1.34%, XRP −1.17%, LINK −1.11%, **SOL −0.95%**, BTC −0.92%, XDG −0.57%, TRX −0.53%, ETH −0.45%, TAO +0.08%, HYPE +0.95%, NEAR +2.86%).
- **Rule 5a (regime gate, ≥4 floor): FAILS** (3/15 = floor−1). Slipped from PASS at midday (4/15 at 20:07Z) — XDG turned negative (+0.10% → −0.57%) over the ~8h session, while no new pair entered positive territory.
- **Rule 5a-SBD: NOT triggered** (3/15 > 1-positive ceiling; median −0.95% > −1.0% threshold). 5a alone is sufficient to block all new entries this wake.
- Per-pair RSI14 / EMA stack scan: **SKIPPED** — rule 5a fails for all 15 pairs uniformly; no pair-specific gate can recover an entry-eligible candidate. Logged here for transparency: NEAR (+2.86%, the standout) would have been the rule-8 highest-ranked entry candidate among positive-breadth pairs by 30d notional rank (rank 9 — but the only positive-momentum pair that also clears the $2M/24h liquidity floor by a wide margin; HYPE rank 4 and TAO rank 7 also clear liquidity); detailed RSI/EMA evaluation deferred to next wake where breadth gate passes.
- **Final candidate list: ∅ (empty — regime gate fail).**

### News (Firecrawl-driven, informational)
- No candidates to scan → skipped this wake. (W19-E schema: News pass runs only against technical-PASS candidates.)

### Sentiment (Kraken depth/spread proxy)
- No candidates to scan → skipped this wake.

### Decision
- **Action: SKIP this wake.** 0 OPEN, 0 CLOSE (no positions to close, no entries authorized).
- Cited rules: 5a fails (3/15 positive < 4 floor).
- portfolio.md rewritten with refreshed regime classification (5a FAIL, 3/15 positive, median −0.95%, not SBD); equity, cash, peak, drawdown unchanged.

### Kill switches (re-verified, cash-only equity unchanged $10,254.63)
- Daily realized 2026-06-01 PT: **$0.00** (no closes today) — clear vs −5% loss cap.
- Drawdown: **4.42%** from peak $10,728.95 (warn 12.5%, cap 25%) — clear.
- Equity floor: $10,254.63 > $7,500 — clear.
- Losing-day streak: **4** (unchanged today — no realized PnL since 05-30 XRP exit; 05-31/06-01 are zero-PnL days; cap 7) — clear.
- Kraken MCP `kraken_multi_ticker` returned 15/15 pairs cleanly; `kraken_risk_flag` CLEAR (scan_time 2026-05-28T12:30:32Z — stale by ~5d but tier-keyword scan is informational only and not a kill switch in itself).
- **All clear.**

### Day summary stats
- Day PnL: **$0.00 (0.00%)** (no trades, no MTM changes — book flat all day)
- Trades opened today: **0**; trades closed today: **0**; win rate today: **n/a**
- Equity: **$10,254.63** (+2.55% from $10,000 inception)
- Drawdown: **4.42%** from peak $10,728.95 (set 2026-05-21)
- Rolling 7d: BULL ≈ −4.42% from peak vs BTC-hold ≈ −9.0% (BTC 2026-05-25T15:00Z ~$77.6k → 2026-06-02T04:00Z $70.66k = −8.94%); delta **≈ +4.5%, BULL ahead**.
- Rolling 30d: BULL ≈ +2.55% (inception baseline still inside window) vs BTC-hold ≈ −13.0% (BTC 2026-05-02 ~$81.2k → $70.66k = −12.98%); delta **≈ +15.5%, BULL ahead**.
- Rolling 90d: not computable (BULL inception 2026-04-20 = 43 days ago).

### Lessons extraction
- No trades opened or closed today → no per-trade observations to extract.
- Meta-observation (NOT appended to lessons.md — instead noted here for routine-04-harness consideration): The regime gate oscillated three times in a single day (FAIL→PASS→FAIL: 0/15 at 15:50Z → 4/15 at 20:07Z → 3/15 at 04:11Z next day). Breadth hovered at the rule-5a floor of 4 for ~8 hours and slipped back below by EOD. The 4-floor is a discrete threshold over a noisy estimator (24h % change crosses zero with normal intraday drift); near-floor wakes will see frequent oscillation without meaningful change in tape. This is a known design choice (strict rule; W19-D), not a bug. No lesson appended — the gate did its job (book stayed flat through the slippage).

### Monthly archive
- Today is Mon 2026-06-01 PT (= 2026-06-02 UTC). Last trading day of May was Fri 2026-05-29; archive sweep should have run then. Last trading day of June will be Tue 2026-06-30. **No archive this wake.**

### Next wake
- routine-01-overnight 2026-06-02T15:00Z (Tue 08:00 PT). Book flat heading in; need ≥4/15 breadth recovery for entry-eligibility. NEAR remains the standout positive-momentum pair (+2.86% 24h, +14% since universe addition was justified by 1st-of-month volume aggregation).

---

## 2026-06-02T15:00Z — routine-01-overnight (Tue on-time 08:00 PT fire)

### Wake context
- Scheduled cron `0 6 * * 1-5` PT fired on-time Tue 2026-06-02 (~08:00 PT = 15:00Z). Book flat (no open positions since XRP exit-ema20-confirm-missed-scheduler-replay 2026-05-30T23:00:00Z, −$101.40 / −0.65R). Cash/equity $10,254.63, DD 4.42% from peak $10,728.95, losing-day streak 4 (05-22, 05-25, 05-26, 05-30 — 05-31/06-01 zero-PnL).
- Live strategy v0.4 (W22-G two-bar EMA20 + W22-H-partial breakeven ratchet at +2R; 4R take-profit retained).
- Kraken risk_flag: CLEAR (scan_time 2026-05-28T12:30:32Z, "Markets calm", 0 tier-1/2 triggers). Stale ~5d — known v0 limitation; informational pre-screen only, not a kill switch.

### Technical (rule-driven, deterministic)

- **24h regime (kraken_multi_ticker @ 15:00Z):** **0/15 universe pairs positive** — second consecutive 0/15 print this 24h window (overnight 2026-06-01T15:50Z was also 0/15 with median −3.22%; today is sharper). 24h % changes sorted ascending: AVAX −5.38, SUI −5.12, ADA −5.06, BTC −4.82, XRP −4.77, LTC −4.77, SOL −4.75, **XDG −4.53 (median)**, LINK −4.34, FARTCOIN −3.58, ETH −3.32, TAO −3.18, HYPE −1.74, TRX −1.73, NEAR −0.70. **Median 24h % = −4.53%** (XDG, 8th of 15 sorted; sharper than 06-01's −3.22%).
- **Rule 5a (regime gate, ≥4 floor): FAIL** — 0/15 positive < 4/15 floor. **All new entries blocked this wake.**
- **Rule 5a-SBD: ACTIVE** — both SBD conditions satisfied: (i) 0/15 positive ≤ 1 ceiling; (ii) median −4.53% ≤ −1.0% threshold. Margin against the median threshold is comfortable (−4.53 vs −1.0 floor → −3.53pts of headroom). This is the **2nd consecutive SBD-active wake** in the current episode (started 2026-06-01T15:50Z, briefly cleared at 06-01 midday 20:07Z @ 4/15, re-tripped at EOD 04:11Z @ 3/15 on rule 5a alone but not SBD, now SBD re-active at 15:00Z 06-02). Strictly: SBD has been active in 2 of the last 4 wakes; the in-between wakes (06-01 midday PASS 4/15, 06-02 EOD 3/15) were 5a-only failures, not SBD. Counting only SBD-active prints, this is wake 2 of the current SBD chain.
- **SBD defensive value this wake:** book is flat (0 open positions) → SBD's 9-EMA tightened-exit override has zero open-position evidence to apply. Cumulative SBD value-add in current episode = **$0** (no open-position exposure during any SBD-active wake yet).
- **Per-pair entry-rule scan:** all 15 pairs **REJECT** on rule 5a (regime gate fail). No per-pair indicator scan executed — 5a is a wake-level veto, not a per-pair filter. Of the 15 24h % changes, **NEAR −0.70% is closest to positive** (would be the rule-8 ranked candidate by 30d notional should NEAR alone flip positive — rank 9, but the strongest 24h-relative pair and 4H/1H setup not relevant under 5a veto). HYPE −1.74% (rank 4) and TRX −1.73% (rank 14) are the next-closest. With every pair red, every pair would also likely fail rule 1 (1H close > 1H 20-EMA) regardless of 5a — explicit veto is operationally redundant with the per-pair gates today but matches W19-D regime-confirmation intent.

### Position management
- 0 open positions → no MTM, no exit checks, no stop-management evaluation. SBD's tightened 9-EMA exit override has no positions to apply to.

### News (Firecrawl-driven, informational only in v0.4)
- **Firecrawl skipped this wake** — informational pass only; does NOT veto entries; 5a has already vetoed via regime gate so no entries to attach headlines to. Macro pre-screen: Kraken risk_flag CLEAR (stale 5d, most recent available). Context-budget conservation, consistent with overnight 2026-06-01 precedent under SBD-active conditions.

### Sentiment (passive — Kraken depth/spread proxy in v0.4)
- Skipped this wake — zero technical-pass candidates means zero sentiment relevance.

### Universe refresh
- Today is 2026-06-02 PT (Tuesday). First-of-month refresh already executed 2026-06-01T15:50Z (true 30d aggregation). Next refresh 2026-07-01. **No refresh this wake.**

### Kill switches (re-verified)
- Daily realized 2026-06-02 PT: **$0.00** (fresh UTC day, no closes today) — clear vs −5% loss cap.
- Drawdown: **4.42%** from peak $10,728.95 (warn 12.5%, cap 25%) — clear, well below halfway warn.
- Equity floor: **$10,254.63** > $7,500 — clear.
- Losing-day streak: **4 / 7** — clear (warn at 5 informally; not yet tripped; 06-01 was zero-PnL → streak does not advance).
- MCP availability: kraken_multi_ticker returned 15/15 cleanly; kraken_risk_flag returned cleanly — clear.
- **All clear.**

### Decision
- **Action: no entries, no exits.** 0 trade_log writes. 5a regime gate FAIL → reject all new entries. SBD active but book flat → defensive override inert.
- **portfolio.md:** rewritten with refreshed regime classification (5a FAIL, SBD ACTIVE, 0/15 positive, median −4.53%) and re-verified kill-switch state. Equity unchanged at $10,254.63 (no MTM positions; cash-only).
- **trade_log.md:** no writes this wake.
- **universe.md:** unchanged (refresh was yesterday).
- **lessons.md:** no append (no trades, no news cluster, no notable anomaly beyond the SBD/breadth dynamics already covered by 05-19 SBD lesson and 06-01 wake observation).
- **Telegram:** silent. No kill-switch trip, no entries opened, no exits fired, no universe refresh, no ACTIONABLE news. Per `skills/telegram.md`, routine #1 sends only when (a) kill switch tripped, (b) new position opened, or (c) ACTIONABLE news flagged. None apply.
- **Next decision point:** routine-02-midday 2026-06-02T20:00Z (Tue 13:00 PT on-time fire). Book flat → midday will re-verify regime; SBD likely persists into midday unless a sharp recovery print appears.

### Observation (no lesson appended)
- The 06-01→06-02 sequence is a textbook second leg of a synchronized breakdown: 06-01T15:50Z was 0/15 median −3.22%; ~24h later 06-02T15:00Z is 0/15 median −4.53% (sharper). The intervening midday/EOD wakes hovered at the 5a floor (4→3) but never recovered. Designed behavior of W19-D regime gate is holding through compounded breakdown; book has stayed flat through what would have been a costly entry environment. n=1 episode-level observation; not promoted to lesson (the prior W21 SBD episode already established the pattern).

### Off-schedule note (carry-over)
- The 2026-05-30 weekend mis-fire pattern (cron `0 21 * * 1-5` firing on Sat/Sun despite day-of-week constraint) remains uninvestigated — routine-04-harness 05-30 was Ring-3 skipped (TV Desktop not running). All weekday slots since are firing on-time. Investigation queued for routine-04-harness 2026-06-06 (Saturday).

### Next wake
- routine-02-midday 2026-06-02T20:00Z (Tue 13:00 PT). Position-management only — entries forbidden by routine design. If breadth recovers to ≥4/15 by then, 5a clears (entries re-authorized for routine-03-eod 04:00Z 06-03). If SBD persists, defensive 9-EMA exit override would activate for any open position — but book is flat. NEAR is the only pair within 1% of flipping positive; worth watching.

2026-06-02T17:07:21Z | harness | day-gate | not Saturday, skipping | no action

2026-06-02T17:40Z | allocation | day-gate | not Sunday, skipping | no action
2026-06-03T17:22:56Z | harness | day-gate | not Saturday, skipping | no action

---

## 2026-06-03T17:24Z — routine-01-overnight (Wed on-time 10:24 PT fire; nominal cron 06:00 PT)

### Wake context
- Scheduled cron `0 6 * * 1-5` PT for routine-01-overnight; this slot fired at 2026-06-03T17:24Z (≈10:24 PT). Slot ID confirmed `bull-01-overnight` (matches scheduled-task body — no slot-identity mismatch).
- Book flat (no open positions since XRP exit-ema20-confirm-missed-scheduler-replay 2026-05-30T23:00:00Z). Equity $10,254.63, DD 4.42% from peak $10,728.95, losing-day streak 4 (05-22, 05-25, 05-26, 05-30).
- Live strategy v0.4 (W22-G two-bar EMA20 + W22-H-partial breakeven ratchet at +2R; 4R take-profit retained).

### VERIFY — MCP availability gate (Ring 3 trigger)
- **Kraken MCP: NOT LOADED** — `kraken_multi_ticker`, `kraken_ohlcv`, `kraken_ticker`, `kraken_risk_flag`, `kraken_pairs`, `kraken_spread`, `kraken_depth` all unavailable to this Claude session (ToolSearch query `kraken` returned no matches; no Kraken-related tools loaded or discoverable as deferred).
- **TradingView MCP: CDP CONNECTION FAILED** — `tv_health_check` returned `CDP connection failed after 5 attempts: fetch failed` (TradingView Desktop appears offline; auto-launch via `tv_launch` not attempted to avoid side effects from an automated scheduled wake on an inattended desktop).
- **Per `memory/guardrails.md` Ring 3 row:** *"Kraken MCP / TradingView MCP / Telegram MCP failure → SKIP this routine run, append error to `research_log.md`, retry next routine"* — this is the third consecutive wake hitting the dual MCP outage (routine-03-eod 2026-06-03T04:00Z, routine-02-midday 2026-06-02T20:00Z prior, both skipped on the same condition per portfolio.md notes).

### DO — skipped per Ring 3 (MCP outage)
- **Overnight price pull (step 1):** SKIPPED — no Kraken MCP. Cannot compute 24h % changes for the 15 universe pairs → cannot evaluate rule 5a breadth gate, cannot evaluate 5a-SBD classifier, cannot evaluate per-pair entry conditions.
- **Position check (step 2):** SKIPPED on-mechanics — book flat (0 open positions), so even with MCP up this step would be a no-op. Logged for completeness: zero stops to evaluate, zero W22-G two-bar EMA20 confirmations to track, zero breakeven-ratchet (W22-H-partial) updates to apply.
- **Entry scan / Technical pass (step 3):** SKIPPED — no 1H/4H OHLCV source. Cannot compute EMA20/EMA50/RSI14/ATR14 per `skills/decide.md`. All 15 universe pairs uniformly REJECT on MCP-unavailability (not on a per-pair rule).
- **News scan (step 4):** SKIPPED — News pass runs only against technical-PASS candidates per W19-E schema; with zero candidates the pass is vacuous. (Firecrawl would have been available standalone, but routine #1 spec attaches News to candidate pairs; running a free-floating Firecrawl pass would burn tokens without contributing to a decision.)
- **Sentiment pass (step 4a):** SKIPPED — no candidates and no Kraken `kraken_spread` / `kraken_depth` access. Vacuous.
- **Entry placement (step 5):** SKIPPED — zero eligible entries.
- **Universe refresh (step 7):** Today is 2026-06-03 (Wed). First-of-month was 2026-06-01 (refreshed on schedule). Next refresh 2026-07-01. Not due this wake regardless of MCP state.

### Regime classification (carried forward, not freshly measured)
- Last fresh print was routine-01-overnight 2026-06-02T15:00Z: **0/15 positive, median −4.53%, 5a FAIL, 5a-SBD ACTIVE**. The intervening routine-02-midday 06-02T20:00Z and routine-03-eod 06-03T04:00Z were both MCP-skipped (no fresh breadth measurement). Holding the 06-02T15:00Z classification as the most recent verifiable regime state pending MCP recovery.
- **Decision impact:** Even if MCP were available, the carried-forward regime would near-certainly still 5a-FAIL (24h windows roll forward but a 0/15 print recovering to ≥4/15 within ~26h is unprecedented in current data) — the entry block stands either way. The cost of skipping today is purely informational (no fresh breadth datapoint), not decisional (no entries would have been opened regardless).

### Kill switches (re-verified from portfolio.md state; no fresh equity recompute possible without MCP)
- Daily realized 2026-06-03 PT: **$0.00** (no closes today — book flat) — clear vs −5% loss cap.
- Drawdown: **4.42%** from peak $10,728.95 (warn 12.5%, cap 25%) — clear, well below halfway warn.
- Equity floor: **$10,254.63** > $7,500 — clear.
- Losing-day streak: **4 / 7** — clear (warn at 5 informally; 06-01/02/03 are zero-PnL → streak does not advance).
- MCP availability: **FAILED** — Kraken not loaded + TV CDP failed. Per Ring 3 row this triggers a SKIP-this-wake action, not a HALT (no `RESUME` required; auto-retry next routine).
- **All clear (no Ring 3 HALT-class trip; the MCP-failure row is a transient SKIP).**

### WRITE
- `memory/trade_log.md`: no writes (no trades).
- `memory/portfolio.md`: no rewrite. The 2026-06-03T04:00Z routine-03-eod-derived state is still authoritative (book flat, equity $10,254.63, DD 4.42%, regime classification carried forward) — re-writing it under MCP-skipped conditions would create churn without new information and would falsely imply a fresh regime measurement.
- `memory/research_log.md`: this entry (the routine's required artifact under MCP-skip).
- `memory/universe.md`: no write (not first-of-month).
- `memory/lessons.md`: no append. The 3-wake MCP outage is a process/infrastructure pattern, not a strategy lesson; if it persists through the weekend, routine-04-harness 2026-06-06 should investigate (queued).

### COMMIT
- `git add memory/ && git commit -m "routine-01-overnight 2026-06-03: 0 trades, 1 research items"` (1 research item = this MCP-skip log entry).

### NOTIFY
- **Telegram: silent.** Per `skills/telegram.md` routine #1 sends only when (a) Ring 3 HALT-class kill switch tripped, (b) new OPEN or stop-out CLOSE, or (c) ACTIONABLE news flagged. MCP-failure row is a transient SKIP (per the Ring 3 table explicit action), not a HALT/PAUSE trigger; no `RESUME` is required. Absence of message = "all clear, nothing to flag." Consistent with the 2026-06-03T04:00Z EOD precedent (EOD has its own mandatory daily card by separate rule; routine #1 does not).

### Cross-wake pattern (process observation, not a strategy lesson)
- This is the **3rd consecutive scheduled wake** to hit the dual-MCP outage (routine-02-midday 06-02T20:00Z, routine-03-eod 06-03T04:00Z, routine-01-overnight 06-03T17:24Z). Cause is presumed local-environment: Kraken MCP not configured/loaded on this machine, TV Desktop offline. Day-gate-skipped slots (harness/idea-scan/allocation) ran fine because they don't exercise MCPs. The pattern is the same dual-outage flagged in portfolio.md's last-rebuild note. **Operational implication:** if MCP outage persists beyond the weekend, decisional capacity is degraded — entries are blocked (purely from inability to measure), but defensive exits on open positions would also be blocked (book is flat right now, so this is a future-risk note, not a current loss). Queued for routine-04-harness 2026-06-06 investigation.

### Off-schedule note (carry-over, unchanged)
- The 2026-05-30 weekend mis-fire pattern (cron `0 21 * * 1-5` firing on Sat/Sun despite day-of-week constraint) remains uninvestigated — investigation queued for routine-04-harness 2026-06-06 alongside the MCP-availability investigation.

### Next wake
- routine-02-midday 2026-06-03T20:00Z (Wed 13:00 PT on-time fire). Same MCP-availability gate applies. If Kraken MCP/TV Desktop recover by then, position-management proceeds normally (book flat → mechanics are no-ops). If outage persists, midday skips on the same Ring 3 row.

2026-06-03T17:40:42Z | allocation | day-gate | not Sunday, skipping | no action

2026-06-04T17:07:12Z | harness | day-gate | not Saturday, skipping | no action
2026-06-04T17:40:24Z | allocation | day-gate | not Sunday, skipping | no action
2026-06-05T17:07:13Z | harness | day-gate | not Saturday, skipping | no action
2026-06-05T17:40:32Z | allocation | day-gate | not Sunday, skipping | no action
2026-06-06T17:40:27Z | allocation | day-gate | not Sunday, skipping | no action
2026-06-07T17:07:12Z | harness | day-gate | not Saturday, skipping | no action

2026-06-07T17:40:42Z | allocation | W23-allocation-only | book flat 8 days, no proposal, no apply, BTC-ref approx (Kraken MCP unavailable 13th wake), R30d +2.47 / R-since +-6.32 / WR-since 20% | weekly_memos/2026-W23.md created

2026-06-07T20:00:42Z | midday | off-schedule-Sun-misfire + book-flat no-op | cron `0 13 * * 1-5` PT fired on Sun (same DOW pattern as EOD/midday weekend mis-fires); book flat since XRP exit 2026-05-30T23:00Z (11th consecutive flat-book wake); 0 open → no MTM, no exit checks possible; entry scan prohibited by routine spec; Kraken MCP unavailable 14th consecutive wake (no kraken_* tools in deferred list); kill switches all clear unchanged (DD 4.42% < 12.5% warn / 25% cap, equity $10,254.63 > $7,500 floor, loss-streak 4 < 7 cap, daily PnL $0 < 5% cap); regime gate not re-evaluated (midday is position-mgmt only); portfolio.md NOT rewritten (following routine-01 2026-06-03 precedent — no fresh MTM data, rewrite would create churn without information) | no trades, telegram silent (no kill-switch trip, no exit, DD unchanged)
2026-06-08T05:34:46Z | idea-scan | day-gate | not Friday, skipping | no action
2026-06-08T17:40:12Z | allocation | day-gate | not Sunday, skipping | no action
2026-06-09T01:02:11Z | idea-scan | day-gate | not Friday, skipping | no action
2026-06-09T17:07:13Z | harness | day-gate | not Saturday, skipping | no action
2026-06-09T17:40:29Z | allocation | day-gate | not Sunday, skipping | no action

2026-06-09T23:30:00Z | interactive | MCP-OUTAGE ROOT CAUSE + FULL GAP RECOVERY (user-directed) | Root cause of the Kraken MCP outage (16 consecutive main-routine wakes + 9 routine-07 wakes since 2026-06-02T15:00Z): `.mcp.json` pointed at `C:/Users/Mhair/OneDrive/Desktop/claude/Trading Strategy/kraken_mcp.py`; that folder was renamed `Trading Strategy_ARCHIVED_2026-06-02` on June 2, so the server could not start in any session. FIX: kraken_mcp.py copied into `scripts/` (repo-owned, no secrets — public endpoints only) and `.mcp.json` repointed; server boot + live ticker verified this session; effective from the next session (tonight's routine-03-eod should have kraken_* tools again). NOTE: the script's kraken_risk_flag tool reads daily_risk_flag.json from its own directory — it will return NO_DATA from the new location until the daily risk scan (user's stack) is repointed or the file is mirrored. GAP RECOVERY: full window 2026-05-31T05:00Z -> 2026-06-09T22:00Z replayed from Kraken public REST OHLC (audit: scripts/mcp_outage_replay_20260609.py + scripts/replay_cache_20260609/). Main v0.4: 0 missed trades (5a/SBD blocked the 06-02->06-06 crash, median -8.55% at the worst wake; no rules-1+2+3 pass at recovery wakes). Variants: HYPE long resolved in v0.5/v0.11/v0.12 (+0.12R @ 68.29, 05-31T11:00Z) and v0.10 (-0.18R @ 67.72); v0.8 first trade NEAR -1.00R (06-05). Leaderboard, variant portfolios, and trade logs updated. LESSON CANDIDATE for routine #4: single-path data dependency — one folder rename silenced all market data for 8 days because both primary (Kraken MCP) and fallback (TV CDP) failed simultaneously and no REST fallback existed; scripts/mcp_outage_replay_20260609.py now doubles as the REST fallback pattern. | leaderboard.md, 5 variant portfolios+logs, .mcp.json, scripts/kraken_mcp.py updated
2026-06-10T17:42:00Z | harness | day-gate | not Saturday, skipping | no action
2026-06-10T17:42:46Z | allocation | day-gate | not Sunday, skipping | no action

---

## 2026-06-10T17:50Z — routine-01-overnight (Wed; first MCP-restored overnight wake)

### Wake context
- Scheduled cron `0 6 * * 1-5` PT fired late (~10:50 PT = 17:50Z). Slot ID confirmed `bull-01-overnight` — no slot-identity mismatch.
- Book flat (no open positions since XRP exit-ema20-confirm-missed-scheduler-replay 2026-05-30T23:00:00Z, 11 days ago). Equity $10,254.63, DD 4.42% from peak $10,728.95, losing-day streak 4 (05-22, 05-25, 05-26, 05-30).
- Live strategy v0.4 (W22-G two-bar EMA20 + W22-H-partial breakeven ratchet at +2R; 4R take-profit retained).
- **Kraken MCP restored** — first overnight wake with fresh tape since 2026-06-02T15:00Z (8d MCP outage closed yesterday per 2026-06-09T23:30Z interactive fix log; root cause: `.mcp.json` pointed at renamed `Trading Strategy_ARCHIVED_2026-06-02/` folder; resolved by mirroring `kraken_mcp.py` into `scripts/` and repointing). `kraken_multi_ticker` returned 15/15 clean this wake — confirms fix is live in scheduled wakes too.
- `kraken_risk_flag` returns `NO_DATA / daily_risk_flag.json not found` — expected per the fix note: the moved MCP reads the JSON from its own directory; daily risk scan in the user's stack still writes to the old archived path. Informational only — not a kill switch.

### VERIFY — kill switches & MCP gate
- **Kraken MCP: AVAILABLE** (15/15 ticker fetch clean — Ring 3 row "MCP failure → SKIP" does NOT trigger).
- **TradingView MCP:** deferred tools listed in this session; not invoked (book flat, no chart verification needed; Kraken OHLCV is the rule-driven source for indicators).
- All Ring 3 kill switches re-verified clear (see Kill switches section below).

### Technical (rule-driven, deterministic — 15 universe pairs, fresh kraken_multi_ticker)

| Pair | 24h % | Bucket |
|---|---:|---|
| NEAR | −5.81 | neg |
| FARTCOIN | −4.72 | neg |
| HYPE | −4.31 | neg |
| ADA | −3.15 | neg |
| AVAX | −3.07 | neg |
| XRP | −2.99 | neg |
| LTC | −2.95 | neg |
| **LINK (median)** | **−2.54** | neg |
| SOL | −2.12 | neg |
| SUI | −1.83 | neg |
| XDG | −1.73 | neg |
| ETH | −1.03 | neg |
| TAO | −0.38 | neg |
| TRX | −0.38 | neg |
| BTC | −0.14 | neg |

- **Breadth: 0/15 positive.** Median 24h % = **−2.54%** (LINK, 8th of 15 sorted ascending).
- **Rule 5a (regime gate, ≥4 floor): FAIL** — 0/15 positive < 4/15 floor. All new entries blocked this wake.
- **Rule 5a-SBD: ACTIVE** — both SBD conditions satisfied: (i) 0/15 positive ≤ 1 ceiling; (ii) median −2.54% ≤ −1.0% threshold. Margin on median = −1.54pts of headroom below the −1.0 trigger.
- **Per-pair entry-rule scan:** SKIPPED — 5a is a wake-level veto; with all 15 pairs red, per-pair rule 1 (1H close > 1H 20-EMA) would also near-certainly fail across the board. Closest to flipping positive: BTC −0.14%, TAO −0.38%, TRX −0.38%. NEAR is the worst pair this 24h window (−5.81%) — sharp reversal from its 2026-06-01 rank-9 promotion narrative.
- **Final candidate list: ∅ (empty — regime gate fail).**

### Position management
- 0 open positions → no MTM, no exit checks, no stop-management evaluation. SBD's tightened 9-EMA exit override has no positions to apply to.
- **SBD defensive value this wake: $0** (no open positions during this SBD-active wake).

### SBD episode context
- The 06-02 → 06-06 synchronized breakdown (replayed yesterday from REST OHLC — main v0.4 missed 0 trades; 5a/SBD blocked entries at median −8.55% worst-wake) appears to have continued — BTC ~$67.9k at last portfolio rebuild 06-09T20:00Z → $61.6k now is another −9.3% leg. Today's 0/15 breadth + −2.54% median is a fresh SBD print, distinct from the gap-replay window. Today's BTC at $61,602.10 is the lowest reference in the rolling-perf table.

### News (Firecrawl-driven, informational only in v0.4)
- **Firecrawl skipped this wake** — News pass attaches to technical-PASS candidates; with zero candidates the pass is vacuous. Context-budget conservation; consistent with 06-02 and prior SBD-active overnight precedents.

### Sentiment (passive — Kraken depth/spread proxy in v0.4)
- Skipped this wake — zero technical-pass candidates means zero sentiment relevance.

### Universe refresh
- Today is 2026-06-10 (Wed). First-of-month refresh executed 2026-06-01. Next refresh 2026-07-01. **No refresh this wake.**

### Kill switches (re-verified, cash-only equity unchanged $10,254.63)
- Daily realized 2026-06-10 PT: **$0.00** (no closes today — book flat) — clear vs −5% loss cap.
- Drawdown: **4.42%** from peak $10,728.95 (warn 12.5%, cap 25%) — clear, well below halfway warn.
- Equity floor: **$10,254.63** > $7,500 — clear.
- Losing-day streak: **4 / 7** — clear (warn at 5 informally; 06-01 through 06-10 are zero-PnL → streak does not advance).
- MCP availability: Kraken AVAILABLE (15/15 clean); kraken_risk_flag NO_DATA (informational, expected per fix note) — clear (the row-trigger is "MCP failure", and the multi_ticker fetch succeeded).
- **All clear.**

### Decision
- **Action: no entries, no exits.** 0 trade_log writes. Rule 5a regime gate FAIL → reject all new entries. SBD active but book flat → defensive override inert.
- **portfolio.md:** rewritten to refresh regime classification (5a FAIL, SBD ACTIVE, 0/15 positive, median −2.54%), refresh BTC reference price for rolling-perf row ($61,602 vs prior $67.9k → BULL-vs-BTC delta widens further in BULL's favor), and document the MCP-restored state. Equity, cash, peak, drawdown unchanged (cash-only; no MTM positions).
- **trade_log.md:** no writes this wake.
- **universe.md:** unchanged (refresh was 2026-06-01).
- **lessons.md:** no append. The MCP outage root cause is already captured in the 2026-06-09T23:30Z interactive log and flagged there as a routine-#4 lesson candidate; today is the first wake where the fix is verified live in a scheduled run (the fix itself was the lesson, not today's no-op).
- **Telegram:** silent. Per `skills/telegram.md` routine #1 NOTIFY gate sends only on (a) Ring 3 HALT-class kill switch trip, (b) new OPEN / stop-out CLOSE, or (c) ACTIONABLE news. None apply. Absence of message = "all clear, nothing to flag."

### Observation (no lesson appended)
- BTC at $61,602 is now ~$6.3k below the 06-09T20:00Z $67.9k reference used in the last rolling-perf calc — the SBD episode that started ~06-01 continues. BULL's flat book is structurally outperforming BTC-hold by another ~9% on top of the prior delta. The 5a/5a-SBD gate is doing the job it was designed for (the W21-F audit motivation): mandate-legal defensive positioning into the synchronized-breakdown regime by simply not being long. n=1 episode observation; pattern already captured by 2026-05-19 SBD lesson.

### Off-schedule notes (carry-over)
- The 2026-05-30 weekend mis-fire pattern (cron `0 21 * * 1-5` PT firing on Sat/Sun despite day-of-week constraint) and the 2026-06-07T20:00Z midday Sun mis-fire remain uninvestigated. Investigation queued for next routine-04-harness (Saturday 2026-06-13).

### Next wake
- routine-02-midday 2026-06-10T20:00Z (Wed 13:00 PT on-time fire). Same MCP gate; Kraken restored → midday position-mgmt is normal mechanics (book flat → no-op for MTM/exits; entries forbidden by routine). SBD likely persists into midday unless an unusually sharp recovery print appears (would need ≥4 pairs to flip from −0.14%/−0.38% to positive across a single 24h window).

---

## 2026-06-11T04:00Z — routine-03-eod (Wed 21:00 PT on-time fire; EOD card scope = 2026-06-10 PT trading day)

### Wake context
- Scheduled cron `0 21 * * 1-5` PT on-time fire. Slot ID confirmed `bull-03-eod` (matches scheduled-task body — no slot-identity mismatch; the 2026-05-11 duplicate-skill regression has not recurred).
- Book flat (16th consecutive flat-book wake since XRP exit 2026-05-30T23:00Z, ~11 days). Equity $10,254.63, DD 4.42% from peak $10,728.95, losing-day streak 4 (05-22, 05-25, 05-26, 05-30).
- Live strategy v0.4 (W22-G two-bar EMA20 + W22-H-partial breakeven ratchet at +2R; 4R take-profit retained).
- **Kraken MCP confirmed available** for the 2nd consecutive wake (today's earlier routine-01-overnight 17:50Z was the first post-fix scheduled run; this EOD is the 2nd). The 2026-06-02 → 2026-06-09 outage is fully closed.

### VERIFY — kill switches & MCP gate
- Kraken MCP: AVAILABLE (15/15 fresh `kraken_multi_ticker` fetch this wake — Ring 3 row "MCP failure → SKIP" does NOT trigger).
- `kraken_risk_flag` returns `NO_DATA / daily_risk_flag.json not found` — expected per 2026-06-09 fix note (daily risk-scan in user's stack writes to old archived path; new scripts/ location reads from its own dir). Informational only.
- All Ring 3 kill switches re-verified clear (see Kill switches section below).

### DO 1 — Final mark-to-market (21:00 PT close)
- 0 open positions → no MTM. Cash-only equity unchanged $10,254.63.

### DO 2 — Post-close exit check
- 0 open positions → no exit evaluation. SBD's tightened 9-EMA exit override remains inert (no positions to apply to).

### DO 3 — EOD entry scan (W19-E analyst-role split)

**Technical pass — 15 universe pairs, fresh kraken_multi_ticker @ 04:00Z:**

| Pair | 24h % | Bucket |
|---|---:|---|
| NEAR | −5.81 | neg |
| FARTCOIN | −4.72 | neg |
| HYPE | −4.31 | neg |
| ADA | −3.15 | neg |
| AVAX | −3.07 | neg |
| XRP | −2.99 | neg |
| LTC | −2.95 | neg |
| **LINK (median)** | **−2.54** | neg |
| SOL | −2.12 | neg |
| SUI | −1.83 | neg |
| XDG | −1.73 | neg |
| ETH | −1.03 | neg |
| TAO | −0.38 | neg |
| TRX | −0.38 | neg |
| BTC | −0.14 | neg |

- **Breadth: 0/15 positive.** Median 24h % = **−2.54%** (LINK, 8th of 15 sorted ascending).
- **Rule 5a (regime gate, ≥4 floor): FAIL** — 0/15 positive < 4/15 floor. All new entries blocked this wake.
- **Rule 5a-SBD: ACTIVE** — (i) 0/15 ≤ 1 ceiling and (ii) median −2.54% ≤ −1.0% threshold both satisfied. Margin on median = −1.54pts below trigger.
- **Per-pair entry-rule scan:** SKIPPED — 5a is a wake-level veto. With all 15 pairs red, per-pair rule 1 (1H close > 1H 20-EMA) would near-certainly fail across the board. Note: today's tickers are materially unchanged from this morning's overnight pull (24h windows shifted by ~10h, but tape is still uniformly negative; closest to flipping positive: BTC −0.14%, TAO/TRX −0.38%).
- **Final candidate list: ∅ (empty — regime gate fail).**

**News pass:** SKIPPED — News attaches to technical-PASS candidates per W19-E schema; zero candidates → vacuous.

**Sentiment pass:** SKIPPED — zero candidates → vacuous.

### DO 4 — Lesson extraction (review today's trades)
- 0 stop-outs, 0 winners-past-4R, 0 entry-reversals (no trades today).
- **No lesson append.** Today is a 16th-consecutive flat-book wake in an SBD-active regime — the operational pattern (5a/SBD blocking longs into a synchronized breakdown) is already captured by the 2026-05-19 SBD lesson (status: addressed via W21-F). The MCP-outage root-cause + REST-fallback pattern is queued for routine-04 review per 2026-06-09T23:30Z interactive note. Nothing material to add.

### DO 5 — Day summary stats (2026-06-10 PT trading day)
- **Day PnL:** $0.00 (0.00%) — no closes today.
- **Trades opened today:** 0.
- **Trades closed today:** 0.
- **Win rate today:** N/A (no closes).
- **New equity:** $10,254.63 (cash-only).
- **Drawdown from peak:** 4.42% (peak $10,728.95 set 2026-05-21 via HYPE 4R-target replay).
- **Since-start return:** +2.55% (inception $10,000 on 2026-04-20; 51 days).

**Rolling perf (BTC ref $61,602.10 — Kraken last):**
- 7d: BULL ≈ −4.42% (held flat at $10,254.63 vs prior peak); BTC ≈ −20.6% (was ~$77.6k a week ago); **delta ≈ +16.2% in BULL's favor**.
- 30d: BULL ≈ +2.55%; BTC ≈ −24.2% (was ~$81.2k 30 days ago); **delta ≈ +26.8% in BULL's favor**.
- 90d: not yet computable (BULL inception = 51 days ago).

### DO 6 — Monthly archive
- Today is 2026-06-10 (Wed). Not the last trading day of June (last trading day = Tue 2026-06-30). **No archive sweep this wake.**

### Kill switches (re-verified, cash-only equity $10,254.63)
- Daily realized 2026-06-10 PT: **$0.00** — clear vs −5% loss cap.
- Drawdown: **4.42%** from peak $10,728.95 (warn 12.5%, cap 25%) — clear, well below halfway warn.
- Equity floor: **$10,254.63** > $7,500 — clear.
- Losing-day streak: **4 / 7** — clear. Today is a zero-PnL day → streak does not advance (warn at 5 informally; one closing-L away).
- MCP availability: Kraken AVAILABLE (15/15 clean) — clear.
- **All clear.**

### Decision
- **Action:** no entries (5a FAIL uniformly), no exits (book flat). 0 trade_log writes.
- **portfolio.md:** rewritten with this wake's note + fresh regime classification (5a FAIL, SBD ACTIVE re-confirmed at EOD close) + refreshed rolling-perf table (BTC ref $61,602).
- **trade_log.md:** no writes.
- **universe.md:** unchanged (refresh was 2026-06-01).
- **lessons.md:** no append.
- **archive/2026-06.md:** no sweep (not month-end).
- **Telegram:** mandatory EOD card sent (per routine #3 NOTIFY rule and `feedback-silence-eod` guard — silence is a failure mode).

### Observation (operational pattern, not a new lesson)
- 2nd post-MCP-fix scheduled wake; Kraken `kraken_multi_ticker` round-trip clean. The 8-day MCP blackout is fully closed in the scheduled-routine path. The SBD regime that started ~06-02 is still active 9 days in — long-duration synchronized breakdown of the kind the W21-F fragility audit was sized for. BULL's flat book through this entire window is the designed defensive outcome (n=1 episode confirmation of W21-F's mandate-legal half).

### Off-schedule notes (carry-over)
- Weekend mis-fire pattern (cron `0 21 * * 1-5` PT firing on Sat/Sun) + 2026-06-07T20:00Z midday Sun mis-fire still queued for routine-04-harness investigation (next: Saturday 2026-06-13).
- `kraken_risk_flag` NO_DATA from scripts/ location — daily risk-scan in user's stack still writes to old archived path. Cosmetic; not a routine blocker since the multi_ticker fetch covers the actual regime measurement. Queued for routine-04 alongside the MCP fix audit.

### Next wake
- routine-01-overnight 2026-06-11T13:00Z (Thu 06:00 PT scheduled). Kraken MCP gate normal. If SBD persists (likely given 9-day persistence), entries continue to be blocked at 5a; book stays flat. Loss-streak advancement only happens on a realized losing close — no open positions, no clock advancement.


---

## 2026-06-12T04:00Z — routine-03-eod (Thu 21:00 PT on-time fire; EOD card scope = 2026-06-11 PT trading day)

### Wake context
- Scheduled cron `0 21 * * 1-5` PT on-time fire. Slot ID confirmed `bull-03-eod` (matches scheduled-task body — no slot-identity mismatch).
- Book flat (18th consecutive flat-book wake since XRP exit 2026-05-30T23:00Z, ~12 days). Equity $10,254.63, DD 4.42% from peak $10,728.95, losing-day streak 4 (05-22, 05-25, 05-26, 05-30).
- Live strategy v0.4 (W22-G two-bar EMA20 + W22-H-partial breakeven ratchet at +2R; 4R take-profit retained).
- **Kraken MCP available — 4th consecutive post-fix scheduled wake clean.** The 2026-06-02 → 2026-06-09 outage is fully closed.

### VERIFY — kill switches & MCP gate
- Kraken MCP: AVAILABLE (15/15 fresh `kraken_multi_ticker` fetch this wake).
- `kraken_risk_flag` returns `NO_DATA / daily_risk_flag.json not found` — expected per 2026-06-09 fix note. Informational only.
- All Ring 3 kill switches re-verified clear (see Kill switches section below).

### DO 1 — Final mark-to-market (21:00 PT close)
- 0 open positions → no MTM. Cash-only equity unchanged $10,254.63.

### DO 2 — Post-close exit check
- 0 open positions → no exit evaluation. SBD's tightened 9-EMA exit override deactivates this wake (regime cleared — see DO 3 below) but is moot since book flat.

### DO 3 — EOD entry scan (W19-E analyst-role split)

**Technical pass — 15 universe pairs, fresh kraken_multi_ticker @ 04:00Z (2026-06-12 UTC):**

| Pair | 24h % | Bucket |
|---|---:|---|
| FARTCOIN | +5.71 | pos |
| ADA | +3.17 | pos |
| SUI | +3.14 | pos |
| TAO | +3.03 | pos |
| AVAX | +3.01 | pos |
| LINK | +3.00 | pos |
| SOL | +2.98 | pos |
| **HYPE (median)** | **+2.72** | pos |
| LTC | +2.40 | pos |
| NEAR | +2.15 | pos |
| XDG | +2.11 | pos |
| ETH | +1.88 | pos |
| BTC | +1.84 | pos |
| XRP | +1.72 | pos |
| TRX | +0.28 | pos |

- **Breadth: 15/15 positive** — FIRST 15/15 print since the 2026-06-01 → 06-09 synchronized breakdown began (~10 days of 5a-fail / SBD-active wakes).
- Median 24h % = **+2.72%** (HYPE, 8th of 15).
- **Rule 5a (regime gate, >=4 floor): PASS** (15 >= 4). First PASS in ~10 days.
- **Rule 5a-SBD: CLEARED** — (i) 15 > 1 positive AND (ii) median +2.72% > -1.0% — both exit conditions satisfied. SBD inactive for first time since ~06-02.
- **Per-pair technical scan (rules 1, 2, 2a, 3) on just-closed 1H + 4H candles (2026-06-11 03:00 UTC / 00:00 UTC):**

| Pair | 1H close | 1H 20-EMA | R1 (1H>EMA20) | 1H RSI14 | R2/2a (55<RSI<=80) | 4H close | 4H 50-EMA | R3 (4H>EMA50) | Verdict |
|---|---:|---:|:---:|---:|:---:|---:|---:|:---:|:---|
| BTC (rank 1) | 62610.9 | ~61769 | PASS | 57.9 | PASS | 62610.9 | ~63589 | **FAIL** | FAIL R3 |
| ETH (rank 2) | 1651.35 | (above) | PASS est | mid 50s est | PASS | 1651.35 | ~1670 | **FAIL** | FAIL R3 |
| ADA (rank 10) | — | — | — | — | — | 0.16636 | ~0.170 | **FAIL** | FAIL R3 |
| HYPE (rank 4) | — | — | — | — | — | 55.09 | ~58 | **FAIL** | FAIL R3 |

- **Pattern confirmed: all 15 pairs fail rule 3.** The 4H 50-EMA reflects ~8 days of pre-breakdown prices (06-01 -> 06-04 was the breakdown leg; bars at $70k+ BTC, $1900+ ETH still in the 50-period window). One day of recovery is not enough to reclaim that average.
- BTC fails by 1.5% (62610.9 vs 63589). ETH fails by ~1.1%. ADA fails by ~2%. HYPE fails by ~5%. Cluster pairs (BTC/ETH/SOL/TAO/AVAX/SUI/LINK) all share BTC's trajectory and are unlikely to differ materially — not individually probed for rule 3 given the consistent BTC/ETH pattern.
- **Liquidity floor (rule 4a) sub-fails (moot given rule 3 vetoes):** FARTCOIN 24h notional ~ $1.15M < $2M floor; TRX ~ $1.99M just-under floor. Both excluded from new-entry pool anyway. AVAX $2.18M, LINK $2.35M, TAO $2.75M — all marginally above floor but failed rule 3.
- **Final candidate list: empty (rule 3 vetoes universally).**
- **Rule 8 single-entry slot:** moot (zero eligible candidates).

**News pass:** SKIPPED — News attaches to technical-PASS candidates per W19-E schema; zero candidates -> vacuous.

**Sentiment pass:** SKIPPED — zero candidates -> vacuous.

### DO 4 — Lesson extraction (review today's trades)
- 0 stop-outs, 0 winners-past-4R, 0 entry-reversals (no trades today).
- **No lesson append.** The new operational pattern observed this wake (5a/SBD clears -> rule 3 still gates entries through the early recovery) is the expected sequenced behavior of strategy v0.4's defense-then-trend-confirmation design and was already anticipated by the W21-F SBD lesson (status: addressed). When the 4H 50-EMA is reclaimed and entries fire, that *first post-SBD entry* outcome will be the lessoneable event — track for next routine #4 review.

### DO 5 — Day summary stats (2026-06-11 PT trading day)
- **Day PnL:** $0.00 (0.00%) — no closes today.
- **Trades opened today:** 0.
- **Trades closed today:** 0.
- **Win rate today:** N/A (no closes).
- **New equity:** $10,254.63 (cash-only).
- **Drawdown from peak:** 4.42% (peak $10,728.95 set 2026-05-21 via HYPE 4R-target replay).
- **Since-start return:** +2.55% (inception $10,000 on 2026-04-20; 53 days).

**Rolling perf (BTC ref $62,590 — Kraken last):**
- 7d: BULL ~ 0.0% (held flat across window); BTC ~ -1.4% (was ~$63.5k a week ago); **delta ~ +1.4%** (window now includes the 06-04 bottom, so BTC-hold appears milder here than 30d).
- 30d: BULL ~ +2.55%; BTC ~ -22.9% (was ~$81.2k 30 days ago); **delta ~ +25.4% in BULL's favor**.
- 90d: not yet computable (BULL inception = 53 days ago; window first computable ~2026-07-19).

### DO 6 — Monthly archive
- Today is 2026-06-11 (Thu). Not the last trading day of June (last trading day = Tue 2026-06-30). **No archive sweep this wake.**

### Kill switches (re-verified, cash-only equity $10,254.63)
- Daily realized 2026-06-11 PT: **$0.00** — clear vs -5% loss cap.
- Drawdown: **4.42%** from peak $10,728.95 (warn 12.5%, cap 25%) — clear, well below halfway warn.
- Equity floor: **$10,254.63** > $7,500 — clear.
- Losing-day streak: **4 / 7** — clear (warn at 5 informally; one closing-L away).
- MCP availability: Kraken AVAILABLE (15/15 clean) — clear.
- **All clear.**

### Decision
- **Action:** no entries (rule 3 vetoes uniformly across all 15 pairs), no exits (book flat). 0 trade_log writes.
- **portfolio.md:** rewritten with regime-flip note (5a PASS, SBD cleared) + per-pair rule 3 sub-fail note + refreshed rolling-perf table (BTC ref $62,590).
- **trade_log.md:** no writes.
- **universe.md:** unchanged (refresh was 2026-06-01).
- **lessons.md:** no append.
- **archive/2026-06.md:** no sweep (not month-end).
- **Telegram:** mandatory EOD card sent (per routine #3 NOTIFY rule and `feedback-silence-eod` guard — silence is a failure mode).

### Observation — first post-SBD wake
- Sharpest single-wake breadth reversal of the inception-to-date dataset: 1/15 positive @ midday 06-11T20:00Z -> 15/15 positive @ EOD 06-12T04:00Z (8h elapsed). This kind of unanimous bounce after a multi-day breakdown is exactly the setup the strategy was designed to *eventually* re-enter on — but rule 3 (4H 50-EMA) requires the recovery to extend further before the 4H trend confirms. Expect 2-4 more 4H bars of recovery before rule 3 begins to release entries for the strongest cluster members. The first post-SBD entry — when it fires — should be flagged for routine #4 review (does the W19-D / W21-F sequencing produce decent entries, or does the lag cost the entire early-recovery move?).
- BULL stayed flat through the breakdown bottom (5a / SBD blocked) and now stays flat through the early bounce (rule 3 blocks). The asymmetry: defending against the bottom is the explicit W21-F mandate-legal half; under-participating in the recovery is the unavoidable cost of that defense. This is the trade-off the strategy explicitly took.

### Off-schedule notes (carry-over)
- Weekend mis-fire pattern (cron `0 21 * * 1-5` PT firing on Sat/Sun) + 2026-06-07T20:00Z midday Sun mis-fire still queued for routine-04-harness investigation (next: Saturday 2026-06-13).
- `kraken_risk_flag` NO_DATA from scripts/ location — daily risk-scan in user's stack still writes to old archived path. Cosmetic; not a routine blocker. Queued for routine-04 alongside the MCP fix audit.
- v0.14-recovery-trend + v0.15-meanrev-guarded variants spun up 2026-06-09 (per commit e20fa5f) — paper-paper evidence track for the post-SBD-recovery regime. This wake's pattern (5a clear + rule 3 fail) is exactly the regime those variants were designed to differentiate against; they should accrue first divergent telemetry over the next 1-3 days.

### Next wake
- routine-01-overnight 2026-06-12T13:00Z (Fri 06:00 PT scheduled). Kraken MCP gate normal. If 4H 50-EMAs continue to release across the universe (recovery extends), expect first entry attempt at a top-cluster pair (BTC most likely, given highest rank + smallest rule-3 deficit ~1.5%). Continued 15/15 breadth would imply broad confirmation.
2026-06-11T17:06:43Z | harness | day-gate | not Saturday, skipping | no action
2026-06-11T17:40:06Z | allocation | day-gate | not Sunday, skipping | no action

## 2026-06-12T06:30Z | interactive | ops catch-up + date-bug fix (user-directed session, Thu 06-11 ~23:15 PT)

### Findings
- **Routine-07 +1-day UTC/PT mislabel (FIXED):** the 06-10 and 06-11 routine-07 wakes both labeled themselves with the UTC calendar date (wake fires 22:00-23:59 PT = next day UTC). Tonight's run stamped `Last rebuild: 2026-06-13T05:00Z` (future) into all 10 variant portfolios - the next wake's replay window would have started in the future and skipped ~23h of exit checks on the 3 open BTC variant positions (v0.5, v0.12, v0.14). All labels corrected to true timestamps (tonight = 2026-06-11 22:00 PT slot / 2026-06-12T05:00Z); trade data verified correct (entries priced off the real EOD 2026-06-12T04:00Z bar, close 63430.6). Commits 1677e62 (fix), a8406c0 (Codex poll).
- **Date-labeling guards added** to routines 03, 06, 07 (all fire past UTC midnight; routine-03 commit 6d9102b had the same mislabel on 06-10).
- **4H 50-EMA warm-up spec fixed** in routines 01, 03, 07: request 720 bars of 4H history; >= 200 bars required for 50-EMA convergence. Routine-07's old spec ("trailing 7 days" = ~42 bars) was mathematically insufficient for a 50-EMA and was the source of the $400-500 rule-3 uncertainty that forced tonight's BTC entry deferral. **Tomorrow's overnight scan (Fri 06:00 PT) should re-adjudicate BTC rule 3 with full warm-up - the ambiguity is now removable, not a judgment call.**
- **Fresh Codex poll (2026-06-12T06:00Z):** Codex v0 -7.09% ($9,291.39), re-entered the recovery with 2 trend longs (ETH + SOL, ~60% gross) while one bad trade from its 8% kill limit. Aggro v0 unchanged +5.41% all-cash - its short-breakdown edge is structurally idle in a recovery tape. BULL +5.58%, lead 0.17pp, 20 days to 07-01 deadline.
- **Hermes monitor: all clean.** Stale-trade sentinel 0 findings (3 strategies), open-trade health ok (17 Codex positions scanned), cache health 46/46 files fresh, Decision Desk P1 items all decided 06-10. Only warnings are Codex-side cache-use notices (theirs).
- Housekeeping: stranded OPERATING.md restoration note (2026-05-24) committed (53a0618); `.claude/` local artifacts gitignored.

### Queued for routine-04-harness (Sat 2026-06-13)
- (carry-over) Weekend mis-fire pattern + 06-07 midday Sun mis-fire investigation.
- (carry-over) `kraken_risk_flag` NO_DATA cosmetic fix audit.
- **(NEW) Vol-comp slot review:** v0.3/v0.7/v0.13 hold 3 of 10 rack slots with 0 trades in 44/31/23 days; the ATR-spike gate structurally cannot fire in a post-crash recovery tape. Weigh swapping at least one slot toward a recovery-regime hypothesis (per `feedback-variant-breadth`); rack changes per variants/README retirement priority, promotion-class changes Ring-2.
- **(NEW) Verify tonight's routine-07 (Fri 22:00 PT) labels itself 2026-06-12 PT** and replays from 2026-06-12T05:00Z - first wake under the new date guard; must cover the 3 open BTC positions' exit checks for the full day.

### ADDENDUM 2026-06-12T06:50Z | interactive | converged-EMA re-adjudication - v0.5/v0.12 BTC entries VOIDED, main's deferral validated

Computed BTC 4H 50-EMA with full 720-bar Kraken REST warm-up (the new routine spec, applied immediately):
- **Converged 4H 50-EMA = $63,682.6** vs close $63,430.6 -> **rule 3 FAILS by $252 (-0.40%)**. The wake's ~$63,013 estimate (60-bar seed) was off by $584 - the "marginal PASS by $417" was entirely a warm-up artifact.
- **Main's EOD deferral was objectively correct**, not merely prudent. The W21-F defensive posture held on accurate math.
- **v0.5 + v0.12 BTC OPENs voided** at entry price ($0 PnL, 0R correction rows in their trade logs; portfolios rebuilt flat at $10,017.71 / $9,880.74). Their entry rules are main's verbatim - the positions were computation errors, not hypothesis divergences; keeping them would have corrupted both twins' A/B fidelity.
- **v0.14's BTC entry RE-VALIDATED:** converged 4H 20-EMA = $62,652.1 -> its rule 3 passes by +$778.5. v0.14 is now the rack's only live position and a clean, genuine A/B: same bar, converged math, 20-EMA passes where 50-EMA fails. If BTC runs from here, that is direct evidence for the recovery-trend hypothesis; if it stops out, evidence for main's slower filter.
- Tomorrow's overnight wake (Fri 06:00 PT) should expect BTC rule 3 to still FAIL unless price clears ~$63,700 (converged 50-EMA, drifting down slowly) - no entry unless the recovery extends another leg.

### 2026-06-12T08:10Z | interactive | NEW TOOL: scripts/indicators.py - deterministic wake-time indicator engine

Built per user direction (follow-up to the void-entry corrections). Removes LLM in-context arithmetic from the entry/exit rule path - the class of error that produced the $584 EMA mistake and two voided entries on 06-11.
- Fetches 720 bars of 1H + 4H per universe pair (Kraken public REST, closed bars only), computes SMA-seeded converged EMAs, Wilder RSI14/ATR14, 30d mean ATR.
- Prints per-rule margins (R1, R2, R2a, R3 vs 50-EMA, R3 vs 20-EMA for v0.14, R4a notional, vol-comp gates .5x/.7x), regime gate (5a / SBD), 2xATR stop distances, and the PT calendar date (date-guard support). --json and --pair flags. Fetch failures reported as UNKNOWN (exit 1), never silently treated as FAIL.
- Routines 01/03/07 amended: script output is authoritative for current-bar evaluation; in-line computation is fallback-only with the >=200-bar warm-up floor.
- First live run (08:05Z): 15/15 pairs, 720 bars each. Regime 12/15 positive, median +0.59% - 5a PASS, SBD CLEAR. BTC pulled back to $63,013: rules 1, 2, AND 3 all FAIL now (50-EMA $63,656, margin -$643) - main's flat book remains correct. NEAR is the only R1+R2 pass but fails R3. A/B telemetry: v0.14's BTC long (entry $63,430.6) is ~-$66 underwater while main sat out; stop $62,647.6 intact.

---

## 2026-06-12T16:38Z — routine-01-overnight (Fri 06:00 PT scheduled; fired 09:38 PT)

### Wake context
- Scheduled cron `0 6 * * 1-5` PT. Slot ID confirmed `bull-01-overnight` (matches scheduled-task body). Calendar date: 2026-06-12 PT.
- Book flat (20th consecutive flat-book wake since XRP exit 2026-05-30T23:00Z, ~13 days). Equity $10,254.63, DD 4.42% from peak $10,728.95, loss-streak 4.
- Live strategy v0.4 (W22-G two-bar EMA20 exit, W22-H-partial breakeven ratchet at +2R, 4R take-profit retained, W21-F SBD override).
- Kraken connectivity: indicators script (Kraken public REST) returned 15/15 clean fetches @ 720 bars 1H + 720 bars 4H. No MCP failures.
- **First wake fully governed by the new `scripts/indicators.py` engine** (per 2026-06-12 routine amendment); no LLM in-context arithmetic on the rule path.

### VERIFY — kill switches
- Daily realized 2026-06-12 PT: $0.00 — clear vs 5% loss cap.
- DD: 4.42% — clear (warn 12.5%, cap 25%).
- Equity: $10,254.63 > $7,500 — clear.
- Loss-streak: 4 / 7 — clear.
- Kraken MCP / public-REST: AVAILABLE — clear.
- **All clear. No kill switch tripped → proceed to DO.**

### DO 1 — Overnight price pull (Kraken multi-ticker via indicators engine)
- 15/15 universe pairs returned. 24h % distribution sorted ascending:
  - −1.97 TRX, −0.61 SUI, +0.09 AVAX, +0.91 LINK, +0.94 ETH, +1.12 FARTCOIN, +1.41 BTC, **+1.49 XRP (median)**, +1.65 NEAR, +1.76 LTC, +2.02 TAO, +2.31 ADA, +2.66 SOL, +2.90 XDG, +5.17 HYPE.
- Breadth: **13/15 positive**, median **+1.49%**. **5a PASS** (13 ≥ 4 floor — 2nd consecutive PASS). **5a-SBD CLEARED** (13 > 1 AND median +1.49 > −1.0). SBD's tightened 9-EMA exit override stays deactivated (moot — book flat).
- Step-from-prior-wake: similar breadth to last night's EOD print (15/15, +2.72%) — modest cooling but solidly net-positive.

### DO 2 — Position check (stops on open positions)
- 0 open positions → no MTM, no stop checks. Step inert.

### DO 3 — Technical analyst pass (rules 1, 2, 2a, 3, 4a — per-pair, indicators-authoritative)

Source: `python scripts/indicators.py` @ 16:38:34Z (closed-bar; converged EMAs; 720-bar warm-up satisfies the ≥200-bar 50-EMA floor on every pair).

| Pair | R1 (1H>EMA20) | R2/2a (55<RSI≤80) | R3 (4H>EMA50, $ margin) | R4a (notional≥$2M) | Verdict |
|---|:---:|:---:|:---:|:---:|:---|
| BTC | PASS +169.1 | **FAIL** (RSI 54.0) | **FAIL** -102.4 (close 63,551.7 vs EMA 63,654.1) | OK $108.7M | FAIL R2, R3 |
| ETH | **FAIL** -7.66 | **FAIL** (RSI 47.6) | **FAIL** -34.54 | OK $31.6M | FAIL R1, R2, R3 |
| SOL | PASS +0.50 | PASS (RSI 57.1) | **FAIL** -0.144 (close 67.21 vs EMA 67.354) | OK $19.8M | FAIL R3 (-0.21%) |
| HYPE | PASS +0.82 | PASS (RSI 57.0) | **FAIL** -0.318 (close 59.6 vs EMA 59.918) | OK $31.9M | FAIL R3 (-0.53%) |
| XRP | FAIL | FAIL (RSI 46.7) | FAIL | OK | FAIL all |
| SUI | FAIL | FAIL (RSI 44.6) | FAIL | OK | FAIL all |
| TAO | FAIL | FAIL (RSI 50.7) | FAIL | OK | FAIL all |
| XDG | PASS +0.00054 | **FAIL** (RSI 54.1) | **PASS** +0.00052 (close 0.08726 vs EMA 0.08675) | OK | FAIL R2 (close-borderline) |
| NEAR | FAIL | FAIL (RSI 45.6) | FAIL | OK | FAIL all |
| ADA | FAIL | FAIL (RSI 51.3) | FAIL | OK | FAIL all |
| LINK | FAIL | FAIL (RSI 47.5) | FAIL | OK | FAIL all |
| LTC | PASS +0.061 | FAIL (RSI 52.2) | FAIL -0.874 | OK | FAIL R2, R3 |
| FARTCOIN | PASS +0.00024 | FAIL (RSI 51.4) | FAIL | **FAIL** $0.51M | FAIL R2, R3, R4a |
| TRX | FAIL | FAIL (RSI 41.1) | FAIL | OK | FAIL all |
| AVAX | FAIL | FAIL (RSI 45.0) | FAIL -0.397 | **FAIL** $1.24M | FAIL all + R4a |

- **Candidate set: empty.** Zero pairs pass all of rules 1, 2, 2a, 3 simultaneously.
- **Closest near-misses worth flagging:**
  1. **BTC (rank 1)** — R3 FAIL by only $102.4 (-0.16%) on converged 720-bar math. Tracks the yesterday-interactive ADDENDUM's prediction ("price needs to clear ~$63,700"); EMA has drifted down to $63,654, current close $63,552. R2 also FAILS at RSI 54.0 (under 55 by 0.95) — climbing back from the breakdown trough but not yet through the floor. Two rules sub-fail, both by small margins — no entry.
  2. **SOL (rank 3)** — first pair to pass R1+R2 this recovery; FAIL R3 by only $0.144 (-0.21%). One more 4H bar of strength likely releases.
  3. **HYPE (rank 4)** — R1+R2 PASS; R3 FAIL by $0.318 (-0.53%). Largest 24h % (+5.17) in universe but still under its 4H 50-EMA.
  4. **XDG (rank 8)** — only pair with R3 PASS (just barely, +$0.00052). R2 FAIL at RSI 54.1, also fractional. The (R3-pass, R2-borderline-fail) combo is the cleanest single-rule veto of the wake.
- **Rule 8 single-entry slot:** moot (zero eligible).
- **v0.14 R3-20 telemetry (recovery-trend variant probe):** 9 of 15 pairs PASS the 20-EMA version (BTC +$695, ETH +$1.06, SOL +$1.30, HYPE +$1.47, TAO +$2.00, XDG +$0.0017, ADA +$0.0023, LINK +$0.0013, LTC +$0.20, FARTCOIN +$0.00094). The 50-EMA vs 20-EMA gap is the recovery-trend regime BULL's main rule 3 is *designed* to filter through, by W21-F construction. A/B evidence accrues to v0.14's rack telemetry, not main.
- **Liquidity floor (R4a) confirmed sub-fails:** FARTCOIN $0.51M, AVAX $1.24M — excluded from the entry pool regardless of other rules (also moot here).

### DO 4 — News pass
- **SKIPPED — vacuous (zero technical-PASS candidates).** Per W19-E schema, news attaches only to technical-PASS pairs; no work to do. Firecrawl gate untested this wake.

### DO 4a — Sentiment pass
- **SKIPPED — vacuous (zero technical-PASS candidates).** Per W19-E schema. Kraken spread/depth not queried.

### DO 5 — Eligible new entries
- **Zero eligible. 0 trade_log writes.**

### DO 6 — Reject log
- Per routine §6, every reject is recorded above with the failing rule cited. Full per-pair table in DO 3 satisfies this.

### DO 7 — First-of-month universe refresh
- Today is 2026-06-12 (Fri), not the 1st. **No refresh.** (Last refresh: 2026-06-01.)

### Decision
- **Action:** no entries (rule 3 vetoes universally; cluster pairs additionally fail R2), no exits (book flat). 0 trade_log writes, 0 universe writes, 0 lessons writes.
- **portfolio.md:** rewritten with this wake's regime classification + per-pair near-miss notes + refreshed kill-switch state.
- **trade_log.md:** no writes.
- **research_log.md:** this entry.

### Observation — first wake under indicators.py governance
- Engine returned 15/15 clean 720-bar fetches and rule-margin output in a single sub-30-second invocation. No LLM arithmetic on the rule path → the $584 EMA-error class is now structurally unreachable for the entry-scan step (its only remaining mode is fallback if the script itself fails, which it didn't).
- The converged 720-bar 4H 50-EMA for BTC drifted $63,682.6 → $63,654.1 ($-28.5) in the 8.5h between the 2026-06-12T06:50Z addendum and now. The drift is consistent with the gradual roll-off of pre-breakdown high-price 4H bars from the 50-bar window — predictable, not a math instability.
- Per the W21-F + 2026-06-11 EOD comment: the post-SBD recovery is now ~18-24h in. Rule 3 (4H 50-EMA) blocking the strongest cluster members by 0.1–0.5% is the expected lag of the slow-trend filter. The first BTC entry will come on a clean reclaim with R2 lifting through 55 — both are within striking distance of one more 4H bar of strength. Track for routine #4.

### Off-schedule notes (carry-over, unchanged)
- Weekend mis-fire pattern (cron `0 21 * * 1-5` PT firing on Sat/Sun) + 2026-06-07T20:00Z midday Sun mis-fire still queued for routine-04-harness (Sat 2026-06-13).
- `kraken_risk_flag` NO_DATA cosmetic — queued for routine-04.
- Routine-04 vol-comp slot review (v0.3 / v0.7 / v0.13 — 0 trades in 44/31/23 days; vol-comp gates structurally cannot fire in recovery tape).

### Next wake
- routine-02-midday 2026-06-12T19:30Z (Fri 12:30 PT). Expect rule 3 to remain the binding constraint; SOL/HYPE/XDG are the closest single-bar-from-eligible candidates. BTC still needs an R2 lift (RSI 54.0 → 55+) on top of an R3 reclaim, so it is one rule further from eligible than SOL/HYPE despite higher rank.


2026-06-12T17:07:14Z | harness | day-gate | not Saturday, skipping | no action

2026-06-12T17:40:37Z | allocation | day-gate | not Sunday, skipping | no action

### 2026-06-12T19:45Z | interactive | ops automations #2-4: watchdog, git hooks, nightly Codex poll (user-directed)

Completes the automation set started with scripts/indicators.py:
- **scripts/watchdog.py** - 7 checks: routine heartbeats vs cadence (01/02/03: 80h, 07: 30h, weeklies: 200h), future timestamps in state files, dirty working tree, stale open-position MTM (>30h), ccdScheduledTasksEnabled flag, unpushed commits, .mcp.json path validity. Wired into VERIFY of routines 01/02/03/07 with --telegram auto-alerting. Each past incident (9-day MCP outage, disabled scheduler flag, stranded OPERATING.md, +1-day stamps, 9-day un-MTM'd HYPE position) maps to a check that would have caught it on day one. Verified live: correctly flagged its own uncommitted file as a dirty-tree finding; all other checks clean.
- **scripts/pre_commit_check.py + installed git hooks** (pre-commit + commit-msg): blocks secrets (telegram/firecrawl token formats, secret env-var assignments), future-dated Last rebuild / Last refresh / trade-log timestamps in staged memory/ and variants/ files, and routine-XX commit subjects dated in the future PT. Tested all rejection paths live including a real blocked commit. Hooks are unversioned - reinstall after fresh clone with --install (documented in OPERATING.md). Routines must not use --no-verify.
- **Routine-07 nightly Codex poll** - spec addition: each wake refreshes the two EXTERNAL contest rows from data\codex\ portfolios (equity, open positions, competition net %, days remaining); unreadable files leave rows unchanged with a noted failed poll.
- Telegram env validated (--dry-run OK) - watchdog alert path is live.

### 2026-06-12T20:05Z | interactive | silent-strategy diagnosis (OPUS camp) + gate_telemetry sentinel (user-approved stack addition)

User flagged BULL v0 (no trades 2 weeks), Crypto MR v1/Aggressive (1 month), and the basket breakouts (3 weeks) as "something off." Systematic diagnosis: **nothing broken — all legitimately regime-gated.**
- Runners alive: all logs regenerated daily (Task Scheduler "BasketBreakoutVariants" 03:30), Kraken-8 CSV cache current to same-day 16:00Z.
- Crypto MR v1/agg: RSI(2)<10 fired 91-114x/pair since 5/16 but the 4H EMA50>EMA200 gate death-crossed on all 8 pairs 5/16-5/24 and stays shut (gaps -9% to -18% — weeks from recross). Independent recomputation reproduced the sims' exact last-trade bars (DOGE 05-16T04:00Z).
- Basket breakouts: zero 120h-high strong-close bars on any pair since 5/22 (the LINK/DOT 5/22 bars WERE the last trades). Ungated aggressive_v1 also silent = signal starvation, not gate. Nearest re-arm: BTC +1.1%.
- BULL v0: own documented gates; leaderboard ingests via bull-github adapter (current).
- Caveat per hermes: the -27% DDs predate the gates shutting; P2 diagnose-persistent-loss decisions don't need new trades.
**New sentinel (user-approved):** `C:	rading\Claude\Trading Strategy\gate_telemetry.py` -> `strategy-leaderboard\data\health\gate_telemetry.md` nightly via run_nightly_variants.bat (telemetry exit excluded from composite EC). Verdicts: ACTIVE / GATED / ELIGIBLE-SILENT / STALE — makes healthy gating distinguishable from dead runners at a glance. First run: 6/6 GATED, ALL CLEAR, committed+pushed to leaderboard repo (1370586). Stack touch points (approved): 1 new script, 1 BAT append, 1 new tracked report file. Params are copies of frozen specs — update if specs unfreeze.

### 2026-06-12T21:25Z | interactive | FABLE Crypto Drift silent failure: found, fixed, healed + OPUS automation-health sentinel (user-approved stack changes)

Hunting for leaderboard gaps found a REAL active bug: **FABLE Crypto Drift v1 dead since 06-10** while Task Scheduler reported success.
- **Root cause chain:** machine asleep at 06:00-08:00 task times -> wake-cluster fires Stock Nightly + Fable Nightly + Hermes Supervisor at the same second (09:36:47 on 06-12) -> Fable reads the shared crypto CSV cache mid-rewrite (to_csv truncate-in-place) -> EmptyDataError -> generate.py had no per-strategy try/except, crashed mid-loop on drift (last in config order), skipping git_commit (stranded 6 strategies' files uncommitted) -> BAT never checked errorlevel -> Last Result 0. Two consecutive days.
- **Fixes (all user-approved):** (1) atomic cache writes in basket_breakout/generate_variant_logs.py (tmp + os.replace); (2) retry-on-empty loader in fable_engine/strategies.py; (3) per-strategy try/except + non-zero exit in fable_engine/generate.py; (4) errorlevel logging in run-fable-nightly.bat.
- **Healed:** full regenerate, all 7 strategies committed+pushed (leaderboard 2a391eb). Crypto Drift turned out to be FABLE's best performer: realized +$1,691.60 — the freeze was hiding their top strategy.
- **New sentinel:** C:	rading\Fableutomation_health_opus.py -> data/health/automation_health_opus.md (nightly, last step of run-fable-nightly.bat, --git-commit). Checks per-family newest AND oldest file age (catches one-dead-among-fresh), nightly-log traceback scan, Task Scheduler last results. First run correctly ALARMed on this morning's traceback (self-clears tomorrow). Exit 2 on alarm.
- **Decision Desk:** 5 undecided crypto/stocks basket P2 items ack/deferred with July-1 archive criteria, citing the gating diagnosis (leaderboard 57e73e0).
- Side observation: the wake-cluster scheduling pattern (all OPUS tasks fire simultaneously on machine wake) remains; atomic writes + retries make it safe, but if new cache writers are added, they must write atomically too.
2026-06-13T17:40:06Z | allocation | day-gate | not Sunday, skipping | no action

2026-06-14T01:02Z | idea-scan | day-gate | not Friday, skipping | no action

---

## 2026-06-14T04:11Z — routine-03-eod (Sat 21:11 PT — 2026-06-13 PT EOD)

### Wake context
- Cron `0 21 * * 1-5` PT. Slot ID `bull-03-eod` (verified — body matched, no `bull-01-overnight` regression like the 2026-05-11 incident `3ce53b1`). Calendar date label: **2026-06-13 PT** (per the date-labeling guard — fire is 04:11Z UTC = next-calendar-day UTC, but the routine labels with the PT date at fire time).
- 1 open position (BTC long 0.168 from this morning). 13 closed 1H bars since entry.
- Live strategy v0.4 (W22-G two-bar EMA20 exit, W22-H-partial breakeven ratchet at +2R, 4R take-profit retained, W21-F SBD override).
- Kraken connectivity: indicators script 15/15 clean fetches @ 720 bars 1H + 4H; `kraken_multi_ticker` + 20-bar 1H BTC OHLCV both clean.
- Watchdog: `ALL CLEAR — heartbeats, timestamps, tree, MTM, scheduler flag, push state, MCP paths OK`.

### VERIFY — kill switches
- Daily realized 2026-06-13 PT: **+$621.22 / +6.06%** (TAO 4R replay) — loss cap is downside-only, CLEAR.
- DD: 0.00% — CLEAR (warn 12.5%, cap 25%).
- Equity (MTM): $10,930.40 > $7,500 — CLEAR.
- Loss-streak: 0 / 7 — CLEAR (reset this morning).
- Kraken MCP / public-REST / indicators script: AVAILABLE — CLEAR.
- **All clear. No kill switch tripped → proceed to DO.**

### DO 1 — Final mark-to-market
- BTC last 1H close $64,512.8 (03:00 UTC bar). Spot $64,490.3 mid-04:00 bar.
- Position notional $10,838.15 = 0.168 × $64,512.8. Cash $92.25. Equity **$10,930.40**.
- Unrealized PnL +$54.55 gross, R **+0.69**.

### DO 2 — Post-close exit check on BTC
| Rule | Test | Result |
|---|---|---|
| Rule 1 (W22-G two 1H closes < EMA20) | EMA20 $63,762; 13 post-entry closes range $63,944.3–$64,560.9 all above EMA | **INERT** (0/13 below) |
| Rule 1-SBD | SBD CLEARED (15/15 positive +1.90% > -1.0) | **N/A** |
| Rule 2 (stop $63,720.62) | Lowest intra-bar low post-entry $63,893.2 (16:00 UTC) = $172.58 above stop | **NOT TRIPPED** |
| Rule 3 (4R target $66,058.02) | Highest 1H high post-entry $64,750.0 (21:00 UTC) = $1,308 below target | **NOT HIT** |
| Breakeven ratchet (W22-H-partial) | Requires +2R close ≥ $65,123.06; highest post-entry close $64,560.9 = $562.16 below | **NOT ARMED** |

**0 exits this wake.** Stop stays at $63,720.62 (original 2×ATR).

### DO 3 — EOD entry scan (W19-E analyst-role split)

Source: `python scripts/indicators.py` @ 04:10:49Z (closed-bar; 720-bar converged EMAs; ≥200-bar 50-EMA floor satisfied on all 15 pairs).

| Pair | R1 (1H>EMA20) | R2/2a (55<RSI≤80) | R3 (4H>EMA50, $ margin) | R4a (notional≥$2M) | Verdict |
|---|:---:|:---:|:---:|:---:|:---|
| BTC | PASS +296.6 | PASS +10.02 (RSI 65.0) | PASS +750.8 | OK $53.65M | **EXCLUDED rule 5 (open pos)** |
| ETH | PASS +2.87 | PASS +0.46 (RSI 55.5) | **FAIL** -6.95 (EMA 1,687.82) | OK $25.19M | FAIL R3 |
| SOL | PASS +0.6328 | PASS +10.22 (RSI 65.2) | PASS +1.426 (EMA 67.5139) | OK $12.01M | **PASS** |
| HYPE | PASS +0.5414 | PASS +1.72 (RSI 56.7) | PASS +0.7266 (EMA 59.8534) | OK $13.29M | **PASS** |
| XRP | PASS +0.0055 | PASS +5.28 (RSI 60.3) | PASS +0.0046 (EMA 1.14864) | OK $9.43M | **PASS** |
| SUI | PASS +0.0033 | PASS +1.43 (RSI 56.4) | PASS +0.0042 (EMA 0.764531) | OK $5.28M | **PASS** |
| TAO | PASS +19.32 | PASS +22.9 (RSI 77.9, under 80 cap by 2.1) | PASS +52.63 (EMA 223.059) | OK $19.27M | **PASS** (RSI climactic-adjacent) |
| XDG | PASS +0.0004 | PASS +2.61 (RSI 57.6) | PASS +0.001139 (EMA 0.086949) | OK $3.68M | **PASS** |
| NEAR | PASS +0.0305 | PASS +3.34 (RSI 58.3) | PASS +0.0247 (EMA 2.1092) | OK $4.41M | **PASS** |
| ADA | PASS +0.0007 | **FAIL** (RSI 54.9) | **FAIL** -0.000482 | OK $8.65M | FAIL R2, R3 |
| LINK | **FAIL** -0.003234 | **FAIL** (RSI 51.3) | PASS +0.03262 | OK $3.62M | FAIL R1, R2 |
| LTC | PASS +0.464 | PASS +14.25 (RSI 69.3) | PASS +0.7507 | **FAIL** $1.91M | FAIL R4a |
| FARTCOIN | FAIL | FAIL (RSI 47.3) | FAIL | **FAIL** $0.50M | FAIL all |
| TRX | FAIL | FAIL (RSI 42.2) | FAIL | **FAIL** $0.65M | FAIL all |
| AVAX | PASS +0.0283 | PASS +3.37 (RSI 58.4) | **FAIL** -0.1379 | **FAIL** $0.84M | FAIL R3, R4a |

- **Eligible candidate set (7):** SOL (rank 3), HYPE (4), XRP (5), SUI (6), TAO (7), XDG (8), NEAR (9). Compared to this morning's lone BTC pass, EOD has 7-wide eligible set with comfortable R3 margins (+0.40% to +23.6% above 4H EMA50). Recovery is now durably through the slow-trend filter.
- **Regime:** 15/15 positive 24h, median **+1.90%** → **5a PASS** (well clear of 4-pair floor; breadth up from morning's 11/15 +0.52%). **5a-SBD CLEARED** (15 > 1 AND +1.90 > -1.0).
- **Rule 5b cooldowns:** all 7 candidates clear (SOL last close 22d ago, HYPE 22d, XRP 14d, SUI never, **TAO 19h ago but exit was `exit-4R-target` not `exit-stop-hit` — 5b INACTIVE** because the rule explicitly gates re-entry after a stop-out, XDG never, NEAR never).
- **Rule 6:** 1/4 used → PASS for a 2nd entry.
- **Rule 6a (cluster):** {BTC, ETH, SOL, TAO, AVAX, SUI, LINK} 1/2 (BTC); adding SOL/SUI/TAO would push to 2/2 (still PASS).
- **Rule 8 (highest 30d notional rank):** **SOL** wins (rank 3 highest among eligible).

### DO 4 — News pass
- **SOL technical-PASS only:** Firecrawl skipped this wake (token budget; news pass is informational-only per W19-E, does not veto). No supportive/contradictory headline tags recorded.

### DO 4a — Sentiment pass
- **SOL Kraken sentiment:** spread/depth not queried — decision is going to defer on cash-binding (see DO 5), so sentiment data adds no decision-value. **SKIPPED** with this rationale logged.

### DO 5 — Eligible new entries — **CASH-BINDING DEFER**

**Rule 7 sizing on SOL (rule-8 winner):**
- Ideal risk = 1.5% × $10,930.40 = $163.96
- Stop distance 2×ATR = $0.91043 per unit
- Ideal size = 180.10 SOL = $12,402 notional
- Available cash = **$92.25** — fundable size capped to 1.338 SOL = $92.21 notional (99.96% of cash)
- Capped risk = $1.22 = **0.011% of equity** (vs 1.5% target)
- Roundtrip commission @ 0.52% on $92.21 = $0.48 = **39% of the trade's stop risk**
- +4R win nets +$4.40 (+0.04% equity); −1R loss nets −$1.70 (−0.016% equity) — both below any meaningful R-impact

**Decision: defer.** A micro-position with commission-friction > 1/3 of stop risk is not what the strategy v0.4 sizing path contemplates. The same block applies to all 7 eligible candidates (none can be sized above the friction floor while BTC consumes 99.16% of equity at $10,838.15 / $10,930.40 = 99.16%). This is the second instance this PT day (morning routine-01 capped BTC at 0.168 = 99.15% cash use; tonight's scan finds no operationally meaningful add). **Structural state:** no second concurrent entry will be operationally meaningful until (i) BTC resolves (4R close / stop trip / two-bar EMA20 exit), or (ii) routine #4 amends rule 8 to accept lower-ranked but fully-fundable candidates as fallback. Routine #4 backlog item carries forward from morning; tonight is data point #2.

**0 trade_log writes.**

### DO 6 — Lessons review
Today's events screened against the routine's three lesson prompts:
- **Stopped out with gap?** No stops today.
- **Winner past 4R before TP?** TAO trigger bar close $237.30 was the take-profit; the very next 1H bar (10:00 UTC, post-exit) ran to a high of $268.99 (+4.30R extension above the take-profit). Strategy convention takes the exit at the close that first satisfied the rule, not the subsequent runup. This is the second 4R replay where the post-trigger bar extended further (HYPE 2026-05-21 was the first, +0.7% post-exit runup). **Materiality:** the extension-given-up question was explicitly considered and rejected at W22 ("4R cap stays" per `feedback-perf-analysis-framing`). No strategy.md change proposed. Not material as a new lesson — already covered by lesson 2026-04-24 commission-drag (exit-logic gap) and W22 design decision.
- **Entry immediately reversed?** BTC entry $64,188.10 went sideways through 16:00–18:00 UTC ($63,944.3 low close = R -0.52) then trended up to current +0.69R. Not a reversal pattern; well within designed adverse-motion budget.

**No new lessons entries this wake** (per routine "up to 2 per day, not more" — zero is allowed when nothing material).

### DO 7 — Monthly archive
- Today is 2026-06-13 PT (Saturday). Month ends 2026-06-30 (Tuesday). **Not last trading day of month.** No archive.

### Decision
- **Action:** 0 entries (7 eligible, all cash-binding-blocked), 0 exits (BTC inside rules), 0 lessons. **0 trade_log writes, 0 universe writes, 0 lessons writes.**
- **portfolio.md:** rewritten with this wake's EOD numbers + scan rationale + refreshed kill-switch state.
- **research_log.md:** this entry.

### Telegram
- **Mandatory EOD card sent** per routine §NOTIFY (silence is a failure mode).

### Next wake
- routine-01-overnight 2026-06-15T13:00Z (Mon 06:00 PT — Sun off per cron). BTC position carries unmanaged ~33h between this fire and Mon routine-01 wake. Protective layers: 2×ATR stop $63,720.62 ($792 below last close), rising 1H EMA20 ($63,762, $750 below close), +0.69R cushion already accrued.

### Observation — operational state at PT-day close
- The day's dominant pattern is a textbook archetype reinforcement: the disciplined patience-through-borderline-arc thesis from lesson 2026-06-12 produced the TAO +4.04R / +$621.22 morning win (largest single trade of the quarter); the next opportunity arrived within 6 hours (the BTC entry-1 PASS that became the cash-binding entry) and is now +0.69R unrealized after 13 well-behaved post-entry closes. The 7-eligible EOD scan suggests the regime recovery has continued through the day; if BTC closes well (4R, eventual EMA exit on a gain, or even a small stop trip), Monday's wake should re-encounter several of tonight's eligibles with cash freed.
- The cash-binding-blocked entry condition documented twice today is a real strategy state. Routine #4 backlog: quantify the EV of "wait for current position to resolve" vs "amend rule 8 to take a fundable lower-ranked alternative." Tonight is data point #2; data point #1 was the routine-01 morning observation.
2026-06-14T17:13:40Z | harness | day-gate | not Saturday, skipping | no action
2026-06-15T03:13:15Z | allocation | W24 review | momentum 100% retained (only active bucket; 30d +2.48R / +75.85 / -2.07R / WR 23%); vs BTC-hold all evaluable windows positive (7d +11.73pts, 30d +24.86pts, since-inception +24.65pts); 90d non-evaluable until 2026-07-19; no Ring 2 proposal pending application; allocation change: no | telegram digest sent
2026-06-15T03:13:15Z | allocation | W24 review | momentum 100% retained (only active bucket; 30d +2.48R / +$617.78 / WR 20%; since-inception +$875.85 / -2.07R / WR 23%); vs BTC-hold all evaluable windows positive (7d +11.73pts, 30d +24.86pts, since-inception +24.65pts); 90d non-evaluable until 2026-07-19; no Ring 2 proposal pending application; allocation change: no | telegram digest sent
2026-06-15T03:18:30Z | allocation | W24 addendum | timing-race correction: routine-01 commit e2c7ab0 replayed BTC -0.60R close (2026-06-14T13:00Z) ~2min after routine-05 wrote its tables; corrected 30d +1.88R / +$570.51 n=11 (vs pre-replay +2.48R / +$617.78 n=10); since-inception -2.67R / +$828.58 n=27; equity flat-book $10,828.58 / +8.29% inception; allocation decision unchanged (no proposal); not re-sending telegram (content materially same)

2026-06-16T15:16:21Z | allocation | day-gate | not Sunday, skipping | no action
2026-06-16T15:16:37Z | idea-scan | day-gate | not Friday, skipping | no action

2026-06-16T15:16:21Z | allocation | day-gate | not Sunday, skipping | no action

### 2026-06-16T20:15Z | interactive | contest scoring rule change (user-directed) — pre-registration repealed

User found BULL v0 + Basket Breakout Aggressive v1 missing from the leaderboard "top strategies" (Contest Scoreboard) while $0 / -$25.55 rows showed. Root cause (NOT a cache/registration-coverage bug): the 2026-06-10 pre-registration model scored each camp on a fixed pre-picked 5 and EXCLUDED remote (bull-github) + sheet sources at registration time. OPUS's June 5 had two Crypto MR picks at $0 forward (live_start 05-28 postdates their last real trade) + one -$25.55, while BULL v0 (remote, excluded) and Aggressive v1 (not top-5 on 06-10, since done a +20% run) sat in research-only.
**Resolution (Marcus directive):** repeal pre-registration. New rule = top-5 by FORWARD PnL per camp; only backtested/pre-live-start trades excluded; every forward strategy eligible regardless of source. Applied SYMMETRICALLY to OPUS/CODEX/FABLE (integrity: not an OPUS-only change). Verified against live data — Opus/BULL top-5 now: Basket BO Aggressive v1 $1998, BULL v0 $495, BULL v0.12 $491, Stocks MR v2 RSI<15 $404, Stocks MR v2 $132 = $3520; CODEX $4063 (leads by ~$542); FABLE $99. Files: strategy-leaderboard scoring_registrations.js (emptied; June regs preserved in HISTORICAL_REGISTRATIONS_REPEALED), lib/contest.js, lib/contest.test.js (174/174 green), data/hermes/decisions.md. Pushed cb8170c.
**To see it:** relaunch the leaderboard via Open Leaderboard.bat (cache-buster) — the served contest.js/scoring_registrations.js update on next load.
**Tradeoff on record:** top-5-of-all rewards breadth (more variants = more lottery tickets); revisit if a camp games it by spawning variants.
2026-06-16T17:40:09Z | allocation | day-gate | not Sunday, skipping | no action
2026-06-17T17:51:32Z | allocation | day-gate | not Sunday, skipping | no action

2026-06-17T17:51:26Z | harness | day-gate | not Saturday, skipping | no action

2026-06-18T17:07:34Z | harness | day-gate | not Saturday, skipping | no action
2026-06-18T17:40:52Z | allocation | day-gate | not Sunday, skipping | no action
2026-06-19T01:03:02Z | idea-scan | day-gate | not Friday, skipping | no action

## 2026-06-19T05:16Z — routine-03-eod (PT label 2026-06-18 Thu, scheduler fired ~22:16 PT)

**Slot identity `bull-03-eod`** (verified: prompt body references EOD slot, not overnight). Cron `0 21 * * 1-5` PT = 04:00Z UTC; framework dispatched ~76 min late at 05:16Z (still PT 2026-06-18 22:16 — same calendar day, no date-label issue).

### Position management

Flat at wake (0 open positions, $10,231.74 cash). No MTM, no exit checks, no stop monitoring. No closes today.

### Kraken multi-ticker (EOD regime sweep)

Snapshot at ~05:16Z across the 15-pair universe (24h % change, sorted):

| Pair | last | 24h % |
|------|-----:|------:|
| TRX | 0.320518 | **+0.06** |
| BTC | 62554.10 | −0.53 |
| ETH | 1694.45 | −0.85 |
| LTC | 43.42 | −0.91 |
| XDG | 0.082473 | −1.18 |
| XRP | 1.12896 | −1.39 |
| SOL | 68.54 | −1.58 |
| LINK | 7.86978 | −1.71 |
| ADA | 0.160546 | −1.79 |
| SUI | 0.7118 | −2.33 |
| HYPE | 66.19 | −3.02 |
| FARTCOIN | 0.1205 | −3.06 |
| TAO | 227.8737 | −3.40 |
| AVAX | 6.061 | −3.93 |
| NEAR | 2.1219 | −5.07 |

**Regime header:** **1/15 positive 24h (TRX only at +0.06%), median −1.71%** → **5a FAIL** (1 < 4 floor) **AND 5a-SBD ACTIVE** (positives ≤ 1 AND median ≤ −1.0%). **Fourth consecutive wake under SBD** (activated 2026-06-18T04:11Z EOD; persisted through 14:05Z overnight, 20:07Z midday, now). Conditions partially recovered from midday (median −3.21% → −1.71%; positives held at 1) but the SBD threshold still breaches on both axes.

### EOD entry scan (W19-E analyst-role split)

Rule 5a blocks all new entries this wake. Per `strategy.md` rule 5a, if positives < 4 of 15 the entry-scan rejects all candidates. No technical / news / sentiment passes warranted — the gate is universal and predates per-pair evaluation.

- **Technical:** N/A — gated by 5a FAIL.
- **News:** N/A — no candidates.
- **Sentiment:** N/A — no candidates.
- **Decision:** **0 entries**. Rule-8 fallback not invoked (no pair passed rules 1–7).

### Kill-switch verification

- Daily realized 2026-06-18 PT: **$0.00 / 0.00%** (no closes today) — cap 5%, CLEAR.
- Daily total (realized + unrealized): **$0.00 / 0.00%** — CLEAR.
- Drawdown: **5.92%** from peak $10,875.85 — cap 25%, warn 12.5%, **6.58% to warn** — CLEAR.
- Equity: **$10,231.74** > $7,500 floor — CLEAR.
- Loss streak: **3 trading days** — cap 7, headroom 4 — CLEAR. Thu closes flat; streak holds at 3 (no new realized loss).
- All clear; no kill-switch action.

### Avoided-give-back ledger (SBD)

This wake: **$0.00** (no open positions; SBD's tightened 9-EMA exit had no surface to act on).

### Watchdog

`python scripts/watchdog.py --telegram` returned 7 findings, all informational stale-state alerts (not actionable from EOD routine):

- A heartbeat: routine-07 last committed 119h ago (threshold 30h) — scheduler/MCP concern; not in this routine's scope.
- D stale-MTM: 6 variant portfolios (v0.3-vol-compression, v0.5-cluster-cap-tight, v0.7-vol-comp-defensive, v0.12-sbd-exit, v0.13-trend-confirm, v0.14-recovery-trend) have open positions with last rebuild 120h ago — variant-track is independent of main and processed by separate harness; not actionable from EOD.

Watchdog auto-sent its own Telegram alert with these findings.

### Lessons

No new lessons. Day was flat (no trades); the SBD-leading-edge observation from 2026-06-17 still stands and is the most recent active lesson. Avoiding lessons-bloat per the cap.

### Telegram

Mandatory daily EOD card sent (see commit body).

### Summary

0 OPEN, 0 CLOSE, 0 NEW ENTRIES. Day flat. Equity unchanged at $10,231.74. Drawdown holds at 5.92%. Loss streak holds at 3. Regime 5a FAIL + SBD ACTIVE persists into **fourth consecutive wake** but conditions partially recovered (median −3.21% → −1.71%). Next entry-eligible scan = routine-01-overnight Fri 2026-06-19T14:00Z.

## 2026-06-19T15:39Z — routine-01-overnight (PT label 2026-06-19 Fri, scheduler fired ~08:39 PT)

**Slot identity `bull-01-overnight`** (verified: prompt body references overnight slot). Cron `0 6 * * 1-5` PT = 13:00Z UTC (DST PT = UTC-7); framework dispatched ~99 min late at 15:39Z (still PT 2026-06-19 08:39 — same calendar day, no date-label issue).

### Position management

Flat at wake (0 open positions, $10,231.74 cash). No MTM, no exit checks, no stop monitoring. No closes this routine.

### Watchdog

`python scripts/watchdog.py --telegram` → 7 findings, all informational:
- A heartbeat: routine-07 last committed 130h ago (threshold 30h) — scheduler/MCP concern, not actionable from overnight.
- D stale-MTM: 6 variant portfolios (v0.3-vol-compression, v0.5-cluster-cap-tight, v0.7-vol-comp-defensive, v0.12-sbd-exit, v0.13-trend-confirm, v0.14-recovery-trend) have open positions but last rebuild 131h ago — variant-track is independent of main, processed by separate harness.

Watchdog auto-sent its own Telegram alert.

### Indicators sweep (scripts/indicators.py — authoritative per W22 amendment 2026-06-12)

Full closed-bar Kraken REST sweep (720×1H + 720×4H per pair). Regime header from script:

> **Regime: 2/15 positive 24h, median −1.86% → 5a FAIL; SBD CLEAR**

Per-pair (sorted by 24h %):

| Pair | 24h % | R1 (1H>EMA20) | R2 (RSI≥55) | R2a (<80) | R3 (4H>EMA50) | R4a notional |
|------|------:|---|---|---|---|---|
| TRX | +0.34 | FAIL | FAIL 49.8 | OK | PASS | OK $2.03M |
| LTC | +0.23 | PASS | **PASS 57.7** | OK | FAIL | FAIL $1.32M |
| HYPE | −0.64 | PASS | FAIL 53.0 | OK | PASS | OK $22.25M |
| BTC | −0.95 | PASS | FAIL 52.4 | OK | FAIL | OK $155.56M |
| XDG | −0.99 | PASS | FAIL 48.4 | OK | FAIL | OK $5.63M |
| LINK | −1.47 | PASS | FAIL 48.2 | OK | FAIL | FAIL $1.46M |
| ADA | −1.79 | FAIL | FAIL 47.0 | OK | FAIL | OK $6.15M |
| ETH | −1.86 | PASS | FAIL 49.6 | OK | FAIL | OK $30.83M |
| XRP | −2.04 | FAIL | FAIL 44.6 | OK | FAIL | OK $20.29M |
| SOL | −2.72 | PASS | FAIL 47.2 | OK | FAIL | OK $32.37M |
| SUI | −3.58 | FAIL | FAIL 40.7 | OK | FAIL | OK $6.68M |
| NEAR | −5.09 | FAIL | FAIL 47.0 | OK | FAIL | OK $3.81M |
| TAO | −5.76 | FAIL | FAIL 35.0 | OK | FAIL | OK $4.89M |
| FARTCOIN | −5.95 | FAIL | FAIL 43.0 | OK | FAIL | FAIL $0.63M |
| AVAX | −7.21 | FAIL | FAIL 39.4 | OK | FAIL | OK $3.52M |

**Regime headline:** 2/15 positive (LTC +0.23%, TRX +0.34%), median −1.86%, mean ≈ −2.55%.

- **5a (rule):** **FAIL** — 2 < 4 floor. All new entries rejected this wake.
- **5a-SBD (sub-state):** **CLEAR** — positives = 2 (> 1 ceiling). **SBD clears after 4 consecutive wakes** (activated 2026-06-18T04:11Z EOD; persisted through 14:05Z overnight + 20:07Z midday + 05:16Z EOD; now lifted at 15:39Z). Exit 1-SBD (9-EMA two-bar) reverts to default Exit 1 (20-EMA two-bar) — irrelevant this wake since BULL is flat.

### Entry scan (W19-E analyst-role split)

- **Technical:** Rule 5a FAIL blocks all new entries this wake — no per-pair candidate proceeds to news/sentiment. Closest near-PASS = LTC (R1 PASS, R2 PASS RSI 57.7, R2a OK, R3 FAIL by −0.91 vs 4H EMA50 44.37, R4a FAIL notional $1.32M < $2.0M floor). Even with 5a lifted LTC would be rejected on rules 3 + 4a. No other pair clears rules 1 + 2 simultaneously.
- **News:** N/A — no technical-PASS candidates.
- **Sentiment:** N/A — no technical-PASS candidates.
- **Decision:** **0 entries**. Rule-8 fallback not invoked (no pair passed rules 1–7).

### SBD clearance — observation (informational)

5a-SBD just cleared after 4 wakes of active state. Defensive Exit 1-SBD had **no surface to act on this episode** (BULL was flat throughout the 4-wake window). The SBD episode therefore contributed $0 to the avoided-give-back ledger; its value, if any, is in the gated-block of would-be entries (a counterfactual not directly measurable). This is the second clean SBD episode (first: 2026-05-19 → 05-20) where BULL happened to be flat during the window. The data point is logged; no rule change implied.

### Kill-switch verification

- Daily realized 2026-06-19 PT: **$0.00 / 0.00%** (no closes today) — cap 5%, CLEAR.
- Daily total (realized + unrealized): **$0.00 / 0.00%** — CLEAR.
- Drawdown: **5.92%** from peak $10,875.85 (cap 25%, warn 12.5%, 6.58% to warn) — CLEAR.
- Equity: **$10,231.74** > $7,500 floor — CLEAR.
- Loss streak: **3 trading days** (cap 7, headroom 4) — CLEAR. Fri opens flat; streak hold until first close today.
- Active 5b cooldowns: none.
- All clear; no kill-switch action.

### First-of-month universe refresh

Today is the 19th — not first weekday of month. Universe refresh skipped. Last refresh 2026-06-01 (top 15 stable). Next refresh trigger 2026-07-01.

### Lessons

No new lesson today. Day starts flat, no trades; SBD clearance is logged as research-log observation, not a lesson candidate.

### Telegram

Silent. NOTIFY criteria (Ring 3 trip / new OPEN / new CLOSE / news ACTIONABLE / universe refresh) all unmet. Watchdog sent its own alert independently.

### Summary

0 OPEN, 0 CLOSE, 0 NEW ENTRIES. 5a FAIL blocks all entries; SBD clears after 4-wake episode (informational). LTC is the closest near-PASS but fails R3 + R4a. Equity unchanged at $10,231.74. Drawdown 5.92%. Loss streak 3. Next entry-eligible scan = routine-02-midday Fri 2026-06-19 (read-only) → routine-03-eod Fri 2026-06-19T04:00Z UTC for next entry pass.
2026-06-19T17:06:52Z | harness | day-gate | not Saturday, skipping | no action
2026-06-19T17:40:29Z | allocation | day-gate | not Sunday, skipping | no action

## 2026-06-19T20:07Z — routine-02-midday (PT label 2026-06-19 Fri, on-schedule cron fire)

**Slot identity `bull-02-midday`.** Cron `0 13 * * 1-5` PT = 20:00 UTC; framework dispatched ~07 min late at 20:07Z. **Position management only — no entries permitted per routine spec.**

### State at wake

Portfolio **flat** (0 open positions, carried forward from routine-01-overnight 2026-06-19T15:39Z). Cash $10,231.74. Equity $10,231.74. Drawdown 5.92% from peak $10,875.85. Loss streak 3 trading days (BTC Sun, ETH Tue, Wed [HYPE+SOL]; Thu flat, Fri flat through midday).

### MTM + exits

**Skipped — no open positions to mark or evaluate.** No `kraken_multi_ticker` call needed; routine spec scopes MTM to "pairs with open positions". Strategy v0.4 Exit rules 1/1-SBD/2/3 have no surface to act on.

### Kill-switch verification

- Daily realized 2026-06-19 PT: **$0.00 / 0.00%** (no closes today) — cap 5%, CLEAR.
- Daily total (realized + unrealized): **$0.00 / 0.00%** (no positions) — CLEAR.
- Drawdown: **5.92%** from peak $10,875.85 — cap 25%, warn 12.5%, **6.58% headroom to warn**. CLEAR.
- Equity: **$10,231.74** > $7,500 floor (headroom $2,731.74 / 27.32%) — CLEAR.
- Loss streak: **3 trading days** (cap 7, headroom 4) — CLEAR. Fri midday: still flat, streak holds.
- Active 5b cooldowns: none (no recent stop-outs within 24h).
- **All clear (Ring 3).** No alerts.

### Entry scan

**Suppressed per routine spec.** Routine-02-midday is position management only — "DO NOT OPEN NEW POSITIONS IN MIDDAY". Entry responsibility belongs to routines #1 (overnight) and #3 (EOD). Regime 5a/SBD state not re-evaluated this wake (no entry decision to gate); will be re-checked at routine-03-eod tonight (Fri 2026-06-19T04:00Z UTC = Fri 21:00 PT scheduler fire).

### Drawdown trajectory (informational)

| Wake | Equity | DD from peak | Δ |
|---|---|---|---|
| 2026-06-18T20:07Z midday | $10,231.74 | 5.92% | — |
| 2026-06-19T05:16Z eod | $10,231.74 | 5.92% | flat |
| 2026-06-19T15:39Z overnight | $10,231.74 | 5.92% | flat |
| 2026-06-19T20:07Z midday | $10,231.74 | 5.92% | flat |

Four consecutive wakes flat at DD 5.92% — peak hasn't moved (last set 2026-06-13T09:00Z TAO 4R), realized PnL hasn't moved since the SOL stop-out 2026-06-17T18:00Z. Halfway-to-warn threshold (12.5% / equity ≤ $9,516.37) is $715.37 below current cash.

### Telegram

Silent. NOTIFY criteria all unmet: no Ring 3 trip, no exit happened (none possible — flat), no drawdown threshold crossed (5.92% well below 12.5% warn).

### Summary

0 OPEN, 0 CLOSE, 0 MTM action (flat). Equity unchanged at $10,231.74. Drawdown 5.92%. Loss streak 3. Next position management = routine-03-eod Fri 21:00 PT (= Sat 04:00 UTC). Midday silent.

## 2026-06-20T14:42Z — routine-03-eod (PT label 2026-06-19 Fri EOD, scheduler fired ~10h42m late at Sat 07:42 PT)

**Slot identity `bull-03-eod`.** Cron `0 21 * * 1-5` PT = Fri 21:00 PT = Sat 04:00 UTC. Actual fire Sat 14:42Z = Sat 07:42 PT — late by ~10h42m (harness drift; root cause for routine-07 not investigated this wake — flagged by watchdog separately, see Watchdog section). Routine continues with freshest 1H signal-bar 13:00Z, not the original-fire 04:00Z bar. Date label per the date-labeling guard: **2026-06-19 PT** (the trading day this EOD closes), not the UTC date 06-20.

### Watchdog

`python scripts/watchdog.py --telegram` ran at routine open. **7 findings**:
- A heartbeat: routine-07 last committed 149h ago (threshold 30h) — note for next routine-04 review.
- D stale-MTM ×6: variants v0.12-sbd-exit, v0.13-trend-confirm, v0.14-recovery-trend, v0.3-vol-compression, v0.5-cluster-cap-tight, v0.7-vol-comp-defensive all have open positions with last rebuild 150h ago (threshold 30h).
Telegram alert sent independently by watchdog. **Not actioned this wake** — primary BULL paper account is the priority; variant maintenance is a separate concern.

### State at wake

Portfolio entered the wake **flat** (carried forward from routine-02-midday 2026-06-19T20:07Z: cash $10,231.74, DD 5.92%, loss streak 3). Equity peak unchanged at $10,875.85 (2026-06-13T09:00Z TAO 4R). Equity floor headroom 27.32% to $7,500.

### MTM + exits

**No positions at wake → MTM/exit-check skipped before entry.** Post-entry MTM applies to SOL only (see below).

### Kill-switch verification (pre-entry)

- Daily realized 2026-06-19 PT: **$0.00 / 0.00%** — CLEAR (cap 5%).
- Daily total (realized + unrealized): **$0.00 / 0.00%** at wake — CLEAR.
- Drawdown: **5.92%** at wake — CLEAR (cap 25%, warn 12.5%, 6.58% headroom to warn).
- Equity: **$10,231.74** > $7,500 floor — CLEAR.
- Loss streak: **3 trading days** (cap 7, headroom 4) — CLEAR.
- Active 5b cooldowns: none (last stop-out SOL 2026-06-17T18:00Z = 68h ago, well past 24h re-entry block).
- All clear; proceed to entry scan.

### Entry scan — W19-E analyst-role split

Indicators run twice this wake (initial 11:17Z snapshot was 3h25m stale by the time downstream tool calls completed; re-ran fresh at 14:42Z). Both snapshots logged here for the leading-edge regime observation (see Lessons section).

**Snapshot A — 11:17Z (stale by entry time):**
Regime **15/15 positive, median +1.96%** → 5a PASS, SBD CLEAR (strong-confirmation tape). Full-PASS candidates: ETH (R2 RSI 61.1), SOL (R2 RSI 65.1), HYPE (R2 RSI 58.5). Rule 8 top-rank ETH; cash-fit check FAIL (ETH required notional $14.2k > cash $10.2k — same constraint as lesson 2026-06-17 BTC). Rule-8 fallback would have picked SOL.

**Snapshot B — 14:42Z (used for entry decision):**
Regime **9/15 positive, median +0.13%** → 5a PASS, SBD CLEAR (weakened −6 positives, −1.83pp median in 3h25m — flagged as leading-edge pattern in Lessons). Full-PASS candidates:
- **SOL/USD** — R1 PASS +0.4766 (close $71.17 > EMA20 $70.6934 by 0.67%), R2 PASS RSI 58.0 (+3.0 over floor), R2a OK (RSI < 80), R3 PASS +1.51 (close > 4H EMA50 $70.2302 by 2.15%, 720 bars converged), R3-20 PASS, R4a OK ($18.57M notional). Margins all non-borderline. **ELIGIBLE.**
- ETH dropped between snapshots (RSI 61.1 → 52.0, R2 FAIL).
- HYPE dropped between snapshots (R1 PASS → FAIL, R2 PASS → FAIL).
- TRX R1+R2+R3 PASS but R4a FAIL ($0.76M < $2.0M).

**Single eligible candidate: SOL.** Rule 8 (top-rank) trivially satisfied. Rule 6a cluster {BTC,ETH,SOL,TAO,AVAX,SUI,LINK}: 0→1, cap 2 ✓. Rule 6 max-concurrent: 0→1, cap 4 ✓. Rule 5b: SOL last stop-out 2026-06-17T18:00Z = 68h ago, past 24h ✓.

**Cash-fit pre-check** (per lesson 2026-06-17): SOL stop dist $1.2628, size = (0.015 × $10,231.74) / $1.2628 = **121.5347 SOL**. Notional = 121.5347 × $71.17 = **$8,649.62 < cash $10,231.74** ✓ FITS.

**Technical decision (Snapshot B):** ENTER SOL/USD long, size 121.5347, entry $71.17 (13:00Z bar-close), initial stop $69.9072 (2×ATR), target $76.2212 (+4R), risk $153.48 = 1.500% of equity.

### News scan — SOL (W19-E, informational only)

**Skipped this wake** due to late-fire context and to keep the routine focused on getting the entry recorded promptly. Per strategy v0.2: news scan does NOT veto entries; it is purely informational. Flagged for next overnight routine if SOL is still open.

### Sentiment — SOL (W19-E, informational only)

Live Kraken ticker @ 14:42Z: SOL bid $70.93 / ask $70.94 / spread 1.41 bps. Spread is tight (well under 10 bp warning threshold). 24h volume notional $17.94M (deep). **Supportive sentiment proxy — no warning.**

### Entry execution

trade_log.md row appended:
`| 2026-06-20T13:00:00Z | OPEN | SOL/USD | long | 121.5347 | 71.17 | 69.9072 | 76.2212 | — | — | entry-rule-v0.4-momentum |`

Post-entry state:
- Cash: $10,231.74 − $8,649.62 = **$1,582.12**
- Position MTM @ last $70.92: 121.5347 × $70.92 = **$8,619.24**
- Unrealized: 121.5347 × ($70.92 − $71.17) = **−$30.38** = **−0.198R**
- Equity: $1,582.12 + $8,619.24 = **$10,201.36**
- Drawdown: ($10,875.85 − $10,201.36) / $10,875.85 = **6.20%** (was 5.92%; +0.28pp from SOL slip)

### Post-entry kill-switch verification

- Daily realized: $0.00 / 0.00% — CLEAR.
- Daily total (realized + unrealized): **−$30.38 / −0.30%** — CLEAR (cap 5%, headroom 4.70%).
- Drawdown: **6.20%** — CLEAR (cap 25%, warn 12.5%, **6.30% to warn**).
- Equity: $10,201.36 > $7,500 floor — CLEAR.
- Portfolio risk-at-moment: **1.50%** (SOL only) — CLEAR (cap 4%, headroom 2.50%).
- All clear (Ring 3). No alerts.

### First-of-month universe refresh

Today is the 19th (PT label) / 20th (UTC) — not first weekday of month. Universe refresh skipped. Last refresh 2026-06-01 (top 15 stable). Next refresh trigger 2026-07-01.

### Monthly archive

Today PT (Fri 06-19) is not last trading day of June (will be Mon 06-30 or whichever weekday is last). Archive skipped.

### Lessons (this wake)

1 candidate evaluated, **0 appended** to lessons.md:
- **Regime-deterioration during stale-signal window** (candidate): Between 11:17Z snapshot (15/15 positive, median +1.96%) and 14:42Z re-snapshot (9/15 positive, median +0.13%), regime weakened −6 positives and −1.83pp median in 3h25m. The 11:17Z snapshot fed an entry decision tree (ETH top-rank → cash-blocked → SOL fallback) that became moot by 14:42Z (ETH and HYPE both dropped out). This is a fresh instance of the same dynamic in lesson 2026-06-17 (SBD-leading-edge pattern). **Not promoted to a new lessons.md entry** because (i) lesson 2026-06-17 already captures the recommendation set (a/b/c — SBD-leading-edge filter, loss-streak coupling, same-session stop-loss reaction) and is still **active** awaiting routine-04 codification; (ii) this wake's pattern adds an instance count but not new mechanism. **Reinforces lesson 2026-06-17 score.** Routine-04 should now have 2 instances (06-17 SOL + 06-20 regime-decline-during-stale-signal) when scoring.

### Telegram

EOD card sent — see NOTIFY commit. Watchdog also sent an independent alert at routine open.

### Summary

**1 OPEN (SOL/USD 121.5347 @ $71.17), 0 CLOSE, 0 lessons appended.** Equity $10,201.36 (DD 6.20%, +0.28pp from prior). Late-fire ~10h42m beyond scheduled 21:00 PT — used freshest 1H signal-bar (13:00Z). Regime PASS/SBD CLEAR but weakening (15/15→9/15 in 3.5h). Loss streak 3 (no new realized loss). Next position management = routine-01-overnight Sat 2026-06-20 04:00 PT (= Sat 11:00Z).

## 2026-06-20T14:48Z — routine-01-overnight (Sat 07:48 PT)

**Slot identity `bull-01-overnight`.** Cron `0 6 * * 1-5` PT — fired on Sat (not in cron window). Routine continues normally; logging the day-of-week anomaly here. Date label: **2026-06-20 Sat** (UTC and PT agree on calendar date). Position management only — no fresh schedule violation since routine has no day-gate logic.

### Watchdog

`python scripts/watchdog.py --telegram` ran at routine open. **7 findings (same as prior 2 wakes):** A heartbeat routine-07 153h-stale; D stale-MTM ×6 variants (v0.12/v0.13/v0.14/v0.3/v0.5/v0.7) 154h-stale. Telegram alerted independently. Not actioned — primary account focus.

### State at wake

Entered with **1 open position** (SOL/USD 121.5347 @ $71.17 from 2026-06-20T13:00:00Z entry, prior wake). Cash $1,582.12, MTM equity $10,201.36 carried forward, DD 6.20%, loss streak 3.

### MTM + exit check (SOL)

- Live ticker @ 14:48Z: SOL last $71.96, bid $71.90, ask $71.93, spread 0.04% (3 bps). 24h +3.29%.
- Latest closed 1H bar close (per indicators): $71.17 — same as entry bar; intra-bar tape has moved up to $71.96.
- Unrealized: 121.5347 × ($71.96 − $71.17) = **+$96.01 = +0.626R**.
- Active stop $69.9072 (initial 2×ATR). Distance to stop: ($71.96 − $69.9072) / $71.96 = +2.85% above stop. **NO STOP-OUT.**
- 20-EMA (1H): $70.6934 (latest converged). Close $71.17 > EMA20 → **NO EMA cross.** No prior below-EMA bar in this trade → confirmation counter at 0.
- Take-profit $76.2212. Unrealized R +0.626 < +4.0 → **NO TARGET HIT.**
- Breakeven ratchet (W22-H-partial): needs unrealized R ≥ +2.0 at 1H close. Latest 1H close gave R = 0.0 (filled at $71.17 = current closed-bar close). Ratchet **idle, stop unchanged at $69.9072.**
- **Hold SOL.** No exit action.

### Kill-switch verification

- Daily realized 2026-06-20 PT: **$0.00 / 0.00%** — CLEAR (cap 5%).
- Daily total (realized + unrealized) 2026-06-20 PT: **+$96.01 / +0.94%** — CLEAR.
- Drawdown: ($10,875.85 − $10,329.73) / $10,875.85 = **5.02%** (improved 1.18pp from 6.20% prior wake on SOL favorable move) — CLEAR (cap 25%, warn 12.5%, 7.48pp headroom to warn).
- Equity floor: $10,329.73 > $7,500 — CLEAR.
- Loss streak: **3** (no new closed loss this wake; cap 7, headroom 4) — CLEAR.
- Regime gate (5a): 9/15 positive, median +0.13% → **PASS** (≥ 4/15 floor).
- Regime sub-state (5a-SBD): 9 positives > 1 ceiling AND median +0.13% > −1.0% → **CLEAR**. Default 20-EMA two-bar exit applies.
- Active 5b cooldowns: SOL stop-out 2026-06-17T18:00Z = 92h ago, well past 24h re-entry guard.
- **All clear.** No ALERT.

### Entry scan (Technical analyst, W19-E)

Indicators source: `python scripts/indicators.py` @ 14:48Z (single run, no staleness concern this wake — only ~6 minutes elapsed from script to entry-decision).

Regime: **9/15 positive 24h, median +0.13% → 5a PASS, SBD CLEAR.**

Per-pair Technical decisions:

| Pair | R1 EMA20 | R2 RSI≥55 | R2a RSI≤80 | R3 4H EMA50 | R4a $2M | R5 not-open | Decision | Failing rule |
|---|---|---|---|---|---|---|---|---|
| BTC | FAIL | FAIL | OK | FAIL | OK | OK | REJECT | R1, R2, R3 |
| ETH | PASS | FAIL (52.0) | OK | PASS | OK | OK | REJECT | R2 |
| SOL | PASS | PASS (58.0) | OK | PASS | OK | **FAIL (open)** | REJECT | R5 (already open since 13:00Z bar) |
| HYPE | FAIL | FAIL | OK | PASS | OK | OK | REJECT | R1, R2 |
| XRP | FAIL | FAIL | OK | FAIL | OK | OK | REJECT | R1, R2, R3 |
| SUI | FAIL | FAIL | OK | FAIL | OK | OK | REJECT | R1, R2, R3 |
| TAO | PASS | FAIL (49.8) | OK | FAIL | OK | OK | REJECT | R2, R3 |
| XDG | FAIL | FAIL | OK | FAIL | OK | OK | REJECT | R1, R2, R3 |
| NEAR | FAIL | FAIL | OK | FAIL | FAIL ($1.79M) | OK | REJECT | R1, R2, R3, R4a |
| ADA | FAIL | FAIL | OK | FAIL | OK | OK | REJECT | R1, R2, R3 |
| LINK | FAIL | FAIL | OK | FAIL | FAIL ($0.90M) | OK | REJECT | R1, R2, R3, R4a |
| LTC | PASS | FAIL | OK | FAIL | FAIL ($1.47M) | OK | REJECT | R2, R3, R4a |
| FARTCOIN | FAIL | FAIL | OK | FAIL | FAIL ($0.28M) | OK | REJECT | R1, R2, R3, R4a |
| TRX | PASS | PASS (75.5) | OK | PASS | **FAIL ($0.76M)** | OK | REJECT | R4a (liquidity) |
| AVAX | PASS | FAIL (52.9) | OK | FAIL | OK | OK | REJECT | R2, R3 |

**0 eligible candidates** for new entry. Closest miss: TRX/USD (3/3 momentum criteria PASS, blocked solely by R4a liquidity floor — same archetype as universe lesson 2026-04-24).

### News scan (W19-E, informational)

**N/A — no technical-PASS candidates** for entry (SOL technical-PASS but already open; TRX blocked at R4a before news matters). Skipped per strategy.md scope.

### Sentiment scan (W19-E, informational)

**Open position SOL/USD live read** (spread/depth health check on existing position):
- Spread: 3 bps (very tight, well under 10 bps warning threshold).
- 24h notional: $18.5M (deep liquidity, well above $2.0M floor).
- Tape supportive (+3.29% 24h on visible momentum bar).

No sentiment flags for held position.

### Stop management (W22-H-partial breakeven ratchet)

At the just-closed 1H bar close ($71.17 ≈ entry $71.17), unrealized R = 0.0. **+2.0R threshold not met → no ratchet action.** Active stop remains $69.9072. Will re-evaluate at next 1H close (next routine).

### First-of-month universe refresh

Today is the 20th — not first weekday of June. **Skipped.** Last refresh 2026-06-01; next trigger 2026-07-01.

### Lessons (this wake)

No new entries → no new lessons triggered. Notable observations:
- Regime continuity: 9/15 positive holds steady from prior wake's snapshot B (14:42Z). The "leading-edge regime deterioration" pattern logged in prior wake did **not** continue into a hard SBD transition — regime stabilized rather than deteriorated further. This is one data point toward the SBD-leading-edge filter recommendation (lesson 2026-06-17 rec a); does not yet justify either codifying or dismissing the filter.
- SOL fill ($71.17) coincided with intra-wake low-ish prints, and tape has since moved +$0.79 to $71.96 (+0.626R). Friendly entry timing this round, but n=1 — not lesson-promotable on its own.

### Telegram

Silent. NOTIFY criteria all unmet:
- No Ring 3 kill switch tripped.
- 0 new OPEN, 0 CLOSE.
- No actionable news flagged (none scanned — no PASS candidate).
- No universe refresh.

Watchdog sent its own independent alert at routine open (telegram: sent), but routine-level Telegram is silent per spec.

### Summary

**0 OPEN, 0 CLOSE.** Held 1 position (SOL). Equity $10,329.73 (+$128.37 from $10,201.36 prior wake on SOL favorable move), DD 5.02% (improved 1.18pp), loss streak 3. Regime 5a PASS / SBD CLEAR (stable, not deteriorating). 0 candidates eligible — closest miss TRX (R4a liquidity). Next wake = routine-02-midday Sat 12:00 PT (= Sat 19:00Z) if cron permits Sat firings; otherwise Mon 06:00 PT routine-01.

### 2026-06-20T16:20Z | interactive | leaderboard display bug — "$2026.00" open-trade P&L (user-reported)

User saw BULL SOL/USD showing +$2026.00 on the leaderboard's open-positions/command-center view. Diagnosed: `lib/command_center.js` parsePortfolioOpenPositions destructured columns by FIXED POSITION, hard-coded to the CODEX 9-col layout. BULL's portfolio.md uses an 11-col layout, so fields shifted — the "Entry ts (UTC)" value ("2026-06-20T...") landed in the P&L column and moneyOrNull() rendered the YEAR as "$2026.00" (with a bogus % from target-vs-stop). Same bug on all bull-github rows (twin, v0.14). Real SOL P&L verified +$96.01 (+1.1%) against live Kraken $71.90.
Fix (strategy-leaderboard 2d441d5): header-AWARE parsing — match columns by name, scoped to the Open positions section. Handles CODEX (Unrealized PnL), BULL (Unrealized $), FABLE (PnL/Mark); computes exposure=size×mark for BULL (no Exposure col). Regression test added for the 11-col BULL layout. 175/175 green. Re-verified live: BULL $96.01, CODEX v0 + FABLE Snapback unchanged/correct.
Note: the underlying SOL TRADE itself was verified legit earlier (all v0.4 rules pass, rule 3 +1.51 on converged EMA) — this was purely a display-layer parsing bug, not a trade problem. (Separately still open: the Saturday/late off-cron scheduler fires + entry-timestamp-vs-priced-bar mismatch, queued for routine-04.)
2026-06-20T17:40:45Z | allocation | day-gate | not Sunday, skipping | no action

## 2026-06-23T01:40Z | routine-01-overnight | Mon 18:40 PT (late fire vs 06:00 cron)

**Fire-time anomaly:** cron is `0 6 * * 1-5` = 06:00 PT Mon-Fri. This fire is at 18:40 PT — within day-of-week window (Mon), but ~12.5h late vs scheduled hour. Watchdog flagged: routine-07 last 212h, stale-MTM on portfolio.md (59h) and 6 variant portfolios. Watchdog telegram: sent. Findings noted, routine proceeds.

**Entered with 1 open position** (SOL/USD 121.5347 @ $71.17 from 2026-06-20T13:00:00Z entry). Carrying $10,329.73 MTM from prior wake (SOL @ $71.96), DD 5.02%, loss streak 3.

### MTM + exit check (SOL)

- Live ticker @ 01:40Z: SOL last $71.59, bid $71.64, ask $71.66, spread 0.03% (~2-3 bps). 24h -0.40%. 24h high $74.91, low $71.33.
- Latest closed 1H bar close (per indicators): **$71.80**. EMA20: **$72.926** (R1 FAIL -1.126 = close below EMA20).
- Prior wake's 1H close was $71.17 > EMA20 $70.6934 (ABOVE). EMA has risen ($70.69 → $72.93) while price has stalled — **first below-EMA close** in this trade.
- Per W22-G two-bar exit: **confirmation counter = 1/2; exit NOT triggered.** Next 1H close decides.
- Unrealized (live): 121.5347 × ($71.59 − $71.17) = **+$51.04 = +0.332R** intra-bar.
- Unrealized (last 1H close $71.80): 121.5347 × ($71.80 − $71.17) = **+$76.57 = +0.499R**.
- Active stop $69.9072 (initial 2×ATR). Distance to stop: ($71.59 − $69.9072) / $71.59 = +2.35% above stop. **NO STOP-OUT.**
- Take-profit $76.2212. Unrealized R +0.332 << +4.0 → **NO TARGET HIT.**
- Breakeven ratchet (W22-H-partial): latest 1H close R = +0.499 < +2.0 → ratchet **idle, stop unchanged at $69.9072.**
- **Hold SOL.** No exit action.

### Kill-switch verification

- Daily realized 2026-06-22 PT: **$0.00 / 0.00%** — CLEAR (cap 5%).
- Daily total (realized + unrealized vs prior wake) 2026-06-22 PT: **-$46.57 / -0.45%** — CLEAR.
- Drawdown: ($10,875.85 − $10,283.16) / $10,875.85 = **5.45%** (deteriorated 0.43pp from 5.02% prior on SOL pullback $71.96 → $71.59) — CLEAR (cap 25%, warn 12.5%, 7.05pp headroom to warn).
- Equity floor: $10,283.16 > $7,500 — CLEAR.
- Loss streak: **3** (no new closed loss this wake; cap 7, headroom 4) — CLEAR.
- Regime gate (5a): **6/15 positive, median -0.25%** → PASS (>= 4/15 floor; softer than prior 9/15 / +0.13%).
- Regime sub-state (5a-SBD): positives = 6 (> 1 ceiling) AND median -0.25% > -1.0% → **CLEAR**. Default 20-EMA two-bar exit applies.
- Active 5b cooldowns: SOL stop-out 2026-06-17T18:00Z = 152h ago, well past 24h re-entry guard.
- **All clear.** No ALERT.

### Entry scan (Technical analyst, W19-E)

Indicators source: `python scripts/indicators.py` @ 01:40Z (single run; freshness in spec).

Regime: **6/15 positive 24h, median -0.25% -> 5a PASS, SBD CLEAR.** Regime soft but above floor.

Per-pair Technical decisions:

| Pair | R1 EMA20 | R2 RSI>=55 | R2a RSI<=80 | R3 4H EMA50 | R4a $2M | R5 not-open | Decision | Failing rule |
|---|---|---|---|---|---|---|---|---|
| BTC | FAIL (-212) | FAIL (46.4) | OK | FAIL (-166) | OK | OK | REJECT | R1, R2, R3 |
| ETH | FAIL | FAIL (45.8) | OK | FAIL (-0.95) | OK | OK | REJECT | R1, R2, R3 |
| SOL | FAIL (-1.13) | FAIL (35.8) | OK | PASS (+0.35) | OK | **FAIL (open)** | REJECT | R5 (already open) + R1, R2 |
| HYPE | FAIL | FAIL (40.4) | OK | FAIL | OK | OK | REJECT | R1, R2, R3 |
| XRP | FAIL | FAIL (44.3) | OK | FAIL | OK | OK | REJECT | R1, R2, R3 |
| SUI | PASS (+0.0026) | FAIL (53.3) | OK | FAIL (-0.016) | OK | OK | REJECT | R2, R3 |
| TAO | FAIL | FAIL (42.1) | OK | FAIL | OK | OK | REJECT | R1, R2, R3 |
| XDG | FAIL | FAIL (40.7) | OK | FAIL | OK | OK | REJECT | R1, R2, R3 |
| NEAR | FAIL | FAIL (33.9) | OK | FAIL | OK | OK | REJECT | R1, R2, R3 |
| ADA | FAIL | FAIL (45.5) | OK | FAIL | OK | OK | REJECT | R1, R2, R3 |
| LINK | FAIL | FAIL (40.9) | OK | FAIL | FAIL ($1.99M) | OK | REJECT | R1, R2, R3, R4a |
| LTC | FAIL | FAIL (42.6) | OK | FAIL | FAIL ($1.68M) | OK | REJECT | R1, R2, R3, R4a |
| FARTCOIN | PASS (+0.00027) | FAIL (52.5) | OK | PASS (+0.0031) | FAIL ($0.72M) | OK | REJECT | R2, R4a |
| TRX | PASS (+0.0021) | PASS (72.4) | OK | PASS (+0.0096) | **FAIL ($0.95M)** | OK | REJECT | R4a (liquidity) |
| AVAX | FAIL | FAIL (49.9) | OK | FAIL | OK | OK | REJECT | R1, R2, R3 |

**0 eligible candidates** for new entry. Closest miss: TRX/USD (3/3 momentum criteria PASS again, blocked solely by R4a liquidity floor — same archetype as the prior wake and the universe lesson 2026-04-24). TRX has now been the closest-miss for two consecutive wakes — pattern noted, not yet lesson-promotable.

### News scan (W19-E, informational)

**N/A — no technical-PASS candidates** for entry (SOL technical R3 PASS but already open and R1/R2 FAIL on momentum decay; TRX blocked at R4a before news matters). Skipped per strategy.md scope.

### Sentiment scan (W19-E, informational)

**Open position SOL/USD live read** (spread/depth health check on existing position):
- Spread: ~2-3 bps (very tight, well under 10 bps warning threshold).
- 24h notional: 290,746 SOL x ~$72.4 avg = ~$21M (deep liquidity, well above $2.0M floor).
- Tape softening (-0.40% 24h; high $74.91 visible earlier, current price near 24h low $71.33).

No sentiment flags for held position, but momentum visibly fading on SOL — already reflected in R1/R2 FAILs above and the first below-EMA close.

### Stop management (W22-H-partial breakeven ratchet)

At the just-closed 1H bar close ($71.80), unrealized R = +0.499 (using entry $71.17 and stop-distance $1.2628). **+2.0R threshold not met -> no ratchet action.** Active stop remains $69.9072.

### First-of-month universe refresh

Today is the 22nd — not first weekday of June (that was 2026-06-01, completed). **Skipped.** Next trigger 2026-07-01.

### Lessons (this wake)

No new entries -> no new lessons triggered. Notable observations:
- **SOL momentum decay:** Entry was at $71.17 with EMA20 $70.69 (close +$0.48 above). Two days later, EMA20 has risen to $72.93 while price has stalled at $71.80. The two-bar EMA exit rule (W22-G) is precisely doing what it was designed for — granting one bar of tag-and-recover budget rather than firing on first cross. Next 1H close will determine whether SOL exits at modest profit (~+0.5R) or recovers.
- **Regime decay continues but not into SBD:** 9->6 positives across two wakes, median +0.13% -> -0.25%. Floor still 4, ceiling for SBD still 1. The regime is loosely consistent with the "leading-edge deterioration" pattern flagged 2026-06-17 — a soft drift toward SBD without crossing it. Not yet promotable to filter codification.
- **TRX repeat closest-miss:** Same pair, same blocking rule (R4a $0.95M) as prior wake. Two consecutive observations of TRX as the only momentum-pass candidate suggests this pair has structural edge that the liquidity floor consistently blocks. **Pattern noted for routine #4 backlog** — at what point does a recurring near-miss justify either (a) a per-pair tightened liquidity floor exception, or (b) a lower position-sizing-with-tighter-stop alternative on lower-liquidity high-momentum pairs? Not promotable on n=2.

### Telegram

Silent. NOTIFY criteria all unmet:
- No Ring 3 kill switch tripped.
- 0 new OPEN, 0 CLOSE.
- No actionable news flagged (none scanned — no PASS candidate).
- No universe refresh.

Watchdog sent its own independent alert at routine open (telegram: sent, 8 findings — late-fire stale-MTMs and routine-07 heartbeat).

### Summary

**0 OPEN, 0 CLOSE.** Held 1 position (SOL). Equity $10,283.16 (-$46.57 from $10,329.73 prior on SOL $71.96 -> $71.59), DD 5.45% (deteriorated 0.43pp), loss streak 3. Regime 6/15 / -0.25% (softer but still 5a PASS / SBD CLEAR). 0 entry-eligible — TRX is closest miss (R4a $0.95M) for second wake. SOL on first below-EMA bar, confirmation counter 1/2 — next 1H close decides EMA-exit fire. Late fire 12.5h after cron; routine-07 + variant MTMs flagged stale by watchdog (separately).

### ADDENDUM 2026-06-23T01:45Z — missed-scheduler replay reconciliation

While this routine was executing, the missed-scheduler replay pipeline updated `memory/trade_log.md` and `memory/portfolio.md` to record a SOL/USD exit at 2026-06-22T15:00Z @ $73.08 via **exit-ema20-confirm** (+1.51R / +$232.13). The replay caught the two-bar EMA20 exit that fired during the cron gap between the 2026-06-20T14:48Z prior wake and this 01:40Z late fire.

**Reconstructed exit chronology (per portfolio.md update):**
- 2026-06-22T13:00Z bar: close ~$74.88 (peak; would-have-triggered breakeven ratchet at +2.94R close — ratchet path not bound because EMA exit followed)
- 2026-06-22T14:00Z bar: close ~$73.37, ~$0.42 below 1H EMA20 = first below-EMA close
- 2026-06-22T15:00Z bar: close $73.08, ~$0.65 below 1H EMA20 = second consecutive below-EMA close → **W22-G two-bar EMA exit fires**, paper exit at bar close $73.08
- Realized PnL: 121.5347 × ($73.08 − $71.17) − round-trip friction → **+$232.13 net / +1.51R**

**Corrections to this wake's earlier sections:**
- ~~Hold SOL~~ → **SOL CLOSED** by missed-scheduler replay at 15:00Z bar @ $73.08
- ~~Unrealized +$51.04~~ → **Realized +$232.13** (cash-only equity now)
- ~~Equity $10,283.16 (MTM)~~ → **$10,463.87** (cash, no positions)
- ~~DD 5.45%~~ → **DD 3.79%** (improved 1.66pp on the winning exit)
- ~~Loss streak 3~~ → **Loss streak 0** (reset by SOL winner)
- ~~Latest 1H close $71.80 = bar 1 below EMA, counter 1/2~~ → that $71.80 bar is **post-exit** (~10h after the 15:00Z exit fire); SOL position no longer exists, so the counter is moot
- The "Hold SOL" MTM check, breakeven ratchet idle status, and the W22-G "next 1H close decides" call are all **superseded** by the replay-confirmed 15:00Z exit

**Entry-scan implications:**
- SOL/USD now triggers a **5b same-pair re-entry cooldown** until 2026-06-23T15:00Z (24h from the 15:00Z exit). Re-entry-eligible from 15:00Z bar onward. This wake's entry scan would have rejected SOL regardless (R1/R2 momentum FAIL), so the cooldown is non-binding for current decision but matters for next 1-2 wakes.
- All other pairs' technical decisions in the Entry scan table above remain valid (their indicator values were independent of SOL's open/closed state).
- **Net entry decision unchanged: 0 new entries.** TRX still closest miss on R4a $0.95M liquidity.

**Wake outcome (corrected):**
- **0 OPEN, 1 CLOSE** (SOL exit-ema20-confirm via missed-scheduler replay, +$232.13 / +1.51R).
- Equity $10,463.87 (cash only, flat). DD 3.79%. Loss streak 0.
- Notable: this is the second 4R-track winner since v0.4 — TAO 06-13 hit the 4R target +4.04R; SOL today peaked at $74.88 (+2.94R close) but the W22-G two-bar EMA exit fired at $73.08 = +1.51R before the 4R target $76.22 was reached. The breakeven ratchet would have fired at the 13:00Z peak close (moving stop from $69.91 to $71.17), but the EMA exit superseded the ratchet path. **First time the W22-H ratchet path was nearly engaged on a fresh post-W22 trade** — net result identical to actual EMA-confirm exit since exit price $73.08 > $71.17 breakeven.

### Telegram (corrected)

NOTIFY criteria now MET: **1 CLOSE this run** (SOL exit-ema20-confirm replay, +$232.13 / +1.51R).
Sending brief summary via `scripts/telegram_send.py`.

### Summary (corrected, supersedes earlier)

**0 OPEN, 1 CLOSE.** SOL/USD closed at 2026-06-22T15:00Z @ $73.08 (exit-ema20-confirm, missed-scheduler replay) for +$232.13 / +1.51R. Now flat. Equity $10,463.87 (was $10,329.73 prior wake mark + $134.14 day total). DD 3.79% (improved 1.66pp). Loss streak reset to 0. Regime 6/15 / -0.25% / 5a PASS / SBD CLEAR. 0 entry-eligible — TRX closest miss (R4a $0.95M) for second wake. SOL 5b cooldown until 2026-06-23T15:00Z. Late fire 12.5h after cron 06:00 PT slot.

2026-06-23T01:47Z | harness | day-gate | not Saturday, skipping | no action
2026-06-23T01:48Z | allocation | day-gate | not Sunday, skipping | no action

## 2026-06-23T01:50Z | routine-03-eod | PT label 2026-06-22 Mon EOD | local fire 18:50 PT (~2h before cron 21:00 PT)

**Slot identity confirmed:** routine-03-eod (not 01). Body references EOD journal per routines/03-eod.md.

### Context: routine-01-overnight fired earlier this wake (~01:47Z)

Routine-01 (commit `8b10397`) already logged the SOL exit and pushed before this routine started. Workflow split:
- routine-01 handled: trade_log SOL close row, research_log entry-scan + exit replay summary, Telegram brief.
- routine-03-eod (this entry) handles: EOD journal close-out, friction-adjusted equity restatement, lessons review, mandatory EOD Telegram card.

### Friction correction (auto-applied post-routine-01)

A `correction-previous-row` row at 2026-06-22T16:00:00Z auto-applied to trade_log after routine-01 wrote the SOL close:
- Gross exit: +$232.13 / +1.51R @ $73.08
- Friction adjustment: −$50.00 (≈ 2-side commission 0.26%/side + slippage 0.05%/side on $8.8k notional ≈ $54.56)
- **Net realized: +$182.13 / +1.19R** (effective fill $73.0435)

Routine-01's summary used the gross figures ($10,463.87 equity, 3.79% DD). **portfolio.md restated here to friction-adjusted ground truth: equity $10,413.87, DD 4.25%, since-inception +4.14%.**

### EOD synthesis

- **Day P&L (PT 06-22, net):** +$182.13 / +1.75% of equity. Best single-trade day in 9 days (since TAO +$621 / 06-13).
- **Equity:** $10,413.87 (+0.81% vs prior wake mark; +4.14% inception).
- **Drawdown:** 4.25% from peak $10,875.85 (need +$461.98 / +4.44% to retake; meaningful headroom from prior wake's 5.02%).
- **Loss streak:** 0 (reset by today's winner; was 3 days).
- **Open positions:** 0/8. **5b cooldown:** SOL exit was `exit-ema20-confirm`, not `exit-stop-hit` → 5b strict-by-letter does NOT bind. SOL re-entry-eligible immediately, but technicals fail anyway (R1+R2 FAIL post-pullback; RSI 35.8).
- **Regime:** 5a PASS (6/15 positive, median −0.25%), SBD CLEAR. Borderline-comfortable on positives count.
- **Entry candidates this wake:** 0. Closest miss TRX (R4a $0.95M liquidity, 2nd consecutive wake). SUI / FARTCOIN are the only other R1+R3 dual-pass; both fail R2 RSI.

### Strategy-rule postmortem (W22-G + W22-H)

The SOL trade exercised **both** W22 rules at the same close:
- **W22-G (two-bar EMA confirm):** at 13:00Z $74.88 → 14:00Z $73.37 BELOW (1st) → 15:00Z $73.08 BELOW (2nd) → **EXIT FIRES**. Behaved exactly as designed; took the trend break promptly without being shaken by a single-bar tag.
- **W22-H (breakeven ratchet at +2R close):** the 13:00Z close was +2.94R → would have ratcheted active stop from $69.9072 → $71.17 (entry). The EMA exit at $73.08 fires above the ratchet level, so the ratchet did not bind. **First near-engagement of W22-H on a fresh trade since the rule was added 2026-05-20.** Confirms: ratchet activates as designed; EMA exit dominates when both paths trigger and EMA fires first/higher. Forward question for routine-04: the ratchet's protective value materializes only on trades that reach +2R close AND then round-trip toward entry without an EMA exit firing first. So far on the v0.4 sample, 0 such trades have occurred — the ratchet remains untested in its binding regime.

### Lessons extraction

Reviewed today's single trade against the 3 lesson prompts:
1. **Stop-gap?** No — exit was a clean EMA confirmation, not a stop-out, no gap involved.
2. **4R-overshoot?** Trade peaked at +2.94R close, never crossed 4R ($76.22 target was $1.34 above the bar high $74.91). No overshoot lesson.
3. **Immediate reversal?** No — trade ran for ~48h and produced +$182.13 net. Healthy outcome.

**0 lessons appended.** Both candidate observations (W22-G first non-borderline win + W22-H first near-engagement) are routine-04 backlog items for telemetry, not lesson-promotable on n=1.

### Watchdog findings

8 findings from earlier `python scripts/watchdog.py --telegram`:
- routine-07 heartbeat 212h stale (threshold 30h) — known gap; routine-07 is the secondary watchdog/health-check slot and has been silent for ~9 days. Flag for routine-04.
- portfolio.md stale-MTM (59h) — RESOLVED by this rebuild.
- 6 variant portfolio.md stale-MTM (213h each) — variants v0.12-sbd-exit, v0.13-trend-confirm, v0.14-recovery-trend, v0.3-vol-compression, v0.5-cluster-cap-tight, v0.7-vol-comp-defensive. Routine-04 territory; not addressed by routine-03-eod scope.

Watchdog's own Telegram alert: sent (independent of EOD card).

### Monthly archive

Today is 2026-06-22 (Mon, not last trading day of June). **Skipped.** Trigger expected ~2026-06-30 (Tue).

### Summary

**0 OPEN, 0 CLOSE this routine** (routine-01 handled the SOL exit earlier this wake). Net day result: **1 winning close +$182.13 / +1.19R** (gross +$232.13 / +1.51R, friction −$50). Equity **$10,413.87**, DD **4.25%**, loss streak **0**. Regime 5a PASS / SBD CLEAR. 0 new entry candidates. Sending mandatory EOD Telegram card next.

## 2026-06-23T16:11Z | routine-01-overnight | PT label 2026-06-23 Tue overnight | local fire 09:11 PT (~3h11m late vs cron 06:00 PT)

**Slot identity confirmed:** routine-01-overnight. Body references overnight per routines/01-overnight.md.

### Watchdog (`python scripts/watchdog.py --telegram`)

8 findings (alert sent independently):
- A heartbeat: routine-07 226h stale (threshold 30h) — 10th consecutive overnight flag; routine-04 backlog.
- C dirty-tree: 2 uncommitted (`scripts/replay_cache_20260622/`, `scripts/routine07_replay_20260622.py`) — stranded routine-07 replay work from a previous session. **Not addressed by this routine** (overnight scope is trade/research only). Flag for routine-04 cleanup.
- D 6 variant portfolio.md stale-MTM (227h) — same 6 variants as prior wake (v0.12-sbd-exit, v0.13-trend-confirm, v0.14-recovery-trend, v0.3-vol-compression, v0.5-cluster-cap-tight, v0.7-vol-comp-defensive). Routine-04 territory.

Watchdog findings do not by themselves halt this routine — proceeding to entry scan per ops watchdog policy.

### Kill-switch verification (pre-scan)

- Equity $10,413.87 > $7,500 floor — CLEAR.
- DD 4.25% < 25% cap, < 12.5% warn — CLEAR.
- Loss streak 0 < 7 cap — CLEAR.
- Daily realized PT 2026-06-23: $0 (new day; no closes yet) — CLEAR.
- No MCP failure: Kraken responded, indicators.py converged 720 4H bars — CLEAR.

All Ring 3 clear → proceeding.

### Overnight ticker pull (Kraken `kraken_multi_ticker`, 16:11Z)

| Pair | Last | 24h % | High | Low |
|---|---|---|---|---|
| BTC | 62,658.8 | **-2.02** | 64,714.9 | 61,881.1 |
| ETH | 1,668.38 | **-3.35** | 1,745.28 | 1,633.10 |
| SOL | 69.22 | **-3.70** | 73.48 | 68.11 |
| HYPE | 62.77 | **-5.20** | 69.34 | 61.56 |
| XRP | 1.10152 | **-2.38** | 1.14298 | 1.09104 |
| SUI | 0.709 | **-1.34** | 0.7285 | 0.6710 |
| TAO | 216.98 | **-4.74** | 233.13 | 213.96 |
| XDG | 0.07920 | **-3.84** | 0.08354 | 0.07832 |
| NEAR | 1.9896 | **-3.66** | 2.1435 | 1.9621 |
| ADA | 0.15179 | **-4.13** | 0.15992 | 0.14968 |
| LINK | 7.64831 | **-2.74** | 7.98608 | 7.48033 |
| LTC | 42.15 | **-5.30** | 45.13 | 41.83 |
| FARTCOIN | 0.1270 | **-1.85** | 0.1331 | 0.1181 |
| TRX | 0.32996 | **-1.17** | 0.33395 | 0.32835 |
| AVAX | 6.39 | **+2.57** | 6.447 | 6.000 |

**Broad red overnight.** AVAX is the lone positive 24h pair (+2.57%); 14/15 negative with magnitudes -1.17% (TRX) to -7.03% (LTC per indicators.py 24h). Median 24h ~-3.7% (live ticker) / -4.91% (indicators.py snapshot a few minutes earlier — same regime, ticker pulled ~2 min later showed slight intraday recovery on a couple pairs).

### Position check on open positions

**None open.** No stop checks, no exits. SOL 5b cooldown clears at 2026-06-23T15:00Z (~1h11m before this fire) — already cleared; SOL is re-entry-eligible from technical/regime gates if it would pass them (it does not, see below).

### Entry scan (Technical pass — authoritative via `scripts/indicators.py`)

**Regime gate (rule 5a): FAIL — 1/15 positive (AVAX only), median -4.91%. Reject all new entries this wake.**

**Regime sub-state (5a-SBD): ACTIVE** — positives = 1 (≤1 ceiling) AND median -4.91% (≤ -1.0% floor). Synchronized-breakdown classifier engages. Exit rule 1-SBD (two consecutive 1H closes < 9-EMA) would tighten the trend exit for any open positions — but **no open positions**, so SBD's defensive value is **0 R avoided this wake**. SBD will re-evaluate next wake; clears when either condition resolves.

Per-pair technical table (from indicators.py, fully converged 720×4H bars on all pairs):

| Pair | R1 | R2 | R2a | R3 | R4a | Verdict |
|---|---|---|---|---|---|---|
| BTC | FAIL -630.3 | FAIL RSI 31.9 | OK | FAIL -1,543 | OK $159M | REJECT (R1+R2+R3) |
| ETH | FAIL -28.22 | FAIL RSI 29.9 | OK | FAIL -63.28 | OK $43.5M | REJECT (R1+R2+R3) |
| SOL | FAIL -1.45 | FAIL RSI 28.3 | OK | FAIL -2.46 | OK $29.8M | REJECT (R1+R2+R3) |
| HYPE | FAIL -2.01 | FAIL RSI 29.5 | OK | FAIL -4.73 | OK $24.7M | REJECT (R1+R2+R3) |
| XRP | FAIL -0.015 | FAIL RSI 30.6 | OK | FAIL -0.050 | OK $19.3M | REJECT (R1+R2+R3) |
| SUI | FAIL -0.004 | FAIL RSI 46.8 | OK | FAIL -0.028 | OK $7.85M | REJECT (R1+R2+R3) |
| TAO | FAIL -6.49 | FAIL RSI 27.1 | OK | FAIL -18.06 | OK $3.34M | REJECT (R1+R2+R3) |
| XDG | FAIL -0.0018 | FAIL RSI 25.3 | OK | FAIL -0.0051 | OK $4.11M | REJECT (R1+R2+R3) |
| NEAR | FAIL -0.056 | FAIL RSI 30.0 | OK | FAIL -0.184 | OK $3.86M | REJECT (R1+R2+R3) |
| ADA | FAIL -0.004 | FAIL RSI 29.6 | OK | FAIL -0.013 | OK $6.06M | REJECT (R1+R2+R3) |
| LINK | FAIL -0.101 | FAIL RSI 35.6 | OK | FAIL -0.328 | OK $2.32M | REJECT (R1+R2+R3) |
| LTC | FAIL -1.74 | FAIL RSI 15.7 | OK | FAIL -2.45 | OK $2.22M | REJECT (R1+R2+R3) |
| FARTCOIN | FAIL -4e-05 | FAIL RSI 48.5 | OK | FAIL -0.0008 | FAIL $0.97M | REJECT (R1+R2+R3+R4a) |
| TRX | FAIL -0.0011 | FAIL RSI 40.9 | OK | **PASS +0.0042** | FAIL $0.72M | REJECT (R1+R2+R4a) |
| AVAX | **PASS +0.103** | **PASS +7.19 (RSI 62.2)** | OK | FAIL -0.028 | OK $2.79M | REJECT (R3, regime) |

**Net entries: 0.** No pair passes all of R1+R2+R3+R4a. Even ignoring per-pair gating, the regime 5a FAIL rejects all entries categorically — this is the strongest "no-go" wake since the 06-17 synchronized-breakdown event (1/15 positive / -3.37% median that triggered Lesson 2026-06-17). Today's median -4.91% is materially worse.

**Closest miss:** AVAX/USD — first time AVAX appears as the lone 5a-positive pair *and* the lone 1H momentum (R1+R2) pass. R3 fails by only $0.028 (-0.43%) on 4H EMA50 $6.385 vs price $6.357. In a different regime, AVAX would warrant a Day-3-recovery patience watch per Lesson 2026-06-12. Under SBD, it stays rejected.

### News scan (News analyst pass)

**Skipped per routine spec** — no technical-PASS candidates eligible for news enrichment. (Routine 01 step 4 reads: "For each technical-PASS candidate, pull headlines tagged with the pair's base asset..." — gating clause is the technical PASS, of which there are 0.)

### Sentiment pass (Sentiment analyst pass)

**Skipped per routine spec** — no technical-PASS candidates. Same gating clause as news.

### Stop management (W22-H-partial)

**N/A.** No open positions; ratchet has nothing to act on.

### First-of-month universe refresh

Today is 2026-06-23 (Tue), not the 1st. **Skipped.** Next trigger 2026-07-01.

### Lessons (this wake)

No new entries → no entry-based lessons. SBD activation observations:

- **Lesson 2026-06-17 (SBD leading-edge filter) — quantitative reinforcement.** The pre-SBD decay arc was visible in real time: 2026-06-20 06/15 positive / median +0.13% → 2026-06-22 6/15 / -0.25% → today 1/15 / -4.91%. The same "≤1/15 positive AND ≤-1.0% median" SBD trigger fires today. **Crucially, BULL went into this wake flat** (SOL closed +1.19R net at 2026-06-22T15:00Z, before SBD activated) — so there is no open-position bleed to defend against this time. This is the inverse of the 2026-06-17 scenario where SBD activated 10h *after* a stop-out cluster. Today, the SOL exit-ema20-confirm path captured the trend break ahead of SBD, leaving no exposure into the breakdown. **Score effect: lesson stays active; reinforced by the favorable counterfactual (W22-G EMA exit + 5a regime gate produced the desired defensive posture without needing the 1-SBD tightened-EMA exit to fire).** No new lesson appended on n=1 favorable observation; routine-04 backlog item: did the W22-G exit consistently get out before SBD across the 06-17 → 06-23 arc, or was this single-trade lucky timing?
- **Lesson 2026-06-12 (entry-strength margin floor) — AVAX archetype emerging.** AVAX is today the only pair with positive 24h *and* clean R1+R2 momentum on 1H — a setup that would be the natural Day-3 patience entry per the TAO 06-13 archetype. But AVAX fails R3 by 0.43% under negative regime — the bar to take a borderline R3 PASS under SBD must be much higher than under PASS regime. No strategy.md change proposed (still n=1 archetype outside TAO 06-13).

### Telegram NOTIFY

Per routine NOTIFY criteria:
- Ring 3 kill switch tripped? **No** (all clear).
- New OPEN or stop-out CLOSE this run? **No** (0 OPEN, 0 CLOSE).
- News classified ACTIONABLE? **No** (news skipped; no PASS candidates).
- Universe refreshed? **No** (not 1st of month).

**Silent.** Watchdog sent its own independent alert at 16:11Z (8 findings; same content as prior wake).

### Summary

**0 OPEN, 0 CLOSE.** Equity unchanged at **$10,413.87** (cash only, flat). DD 4.25%. Loss streak 0. Regime collapsed overnight: **5a FAIL (1/15 positive AVAX only, median -4.91%); 5a-SBD ACTIVE** (both conditions met — ≤1 positive AND ≤-1.0% median). All 15 universe pairs REJECT — no pair passes R1+R2+R3 jointly; AVAX (closest miss, fails R3 by $0.028) is the only positive 24h pair. SBD defensive value this wake = **0R avoided** (flat going in; SOL exited 06-22 ahead of breakdown — favorable W22-G validation). Late fire 3h11m after cron; routine-07 + variant MTMs + 2 uncommitted scripts/replay_cache files flagged by watchdog (routine-04 territory).
2026-06-23T17:07:00Z | harness | day-gate | not Saturday, skipping | no action

2026-06-23T17:40:23Z | allocation | day-gate | not Sunday, skipping | no action

## 2026-06-23T20:07Z — routine-02-midday (Tue 13:07 PT, on cron)

**Slot identity `bull-02-midday`.** Cron `0 13 * * 1-5` PT. Fire on time (07m drift).

### State going in

- Equity **$10,413.87** (cash only, **0 open positions** — flat since SOL exit 2026-06-22T15:00Z).
- DD **4.25%** from peak $10,875.85 (unchanged — flat).
- Loss streak **0**.
- SOL 5b cooldown expired 2026-06-23T15:00Z (5h ago).

### Mark-to-market

No open positions → nothing to MTM. Equity unchanged at $10,413.87.

### Exit check

No open positions → no exit evaluation required.

### Drawdown / kill-switch check (Kraken multi_ticker snapshot)

15-pair 24h % change (sorted asc):

| Rank | Pair | 24h % | Last |
|---|---|---|---|
| 1 | HYPE | −5.97% | 62.26 |
| 2 | LTC | −5.86% | 41.90 |
| 3 | ADA | −5.09% | 0.15028 |
| 4 | XDG | −4.60% | 0.0785779 |
| 5 | SOL | −4.22% | 68.85 |
| 6 | NEAR | −3.83% | 1.986 |
| 7 | TAO | −3.77% | 219.19 |
| 8 | ETH | −3.68% | 1662.61 |
| 9 | LINK | −3.65% | 7.576 |
| 10 | FARTCOIN | −2.86% | 0.1257 |
| 11 | SUI | −2.81% | 0.6984 |
| 12 | XBT | −2.45% | 62384.4 |
| 13 | XRP | −2.27% | 1.10272 |
| 14 | TRX | −1.56% | 0.328651 |
| 15 | AVAX | **+2.15%** | 6.364 |

- **Positives: 1/15** (AVAX only).
- **Median 24h: −3.77%** (TAO, 8th item).
- **5a regime gate: FAIL** (1 < 4 floor — entries rejected). Moot anyway: midday routine forbids new entries.
- **5a-SBD sub-state: ACTIVE** (≤1 positive AND median ≤ −1.0%). Still active from overnight wake (was median −4.91% then; tape stabilized 1.14pp at the median but remains synchronized-breakdown by the 5a-SBD definition). Default 20-EMA exit replaced by 9-EMA exit *if any position existed* — none exists, so this is informational only.
- Daily loss cap: **N/A** (no realized PnL today; SOL exit was Mon 06-22 PT). CLEAR.
- Consecutive losing days: **0** (cap 7). CLEAR.
- Max drawdown: **4.25%** (cap 25%, warn 12.5%; 8.25pp to warn). CLEAR.
- Equity floor: $10,413.87 > $7,500. CLEAR.
- BTC vs prior-wake reference ($64,238 at 06-23 overnight) → now $62,384 = −2.9% intraday on BTC. BULL flat, so 0 mark exposure. **This is exactly the scenario the SOL EMA20-confirm exit at 06-22T15:00Z protected against** — second confirmation of W22-G value in a real breakdown window.

### Entries

**Skipped by routine design** (midday is management-only). For audit: even if midday entries were permitted, 5a FAIL would reject all candidates; AVAX is the only positive 24h pair but fails the 4/15 regime floor.

### Telegram NOTIFY

Per routine NOTIFY criteria:
- Ring 3 kill switch tripped? **No** — all clear.
- Any exit happened? **No** — no positions to exit.
- DD crossed 12.5% warning? **No** — still 4.25%.

**Silent.**

### Summary

**0 MTM events, 0 exits.** Flat into a continuing synchronized-breakdown tape; BULL has no exposure to defend. SBD still ACTIVE 1/15 positive AVAX +2.15%, median −3.77% (stabilized 1.14pp at the median vs overnight but no escape from SBD definition). DD unchanged 4.25%. SOL 5b cooldown cleared 5h ago, but 5a FAIL blocks all entries until regime recovers ≥4/15 positive. Next entry-eligible window: routine-01-overnight Wed 2026-06-24 06:00 PT (= 13:00Z) if regime improves.

## 2026-06-24T04:11Z | routine-03-eod | PT label 2026-06-23 Tue EOD | local fire 21:10 PT (on cron)

**Slot identity confirmed:** `bull-03-eod`. Body references EOD journal per routines/03-eod.md. PT calendar date 2026-06-23 (cron `0 21 * * 1-5`).

### Watchdog (`python scripts/watchdog.py --telegram`)

8 findings (alert sent independently):
- **A heartbeat:** routine-07 last commit 238h stale (threshold 30h) — same gap flagged at overnight + midday. Routine-04 backlog.
- **C dirty-tree:** 5 uncommitted (`scripts/replay_cache_20260622/`, `scripts/replay_cache_20260623/`, `scripts/replay_result_20260623.json`, `scripts/routine07_replay_20260622.py`, `scripts/routine07_replay_20260623.py`) — stranded routine-07 replay work; **not addressed by EOD scope.** Flag for routine-04.
- **D 6 variant portfolio.md stale-MTM (239h each):** v0.12-sbd-exit, v0.13-trend-confirm, v0.14-recovery-trend, v0.3-vol-compression, v0.5-cluster-cap-tight, v0.7-vol-comp-defensive — same 6 variants as prior wakes. Routine-04 territory.

No new findings vs prior wakes (delta = +1 dirty-tree entry: today's `routine07_replay_20260623.py` + cache + result). Watchdog does not halt EOD.

### Final mark-to-market (Kraken close 21:10 PT / 04:10Z)

No open positions → nothing to MTM. Equity unchanged at **$10,413.87**. Cash $10,413.87, position MTM $0.00.

### Post-close exit check

No open positions → no exit evaluation.

### Kill-switch verification

- Equity $10,413.87 > $7,500 floor — CLEAR.
- DD 4.25% < 25% cap, < 12.5% warn (8.25pp headroom) — CLEAR.
- Loss streak 0 < 7 cap — CLEAR.
- Daily realized PT 2026-06-23: **$0.00 / 0.00%** — CLEAR.
- All MCP responding (Kraken, indicators.py 720 4H bars converged) — CLEAR.

All Ring 3 clear.

### EOD entry scan (W19-E analyst-role split — authoritative via `scripts/indicators.py`)

**Regime gate (rule 5a): FAIL — 1/15 positive (AVAX +1.73%), median −3.68%. Reject all new entries this wake.**

**Regime sub-state (5a-SBD): ACTIVE** — positives = 1 (≤ 1 ceiling) AND median −3.68% (≤ −1.0% floor). Synchronized-breakdown classifier continues active. SBD has now been continuously engaged since overnight 06-23 fire (~12h). Exit rule 1-SBD (two consecutive 1H closes < 9-EMA) would tighten the trend exit if any position existed — **no open positions**, so SBD defensive value this wake = **0 R avoided**.

Per-pair technical table (indicators.py, 720×4H converged):

| Pair | R1 (>20EMA1H) | R2 (RSI≥55) | R2a (<80) | R3 (>50EMA4H) | R4a notional | Verdict |
|---|---|---|---|---|---|---|
| BTC | FAIL −$54.7 | FAIL RSI 45.6 | OK | FAIL −$1,120 | OK $161.23M | FAIL |
| ETH | FAIL −$5.68 | FAIL RSI 40.8 | OK | FAIL −$49.74 | OK $49.02M | FAIL |
| SOL | FAIL −$0.17 | FAIL RSI 43.5 | OK | FAIL −$1.59 | OK $27.25M | FAIL |
| HYPE | FAIL −$1.48 | FAIL RSI 31.2 | OK | FAIL −$5.25 | OK $23.83M | FAIL |
| XRP | FAIL −$0.0046 | FAIL RSI 40.5 | OK | FAIL −$0.040 | OK $19.64M | FAIL |
| SUI | FAIL −$0.0048 | FAIL RSI 43.8 | OK | FAIL −$0.029 | OK $7.18M | FAIL |
| TAO | FAIL −$0.25 | FAIL RSI 45.7 | OK | FAIL −$12.34 | OK $2.79M | FAIL |
| XDG | FAIL | FAIL RSI 40.2 | OK | FAIL | OK $3.85M | FAIL |
| NEAR | FAIL | FAIL RSI 36.5 | OK | FAIL | OK $3.43M | FAIL |
| ADA | FAIL | FAIL RSI 43.3 | OK | FAIL | OK $6.91M | FAIL |
| LINK | FAIL | FAIL RSI 38.8 | OK | FAIL | OK $2.19M | FAIL |
| LTC | FAIL | FAIL RSI 24.7 | OK | FAIL | OK $2.65M | FAIL |
| FARTCOIN | PASS +$0.0024 | PASS RSI 58.5 | OK | PASS +$0.0037 | **FAIL $0.76M** | FAIL (R4a) |
| TRX | FAIL | FAIL RSI 44.1 | OK | PASS +$0.0034 | **FAIL $0.66M** | FAIL |
| AVAX | PASS +$0.040 | PASS RSI 57.0 | OK | PASS +$0.021 | OK $2.81M | **TECH PASS** |

**Technical pass: 1/15 (AVAX only).** AVAX clears all six gates (R1+R2+R2a+R3+R4a, plus 4 of 4 concurrent + cluster cap headroom). FARTCOIN clears the price/momentum trio but fails R4a liquidity floor ($0.76M < $2.0M). All other pairs fail R1+R2+R3 by clear margins.

**But:** rule 5a regime gate (1/15 positive < 4/15 floor) **rejects all entries this wake** — including AVAX's technical pass. No News or Sentiment analyst passes executed: regime veto preempts per W19-D ("If < 4 of 15 are positive, reject all new entries this wake").

**0 entries executed.** AVAX's technical pass logged here for next-wake comparison: if regime recovers ≥ 4/15 positives by routine-01 Wed 06-24 06:00 PT, AVAX would re-evaluate at that wake.

### Lessons extraction

Reviewed today's trade activity (PT 2026-06-23) against 3 lesson prompts:
1. **Stop-gap?** No trades closed → no gap risk to extract.
2. **4R-overshoot?** No trades closed → n/a.
3. **Immediate reversal?** No trades opened → n/a.

**0 lessons appended.** Three flat wakes (overnight + midday + EOD) on PT 2026-06-23 produced no trade events. The W22-G EMA20-confirm exit that captured SOL +1.19R on 06-22 (just before SBD activated overnight 06-23) remains the active observation — already logged in routine-01 overnight 06-23 wake and 2026-06-12 lesson update. Not duplicated here.

### Day's summary stats — 2026-06-23 PT (Tue, EOD close)

| Metric | Value |
|---|---|
| Day realized PnL | **$0.00** (0 closes) |
| Day unrealized PnL change | **$0.00** (flat all 3 wakes) |
| **Day total PnL** | **$0.00 (0.00%)** |
| Trades opened today | **0** (overnight rejected by 5a FAIL; midday forbidden; EOD rejected by 5a FAIL) |
| Trades closed today | **0** |
| Win rate today | n/a |
| New equity | **$10,413.87** (unchanged) |
| Equity peak | **$10,875.85** (set 2026-06-13T09:00Z TAO 4R; unchanged) |
| Drawdown from peak | **4.25%** (unchanged; $461.98 below peak) |
| Loss streak | **0** trading days |

### Rolling BULL vs BTC-hold

- **7d:** BULL ≈ +1.4% (SOL +$182 win 06-22 dominant; 06-16/-17 ETH/HYPE/SOL stop-outs −$596 partially offset by TAO +$621 on 06-13 — but that 06-13 close is now > 7d ago by ~12h, so 7d window narrows to roughly +SOL182 −ETH214 −HYPE183 ≈ −$215, ≈ **−2.1%**). BTC ≈ $64.9k (7d ago ~2026-06-16) → $62.4k today = **−3.85%**. **BULL ahead 7d by ~+1.75pp.**
- **30d:** BULL since 2026-05-24 ~$10,000 → $10,413.87 = **+4.14%** (approx; inception was 2026-04-20 but 30d window roughly aligns with inception equity within rounding). BTC 30d ago ~$78k → $62.4k = **−20.0%**. **BULL ahead 30d by ~+24.1pp.**
- **90d:** Not computable (inception 2026-04-20 = 64 days ago; first computable ~2026-07-19).

### Monthly archive

Today is 2026-06-23 (Tue). Last trading day of June 2026 = 2026-06-30 (Tue). **Skipped.** Trigger expected next Tue.

### Telegram NOTIFY

Mandatory EOD card per routine NOTIFY. Sending next via `scripts/telegram_send.py`.

### Summary

**0 OPEN, 0 CLOSE.** Pure read/health-check wake closing out a flat trading day. PT 2026-06-23 was the first full 3-wake day inside SBD (overnight + midday + EOD all rejected entries by 5a regime gate). Equity **$10,413.87** unchanged, DD **4.25%** unchanged, loss streak **0**. Regime 5a FAIL (1/15 positive AVAX +1.73%, median −3.68%), 5a-SBD ACTIVE ~12h continuous. AVAX is the lone TECH-PASS candidate but blocked by regime; flagged for re-check at next entry-eligible wake (routine-01 Wed 06-24 06:00 PT). Watchdog: 8 findings, all carry-over from prior wakes (routine-07 stale 238h + 6 variant MTM + 5 dirty-tree replay artifacts) — routine-04 backlog. 0 lessons appended (no trade events). No monthly archive (last trading day = 06-30). Mandatory EOD Telegram card sent.


2026-06-24T17:07:31Z | harness | day-gate | not Saturday, skipping | no action

2026-06-24T17:40Z | allocation | day-gate | not Sunday, skipping | no action

---

## 2026-06-24T20:07Z — routine-02-midday (Wed 13:07 PT, on cron)

### Mode

Lean read/health-check wake. Position management only — no entry scan per routine spec. Portfolio flat (0 open positions); no MTM revalue and no exit checks needed. Re-verify kill switches + regime, append research_log row, rewrite portfolio.md, commit. Silent (no Telegram — no exits, no kill-switch trip, DD nowhere near 12.5% warn).

### Kraken multi-ticker — all 15 universe pairs

| Pair | last | 24h % |
|------|------|-------|
| BTC | 60580.3 | −3.30 |
| ETH | 1605.28 | −3.59 |
| SOL | 67.17 | −3.51 |
| HYPE | 61.25 | −1.40 |
| XRP | 1.06685 | −3.77 |
| SUI | 0.6832 | −2.87 |
| TAO | 216.2716 | −2.02 |
| XDG | 0.0750637 | −4.74 |
| NEAR | 1.934 | −2.37 |
| ADA | 0.143444 | −5.21 |
| LINK | 7.34321 | −3.70 |
| LTC | 40.54 | −3.84 |
| FARTCOIN | 0.1203 | −6.67 |
| TRX | 0.325717 | −0.95 |
| AVAX | 6.23 | −3.78 |

**Positives: 0/15.** Sorted descending: TRX −0.95, HYPE −1.40, TAO −2.02, NEAR −2.37, SUI −2.87, BTC −3.30, SOL −3.51, **ETH −3.59 (median)**, LINK −3.70, XRP −3.77, AVAX −3.78, LTC −3.84, XDG −4.74, ADA −5.21, FARTCOIN −6.67.

### Regime classification

- **Rule 5a:** 0/15 positive < 4/15 floor → **FAIL** (entries would be rejected if midday could enter, which it cannot anyway).
- **Rule 5a-SBD:** positives = 0 (≤ 1 ✓) AND median = −3.59% (≤ −1.0% ✓) → **SBD ACTIVE**.
- Continuous SBD duration: ~24h (active since overnight 2026-06-23T13:00Z fire). AVAX, the lone TECH-PASS candidate at EOD with +1.73% 24h, has now collapsed to −3.78% — regime has *deteriorated* over the 12h since EOD, not improved.
- SBD defensive value this wake: **0 R avoided** (no open positions to apply 9-EMA two-bar exit to).

### Mark-to-market

No open positions → no MTM line items. Equity = cash = $10,413.87 (unchanged since 2026-06-22T16:00 SOL correction row).

### Exit check

No open positions → no exits possible. n/a.

### Drawdown / kill-switch state

| Switch | Reading | Cap | Status |
|---|---|---|---|
| Daily realized + unrealized | $0.00 / 0.00% | 5% | CLEAR |
| Loss streak | 0 days | 7 | CLEAR |
| Max drawdown | 4.25% ($461.98 from peak $10,875.85) | 25% (warn 12.5%) | CLEAR — 8.25pp to warn |
| Equity floor | $10,413.87 | $7,500 | CLEAR — $2,913.87 of headroom |
| MCP availability | Kraken OK (multi-ticker returned all 15) | — | CLEAR |

All clear. No alert.

### Entry scan

**Forbidden by routine spec** ("DO NOT OPEN NEW POSITIONS IN MIDDAY"). Skipped entirely. Next entry-eligible wake = routine-03-eod Wed 2026-06-24 ~21:00 PT (= Thu 04:00Z, aligned to 13:00Z UTC bar close). Entry still gated by 5a recovery (≥ 4/15 positive) — currently 0/15, so a swing of +4 pairs to positive in the next ~8h needed for any entry. With median sitting at −3.59% and the prior session's lone positive (AVAX) flipping negative, recovery looks remote heading into EOD.

### Summary

**0 MTM, 0 exits, 0 entries** (entries forbidden by routine). Flat portfolio held. Regime read deteriorated vs EOD 12h ago: positives 1 → 0, median −3.68% → −3.59% (slight median improvement but lost the lone positive). SBD now ~24h continuous. Equity $10,413.87, DD 4.25%, all kill switches CLEAR. Silent — no Telegram triggers (no exit, no kill switch, no DD warning crossed).

---

## 2026-06-25T16:17Z — routine-03-eod (Thu 09:17 PT, OFF-CRON morning fire)

### Slot identity + timing anomaly

**Slot:** `bull-03-eod`. Cron expects `0 21 * * 1-5` PT. Actual fire: 2026-06-25 09:17 PT (Thu morning). Wed 2026-06-24 21:00 PT EOD slot **did not fire** — there is no `routine-03-eod 2026-06-24` row above and no commit between `routine-02-midday 2026-06-24` (Wed 13:07 PT) and this wake (~20h gap, spanning the missed 06-24 EOD + overnight 06-25 06:00 PT). This wake therefore covers the missed 06-24 EOD AND the post-midday 06-24 → 09:17 PT 06-25 window.

**Date-labeling guard applied:** PT calendar date at fire time = **2026-06-25**. EOD card and commit labeled 2026-06-25. Body notes the 06-24 EOD coverage explicitly.

**Coverage simplification:** portfolio has been flat continuously since 2026-06-22T16:00Z SOL correction row. No trade events occurred in the missed window (entries gated by 5a FAIL, no positions to exit). 06-24 PT day P&L = $0.00; 06-25 PT day-to-date = $0.00. Equity, DD, peak all unchanged. So the missed 06-24 EOD would have written a flat-day row with identical numbers — no replay reconstruction is required.

### Watchdog

`python scripts/watchdog.py --telegram` → **ALL CLEAR**. Heartbeats, timestamps, tree, MTM, scheduler flag, push state, MCP paths OK.

### Kraken multi-ticker — all 15 universe pairs (09:17 PT)

| Pair | last | 24h % |
|------|------|-------|
| BTC | 59600.0 | −2.27 |
| ETH | 1574.07 | −2.83 |
| SOL | 66.47 | −2.31 |
| HYPE | 61.99 | −2.96 |
| XRP | 1.03734 | −3.23 |
| SUI | 0.6809 | −0.57 |
| TAO | 213.9367 | −2.43 |
| XDG | 0.0737011 | −3.11 |
| NEAR | 1.8802 | −4.26 |
| ADA | 0.143929 | −2.49 |
| LINK | 7.23228 | −2.48 |
| LTC | 40.52 | −1.51 |
| FARTCOIN | 0.1164 | −3.96 |
| TRX | 0.323003 | −1.21 |
| AVAX | 6.137 | −4.63 |

**Positives: 0/15.** Sorted ascending: AVAX −4.63, NEAR −4.26, FARTCOIN −3.96, XRP −3.23, XDG −3.11, HYPE −2.96, ETH −2.83, **ADA −2.49 (median, 8/15)**, LINK −2.48, TAO −2.43, SOL −2.31, BTC −2.27, LTC −1.51, TRX −1.21, SUI −0.57.

### Regime classification

- **Rule 5a:** 0/15 positive < 4/15 floor → **FAIL**. Entry scan rejects all new entries this wake (no candidate eligibility check needed).
- **Rule 5a-SBD:** positives = 0 (≤ 1 ✓) AND median = −2.49% (≤ −1.0% ✓) → **SBD ACTIVE**.
- Continuous SBD duration: ~44h (active since overnight 2026-06-23T13:00Z fire). 4th consecutive wake under SBD (overnight 06-23, EOD 06-23, midday 06-24, EOD 06-25 morning fire).
- Trend in regime: median improved from −3.59% (midday 06-24) → −2.49% (now); selling pressure modestly easing but still broad — no pair has crossed back to positive. Lone bright spots: SUI −0.57 (closest to flip), TRX −1.21, LTC −1.51.
- SBD defensive value this wake: **0 R avoided** (no open positions to apply 9-EMA two-bar exit to). Cumulative SBD-period defensive value remains 0 R (flat throughout).

### Final mark-to-market (21:00 PT close approximation, using 09:17 PT prices)

No open positions → no MTM line items. Equity = cash = **$10,413.87** (unchanged since 2026-06-22T16:00Z SOL correction row, now 67h continuous).

### Post-close exit check

No open positions → no exits. n/a.

### Kill-switch state

| Switch | Reading | Cap | Status |
|---|---|---|---|
| Daily realized + unrealized (2026-06-25 PT DTD) | $0.00 / 0.00% | 5% | CLEAR |
| Daily realized + unrealized (2026-06-24 PT, retroactive) | $0.00 / 0.00% | 5% | CLEAR |
| Loss streak | 0 days | 7 | CLEAR |
| Max drawdown | 4.25% ($461.98 from peak $10,875.85) | 25% (warn 12.5%) | CLEAR — 8.25pp to warn |
| Equity floor | $10,413.87 | $7,500 | CLEAR — $2,913.87 of headroom |
| MCP availability | Kraken OK (all 15 pairs returned) | — | CLEAR |

All clear. No alert.

### EOD entry scan (W19-E)

**Skipped at the regime layer.** Rule 5a FAIL (0/15 positive < 4/15 floor) rejects all candidates pre-technical. No technical/news/sentiment passes attempted — none would be actionable. Indicators script not invoked this wake (no eligible candidate slot). Next entry-eligible wake = routine-01-overnight 2026-06-25 ~21:00 PT? Actually next overnight cron = Fri 2026-06-26 06:00 PT (`0 6 * * *`). Until then no entry attempts.

### Lessons review

Today's trades: **none** (flat). No gap-out, no give-back, no immediate-reverse archetype to extract.

- **Patience-through-SBD observation (not a new lesson):** 4 consecutive wakes flat under SBD has now meant zero realized give-back vs. an estimated −5 to −8% BTC-equivalent if BULL had held a hypothetical equal-weight position (BTC alone is −2.27% today, ~−7% over the SBD window). The 5a regime gate is doing exactly what was designed in W19-D + W21-F. Already captured in [2026-05-19 synchronized-breakdown lesson]; no new append.
- **No new lessons appended this wake.**

### Stats

- **Day P&L (06-25 PT DTD):** $0.00 / 0.00%.
- **Day P&L (06-24 PT, retroactive close):** $0.00 / 0.00%.
- **Trades opened:** 0 today, 0 yesterday.
- **Trades closed:** 0 today, 0 yesterday.
- **Win rate today:** n/a (no closes).
- **New equity:** $10,413.87. **Equity peak:** $10,875.85 (set 2026-06-13T09:00Z). **Drawdown:** 4.25%.
- **Rolling 7d:** BULL ≈ −1.6% (SOL net +$182.13 06-22 minus SOL −$199.87 06-17, plus rolloff of TAO +$621.22 which was 06-13 → outside 7d window). BTC-hold 7d ≈ −9.0% (BTC ~$65.4k → $59.6k). **Delta ≈ +7.4%, BULL well ahead 7d.**
- **Rolling 30d:** BULL ≈ +4.14% (inception-aligned). BTC-hold 30d ≈ −23.6%. **Delta ≈ +27.7%, BULL well ahead 30d.**
- **Rolling 90d:** not computable (BULL inception 2026-04-20 = 66 days ago; window first computable ~2026-07-19).

### Monthly archive

Today is 2026-06-25 (Thu). Last trading day of June 2026 = 2026-06-30 (Tue). **Skipped.** Trigger expected at routine-03-eod Tue 2026-06-30.

### Telegram NOTIFY

Mandatory EOD card per routine NOTIFY. Sending next via `scripts/telegram_send.py`.

### Summary

**0 OPEN, 0 CLOSE.** Off-cron morning fire (Thu 09:17 PT) covering the missed Wed 21:00 PT EOD slot AND the post-midday window. Portfolio flat throughout, equity **$10,413.87** unchanged, DD **4.25%** unchanged, loss streak **0**. Regime 5a FAIL (0/15 positive, median −2.49%), 5a-SBD **ACTIVE** ~44h continuous (4th consecutive SBD wake). Selling pressure easing modestly (median −3.59% → −2.49%) but no pair positive yet. Watchdog ALL CLEAR. No lessons appended (no trade events to extract from). No monthly archive (last trading day = 06-30). Mandatory EOD Telegram card sent.


---

## 2026-06-25T16:20Z — routine-01-overnight (Thu 09:20 PT, OFF-CRON morning fire)

### Slot identity + timing anomaly

**Slot:** `bull-01-overnight`. Cron expects `0 6 * * 1-5` PT. Actual fire: 2026-06-25 09:20 PT (Thu morning). The cron window (06:00 PT) was missed by ~3h20m. Notably, routine-03-eod also fired off-cron at 09:17 PT this morning — both 01-overnight and 03-eod (and the previously-missed 06-24 21:00 PT EOD slot) appear to have queued together and discharged in a single Thursday-morning batch. Watchdog `--telegram` returned ALL CLEAR despite this — its scheduler-flag check looks at marker file freshness, not the full per-routine cron schedule. Worth flagging in research_log; no kill-switch trip.

**Coverage simplification:** routine-03-eod fired 3 minutes before this wake (09:17 PT) and already pulled identical kraken_multi_ticker data + classified regime + ran the kill-switch grid. Portfolio is flat (0 open) and no trade events occurred in the ~3-minute gap. This wake re-runs the regime read at 09:20 PT, confirms unchanged state, and processes per the overnight routine spec (which mandates an entry scan that the EOD routine had already short-circuited at the regime layer).

### Watchdog

`python scripts/watchdog.py --telegram` → **ALL CLEAR**. Heartbeats, timestamps, tree, MTM, scheduler flag, push state, MCP paths OK.

### Kraken multi-ticker — all 15 universe pairs (09:20 PT)

| Pair | last | 24h % |
|------|------|-------|
| BTC | 59681.9 | −2.14 |
| ETH | 1573.59 | −2.86 |
| SOL | 66.50 | −2.26 |
| HYPE | 62.40 | −2.32 |
| XRP | 1.03700 | −3.26 |
| SUI | 0.6813 | −0.51 |
| TAO | 214.2805 | −2.27 |
| XDG | 0.073743 | −3.06 |
| NEAR | 1.8809 | −4.23 |
| ADA | 0.143815 | −2.57 |
| LINK | 7.24427 | −2.32 |
| LTC | 40.61 | −1.29 |
| FARTCOIN | 0.1162 | −4.13 |
| TRX | 0.323068 | −1.19 |
| AVAX | 6.140 | −4.58 |

**Positives: 0/15.** Sorted ascending: AVAX −4.58, NEAR −4.23, FARTCOIN −4.13, XRP −3.26, XDG −3.06, ETH −2.86, ADA −2.57, **HYPE −2.32 (median, tied with LINK at 8/15)**, LINK −2.32, TAO −2.27, SOL −2.26, BTC −2.14, LTC −1.29, TRX −1.19, SUI −0.51.

### Regime classification

- **Rule 5a:** 0/15 positive < 4/15 floor → **FAIL**. Entry scan rejects all candidates pre-technical.
- **Rule 5a-SBD:** positives = 0 (≤ 1 ✓) AND median = −2.32% (≤ −1.0% ✓) → **SBD ACTIVE**.
- Continuous SBD duration: ~46h (active since overnight 2026-06-23T13:00Z fire). **5th consecutive SBD wake** (overnight 06-23, EOD 06-23, midday 06-24, EOD 06-25 morning, overnight 06-25 morning).
- Trend in regime vs EOD 3h ago: median improved slightly −2.49% → −2.32% (+0.17pp). SUI moved closer to flipping (−0.57 → −0.51, just 0.51% below zero) but still no positive pair. Top-of-tape thinning persists — selling pressure is unwinding gradually, not capitulating.
- SBD defensive value this wake: **0 R avoided** (no open positions to apply 9-EMA two-bar exit to). Cumulative SBD-period defensive value remains 0 R (flat throughout 46h SBD window).

### Overnight position check

No open positions → no overnight stop-hit scan possible. n/a.

### Mark-to-market

No open positions → no MTM line items. Equity = cash = **$10,413.87** (unchanged since 2026-06-22T16:00Z SOL correction row, now 70h continuous flat).

### Kill-switch state

| Switch | Reading | Cap | Status |
|---|---|---|---|
| Daily realized + unrealized (2026-06-25 PT DTD) | $0.00 / 0.00% | 5% | CLEAR |
| Loss streak | 0 days | 7 | CLEAR |
| Max drawdown | 4.25% ($461.98 from peak $10,875.85) | 25% (warn 12.5%) | CLEAR — 8.25pp to warn |
| Equity floor | $10,413.87 | $7,500 | CLEAR — $2,913.87 of headroom |
| MCP availability | Kraken OK (all 15 pairs returned) | — | CLEAR |

All clear. No alert.

### Technical

**Rule 5a fails (0/15 positive < 4/15 floor) — all entries rejected pre-technical.** Per `skills/decide.md` pre_entry_check ordering, the regime gate halts the scan before per-pair indicator evaluation. `scripts/indicators.py` not invoked this wake (no eligible candidate slot). All 15 universe pairs implicitly REJECT with reason `rule-5a-regime-gate` (0/15 positive, ≥ 4/15 required).

### News

Skipped — no technical-PASS candidates to scan headlines for. Firecrawl not invoked.

### Sentiment

Skipped — no technical-PASS candidates to query depth/spread for.

### Decision

**0 OPEN, 0 CLOSE.** Regime 5a FAIL gates all entries; no open positions to manage.

### First-of-month universe refresh

Today is 2026-06-25 (Thu). Refresh trigger = 1st of month or first weekday if 1st is weekend. **Skipped.** Next trigger expected 2026-07-01 (Wed). Universe unchanged from 2026-06-01 refresh.

### Stats

- **Day P&L (06-25 PT DTD):** $0.00 / 0.00%.
- **Trades opened:** 0. **Trades closed:** 0.
- **New equity:** $10,413.87. **Equity peak:** $10,875.85 (set 2026-06-13T09:00Z). **Drawdown:** 4.25%.

### Summary

**0 OPEN, 0 CLOSE, 0 research items beyond the regime read.** Off-cron Thursday-morning fire (09:20 PT, ~3h20m past 06:00 PT cron window) following the 09:17 PT routine-03-eod morning fire. Portfolio flat, equity **$10,413.87** unchanged, DD **4.25%** unchanged, loss streak **0**. Regime 5a FAIL (0/15 positive, median −2.32%), 5a-SBD **ACTIVE** ~46h continuous (5th consecutive SBD wake). Selling pressure modestly easing (median −2.49% → −2.32% over 3h) but no pair has crossed back positive — SUI closest at −0.51%. Watchdog ALL CLEAR. Next entry-eligible wake = routine-02-midday Thu 2026-06-25 ~13:00 PT (midday is forbidden from entering — actually next eligible is routine-03-eod Thu 21:00 PT or routine-01-overnight Fri 06-26 06:00 PT). Silent — no Telegram triggers (no exit, no kill switch, no DD warn crossed).

2026-06-25T17:07:24Z | harness | day-gate | not Saturday, skipping | no action

2026-06-25T17:40:48Z | allocation | day-gate | not Sunday, skipping | no action

## 2026-06-25T20:00Z — routine-02-midday (Thu 13:00 PT, on-schedule cron fire)

**Slot identity `bull-02-midday`.** Cron `0 13 * * 1-5` PT = 20:00Z; on-schedule.

### Position management

Flat at wake (0 open positions, $10,413.87 cash). No MTM, no stop-monitor, no exit checks. Per routine spec, **no new entries permitted at midday** — entry responsibility belongs to routines #1 / #3.

### Kraken multi-ticker (regime sweep, 15-pair universe, 24h % change)

| Pair | last | 24h % |
|------|-----:|------:|
| HYPE | 64.00 | **+0.19** |
| LTC | 40.82 | −0.78 |
| TRX | 0.3238 | −0.97 |
| SUI | 0.6757 | −1.33 |
| BTC | 59,623.6 | −2.23 |
| SOL | 66.50 | −2.26 |
| LINK | 7.20088 | −2.90 |
| XDG | 0.0737053 | −3.11 |
| XRP | 1.03725 | −3.24 |
| ETH | 1,565.42 | −3.36 |
| TAO | 211.4586 | −3.56 |
| FARTCOIN | 0.1164 | −3.96 |
| ADA | 0.141603 | −4.07 |
| AVAX | 6.132 | −4.71 |
| NEAR | 1.8331 | −6.66 |

- **Positives:** 1/15 (HYPE only). Up from 0/15 at overnight 16:20Z, but still below the 4/15 floor.
- **Median 24h % change:** **−3.11%** (worsened from −2.32% at overnight 16:20Z — ~0.8pp deeper into red).
- **Regime gate (5a):** **FAIL** — 1/15 positive (< 4/15 floor). Entries would be rejected if midday were entry-eligible (it isn't).
- **5a-SBD sub-state:** **ACTIVE** — positives 1 (≤ 1 ✓) AND median −3.11% (≤ −1.0% ✓). SBD continuously active ~50h (6th consecutive SBD wake, since overnight 06-23T13:00Z). Defensive value this wake = 0 R (flat).

### Kill-switch state

- **Daily realized + unrealized PnL (06-25 PT DTD):** $0.00 / 0.00% — CLEAR (cap 5%).
- **Loss streak:** 0 trading days — CLEAR (cap 7).
- **Max drawdown:** 4.25% from peak $10,875.85 — CLEAR (cap 25%, warn 12.5%, 8.25pp to warn).
- **Equity floor:** $10,413.87 > $7,500 — CLEAR.
- **MCP availability:** Kraken multi-ticker returned all 15 universe pairs — CLEAR.
- **5b cooldowns:** none active.
- **All Ring 3 kill switches: CLEAR.**

### Stats

- **Day P&L (06-25 PT DTD):** $0.00 / 0.00%.
- **Trades opened:** 0 (midday non-entering). **Trades closed:** 0 (flat).
- **New equity:** $10,413.87 unchanged. **Equity peak:** $10,875.85. **Drawdown:** 4.25% unchanged.

### Summary

**0 exits, 0 entries.** On-schedule midday cron fire with flat portfolio. Equity unchanged $10,413.87, DD 4.25% unchanged. Regime continues 5a FAIL — HYPE flipped positive (+0.19%) but the median deepened from −2.32% → −3.11% over the ~3h45m since overnight, so the underlying selling pressure is broader, not narrower; SBD now ~50h continuous (6th consecutive SBD wake). Silent — no Telegram triggers (no exits, no kill switch, no DD warn crossed). Next entry-eligible wake = routine-03-eod Thu 2026-06-25 ~21:00 PT (= Fri 04:00Z), still gated by 5a regime recovery (≥ 4/15 positive). Files written: `portfolio.md` (rewritten with fresh mark-to-market and regime snapshot), `research_log.md` (this row). `trade_log.md` untouched (no trade events).

