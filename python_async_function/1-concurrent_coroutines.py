#!/usr/bin/env python3

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int):
    all_delay = []
    result = ""
    
    while n != 0:

        all_delay.append(wait_random(max_delay))
        n -= 1
    
    return all_delay
    