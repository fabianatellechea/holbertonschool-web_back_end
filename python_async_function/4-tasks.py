#!/usr/bin/env python3
"""Let's execute multiple coroutines at the same time with async"""
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """wait_n function"""
    wait_list = []
    for _ in range(n):
        wait = await task_wait_random(max_delay)
        wait_list.append(wait)
    return sorted(wait_list)
