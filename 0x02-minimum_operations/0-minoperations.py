#!/usr/bin/python3
"""solution for minoperations"""


def minOperations(n):
    """method for the problem"""

    t = 0
    m = 2
    while n > 1:
        while not n % m:
            t += m
            n /= m
        m += 1
    return t
