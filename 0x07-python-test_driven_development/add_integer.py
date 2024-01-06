#!/usr/bin/python3
""" Math Module"""


def add_integer(a, b=98):
    """Add Function Adds two integer
    Returns a + b

    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    if b is not None:
        b = int(b)
    return a + b
