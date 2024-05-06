#!/usr/bin/env python3
"""Module"""
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    '''Measuring execution time'''
    coroutine = await wait_n(n, max_delay)
    total_time = sum(coroutine)
    return total_time/n
