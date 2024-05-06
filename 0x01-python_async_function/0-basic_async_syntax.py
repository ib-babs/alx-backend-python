#!/usr/bin/env python3
"""Module"""
from random import uniform
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    '''Awaiting random number'''
    wait = uniform(0, max_delay)
    await asyncio.sleep(wait)
    return wait
