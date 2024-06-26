#!/usr/bin/python3
""" Defines a class called Square """


class Square:
    """ square class """
    def __init__(self, size=0):
        """ init function """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ calculate the square """
        area = self.__size ** 2
        return area
