#!/usr/bin/env python3
# Description: Write a function measure_runtime that measures the total runtime

import asyncio
import time
from importlib import import_module

aync_comprehension = import_module('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the runtime of async_comprehension four times and return the
    total runtime.
    """

    start = time.time()
    await asyncio.gather(*(aync_comprehension() for i in range(4)))
    end = time.time()
    return end - start
