
import argparse
import logging
import os
import sqlite3
import sys
from pathlib import Path

from app_paths import get_data_dir, get_log_dir


def migrate_legacy_database():
    """Import development history only when the packaged DB is absent."""
    data_dir = get_data_dir()
    target = data_dir / "assistant.db"

    if target.exists():
        return

    # This is the previous development database location.
    legacy = Path.home() / "OfflineCodingAssistant" / "assistant.db"

    if not legacy.exists():
        return

    temporary = data_dir / "assistant.db.importing"

    if temporary.exists():
        temporary.unlink()

    try:
        with sqlite3.connect(legacy) as source:
            with sqlite3.connect(temporary) as destination:
                source.backup(destination)

        with sqlite3.connect(temporary) as check:
            result = check.execute(
                "PRAGMA integrity_check"
            ).fetchone()[0]

        if result != "ok":
            raise RuntimeError(
                f"Database import failed integrity check: {result}"
            )

        # Do not overwrite an existing destination.
        if target.exists():
            temporary.unlink()
        else:
            os.replace(temporary, target)

    finally:
        if temporary.exists():
            temporary.unlink()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args()

    if args.host != "127.0.0.1":
        raise SystemExit("Backend must bind to 127.0.0.1")

    if not 1 <= args.port <= 65535:
        raise SystemExit("Invalid port")

    os.environ["OFFLINE_ASSISTANT_USE_USER_DATA"] = "1"

    log_file = get_log_dir() / "backend.log"
    logging.basicConfig(
        filename=str(log_file),
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )

    migrate_legacy_database()

    # Import only after the data directory and migration are ready.
    import main as application
    import uvicorn

    uvicorn.run(
        application.app,
        host=args.host,
        port=args.port,
        log_config=None,
    )


if __name__ == "__main__":
    main()

