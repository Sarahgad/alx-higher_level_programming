#!/usr/bin/python3
"""costruct class sorted list"""


class BaseGeometry:
    """Base Class"""

    def area(self):

        """return Exception raises"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """that validates value:"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
bg = BaseGeometry()

try:
    bg.integer_validator("name", True)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))