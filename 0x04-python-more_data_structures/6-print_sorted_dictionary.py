#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dict_sorte = dict(sorted(a_dictionary.items()))
    for k, v in dict_sorte.items():
        print("{0}: {1}".format(k, v))
