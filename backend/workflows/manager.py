import json
import os

WORKFLOW_FILE = "workflows/workflows.json"

def load_workflows():
    if not os.path.exists(WORKFLOW_FILE):
        return []

    with open(WORKFLOW_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

def save_workflows(workflows):
    with open(WORKFLOW_FILE, "w", encoding="utf-8") as file:
        json.dump(workflows, file, indent=4)

def add_workflow(name, task):
    workflows = load_workflows()

    workflows.append({
        "id": len(workflows) + 1,
        "name": name,
        "task": task
    })

    save_workflows(workflows)

    return workflows

def get_workflow(workflow_id):
    workflows = load_workflows()

    for workflow in workflows:
        if workflow["id"] == workflow_id:
            return workflow

    return None