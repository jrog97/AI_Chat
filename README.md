# Offline AI Coding Assistant

A privacy-focused AI coding assistant powered by locally running large language models (LLMs). Built to help developers write, explain, debug, analyze, and improve code while keeping control of their source code and development environment.

The project combines a local AI runtime, a Python backend, persistent conversation history, project-aware coding tools, and a desktop interface. The long-term vision is a standalone macOS application with a native iPhone companion.

## Overview

The Offline AI Coding Assistant is designed to bring AI-assisted software development to your local machine without requiring a cloud-based AI service for normal model inference.

The application uses [Ollama](https://ollama.com/) to run compatible language models locally. Its development environment includes a Python/FastAPI backend, SQLite persistence, project analysis tools, and an interactive code editor.

The project emphasizes:

- Local AI inference and privacy-conscious operation.
- Project-aware debugging and code analysis.
- Explicit approval before applying AI-generated code changes.
- Safe file editing, backups, and stale-file protection.
- Persistent conversations and configurable model settings.
- A path toward desktop distribution and mobile access.

**Current status:** Core functionality and release-preparation checks have been reported as passing. The packaged macOS application's automatic backend startup remains under investigation. The iPhone companion is planned, not yet implemented.

## Features

### Local AI Assistance

- **Local LLM inference:** Connect to locally installed models through Ollama.
- **Code generation:** Generate code from natural-language instructions.
- **Code explanations:** Understand functions, algorithms, dependencies, and unfamiliar code.
- **Debugging assistance:** Investigate errors, identify potential bugs, and explore possible fixes.
- **Project-aware assistance:** Select a local project and ask questions about its files and implementation.
- **Project analysis:** Inspect project structure and request contextual analysis.
- **Configurable inference:** Select installed models and adjust supported generation settings, including temperature and token limits.

### Code Editing and Safety

- **Interactive code editor:** View and edit supported source files.
- **Save and reset controls:** Save changes or reset the editor to the loaded file contents.
- **Automatic backups:** Preserve previous file contents before supported edits.
- **Stale-file protection:** Detect when a file has changed since it was loaded, helping prevent accidental overwrites.
- **AI-generated change proposals:** Review proposed code modifications before applying them.
- **Patch validation:** Validate proposed changes and restrict file operations to approved project paths.
- **Conversation management:** Create, switch between, rename, and delete conversations.

### Persistence and Privacy

- **SQLite storage:** Persist conversations, messages, and application settings.
- **Local configuration:** Save supported model and inference preferences.
- **Offline-oriented design:** Use local models without a cloud inference dependency when all required components are installed.
- **Filesystem safeguards:** Apply path validation and other protections to supported project operations.
- **User-data migration:** Prepare a dedicated application-data location for packaged macOS use.

Security protections apply to the operations implemented by the application; they should not be interpreted as a guarantee that every possible file operation or AI-generated change is risk-free.

### Platform Development

- **macOS desktop:** A Tauri-based desktop wrapper is being developed around the existing Python backend.
- **iPhone companion:** A native SwiftUI client is planned to access the assistant through a secured local-network connection to the Mac.
- **Future expansion:** Additional development workflows and model integrations may be introduced as the project evolves.

## Technology Stack

| Technology            | Purpose                                          |
| --------------------- | ------------------------------------------------ |
| Python                | Backend logic and AI integration                 |
| FastAPI               | Local HTTP API                                   |
| Ollama                | Local LLM runtime                                |
| Qwen2.5-Coder         | Coding model used in development                 |
| SQLite                | Conversation history and application settings    |
| HTML, CSS, JavaScript | Existing application interface                   |
| Prism.js              | Source-code syntax highlighting                  |
| PyInstaller           | Packaging the Python backend executable          |
| Tauri 2               | macOS desktop application wrapper                |
| Rust                  | Tauri desktop integration and process management |
| Swift and SwiftUI     | Planned native iPhone companion                  |
| Git and GitHub        | Version control and project collaboration        |

The stack may evolve. The desktop packaging and iPhone components should be considered works in progress until their respective builds and acceptance tests pass.

## Requirements

### Development environment

- A compatible Mac.
- Python and `venv`.
- Node.js and npm.
- Rust and the required Apple development tools for Tauri.
- Git.
- [Ollama](https://ollama.com/).
- At least one compatible local language model.

The packaged desktop app may not require a separate Python development environment, but it still depends on the components included in or installed alongside the release.

## Getting Started

### 1. Clone the repository

Replace the placeholders with your GitHub username and repository name.

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

### 2. Install and verify Ollama

Install Ollama from [ollama.com](https://ollama.com/), then check the installation:

```bash
ollama --version
ollama list
```

If Ollama is not running, start it using the normal method for your installation.

### 3. Download a coding model

The model used during development is:

```bash
ollama pull qwen2.5-coder:7b-instruct
```

Model availability, memory usage, and inference speed depend on your hardware and Ollama version. Other compatible models may work, but model compatibility should be verified.

### 4. Verify local inference

Run the model directly:

```bash
ollama run qwen2.5-coder:7b-instruct
```

Try a simple prompt:

```text
Write a Python function that checks whether a string is a palindrome.
Explain the algorithm and provide two test cases.
```

This verifies that the model can respond locally. Exit the interactive session when finished.

### 5. Set up the Python environment

From the application root, create or activate the project's virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the project's dependencies using its dependency manifest, if present. For example, if the repository includes `requirements.txt`:

```bash
python -m pip install -r requirements.txt
```

Use the actual dependency manifest maintained by the repository; do not install an unrelated dependency list.

### 6. Launch the development backend

For the current development layout:

```bash
cd ~/OfflineCodingAssistant
source .venv/bin/activate
uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```

Open the application interface at:

- Application: [http://127.0.0.1:8000/app](http://127.0.0.1:8000/app)
- API documentation: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

This command assumes the repository contains `main.py`, the configured virtual environment, and the required dependencies. Adjust the paths if you cloned the repository elsewhere.

The development server binds to the loopback interface so it is accessible from the local Mac, not directly from other devices on the network.

## Usage

The intended workflow is to launch the application, select an installed model, and submit coding questions or project-specific tasks.

### Example prompts

- "Explain what this Python function does."
- "Find potential bugs in this code and explain why they occur."
- "Write unit tests for this class."
- "Refactor this function for readability without changing its behavior."
- "Explain this error and suggest a minimal fix."
- "Analyze the project structure and identify important dependencies."
- "Review this proposed change before I apply it."

For project operations, select a project directory and use the available project-analysis and question features.

For code modifications, review the proposed changes and approve them explicitly before applying them. Keep version control enabled and review diffs even when automated validation succeeds.

## Configuration and Data

### Application settings

The application supports persisted settings for installed Ollama models and supported generation parameters. The default development configuration uses the Qwen2.5-Coder model, temperature `0.2`, and a maximum output limit of `2048` tokens, subject to the model being installed and the settings implementation in the current version.

### Development data

During development, the SQLite database is stored at:

```text
~/OfflineCodingAssistant/assistant.db
```

### Packaged macOS data

The intended packaged-app location is:

```text
~/Library/Application Support/OfflineCodingAssistant/assistant.db
```

Application logs are intended to be stored at:

```text
~/Library/Logs/OfflineCodingAssistant/
```

The migration from the development database to the packaged-app location must preserve existing data. Never delete the original database to troubleshoot a packaging or migration issue.

These paths describe the current packaging design; verify the actual runtime paths before relying on them for a release.

## Privacy and Security

Privacy is a primary design goal.

- Local Ollama inference can keep prompts and model processing on your own hardware.
- The development server is configured to bind to `127.0.0.1`.
- Project paths are validated by supported project operations.
- Supported editor saves use backups and stale-file checks.
- AI-generated file changes require explicit approval.
- Model downloads, software installation, and updates require internet access.
- Network access and behavior of external integrations must be assessed separately.

**Important:** Running a model locally does not automatically make the entire application secure or fully offline. Validate network behavior, dependencies, file permissions, API exposure, logging, and update mechanisms before distributing the application.

The planned iPhone companion will require additional authentication and network protections before the Mac backend is made accessible over a local network.

## Testing and Release Status

The development workflow includes regression tests and release smoke tests. Previous development and release-preparation checks have been reported as passing; packaged-app acceptance testing is still in progress.

The macOS `.dmg` has been generated and its disk-image checksum has been verified. However, the packaged application has not yet passed the automatic backend startup check.

| Component                                  | Status                               |
| ------------------------------------------ | ------------------------------------ |
| Core assistant functionality               | Implemented                          |
| Local Ollama integration                   | Implemented                          |
| Conversation and settings persistence      | Implemented                          |
| Project-aware analysis and questions       | Implemented                          |
| Editor, backups, and stale-file protection | Implemented                          |
| Approval-based AI code proposals           | Implemented                          |
| Release-preparation checks                 | Reported passing                     |
| macOS `.dmg` generation                    | Generated; launch validation pending |
| Packaged backend auto-start                | Under investigation                  |
| Packaged-app end-to-end testing            | Pending                              |
| Native iPhone companion                    | Planned                              |

A generated disk image is not, by itself, evidence that the packaged app is ready for distribution.

## Roadmap

The following roadmap distinguishes existing functionality from remaining release work.

- [x] Install and configure Ollama.
- [x] Verify local model inference.
- [x] Implement the core assistant interface and backend.
- [x] Add conversation history and persistent settings.
- [x] Implement project-aware analysis and debugging assistance.
- [x] Add editor save controls, backups, and stale-file protection.
- [x] Implement approval-based AI code proposals.
- [x] Complete initial security, regression, and release-preparation checks.
- [x] Generate a macOS disk image.
- [x] Resolve packaged backend startup.
- [x] Verify the interface and all existing features in the packaged app.
- [x] Verify safe migration of existing conversations and settings.
- [x] Test clean installation and offline operation.
- [x] Complete macOS release acceptance testing.
- [x] Evaluate signing and notarization for distribution.
- [ ] Create the native SwiftUI iPhone application.
- [ ] Implement a secured iPhone-to-Mac connection.
- [ ] Test mobile chat, conversation history, and project workflows.
- [ ] Evaluate direct on-device inference as a possible future enhancement.

Roadmap items should only be marked complete when their implementation and acceptance criteria have been verified.

## Contributing

Contributions, suggestions, bug reports, and feature requests are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Implement and test your changes.
4. Commit with a descriptive message.
5. Open a pull request explaining the change and how it was tested.

Before contributing, avoid committing local databases, model weights, virtual environments, credentials, generated executables, or other machine-specific artifacts.

## License

A license has not yet been selected. Until a license is added to the repository, do not assume the project is available for unrestricted reuse, modification, or redistribution.

## Acknowledgments

- [Ollama](https://ollama.com/) for local model execution.
- [LM Studio](https://lmstudio.ai/) as an optional local-model management alternative.
- The developers of Qwen2.5-Coder and other open-source models.
- The Python, FastAPI, SQLite, Tauri, Rust, and SwiftUI communities.

---

**Project Status: In Development**

The goal is to deliver a practical, privacy-focused coding assistant that combines local AI inference, project-aware software engineering tools, safe code-editing workflows, a distributable macOS application, and eventually a native iPhone companion.
