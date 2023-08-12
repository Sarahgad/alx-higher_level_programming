#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None or my_list == []:
        print(" ", end="")
    elif len(my_list) == 1:
        print("{}".format(my_list[0]))
    else:
        my_list.reverse()
        for i in my_list:
            print("{:d}".format(i))
