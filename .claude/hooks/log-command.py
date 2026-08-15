#!/usr/bin/env python3
"""Claude Code PostToolUse hook: append each Bash command Claude runs to command-log.txt."""
import datetime
import json
import os
import sys

data = json.load(sys.stdin)
cmd = data.get("tool_input", {}).get("command", "")
if cmd:
    log_path = os.path.join(os.environ.get("CLAUDE_PROJECT_DIR", "."), "command-log.txt")
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_path, "a") as f:
        f.write(f"[{ts}] {cmd}\n")
