#!/usr/bin/python3
"""
Module for Square Class

This module defines the Square class, a subclass of the Rectangle class.

Classes:
    Square: Represents a square with equal width and
    height, inheriting from Rectangle.

Methods:
    __init__(self, size, x=0, y=0, id=None): Constructor
      method for initializing a Square instance.
    __str__(self): Return a string representation of the
      Square object.
    update(self, *args, **kwargs): Update the attributes
    of the Square object using either positional or keyword arguments.
    to_dictionary(self): Convert the Square object to a
    dictionary.

Properties:
    size: Getter and setter for the size attribute.

Inheritance:
    Inherits from the Rectangle class.

"""
from .base import *
from .rectangle import *


class Square(Rectangle):
    """
    Square Class

    Attributes:
        size (int): The size of the square.
        x (int): The x-coordinate of the square.
        y (int): The y-coordinate of the square.
        id (int): The identifier of the square.

    Methods:
        __init__(self, size, x=0, y=0, id=None): Constructor
        method for initializing a Square instance.
        __str__(self): Return a string representation of the

        Square object.
        update(self, *args, **kwargs): Update the attributes
        of the Square object using either positional or keyword arguments.
        to_dictionary(self): Convert the Square object to a
        dictionary.

    Properties:
        size: Getter and setter for the size attribute.

    Inheritance:
        Inherits from the Rectangle class.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor Method

        Args:
            size (int): The size of the square.
            x (int): The x-coordinate of the square.
            y (int): The y-coordinate of the square.
            id (int): The identifier of the square.

        Returns:
            None
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Return a string representation of the Square object.

        Returns:
            str: A string representation of the Square.
        """
        return f"[{__class__.__name__}] ({self.id}) \
            {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """
        Getter method for the size attribute.

        Returns:
            int: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.

        Args:
            value (int): The new size value.

        Returns:
            None
        """
        super(Square, Square).width.fset(self, value)
        super(Square, Square).height.fset(self, value)

    def update(self, *args, **kwargs):
        """
        Update the attributes of the Square object using either
        positional or keyword arguments.

        Args:
            *args: Positional arguments.
            **kwargs: Keyword arguments.

        Returns:
            None
        """
        if len(args) != 0:
            for (key, _), arg in zip(self.__dict__.items(), args):
                setattr(self, key, arg)
        elif len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Convert the Square object to a dictionary.

        Returns:
            dict: A dictionary representation of the Square object.
        """
        myself = {'id': self.id, 'x': self.x, 'size': self.width, 'y': self.y
                  }
        return myself
