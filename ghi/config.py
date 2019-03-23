import json
from pathlib import Path

def load():
    return json.loads(Path(Path.home(), ".config", "ghi", "config.json").read_text())

def token():
    return load()["github"]["token"]

def ignored():
    return load()["ignored"]
