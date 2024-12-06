#!/usr/bin/env python3
"""
 write an async routine called wait_n
 that takes in 2 int arguments (in this order):
    n and max_delay.
You will spawn wait_random n times with the specified max_delay.

wait_n should return the list
of all the delays (float values).
The list of the delays should be
in ascending order without using sort() because of concurrency.
"""
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    function wait_n
    """
    all_delay = []
    result = ""

    for num in range(n):
        result = await wait_random(max_delay)
        all_delay.append(result)

    for i in range(0, len(all_delay)):
        for j in range(i+1, len(all_delay)):
            if all_delay[i] >= all_delay[j]:
                all_delay[i], all_delay[j] = all_delay[j], all_delay[i]
    
    return all_delay
