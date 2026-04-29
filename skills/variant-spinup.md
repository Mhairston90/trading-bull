# skill: variant-spinup

> Codifies the process of spinning up a new strategy variant in `variants/`. Invoked by routine #4 (or by the agent on direct user request, or autonomously when a high-fit `idea_bank.md` row qualifies).

## When to spin up a variant

Spin up a new variant when ANY of these is true:
1. An `idea_bank.md` row with `score >= 11` AND `status: raw or under-review` proposes a testable rule change
2. Routine #4 backtest harness shows a parameter tweak that beats main on profit factor by ≥10% over 180 days
3. User explicitly requests one
4. A retired variant has 30+ days of new evidence justifying a re-spin

Do NOT spin up if:
- Concurrent variants would exceed 3 (instead, retire the worst before spinning the new one)
- The proposed rules violate any item in `memory/guardrails.md` (mandate floor)
- An identical or near-identical variant has been retired in the past 30 days (avoid churn)
- The idea is methodology-only with no concrete testable rule

## Mandate-compliance checklist (run BEFORE creating files)

Every variant must pass ALL of these. Document Pass/Fail in the variant's README.

- [ ] **Spot only.** No rule references leverage, margin, perps, options, or futures.
- [ ] **Position cap.** Variant rules cap concurrent positions at ≤ 8 (mandate hard floor).
- [ ] **Per-trade risk.** Variant sizing rule yields ≤ 1.5% risk per trade.
- [ ] **Portfolio risk.** Variant entry-acceptance rule caps portfolio-risk-at-moment at ≤ 4%.
- [ ] **Universe.** Variant operates only on pairs in `memory/universe.md`.
- [ ] **Starting equity.** Variant initializes synthetic portfolio at $10,000.
- [ ] **No external broker.** Variant is paper-paper only — does not place real Kraken orders.
- [ ] **Kill switches.** Variant inherits Ring-3 kill switches from `memory/guardrails.md`.

If any check fails, the variant is not spun up. Log the failure with reason in `memory/leaderboard.md` under "Rejected at spin-up".

## File layout (create in this order)

1. `variants/v0.X-<short-name>/README.md` — see template below
2. `variants/v0.X-<short-name>/strategy.md` — copy current main `memory/strategy.md` verbatim, then add/modify the specific rules being tested. Mark variant-only rules with `(v0.X only)` so the diff vs. main is unambiguous.
3. `variants/v0.X-<short-name>/portfolio.md` — initialize at $10K, no positions, all kill-switches clear, equity peak = $10K.
4. `variants/v0.X-<short-name>/trade_log.md` — empty header, schema reference.
5. Append a row to `memory/leaderboard.md` under "Active rack" with status `LAB`.
6. Mark the source `idea_bank.md` row (if applicable) with status `under-review` and a pointer to the variant directory.

## README template

```markdown
# Variant v0.X — <descriptive name>

**Spin-up date:** YYYY-MM-DD
**Source idea:** IDEA-YYYYMMDD-NN (or "internal" / "user-requested")
**Hypothesis:** <one-sentence statement of what this variant believes about the market>
**Diff vs main (currently v0.Y):**
- Added: <rule(s)>
- Removed: <rule(s)>
- Modified: <rule(s)>

## Mandate-compliance check

- [x] Spot only
- [x] ≤ 8 positions
- [x] ≤ 1.5% per trade
- [x] ≤ 4% portfolio
- [x] Universe from memory/universe.md
- [x] $10K start
- [x] Paper-paper only
- [x] Inherits Ring-3 kill switches

## Promotion criteria (from variants/README.md)

Standard: 30+ days live, beats main on net return + profit factor, DD increase ≤ 25%, trade count ≥ 10 in rolling 30d window.

## Notes

<rationale, source quotes, threshold-pick reasoning, expected behavior>
```

## After spin-up

- Routine #7 (variant-paper) picks up the variant on its next daily wake (22:00 PT). No additional registration step.
- The variant accumulates synthetic trades; leaderboard updates every routine #7 run.
- Routine #4 Saturday reads the leaderboard when drafting weekly memos.

## Retirement (when the cap-of-3 forces it, or when criteria triggered)

1. Move `variants/v0.X-<name>/` to `variants/archive/v0.X-<name>-YYYY-MM-DD/`
2. Update the leaderboard row: `status: retired`, add reason
3. Final stats snapshot stays in the archive copy
4. If the variant was tracking an `idea_bank.md` row, mark that row `pruned` with retirement reason

## Promotion (when criteria met + user `[Y]` on memo)

1. Variant strategy.md → main `memory/strategy.md` (with version bump)
2. Old main rules → `variants/archive/v0.Y-<name>-YYYY-MM-DD/`
3. Main `memory/portfolio.md` and `memory/trade_log.md` are NOT replaced — main BULL keeps trading on the new rules from this point forward; the variant's hypothetical history stays in archive
4. Update `memory/leaderboard.md` to reflect new main + archived variant
5. Mark the source `idea_bank.md` row `applied`

## Mandate footnote

Spin-up does NOT modify `memory/strategy.md`, `memory/guardrails.md`, `memory/portfolio.md`, `memory/trade_log.md`, or any non-variant routine. Spin-up only creates new files under `variants/` and a leaderboard row.

The autonomy granted is to create candidates, not to alter trading. Promotion remains Ring-2 gated.
