from tools.registry import execute_tool

from agents.research import research_agent
from agents.writer import writer_agent
from agents.automation import automation_agent


def detect_agent(task: str) -> str:
    text = task.lower().strip()

    # -------------------------
    # Calculator
    # -------------------------
    calculator_words = [
        "calculate",
        "calculator",
        "compute",
        "multiply",
        "times",
        "divide",
        "divided by",
        "plus",
        "minus",
        "subtract",
        "addition",
    ]

    if (
        any(word in text for word in calculator_words)
        or any(symbol in text for symbol in ["*", "+", "/"])
    ):
        return "calculator"

    # -------------------------
    # Research Agent
    # -------------------------
    research_words = [
        "research",
        "what is",
        "who is",
        "explain",
        "find information",
        "information about",
        "analyze",
        "analysis",
        "study",
        "compare",
        "difference between",
        "how does",
        "why does",
        "latest information",
        "investigate",
    ]

    if any(word in text for word in research_words):
        return "research"

    # -------------------------
    # Writer Agent
    # -------------------------
    writer_words = [
        "write",
        "writer",
        "draft",
        "email",
        "cover letter",
        "resume",
        "cv",
        "article",
        "blog",
        "content",
        "document",
        "rewrite",
        "compose",
        "professional message",
    ]

    if any(word in text for word in writer_words):
        return "writer"

    # -------------------------
    # Automation Agent
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
        "process",
        "pipeline",
        "trigger",
    ]

    if any(word in text for word in automation_words):
        return "automation"

    # Default
    return "research"


def execute_task(task: str):

    if not task or not task.strip():
        return {
            "status": "error",
            "message": "Task cannot be empty",
        }

    agent = detect_agent(task)

    # =========================================================
    # 1. CALCULATOR
    # =========================================================

    if agent == "calculator":

        result = execute_tool(
            "calculator",
            task,
        )

        return {
            "status": "success",
            "task": task,
            "agent": "calculator",
            "tool_selected": "calculator",
            "result": result,
        }

    # =========================================================
    # 2. RESEARCH AGENT
    # =========================================================

    if agent == "research":

        result = research_agent(task)

        return {
            "status": "success",
            "task": task,
            "agent": "research_agent",
            "tool_selected": "research_agent",
            "result": result,
        }

    # =========================================================
    # 3. WRITER AGENT
    # =========================================================

    if agent == "writer":

        result = writer_agent(task)

        return {
            "status": "success",
            "task": task,
            "agent": "writer_agent",
            "tool_selected": "writer_agent",
            "result": result,
        }

    # =========================================================
    # 4. AUTOMATION AGENT
    # =========================================================

    if agent == "automation":

        result = automation_agent(task)

        return {
            "status": "success",
            "task": task,
            "agent": "automation_agent",
            "tool_selected": "automation_agent",
            "result": result,
        }

    # =========================================================
    # FALLBACK
    # =========================================================

    return {
        "status": "error",
        "task": task,
        "agent": "unknown",
        "tool_selected": None,
        "message": "No suitable agent found",
    }