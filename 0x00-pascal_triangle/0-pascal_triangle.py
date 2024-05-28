#!/usr/bin/python3
"""
Returns ls representing the Pascal's triangle of n
"""


def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []

    for u in range(n):
        row = []
        for v in range(u + 1):
            if v == 0 or v == u:
                row.append(1)
            else:
                row.append(triangle[u-1][v-1] + triangle[u-1][v])
        triangle.append(row)

    return triangle
