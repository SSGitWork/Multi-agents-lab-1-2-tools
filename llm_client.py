"""
LLM client for this course.

All API calls are routed through Helicone, which handles authentication
and usage tracking. You do not need an OpenAI API key.

Usage:
    from llm_client import get_client
    client = get_client()
    # Use exactly like the standard OpenAI client.
"""

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv(override=True)


def get_client() -> OpenAI:
    """
    Return a pre-configured OpenAI client routed through Helicone.

    Reads HELICONE_API_KEY from the environment. In GitHub Codespaces
    this is injected automatically — you do not need to set it yourself.

    Raises
    ------
    EnvironmentError
        If HELICONE_API_KEY is not set in the environment.
    """

    _HELICONE_BASE = os.getenv("HELICONE_BASE_URL")
    _OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
    _HELICONE_API_KEY = os.getenv("HELICONE_API_KEY")

    if not _HELICONE_API_KEY:
        raise EnvironmentError(
            "HELICONE_API_KEY is not set.\n"
            "In Codespaces this is injected automatically.\n"
            "If running locally, copy .env.example to .env and ask "
            "your instructor for the key."
        )

    return OpenAI(
        # Helicone key doubles as the auth token.
        api_key=_OPENROUTER_API_KEY,
        base_url=_HELICONE_BASE,
        default_headers={
            "Helicone-Auth": f"Bearer {_HELICONE_API_KEY}",
        },
    )
