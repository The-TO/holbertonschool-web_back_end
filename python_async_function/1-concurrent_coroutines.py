#!/usr/bin/env python3
"""Module providing a basic coroutine that waits for a random delay."""
import asyncio
from typing import List

wait_random = __import__('0_basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """Wait a random delay between 0 and max_delay seconds, then return it."""
    coroutines = [wait_random(max_delay) for _ in range(n)]
    delay: List[float] = []
    for result in asyncio.as_completed(coroutines):
        delay.append(await finished)
    return delay
