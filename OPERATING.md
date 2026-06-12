# BULL — Operating Notes

> Operational constraints discovered through use. Not part of the locked mandate.
> Edit freely as new constraints emerge.

## Cron requires Claude Code Desktop to be open

**The scheduled-tasks MCP that fires BULL's 7 routines only runs while Claude Code Desktop is the active host process.** When Claude Code is closed, the cron pauses entirely — routines do NOT fire and they do NOT catch up later.

**Observed gap:** 2026-04-29 20:07Z → 2026-05-04 (today). User went offline, Claude Code closed, cron silent for ~5 days. Zero routine wakes, zero trades, zero research_log entries during the gap.

When Claude Code is reopened, the scheduler resumes from the **next** scheduled `nextRunAt` (not from missed wakes). One missed wake stays missed.

### Mitigations (pick one)

| Option | Effort | Robustness |
|---|---|---|
| **A. Keep Claude Code Desktop open 24/7** | trivial | breaks on Windows reboot until re-opened |
| **B. Auto-launch Claude Code on Windows boot** | small (Windows startup folder shortcut) | survives reboots, breaks if Claude Code crashes |
| **C. Both A + B** | small | recommended baseline |
| **D. Move BULL routines to Windows Task Scheduler + Claude API bridge script** | medium (~2-4h build) | independent of Claude Code state |

**Current choice (2026-05-04):** A + B (auto-launch + keep open). D deferred to v2 infrastructure work.

**2026-05-24 restoration note:** A Codex-side ops audit found Claude Desktop running but `C:\Users\Mhair\AppData\Roaming\Claude\claude_desktop_config.json` had `"ccdScheduledTasksEnabled": false`, which disables the Claude Code scheduled-task runner even while the app is open. Restored it to `true`. Also converted `C:\Users\Mhair\.claude\scheduled-tasks\bull-01-overnight\SKILL.md` from an older copied prompt body into a source-of-truth wrapper that reads `routines/01-overnight.md`, matching the safer `bull-03-eod` pattern.

### How to verify cron is alive

In a Claude Code session, ask:
> List BULL scheduled tasks

If `lastRunAt` for any task is older than its scheduled cadence, cron stalled. Check that Claude Code is actually running (not just minimized — fully alive).

Also verify `ccdScheduledTasksEnabled` is `true` in `C:\Users\Mhair\AppData\Roaming\Claude\claude_desktop_config.json`. If it is `false`, BULL's scheduled task files can exist but no routine will fire.

### How to manually fire a missed routine

Routines live at `C:\Users\Mhair\.claude\scheduled-tasks\bull-XX-name\SKILL.md`. Manual catch-up isn't recommended for routine #1/#2/#3 (they make trade decisions — if you've moved on multiple wakes, the regime context is stale anyway). Manual catch-up IS fine for #4 (Saturday harness) and #5 (Sunday allocation) since they're weekly + idempotent.

To manually fire: open the SKILL.md, copy the prompt body, paste into a fresh Claude Code conversation. Same effect as the scheduler firing it.

## CODEX competitor data feed (stale)

The leaderboard at `C:\Users\Mhair\OneDrive\Desktop\strategy-leaderboard\` reads CODEX competitor data from `data/codex/*.md`. As of 2026-05-04, all 6 CODEX files show **0 trades / $10,000 baseline**.

This is either:
1. **Genuinely flat** — Codex's strategies haven't fired any entries in their setup window
2. **Stale baseline** — the files haven't been refreshed since the user manually populated them

If (2), the competition tracker is showing stale data. To refresh, manually copy fresh `portfolio.md` + `trade_log.md` from each Codex variant into the matching `data/codex/<variant>_portfolio.md` and `<variant>_trade_log.md` paths.

There is no automated sync between Codex's trading repo and the leaderboard's local files. v2 idea: build a `pull-codex.bat` that pulls Codex's GitHub raw or a shared sheet and writes the local files.

## Routine cadence reference

| Cron | Routine | Local time (PT) | Notes |
|---|---|---|---|
| `0 6 * * *` | #1 overnight | 06:06 | full agent — entry scan + position mgmt + Telegram |
| `0 13 * * *` | #2 midday | 13:06 | lean — exit checks + anomaly Telegram only |
| `0 21 * * *` | #3 eod | 21:10 | journal + mandatory Telegram EOD card |
| `0 10 * * *` | #4 harness | 10:06 | day-gates Saturday — strategy proposals |
| `30 10 * * *` | #5 allocation | 10:40 | day-gates Sunday — allocation review |
| `0 18 * * *` | #6 idea-scan | 18:02 | daily — adds candidates to `idea_bank.md` |
| `0 22 * * *` | #7 variant-paper | 22:05 | daily — simulates variant rack |

All times PT. Day-gate routines (#4 #5) fire daily but no-op on the wrong day.
