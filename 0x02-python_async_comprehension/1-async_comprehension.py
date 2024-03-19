#!/usr/bin/env python3
"""async comprehension used to return 10 random numbers"""
import asyncio
from typing import List
from random import uniform

async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    """
    Async coroutine to collect 10 random numbers using async comprehensions
    """
    return [num async for num in async_generator()]

# For testing
async def main():
    print(await async_comprehension())

asyncio.run(main())
