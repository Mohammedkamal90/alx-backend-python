#!/usr/bin/env python3
"""async basic"""

import asyncio
from typing import Callable

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """task"""
    return asyncio.create_task(wait_random(max_delay))
