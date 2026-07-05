"""
logger.py
Writes every conversation turn to a log file on disk, so a session's
history survives after the program exits (unlike memory.py, which is
only in-memory for the current run).

COMMIT 4 (on feature/logging branch): Adds file-based logging.
"""

import datetime
import os

LOG_FILE = "agent_log.txt"


def log_turn(speaker, text):
    """Append one conversation turn to the log file with a timestamp."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] {speaker.upper()}: {text}\n"
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line)


def read_log():
    """Return the full contents of the log file, or a message if none exists."""
    if not os.path.exists(LOG_FILE):
        return "No log file yet -- nothing has been logged this session."
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        return f.read()


def clear_log():
    """Delete the log file, starting fresh."""
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)