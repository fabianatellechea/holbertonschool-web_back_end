#!/usr/bin/env python3
"""Async Comprehensions"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """async_comprehension function"""
    async_list = []
    async for i in async_generator():
        async_list.append(i)
    return async_list
