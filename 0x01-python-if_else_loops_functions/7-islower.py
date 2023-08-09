#!/usr/bin/python3

def islower(c):

    for i in range(97, 124):
        if i == ord(c):
            break
    else:
        return False
    return True
