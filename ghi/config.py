import json
from pathlib import Path


def load():
    config_file = Path(Path.home(), ".config", "ghi", "config.json")
    return json.loads(config_file.read_text())


def token():
    return load()["github"]["token"]


def ignored():
    return load()["ignored"]
