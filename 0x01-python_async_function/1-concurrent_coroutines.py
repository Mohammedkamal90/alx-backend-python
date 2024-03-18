#!/usr/bin/env python3
'''
basic of async
'''

import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    wait_random n times with specifi max_delay
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    return await asyncio.gather(*tasks)
