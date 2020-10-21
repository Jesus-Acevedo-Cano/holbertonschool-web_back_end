#!/usr/bin/env python3
""" Let's execute multiple coroutines at the same time """
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ measures the total execution time """
    a: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    b: float = time.time()
    return (b - a) / n
