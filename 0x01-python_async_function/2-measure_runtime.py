#!/usr/bin/env python3
"""basic of async"""

import asyncio
import time
from typing import List
from random import uniform

async def wait_random(max_delay: int = 10) -> float:
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

async def wait_n(n: int, max_delay: int) -> List[float]:
    tasks = [wait_random(max_delay) for _ in range(n)]
    return await asyncio.gather(*tasks)

def measure_time(n: int, max_delay: int) -> float:
    """measure runtime"""
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n

if __name__ == "__main__":
    n = 5
    max_delay = 9
    print(measure_time(n, max_delay))
