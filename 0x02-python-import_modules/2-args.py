#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("0 argumets.".format(len(sys.argv)))
    elif len(sys.argv) == 2:
        print("1 argument: \n1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(len(sys.argv)-1))
        n = 1
        while n < len(sys.argv):
            print("{}: {}".format(n, sys.argv[n]))
            n += 1
