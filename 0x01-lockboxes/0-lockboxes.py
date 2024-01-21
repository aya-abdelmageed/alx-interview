#!/usr/bin/python3
"""solution for lockboxes"""

def canUnlockAll(boxes):
    """method that determines if all the boxes can be opened."""

    n = len(boxes)
    opened = [0]

    for key, box in enumerate(boxes):
        
        for k in box:
            if k not in opened and k != key:
                opened.append(k)

    if len(opened) == n:
        return True
    else:
        return False


        