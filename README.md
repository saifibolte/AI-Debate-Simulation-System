# AI Debate Simulation System

This project is a command-line interface (CLI) tool that simulates a structured debate between two AI agents on a given topic. The system enforces turn-taking, tracks the debate history, prevents argument repetition, and concludes with a verdict from an AI judge. The entire debate flow is visualized as a Directed Acyclic Graph (DAG).

This implementation uses local language models via [Ollama](https://ollama.com/) and visualizes the debate structure using [Graphviz](https://graphviz.org/).

## Features

-   **Dynamic Topic Input**: The debate topic is provided by the user at runtime.
-   **Two-Agent Debate**: `AgentA` argues FOR the topic, and `AgentB` argues AGAINST it.
-   **Structured Rounds**: The debate is fixed to 8 rounds, with each agent making 4 arguments.
-   **Memory & Repetition Check**: A memory node stores all arguments and uses string similarity to prevent agents from repeating themselves.
-   **AI Judge**: A third AI agent reviews the arguments and declares a winner with a justification.
-   **Automated Logging**: A complete transcript of the debate is saved to `debate_log.txt`.
-   **DAG Visualization**: The logical flow of the debate is rendered as an SVG image (`dag.svg`).

## How It Works

The system follows a clear, graph-inspired workflow:

1.  **Initialization**: The `main.py` script prompts the user for a debate topic.
2.  **Debate Loop**: The script iterates through 8 rounds. In each round:
    -   `AgentA` and `AgentB` are called sequentially.
    -   The `models.py` module sends a formatted prompt to a local LLM (e.g., `gemma:2b`) via Ollama.
    -   The `nodes.py` module's `DebateMemory` class checks if the generated argument is too similar to previous ones. If it is, the turn is skipped.
    -   Valid arguments are added to memory.
    -   The `graph.py` module adds a new node to the DAG for each valid argument.
3.  **Judgment**: After 8 rounds, the Judge agent is prompted with the debate context to provide a verdict.
4.  **Output Generation**: The final DAG is rendered to `dag.svg`, and the complete session log is written to `debate_log.txt`.

## Setup and Installation

### Prerequisites

-   Python 3.7+
-   [Ollama](https://ollama.com/): You must have Ollama installed and running.
-   [Graphviz](https://graphviz.org/download/): The Graphviz system package must be installed to render the DAG.
    -   **On macOS (using Homebrew):** `brew install graphviz`
    -   **On Debian/Ubuntu:** `sudo apt-get install graphviz`
    -   **On Windows:** Download from the official site and add it to your system's PATH.

### Installation Steps

1.  **Clone the repository:**
    ```sh
    git clone <your-repo-url>
    cd <your-repo-directory>
    ```

2.  **Install Python dependencies:**
    *(Note: The provided `requirements.txt` was adjusted to fit the actual code.)*
    ```sh
    pip install graphviz
    ```

3.  **Pull the LLM model using Ollama:**
    ```sh
    ollama pull gemma:2b
    ```

## Usage

Run the main script from your terminal.

**Interactive Mode:**
The script will prompt you to enter a topic.

```sh
python main.py
