#!/usr/bin/env python3
""" Redis basic """
from functools import wraps
import redis
from sys import byteorder
from typing import Union, Callable, Optional, Any
import uuid


def count_calls(method: Callable) -> Callable:
    """ decorator """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """ wrapped function """
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper


def call_history(method: Callable) -> Callable:
    """ decorator """
    key = method.__qualname__
    inputs = key + ":inputs"
    outputs = key + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """ wrapped function """
        self._redis.rpush(inputs, str(args))
        result = method(self, *args, **kwds)
        self._redis.rpush(outputs, str(result))
        return result
    return wrapper


def replay(method: Callable):
    """ display the history of calls of
    a particular function """
    key = method.__qualname__
    inputs = key + ":inputs"
    outputs = key + ":outputs"
    redis = method.__self__._redis
    counter = redis.get(key).decode("utf-8")
    print(f"{key} was called {counter} times:")
    input_ = redis.lrange(inputs, 0, -1)
    output_ = redis.lrange(outputs, 0, -1)
    for i, j in list(zip(input_, output_)):
        attr, result = i.decode("utf-8"), j.decode("utf-8")
        print(f"{key}(*{attr}) -> {result}")


class Cache:
    """ Cache class """

    def __init__(self):
        """ constructor """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in cache"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) ->\
            Union[str, bytes, int, float]:
        """ Reading from Redis and recovering original type """
        result = self._redis.get(key)
        if fn:
            return fn(result)
        else:
            return result

    def get_str(self, result: bytes) -> str:
        """ automatically parametrize Cache.get with
        the correct conversion function """
        return result.decode("utf-8")

    def get_int(self, result: bytes) -> int:
        """ automatically parametrize Cache.get with
        the correct conversion function """
        return int.from_bytes(result, byteorder)
