# Variant v0.13-trend-confirm — Synthetic Trade Log

> Paper-paper. Same schema as main v0.3 trade_log.

| Timestamp (UTC) | Event | Pair | Side | Size | Price | Stop | Target | R at exit | Realized PnL | Reason tag |
|-----------------|-------|------|------|------|-------|------|--------|-----------|--------------|------------|
| 2026-06-13T04:00Z | OPEN | TAO/USD | LONG | 32.17 | 217.286 | 212.6226 | 235.9396 | — | $0.00 | entry-rule-v0.13-trend-confirm-EOD (inherits v0.3 rules: R1 ✓ +$3.88; RSI 62.5 ≥ 55 ✓; 4H close > 50-EMA ✓ HIGH-CONF; vol-comp gate 5c: TAO SHUT at 0.5 → ALLOWED ✓; cluster 0/2→1/2 ✓; v0.13 additional filters: 2-bar EMA confirm — prior 1H bar also above EMA20 213.406 HIGH-CONF (TAO trending +$3.88 above EMA, strong trend); 4H RSI ≥ 50: est. ~60-65 based on strong 4H uptrend ✓; 5a 4/15 pos ✓; SBD CLEAR ✓; ATR 2.3317 2×ATR=4.6634; risk $150.00/1.50% of $10,000; first hypothetical trade for v0.13 — 24d to first entry; routine-07 2026-06-12 22:00 PT) |
