#!/usr/bin/python3
import sys
if __name__ == "__main__":
    text = "argument"
    numOfArgs = len(sys.argv) - 1
    if numOfArgs == 0:
        print("{} {}s.".format(numOfArgs, text))
    else:
        if numOfArgs > 1:
            text = "arguments"
        print("{} {}:".format(numOfArgs, text))
        for argPassed in range(1, (numOfArgs + 1)):
            print("{}: {}".format(argPassed, sys.argv[argPassed]))
