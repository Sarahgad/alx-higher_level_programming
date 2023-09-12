#!/usr/bin/python3
"""practicing on input/output python"""
import json


def save_to_json_file(my_obj, filename):
    """ returns the JSON
    representation of an
    object (string)"""
    with open(filename, 'w') as my_file:
        data = json.dump(my_obj, my_file)
        return data
