#!/usr/bin/python3
class MyList(list):

    def print_sorted(self):
        if not all(isinstance(i, int) for i in self):
            raise TypeError("Contains non-integer elements")
        sorted_list = sorted(self)
        print(sorted_list)
