"""Send a message to the BULL Telegram chat.

Usage:
  python scripts/telegram_send.py "message body"
  python scripts/telegram_send.py "message body" --dry-run

Env vars required:
  TELEGRAM_BOT_TOKEN, TELEGRAM_BULL_CHAT_ID
"""
import argparse
import os
import sys
import urllib.parse
import urllib.request


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("message", help="Message body (markdown allowed)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Validate env and args, do not send")
    args = parser.parse_args()

    token = os.environ.get("TELEGRAM_BOT_TOKEN", "").strip()
    chat_id = os.environ.get("TELEGRAM_BULL_CHAT_ID", "").strip()

    if not token:
        print("ERROR: TELEGRAM_BOT_TOKEN not set", file=sys.stderr)
        sys.exit(2)
    if not chat_id:
        print("ERROR: TELEGRAM_BULL_CHAT_ID not set", file=sys.stderr)
        sys.exit(2)

    if args.dry_run:
        print("OK: token and chat_id present")
        return

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = urllib.parse.urlencode({
        "chat_id": chat_id,
        "text": args.message,
        "parse_mode": "Markdown",
        "disable_web_page_preview": "true",
    }).encode()

    try:
        with urllib.request.urlopen(url, data=data, timeout=10) as resp:
            body = resp.read().decode()
            if resp.status != 200:
                print(f"ERROR: Telegram returned {resp.status}: {body}", file=sys.stderr)
                sys.exit(3)
            print("OK: sent")
    except Exception as exc:
        print(f"ERROR: Telegram send failed: {exc}", file=sys.stderr)
        sys.exit(3)


if __name__ == "__main__":
    main()
