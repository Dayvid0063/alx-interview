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
    for i in range(0, n + 1):
        row = [j > 0 and j < i - 1 and i > 2 and p_r[j-1] +
               p_r[j] or 1 for j in range(0, i)]
        p_r = row
        triangle += [row]
    return triangle[1:]
