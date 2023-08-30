#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes a Square instance.
        Args:
            size (int): the size of square.
        Raises:
            TypeError: the size not integer
            ValueError: the size less that 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """to get the value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """
        to modifiy the value of size

        args:
                value: the value you can modify it
        """
        if not type(value) is int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of the square.

        Returns:
        int: The area of the square.

        """
        return self.__size ** 2

    def my_print(self):
        """that prints in stdout the square with the character #.
        if size is equal to 0, print an empty line
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end="")
                print()
