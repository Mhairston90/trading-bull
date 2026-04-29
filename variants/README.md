# BULL Variants Rack

This directory holds **paper-paper strategy variants** that run alongside main BULL (currently `memory/strategy.md` v0.2). Variants are evaluated, not executed against the broker — they trade against synthetic $10K accounts using the same Kraken bars that main BULL sees.

## What lives here

```
variants/
├── README.md                    # this file
├── v0.X-<short-name>/
│   ├── README.md                # hypothesis + source idea + spin-up date + criteria
│   ├── strategy.md              # full self-contained strategy spec (variant rules)
│   ├── portfolio.md             # synthetic paper-paper portfolio, $10K start
│   └── trade_log.md             # hypothetical trades (paper-paper)
```

Each variant is self-contained — no shared state with main, no shared state across variants.

## Spin-up authority

Per user grant 2026-04-29: I (Claude / BULL agent) may spin up new variants autonomously when a candidate idea has high enough confidence to be worth running paper-paper. **Spin-up does not require Ring-2 `[Y/N]` approval** because variants do not affect main BULL's trades. Promotion of a variant to replace main IS Ring-2 gated through the standard weekly-memo channel.

## Mandate compliance — applies to ALL variants

Every variant strategy.md must respect the LOCKED guardrails in `memory/guardrails.md`:
- Spot only — no leverage, no margin, no perps, no options
- $10K starting equity (synthetic, paper-paper)
- Max 8 concurrent positions
- Max 4% portfolio risk at any moment
- Max 1.5% risk per trade
- Universe of 15 Kraken USD pairs from `memory/universe.md`
- Same Ring-3 kill switches apply per variant (a variant that trips a kill switch halts that variant's new entries; doesn't affect other variants)

A variant that proposes rules violating any of these gets status `REJECTED` on the leaderboard and is not run.

## Concurrent variants cap

**Maximum 3 active variants at any time.** When a 4th idea qualifies for spin-up, the worst-performing active variant by 30-day net return is retired (its files archived to `variants/archive/`).

If two variants are tied for worst, the older one (by spin-up date) is retired.

## Daily simulation cadence

Routine #7 (`routines/07-variant-paper.md`) runs daily at 22:00 PT. For each active variant:
1. Fetch past 24h of Kraken 1H + 4H bars on the universe
2. Apply variant entry rules at routine-equivalent wake times (06:00 / 13:00 / 21:00 PT closes)
3. Apply variant exit rules at every 1H close
4. Record hypothetical trades to `variants/<name>/trade_log.md`
5. Rebuild `variants/<name>/portfolio.md`
6. Update `memory/leaderboard.md`

## Promotion criteria

A variant becomes a Ring-2 promotion candidate when ALL of the following hold:

- ≥ 30 days live (statistical base requirement)
- Beats main BULL on net return over rolling 30-day window
- Beats main BULL on profit factor over rolling 30-day window
- Max drawdown does not exceed main BULL's max DD by more than 25%
- Trade count ≥ 10 in the rolling 30-day window (avoid evaluating on too few trades)

When all five hold, routine #4 Saturday harness drafts a promotion proposal in the weekly memo. User `[Y]` → variant rules become the new main `memory/strategy.md`, variant moves to `variants/archive/`, leaderboard updates. User `[N]` → variant continues running; can be re-proposed in a future memo if it keeps winning.

## Retirement criteria

A variant is retired (moved to `variants/archive/`) when:

- It loses to main BULL on net return for 60 consecutive days, OR
- It trips a Ring-3 kill switch in its synthetic account that the variant's rules don't recover from in 7 days, OR
- A 4th-ranked spin-up candidate displaces it per the cap-of-3 rule, OR
- User explicitly requests retirement

## Active rack

See `memory/leaderboard.md` for the live view.
