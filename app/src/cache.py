import json

import redis


class Cache:
    def __init__(self, cache):
        self.cache = cache

    def get(self, key):
        value = self.cache.get(name=key)
        if value:
            return json.loads(value)
        return None

    def set(self, key, value):
        self.cache.set(name=key, value=value)

    def delete(self, key):
        self.cache.delete(name=key)


def get_redis():
    r = redis.Redis(host='localhost', port=6379)
    try:
        yield r
    finally:
        r.close()
