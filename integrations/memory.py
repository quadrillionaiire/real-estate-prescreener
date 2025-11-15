import json, os

MEM_PATH = "data/conversation_history.json"

def append_history(session_id, role, text):
    history = {}
    if os.path.exists(MEM_PATH):
        with open(MEM_PATH, "r") as f:
            history = json.load(f)
    history.setdefault(session_id, []).append({"role": role, "text": text})
    with open(MEM_PATH, "w") as f:
        json.dump(history, f, indent=2)
