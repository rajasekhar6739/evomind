from services.ai import ask_ai


def writer_agent(task: str):
    prompt = f"""
You are a professional AI writing agent.

User task:
{task}

Create a clear, structured and professional response.

Requirements:
- Understand the user's intent
- Use professional language
- Keep the response relevant
- Use headings or bullet points when useful
- Do not invent information
"""

    return ask_ai(prompt, task)