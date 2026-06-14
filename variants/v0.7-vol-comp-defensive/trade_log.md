# Variant v0.7-vol-comp-defensive — Synthetic Trade Log

> Paper-paper. Same schema as parent v0.3.

| Timestamp (UTC) | Action | Pair | Side | Size | Price | Stop | Target | R | Reason | Variant |
|-----------------|--------|------|------|------|-------|------|--------|---|--------|---------|

| 2026-06-14T04:00Z | OPEN | TAO/USD | LONG | 9 | 274.733 | 259.015 | 337.606 | — | entry-rule-v0.7-volcomp-EOD (indicators.py 04:00Z bar: TAO close 274.733 > EMA20 ✓; RSI 76.3 ≥ 55 ✓ (≤80 ✓); 4H 50-EMA PASS +$52.63 ✓; vol $20.46M ✓; 5a 15/15 pos ✓; SBD CLEAR ✓; vol-comp 5c (0.7 threshold): BTC OPEN→blocked; SOL OPEN at 0.7→blocked; TAO volcomp_07=shut → ALLOWED ✓; cluster 0/2→1/2 ✓; ATR 7.8591, 2×ATR=15.7182; stop=274.733−15.7182=259.015; target=274.733+62.873=337.606; size: 1.5%×$10,000=$150/15.7182=9.54→floor 9 units; actual risk $141.46/1.41% of $10,000; FIRST TRADE for v0.7 — day 33; rule 8: BTC/SOL/HYPE blocked → TAO highest unblocked pair passing R1-R3; routine-07 2026-06-13 22:00 PT) | v0.7-vol-comp-defensive |
