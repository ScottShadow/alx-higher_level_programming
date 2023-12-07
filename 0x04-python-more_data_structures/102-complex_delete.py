#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    temp_dictionary = {**a_dictionary}
    for key in temp_dictionary:
        if temp_dictionary[key] == value:
            del a_dictionary[key]
    return a_dictionary
