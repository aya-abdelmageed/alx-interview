#!/usr/bin/python3
"""
0-validate_utf8
"""


def validUTF8(data):
    """
    method that determines if a given data set represents a valid UTF-8 encoding.
    """
    count = 0
    for d in data:
        if count == 0:
            if d & 128 == 0:
                count = 0
            elif d & 224 == 192:
                count = 1
            elif d & 240 == 224:
                count = 2
            elif d & 248 == 240:
                count = 3
            else:
                return False
        else:
            if d & 192 != 128:
                return False
            count -= 1
    if count == 0:
        return True
    return False
