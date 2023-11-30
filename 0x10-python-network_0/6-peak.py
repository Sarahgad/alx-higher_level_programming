#!/usr/bin/python3
"""Technical interview
my first solution worked but not effecient
def find_peak(list_of_integers):
    if list_of_integers == []:
        return None
    i = int(len(list_of_integers) / 2)
    if list_of_integers[i] > list_of_integers [i - 1] and \
   list_of_integers[i] > list_of_integers [i + 1]:
        return list_of_integers[i]
    if list_of_integers[i] >= list_of_integers [i - 1]
    and list_of_integers[i] < list_of_integers [i + 1]:
        for i in range(i, len(list_of_integers) - 1, 1):
            if list_of_integers[i] >= list_of_integers [i - 1] and \
   list_of_integers[i] >= list_of_integers [i + 1]:
                return list_of_integers[i]
    else:
         for i in range(0, i, 1):
            if list_of_integers[i] >= list_of_integers [i - 1] and \
   list_of_integers[i] >= list_of_integers [i + 1]:
                return list_of_integers[i]"""
"""Technical interview"""


def find_peak(list_of_integers):
    """find peak method"""
    if list_of_integers == []:
        return None
    low, high = 0, len(list_of_integers) - 1
    while low < high:
        mid = (high + low) // 2
        if list_of_integers[mid] >= list_of_integers[mid + 1]:
            high = mid
        else:
            low = mid + 1
    return list_of_integers[low]
