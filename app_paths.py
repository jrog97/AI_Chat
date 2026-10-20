
from pathlib import Path
import os
import sys


APP_NAME = "OfflineCodingAssistant"


def get_data_dir() -> Path:
    """Return the per-user directory for writable application data."""
    override = os.environ.get("OFFLINE_ASSISTANT_DATA_DIR")

    if override:
        data_dir = Path(override).expanduser()
    elif sys.platform == "darwin":
        data_dir = (
            Path.home()
            / "Library"
            / "Application Support"
            / APP_NAME
        )
    else:
        # A fallback for development and other platforms.
        data_dir = Path.home() / f".{APP_NAME}"

    data_dir.mkdir(parents=True, exist_ok=True)
    return data_dir


def get_log_dir() -> Path:
    """Return the directory for application log files."""
    if sys.platform == "darwin":
        log_dir = (
            Path.home()
            / "Library"
            / "Logs"
            / APP_NAME
        )
    else:
        log_dir = get_data_dir() / "logs"

    log_dir.mkdir(parents=True, exist_ok=True)
    return log_dir
