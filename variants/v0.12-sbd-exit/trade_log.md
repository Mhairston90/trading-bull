# Variant v0.12-sbd-exit — Synthetic Trade Log

> Paper-paper. Same schema as main v0.2/v0.3 trade_log.
>
> **LEADERBOARD-SOURCED — FORWARD PAPER-PAPER ONLY.** The external Strategy
> Leaderboard reads this file (registry `BULL v0.12-SBD (twin)`). **Never write
> backtest / reconstructed / hypothetical-historical rows here.** Only routine #7
> forward-simulated trades dated on/after spin-up 2026-05-19 belong in this file.
> Backtests live in `backtest_notes.md` (NOT registry-sourced) and must stay there.
> Defense-in-depth: the registry sets `live_start_iso: 2026-05-19`, so the adapter
> filters out any trade entered before then even if one is mistakenly added.

| Timestamp (UTC) | Event | Pair | Side | Size | Price | Stop | Target | R at exit | Realized PnL | Reason tag |
|-----------------|-------|------|------|------|-------|------|--------|-----------|--------------|------------|

(empty — spun up 2026-05-19)
