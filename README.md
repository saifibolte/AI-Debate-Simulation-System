# 🗣️ AI Debate Simulation with LangGraph

This project simulates a structured **8-round debate** between two AI agents with memory, turn control, and an automated judge.  
It is built using **LangGraph**, **Graphviz**, and **Ollama** (for running local LLMs).

---

## ✨ Features
- **Two alternating agents** (AgentA vs AgentB) with profession-like personas.
- **8 fixed rounds** (4 arguments each).
- **Memory node** that prevents repetition and ensures logical flow.
- **Judge node** that reviews the debate and declares a winner with justification.
- **DAG diagram** showing the debate workflow.
- **Logging** of all rounds, memory updates, and final judgment to `debate_log.txt`.
- **CLI interface** for entering a topic at runtime.

---

## 🛠️ Installation

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/debate-simulation.git
cd debate-simulation
```

### 2. Install dependencies
Make sure you have **Python 3.9+** and **pip** installed.

```bash
pip install -r requirements.txt
```

### 3. Install Graphviz
Required for DAG generation.

- **Linux (Debian/Ubuntu)**:
  ```bash
  sudo apt-get install graphviz
  ```
- **macOS (Homebrew)**:
  ```bash
  brew install graphviz
  ```
- **Windows**: Download installer from [Graphviz.org](https://graphviz.org/download/).

### 4. Install Ollama
Download Ollama from: [https://ollama.ai](https://ollama.ai)  
Pull the required model (Gemma 2B is used by default):

```bash
ollama pull gemma:2b
```

---

## ▶️ Usage

Run the debate system from the CLI:

```bash
python main.py --topic "Should AI be regulated like medicine?"
```

or interactively:

```bash
python main.py
Enter topic for debate: Should AI be regulated like medicine?
```

---

## 📊 Example Output

```text
[Round 1]
AgentA: AI must be regulated to protect human lives in high-risk applications.
[Round 2]
AgentB: Over-regulation could hinder innovation and delay critical benefits.
...
[Round 8]
AgentB: History shows overregulation often delays societal evolution.

[Judge Decision]
Winner: AgentA
Reason: Presented more risk-aware and safety-aligned arguments.
```

The full debate is saved to:
```
debate_log.txt
```

The DAG diagram is generated as:
```
dag.svg
```

---

## 🧩 Project Structure

```
├── main.py          # CLI entrypoint & debate loop
├── graph.py         # Graphviz DAG builder
├── nodes.py         # DebateMemory for structured history
├── models.py        # Wrapper for Ollama LLM calls
├── requirements.txt # Dependencies
└── README.md        # Documentation
```

---

## 📐 DAG Workflow

```
UserInput ──▶ AgentA ──▶ Memory ──▶ Judge
          └▶ AgentB ──▶ Memory ──▶ Judge
```

Each agent → Memory → Judge ensures structured debate and final evaluation.

---

## 📜 Deliverables
- **Source Code**: Modular nodes & debate logic
- **README.md**: Setup & instructions (this file)
- **DAG Diagram**: `dag.svg` generated at runtime
- **Debate Log**: `debate_log.txt` (full transcript & verdict)
- **Demo Video**: 2–4 min walkthrough (script below)

---
