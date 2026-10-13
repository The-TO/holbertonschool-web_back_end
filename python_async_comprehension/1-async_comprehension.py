#!/usr/bin/env python3
"""Module that runs several wait_random coroutines concurrently."""
import asyncio
import random
from typing import AsyncGenerator
from typing import List

async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    return