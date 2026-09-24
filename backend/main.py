from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from orchestrator.engine import execute_task
from tools.registry import list_tools, execute_tool

from memory.store import update_preference, get_preferences
from workflows.manager import (
    add_workflow,
    load_workflows,
    get_workflow
)
from evolution.engine import (
    add_feedback,
    generate_suggestions
)


app = FastAPI(
    title="EvoMind",
    description="AI Agent Automation Platform",
    version="1.0.0"
)


# --------------------------------
# CORS
# --------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "https://evomind-nine.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --------------------------------
# Task
# --------------------------------

class TaskRequest(BaseModel):
    task: str


@app.get("/")
def root():
    return {
        "name": "EvoMind",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/agent/execute")
def execute(request: TaskRequest):

    return execute_task(
        request.task
    )


# --------------------------------
# Tools
# --------------------------------

@app.get("/tools")
def get_tools():

    return {
        "tools": list_tools()
    }


@app.post("/tools/{tool_name}")
def run_tool(
    tool_name: str,
    tool_input: str
):

    return execute_tool(
        tool_name,
        tool_input
    )


# --------------------------------
# Memory
# --------------------------------

class Preference(BaseModel):
    key: str
    value: str


@app.get("/memory")
def memory():

    return get_preferences()


@app.post("/memory")
def save_pref(
    pref: Preference
):

    return update_preference(
        pref.key,
        pref.value
    )


# --------------------------------
# Workflows
# --------------------------------

class WorkflowRequest(BaseModel):
    name: str
    task: str


@app.get("/workflows")
def workflows():

    return load_workflows()


@app.post("/workflows")
def create_workflow(
    workflow: WorkflowRequest
):

    return add_workflow(
        workflow.name,
        workflow.task
    )


@app.post("/workflows/run/{workflow_id}")
def run_workflow(
    workflow_id: int
):

    workflow = get_workflow(
        workflow_id
    )

    if not workflow:
        return {
            "error": "Workflow not found"
        }

    return execute_task(
        workflow["task"]
    )


# --------------------------------
# Feedback
# --------------------------------

class FeedbackRequest(BaseModel):
    workflow: str
    rating: int
    comment: str


@app.post("/feedback")
def feedback(
    item: FeedbackRequest
):

    return add_feedback(
        item.workflow,
        item.rating,
        item.comment
    )


# --------------------------------
# Evolution
# --------------------------------

@app.get("/evolution")
def evolution():

    return {
        "suggestions": generate_suggestions()
    }
