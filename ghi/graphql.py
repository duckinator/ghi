import json
from urllib.request import urlopen, Request
from . import config

def request(query):
    req = Request("https://api.github.com/graphql",
            data=json.dumps({'query': query}).encode('utf-8'),
            headers={'Authorization': 'bearer {}'.format(config.token())})
    result = urlopen(req).read().decode()
    return json.loads(result)
