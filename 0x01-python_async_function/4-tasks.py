#!/usr/bin/env python3
"""Module"""
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''New versiom 0f wait_n code'''
    return [await task_wait_random(max_delay) for _ in range(n)]
