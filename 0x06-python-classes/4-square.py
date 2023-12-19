#!/usr/bin/python3
"""Module for Square Class"""


class Square:
    """Square Class Defined"""

    def __init__(self, size=0):
        """Constructor Method
        Args:
            size: the size of the side of the square
            """
        self.size = size

    def area(self):
        """Method For computing Area
        Returns:
            int: Area, side squared
        """
        return self.__size * self.__size

    @property
    def size(self):
        """Getter method for size
        Returns:
            int: value of the variable size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for size
        Args:
            size: the length of the side of the square
        Returns:
            int: value of size"""
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value
        return self.__size
