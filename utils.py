
import json
import os

DATA_PATH = os.path.join("data", "tasks.json")

def save_tasks_to_file(tasks):
    os.makedirs("data", exist_ok=True)
    with open(DATA_PATH, "w") as f:
        json.dump(tasks, f, indent=4)

def load_tasks_from_file():
    if not os.path.exists(DATA_PATH):
        return []
    with open(DATA_PATH, "r") as f:
        return json.load(f)
