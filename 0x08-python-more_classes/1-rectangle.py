#!/usr/bin/python3
""" Defines a class Rectangle """


class Rectangle:
    """ Class with setter and getter """
    def __init__(self, width=0, height=0):
        """ Init method """
        self.__width = width
        self.__height = height

    def width(self, value):
        """ Width setter """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def height(self, value):
        """ Height setter """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
