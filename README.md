# EvoMind

EvoMind is a modular AI application that demonstrates agent orchestration, tool execution, retrieval-augmented knowledge access, workflow automation, user memory, and feedback-driven evolution.

## Overview

EvoMind accepts a user's task and routes it through an orchestrator to the appropriate capability.

The current system includes:

* Orchestrator-based task routing
* Research Agent
* Writer Agent
* Automation Agent
* Universal Tool Layer
* Calculator Tool
* Lightweight RAG retrieval
* User preference memory
* Reusable workflows
* Feedback-driven evolution suggestions
* React frontend dashboard
* FastAPI backend

## Architecture

```text
                         USER
                           |
                           v
                    React Frontend
                           |
                           v
                       FastAPI
                           |
                           v
                    ORCHESTRATOR
                     /    |    \
                    /     |     \
                   v      v      v
             Research   Writer  Automation
                 |
                 v
             RAG Layer
                 |
                 v
          Knowledge Base

                    ORCHESTRATOR
                          |
                          v
                  Universal Tool Layer
                          |
                          v
                     Calculator

Memory -----------------> User Preferences

Workflows --------------> Reusable Tasks

Feedback ----------------> Evolution Engine
```

## Main Components

### Orchestrator

The orchestrator analyzes the user's request and selects an appropriate capability such as a calculator tool, research agent, writer agent, or automation agent.

### Research Agent

The Research Agent retrieves relevant documents from the local knowledge base and uses the retrieved context as input for answer generation.

### Writer Agent

The Writer Agent handles writing-oriented tasks such as emails, articles, documents, and content generation.

### Automation Agent

The Automation Agent converts automation requests into structured workflow plans containing goals, triggers, steps, tools, inputs, outputs, and improvements.

### Universal Tool Layer

Tools are registered through a central registry so that capabilities can be discovered and executed by the orchestration layer.

Current tool:

```text
Calculator
```

### RAG

The current RAG implementation uses lightweight lexical-overlap retrieval over local text documents.

Knowledge source:

```text
backend/knowledge/ai_architecture.txt
```

This is intentionally simple and can later be replaced by embeddings and a vector database.

### Memory

EvoMind stores user preferences such as:

```json
{
  "report_style": "short"
}
```

This creates the foundation for behavioral personalization.

### Workflow Engine

Reusable workflow definitions can be created and executed through the backend API.

### Evolution Engine

User feedback is stored and converted into improvement suggestions.

Example:

```text
"Make future reports short"
```

can produce:

```text
Use shorter reports by default.
```

The current implementation is user-directed feedback evolution rather than automatic source-code modification.

## Tech Stack

### Backend

* Python
* FastAPI
* Pydantic
* Uvicorn

### Frontend

* React
* Vite
* JavaScript
* CSS

### AI / Architecture Concepts

* Agent orchestration
* Sub-agent architecture
* Tool calling abstraction
* RAG
* Workflow automation
* Behavioral memory
* Feedback-driven evolution
* Modular AI software architecture

## Project Structure

```text
evomind/
│
├── backend/
│   ├── agents/
│   │   ├── research.py
│   │   ├── writer.py
│   │   └── automation.py
│   │
│   ├── evolution/
│   │   └── engine.py
│   │
│   ├── knowledge/
│   │   └── ai_architecture.txt
│   │
│   ├── memory/
│   │   └── store.py
│   │
│   ├── orchestrator/
│   │   └── engine.py
│   │
│   ├── rag/
│   │   └── retriever.py
│   │
│   ├── services/
│   │   └── ai.py
│   │
│   ├── tools/
│   │   ├── calculator.py
│   │   └── registry.py
│   │
│   ├── workflows/
│   │   └── manager.py
│   │
│   ├── main.py
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   ├── index.css
│   │   └── main.jsx
│   └── package.json
│
├── .gitignore
└── README.md
```

## Setup

### 1. Clone the project

```bash
git clone <our-repository-url>
cd evomind
```

### 2. Backend setup

```bash
cd backend
python -m venv venv
```

Windows:

```bat
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Start backend

```bash
python -m uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```

Backend:

```text
http://127.0.0.1:8000
```

Swagger API documentation:

```text
http://127.0.0.1:8000/docs
```

### 4. Start frontend

Open another terminal:

```bash
cd frontend
npm install
npm run dev
```

Frontend:

```text
http://localhost:5173
```

## Example Tasks

### Calculator

```text
Calculate 125 * 8
```

Expected result:

```text
1000
```

### Research

```text
Research EvoMind AI architecture
```

### Writing

```text
Write an email about AI automation
```

### Automation

```text
Create an automation workflow for daily reports
```

## API Endpoints

```text
GET  /
GET  /health

POST /agent/execute

GET  /tools
POST /tools/{tool_name}

GET  /memory
POST /memory

GET  /workflows
POST /workflows
POST /workflows/run/{workflow_id}

POST /feedback
GET  /evolution
```

## Current AI Mode

The project currently supports an AI-service abstraction with an offline demonstration mode so that the application can run without an active external model quota.

The AI service is designed to be provider-swappable. A production deployment can connect the same architecture to an external LLM provider or a local model.

## Security

Do not commit secrets such as:

```text
.env
API keys
credentials
tokens
```

The repository includes a `.gitignore` file to prevent common secret and environment files from being committed.

## Future Improvements

* Embedding-based semantic search
* Vector database integration
* Multiple production LLM providers
* Local model support
* More tools
* Dependency-aware tool composition
* Tool generation
* Capability replication and composition
* Human approval gates for autonomous actions
* Automatic feature deployment with safety checks
* Post-quantum cryptography integration
* Authentication and role-based access control
* Observability and agent execution tracing

## Portfolio Highlights

EvoMind demonstrates practical experience with:

```text
AI / GenAI
Agent Orchestration
Sub-Agent Architecture
AI Application Development
RAG
Workflow Automation
Tool Systems
Behavioral Memory
Feedback-Driven Evolution
FastAPI
React
Modular Software Architecture
```

## License

For portfolio and educational use.
