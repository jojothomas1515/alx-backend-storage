#!/usr/bin/env python3
"""Excercise."""
import redis
from typing import Union, Optional, Callable
from uuid import uuid4
from functools import wraps


def count_calls(fn: Callable) -> Callable:
    """Decorator to know how many times a method was called."""
    @wraps(fn)
    def wrapper(*args, **kwargs) -> Callable:
        args[0]._redis.incr(str(fn.__qualname__))
        return fn(*args, **kwargs)
    return wrapper


# def call_history(fn: Callable) -> Callable:
#     """records the history."""
#     @wraps(fn)
#     def wrapper(*ar)

class Cache:
    """
    Redis cache class.
    """

    def __init__(self):
        """Constructor."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Generate a random key (e.g. using uuid).

        store the input data in Redis using the
        random key and return the key.
        """
        key: str = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None)\
            -> Union[str, bytes, int, float]:
        """Get value with reference to a key."""
        val: Union[bytes, None] = self._redis.get(key)
        if callable(fn):
            return fn(val)
        return val

    def get_str(self, key: str) -> str:
        """Call the get method with a str coversion method."""
        return self.get(key, lambda x: str(x))

    def get_int(self, key: int) -> int:
        """Call the get method with a str coversion method."""
        return self.get(key, lambda x: int(x))
