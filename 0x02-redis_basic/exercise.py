#!/usr/bin/env python3
"""Excercise."""
import redis
from typing import Union, Optional, Callable
from uuid import uuid4
from functools import wraps


def count_calls(fn: Callable) -> Callable:
    """Decorator to know how many times a method was called."""
    @wraps(fn)
    def wrapper(self, *args, **kwargs) -> Callable:
        self._redis.incr(str(fn.__qualname__))
        return fn(self, *args, **kwargs)
    return wrapper


def replay(method: Callable) -> None:
    """Display replay."""
    method_name = str(method.__qualname__)
    in_key = f"{method_name}:inputs"
    out_key = f"{method_name}:outputs"
    red = redis.Redis()
    c_counts = red.get(method_name)

    inp = red.lrange(in_key, 0, -1)
    out = red.lrange(out_key, 0, -1)
    res = zip(inp, out)
    print(f"Cache.store was called {c_counts.decode('utf-8')} times:")
    for i, o in res:
        print(f"{method_name}(*{i.decode('utf-8')}) -> {str(o.decode('utf-8'))}")


def call_history(method: Callable) -> Callable:
    """records the history."""
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Callable:
        in_key = f"{str(method.__qualname__)}:inputs"
        out_key = f"{str(method.__qualname__)}:outputs"
        self._redis.rpush(in_key, str(args))
        results = method(self, *args, **kwargs)
        self._redis.rpush(out_key, results)
        return results
    return wrapper


class Cache:
    """
    Redis cache class.
    """

    def __init__(self):
        """Constructor."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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
