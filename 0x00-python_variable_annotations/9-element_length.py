#!/usr/bin/env python3
"""
a type-annotated function which takes an iterable list
containing Sequence items
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Returns a list of tuples """

    return [(i, len(i)) for i in lst]
