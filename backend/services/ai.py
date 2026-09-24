import os

from dotenv import load_dotenv
from openai import OpenAI


# Load environment variables
load_dotenv()


# ---------------------------------------------------------
# Groq API configuration
# ---------------------------------------------------------

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise RuntimeError("GROQ_API_KEY is not configured")


# Groq provides an OpenAI-compatible API
client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1",
)


# ---------------------------------------------------------
# AI helper
# ---------------------------------------------------------

def ask_ai(system_prompt: str, user_prompt: str) -> str:
    """
    Send a prompt to Groq and return the generated text.
    """

    response = client.responses.create(
        model="openai/gpt-oss-20b",
        instructions=system_prompt,
        input=user_prompt,
    )

    return response.output_text
