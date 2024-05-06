#!/usr/bin/env python3
"""Module"""
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> list:
    '''New versiom 0f wait_n code'''
    return [await task_wait_random(max_delay) for _ in range(n)]

n = 5
max_delay = 6
print(asyncio.run(task_wait_n(n, max_delay)))
