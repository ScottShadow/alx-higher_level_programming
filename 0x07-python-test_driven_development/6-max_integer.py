#!/usr/bin/python3
def max_integer(list=[]):
    if not all((isinstance(i, int)) for i in list):
        raise TypeError("List must (list of ints)")
    if not list:
        return None
    max_value = list[0]
    for i in list:
        if max_value < i:
            max_value = i
    return max_value
