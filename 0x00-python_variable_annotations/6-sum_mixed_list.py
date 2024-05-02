#!/usr/bin/env python3
'''Module'''
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    '''function sum_mixed_list which takes a list
    mxd_lst of integers and floats and returns their
    sum as a float.'''
    return float(sum(mxd_list))
