#!/usr/bin/python3
""" Defines a Rectangle class """


class Rectangle:
    """ Class with setter and getter """
    def __init__(self, width=0, height=0):
        """ Init method """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """ Width Getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ Width setter """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Height Getter """
        return self.__heigt

    @height.setter
    def height(self, value):
        """ Height setter """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        area = int(self.__width) * int(self.__height)
        return area

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            perimeter = 0
            return perimeter
        else:
            perimeter = 2 * (int(self.__width) + int(self.__height))
            return perimeter

    def __str__(self):
        """Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = '#' * self.__width + '\n'
        return rect * (self.__height - 1) + '#' * self.__width
