#!/usr/bin/python3
def fuzzbuzz():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("Fizzbuzz ", end="")
        elif number % 3 == 0:
            print("Fizz ", end="")
        elif number % 5 == 0:
            print("Fizz ", end="")
        else:
            print("{} ".format(number), end="")
