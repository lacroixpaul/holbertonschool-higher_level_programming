#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for ligne in matrix:
        for element in ligne:
            print("{:d}".format(element), end=" ")
        print()
