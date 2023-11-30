#!/usr/bin/python3
from calculator_1 import *
import sys


def myCalc():
    if len(sys.argv) == 4:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        op = sys.argv[2]
        if op == "+":
            rez = add(a, b)
        elif sys.argv[2] == "-":
            rez = sub(a, b)
        elif op == "*":
            rez = mul(a, b)
        elif op == "/":
            rez = div(a, b)
        else:
            print("Usage: ./100-my_calculator.py <a> <operator> <b>")
            return 1
        print(rez)
        return 0
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        return 1


if __name__ == "__main__":
    myCalc()