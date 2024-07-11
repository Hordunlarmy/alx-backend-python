#!/usr/bin/env python3
"""Random number generator using async generator"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Generate 10 random numbers between 0 and 10, waiting 1 second between
    each.
    """

    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
