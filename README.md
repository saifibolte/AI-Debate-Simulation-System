# AI Debate Simulation System

This project simulates a structured **8-round debate** between two AI agents with memory, turn control, and an automated judge.  
It is built using **LangGraph**, **Graphviz**, and **Ollama** (for running local LLMs).

---

## Features
- **Two alternating agents** (AgentA vs AgentB) with profession-like personas.
- **8 fixed rounds** (4 arguments each).
- **Memory node** that prevents repetition and ensures logical flow.
- **Judge node** that reviews the debate and declares a winner with justification.
- **DAG diagram** showing the debate workflow.
- **Logging** of all rounds, memory updates, and final judgment to `debate_log.txt`.
- **CLI interface** for entering a topic at runtime.

---

## Installation

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

## Usage

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

## Example Output

```text
Enter topic for debate: Should homework be banned?

AgentA: Homework should be banned because it is a waste of time and effort, and can lead to procrastination and poor academic performance.
AgentB: Banning homework would have a detrimental impact on students' learning and academic success. It would deprive them of the valuable opportunity to practice and apply their knowledge in a structured learning environment. Homework also helps students develop time management skills, independence, and a love of learning.

[Round 2]
AgentA: Homework should be banned as it creates a significant burden on students' time and can hinder their cognitive development.
AgentB: While a complete ban on homework may be necessary to combat lazy students, it would be an unfair punishment for those who diligently complete their assignments and demonstrate their learning.
...
[Round 8]
AgentA: Homework is a crucial educational tool that fosters independent learning and critical thinking skills. Banning homework would hinder a student's progress and limit their opportunities to develop vital life skills.
AgentB: While some argue that homework is unnecessary or even detrimental to students' learning, it is a valuable tool for developing critical thinking, independent problem-solving, and time management skills. Homework allows students to practice and apply concepts learned in the classroom in a structured and independent setting, thus promoting deeper understanding and retention. Additionally, homework can provide valuable parental insights into their children's academic progress and a chance to encourage them to stay engaged with learning outside of school hours.

[Judge Decision]
Winner: AgentB
Reason: Homework can be a valuable tool for learning and development, but it can also be a burden for students and families. When homework is not carefully managed, it can lead to increased stress, anxiety and burnout, which can negatively impact academic performance. Additionally, it can limit opportunities for social interaction and other extracurricular activities.
DAG written to dag.svg
Full debate log saved to debate_log.txt
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

## Project Structure

```
├── main.py          # CLI entrypoint & debate loop
├── graph.py         # Graphviz DAG builder
├── nodes.py         # DebateMemory for structured history
├── models.py        # Wrapper for Ollama LLM calls
├── requirements.txt # Dependencies
└── README.md        # Documentation
```

