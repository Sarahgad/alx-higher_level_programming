#!/usr/bin/python3
"""practicing on input/output python"""
import json


def load_from_json_file(filename):
    """ returns the JSON
    representation of an
    object (string)"""
    with open(filename, 'r') as my_file:
        data = json.load(my_file)
    print (data)
