#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return
    for row in matrix:
        for i in range(len(row)):
            print(row[i], end=" ")
        print()