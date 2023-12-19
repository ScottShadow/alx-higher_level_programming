#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        num = fct(*args)
        return num
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
