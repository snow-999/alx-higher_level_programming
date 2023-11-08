#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return list(map(lambda mat: list(map(lambda i: i**2, mat)), matrix))
