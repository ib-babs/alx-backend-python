#!/usr/bin/env python3
"""Module"""
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    '''Running concurrent coroutines running n-times'''
    return [await wait_random(max_delay) for _ in range(n)]
