#!/usr/bin/env python3
"""
a type-annotated function which takes any type of sequence
"""

from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ Returns any type of object or None when the sequence is empty"""
    if lst:
        return lst[0]
    else:
        return None
