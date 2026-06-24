# Variant v0.7-vol-comp-defensive — Synthetic Portfolio

> **Paper-paper account.** Synthetic $10K starting equity.
> **Category:** LAB-SWEEP (parameter sweep of v0.3, threshold 0.5 → 0.7)
> **Last rebuild:** 2026-06-24T16:35Z (routine-07 wake 2026-06-24 PT — gap replay 2026-06-14T05:00Z→2026-06-24T13:00Z; TAO stop-hit, ETH 4R +$591.51 WIN, BTC EMA exit, XDG stop-hit; 4 closed trades lifetime)

## Account

- Starting equity: **$10,000.00**
- Cash: **$10,202.68** (flat)
- Realized PnL (variant lifetime): **+$202.69** (TAO stop-hit −$141.46 −1.00R; ETH +$591.51 +4.00R; BTC −$91.99 −0.59R; XDG stop-hit −$155.37 −1.00R)
- Unrealized PnL: **$0.00** (no open positions)
- Position values (MTM): **$0.00**
- Current equity: **$10,202.68**
- Equity peak: **$10,450.05** (set 2026-06-15T14:00Z at ETH 4R close)
- Drawdown from peak: **2.37%** ($10,450.05 → $10,202.68 after BTC EMA exit + XDG stop-out)

## Open positions

_None._

Portfolio risk-at-moment: **0.00%** (cap 4%, full headroom).
Open positions: **0 / 4** (cluster 0/2).

## Active kill-switch state

- Daily realized 2026-06-24 PT: $0.00 (last trade was XDG Jun17) — clear vs 5% cap
- Consecutive losing trading days: 2 (BTC Jun16, XDG Jun17; cap 7) — clear
- Max drawdown: 2.37% from peak $10,450.05 (cap 25%, warn 12.5%) — clear
- Equity floor: $10,202.68 > $7,500 — OK
- Regime gate: 5a FAIL / SBD ACTIVE at OVERNIGHT 2026-06-24T13:00Z → 0 entries
- **All clear. No open positions. 4 closed trades lifetime.**

## Rolling performance vs main v0.2 AND parent v0.3

| Window | v0.7 return | v0.3 (parent) return | main return | Verdict |
|--------|-------------|----------------------|-------------|---------|
| 30d | +2.03% | +5.87% | +4.14% | v0.3 AHEAD of v0.7; but v0.7's single ETH 4R win is its best trade; need more samples |
| 90d | — | — | — | not yet computable |

## Days live

- Spin-up: 2026-05-12
- As of last rebuild: **43 days**
- Promotion-eligible: **2026-06-11 (reached)** — 4 closed trades lifetime (need ≥10) → NOT promotion-eligible. 0.7× vol-comp gate restricts entries more aggressively than the 0.5× gate in v0.3. More samples needed.

## Notes

