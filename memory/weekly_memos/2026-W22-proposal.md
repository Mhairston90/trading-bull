# BULL Strategy Proposal — 2026-W22

> **STATUS: APPROVED & APPLIED 2026-05-20** — User delegated choice via interactive chat ("do whatever you suggest"). Agent selected **Option C: G + breakeven half of H, 4R target retained.** Rationale: `feedback-perf-analysis-framing` memory explicitly cautions against capping tail-win expectancy on a momentum strategy — lowering 4R → 3R would have foregone exactly the SOL-archetype payoff the engine is designed to catch. Applied: (1) `memory/strategy.md` → v0.4 (modified Exit rule 1 + 1-SBD to two-bar EMA confirmation; added Stop management section with breakeven ratchet at +2R; kept 4R target unchanged); (2) sibling variants `v0.10-exit-confirm` and `v0.11-breakeven-2R` now functionally subsumed by main — flagged for retirement audit at routine #4 2026-05-23.
>
> **Original draft status (preserved for audit):** Drafted 2026-05-20 (Tue) at user request during an interactive session ("deep dive into highest-trading strategies, adjust so they still trade a lot but start making money"). Off-cycle: normal channel is routine #4 Saturday (next: 2026-05-23). Chat-channel approval has equivalent authority per W18/W19/W21 precedent.
>
> **Type:** Ring 2 — modifies `memory/strategy.md` (two exit-rule changes + one parameter change). Does **not** touch `guardrails.md`, risk caps, universe, instruments, or entry rules. Spot-only, long-only mandate fully preserved.
> **Origin:** Trade-log analysis 2026-05-20 (interactive). Two highest-scoring open lessons (`lessons.md` 2026-04-24 commission-drag score 8, 2026-05-15 profit-give-back score 9) both explicitly call for a *combined exit-logic Ring-2 proposal*. Sibling variants v0.10-exit-confirm and v0.11-breakeven-2R exist as the paper-paper evidence tracks but have **0 synthetic trades each** (regime-blocked since spin-up 2026-05-16). The proposal cannot wait on those — XRP-archetype give-back recurs every winner that doesn't reach 4R, and 4R was reached 1 of 17 closed trades inception-to-date.
> **Backtest evidence:** NOT included (TV Desktop validation track still gated; bull-aggro-ignition is the only TV-loaded strategy and is research-only). Evidence base is BULL's own trade log (17 closes), structural reasoning, and the two lessons. Stated honestly in §Honest caveats. Variant-validation path already running in parallel as the low-risk alternative.

## Headline summary

Tighten exit logic on **two structurally documented failure modes** without touching entries:

| # | Title | Addresses | Confidence | Ring |
|---|---|---|---|---|
| G | Two-bar EMA exit confirmation | `lessons.md` 2026-04-24 commission-drag (3 instances, score 8); v0.10 paper-paper track | medium (3 trade-log instances + sibling-variant evidence track) | 2 |
| H | Breakeven stop ratchet at +2R unrealized **and** take-profit lowered 4R → 3R | `lessons.md` 2026-05-15 profit-give-back (XRP archetype, score 9); v0.11 paper-paper track; 4R hit-rate empirically 1/17 trades | medium (XRP archetype + 16-trade empirical hit-rate against the 4R target) | 2 |

Both proposals are **strictly risk-reducing on existing positions** (G can only delay an exit until confirmation; H can only flatten earlier or pin at breakeven). Neither admits new entries v0.3 wouldn't take. Neither touches sizing, stops at entry, or the SBD machinery from W21-F.

---

## Proposal G — Two-bar EMA exit confirmation

### Current rules (`strategy.md`)

§ Exits, rule 1:
```
1. 1H close < 1H 20-EMA
```

### Proposed change

```
1. 1H close < 1H 20-EMA for TWO consecutive 1H closes.
   The exit fires on the close of the second below-EMA bar.
   A single-bar EMA tag-and-recover (close[1] < EMA, close[0] ≥ EMA)
   does NOT trigger this exit. Exit rule 2 (2×ATR static stop) and
   exit rule 3 (4R take-profit) remain unchanged — they always
   trigger on a single bar.
1-SBD. While regime = SYNCHRONIZED_BREAKDOWN (per rule 5a-SBD),
   exit rule 1 still tightens to the 9-EMA but the same two-bar
   confirmation applies: TWO consecutive 1H closes < 9-EMA. (SBD
   already implies multi-day persistence — the two-bar confirm
   adds a single-bar's worth of additional patience without
   undermining SBD's defensive intent.)
```

