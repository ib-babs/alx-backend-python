#!/usr/bin/env python3
"""Module"""
from typing import AsyncIterable
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> AsyncIterable[float]:
    """The coroutine will collect 10 random numbers using an
    async comprehensing over `async_generator`, then return
    the 10 random numbers."""
    ten_async_random_numbers = [i async for i in async_generator()]
    return ten_async_random_numbers
