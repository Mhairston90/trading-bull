# scripts/test_telegram_send.py
import os
import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).parent / "telegram_send.py"

def run(args, env=None):
    base_env = os.environ.copy()
    if env:
        base_env.update(env)
    result = subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        capture_output=True, text=True, env=base_env,
    )
    return result.returncode, result.stdout, result.stderr


def test_dry_run_with_env_vars_reports_ok():
    rc, out, err = run(
        ["hello", "--dry-run"],
        env={"TELEGRAM_BOT_TOKEN": "fake:token", "TELEGRAM_BULL_CHAT_ID": "-100"},
    )
    assert rc == 0, f"stderr: {err}"
    assert "OK" in out


def test_dry_run_missing_token_exits_nonzero():
    rc, out, err = run(
        ["hello", "--dry-run"],
        env={"TELEGRAM_BOT_TOKEN": "", "TELEGRAM_BULL_CHAT_ID": "-100"},
    )
    assert rc != 0
    assert "TELEGRAM_BOT_TOKEN" in (out + err)


def test_dry_run_missing_chat_exits_nonzero():
    rc, out, err = run(
        ["hello", "--dry-run"],
        env={"TELEGRAM_BOT_TOKEN": "fake:token", "TELEGRAM_BULL_CHAT_ID": ""},
    )
    assert rc != 0
    assert "TELEGRAM_BULL_CHAT_ID" in (out + err)


def test_missing_message_exits_nonzero():
    rc, out, err = run(
        ["--dry-run"],
        env={"TELEGRAM_BOT_TOKEN": "fake:token", "TELEGRAM_BULL_CHAT_ID": "-100"},
    )
    assert rc != 0
