#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys


def myCalc():
    if len(sys.argv) == 4:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        op = sys.argv[2]
        if op == "+":
            rez = add(a, b)
        elif op == "-":
            rez = sub(a, b)
        elif op == "*":
            rez = mul(a, b)
        elif op == "/":
            rez = div(a, b)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        print("{} {} {} = {}".format(a, op, b, rez))
        sys.exit(0)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)


if __name__ == "__main__":
    myCalc()
