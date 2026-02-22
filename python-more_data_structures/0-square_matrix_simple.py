#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """Computes the square value of all integers of a matrix.

    Args:
        matrix (list): A list of lists of integers.

    Returns:
        A new list of lists of integers representing the square value
        of all integers of the input matrix.
    """
    return [[i ** 2 for i in row] for row in matrix]
