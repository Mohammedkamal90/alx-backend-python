#!/usr/bin/env python3
"""validate piece of code
and necessary changes.
"""

from typing import Tuple, List



def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """correct annontation"""
    zoomed_in: List = (
        item for item in lst
        for i in range(factor)
    )
    return zoomed_in


array = (12, 72, 91)  # Use tuple instead of list

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)  # Use an integer instead of float
