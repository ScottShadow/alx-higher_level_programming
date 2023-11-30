#!/usr/bin/python3
import sys
if __name__ == "__main__":
    numOfArgs = len(sys.argv) - 1
    if numOfArgs == 0:
        print("{} arguments.".format(numOfArgs))
    else:
        print("{} argument:".format(numOfArgs))
        for argPassed in range(1, (numOfArgs + 1)):
            print("{}: {}".format(argPassed, sys.argv[argPassed]))
