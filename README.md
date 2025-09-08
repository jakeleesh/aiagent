# AI Agent

An LLM-powered command-line program capable of reading, updating, and running Python code using the Gemini API.

AI Agent is able to:
- Accept a task
- Run predefined functions
  - Scan files in a directory
  - Read file
  - Write file
  - Run the Python file
- Agentic loop to complete task

Built a calculator app inside as the AI Agent needs a project to work on. A calculator is one of the easier apps to debug.

Used Gemini because it has a free tier and the model is good.

[uv](https://github.com/astral-sh/uv) used as package manager.

## Installation

Create a .env file in the root of the folder with GEMINI_API_KEY. Get the API Key from [Google AI Studio](https://aistudio.google.com/).

```dotenv
GEMINI_API_KEY=<key>
```

## Usage

It is a CLI tool, give the prompt as an argument.

```bash
uv run main.py "What is 9 + 10?"

# Add verbose flag to make output verbose
uv run main.py "How does my calculator app work?" --verbose