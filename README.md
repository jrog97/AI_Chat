# Offline AI Coding Assistant

A privacy-focused AI coding assistant powered by locally running large language models (LLMs). Designed to help developers write, explain, debug, and improve code without depending on cloud-based AI services.

## Overview

The Offline AI Coding Assistant aims to bring AI-powered development tools directly to your local machine. By running language models locally through Ollama, the project prioritizes privacy, local control, and accessibility.

The long-term goal is to build a standalone desktop application for macOS, with a potential mobile companion app.

## Features

- **Local AI Inference:** Run supported language models on your own hardware through Ollama.
- **Code Generation:** Generate code from natural-language instructions.
- **Code Explanations:** Understand functions, algorithms, and unfamiliar code.
- **Debugging Assistance:** Investigate errors and explore potential fixes.
- **Privacy-Focused Development:** Keep prompts and source code local when using local models and local-only integrations.
- **Offline Operation:** Work without an internet connection after downloading the required models and dependencies, provided all required components are available locally.
- **Developer-Focused Workflow:** Build toward a streamlined experience for everyday coding tasks.
- **Desktop Application:** Planned standalone macOS application.
- **Mobile Companion:** Planned mobile application to extend access to the assistant.

## Technology Stack

| Technology            | Purpose                                                    |
| --------------------- | ---------------------------------------------------------- |
| Ollama                | Local LLM runtime                                          |
| Large Language Models | Code generation, explanations, and debugging               |
| macOS                 | Primary development platform                               |
| LM Studio             | Optional alternative for managing and running local models |
| Git and GitHub        | Version control and project collaboration                  |

*The technology list may evolve as development progresses. Features marked as planned are not necessarily implemented yet.*

## Getting Started

### Prerequisites

Before running the assistant, make sure you have:

- A compatible macOS computer.
- [Ollama](https://ollama.com/) installed.
- Git installed.
- At least one compatible language model downloaded.
- Any additional dependencies required by the current version of the application.

### 1. Clone the Repository

Replace `YOUR_USERNAME` with your GitHub username and `YOUR_REPOSITORY` with your repository name.

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

### 2. Verify Ollama

Check that Ollama is installed:

```bash
ollama --version
```

Check which models are available locally:

```bash
ollama list
```

### 3. Download a Coding Model

For example, download a model supported by your hardware:

```bash
ollama pull qwen2.5-coder:7b
```

Model availability and performance depend on your hardware, memory, and Ollama version. You can substitute another compatible coding model.

### 4. Run the Model

Start an interactive session:

```bash
ollama run qwen2.5-coder:7b
```

This verifies that the model can run locally. The final assistant application may use a different command or interface once its application components are complete.

## Usage

The intended workflow is to launch the assistant, select an available local model, and submit coding questions or tasks.

### Example Prompts

- "Explain what this Python function does."
- "Find potential bugs in this code."
- "Write unit tests for this class."
- "Refactor this function for readability."
- "Explain this error and suggest possible fixes."
- "Help me understand this algorithm."

Specific capabilities depend on the model and the features implemented in the application.

## Privacy and Security

Privacy is a core design goal.

- Local models can process prompts without sending them to a cloud-based AI provider.
- Downloading models and application updates requires internet access.
- External integrations, telemetry, and other network-dependent features must be evaluated separately.
- Never share API keys, passwords, access tokens, or other sensitive information in prompts or source control.
- Use a `.gitignore` file to exclude environment files, secrets, local configuration, and generated artifacts where appropriate.

**Important:** Offline operation and privacy should be verified for the complete application, not assumed solely because Ollama runs locally.

## Project Roadmap

The following roadmap describes the intended direction of development. Items should be marked complete only after implementation and testing.

- [x] Install and configure Ollama.
- [x] Verify that a local language model can run.
- [x] Complete the assistant's core functionality.
- [x] Improve code generation and debugging workflows.
- [x] Implement a polished user interface.
- [ ] Add error handling and automated tests.
- [ ] Package the macOS application as a distributable `.dmg`.
- [ ] Test installation and operation without an internet connection.
- [ ] Explore a mobile companion application.
- [ ] Write end-user installation and troubleshooting documentation.

## Contributing

Contributions, suggestions, bug reports, and feature requests are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Implement and test your changes.
4. Commit your work with a descriptive message.
5. Open a pull request describing your changes.

## License

A license has not yet been selected. Until a license is added to the repository, do not assume that the project is available for unrestricted reuse or redistribution.

## Acknowledgments

- [Ollama](https://ollama.com/) for local model execution.
- [LM Studio](https://lmstudio.ai/) for local model management.
- The open-source model developers and contributors whose work makes local AI development possible.

---

**Project Status:** In Development.

The goal is to create a practical, privacy-focused coding assistant that brings locally powered AI development capabilities to everyday software engineering workflows.