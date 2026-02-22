#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers.

    Args:
        matrix (list): The matrix of integers to print.
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j != len(matrix[i]) - 1:
                print("{:d}".format(matrix[i][j]), end=" ")
            else:
                print("{:d}".format(matrix[i][j]), end="")
        print()
