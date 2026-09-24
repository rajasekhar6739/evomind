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

    agent = detect_agent(task)

    # -------------------------
    # Calculator
    # -------------------------
    if agent == "calculator":

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

        result = research_agent(task)

        return {
            "status": "success",
            "agent": "research",
            "result": result
        }

    # -------------------------
    # Writing Agent
    # -------------------------
    if agent == "writer":

        result = writer_agent(task)

        return {
            "status": "success",
            "agent": "writer",
            "result": result
        }

    # -------------------------
    # Automation Agent
    # -------------------------
    if agent == "automation":

        result = automation_agent(task)

        return {
            "status": "success",
            "agent": "automation",
            "result": result
        }

    return {
        "status": "error",
        "message": "No suitable agent found"
    }
