import json
from pathlib import Path


def _path(filename):
    return Path(Path.home(), '.config', 'ghi', filename)


def load(filename='config.json'):
    return json.loads(_path(filename).read_text())


def save(filename='config.json', data=None):
    return _path(filename).write_text(json.dumps(data))


def exists(filename='config.json'):
    return _path(filename).is_file()


def token():
    return load()['github']['token']


def ignored():
    return load()['ignored']
