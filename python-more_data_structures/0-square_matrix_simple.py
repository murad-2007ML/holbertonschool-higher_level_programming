#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    a = []
    for i in range(len(matrix)):
        a.append([])
        for j in range(len(matrix[i])):
            a[i].append(matrix[i][j]**2)
    return a
