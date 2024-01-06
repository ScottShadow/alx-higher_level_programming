#!/usr/bin/python3
def matrix_divided(matrix, div):
    if not all(isinstance(row, list) and all(isinstance(i, (int, float)) for i in row) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    new_matrix = []

    for row in matrix:
        new_list = []
        for i in row:
            dividend = round(i / div, 2)
            new_list.append(dividend)
        new_matrix.append(new_list)
