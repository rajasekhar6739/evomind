def plan_task(user_request: str):
    request = user_request.lower()

    if any(word in request for word in ["research", "latest", "find", "analyze"]):
        agent = "research"

    elif any(word in request for word in ["write", "summarize", "report", "create"]):
        agent = "writer"

    elif any(word in request for word in ["automate", "schedule", "workflow", "repeat"]):
        agent = "automation"

    else:
        agent = "writer"

    return {
        "agent": agent,
        "task": user_request
    }