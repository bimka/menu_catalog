import json

import redis
from fastapi.encoders import jsonable_encoder


class Cache:
    def __init__(self, cache):
        self.cache = cache

    def get(self, key):
        value = self.cache.get(name=key)
        if value:
            ola = json.loads(value)
            print(type(ola))
            return json.loads(value)
        return None

    def set(self, key, value):
        json_value = json.dumps(jsonable_encoder(value))
        self.cache.set(name=key, value=json.dumps(json_value))

    def delete(self, key):
        self.cache.delete(name=key)


def get_redis():
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    try:
        yield r
    finally:
        r.close()
