#!/usr/bin/python3
"""
Base Geometry Module

Defines a basic geometric class, BaseGeometry, with additional
validation method.

Class:
    BaseGeometry - Base class for geometric objects.

Methods:
    area() - Raises an exception indicating it is not implemented.
    integer_validator(name, value) - Validates that a value is an integer
    greater than 0.

Usage:
    Inherit from BaseGeometry to create specific geometric classes and
      implement the area method.
"""


class BaseGeometry:
    """Defines a basic geometric class, BaseGeometry."""

    def area(self):
        """
        Calculate the area of the geometric object.

        Raises:
            Exception: Indicates that this method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate that a value is an integer greater than 0.

        Args:
            name (str): The name of the variable.
            value: The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int) or type(value) is bool:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        return True
