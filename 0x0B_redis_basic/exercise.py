#!/usr/bin/env python3
""" Redis basic """
import redis
from typing import Union, Callable, Optional, Any
import uuid


class Cache:
    """ Cache class """

    def __init__(self):
        """ constructor """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in cache"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) ->\
            Union[str, bytes, int, float]:
        """ Reading from Redis and recovering original type """
        if key:
            res = self._redis.get(key)
            if fn:
                return fn(res)
            else:
                return res
