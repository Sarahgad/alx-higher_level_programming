#!/usr/bin/python3
"""a class LockedClass with no class or object attribute"""


class LockedClass:
    """ locked class except slot "first_name" """
    __slots__ = ["first_name"]
