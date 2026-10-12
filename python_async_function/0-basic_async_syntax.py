#!/usr/bin/env python3
"""coroutine that takes in a integer argument that wait for a random belay between 0 and a max delay"""

import asyncio, random 
from typing import List

async def wait_random(max_delay: int = 10) -> Float:
    """Wait a random delay between 0 and max_delay seconds, then return it."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
