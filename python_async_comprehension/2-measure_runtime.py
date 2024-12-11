#!/usr/bin/env python3
"""
write a measure_runtime coroutine
that will execute async_comprehension four times
in parallel using asyncio.gather.
measure_runtime should measure the total runtime and return it.
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """
    function measure_runtime
    """
    start_time = time.time()

    result = await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension())

    total_time = time.time() - start_time
    return total_time
