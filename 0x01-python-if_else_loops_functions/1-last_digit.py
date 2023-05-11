#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num_str = repr(number)
last_digit = int(num_str[-1]) * (number / abs(number))
if last_digit > 6:
    abv_five = "and is greater than 5"
elif last_digit == 0:
    abv_five = "and is 0"
else:
    abv_five = "and is less than 6 and not 0"
print("Last digit of {0:.0f} is {1:.0f} {2}".format(number, last_digit, abv_five))
