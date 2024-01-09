#!/usr/bin/python3
"""Pascal's Triangle Generator Function Module"""


def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to the specified number of rows.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list: A list of lists representing Pascal's Triangle.
    """
    n = n + 1
    mylist = []
    oldlist = []
    for i in range(n):
        newlist = []
        for j in range(i):
            if j == 0 or j == i - 1:
                newlist.append(1)
            else:
                newlist.append(oldlist[j - 1] + oldlist[j])
        oldlist = newlist
        if i != 0:
            mylist.append(oldlist)

    return mylist
