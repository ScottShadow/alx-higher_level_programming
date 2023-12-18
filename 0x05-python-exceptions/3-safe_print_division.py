#!/usr/bin/python3
def safe_print_division(a, b):
    rez = 0
    try:
        rez = a / b
    except ZeroDivisionError:
        rez = None
    finally:
        print("Inside result: {}".format(rez))
    return rez
