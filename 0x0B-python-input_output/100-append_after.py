#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    content = []
    with open(filename, 'r') as file:
        for line in file:
            content.append(line)
            if search_string in line:
                content.append(new_string)

    with open(filename, 'w') as file:
        file.writelines(content)
