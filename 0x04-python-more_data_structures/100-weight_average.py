#!/usr/bin/python3
def weight_average(my_list=[]):
    rez = 0
    total_weight = 0
    if bool(my_list):
        for element in my_list:
            rez += element[0] * element[1]
            total_weight += element[1]
        rez = rez / total_weight
    return (rez)
