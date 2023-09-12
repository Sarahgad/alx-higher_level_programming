#!/usr/bin/python3
"""practicing on input/output python"""


def read_file(filename=""):
    """read the file with encoding UTF8"""

    with open(filename, encoding="UTF8") as myfile:
        print(myfile.read())
