#!/usr/bin/python3
""" Defines a class called Square """


class Square:
    """ square class """
    def __init__(self, size=0):
        """ init function """
        self.__size = size

    @property
    def size(self):
        """ Getter for private attribute size """
        return self.__size

    @size.setter
    def size(self, value):
        """ setter for private attribute size """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ calculate the square """
        area = self.__size ** 2
        return area
