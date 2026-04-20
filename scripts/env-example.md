# Required Environment Variables

All secrets come from the **local environment** (Claude Code session or user shell). They are NEVER written to any file in this repo.

## Variables

| Name | Purpose | Format |
|------|---------|--------|
| `TELEGRAM_BOT_TOKEN` | Sends messages to BULL chat | `NNNNNNNN:AAAA...` (from @BotFather) |
| `TELEGRAM_BULL_CHAT_ID` | Chat/thread ID for BULL notifications | Numeric, negative for groups |
| `FIRECRAWL_API_KEY` | News scanning via Firecrawl | `fc-...` |

## How to set them (Windows)

Open a PowerShell as the user running Claude Code:

```powershell
setx TELEGRAM_BOT_TOKEN "123456:ABC..."
setx TELEGRAM_BULL_CHAT_ID "-1001234567890"
# FIRECRAWL_API_KEY already set if firecrawl CLI works
```

Then restart Claude Code Desktop so routines inherit the new env vars.

## Verification

```bash
python scripts/telegram_send.py "BULL env test" --dry-run
```

Should print `OK: token and chat_id present` and exit 0 without actually sending.
