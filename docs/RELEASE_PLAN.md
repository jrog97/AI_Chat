
# Offline Coding Assistant — Release Plan

## Target platform
- macOS on Apple Silicon
- Desktop shell: Tauri
- Backend: Python + FastAPI
- Database: SQLite
- Local inference: Ollama

## User data
- Store the database in macOS Application Support.
- Keep logs in macOS Logs.
- Preserve existing data during upgrades.
- Never package personal conversation history.

## Startup
- Start the bundled backend as a managed local process.
- Bind to loopback only.
- Wait for a backend health check before loading the UI.
- Display a clear error if Ollama is unavailable.
- Stop the backend process on application exit.

## Model management
- Detect installed local models.
- Do not download models silently.
- Explain the storage requirements before model installation.
- Keep inference local by default.

## Release checks
- Verify app startup and shutdown.
- Verify database migration and recovery.
- Run automated tests.
- Test without Internet access.
- Test on a clean macOS user account.
- Verify signing and distribution requirements.
