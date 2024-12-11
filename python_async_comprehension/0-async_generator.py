#!/usr/bin/env python3
"""
The coroutine will loop 10 times,
each time asynchronously wait 1 second,
then yield a random number between 0 and 10.
"""
import random
import asyncio
from typing import List

async def async_generator() -> List[float]:
    """
    function asyc generator
    """
    for num in range(0, 11):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
