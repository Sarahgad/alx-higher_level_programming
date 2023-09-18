#!/usr/bin/python3
"""class Rectangle that inhrient from Base"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class constructor:
    width, height, x, y
    super class with id"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialize the square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter size"""
        return self.width

    @size.setter
    def size(self, value):
        """set the size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """upate the args and keywordargument"""

        attributes = ['id', 'size', 'x', 'y']
        if args:
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """return dict"""
        return {"id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y}

    def to_csv(self):
        """to csv"""
        return [self.id, self.size, self.x, self.y]

    @classmethod
    def from_csv(cls, row):
        """from csv"""
        id, size, x, y = row
        return cls(int(size), int(x), int(y), int(id))

    def __str__(self):
        """represent the object"""
        return "[Square] ({0}) {1}/{2} - {3}".format(self.id,
                                                     self.x,
                                                     self.y,
                                                     self.size)
