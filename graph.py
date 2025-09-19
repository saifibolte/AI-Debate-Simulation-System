from graphviz import Digraph

class DebateGraph:
    def __init__(self):
        self.graph = Digraph(comment="AI Debate Graph", format="svg")
        self.graph.attr(rankdir="LR")  # left-to-right layout
        self.nodes_added = set()

        # Core workflow nodes
        self.add_node("UserInput", "User Input")
        self.add_node("AgentA", "Agent A")
        self.add_node("AgentB", "Agent B")
        self.add_node("Memory", "Memory Node")
        self.add_node("Judge", "Judge Node")

        # Base edges (workflow order)
        self.graph.edge("UserInput", "AgentA")
        self.graph.edge("UserInput", "AgentB")
        self.graph.edge("AgentA", "Memory")
        self.graph.edge("AgentB", "Memory")
        self.graph.edge("Memory", "Judge")

    def add_node(self, node_id: str, label: str):
        """Add a node if not already present."""
        if node_id not in self.nodes_added:
            self.graph.node(node_id, label)
            self.nodes_added.add(node_id)

    def add_argument(self, agent: str, round_num: int, text: str):
        """Add an argument node for a given round."""
        arg_id = f"{agent}_R{round_num}"
        short_text = text[:30] + ("..." if len(text) > 30 else "")

        self.add_node(arg_id, f"{agent} (R{round_num})\n{short_text}")
        self.graph.edge(agent, arg_id)
        self.graph.edge(arg_id, "Memory")

    def generate_dag(self, path: str = "dag.svg"):
        """Render the DAG to file (requires Graphviz installed)."""
        self.graph.render(filename=path, cleanup=True)
