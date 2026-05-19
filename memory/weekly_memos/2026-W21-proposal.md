# BULL Strategy Proposal — 2026-W21

> **STATUS: APPROVED & APPLIED 2026-05-19** — User approved via interactive chat: scope "Live v0.2 + spin variant". Applied: (1) `memory/strategy.md` → v0.3 (added rule 5a-SBD + Exit rule 1-SBD); (2) spun `variants/v0.12-sbd-exit/` as the instrumented paper-paper twin (rack now 10/10). Lesson recorded in `lessons.md` 2026-05-19; decision appended to `research_log.md`. Chat-channel approval has equivalent authority per W18/W19 precedent.
>
> **Original draft status (preserved for audit):** Drafted 2026-05-19 (Tue) at user request during an interactive session (fragility-audit follow-up). Off-cycle: normal channel is routine #4 Saturday (next: 2026-05-23).
>
> **Type:** Ring 2 — modifies `memory/strategy.md` (entry rule 5a + a conditional exit-rule change). Does **not** touch `guardrails.md`, risk caps, universe, or instruments. Spot-only, long-only mandate fully preserved (no shorting, no leverage — see §Mandate compliance).
> **Origin:** Fragility audit 2026-05-19 of the BULL-vs-Codex contest stable. Finding: the single edge that paid in the contest window was being positioned for the 2026-05-12→05-17 synchronized crypto breakdown. BULL's mandate structurally forbids monetizing it (long-only, no shorts), but BULL *can* mandate-compliantly capture the **defensive half**: stop bleeding open longs faster when the same breakdown signature appears.
> **Backtest evidence:** NOT included (requires routine #4 TradingView harness). Evidence base is one BULL trade + cross-strategy corroboration + structural reasoning. Stated honestly in §Honest caveats. A variant-validation path is offered as the low-risk alternative to direct adoption.

## Headline summary

Upgrade rule **5a** from a *passive long-block* ("don't add new longs in weak tape") into a **regime classifier with an active, mandate-compliant defensive response** on open positions when a *synchronized breakdown* is detected.

| # | Title | Addresses | Confidence | Ring |
|---|---|---|---|---|
| F | Synchronized-breakdown classifier + defensive exit-tightening | Contest fragility audit 2026-05-19; XRP 2026-05-14 give-back | medium-low (1 BULL trade + cross-strategy + structural) | 2 |

**The asymmetry this addresses:** during 2026-05-12→05-17, Codex Aggro/Apex made ~all their contest P&L *short* the synchronized breakdown. BULL's existing 5a correctly kept it from opening longs into it — but 5a does nothing for positions already open. BULL gives back unrealized R round-tripping through the dump (XRP pattern, see Evidence). 5a today is "don't add"; this makes it also "protect the book."

---

## Proposal F — Synchronized-breakdown classifier + defensive exit-tightening

### Current rules (`strategy.md`)

§ Entries, rule 5a:
```
5a. Regime-confirmation gate: at entry-scan time, count universe pairs
    with positive 24h % change. If < 4 of 15 are positive, reject all
    new entries this wake.
```
§ Exits, rule 1:
```
1. 1H close < 1H 20-EMA
```

### Proposed change

Add a stricter sub-state to 5a and one **conditional** modification to Exit rule 1:

```
5a. Regime-confirmation gate (unchanged): at entry-scan time, count
    universe pairs with positive 24h % change. If < 4 of 15 are
    positive, reject all new entries this wake.

5a-SBD. Synchronized-breakdown sub-state: at entry-scan time, classify
    regime = SYNCHRONIZED_BREAKDOWN when BOTH:
      (i)  <= 1 of 15 universe pairs positive on 24h % change, AND
      (ii) median 24h % change across the 15 universe pairs <= -1.0%.
    SBD is a strict subset of a 5a failure (reject-all-entries still
    applies, unchanged). SBD additionally triggers the defensive
    exit per Exit rule 1-SBD. SBD is re-evaluated every wake; it
    clears automatically when (i) or (ii) is no longer true.

Exits, rule 1:
1.   Default: 1H close < 1H 20-EMA.
1-SBD. While regime = SYNCHRONIZED_BREAKDOWN, the trend exit tightens
       to: 1H close < 1H 9-EMA. Faster exit reduces give-back of
       unrealized R through a multi-day synchronized decline. Reverts
       to the 20-EMA exit automatically when SBD clears. The 2xATR
       static stop (Exit rule 2) and 4R take-profit (rule 3) are
       UNCHANGED.
```

Plus a logging obligation: every wake SBD is active, `research_log.md` records the classification and an estimated avoided-give-back (open-position unrealized R at the 9-EMA exit vs. modeled 20-EMA exit). This is the telemetry that finally **credits the regime gate's defensive value** in weekly memos (currently uncredited).

### Mandate compliance (explicit)

- **No shorting.** SBD does not open shorts or any inverse position. BULL stays long-only; the only action is exiting existing longs sooner.
- **No leverage / margin / perps / options.** Unchanged. Spot only.
- **Strictly risk-reducing in a downtrend.** A tighter exit can only flatten earlier, never increase exposure or size.
- Does not touch `guardrails.md`, the 8/4%/1.5% caps, universe, or kill switches.

### Evidence

- **BULL trade-log (sample size 1):** XRP opened 2026-05-14T16:00Z (5a passed at entry). Per `portfolio.md` reconstruction it ran **~+2.8R then round-tripped**, exiting on the 20-EMA cross 2026-05-15T04:00Z at **−0.14R / −$21.92**. The 05-15T13:00Z bar was a synchronized crash bar (0/15 positive). Under 5a-SBD the 9-EMA exit would have fired earlier in the roll-over, preserving part of the +2.8R excursion instead of surrendering it. Directionally supportive; not a clean backtest.
- **Cross-strategy corroboration (informative, not BULL's own):** Codex Aggro/Apex opened the 05-12 short basket and held to 05-17; the SBD state was real, broad (BTC ≈ −6%, ~$1B ETF outflows, 0–1/15 positive for days) and **persisted ~5 days**. This matters: SBD is a *durable multi-day* state, not single-bar noise, so a tightened-exit response has time to pay and is unlikely to be pure whipsaw.
- **Structural:** the fragility audit showed every contest "winner" was this one regime. BULL cannot take the offensive side by mandate; the defensive side is the only mandate-legal way to learn from it.

### Risk assessment

- **Downside if adopted:** in a sharp 1–2 bar flush that V-reverses, the 9-EMA exit flattens a long that would have recovered under the 20-EMA exit. Real cost in violent-reversal tape. Mitigation: SBD requires *both* breadth (≤1/15) *and* depth (median ≤ −1%), which historically maps to genuine multi-day risk-off, not shallow wicks. Still, expect occasional give-up-the-bounce events.
- **Downside if NOT adopted:** BULL keeps round-tripping open longs through synchronized dumps (the XRP give-back pattern repeats), and the regime gate's defensive value stays uncredited/unmeasured.
- **Upside:** converts 5a into an active book-protector in exactly the regime that did the most damage *and* generated the most opportunity in the contest. Mandate-legal capture of the defensive half of the breakdown edge.

### Expected impact

- Fewer "ran +R then stopped flat/negative" outcomes in synchronized risk-off (the XRP failure mode).
- Slightly lower average winner size in choppy-but-not-SBD tape: none (SBD is a strict subset; non-SBD behavior is byte-for-byte unchanged).
- Frequency of SBD firing: low. Over the available window it would have been active only around the 05-15 and 05-12→05-17 clusters.

### Calibration notes

- `≤1/15 positive` and `median ≤ −1.0%` chosen so SBD is a *strict, rare* subset of an ordinary 5a fail (which is already ≤3/15). Looser thresholds would conflate normal weak tape with a genuine synchronized break.
- 9-EMA as the SBD exit (vs. default 20-EMA): conventional fast/slow pair already used elsewhere in the stack; not backtested-optimal, a reasoned default. Routine #4's harness could tune 9 vs. 12.

---

## Recommended path (risk mitigation)

Given the honest evidence weakness (1 BULL trade), the **recommended** application is **not** a direct live-v0.2 amend but a **variant-validation first**:

- **Option A (recommended): spin `v0.12-sbd-exit`** — a paper-paper variant identical to v0.2 plus 5a-SBD / Exit 1-SBD. Validate 30 days on the rack against live v0.2 (the rack has 1 open slot). Promote via the normal Ring-2 path only if it demonstrably reduces give-back without material whipsaw cost. Lowest risk, slowest.
- **Option B: direct adopt into v0.2 now.** Justified because the change is *strictly risk-reducing in a downtrend* (it can only exit earlier, never add risk), and the failure mode (missing a V-reversal bounce) is bounded and rare. Faster, accepts thin evidence.

---

## What this proposal does NOT change

- All risk caps, position caps, stop distance, 2xATR static stop, 4R take-profit, sizing.
- Non-SBD entry and exit behavior (identical to current v0.2).
- Concept buckets (`momentum: 100%`), universe, routine schedule.
- Any guardrail. No shorting, leverage, margin, perps, options.

## Honest caveats

- **Sample size 1 on BULL's own logs.** The strongest support is cross-strategy + structural, not a BULL backtest. This is exactly the caveat that motivates Option A.
- **No backtest.** Thresholds (≤1/15, median ≤ −1%, 9-EMA) are reasoned, not optimized. Routine #4 harness would tighten them.
- **It does not recover the offensive edge.** BULL still cannot short; this captures only the defensive half. The "+$767 Aggro" type outcome remains structurally off-limits and that is correct per mandate — do not read this proposal as closing that gap.
- **Whipsaw is a real cost**, not a hypothetical, in sharp-reversal tape. SBD's dual breadth+depth gate reduces but does not eliminate it.

## Decision

User reply (Telegram or chat-channel equivalent):
- `[Y A]` — spin `v0.12-sbd-exit` variant for 30-day paper validation (recommended)
- `[Y B]` — adopt 5a-SBD + Exit 1-SBD directly into live v0.2 now
- `[N]` — reject; fragility-audit lesson recorded in `lessons.md` only
- (no reply within 24h) — auto-rejected per mandate

---

*Drafted 2026-05-19 at user request. Source evidence: fragility audit of contest trade logs (this session); BULL `portfolio.md`/`trade_log.md` XRP 2026-05-14 reconstruction; cross-strategy read-only observation of Codex Aggro/Apex logs (read access per `project_competition.md` grant). No `strategy.md` or `guardrails.md` edits made — this is a proposal only.*
