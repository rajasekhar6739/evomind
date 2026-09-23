import json
import os

MEMORY_FILE = "memory/user_memory.json"

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {}

    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_memory(data):
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def update_preference(key, value):
    memory = load_memory()
    memory[key] = value
    save_memory(memory)
    return memory

def get_preferences():
    return load_memory()