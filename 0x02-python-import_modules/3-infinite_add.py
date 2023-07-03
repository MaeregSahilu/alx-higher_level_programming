#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum, n = 0, 1
    while n < len(sys.argv):
        sum += int(sys.argv[n])
        n += 1
    print(sum)
