#!/usr/bin/python3
class  MyList(list):
    def __init__ (self):
        super().__init__()

    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list) 
