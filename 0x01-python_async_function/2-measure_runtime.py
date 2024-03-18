#!/usr/bin/env python3
"""basic of async"""

import asyncio
import time
from typing import List
from random import uniform


wait_n = __import__('1-concurrent_coroutines').wait_n


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
