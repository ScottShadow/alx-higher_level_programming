#!/usr/bin/python3
def max_integer(my_list=[]):
    max_val = 0
    for element in my_list:
        if element > max_val:
            max_val = element
    return max_val
