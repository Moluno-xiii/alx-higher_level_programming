#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
match last_digit:
    case digit if digit > 5:
        print(f'Last digit of {number} is {last_digit} and is greater than 5')
    case 0:
        print(f'Last digit of {number} is {last_digit} and is 0')
    case digit if 0 < digit < 6:
        print(f'Last digit of {number} is {last_digit} '
                f'and is less than 6 and not 0')
    case _:
        print('nothing happened')
