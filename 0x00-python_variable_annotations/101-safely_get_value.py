#!/usr/bin/env python3

"""give parameter, return values, add type
annotations to function

Hint: look into TypeVar

def safely_get_value(dct, key, default = None):
    if key in dct:
        return dct[key]
    else:
        return default
"""


from typing import TypeVar, Mapping, Any, Union

# Define a type variable representing the possible types of values
T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    if key in dct:
        return dct[key]
    else:
        return default
