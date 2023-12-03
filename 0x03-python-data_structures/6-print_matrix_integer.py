#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for outer_el in matrix:
        for inner_el in outer_el:
            print("{:d}".format(inner_el), end="")
            if inner_el != outer_el[len(outer_el)-1]:
                print(" ", end="")
        print("")
