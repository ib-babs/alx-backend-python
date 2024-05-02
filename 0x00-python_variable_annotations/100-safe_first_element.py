#!/usr/bin/env python3
'''Module'''
from typing import Any, Union, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''Annotating...'''
    if lst:
        return lst[0]
    else:
        return None
