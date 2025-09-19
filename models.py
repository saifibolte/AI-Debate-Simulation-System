import subprocess

def run_model(model: str, prompt: str) -> str:
    try:
        # Correct Ollama command (no --prompt)
        result = subprocess.run(
            ["ollama", "run", model, prompt],
            capture_output=True,
            text=True,
            check=True
        )
        output = result.stdout.strip()
        if not output:
            return "[MODEL ERROR] No response from model."
        return output
    except subprocess.CalledProcessError as e:
        return f"[MODEL ERROR] {e.stderr.strip() or str(e)}"
    except FileNotFoundError:
        return "[MODEL ERROR] Ollama is not installed or not in PATH."
    except Exception as e:
        return f"[MODEL ERROR] Unexpected error: {str(e)}"
