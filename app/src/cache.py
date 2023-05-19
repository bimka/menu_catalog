import json

import redis
from fastapi import Depends


class Cache:
    def __init__(self, cache):
        self.cache = cache

    def append(self, key, value):
        self.cache.append(key=key, value=value)

    def get(self, key):
        value = self.cache.get(name=key)
        if value:
            return json.loads(value)
        return None

    def set(self, key, value):
        self.cache.set(name=key, value=value)

    def delete(self, key):
        self.cache.delete(key)


def get_redis():
    r = redis.Redis(host="localhost", port=6379)
    try:
        yield r
    finally:
        r.close()


def get_cache(cashe=Depends(get_redis)):
    return Cache(cashe)
