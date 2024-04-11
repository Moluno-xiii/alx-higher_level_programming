#!/usr/bin/python3
class Square:
    """ square class """
    def __init__(self, square_size=0):
        """ init function """
        self.__size = square_size

    @property
    def square_size(self):
        """ Getter for private attribute size """
        return self.__size

    @square_size.setter
    def square_size(self, value):
        """ setter for private attribute size """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ calculate the square """
        area = self.__size ** 2
