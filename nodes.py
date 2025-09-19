import difflib

class DebateMemory:
    def __init__(self):
        self.arguments = []      # list of dicts: {"agent", "round", "text"}
        self.arg_texts = []      # list of all previous argument texts (lowercased)

    def add_argument(self, agent_name: str, round_num: int, text: str):
        """Add a new argument, avoid duplicates (even paraphrased)"""
        text_clean = text.strip()

        # Handle model errors gracefully
        if text_clean.startswith("[MODEL ERROR]"):
            text_clean = f"{text_clean} (round {round_num})"

        # Check similarity to previous arguments (avoid exact/very similar repeats)
        for prev_text in self.arg_texts:
            similarity = difflib.SequenceMatcher(None, prev_text, text_clean.lower()).ratio()
            if similarity > 0.85:  # 85% similar = consider repeated
                raise ValueError("Argument repeated or too similar to previous.")

        self.arg_texts.append(text_clean.lower())
        self.arguments.append({
            "agent": agent_name,
            "round": round_num,
            "text": text_clean
        })

    def is_repeated(self, agent_name: str, text: str) -> bool:
        """Check if text is repeated (for CLI checks)"""
        text_clean = text.strip().lower()
        for prev_text in self.arg_texts:
            similarity = difflib.SequenceMatcher(None, prev_text, text_clean).ratio()
            if similarity > 0.85:
                return True
        return False
