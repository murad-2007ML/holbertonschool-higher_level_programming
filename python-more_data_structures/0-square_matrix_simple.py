#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for i in matrix:
        for j in range(len(i)):
            i[j] = i[j] ** 2
    return matrix
