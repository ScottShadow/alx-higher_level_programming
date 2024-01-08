#!/usr/bin/python3
"""
Base Geometry Module


Class:
    BaseGeometry - Base class for geometric objects.

Methods:
    area() - Raises an exception indicating it is not implemented.

Usage:
    Inherit from BaseGeometry to create specific geometric classes
      and implement the area method.
"""


class BaseGeometry:
    """Defines a basic geometric class, BaseGeometry."""

    def area(self):
        """area class unimplemented"""
        raise Exception("area() is not implemented")
