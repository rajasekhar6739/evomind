import json
import os

FEEDBACK_FILE = "evolution/feedback.json"


def load_feedback():
    if not os.path.exists(FEEDBACK_FILE):
        return []

    with open(FEEDBACK_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_feedback(data):
    with open(FEEDBACK_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def add_feedback(workflow, rating, comment):
    feedback = load_feedback()

    feedback.append({
        "workflow": workflow,
        "rating": rating,
        "comment": comment
    })

    save_feedback(feedback)

    return feedback


def generate_suggestions():
    feedback = load_feedback()

    suggestions = []

    for item in feedback:

        text = item["comment"].lower()

        if "short" in text:
            suggestions.append("Use shorter reports by default.")

        if "enterprise" in text:
            suggestions.append("Focus future reports on enterprise AI.")

        if "detail" in text:
            suggestions.append("Generate more detailed summaries.")

    return list(set(suggestions))