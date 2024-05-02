#!/usr/bin/env python3
"""
a type-annotated function which takes a list of floats as argument
"""


def sum_list(input_list: list[float]) -> float:
    """ returns their sum as a float. """

    return sum(input_list)
