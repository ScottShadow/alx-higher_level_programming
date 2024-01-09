#!/usr/bin/python3
"""
Rectangle Geometry Module

Defines a Rectangle class inheriting from BaseGeometry.

Class:
    Rectangle - Represents a rectangle with methods for initialization,
                string representation, and area calculation.

Usage:
    Create an instance of Rectangle, providing width and height values.
    Inherited from BaseGeometry, Rectangle includes integer validation
    for width and height.

Methods:
    __str__() - Returns a string representation of the rectangle.
    area() - Calculates and returns the area of the rectangle.
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
        if self.integer_validator("width", width):
            self.width = width

        if self.integer_validator("height", height):
            self.height = height

    def __str__(self):
        """Returns a string representation of the rectangle."""
        return f"[{self.__class__.__name__}] {self.width}/{self.height}"

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.width * self.height
