#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    size = 0
    try:
        if (x <= 0):
            return 0
        for i in range(x):
            print(my_list[i], end="")
            size += 1
        print()
        return (size)
    except IndexError:
        for i in my_list:
            pass
        print()
        return (size)
    except Exception:
        return 0
