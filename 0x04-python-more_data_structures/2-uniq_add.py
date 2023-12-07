#!/usr/bin/python3
def uniq_add(my_list=[]):
    rez = 0
    new_list = my_list[:]
    for element in my_list:
        if new_list.count(element) != 1:
            new_list.remove(element)
    for element in new_list:
        rez += element
    return rez
