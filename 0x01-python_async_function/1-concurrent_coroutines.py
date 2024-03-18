#!/usr/bin/env python3
'''
basic of async
'''

import asyncio
from typing import List
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    wait_random n times with specifi max_delay
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    return await asyncio.gather(*tasks)
