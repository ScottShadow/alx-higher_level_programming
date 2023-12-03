#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list is None:
        return None
    if 0 > idx >= len(my_list):
        return my_list.copy()
    else:
        my_new_list = my_list.copy()
        my_new_list[idx] = element
        return my_new_list
