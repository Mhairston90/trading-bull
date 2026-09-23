# BULL Portfolio State

> **Rebuilt each wake** from `trade_log.md`; the log remains the source of truth.
> **Last rebuild:** 2026-09-23T20:00:00Z routine-02-midday — NEAR/USD stop-hit-intrabar on 14:00Z bar (low 4.4012 < stop 4.45616). Book now flat.

## Account

- Starting equity: **$10,000.00**
- Cash: **$10,309.52** (flat book)
- Realized PnL: **+$309.52**
- Unrealized PnL: **$0.00** (no open positions)
- Current equity: **$10,309.52**
- Equity peak: **$11,068.89**
- Drawdown from peak: **6.86%**
- Since-inception return: **+3.10%**

## Open positions

None. Book flat.

Portfolio risk-at-moment: **0.000%**
Open positions: **0 / 8** (strategy cap 0/4; BTC cluster 0/2).

## Midday exit rationale (2026-09-23T14:00Z)

- **Trigger**: static 2×ATR stop at $4.45616 pierced intrabar on the 14:00-15:00Z 1H bar (bar low $4.4012).
- **Fill**: stop price × (1 − 0.0005) slippage = $4.45393 (per prior stop-hit-intrabar convention: SOL 06-17/06-27, HYPE 07-07).
- **R at exit**: −1.01R (marginal negative slippage vs pure −1R stop).
- **Realized PnL**: −$172.30 (gross −$158.51, entry commission $7.10, exit commission $6.69, both at 0.26% Kraken taker).
- **Time-in-trade**: 1 bar (13:00→14:00Z; ~60min).
- **Reason tag**: `exit-stop-hit-intrabar`.

### Post-mortem — brief

- Entry was on-rule (all rule-1..8 checks documented in routine-01 research_log). Fill 4.72836 was near the top of the 13:00Z bar (which itself topped 4.7531). The following 14:00Z bar posted an outside-day style range 4.4012→4.773 with close 4.6476 — a −7% intrabar sweep from the 14:00Z high pierced the stop before recovering.
- Live-ticker showed continued weakness after the sweep: 15:00Z bar low 4.1327 close 4.216 (−16% peak-to-trough vs 12:00Z close), reaffirming the stop's protective purpose.
- Not a mandate/discipline failure — this is the designed −1R outcome of a stop-out on a rule-8 default winner entering into a distribution top. Regime was already marginal at entry (4/15 at exact 5a floor).
- Post-stop live NEAR spread 2-5bps confirmed clean fill availability at stop.
- Cooldown 5b now active for NEAR — no new NEAR entry until 2026-09-24T14:00:00Z.

## Active kill-switch state

- Daily loss cap (2026-09-23 PT): **-1.64%** ($-172.30 / $10,481.82 start-of-day). CLEAR (5% cap, 3.36pp headroom).
- Consecutive-loss cap: 1 loss (NEAR today). Streak = 1 of 7. CLEAR.
- Max drawdown: **6.86%** from peak $11,068.89. CLEAR (25% cap, 12.5% warn, 5.64pp headroom).
- Equity floor: **$10,309.52 > $7,500** (+$2,809.52 above). CLEAR.
- Exposure: 0.000% / 4% used. CLEAR.
- Cluster cap: 0/2. CLEAR.
- Universe/liquidity: N/A (flat). CLEAR.
- MCP availability: Kraken REST + MCP OK. CLEAR.
- **All Ring 3 kill switches CLEAR.**
