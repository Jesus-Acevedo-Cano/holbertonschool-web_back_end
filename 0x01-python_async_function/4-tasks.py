#!/usr/bin/env python3
""" Let's execute multiple coroutines at the same time """
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ spawn task_wait_random n times """
    delay_list: List[float] = []
    for i in range(n):
        delay_list.append(await task_wait_random(max_delay))
    return sorted(delay_list)
