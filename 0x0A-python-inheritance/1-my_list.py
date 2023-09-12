#!/usr/bin/python3
"""costruct class sorted list"""


class MyList(list):
    """class inhrenet from list class"""

    def __init__(self):
        """initized subclass"""
        super().__init__()

    def print_sorted(self):
        """printed sorted function"""

        sorted_list = sorted(self)
        print(sorted_list)
