#!/usr/bin/python3
"""creat a Rectangle class """


class Rectangle:
    """Difention of class Rectangle
        Args:
        width(int): the width of rectangle
        height(int): the hight of rectangle
        number_of_instances (int)
        print_symbol can be any type
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """intialize the variable of rectangle"""
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """get the value of the width

        Return: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """reset the value of the width
            Args:
            value: the new value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get the value of the width

        Return: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """reset the value of the height
            Args:
            value: the new value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return area of rectangle"""
        return self.width * self.height

    def perimeter(self):
        """return perimeter of rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """return str with '#'
        Args: str(str)
        """
        if self.width == 0 or self.height == 0:
            return ""
        v = ""
        for i in range(self.height):
            v += (str(self.print_symbol) * self.width)
            v += "\n"
        return v[:-1]

    def __repr__(self):
        """returns the value of rectangle"""

        return "Rectangle({0}, {1})".format(self.width, self.height)

    def __del__(self):
        """print the destroy message"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
