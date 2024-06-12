#!/usr/bin/python3
"""Minimum operations coding challenge"""


def minOperations(n):
    """Method that calculates the fewest number of operations
    needed to result in exactly n H characters"""
    if not isinstance(n, int) or n <= 1:
        return 0
    
    ops = 0
    cur = 1
    c_len = 0

    while cur < n:
        if c_len == 0:
            c_len = cur
            ops += 1
        if (n - cur) % cur == 0:
            c_len = cur
            ops += 1
        cur += c_len
        ops += 1

    return ops
