#!/usr/bin/env python3
"""Module that collects random numbers with an asynchronous comprehension."""
import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def mesure_runtime() -> float:
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.perf_counter - start
