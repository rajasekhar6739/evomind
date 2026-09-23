from tools.registry import execute_tool
from services.ai import ask_ai

from agents.research import research_agent
from agents.writer import writer_agent
from agents.automation import automation_agent


def execute_task(task: str):

    task_lower = task.lower().strip()

    # =========================================================
    # 1. CALCULATOR TOOL
    # =========================================================

    math_words = [
        "+",
        "-",
        "*",
        "/",
        "%",
        "calculate",
        "calculator",
        "compute",
        "what is",
    ]

    if any(word in task_lower for word in math_words):

        expression = task_lower

        # Remove natural-language words
        for word in [
            "calculate",
            "calculator",
            "what is",
            "compute",
        ]:
            expression = expression.replace(word, "")

        # Convert simple natural-language math
        expression = expression.replace("multiply", "*")
        expression = expression.replace("times", "*")
        expression = expression.replace("divided by", "/")
        expression = expression.replace("divide", "/")
        expression = expression.replace("plus", "+")
        expression = expression.replace("minus", "-")

        expression = expression.strip()

        result = execute_tool(
            "calculator",
            expression
        )

        return {
            "task": task,
            "agent": "orchestrator",
            "tool_selected": "calculator",
            "result": result
        }

    # =========================================================
    # 2. RESEARCH AGENT
    # =========================================================

    if any(word in task_lower for word in [
        "research",
        "analyze",
        "study",
        "information",
        "explain",
    ]):

        return {
            "task": task,
            "agent": "research_agent",
            "tool_selected": "rag",
            "result": research_agent(task)
        }

    # =========================================================
    # 3. WRITER AGENT
    # =========================================================

    if any(word in task_lower for word in [
        "write",
        "email",
        "article",
        "content",
        "document",
        "draft",
    ]):

        return {
            "task": task,
            "agent": "writer_agent",
            "tool_selected": None,
            "result": writer_agent(task)
        }

    # =========================================================
    # 4. AUTOMATION AGENT
    # =========================================================

    if any(word in task_lower for word in [
        "automate",
        "automation",
        "workflow",
        "process",
    ]):

        return {
            "task": task,
            "agent": "automation_agent",
            "tool_selected": "workflow",
            "result": automation_agent(task)
        }

    # =========================================================
    # 5. GENERAL AI
    # =========================================================

    response = ask_ai(
        "You are the EvoMind general AI assistant. "
        "Answer the user's request clearly and helpfully.",
        task
    )

    return {
        "task": task,
        "agent": "general_ai",
        "tool_selected": None,
        "result": response
    }