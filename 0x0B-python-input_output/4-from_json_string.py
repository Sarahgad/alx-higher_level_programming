#!/usr/bin/python3
"""practicing on input/output python"""
import json


def from_json_string(my_str):
    """ returns the JSON
    representation of an
    object (string)"""
    data = json.loads(my_str)
    return data
