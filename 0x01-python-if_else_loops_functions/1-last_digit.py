#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num_str = repr(number)
if number == 0:
    digit = number
else:
    digit = int(num_str[-1]) * (number / abs(number))
if digit > 6:
    five = "and is greater than 5"
elif digit == 0:
    five = "and is 0"
else:
    five = "and is less than 6 and not 0"
print("Last digit of {0:.0f} is {1:.0f} {2}".format(number, digit, five))
