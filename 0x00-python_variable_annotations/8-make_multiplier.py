#!/usr/bin/env python3
"""Takes a float multiplier as argument and returns a function that multiplies a float by multiplier.
    Args:
        multiplier (float): The multiplier value.
    Returns:
        Callable[[float], float]: A function that takes a float as input and returns the result of multiplying it by the multiplier.
"""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:

    """return function multip float multiplier"""
    def multiplier_function(x: float) -> float:
        return x * multiplier

    return multiplier_function
