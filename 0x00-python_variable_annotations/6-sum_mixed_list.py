#!/usr/bin/env python3
"""
a type-annotated function which takes a list of integers and floats
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ returns their sum as a float. """

    return sum(mxd_lst)
