#!/usr/bin/python3
import sys
if __name__ == "__main__":
    rez = 0
    numArgs = len(sys.argv)
    for element in range(1, numArgs):
        rez = rez + int(sys.argv[element])
    print(rez)
