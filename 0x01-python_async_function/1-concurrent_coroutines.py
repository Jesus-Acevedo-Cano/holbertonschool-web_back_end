#!/usr/bin/env python3
""" Let's execute multiple coroutines at the same time """
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ spawn wait_random n times """
    delay_list: List[float] = []
    for i in range(n):
        delay_list.append(await wait_random(max_delay))
    return sorted(delay_list)
