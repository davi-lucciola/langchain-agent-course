import os
from pathlib import Path


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY")


BASE_DIR = Path(__file__).resolve().parent


def get_path(*relative_path_parts):
    return Path(__file__).resolve().parent.joinpath(*relative_path_parts)
