#!/usr/bin/python3
"""
Module for Rectangle Class

This module defines the Rectangle class, a subclass of the Base class.

Classes:
    Rectangle: Represents a rectangle with width, height, x, y
    coordinates, and an identifier.

Attributes:
    display_character (str): The character used for displaying
    the rectangle.

Methods:
    __init__(self, width, height, x=0, y=0, id=None): Constructor
    method for initializing a Rectangle instance.
    area(self): Calculate and return the area of the rectangle.
    display(self): Display the rectangle using the specified
    character and dimensions.
    __str__(self): Return a string representation of the Rectangle
    object.
    update(self, *args, **kwargs): Update the attributes of the
    Rectangle object using either positional or keyword arguments.
    to_dictionary(self): Convert the Rectangle object to a dictionary.

Properties:
    width: Getter and setter for the width attribute.
    height: Getter and setter for the height attribute.
    x: Getter and setter for the x attribute.
    y: Getter and setter for the y attribute.

Inheritance:
    Inherits from the Base class.

"""
from .base import Base


class Rectangle(Base):
    """
    Rectangle Class

    Attributes:
        display_character (str): The character used for displaying the
        rectangle.
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the rectangle.
        y (int): The y-coordinate of the rectangle.
        id (int): The identifier of the rectangle.

    Methods:
        __init__(self, width, height, x=0, y=0, id=None): Constructor
          method for initializing a Rectangle instance.
        area(self): Calculate and return the area of the rectangle.
        display(self): Display the rectangle using the specified character
        and dimensions.
        __str__(self): Return a string representation of the Rectangle
        object.
        update(self, *args, **kwargs): Update the attributes of the
        Rectangle object using either positional or keyword arguments.
        to_dictionary(self): Convert the Rectangle object to a dictionary.

    Properties:
        width: Getter and setter for the width attribute.
        height: Getter and setter for the height attribute.
        x: Getter and setter for the x attribute.
        y: Getter and setter for the y attribute.

    Inheritance:
        Inherits from the Base class.
    """
    display_character = "#"

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor Method

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the rectangle.
            y (int): The y-coordinate of the rectangle.
            id (int): The identifier of the rectangle.

        Returns:
            None
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError(
                f"width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError(
                f"height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError(
                f"x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError(
                f"y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height

    def display(self):
        """
        Display the rectangle using the specified character and dimensions.

        Returns:
            None
        """
        for i in range(self.height+self.y):
            if i < self.y:
                print("")
            else:
                print(" " * self.x, end="")
                print(self.display_character * self.width)

    def __str__(self):
        """
        Return a string representation of the Rectangle object.

        Returns:
            str: A string representation of the Rectangle.
        """
        return f"[{__class__.__name__}] ({self.id}) {self.x}/{self.y} - \
            {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """
        Update the attributes of the Rectangle object using either
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
        Convert the Rectangle object to a dictionary.

        Returns:
            dict: A dictionary representation of the Rectangle object.
        """
        myself = {'x': self.x, 'y': self.y, 'id': self.id,
                  'height': self.height, 'width': self.width}
        return myself
