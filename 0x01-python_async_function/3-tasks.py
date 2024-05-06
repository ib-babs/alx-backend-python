#!/usr/bin/env python3
"""Module"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''Asyncio Task: The optional event_loop argument
    allows explicitly setting the event loop object
    used by the future. If it's not provided,
    the future uses the default event loop.'''
    return asyncio.Task(wait_random(max_delay))
