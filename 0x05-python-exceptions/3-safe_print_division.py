#!/usr/bin/python3
def safe_print_divison(a, b):
    try:
        result = a / b
    except (ValueError, ZeroDivisionError):
        passi
    finally:
        print("Inside result: {}".format(result))
    return result
