import argparse
import os
from graph import DebateGraph
from nodes import DebateMemory
from models import run_model  # your existing wrapper for gemma models

LOG_FILE = "debate_log.txt"


def log_output(text, log_list=None):
    """Print and append to log"""
    print(text)
    if log_list is not None:
        log_list.append(text)


def run_debate(topic: str):
    memory = DebateMemory()
    graph = DebateGraph()
    debate_log = []

    # ---- Agent prompts ----
    agent_a_prompt = (
        f"Resolution: '{topic}'.\n"
        "You are AgentA. Argue FOR the resolution.\n"
        "Respond with exactly ONE persuasive sentence only.\n"
        "Do not say 'here is', 'summary', or introduce the argument.\n"
        "Do not use bullet points, headings, or meta-commentary.\n"
        "Write naturally as a confident human debater."
    )

    agent_b_prompt = (
        f"Resolution: '{topic}'.\n"
        "You are AgentB. Argue AGAINST the resolution.\n"
        "Respond with exactly ONE persuasive sentence only.\n"
        "Do not say 'here is', 'summary', or introduce the argument.\n"
        "Do not use bullet points, headings, or meta-commentary.\n"
        "Write naturally as a confident human debater."
    )

    judge_prompt = (
        f"You are the Judge of this debate on '{topic}'.\n"
        "Decide who won the debate based on the arguments presented by AgentA and AgentB.\n"
        "Output MUST be in this exact format:\n\n"
        "Winner: <AgentA or AgentB>\n"
        "Reason: <brief 1-2 sentence explanation>\n\n"
        "Do not add extra text or disclaimers."
    )

    agents = [
        ("AgentA", "gemma:2b", agent_a_prompt),
        ("AgentB", "gemma:2b", agent_b_prompt)
    ]

    max_rounds = 8  # total rounds (adjustable)

    # ---- Debate rounds ----
    for r in range(1, max_rounds + 1):
        log_output(f"\n[Round {r}]", debate_log)

        for agent_name, model, prompt in agents:
            try:
                arg_text = run_model(model, prompt).strip()

                # Skip if repeated/fuzzy similar
                if memory.is_repeated(agent_name, arg_text):
                    log_output(f"{agent_name} repeated an argument. Skipping...", debate_log)
                    continue

                memory.add_argument(agent_name, r, arg_text)
                graph.add_argument(agent_name, r, arg_text)
                log_output(f"{agent_name}: {arg_text}", debate_log)

            except Exception as e:
                log_output(f"{agent_name}: [MODEL ERROR] {str(e)}", debate_log)

    # ---- Judge decision ----
    try:
        judge_text = run_model("gemma:2b", judge_prompt).strip()
        log_output("\n[Judge Decision]", debate_log)
        log_output(judge_text, debate_log)
    except Exception as e:
        log_output(f"[Judge Decision] [MODEL ERROR] {str(e)}", debate_log)

    # ---- Save DAG and log ----
    graph.generate_dag("dag.svg")
    log_output("DAG written to dag.svg", debate_log)

    with open(LOG_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(debate_log))
    log_output(f"Full debate log saved to {LOG_FILE}", debate_log)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", type=str, help="Debate topic", required=False)
    args = parser.parse_args()

    if not args.topic:
        args.topic = input("Enter topic for debate: ")

    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)

    run_debate(args.topic)
