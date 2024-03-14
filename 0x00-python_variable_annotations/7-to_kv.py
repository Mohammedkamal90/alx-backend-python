#!/usr/bin/env python3
"""
    Takes a string k and an int or float v as arguments and returns a tuple.
    The first element of the tuple is the string k.
    The second element is the square of the int/float v and should be annotated as a float.

    Args:
        k (str): The string key.
        v (Union[int, float]): The integer or float value.

    Returns:
        Tuple[str, float]: A tuple containing the string k and the square of the int/float v.
"""

import  typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """return tuple of string"""
    return (k, float(v * v))

