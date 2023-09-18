#!/usr/bin/python3
"""class Rectangle that inhrient from Base"""
from models.base import Base


class Rectangle(Base):
    """Class constructor:
    width, height, x, y
    super class with id"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize the class constructor"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """get the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width"""
        if not type(value) is int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get the heights"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height"""
        if not type(value) is int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get the x"""
        return self.__x

    @x.setter
    def x(self, value):
        """set the x"""
        if not type(value) is int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get the y"""
        return self.__y

    @y.setter
    def y(self, value):
        """set the y"""
        if not type(value) is int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """calculate the area of rectangle"""
        return self.width * self.height

    def display(self):
        """display the rec with #"""
        [print() for _ in range(self.__y)]
        for h in range(self.__height):
            [print(" ", end="")for _ in range(self.__x)]
            [print("#", end="") for w in range(self.__width)]
            print()

    def __str__(self):
        """return string format"""
        return "[Rectangle] ({0}) {1}/{2} - {3}/{4}".format(self.id,
                                                            self.x,
                                                            self.y,
                                                            self.width,
                                                            self.height)

    def update(self, *args,  **kwargs):
        """upate the args and keywordargument"""

        attributes = ['id', 'width', 'height', 'x', 'y']
        if args:
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """return dict"""
        return {"id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y}

    def to_csv(self):
        """to csv"""
        return [self.id, self.width, self.height, self.x, self.y]

    @classmethod
    def from_csv(cls, row):
        """from csv"""
        id, width, height, x, y = row
        return cls(int(width), int(height), int(x), int(y), int(id))
