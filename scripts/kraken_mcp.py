#!/usr/bin/env python3
"""
Kraken MCP Server — gives Claude Code direct access to Kraken market data.

Tools:
  - kraken_ticker: Real-time price for any trading pair
  - kraken_ohlcv: OHLCV candle data (1m to 1w)
  - kraken_pairs: List available trading pairs
  - kraken_spread: Current bid/ask spread
  - kraken_risk_flag: Read today's daily risk scan result

Runs as stdio MCP server. No API key needed (public endpoints only).
"""

import json
import os
import time
from datetime import datetime, timezone

import krakenex
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("kraken", log_level="ERROR")
api = krakenex.API()

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FLAG_FILE = os.path.join(SCRIPT_DIR, "daily_risk_flag.json")

# Interval map for OHLCV
INTERVAL_MAP = {
    "1m": 1, "5m": 5, "15m": 15, "30m": 30,
    "1h": 60, "4h": 240, "1d": 1440, "1w": 10080,
}


@mcp.tool()
def kraken_ticker(pair: str = "XBTUSD") -> str:
    """Get real-time ticker data for a Kraken trading pair.

    Args:
        pair: Trading pair (e.g. XBTUSD, ETHUSD, SOLUSD, XBTUSDT).
              Kraken uses XBT for Bitcoin. Common pairs: XBTUSD, ETHUSD, SOLUSD, XXBTZUSD.
    """
    result = api.query_public("Ticker", {"pair": pair})
    if result.get("error") and result["error"]:
        return f"Error: {result['error']}"

    data = list(result["result"].values())[0]
    pair_name = list(result["result"].keys())[0]

    last = float(data["c"][0])
    high_24h = float(data["h"][1])
    low_24h = float(data["l"][1])
    open_24h = float(data["o"])
    volume_24h = float(data["v"][1])
    vwap_24h = float(data["p"][1])
    bid = float(data["b"][0])
    ask = float(data["a"][0])
    trades_24h = int(data["t"][1])

    change_pct = ((last - open_24h) / open_24h) * 100 if open_24h else 0

    return json.dumps({
        "pair": pair_name,
        "last": last,
        "bid": bid,
        "ask": ask,
        "spread": round(ask - bid, 6),
        "open_24h": open_24h,
        "high_24h": high_24h,
        "low_24h": low_24h,
        "change_24h_pct": round(change_pct, 2),
        "volume_24h": round(volume_24h, 4),
        "vwap_24h": round(vwap_24h, 2),
        "trades_24h": trades_24h,
    }, indent=2)


@mcp.tool()
def kraken_ohlcv(pair: str = "XBTUSD", interval: str = "4h", bars: int = 50) -> str:
    """Get OHLCV candle data from Kraken.

    Args:
        pair: Trading pair (e.g. XBTUSD, SOLUSD).
        interval: Candle interval — 1m, 5m, 15m, 30m, 1h, 4h, 1d, 1w.
        bars: Number of most recent bars to return (max 720, default 50).
    """
    minutes = INTERVAL_MAP.get(interval)
    if not minutes:
        return f"Error: invalid interval '{interval}'. Use: {', '.join(INTERVAL_MAP.keys())}"

    bars = min(bars, 720)
    since = int(time.time()) - (bars * minutes * 60)

    result = api.query_public("OHLC", {"pair": pair, "interval": minutes, "since": since})
    if result.get("error") and result["error"]:
        return f"Error: {result['error']}"

    pair_key = [k for k in result["result"] if k != "last"][0]
    candles = result["result"][pair_key][-bars:]

    rows = []
    for c in candles:
        ts = datetime.fromtimestamp(int(c[0]), tz=timezone.utc).strftime("%Y-%m-%d %H:%M")
        rows.append({
            "time": ts,
            "open": float(c[1]),
            "high": float(c[2]),
            "low": float(c[3]),
            "close": float(c[4]),
            "vwap": float(c[5]),
            "volume": float(c[6]),
            "trades": int(c[7]),
        })

    return json.dumps({
        "pair": pair_key,
        "interval": interval,
        "bars": len(rows),
        "data": rows,
    }, indent=2)


@mcp.tool()
def kraken_pairs(filter: str = "") -> str:
    """List available Kraken trading pairs, optionally filtered.

    Args:
        filter: Optional substring to filter pairs (e.g. 'USD', 'SOL', 'ETH').
    """
    result = api.query_public("AssetPairs")
    if result.get("error") and result["error"]:
        return f"Error: {result['error']}"

    pairs = sorted(result["result"].keys())
    if filter:
        pairs = [p for p in pairs if filter.upper() in p.upper()]

    return json.dumps({"count": len(pairs), "pairs": pairs[:100]}, indent=2)


@mcp.tool()
def kraken_spread(pair: str = "XBTUSD") -> str:
    """Get recent bid/ask spread data for a pair.

    Args:
        pair: Trading pair (e.g. XBTUSD).
    """
    result = api.query_public("Spread", {"pair": pair})
    if result.get("error") and result["error"]:
        return f"Error: {result['error']}"

    pair_key = [k for k in result["result"] if k != "last"][0]
    spreads = result["result"][pair_key][-10:]

    rows = []
    for s in spreads:
        ts = datetime.fromtimestamp(int(s[0]), tz=timezone.utc).strftime("%H:%M:%S")
        bid = float(s[1])
        ask = float(s[2])
        rows.append({"time": ts, "bid": bid, "ask": ask, "spread": round(ask - bid, 6)})

    return json.dumps({"pair": pair_key, "recent_spreads": rows}, indent=2)


@mcp.tool()
def kraken_risk_flag() -> str:
    """Read today's daily risk scan result (CLEAR or BLOCKED).
    Returns the most recent risk flag from daily_risk_flag.json.
    """
    if not os.path.exists(FLAG_FILE):
        return json.dumps({"status": "NO_DATA", "message": "daily_risk_flag.json not found"})

    with open(FLAG_FILE, "r") as f:
        data = json.load(f)

    return json.dumps(data, indent=2)


@mcp.tool()
def kraken_multi_ticker(pairs: str = "XBTUSD,SOLUSD,ETHUSD") -> str:
    """Get ticker data for multiple pairs at once.

    Args:
        pairs: Comma-separated trading pairs (e.g. 'XBTUSD,SOLUSD,ETHUSD').
    """
    result = api.query_public("Ticker", {"pair": pairs})
    if result.get("error") and result["error"]:
        return f"Error: {result['error']}"

    tickers = {}
    for pair_key, data in result["result"].items():
        last = float(data["c"][0])
        open_24h = float(data["o"])
        change_pct = ((last - open_24h) / open_24h) * 100 if open_24h else 0
        tickers[pair_key] = {
            "last": last,
            "change_24h_pct": round(change_pct, 2),
            "high_24h": float(data["h"][1]),
            "low_24h": float(data["l"][1]),
            "volume_24h": round(float(data["v"][1]), 4),
        }

    return json.dumps(tickers, indent=2)


if __name__ == "__main__":
    mcp.run(transport="stdio")
