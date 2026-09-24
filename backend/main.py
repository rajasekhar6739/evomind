# =========================================================
# LOAD ENVIRONMENT VARIABLES FIRST
# =========================================================

from dotenv import load_dotenv

load_dotenv()

# =========================================================
# FASTAPI IMPORTS
# =========================================================

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


# =========================================================
# E V O M I N D  MODULES
# =========================================================

from orchestrator.engine import execute_task
from tools.registry import list_tools, execute_tool

from memory.store import (
    update_preference,
    get_preferences,
)

from workflows.manager import (
    add_workflow,
    load_workflows,
    get_workflow,
)

from evolution.engine import (
    add_feedback,
    generate_suggestions,
)


# =========================================================
# CREATE APP
# =========================================================

app = FastAPI(
    title="EvoMind",
    description="AI Agent Automation Platform",
    version="1.0.0",
)


# =========================================================
# CORS
# =========================================================

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


# =========================================================
# REQUEST MODELS
# =========================================================

class TaskRequest(BaseModel):
    task: str


class Preference(BaseModel):
    key: str
    value: str


class WorkflowRequest(BaseModel):
    name: str
    task: str


class FeedbackRequest(BaseModel):
    workflow: str
    rating: int
    comment: str


# =========================================================
# ROOT
# =========================================================

@app.get("/")
def root():
    return {
        "name": "EvoMind",
        "status": "running",
        "version": "1.0.0",
    }


# =========================================================
# HEALTH CHECK
# =========================================================

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


# =========================================================
# AI AGENT
# =========================================================

@app.post("/agent/execute")
def execute(request: TaskRequest):
    return execute_task(request.task)


# =========================================================
# TOOLS
# =========================================================

@app.get("/tools")
def get_tools():
    return {
        "tools": list_tools()
    }


@app.post("/tools/{tool_name}")
def run_tool(tool_name: str, tool_input: str):
    return execute_tool(
        tool_name,
        tool_input
    )


# =========================================================
# MEMORY
# =========================================================

@app.get("/memory")
def memory():
    return get_preferences()


@app.post("/memory")
def save_pref(pref: Preference):
    return update_preference(
        pref.key,
        pref.value
    )


# =========================================================
# WORKFLOWS
# =========================================================

@app.get("/workflows")
def workflows():
    return load_workflows()


@app.post("/workflows")
def create_workflow(workflow: WorkflowRequest):
    return add_workflow(
        workflow.name,
        workflow.task
    )


@app.post("/workflows/run/{workflow_id}")
def run_workflow(workflow_id: int):

    workflow = get_workflow(workflow_id)

    if not workflow:
        return {
            "error": "Workflow not found"
        }

    return execute_task(
        workflow["task"]
    )


# =========================================================
# EVOLUTION / FEEDBACK
# =========================================================

@app.post("/feedback")
def feedback(item: FeedbackRequest):
    return add_feedback(
        item.workflow,
        item.rating,
        item.comment
    )


@app.get("/evolution")
def evolution():
    return {
        "suggestions": generate_suggestions()
    }
