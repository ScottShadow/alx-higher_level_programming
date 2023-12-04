#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    index = 0
    for element in my_list:
        if int(element) % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
