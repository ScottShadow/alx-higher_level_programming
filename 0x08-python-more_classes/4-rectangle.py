#!/usr/bin/python3
"""Rectangle Class Module"""


class Rectangle:
    """Rectangle Object Class"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Parameters:
            value (int): The width value to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Parameters:
            value (int): The height value to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """
        Returns a string representation of the Rectangle, displaying
        its visual representation.

        The visual representation consists of rows of '#' characters,
          where each row represents
        the width of the rectangle, and the height is determined by
        the value of the height attribute.

        Returns:
        str: A string representing the visual representation of the R
        ectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")
        return (("#" * self.__width) + "\n") * (
            self.__height - 1) + ("#" * self.__width)

    def __repr__(self):
        """
        Returns a string representation of the Rectangle that can be
        used to recreate the object.

        Returns:
        str: A string representing the Rectangle in the format
        'Rectangle(width, height)'.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)
