#!/usr/bin/env python3
"""async comprehension used to return 10 random numbers"""
import asyncio
from typing import List
from random import uniform

async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    """
    async_comprehension function return 10 random unms
    """
    return [num async for num in async_generator()]
