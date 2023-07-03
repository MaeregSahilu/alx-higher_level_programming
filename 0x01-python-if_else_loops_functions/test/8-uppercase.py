#!/usr/bin/python3
def uppercase(str):
    a = ''
    for c in str:
        c = ord(c)
        if c >= 97 and c <= 122:
            a = a + chr(c - 32)
        else:
            a = a + chr(c)
    print(a)
