# Skill: Sending Telegram Messages

Used by routines to notify the user. Always through `scripts/telegram_send.py`, never via a raw HTTP call, never by echoing the token anywhere.

## When to send

- **Routine #1 Overnight:** digest only if (a) kill switch tripped, (b) a new position was opened, or (c) an unusual news item was flagged. Silent otherwise.
- **Routine #2 Midday:** only if an anomaly is detected (drawdown warning, kill-switch approaching, open-position stop breached between candles).
- **Routine #3 EOD:** mandatory daily card with P&L summary, trades, and notes.
- **Routine #4 Harness:** mandatory weekly memo summary + any gated approval request.
- **Routine #5 Allocation:** mandatory weekly allocation summary + any gated approval request.
- **Any routine:** immediate ALERT if a Ring 3 kill switch fires.

## How to send

From within a routine, invoke the Bash tool:

```bash
python scripts/telegram_send.py "MESSAGE_BODY"
```

`MESSAGE_BODY` supports Telegram Markdown. Keep it under ~3000 chars to avoid the 4096 limit.

## Message templates

### EOD card (routine #3)

```
📊 BULL EOD — 2026-04-21

Equity: $10,123.45 (+1.23%)
Day PnL: +$123.45 (+1.23%)
Since start: +1.23%
Drawdown: 0.00%

Trades today: 3 opened, 2 closed
- OPENED: SOL/USD long @ 142.10, stop 138.50
- OPENED: ETH/USD long @ 3310, stop 3240
- CLOSED: BTC/USD long @ 67420 for +2.1R

Open positions: 4/8
Status: ✅ all clear

vs BTC-hold (rolling 30d): +0.4%

Notes:
- ETH momentum acceleration after macro headline
```

### Gated approval request (routines #4, #5)

```
🔔 BULL proposal — W17 memo

Change: Add RSI(4) < 20 as mean-rev entry trigger
Evidence: 12/15 backtest days improved, PF 1.8→2.1
Risk: may overtrade in chop
Expected impact: +0.3R/trade average

Reply:
[Y] approve    [N] reject    [D] defer 1 week

Auto-reject in 24h if no response.
```

### Kill-switch ALERT (any routine)

```
🚨 BULL KILL SWITCH TRIPPED

Trigger: daily loss > 5% (-5.2% today)
Action: halted new entries, holding open positions
Open: 3 positions, total risk 1.2% of equity
Next: midday routine will re-check. Manual override: send `RESUME`.
```

## User command vocabulary

These keywords in user's replies to Telegram are recognized by routine #1 (picks them up from a `user_inbox.md` if the user maintains one, or ignored in v1 — approval flow is informal in v1, user replies in the chat and BULL reads them in the next routine run):

- `Y` / `YES` — approve the most recent gated proposal
- `N` / `NO` — reject
- `D` / `DEFER` — defer one week
- `RESUME` — clear kill-switch pause, resume trading
- `UNLOCK <guardrail-key>` — explicit override (e.g. `UNLOCK daily-loss-cap`)

**v1 note:** BULL does not poll Telegram for replies. User-decisions are captured by the user pasting the approval into the next routine run or updating `memory/strategy.md` directly. v2 could poll getUpdates. For v1, the gated flow works on trust — BULL writes the proposal + waits for the file change.
