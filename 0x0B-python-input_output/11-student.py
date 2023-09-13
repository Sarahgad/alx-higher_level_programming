#!/usr/bin/python3
""" Student module
"""


class Student:
    """Write a class Student that defines a student by:
    args:
        first_name
        last_name
        age
    """
    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """that retrieves
        a dictionary representation of a Student"""
        if attrs is None:
            return self.__dict__
        else:
            return {key: getattr(self, key)
                    for key in attrs if hasattr(self, key)}

    def reload_from_json(self, json):
        """that replaces all attributes
        of the Student instance
        First method
        #for attr in json:
        #    setattr(self, attr, json[attr])
        Second method
        #for key, value in json.items():
        #       self.__setattr__(key, value)
        Third method:
        # self.first_name = data['first_name']
        # self.last_name = data['last_name']
        # self.age = data['age']"""
        for attr in json:
            setattr(self, attr, json[attr])
