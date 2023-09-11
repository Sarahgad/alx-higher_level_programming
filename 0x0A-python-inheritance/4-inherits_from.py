#!/usr/bin/python3
"""constructed booling class"""


def inherits_from(obj, a_class):
    """return True if the object is instance of class
    or specified class"""

    return issubclass(type(obj), a_class) and type(obj) is not a_class
