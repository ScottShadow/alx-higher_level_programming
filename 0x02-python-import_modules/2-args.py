#!/usr/bin/python3
import sys
if __name__ == "__main__":
    numOfArgs = len(sys.argv)
    if numOfArgs == 0:
        print("{} arguments.".format(numOfArgs - 1))
    else:
        print("{} argument:".format(numOfArgs - 1))
        for argPassed in range(1, numOfArgs):
            print("{}: {}".format(argPassed, sys.argv[argPassed]))
