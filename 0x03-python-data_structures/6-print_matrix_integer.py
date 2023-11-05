#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for mat in matrix:
        if len(mat) == 0:
            print("")
        for i in range(len(mat)):
            if i == len(mat) - 1:
                print("{:d}".format(mat[i]), end="\n")
            else:
                print("{:d}".format(mat[i]), end=" ")
