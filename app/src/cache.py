import json

import redis
from fastapi.encoders import jsonable_encoder


class Cache:
    def __init__(self, cache):
        self.cache = cache

    def get(self, key):
        value = self.cache.get(name=key)
        if value:
            return json.loads(value)
        return None

    def set(self, key, value):
        json_value = jsonable_encoder(value)
        self.cache.set(name=key, value=json.dumps(json_value))


def get_redis():
    r = redis.Redis(host='localhost', port=6379)
    try:
        yield r
    finally:
        r.close()
