#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Given an n x n 2D matrix, rotate it 90 degrees clockwise.
    """

    i = 0
    for m in list(zip(*matrix)):
        matrix[i][:] = m[::-1]
        i += 1
