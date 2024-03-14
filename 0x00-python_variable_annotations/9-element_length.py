#!/usr/bin/env python3
"""Takes an iterable object `lst` as input and returns a list of tuples.
Each tuple contains an element from `lst` and its length.
Args:
lst (Iterable[Sequence]): The input iterable object.
Returns:
List[Tuple[Sequence, int]]: A list of tuples where each tuple contains an element from `lst` and its length.
"""

from typing import Iterable, Sequence, Tuple, List

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """return list of tuples"""
    return [(i, len(i)) for i in lst]
