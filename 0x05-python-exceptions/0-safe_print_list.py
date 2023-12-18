#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        if (x <= 0):
            return 0
        for i in range(x):

            print("{:d}".format(my_list[i]), end="")
        print()
        return my_list[i]
    except IndexError:
        for i in my_list:
            pass
        print()
        return i
    except Exception:
        return 0
