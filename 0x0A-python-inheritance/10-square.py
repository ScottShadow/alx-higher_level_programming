#!/usr/bin/python3
"""
Square Geometry Module

Defines a Square class inheriting from Rectangle.
Usage:
    Create an instance of Square, providing a size value.
    Inherited from Rectangle, Square automatically sets the width and
    height to the same size.

Methods:
    area() - Calculates and returns the area of the square, utilizing
    the area method from the parent class.
"""
rectangle_module = __import__('9-rectangle')
Rectangle = getattr(rectangle_module, 'Rectangle')


class Square(Rectangle):
    """
    Square - Represents a square with methods for initialization and
    area calculation.
    """

    def __init__(self, size):
        """
        Constructor method for Square.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        super().__init__(size, size)

    def area(self):
        """
        Calculate the area of the square using the area method from
          the parent class.

        Returns:
            int: Area of the square, side squared.
        """
        return super().area()
