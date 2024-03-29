#!/usr/bin/env python3
"""Let's execute multiple coroutines at the same time with async"""
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """wait_n function"""
    wait_list = []
    for _ in range(n):
        wait = await wait_random(max_delay)
        wait_list.append(wait)
    return sorted(wait_list)
