#!/usr/bin/env python3
"""Module that runs several wait_random coroutines concurrently."""
import asyncio
from typing import List

wait_random = __import__('0_basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Run wait_random n times concurrently and return the sorted delays."""
    coroutines = [wait_random(max_delay) for _ in range(n)]
    delay: List[float] = []
    for result in asyncio.as_completed(coroutines):
        delay.append(await result)
    return delay
