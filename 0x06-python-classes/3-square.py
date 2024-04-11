#!/usr/bin/python3
class Square:
    """ square class """
    def __init__(self, square_size):
        """ init function """
        if type(square_size) is not int:
            raise TypeError("size must be an integer")
        elif square_size < 0:
            raise ValueError("size must be >= 0")
        self.__size = square_size

    def area(self):
        """ calculate the square """
        area = math.pow(self.size, 2)
