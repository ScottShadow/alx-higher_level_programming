#!/usr/bin/python3
"""
Rectangle Geometry Module

Classes:
    Rectangle - Represents a rectangle with methods for initialization.

Usage:
    Create an instance of Rectangle, providing width and height values.
    Inherited from BaseGeometry, Rectangle includes integer validation
    for width and height.
"""

geometry_module = __import__('7-base_geometry')
BaseGeometry = getattr(geometry_module, 'BaseGeometry')


class Rectangle(BaseGeometry):
    """Defines a Rectangle class inheriting from BaseGeometry."""

    def __init__(self, width, height):
        """
        Constructor method for Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
        """
        base_geometry_instance = BaseGeometry()

        if base_geometry_instance.integer_validator("width", width):
            self.__width = width

        if base_geometry_instance.integer_validator("height", height):
            self.__height = height
