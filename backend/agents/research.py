from services.ai import ask_ai
from rag.retriever import retrieve


def research_agent(task: str):

    documents = retrieve(task)

    context = "\n\n".join(
        [
            f"Source: {doc['filename']}\n{doc['content']}"
            for doc in documents
        ]
    )

    prompt = f"""
You are the EvoMind Research Agent.

Use the retrieved knowledge below when relevant.

KNOWLEDGE:
{context}

USER QUESTION:
{task}

Provide a clear and structured answer.

If the knowledge base does not contain enough
information, clearly state that.
"""

    return ask_ai(prompt, task)