#!/usr/bin/python3
"""multiple inhrient"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """implement all in Rectangle by using size
    Args:
    size(int)
    """
    def __init__(self, size):
        """initialize the size as a private valid int"""

        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """over ride to the area for square"""

        return self.__size ** 2

    def __str__(self):
        """return the value of base class"""

        return super().__str__()
