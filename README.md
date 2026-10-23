# Offline AI Coding Assistant

A privacy-focused AI coding assistant built around local AI inference. The project includes a completed Mac-connected development version and a separate, upcoming native iPhone application designed to run AI models directly on the device without requiring a Mac connection.

The goal is to help developers write, explain, debug, analyze, and improve code while keeping their source code and development environment under their control.

## Project Status

- **Mac version — Completed:** The existing coding assistant uses Ollama, Python/FastAPI, SQLite, project-aware coding tools, and a desktop interface. The Mac-connected version is the foundation of the project.
- **Standalone iPhone version — In development:** A native SwiftUI application designed to run on the iPhone using on-device AI inference, without depending on the Mac application, FastAPI server, or Ollama runtime running on the Mac.

The standalone iPhone version is a separate development phase. Its offline inference, device performance, and feature completeness must be validated before release.

## Overview

The project is designed to provide local AI-assisted software development while minimizing dependence on cloud-based AI services.

It has two distinct application architectures.

### 1. Mac Version — Completed

The Mac version provides AI-assisted software development through locally running language models and a Python backend.

Key technologies and capabilities include:

- Ollama for local language model inference.
- Python and FastAPI for backend services.
- SQLite for persistent conversations and application settings.
- Project-aware code analysis and debugging.
- Interactive code editing and syntax highlighting.
- AI-generated code proposals with explicit approval.
- File backups and stale-file protection.
- Configurable model settings and conversation management.
- Desktop application packaging using Tauri.

The Mac version uses the Mac's local resources to run supported language models and provide coding assistance.

### 2. Standalone iPhone Version — In Development

The next phase is a native iOS application built with Swift and SwiftUI.

The objective is to run the coding assistant directly on a compatible iPhone, using on-device model inference rather than relying on the Mac's backend.

The intended capabilities include:

- Native iOS interface.
- On-device AI inference.
- Offline coding assistance after the required application and model files have been installed.
- Code explanations, generation, and debugging assistance as supported by the implementation.
- Local conversation history and settings.
- Independent operation without a connection to the Mac.
- No requirement for a running Mac, FastAPI server, or Mac-hosted Ollama service during normal offline use.

These are development objectives, not a claim that every feature has already been implemented or tested.

Initial installation, application signing, software updates, and downloading model files may require internet access. The goal is for supported AI operations to work without a network connection once setup is complete.

## Features

### Mac Version

#### Local AI Assistance

- Local language model inference through Ollama.
- Code generation from natural-language instructions.
- Code explanations and algorithm analysis.
- Debugging assistance and potential bug identification.
- Project-aware analysis and questions.
- Configurable installed models and generation settings.

#### Code Editing and Safety

- Interactive code editor.
- Save and reset controls.
- Automatic backups before supported edits.
- Stale-file protection to help prevent accidental overwrites.
- AI-generated code proposals requiring explicit approval.
- Patch validation and approved-project-path restrictions.
- Create, switch between, rename, and delete conversations.

#### Persistence and Privacy

- SQLite conversation and settings storage.
- Persistent model configuration.
- Local inference without a cloud inference dependency when all required components are installed.
- Filesystem safeguards for supported project operations.
- Application-data migration support for packaged Mac use.

### Standalone iPhone Version

The iPhone application will be developed and validated independently of the Mac version.

The primary objectives are:

- Native SwiftUI application running on iOS.
- AI inference performed locally on the iPhone.
- Offline operation without connecting to the Mac.
- Model and memory usage appropriate for the target device.
- Local storage for supported conversations and settings.
- A practical mobile coding-assistant interface.

Actual model compatibility, available context length, generation speed, storage requirements, and supported features will depend on the implementation and the iPhone hardware.

## Technology Stack

| Technology                  | Purpose                                                                                |
| --------------------------- | -------------------------------------------------------------------------------------- |
| Python                      | Mac backend logic and AI integration                                                   |
| FastAPI                     | Mac application HTTP API                                                               |
| Ollama                      | Local model runtime for the Mac version                                                |
| Qwen2.5-Coder               | Coding model used during Mac development                                               |
| SQLite                      | Conversation history and application settings                                          |
| HTML, CSS, JavaScript       | Existing Mac application interface                                                     |
| Prism.js                    | Source-code syntax highlighting                                                        |
| PyInstaller                 | Packaging the Python backend executable                                                |
| Tauri 2                     | Mac desktop application wrapper                                                        |
| Rust                        | Desktop integration and process management                                             |
| Swift                       | Native iPhone application development                                                  |
| SwiftUI                     | iPhone user interface                                                                  |
| On-device inference runtime | Intended local AI execution on iPhone; runtime and model compatibility to be validated |
| Git and GitHub              | Version control and project collaboration                                              |

