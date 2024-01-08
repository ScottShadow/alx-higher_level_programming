#!/usr/bin/python3
"""
Inheritance Check Module

This module defines a function, inherits_from, to check if an object
inherits (directly or indirectly) from a specified class
(excluding direct instances).
"""


def inherits_from(obj, a_class):
    """
    Check if an object inherits from a specified class
    (excluding direct instances).

    Args:
        obj: The object to be checked.
        a_class: The class to check for inheritance.

    Returns:
        bool: True if the object inherits from the specified class,
              excluding direct instances; otherwise, False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
