# skill: variant-spinup

> Codifies the process of spinning up a new strategy variant in `variants/`. Invoked by routine #4 (or by the agent on direct user request, or autonomously when a high-fit `idea_bank.md` row qualifies).

## When to spin up a variant

Spin up a new variant when ANY of these is true:
1. An `idea_bank.md` row with `score >= 11` AND `status: raw or under-review` proposes a testable rule change
2. Routine #4 backtest harness shows a parameter tweak that beats main on profit factor by ≥10% over 180 days
3. User explicitly requests one
4. A retired variant has 30+ days of new evidence justifying a re-spin
5. **Parameter-sweep spawn (Phase 1 autoloop, 2026-05-12):** routine #4 Saturday spawns sweep variants from active hypothesis variants with declared tuneable parameters. Each spawned variant perturbs one parameter while inheriting all other rules verbatim.

Do NOT spin up if:
- Concurrent variants would exceed 10 (instead, retire the worst before spinning the new one)
- The proposed rules violate any item in `memory/guardrails.md` (mandate floor)
- An identical or near-identical variant has been retired in the past 30 days (avoid churn)
- The idea is methodology-only with no concrete testable rule
- The same parameter value is already being tested in an active variant (no duplicate sweeps)

## Parameter-sweep mode (Phase 1 autoloop)

When spawning from a parameter sweep, the variant README MUST include a `## Lineage` section:

```markdown
## Lineage

- **Parent variant:** v0.X-<parent-name>
- **Parameter perturbed:** <parameter-name> (parent value <X>, this variant <Y>)
- **Perturbation direction:** higher / lower / categorical-alternative
- **Sibling variants:** v0.Y-<sibling-name> (parent's other sweeps; cross-reference for comparison)
- **Hypothesis:** does perturbing <parameter> from <X> to <Y> on this parent improve any of {net return, profit factor, drawdown, trade count}?
```

The strategy.md file copies the parent's rules verbatim, except the perturbed parameter line gets a `(v0.Y sweep)` marker showing the new value.

Sweep variants follow the standard mandate-compliance checklist; since they inherit all rules from a mandate-passing parent and only change one parameter, the check is normally a quick re-confirmation rather than a full audit.

## Tuneable parameters per variant

Each hypothesis variant declares its tuneable parameters in the README under a `## Tuneable parameters` block (for routine #4 to find them). Examples:

- **v0.3-vol-compression:** `vol_compression_threshold` (current 0.5×; reasonable sweep range 0.3-0.8)
- **v0.4-mean-reversion-sleeve:** `rsi_oversold_threshold` (current 25; reasonable sweep range 20-35)
- **v0.5-cluster-cap-tight:** `cluster_cap` (current 1; reasonable sweep range 0-2; bounded by mandate which caps total positions at 8)

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
