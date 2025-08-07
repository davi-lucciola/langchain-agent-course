from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def get_path(*relative_path_parts):
    return Path(__file__).resolve().parent.joinpath(*relative_path_parts)
