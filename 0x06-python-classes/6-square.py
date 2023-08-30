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

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if not isinstance(position, tuple) or len(position) != 2 \
                or not all(isinstance(v, int) and v >= 0 for v in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

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

    @property
    def position(self):
        """get th   e value of position"""
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 \
                or not all(isinstance(v, int) and v >= 0 for v in value):
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
            print("")
            return

        [print("")for i in range(0, self.__position[1])]
        for j in range(0, self.__size):
            [print("_", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0,self.__size)]
            print("")

#!/usr/bin/python3
Square = __import__('6-square').Square

my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")