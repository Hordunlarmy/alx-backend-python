#!/usr/bin/env python3
""" Measure the runtime of wait_n """

import time
from asyncio import run

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """ Measure the runtime of wait_n """

    start = time.time()
    run(wait_n(n, max_delay))
    end = time.time()
    return (end - start) / n
