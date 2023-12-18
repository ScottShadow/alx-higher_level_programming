#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    rez = 0
    if x == 0:
        print(None)
        return 0
    try:
        for i in range(x):
            rez = rez*10 + my_list[i]
        print(rez)
        return (my_list[i])
    except IndexError:
        rez = 0
        for i in my_list:
            rez = rez*10 + i
        print(rez)
        return (i)
