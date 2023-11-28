#!/usr/bin/python3
"""divide a matrix"""


def matrix_divided(matrix, div):
    """function to divide matrix
    args:
        matrix: the matrix will be divided
        div: the num will be divide to
    raise:
        type error if it's not int or float or
        real matrix or the len of matrix is 0
    return:
        list with the divided numbers
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists)" +
                        "of integers/floats")
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists)" +
                            "of integers/floats")
        for i in row:
            if not isinstance(i, (float, int)):
                raise TypeError("matrix must be a matrix (list of lists)" +
                                "of integers/floats")
        return [[round(i / div, 2) for i in row] for row in matrix]


if __name__ == "__main__":
    import docttest
    doctest.testfile("tests/2-matrix_divided.txt")
