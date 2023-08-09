#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 != 0:
            print("{0} ".format("Fizz"), end="")
        elif i % 5 == 0 and i % 3 != 3:
            print("{0} ".format("Buzz"), end="")
        elif i % 3 == 0 and i % 5 != 0:
            print("{0} ".format("FizzBuzz"), end="")
        else:
            print("{0:d} ".format(i), end="")
