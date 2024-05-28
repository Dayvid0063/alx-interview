#!/usr/bin/python3
"""
Returns ls representing the Pascal's triangle of n
"""


def pascal_triangle(n):
    triangle = []
    if not isinstance(n, int) or n <= 0:
        return triangle
    
    for u in range(n):
        r = []
        for v in range(u + 1):
            if v == 0 or v == u:
                r.append(1)
            elif u > 0 and v > 0:
                r.append(triangle[u - 1][v - 1] + triangle[u - 1][v])
        triangle.append(r)
    
    return triangle
