#!/usr/bin/python3
"""Rectangle Class Module"""


class Rectangle:
    """Rectangle Object Class"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        if isinstance(self.print_symbol, list):
            symbol_str = '[' + \
                ', '.join(f"'{item}'" for item in self.print_symbol
                          ) + ']'
        else:
            symbol_str = str(self.print_symbol)

        return ((symbol_str * self.__width) + "\n") * (
            self.__height - 1) + (symbol_str * self.__width)

    def __repr__(self):
        """
        Returns a string representation of the Rectangle that can be
        used to recreate the object.

        Returns:
        str: A string representing the Rectangle in the format
        'Rectangle(width, height)'.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Destructor method for the Rectangle class.

        Prints a farewell message when the Rectangle object is deleted.

        Note:
         This method is automatically called when the object is about
         to be destroyed.

        Returns:
          None
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares two Rectangle objects based on their areas and returns
          the larger or equal one.

        Parameters:
            rect_1 (Rectangle): The first Rectangle object.
            rect_2 (Rectangle): The second Rectangle object.

        Raises:
            TypeError: If either rect_1 or rect_2 is not an instance of
            Rectangle.

        Returns:
            Rectangle: The Rectangle object with the larger or equal area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_2.area() > rect_1.area():
            return rect_2
        elif rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_1