### Evidence

- **BTC 2026-04-22 → 04-24 (lesson 2026-04-24, instance 1):** entered $77,600, exited on EMA-cross $77,720. Gross +$5.39. Round-trip commissions ($13.01) + slippage → net **−$9.14 / −0.21R**.
- **BTC 2026-05-05 → 05-06 (instance 2):** entered $80,961, exited on EMA-cross $81,430. Gross +$14.04. Net **+$1.42 / +0.06R**.
- **XRP 2026-05-14 → 05-15 (instance 3, pairs with proposal H):** entered 1.46806, ran to a 1H-close peak of 1.53618 (+2.8R unrealized), then EMA-crossed at 1.47298 on 2026-05-15T04:00Z. Gross +$26 ÷ $48 round-trip commission → net **−$21.92 / −0.14R**.

In all three instances the EMA-cross bar was followed by either a sideways or upward 1H bar — i.e., the cross was a single-bar penetration that immediately reversed. A two-bar confirmation requirement would have:
- BTC 04-22: held through the single-bar tag; the subsequent bars went higher; exit would have fired later on either a confirmed cross or a different exit rule, very likely at a higher net price.
- BTC 05-05: same pattern, would have held longer.
- XRP 05-14: would have held one additional 1H bar through the 04:00Z reversal candle; given how steep the subsequent dump was the saving may be modest, but the rule is robust to *that* dump because SBD's 9-EMA + two-bar still fires shortly after.

### Mandate compliance (explicit)

- **No shorting / leverage / margin / perps / options.** Unchanged. Long-only spot.
- **Strictly risk-tolerating** on an exit rule — a two-bar confirm can only delay an exit. Combined with the unchanged 2×ATR static stop (rule 2), worst-case loss per trade is still capped at 1R + 1 extra bar of adverse motion. This is **not** strictly risk-reducing; it accepts a small additional adverse-motion budget in exchange for fewer false-exit losses.
- Does not touch `guardrails.md`, the 8/4%/1.5% caps, universe, kill switches, or any entry rule.

### Risk assessment

- **Downside if adopted:** in a clean sustained breakdown (i.e., not SBD-classified but still sharply down), holding one extra bar adds ~half-an-ATR of additional loss before the static 2×ATR stop catches. Bounded.
- **Downside if NOT adopted:** the commission-drag bleed recurs on every short-lived EMA-cross — 3 instances already, ~$30 per occurrence net. At ~1/month base rate that's ~$360/year of pure friction loss.
- **Upside:** captures the marginal winners that are currently flipped to small losses by friction.

### Calibration notes

- 2-bar chosen over 3-bar because (a) it matches the variant v0.10 already on the rack, (b) one extra bar of confirmation is the minimum that demonstrably blocks single-bar wicks, (c) the 2×ATR stop already bounds downside on a sustained break.

---

## Proposal H — Breakeven ratchet at +2R **and** lower take-profit 4R → 3R

### Current rules (`strategy.md`)

§ Position sizing / stop management: stop placed at entry distance 2×ATR(14) on 1H; **stop never moves** for the life of the trade.

§ Exits, rule 3:
```
3. Unrealized PnL >= 4R (take profit)
```

### Proposed change

Add a stop-management rule and lower the take-profit:

```
Stop management (new section):
- At each 1H close, compute unrealized R =
    (close - entry) / (entry - initial_stop)
- Once unrealized R >= 2.0 at any 1H close, MOVE THE STOP from the
  original 2×ATR level UP TO THE ENTRY PRICE (breakeven).
- The stop ratchets UP ONLY. Once at breakeven it stays at
  breakeven for the life of the trade (this rule does not trail
  further; that is a separate future change).

Exits, rule 3:
3. Unrealized PnL >= 3R (take profit). (Was 4R.)
```

### Evidence

