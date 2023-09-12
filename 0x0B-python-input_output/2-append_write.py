#!/usr/bin/python3
"""practicing on input/output python"""


def append_write(filename="", text=""):
    """append the string with encoding UTF8 and
    overwrite on the existing text
    Return the numbers of charchters"""

    with open(filename, 'a', encoding="UTF8") as myfile:
        char = myfile.write(text)
        return char
