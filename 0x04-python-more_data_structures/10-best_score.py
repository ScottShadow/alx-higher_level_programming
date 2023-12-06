#!/usr/bin/python3
def best_score(a_dictionary):
    if bool(a_dictionary):
        max_val = 0
        max_val_key = ""
        for key in a_dictionary:
            if a_dictionary[key] > max_val:
                max_val = a_dictionary[key]
                max_val_key = key
        return max_val_key
    else:
        return None
