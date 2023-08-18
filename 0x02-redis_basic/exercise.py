#!/usr/bin/env python3
"""Excercise."""
import redis
from typing import Union
from uuid import uuid4


class Cache:
    """
    Redis cache class.
    """

    def __init__(self):
        """Constructor."""
        self._redis: redis.Redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """generate a random key (e.g. using uuid).
        store the input data in Redis using the
        random key and return the key.
        """
        key: str = str(uuid4())
        self._redis.set(key, data)
        return key
