#!/usr/bin/env python3
""" Async Comprehensions """
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ collect random numbers using an async comprehensing """
    result: List[float] = []
    async for i in async_generator():
        result.append(i)
    return result
