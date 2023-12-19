#!/usr/bin/python3
"""Module for Square Class"""


class Square:
    """Square Class Defined"""

    def __init__(self, size=0, position=(0, 0)):
        """Constructor Method
        Args:
            size: the size of the side of the square
            position: the position of the square
            """
        self.size = size
        self.position = position

    def area(self):
        """Method For computing Area
        Returns: Area, side squared
        """
        return self.__size * self.__size

    @property
    def size(self):
        """Getter method for size
        Returs: value of the variable size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for size
        Args:
            size: the length of the side of the square
        Returns: value of size"""
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value
        return self.__size

    @property
    def position(self):
        """Getter method for position
        Returns: the value of position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method for position
        Args:
            value: the new value to set to position
        Returns: the new value of positions"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Square printer method, prints out the
            square base on size dimension"""
        if self.__size == 0:
            print()
            return
        [print("_") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print("=", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
