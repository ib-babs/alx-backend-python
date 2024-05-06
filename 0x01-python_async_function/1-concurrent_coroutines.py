#!/usr/bin/env python3
"""Module"""
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''Running concurrent coroutines running n-times'''
    return [await wait_random(max_delay) for _ in range(n)]
