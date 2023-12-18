#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    result = ""
    try:
        for i in range(x):
            result += str(my_list[i])
        print(result)
        return int(result)
    except IndexError:
        result = "".join(map(str, my_list))
        print(result)
        return int(result)
