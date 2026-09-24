import re

from tools.registry import execute_tool
from services.ai import ask_ai

from agents.research import research_agent
from agents.writer import writer_agent
from agents.automation import automation_agent


def execute_task(task: str):

    task_lower = task.lower().strip()

    # =========================================================
    # 1. CALCULATOR
    # =========================================================

    # Only treat it as calculator when there is an actual
    # mathematical expression or explicit calculation language.
    has_math_expression = bool(
        re.search(r"\d+\s*[\+\-\*\/%]\s*\d+", task_lower)
    )

    calculator_words = [
        "calculate",
        "calculator",
        "compute",
        "multiply",
        "times",
        "divided by",
        "divide",
        "plus",
        "minus",
    ]

    if has_math_expression or any(
        word in task_lower for word in calculator_words
    ):

        expression = task_lower

        # Remove natural-language calculator words
        remove_words = [
            "calculate",
            "calculator",
            "compute",
        ]

        for word in remove_words:
            expression = expression.replace(word, "")

        # Convert natural language math
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

    research_words = [
        "research",
        "research on",
        "analyze",
        "analysis",
        "study",
        "information about",
        "explain",
        "explain how",
        "tell me about",
        "investigate",
        "compare",
        "what is",
        "how does",
        "why does",
    ]

    if any(word in task_lower for word in research_words):

        result = research_agent(task)

        return {
            "task": task,
            "agent": "research_agent",
            "tool_selected": "research_agent",
            "result": result
        }

    # =========================================================
    # 3. WRITER AGENT
    # =========================================================

    writer_words = [
        "write",
        "writer",
        "email",
        "article",
        "content",
        "document",
        "draft",
        "compose",
        "rewrite",
        "resume",
        "cover letter",
        "blog",
        "post",
    ]

    if any(word in task_lower for word in writer_words):

        result = writer_agent(task)

        return {
            "task": task,
            "agent": "writer_agent",
            "tool_selected": "writer_agent",
            "result": result
        }

    # =========================================================
    # 4. AUTOMATION AGENT
    # =========================================================

    automation_words = [
        "automate",
        "automation",
        "workflow",
        "process",
        "schedule",
        "automatically",
        "pipeline",
        "trigger",
    ]

    if any(word in task_lower for word in automation_words):

        result = automation_agent(task)

        return {
            "task": task,
            "agent": "automation_agent",
            "tool_selected": "automation_agent",
            "result": result
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
        "tool_selected": "general_ai",
        "result": response
    }