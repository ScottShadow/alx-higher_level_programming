#!/usr/bin/python3
"""
Module for MyList Class
"""


class MyList(list):
    """
    Representation of a Custom MyList Object Type
    """

    def print_sorted(self):
        if not all(isinstance(i, int) for i in self):
            raise TypeError("Contains non-integer elements")
        sorted_list = sorted(self)
        print(sorted_list)
