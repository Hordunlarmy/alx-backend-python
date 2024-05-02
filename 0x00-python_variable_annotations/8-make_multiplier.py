#!/usr/bin/env python3
"""
 a type-annotated function that takes a float as argument
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ returns a function that multiplies a float by multiplier """

    return lambda x: x * multiplier
