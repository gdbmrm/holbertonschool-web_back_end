#!/usr/bin/env python3
"""
Take the code from wait_n
and alter it into a new function task_wait_n.
The code is nearly identical to wait_n
except task_wait_random is being called.
"""
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    function task_wait_n
    """
    all_delay = []
    result = ""

    for num in range(n):
        result = await task_wait_random(max_delay)
        all_delay.append(result)

    for i in range(0, len(all_delay)):
        for j in range(i+1, len(all_delay)):
            if all_delay[i] >= all_delay[j]:
                all_delay[i], all_delay[j] = all_delay[j], all_delay[i]

    return all_delay
