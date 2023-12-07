#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    new_matrix = [list(map(lambda x: x ** 2, listing)) for listing in matrix]
    return new_matrix
