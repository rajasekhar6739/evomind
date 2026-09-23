from services.ai import ask_ai


def automation_agent(task: str):
    prompt = f"""
You are an AI automation agent.

Analyze the following automation task:

{task}

Create a practical automation plan.

Return the response using this structure:

1. Goal
2. Trigger
3. Required Steps
4. Tools Required
5. Data / Inputs
6. Expected Output
7. Possible Improvements

Focus on practical workflow automation and dependency-aware execution.
"""

    return ask_ai(prompt, task)