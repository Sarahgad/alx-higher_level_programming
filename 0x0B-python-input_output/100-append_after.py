#!/usr/bin/python3
"""advanced task in i/o files"""


def append_after(filename="", search_string="", new_string=""):
    """insert the new string if you found the search string"""
    content = []
    with open(filename, 'r') as file:
        for line in file:
            content.append(line)
            if search_string in line:
                content.append(new_string)

    with open(filename, 'w') as file:
        file.writelines(content)
