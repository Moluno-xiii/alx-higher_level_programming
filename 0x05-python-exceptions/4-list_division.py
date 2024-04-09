#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []

    for i in range(list_length):
        try:
            values = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            values = 0
        except ZeroDivisionError:
            print("division by 0")
            values = 0
        except IndexError:
            print("out of range")
            values = 0
        finally:
            new_list.append(values)
    return new_list
