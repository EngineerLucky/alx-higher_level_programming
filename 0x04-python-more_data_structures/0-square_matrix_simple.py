#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_one = [[x ** 2 for x in row] for row in matrix]
    return new_one
