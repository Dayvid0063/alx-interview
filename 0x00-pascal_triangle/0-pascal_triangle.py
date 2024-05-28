#!/usr/bin/python3
"""
Returns ls representing the Pascal's triangle of n
"""


def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []
    prev = []
    for u in range(1, n + 1):
        row = [1] * u
        for v in range(1, u - 1):
            row[v] = prev[v - 1] + prev[v]
        prev = row
        triangle.append(row)
    return triangle
