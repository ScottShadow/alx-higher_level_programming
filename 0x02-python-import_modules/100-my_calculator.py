#!/usr/bin/python3
from calculator_1 import *
import sys


def myCalc():
    if len(sys.argv) == 4:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if sys.argv[2] == "+":
            rez = add(a, b)
        elif sys.argv[2] == "-":
            rez = sub(a, b)
        elif sys.argv[2] == "*":
            rez = mul(a, b)
        elif sys.argv[2] == "/":
            rez = div(a, b)
        print(rez)
        return rez
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        return 1


if __name__ == "__main__":
    myCalc()