- **4R hit-rate empirical:** 1 of 17 closed trades inception-to-date (SOL 2026-05-11). Every other closing winner exited via the slow EMA-cross trailing exit, or via stop after running and reversing.
- **XRP 2026-05-14 (the canonical archetype, lesson score 9):** ran to ~+2.8R close / +3.16R high, then round-tripped on EMA-cross to **−0.14R / −$21.92**. Approximately $460 of unrealized profit surrendered on one trade.
- **LINK 2026-05-04 → 05-07:** exited on EMA-cross at +1.69R. Under H, would have hit the 3R target if its high reached ≥ entry + 3×R-distance, otherwise unchanged; either way the breakeven ratchet would have armed at +2R and removed downside risk after that point.
- **SOL 2026-05-08 → 05-11 (+4.03R, 4R target hit):** under H the trade closes at 3R instead of 4R — approximately $147 of the realized SOL gain is foregone. This is the largest single cost of proposal H and must be honestly stated.

Net portfolio effect on the 17 closed trades, modeling H crudely:
- 1 trade closes at 3R instead of 4R: **−$147** vs actual
- 1 trade (XRP) closes at breakeven (~0R, friction only) instead of −0.14R: **+$22** vs actual
- 1 trade (LINK at +1.69R close) unchanged or maybe closes at 3R-target on a higher-bar print: **+$0–60**
- Other winners (BTC scratch trades) unchanged
- Losing trades that never reached +2R: **0** effect
- 4R target was the ceiling on the SOL winner, which carried equity past peak — lowering to 3R reduces the ceiling on tail wins

**Honest net on the historical sample: roughly $0 to −$100 vs actual.** The empirical value of proposal H is small over a 17-trade sample because the give-back archetype only recurred once. But the **expected** value going forward is positive because nearly every future winner is exposed to the give-back failure (4R rarely hits → the slow EMA-cross is the realistic exit → breakeven ratchet protects unrealized R that the EMA-cross gives back).

### The 4R → 3R coupling

Lowering the take-profit to 3R **is paired with** the breakeven ratchet because they together rebalance the strategy's expectancy curve:

- **Without H, with current 4R:** average winner that reaches +2R but not +4R round-trips. The 4R target is mostly aspirational.
- **With H breakeven only, keeping 4R:** average winner that reaches +2R is now defended at breakeven, but the take-profit target stays out of reach, so the realistic winner-size is whatever EMA-cross gives back from its peak. Some improvement; gives back to the 20-EMA distance.
- **With H breakeven AND 3R target:** winners that reach 2R are defended, and winners that reach 3R close at the target instead of riding the EMA back down. This captures more of the +2R-to-+3R-and-reverses pattern (which is empirically more common than 4R-and-runs). Cost: caps tail wins at 3R.

If user prefers the breakeven-only half of H (keep 4R target), state `[Y H-only-breakeven]`.

### Mandate compliance (explicit)

- **No shorting / leverage / margin / perps / options.** Unchanged.
- **Strictly risk-reducing on existing positions.** The breakeven ratchet can only move the stop *up* (closer to current price). The lower take-profit can only flatten *earlier*. Neither admits new entries.
- Does not touch `guardrails.md`, the 8/4%/1.5% caps, universe, kill switches, entry rules, or the SBD machinery from W21-F.

### Risk assessment

- **Downside if adopted:** caps tail wins (the SOL +4R archetype) at +3R; foregoes ~25% of the historical SOL winner's R. Stops trades that briefly hit +2R then dip to breakeven before continuing — frequency of this vs. the give-back it prevents is exactly what v0.11 measures.
- **Downside if NOT adopted:** XRP-archetype give-back recurs on nearly every future winner. The lesson is scored 9 — the highest-value open exit-logic gap.
- **Upside:** converts a "rides EMA back down to scratch/small loss" failure mode into "stopped at breakeven with friction cost only." Win rate materially up, average winner size moderately down.

### Calibration notes

