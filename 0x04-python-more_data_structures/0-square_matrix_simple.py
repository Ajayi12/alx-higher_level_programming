#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
        function that computes the square value of all integers of a matrix.
    """
    mat = []
    for row in matrix:
        new_matrix = []
        for element in row:
            temp = element * element
            new_matrix.append(temp)
        mat.append(new_matrix)
    return mat
