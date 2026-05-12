# BULL Strategy — Variant v0.7-vol-comp-defensive

> **Variant strategy file. Self-contained.**
> **Status:** active LAB-SWEEP variant, spun up 2026-05-12
> **Lineage:** parameter sweep of v0.3-vol-compression. `vol_compression_threshold` changed from 0.5 to **0.7**.

## Philosophy

Same as v0.3 with a more defensive vol-compression threshold. Blocks entries during mild compression in addition to deep compression.

## Universe

Same as v0.3.

## Entries (long-only)

Rules 1, 2, 2a, 3, 4, 4a, 5, 5a, 5b, 6, 6a, 7, 8 identical to v0.3.

**5c. (v0.7 SWEEP)** Volatility-compression gate: if `current_ATR / mean_ATR < 0.7` → reject. **Threshold 0.7** (vs parent v0.3's 0.5). Source: Phase 1 autoloop parameter sweep, upper-bound perturbation.

## Position sizing, exits, concept buckets

Identical to v0.3.

## Variant-specific tracking

- Files in `variants/v0.7-vol-comp-defensive/`
- Routine #7 daily replays
- Compared to v0.3 (parent) and v0.6 (sibling) on leaderboard

## Promotion path

Standard. Earliest 2026-06-11.
