#!/usr/bin/python3
"""practicing on input/output python"""
import json


def to_json_string(my_obj):
    """ returns the JSON
    representation of an
    object (string)"""
    data = json.dumps(my_obj)
    return data
