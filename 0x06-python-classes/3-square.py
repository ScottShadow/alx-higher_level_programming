#!/usr/bin/python3
"""Module for Square Class"""


class Square:
    """Square Class Defined"""

    def __init__(self, size=0):
        """Constructor Function
        Args:
            size: lenght of side of square
        """
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Method that calculates area
        Returns:
            int: size squared , else 0
        """
        return self.__size * self.__size
