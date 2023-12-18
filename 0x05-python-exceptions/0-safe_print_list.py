#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
        print()
        return my_list[i]
    except IndexError:
        for i in my_list:
            pass
        if x > 0:
            print()
            return i
    except Exception as e:
        print(f"Error: {e}")
        return 0
