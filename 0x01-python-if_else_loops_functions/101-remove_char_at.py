#!/usr/bin/python3

def remove_char_at(str, n):
    str_2 = ''
    for i in range(len(str)):
        if i == n:
            continue
        else:
            str_2 += str[i]
    return (str_2)
