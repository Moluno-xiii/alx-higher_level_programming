#!/usr/bin/python
""" create function to add numbers """


def add_integer(a, b=98):
    """ adds two numbers togther """
    if type(a) != int:
        raise TypeError("a must be an integer")
    elif type(b) != int:
        raise TypeError("b must be an integer")
    else:
        result = int(a) + int(b)
        return result
