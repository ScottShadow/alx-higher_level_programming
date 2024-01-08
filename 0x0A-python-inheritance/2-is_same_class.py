#!/usr/bin/python3
"""
Type Check Module

This module defines a function, is_same_class, to check if an object
is an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Check if an object is an instance of a specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to check against.

    Returns:
        bool: True if the object is an instance of the specified class,
              otherwise False.
    """
    if type(obj) is a_class:
        return True
    else:
        return False
