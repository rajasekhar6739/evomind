import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise RuntimeError("OPENAI_API_KEY is not configured")

client = OpenAI(api_key=api_key)


def ask_ai(system_prompt: str, user_input: str) -> str:
    response = client.responses.create(
        model="gpt-4.1-mini",
        instructions=system_prompt,
        input=user_input,
    )

    return response.output_text
