#!/usr/bin/env python3
"""
Description: Write a coroutine called async_comprehension that takes no
arguments.
"""


from typing import List
from importlib import import_module

async_generator = import_module('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine will collect 10 random numbers using an async comprehensing
    """

    return [i async for i in async_generator()]
