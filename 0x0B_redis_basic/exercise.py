#!/usr/bin/env python3
""" Redis basic """
from redis.client import Redis
from typing import Union, Callable, Optional, Any
import uuid


class Cache:
    """ Cache class """

    def __init__(self):
        """ constructor """
        self._redis = Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ takes a data argument and returns a string """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
