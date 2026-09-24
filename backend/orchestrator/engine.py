from agents.research import research_agent
from agents.writer import writer_agent
from agents.automation import automation_agent
from tools.registry import execute_tool


def detect_agent(task: str):
    text = task.lower()

    # Calculator
    calculator_words = [
        "calculate",
        "add",
        "subtract",
        "multiply",
        "divide",
        "*",
        "+",
        "-",
        "/"
    ]

    if any(word in text for word in calculator_words):
        return "calculator"

    # Research
    research_words = [
        "research",
        "explain",
        "find information",
        "what is",
        "who is",
        "latest",
        "compare",
        "analyze"
    ]

    if any(word in text for word in research_words):
        return "research"

    # Writing
    writing_words = [
        "write",
        "draft",
        "email",
        "article",
        "blog",
        "resume",
        "cover letter",
        "rewrite",
        "content"
    ]

    if any(word in text for word in writing_words):
        return "writer"

    # Automation
    automation_words = [
        "automate",
        "automation",
        "workflow",
        "schedule",
        "create workflow",
        "run workflow"
    ]

    if any(word in text for word in automation_words):
        return "automation"

    return "research"


def execute_task(task: str):

    agent = detect_agent(task)

    if agent == "calculator":
        return {
            "agent": "calculator",
            "tool_selected": "calculator",
            "result": execute_tool("calculator", task)
        }

    if agent == "research":
        return {
            "agent": "research",
            "result": research_agent(task)
        }

    if agent == "writer":
        return {
            "agent": "writer",
            "result": writer_agent(task)
        }

    if agent == "automation":
        return {
            "agent": "automation",
            "result": automation_agent(task)
        }

    return {
        "agent": "research",
        "result": research_agent(task)
    }