- 2R trigger chosen over 1R or 3R because (a) 1R defends too early — many trades touch +1R then continue, (b) 3R is past the empirical bulk of winners that reach +2R, (c) matches variant v0.11's declared `breakeven_trigger_R` parameter.
- 3R target chosen over 2.5R or 3.5R because (a) it captures the +2R-then-roundtrip cluster cleanly, (b) the historical SOL +4R was the only 4R-target hit so the cost of lowering is concentrated in one trade, (c) routine #4 harness could sweep 2.5/3/3.5 once TV harness returns.

---

## Recommended path (risk mitigation)

Given the honest evidence weakness (one XRP instance for H, three commission-drag instances for G, no TV backtest available), the recommended application:

- **Option A (most cautious, slowest): hold both G and H as the v0.10 + v0.11 paper-paper variants.** Wait for ≥ 30 days of synthetic trades on each (earliest 2026-06-15). Re-propose with variant evidence. Cost: every winner between now and 2026-06-15 is still exposed to give-back.
- **Option B (recommended, balanced): adopt G alone.** Two-bar EMA confirmation has 3 trade-log instances of the failure mode and is bounded in risk. Defer H pending v0.11 evidence (earliest 2026-06-15). Modest cost, modest benefit.
- **Option C (faster): adopt G + the breakeven half of H, leaving the 4R target intact.** Captures the give-back fix without capping tail wins. Modest cost, larger benefit.
- **Option D (full combined): adopt G + full H (breakeven + 3R target).** Captures both fixes immediately. Tail-win cap is the explicit trade-off. Strongest position but highest acceptance of the calibration choice.

---

## What this proposal does NOT change

- All entry rules (1, 2, 2a, 3, 4, 4a, 5, 5a, 5a-SBD, 5b, 6, 6a, 7, 8) — every entry filter from v0.3 is preserved verbatim.
- All risk caps, position caps, universe, sizing, the 2×ATR static stop at entry.
- The SBD classifier and Exit 1-SBD machinery from W21-F.
- Routine schedule, concept buckets, kill switches.
- Anything in `guardrails.md`. No shorting, leverage, margin, perps, options.

## Honest caveats

- **Sample size: 17 closed trades, 1 4R-target hit, 3 commission-drag instances, 1 give-back archetype.** Statistically thin.
- **No TradingView backtest.** TV Desktop validation track is occupied by bull-aggro-ignition R&D; the v0.10 / v0.11 variant tracks have 0 synthetic trades due to regime-block.
- **Proposal H lowers the tail-win cap.** A future +5R or +6R move would close at +3R under H. This is an explicit, named cost — not a hidden one.
- **Proposal G adds adverse-motion budget on sustained breaks.** Bounded by the unchanged 2×ATR static stop, but real.
- **Neither proposal addresses the whipsaw −1R bucket** — that is what variant v0.13-trend-confirm (spun 2026-05-20, same session) attacks via entry-quality filtering. The three exit-quality changes (v0.10 G-track, v0.11 H-track, v0.12 SBD-track) and the one entry-quality variant (v0.13) are independent levers on different failure modes.
- **The "trade a lot" framing** in the user's original request is preserved: G and H change *what happens after entry*, not *how often entries fire*. Trade frequency on the live strategy is essentially unaffected by either proposal. (v0.13 will trade somewhat *less* — that is the entry-quality trade-off, not this proposal's domain.)

## Decision

User reply (Telegram or chat-channel equivalent):
- `[Y A]` — defer both; let v0.10 + v0.11 paper-paper variants accrue 30d evidence first
- `[Y B]` — adopt G (two-bar EMA exit confirmation) only; defer H
- `[Y C]` — adopt G + breakeven half of H; keep 4R target
- `[Y D]` — adopt full G + full H (breakeven ratchet + 3R take-profit)
- `[N]` — reject; the trade_log analysis becomes a lesson-update only
- (no reply within 24h) — auto-rejected per mandate

---

*Drafted 2026-05-20 at user request during interactive deep-dive session. Source evidence: `memory/trade_log.md` (17 closes, 18 events), `memory/lessons.md` (2026-04-24 score 8, 2026-05-15 score 9), `memory/portfolio.md` (current state $10,236.14 flat), variant tracks `variants/v0.10-exit-confirm/` and `variants/v0.11-breakeven-2R/` (both 0 synthetic trades). No `strategy.md` or `guardrails.md` edits made — this is a proposal only.*
