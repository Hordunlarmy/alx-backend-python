#!/usr/bin/env python3
"""
 a type-annotated function that retrieves a value from a mapping
 (such as a dictionary) using a given key.
"""
from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')
Result = Union[Any, T]
Default = Union[T, None]


def safely_get_value(dct: Mapping, key: Any,
                     default: Default = None) -> Result:
    """ Return thehe value associated with 'key' in 'dct' if 'key' exists.
    Otherwise, returns 'default' which can be 'None' or another value if
    specified.
    """
    if key in dct:
        return dct[key]
    else:
        return default
