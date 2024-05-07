#!/usr/bin/env python3
"""Module"""
from asyncio import gather
from time import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure_runtime should measure the total runtime and return it."""
    start_time = time()
    await gather(async_comprehension(), async_comprehension(),
                 async_comprehension(), async_comprehension())
    end_time = time()
    return (end_time - start_time)
