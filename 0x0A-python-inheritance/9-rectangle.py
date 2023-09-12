#!/usr/bin/python3
"""Full Rectangular"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """inhtrent class from base_geometry
        Args:
        width(int) the width of rectangulat
        height(int the height of rectangular)
    """

    def __init__(self, width, height):
        """initialize the private value"""

        self.__width = width
        self.__height = height
        super().integer_validator("width", self.__width)
        super().integer_validator("height", self.__height)

    def area(self):
        """over write area function"""
        return self.__width * self.__height

    def __str__(self):
        """using string method as amagic method"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
