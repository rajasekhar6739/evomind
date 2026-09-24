<<<<<<< HEAD
import re

from tools.registry import execute_tool
from services.ai import ask_ai

=======
>>>>>>> ec18223e44072a4474fb2a098010b181ed4894e2
from agents.research import research_agent
from agents.writer import writer_agent
from agents.automation import automation_agent
from tools.registry import execute_tool


def detect_agent(task: str) -> str:
    text = task.lower().strip()

    # -------------------------
    # Calculator
    # -------------------------
    calculator_words = [
        "calculate",
        "calculator",
        "multiply",
        "divide",
        "addition",
        "add",
        "subtract",
        "minus",
        "times",
    ]

    if (
        any(word in text for word in calculator_words)
        or any(symbol in text for symbol in ["*", "+", "/"])
    ):
        return "calculator"

    # -------------------------
    # Research
    # -------------------------
    research_words = [
        "research",
        "what is",
        "who is",
        "explain",
        "find information",
        "analyze",
        "analysis",
        "compare",
        "difference between",
        "how does",
        "why does",
        "latest information",
    ]

    if any(word in text for word in research_words):
        return "research"

    # -------------------------
    # Writer
    # -------------------------
    writer_words = [
        "write",
        "draft",
        "email",
        "cover letter",
        "resume",
        "cv",
        "article",
        "blog",
        "rewrite",
        "rewrite this",
        "create content",
        "professional message",
    ]

    if any(word in text for word in writer_words):
        return "writer"

    # -------------------------
    # Automation
    # -------------------------
    automation_words = [
        "automate",
        "automation",
        "workflow",
        "schedule",
        "automatically",
        "create a workflow",
        "build a workflow",
        "run workflow",
    ]

    if any(word in text for word in automation_words):
        return "automation"

    # Default
    return "research"


def execute_task(task: str):

    if not task or not task.strip():
        return {
            "status": "error",
            "message": "Task cannot be empty"
        }

<<<<<<< HEAD
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
=======
    agent = detect_agent(task)

    # -------------------------
    # Calculator
    # -------------------------
    if agent == "calculator":
>>>>>>> ec18223e44072a4474fb2a098010b181ed4894e2

        result = execute_tool(
            "calculator",
            task
        )

        return {
            "status": "success",
            "agent": "orchestrator",
            "tool_selected": "calculator",
            "result": result
        }

    # -------------------------
    # Research Agent
    # -------------------------
    if agent == "research":

<<<<<<< HEAD
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
=======
        result = research_agent(task)

        return {
            "status": "success",
            "agent": "research",
>>>>>>> ec18223e44072a4474fb2a098010b181ed4894e2
            "result": result
        }

    # -------------------------
    # Writing Agent
    # -------------------------
    if agent == "writer":

<<<<<<< HEAD
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
=======
        result = writer_agent(task)

        return {
            "status": "success",
            "agent": "writer",
>>>>>>> ec18223e44072a4474fb2a098010b181ed4894e2
            "result": result
        }

    # -------------------------
    # Automation Agent
    # -------------------------
    if agent == "automation":

<<<<<<< HEAD
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
=======
        result = automation_agent(task)

        return {
            "status": "success",
            "agent": "automation",
>>>>>>> ec18223e44072a4474fb2a098010b181ed4894e2
            "result": result
        }

    return {
<<<<<<< HEAD
        "task": task,
        "agent": "general_ai",
        "tool_selected": "general_ai",
        "result": response
    }
=======
        "status": "error",
        "message": "No suitable agent found"
    }
>>>>>>> ec18223e44072a4474fb2a098010b181ed4894e2
