# Real-Time Speech-to-Text (Local Whisper Backend)

An optimized, lightweight Python CLI application that captures live microphone streams and transcribes them in real-time using a localized Whisper backbone.

## 🧠 Architectural Overview
* **Orchestration Layer:** Powered by the `RealtimeSTT` Python library to open continuous hardware audio streams and handle automatic Voice Activity Detection (VAD).
* **AI Processing Engine:** Transcriptions are executed via `faster-whisper`, a highly optimized inference framework for OpenAI's Whisper architectures.
* **Hardware Optimization:** Explicitly configured to bypass NVIDIA CUDA requirements. It executes entirely on standard **CPUs** using **INT8 quantization** to safely process high-accuracy text loops within a tiny memory footprint (~145 MB).

## 💾 Local Model Caching
The application operates entirely **offline** after its initial boot. On the first run, the engine fetches the Whisper `base` weights from Hugging Face and saves them to your global hardware storage cache under:
`%USERPROFILE%\.cache\huggingface\hub`

On subsequent runs, it copies the binary model weights straight from your local storage directly into system RAM, completely bypassing network dependency.

## 🚀 Local Setup Instructions

This project uses `uv` for lightning-fast, reproducible dependency management and environment isolation.

### 1. Prerequisites
Ensure you have the `uv` package manager installed globally on your machine:
```bash
powershell -ExecutionPolicy ByPass -c "irm [https://astral.sh/uv/install.ps1](https://astral.sh/uv/install.ps1) | iex"
```

### 2. Project Initialization
EClone the repository and navigate to the project root, then set up the isolated environment:
```bash
# 1. Pin the Python version for compatibility
uv python pin 3.11

# 2. Create the virtual environment
uv venv

# 3. Activate the environment (Windows)
.venv\Scripts\activate
```

### 3. Install Dependencies
Install the core STT library and the optimized whisper engine. We use a specific installation string to ensure the optional faster-whisper components are included:
```bash
uv pip install faster-whisper "RealtimeSTT[faster-whisper]"
```

### 4. Running the Application
Once the environment is active and dependencies are installed, start the real-time transcription loop:

```bash
python main.py
```

### 🛠️ Troubleshooting
ModuleNotFoundError: Ensure you ran the uv pip install command above while the .venv was active.

RuntimeError (Multiprocessing): On Windows, the application code must be wrapped in an if __name__ == "__main__": block to prevent recursive process loops.

Microphone Access: Ensure your default system microphone is correctly configured in Windows Privacy Settings.