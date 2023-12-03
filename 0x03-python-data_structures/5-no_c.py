#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    if my_string is None:
        return None
    for element in my_string:
        if element == "c" or element == "C":
            continue
        else:
            new_string += element
    return new_string
