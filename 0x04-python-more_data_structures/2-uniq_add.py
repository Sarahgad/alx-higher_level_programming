#!/usr/bin/python3
def uniq_add(my_list=[]):
    a = set(my_list)
    count = 0
    for i in a:
        count += i
    return (count)
