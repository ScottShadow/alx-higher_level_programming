#!/usr/bin/python3
islower = __import__('7-islower').islower


def uppercase(str):
    for char in str:
        if islower(char):
            char = chr(ord(char) - 32)
        print(f"{char}", end='')
    print("")