Parameter sweep — `vol_compression_threshold = 0.7` (vs v0.3's 0.5). Key finding from gap replay: the 0.7× gate ALLOWED the ETH entry on June 14 (ATR compressed at that time) while BLOCKING later HYPE, SOL, BTC entries (rally pushing ATR above 0.7× mean). The ETH +4.00R/+$591.51 was the single biggest trade win of any variant in the gap replay — 22h clean trend from $2,480→$2,697. However, the gate also caused 2 stop-hit losses (TAO, XDG) — the 0.7× threshold allows slightly more entries than 0.3's 0.5× but still quite restrictive.

### Routine #7 wake log

- **2026-05-16 22:00 PT (first sim wake since 05-12 spin-up)** — past-24h replay window = 2026-05-15 10:00 UTC → 2026-05-16 10:00 UTC. Wakes: OVERNIGHT (05-15 13:00Z), MIDDAY (05-15 20:00Z, default-skip), EOD (05-16 04:00Z). Broadly-red tape — M3 failed universe-wide 05-15 and 05-16. 5a rejected at both wakes before 0.7× vol-comp gate reached. 0 entries. Kill switches clear at $10,000.
- **2026-05-29 22:00 PT** — SBD active 1/15 positive; 5a FAIL → 0 entries. $10,000. Days live: **17**.
- **2026-05-30 22:00 PT** — 12/15 positive; 5a PASS. HYPE passes R1+R2+R3; vol-comp 0.7× gate check: HYPE ATR elevated in active rally → gate BLOCKS. 0 entries. $10,000. Days live: **18**.
- **2026-06-10 22:00 PT** *(partial-run)* — 7-day cap replay 2026-06-04T05:00Z → 2026-06-11T05:00Z. Crash wakes SBD → 5a FAIL. Recovery wakes 06-07→06-09: 5a PASS but 0.7× vol-comp gate BLOCKED (crash-spiked ATR 3-5×). Post-recovery SBD → 5a FAIL. **0 entries.** $10,000. 30-day threshold reached. 0 trades → NOT eligible.
- **CORRECTION NOTE (2026-06-11 22:00 PT):** BTC close $62,590 stale; corrected $63,430.6 passes rule 3. 0.7× vol-comp gate: threshold 0.7×$412 = $288; current ATR $391.5 > $288 → BLOCKS. 0-entry conclusion unchanged.
- **2026-06-10 22:00 PT (MISLABELED as 2026-06-11 22:00 PT — stale)** — EOD 2026-06-12T04:00Z: 5a PASS, SBD CLEARED. Entry scan: all 15 pairs fail rule 3 (STALE: used BTC $62,590). Vol-comp 0.7× gate: ATR elevated → BLOCKS. **0 entries.** $10,000. Days live: 31.
- **2026-06-11 22:00 PT (correction run)** — EOD 2026-06-12T04:00Z (corrected): BTC passes R1-R3. **Vol-comp gate 5c (0.7× threshold) BLOCKS: threshold 0.7×$412 = $288; current ATR $391.5 > $288. 0 entries.** $10,000. Days live: **31**.
- **2026-06-12 22:00 PT (routine-07)** — replay window 2026-06-12T06:45Z → 2026-06-13T05:00Z (~22h). **OVERNIGHT 13:00Z:** BTC R2 FAIL. **EOD 2026-06-13T04:00Z:** 4/15 pos, SBD CLEAR. TAO sole PASS. **Vol-comp 0.7× gate: indicators `volcomp_07 = OPEN` — TAO ATR 2.4062 compressed → gate BLOCKS (0.7× threshold: ATR must be < 0.7× mean, which TAO does NOT meet). 0 entries.** Key A/B: v0.3 (0.5× threshold) ALLOWS TAO; v0.7 (0.7× threshold) BLOCKS TAO. $10,000. Days live: **32**.
- **2026-06-13 22:00 PT (routine-07)** — replay window 2026-06-13T05:08Z → 2026-06-14T05:00Z (~23.87h). **EOD 2026-06-14T04:00Z:** 15/15 positive. TAO `volcomp_07=shut` → ALLOWED. **ENTRY: TAO/USD LONG 9 @ $274.733, stop $259.015, target $337.606.** FIRST TRADE for v0.7 — 33 days to first entry. Risk $141.46/1.41% of $10,000. Equity $10,000. Days live: **33**.
- **2026-06-24 PT (routine-07 — gap replay via routine07_replay_20260623.py; fired ~09:35 PT off-schedule)** — Replay window: **2026-06-14T05:00Z → 2026-06-24T13:00Z** (10.5 days; fully recovered via Kraken REST 30d history). **4 new closes, 3 new opens across 12 wakes.** Trade sequence: **TAO CLOSE 2026-06-14T06:00Z −1.00R/−$141.46** (stop 259.015 hit ~05:00Z next bar after OVERNIGHT Jun13 entry; 22h hold; TAO pulled back sharply); **ETH OPEN 2026-06-14T13:00Z + CLOSE 2026-06-15T14:00Z +4.00R/+$591.51** (0.7× gate ALLOWED ETH at OVERNIGHT Jun14: ATR compressed post-stable; ETH rallied cleanly from $2,480.2→$2,697.8 over 25h; 4R target fired at 13:00Z bar close — v0.7's BEST TRADE and the largest single trade of any variant in the replay); **BTC OPEN 2026-06-15T04:00Z + CLOSE 2026-06-15T23:00Z −0.59R/−$91.99** (EOD Jun15 BTC entered; 22:00Z bar below EMA20 → 1-bar exit; net unrealized gain then reversed); **XDG OPEN 2026-06-16T04:00Z + CLOSE 2026-06-16T21:00Z −1.00R/−$155.37** (EOD Jun16 XDG entered; Jun17 morning bar hit stop; quick reversal from EOD entry). **Entry scans Jun17–Jun24:** 0.7× gate BLOCKED HYPE (Jun17 ATR elevated post-rally), SOL (Jun20 ATR elevated), BTC (Jun22 OVERNIGHT ATR elevated). June 24 OVERNIGHT: SBD → 5a FAIL. **NEW PEAK $10,450.05** at ETH close (Jun15); subsequent BTC loss and XDG stop-out → DD 2.37%. **Key A/B: v0.7 (0.7× gate, 4 trades) vs v0.5 (no gate, 10 trades): v0.7's ETH +4.00R = 63% of ALL v0.5's realized PnL in 1 trade. But v0.7's 2 stop-hits (TAO, XDG) cost $296.83.** All kill switches clear. Days live: **43**.
