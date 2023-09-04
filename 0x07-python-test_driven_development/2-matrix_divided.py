#!/usr/bin/python3
""" a function that divides a matrix"""

def matrix_divided(matrix, div):
    """ the function"""
    if not isinstance(matrix, list) or \
       not all(isinstance(row, list) for row in matrix):
        msg = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(msg)

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    return [[round(element / div, 2) for element in row] for row in matrix]
