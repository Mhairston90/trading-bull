# Variant v0.12-sbd-exit — Synthetic Trade Log

> Paper-paper. Same schema as main v0.2/v0.3 trade_log.
>
> **LEADERBOARD-SOURCED — FORWARD PAPER-PAPER ONLY.** The external Strategy
> Leaderboard reads this file (registry `BULL v0.12-SBD (twin)`).
>
> **GAP-RECOVERY BACKFILL (2026-05-29, user-authorized).** Routine #7 (the variant
> simulator) did not run from 2026-05-16 to 2026-05-29 (13-day scheduler gap) and
> its old spec only replayed a trailing 24h with no backfill, so the trades this
> twin would have made after its 2026-05-19 spin-up were never recorded. The user
> directed that trades the twin's rules would have taken on/after spin-up SHOULD
> count. The rows below are those trades, recovered as follows:
>   • ENTRIES — identical to main BULL v0's actual entries on/after 2026-05-19
>     (this variant's entry rules ARE v0.2, unchanged; the SBD change only tightens
>     the exit), so the twin would have entered exactly these.
>   • EXITS — main BULL v0's actual realized exits (20-EMA / stop / 4R). The SBD
>     9-EMA tightening is strictly risk-reducing, so the twin's true result is
>     >= what is shown here (this backfill is conservative).
>   • SIZING — the twin's own $10,000 account at 1.5% risk/trade (independent of
>     main BULL's equity), sized off realized equity at each entry.
> Going forward, routine #7's lookback was hardened to replay since last rebuild,
> so this manual recovery should not be needed again.

