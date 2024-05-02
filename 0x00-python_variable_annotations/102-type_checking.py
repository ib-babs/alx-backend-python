#!/usr/bin/env python3
'''Module'''
from typing import Any, Tuple, Union, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    '''Annotating using mypy'''
    zoomed_in: Tuple = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array: list[int] = [12, 72, 91]

zoom_2x: List = zoom_array(array)

zoom_3x: Tuple = zoom_array(array, 3.0)
