#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ordered_keys = []
    sorted_dictionary = {}
    for keys in a_dictionary:
        ordered_keys.append(keys)
    ordered_keys.sort()
    for element in ordered_keys:
        sorted_dictionary[element] = a_dictionary[element]
    for key, value in sorted_dictionary.items():
        print(f"{key}: {value}")
    return sorted_dictionary
