#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print("{0:d} is positive".format(number))
if number == 0:
    print("{0:d} is zero".format(number))
if number < 0:
    print("{0:d} is negative".format(number))
