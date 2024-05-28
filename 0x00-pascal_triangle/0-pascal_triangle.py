#!/usr/bin/python3
"""
Returns ls representing the Pascal's triangle of n
"""


def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []
    p_r = []
    row = []
    for u in range(0, n + 1):
        row = [v > 0 and v < u - 1 and u > 2 and p_r[v-1] +
               p_r[v] or 1 for v in range(0, u)]
        p_r = row
        triangle += [row]
    return triangle[1:]
