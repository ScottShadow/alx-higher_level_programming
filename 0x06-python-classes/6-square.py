#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if (type(value) != int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value
        return self.__size

    def my_print(self):
        max_size = 0
        if self.__size == 0:
            print()
            return
        else:
            max_size = self.__size + self.__position[0]
            for i in range(max_size):
                for j in range(max_size):
                    if (j < self.__position[0] and self.__position[1] <= 0):
                        print(" ", end="")
                    else:
                        print("#", end="")
                print()

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(i, int) for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