The Mac and iPhone applications have different runtime requirements. The standalone iPhone version is not intended to depend on the Mac's Ollama installation or FastAPI backend.

## Requirements

### Mac Version

- Compatible Mac.
- Python and `venv`.
- Node.js and npm.
- Rust and the required Apple development tools for Tauri.
- Git.
- [Ollama](https://ollama.com/).
- At least one compatible local language model.

### Standalone iPhone Version

- Mac with Xcode and the iOS SDK for development and signing.
- Compatible iPhone.
- Sufficient available storage for the app and its supported model.
- An on-device inference implementation compatible with the selected model and target device.

The iPhone app is intended to run supported inference locally after installation and model setup. Model selection and hardware requirements must be validated as development progresses.

## Getting Started

### Mac Version

#### 1. Clone the repository

```bash
git clone https://github.com/jrog97/AI_Chat.git
cd AI_Chat
```

#### 2. Install and verify Ollama

Install Ollama from [ollama.com](https://ollama.com/).

```bash
ollama --version
ollama list
```

#### 3. Download a coding model

The model used during development is:

```bash
ollama pull qwen2.5-coder:7b-instruct
```

Model availability, memory consumption, and inference speed depend on the Mac hardware and Ollama version. Other compatible models may be used after testing.

#### 4. Verify local inference

```bash
ollama run qwen2.5-coder:7b-instruct
```

Example prompt:

```text
Write a Python function that checks whether a string is a palindrome.
Explain the algorithm and provide two test cases.
```

#### 5. Set up the Python environment

From the application root:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies using the manifest maintained by the project. If the repository includes `requirements.txt`:

```bash
python -m pip install -r requirements.txt
```

#### 6. Launch the development backend

For the existing development layout:

```bash
cd ~/OfflineCodingAssistant
source .venv/bin/activate
uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```

Development endpoints:

- Application: [http://127.0.0.1:8000/app](http://127.0.0.1:8000/app)
- API documentation: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

These commands assume the project files and dependencies are present at the specified paths. Adjust them to match the actual local checkout.

The development server binds to the Mac's loopback interface. This is appropriate for local development and does not make the service directly accessible to other devices on the network.

### Standalone iPhone Version

The iPhone application is the next development phase.

1. Open the native iOS project in Xcode.
2. Select the appropriate iPhone simulator or connected physical device.
3. Configure the app's signing settings for development.
4. Build and run the application.
5. Implement and validate the compatible on-device inference runtime and model.
6. Install the required model files and verify offline operation.
7. Test storage, performance, conversation persistence, and supported coding workflows.

The exact build instructions, dependencies, model-download procedure, and inference implementation will be documented once they are established in the iOS project.

The target is a standalone iPhone application that does not require a Mac connection during normal offline use.

## Usage

### Mac Version

Launch the Mac application or development backend, select an installed Ollama model, and submit coding questions or project-specific tasks.

Example prompts:

- Explain what this Python function does.
- Find potential bugs in this code and explain why they occur.
- Write unit tests for this class.
- Refactor this function without changing its behavior.
- Explain this error and suggest a minimal fix.
- Analyze the project structure and identify important dependencies.
- Review this proposed change before I apply it.

For file modifications, review the proposed changes and approve them explicitly. Continue to use version control and review diffs even when automated validation succeeds.

### Standalone iPhone Version

The intended workflow is to open the native iPhone app, select or configure an available on-device model if supported, and submit coding questions directly from the device.

The app must be able to perform its supported offline inference without connecting to the Mac.

Mobile-specific features and limitations will be documented as they are implemented and tested.

## Configuration and Data

### Mac Application Settings

The Mac version supports persistent settings for installed Ollama models and supported generation parameters.

The default development configuration uses:

- Model: Qwen2.5-Coder.
- Temperature: `0.2`.
- Maximum output: `2048` tokens.

These defaults are subject to the model being installed and the current settings implementation.

### Mac Development Data

The development SQLite database is stored at:

```text
~/OfflineCodingAssistant/assistant.db
```

The intended packaged application-data location is:

```text
~/Library/Application Support/OfflineCodingAssistant/assistant.db
```

Application logs are intended to be stored at:

```text
~/Library/Logs/OfflineCodingAssistant/
```

Verify actual runtime paths before relying on them for a release. Preserve the original database when troubleshooting migration issues.

### iPhone Data

The standalone iPhone app will require its own local storage strategy for supported conversations, settings, and other app data.

Its model files and application data must be managed within iOS storage constraints. Data synchronization between Mac and iPhone is not a requirement for the standalone offline architecture.

## Privacy and Security

Privacy is a primary design goal, but each application must be assessed independently.

### Mac

- Ollama can perform inference locally on the Mac.
- The development server binds to `127.0.0.1`.
- Supported project operations validate file paths.
- Supported editor operations use backups and stale-file checks.
- AI-generated file changes require explicit approval.
- Model downloads, software installation, and updates may require internet access.

### iPhone

- The target architecture uses on-device inference.
- Normal supported AI operations should not require a connection to the Mac.
- Model downloads and application updates may require internet access.
- Local data storage, permissions, model loading, and any network behavior must be tested.

Local inference does not automatically guarantee that every component is secure or that the application is fully offline. Validate dependencies, filesystem access, network behavior, logging, and update mechanisms before distribution.

## Testing and Release Status

### Mac Version

The Mac version's core functionality and initial release-preparation checks have been reported as passing. However, the packaged application's automatic backend startup and end-to-end acceptance have been identified as outstanding verification items.

| Component                                  | Status                               |
| ------------------------------------------ | ------------------------------------ |
| Core assistant functionality               | Implemented                          |
| Local Ollama integration                   | Implemented                          |
| Conversation and settings persistence      | Implemented                          |
| Project-aware analysis and questions       | Implemented                          |
| Editor, backups, and stale-file protection | Implemented                          |
| Approval-based AI code proposals           | Implemented                          |
| Initial security and regression checks     | Reported passing                     |
| macOS `.dmg` generation                    | Generated; launch validation pending |
| Packaged backend auto-start                | Requires verification                |
| Packaged-app end-to-end acceptance         | Requires verification                |

### Standalone iPhone Version

| Component                                  | Status                         |
| ------------------------------------------ | ------------------------------ |
| Native SwiftUI project                     | In development                 |
| Standalone architecture                    | Target defined                 |
| On-device inference                        | To be implemented and verified |
| Offline operation without Mac              | Acceptance testing pending     |
| Model storage and device-memory validation | Pending                        |
| Mobile conversation persistence            | To be validated                |
| iPhone release readiness                   | Not yet established            |

A generated disk image or a successful development build alone does not establish release readiness. Each version needs its own acceptance tests.

## Roadmap

### Mac Version

- [x] Implement the core assistant interface and backend.
- [x] Integrate local Ollama inference.
- [x] Add conversation history and persistent settings.
- [x] Implement project-aware analysis and debugging assistance.
- [x] Add editor save controls, backups, and stale-file protection.
- [x] Implement approval-based AI code proposals.
- [x] Complete initial security, regression, and release-preparation checks.
- [x] Generate a macOS disk image.
- [x] Verify packaged backend startup.
- [x] Complete packaged-app end-to-end acceptance testing.

### Standalone iPhone Version

- [x] Establish the native SwiftUI iPhone project.
- [ ] Implement on-device model inference.
- [ ] Validate model compatibility and device resource requirements.
- [ ] Build and install on the target iPhone.
- [ ] Verify supported AI features with network access disabled.
- [ ] Test conversation history and settings persistence.
- [ ] Validate model storage, memory consumption, and inference performance.
- [ ] Complete iPhone-specific regression and offline acceptance tests.
- [ ] Prepare the app for distribution.

Roadmap items should only be marked complete after their implementation and acceptance criteria have been verified.

## Contributing

Contributions, suggestions, bug reports, and feature requests are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Implement and test your changes.
4. Commit with a descriptive message.
5. Open a pull request explaining the change and how it was tested.

Avoid committing local databases, model weights, virtual environments, credentials, generated executables, or other machine-specific artifacts.

## License

A license has not yet been selected. Until a license is added to the repository, do not assume the project is available for unrestricted reuse, modification, or redistribution.

## Acknowledgments

- [Ollama](https://ollama.com/) for local model execution.
- [LM Studio](https://lmstudio.ai/) as an optional local-model management alternative.
- The developers of Qwen2.5-Coder and other open-source models.
- The Python, FastAPI, SQLite, Tauri, Rust, Swift, and SwiftUI communities.

---

**Project Status: Mac Version Completed; Standalone iPhone Version in Development**

The long-term goal is to provide a practical, privacy-focused coding assistant across Mac and iPhone: a local-model Mac application and a native iPhone application capable of running supported AI coding workflows directly on the device without requiring a Mac connection.