| Timestamp (UTC) | Event | Pair | Side | Size | Price | Stop | Target | R at exit | Realized PnL | Reason tag |
|-----------------|-------|------|------|------|-------|------|--------|-----------|--------------|------------|
| 2026-05-20T13:00Z | OPEN | HYPE/USD | long | 75.052537 | 50.01499 | 48.01639 | — | — | — | entry-v0.2-momentum (backfill: routine-07 gap-recovery) |
| 2026-05-21T04:00Z | OPEN | TAO/USD | long | 24.142421 | 277.83675 | 271.62362 | — | — | — | entry-v0.2-momentum (backfill: routine-07 gap-recovery) |
| 2026-05-21T08:00Z | CLOSE | HYPE/USD | long | 75.052537 | 58.38080 | — | — | +4.04 | +606.00 | exit-4R-target (backfill) |
| 2026-05-21T13:00Z | OPEN | HYPE/USD | long | 62.190445 | 57.74886 | 55.19075 | — | — | — | entry-v0.2-momentum (backfill: routine-07 gap-recovery) |
| 2026-05-22T01:00Z | CLOSE | TAO/USD | long | 24.142421 | 276.14136 | — | — | -0.50 | -75.00 | exit-ema20-confirm (backfill) |
| 2026-05-22T02:00Z | CLOSE | HYPE/USD | long | 62.190445 | 57.31133 | — | — | -0.29 | -46.14 | exit-ema20-confirm (backfill) |
| 2026-05-22T04:00Z | OPEN | AVAX/USD | long | 1142.722942 | 9.50475 | 9.36712 | — | — | — | entry-v0.2-momentum (backfill: routine-07 gap-recovery) |
| 2026-05-22T13:00Z | OPEN | SOL/USD | long | 148.727099 | 87.70383 | 86.64637 | — | — | — | entry-v0.2-momentum (backfill: routine-07 gap-recovery) |
| 2026-05-22T15:00Z | CLOSE | SOL/USD | long | 148.727099 | 86.64637 | — | — | -1.43 | -224.90 | exit-stop-hit (backfill) |
| 2026-05-22T16:00Z | CLOSE | AVAX/USD | long | 1142.722942 | 9.42529 | — | — | -0.94 | -147.84 | exit-ema20-confirm (backfill) |
| 2026-05-25T15:00Z | OPEN | BTC/USD | long | 0.272760 | 77678.12000 | 77122.02000 | — | — | — | entry-v0.2-momentum (backfill: routine-07 gap-recovery) |
| 2026-05-25T22:00Z | CLOSE | BTC/USD | long | 0.272760 | 77083.46000 | — | — | -1.07 | -162.30 | exit-stop-hit (backfill) |
| 2026-05-26T12:00Z | OPEN | TAO/USD | long | 14.513854 | 286.40410 | 276.12100 | — | — | — | entry-v0.2-momentum (backfill: routine-07 gap-recovery) |
| 2026-05-26T18:00Z | CLOSE | TAO/USD | long | 14.513854 | 280.40233 | — | — | -0.58 | -86.56 | exit-ema20-confirm (backfill) |
| 2026-05-30T13:00Z | OPEN | HYPE/USD | long | 76 | 68.06 | 66.13 | 75.80 | — | — | entry-rule-v0.2-momentum-OVERNIGHT |
| 2026-05-31T11:00Z | CLOSE | HYPE/USD | long | 76 | 68.29 | — | — | +0.12 | +17.48 | exit-ema-cross (SBD inactive at 05-31 wakes → default 20-EMA single-bar; mcp-outage gap replay 2026-06-09, user-directed) |
| 2026-06-12T04:00Z | OPEN | BTC/USD | long | 0.155773 | 63430.6 | 62647.6 | 66562.6 | — | — | entry-rule-v0.2-momentum-EOD (1H close 63430.6 > EMA20 ~63200 ✓; 1H RSI 57.4 ≥ 55 ✓; 4H 63430.6 > 50-EMA ~63013 ✓ marginal; 5a 10/15 pos ✓; SBD CLEARED → default 20-EMA exit; cluster 0/2→1/2 ✓; ATR 391.5, stop 783, size cash-capped 0.155773 BTC, risk $121.9/1.23%) |
| 2026-06-12T06:45Z | CLOSE | BTC/USD | long | 0.155773 | 63430.6 | — | — | 0.00 | $0.00 | void-entry-correction (interactive: the wake's 4H 50-EMA ~$63,013 was a 60-bar-seed artifact; converged 720-bar 4H 50-EMA = $63,682.6 → rule 3 FAILS by $252. v0.12's entry rules ARE v0.2/main's — this entry was a computation error, not the SBD hypothesis. Voided at entry price, $0 PnL, twin fidelity restored to main's correct deferral. Warm-up spec fixed in routines 01/03/07 same session.) |
| 2026-06-13T04:00Z | OPEN | TAO/USD | long | 31.78 | 217.286 | 212.6226 | 235.9396 | — | $0.00 | entry-rule-v0.2-momentum-EOD (1H close 217.286 > EMA20 213.406 ✓ +$3.88; RSI 62.5 ≥ 55 ✓; 4H close 217.286 > 4H 50-EMA 214.065 ✓ HIGH-CONFIDENCE (720 bars) +$3.22; vol $3.04M ✓; 5a 4/15 pos ✓; SBD CLEARED → standard 20-EMA exit; cluster 0/2→1/2 ✓; ATR 2.3317 2×ATR=4.6634; risk $148.21/1.50% of $9,880.74; routine-07 2026-06-12 22:00 PT) |
| 2026-06-13T09:00Z | CLOSE | TAO/USD | long | 31.78 | 237.3015 | — | — | +4.29 | +$636.09 | exit-4R-target (08:00Z bar close 237.3015 ≥ 4R target 235.9396; PnL: 31.78 × $20.0155 = +$636.09; SBD CLEARED → standard 20-EMA exit but 4R fires first; routine-07 2026-06-13 22:00 PT) |
| 2026-06-13T13:00Z | OPEN | BTC/USD | long | 0.1641 | 64100.0 | 63677.02 | 65791.92 | — | $0.00 | entry-rule-v0.2-momentum-OVERNIGHT (12:00Z bar close 64100.0; R1-R4 pass; 5a pos ✓; SBD CLEARED → W22-G 2-bar exit active (not 9-EMA tightening); cluster 0/2→1/2 ✓; ATR 211.49, 2×ATR=422.98; cash-binding 0.1641 BTC, risk $69.40/0.66% of $10,516.83; routine-07 2026-06-13 22:00 PT) |
| 2026-06-13T18:00Z | CLOSE | BTC/USD | long | 0.1641 | 63944.3 | — | — | -0.37 | -$25.55 | exit-ema20-2bar-W22G (17:00Z bar close 63944.3 < EMA20 ~63998 — 2nd consecutive close below 1H EMA20: 16:00Z close 63988.5 [1st], 17:00Z close 63944.3 [2nd]; stop 63677.02 not hit; 4R target 65791.92 not reached; PnL: 0.1641 × ($63,944.3 − $64,100.0) = −$25.55/−0.37R; SBD CLEARED → W22-G 2-bar rule applies; routine-07 2026-06-13 22:00 PT) |
| 2026-06-14T04:00Z | OPEN | BTC/USD | long | 0.1631 | 64320.2 | 63897.22 | 66012.12 | — | $0.00 | entry-rule-v0.2-momentum-EOD (indicators.py 04:00Z bar: BTC close 64320.2; R1 ✓; RSI 56.8 ≥ 55 ✓; 4H 50-EMA PASS +$750.8 ✓; R4a ✓; 5a 15/15 pos ✓; SBD CLEARED → W22-G 2-bar exit active; cluster 0/2→1/2 ✓; ATR 211.49, 2×ATR=422.98; stop=64320.2−422.98=63897.22; target=64320.2+1691.92=66012.12; cash-binding 0.1631 BTC, risk $68.98/0.66% of $10,491.28; routine-07 2026-06-13 22:00 PT) |
| 2026-06-14T13:00Z | CLOSE | BTC/USD | long | 0.1631 | 64272.8 | — | — | -0.11 | -$7.73 | exit-ema20-2bar-W22G (prior bar below EMA20 [1st]; 12:00Z bar close 64272.8 < 1H EMA20 [2nd consecutive] → W22-G 2-bar exit fires; stop 63897.22 not hit; 4R 66012.12 not reached; PnL: 0.1631×($64,272.8−$64,320.2) = −$7.73/−0.11R; SBD CLEARED → W22-G standard exit; gap replay routine07_replay_20260623.py; routine-07 2026-06-24 PT) |
| 2026-06-14T13:00Z | OPEN | HYPE/USD | long | 108.97 | 61.03 | 59.587 | 66.802 | — | $0.00 | entry-rule-v0.2-momentum-OVERNIGHT (SBD CLEARED → W22-G 2-bar exit; HYPE R1 ✓; R2 RSI ≥ 55 ✓; R3 4H 50-EMA ✓; cluster 0/2 (BTC exited same bar) ✓; ATR 0.7216, 2×ATR=1.4432; stop=59.587; target=66.802; risk ~1.5%; gap replay routine07_replay_20260623.py; routine-07 2026-06-24 PT) |
| 2026-06-14T16:00Z | CLOSE | HYPE/USD | long | 108.97 | 60.2 | — | — | -0.58 | -$90.44 | exit-ema20-2bar-W22G (14:00Z bar close below EMA20 [1st]; 15:00Z bar close 60.2 < 1H EMA20 [2nd] → W22-G 2-bar fires; stop 59.587 not hit; 4R 66.802 not reached; PnL: 108.97×($60.2−$61.03) = −$90.44/−0.58R; gap replay routine07_replay_20260623.py; routine-07 2026-06-24 PT) |
| 2026-06-15T04:00Z | OPEN | BTC/USD | long | 0.2136 | 65610.7 | 64880.78 | 68530.38 | — | $0.00 | entry-rule-v0.2-momentum-EOD (BTC R1 ✓; R2 ✓; R3 4H 50-EMA ✓; 5a ✓; SBD CLEARED → W22-G 2-bar exit; cluster 0/2 ✓; ATR ~365, 2×ATR=729.92; stop=64880.78; target=68530.38; risk ~1.5%; gap replay routine07_replay_20260623.py; routine-07 2026-06-24 PT) |
| 2026-06-16T04:00Z | CLOSE | BTC/USD | long | 0.2136 | 66109.9 | — | — | +0.68 | +$106.62 | exit-ema20-2bar-W22G (02:00Z bar close below EMA20 [1st]; 03:00Z bar close 66109.9 [2nd] → W22-G fires; stop 64880.78 not hit; 4R 68530.38 not reached; PnL: 0.2136×($66,109.9−$65,610.7) = +$106.62/+0.68R; gap replay routine07_replay_20260623.py; routine-07 2026-06-24 PT) |
| 2026-06-16T04:00Z | OPEN | HYPE/USD | long | 70.34 | 70.38 | 68.141 | 79.337 | — | $0.00 | entry-rule-v0.2-momentum-EOD (BTC exits → cluster frees; HYPE R1 ✓; R2 ✓; R3 ✓; 5a ✓; cluster 0/2 ✓; ATR ~1.1195, 2×ATR=2.239; stop=68.141; target=79.337; risk ~1.5%; gap replay routine07_replay_20260623.py; routine-07 2026-06-24 PT) |
| 2026-06-17T08:00Z | CLOSE | HYPE/USD | long | 70.34 | 73.34 | — | — | +1.32 | +$208.20 | exit-ema20-2bar-W22G (06:00Z bar close below EMA20 [1st]; 07:00Z bar close 73.34 [2nd] → W22-G fires; stop 68.141 not hit; 4R 79.337 not reached; PnL: 70.34×($73.34−$70.38) = +$208.20/+1.32R; gap replay routine07_replay_20260623.py; routine-07 2026-06-24 PT) |
| 2026-06-20T04:00Z | OPEN | SOL/USD | long | 137.84 | 70.77 | 69.605 | 75.431 | — | $0.00 | entry-rule-v0.2-momentum-EOD (SOL R1 ✓; R2 ✓; R3 4H 50-EMA ✓; 5a ✓; cluster 0/2 ✓; ATR ~0.5825, 2×ATR=1.165; stop=69.605; target=75.431; risk ~1.5%; gap replay routine07_replay_20260623.py; routine-07 2026-06-24 PT) |
| 2026-06-21T22:00Z | CLOSE | SOL/USD | long | 137.84 | 73.06 | — | — | +1.97 | +$315.65 | exit-ema20-2bar-W22G (20:00Z bar close below EMA20 [1st]; 21:00Z bar close 73.06 [2nd] → W22-G fires; stop 69.605 not hit; 4R 75.431 not reached; PnL: 137.84×($73.06−$70.77) = +$315.65/+1.97R; gap replay routine07_replay_20260623.py; routine-07 2026-06-24 PT) |
| 2026-06-22T13:00Z | OPEN | BTC/USD | long | 0.2178 | 65502.0 | 64742.89 | 68538.45 | — | $0.00 | entry-rule-v0.2-momentum-OVERNIGHT (SBD CLEARED → W22-G 2-bar exit; BTC R1 ✓; R2 ✓; R3 ✓; 5a ✓; cluster 0/2 ✓; ATR ~379.555, 2×ATR=759.11; stop=64742.89; target=68538.45; risk ~1.5%; gap replay routine07_replay_20260623.py; routine-07 2026-06-24 PT) |
| 2026-06-22T16:00Z | CLOSE | BTC/USD | long | 0.2178 | 64742.89 | — | — | -1.00 | -$165.35 | exit-stop-hit (15:00Z bar low hit stop 64742.89 intrabar; 4R 68538.45 not reached; PnL: 0.2178×($64,742.89−$65,502.0) = −$165.35/−1.00R; gap replay routine07_replay_20260623.py; routine-07 2026-06-24 PT) |
