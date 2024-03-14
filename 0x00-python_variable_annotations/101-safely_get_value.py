#!/usr/bin/env python3

"""give parameters, return values, add type
annotations to function
"""
from typing import TypeVar, Mapping, Any, Union

# Define a type variable representing the possible types of values
T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    if key in dct:
        return dct[key]
    else:
        return default
