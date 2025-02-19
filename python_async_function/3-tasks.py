#!/usr/bin/env python3
"""
3. Tasks
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random

"""
Write a function task_wait_random
that takes an integer max_delay
and returns a asyncio.Task.
"""


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    function task_wait_random
    """
    return asyncio.create_task(wait_random(max_delay))
