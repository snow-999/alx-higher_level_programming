#!/usr/bin/python3
"""input output task"""


def pascal_triangle(n):
    """function to print a triangle"""
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        temp = [1]
        temp2 = triangle[-1]
        for i in range(len(temp2) - 1):
            temp.append(temp2[i] + temp2[i + 1])
        temp.append(1)
        triangle.append(temp)
    return triangle
