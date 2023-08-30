#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a Square instance.
        Args:
            size (int): the size of square.
            postition (Tuple)
        Raises size:
            TypeError: the size not integer
            ValueError: the size less that 0

        Raises:
            TypeError: the position must be of two positive integer
            ValueError: the posititon less that 0
        """
        self.__size = size
        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    @property
    def size(self):
        """to get the value of size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        to modifiy the value of size

        args:
                value: the value you can modify it
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """get th   e value of position"""
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates the area of the square.
        Returns:
        int: The area of the square.§:w
        """
        return self.__size ** 2

    def my_print(self):
        """that prints in stdout the square with the character #.
        if size is equal to 0, print an empty line
        position should be use by using space -
          Don’t fill lines by spaces when position[1] > 0
        """
        if self.__size == 0:
            print()
        else:
            if self.__position[1] > 0:
                for d in range(self.__position[1]):
                    print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for k in range(self.__size):
                    print("#", end="")
                print()
