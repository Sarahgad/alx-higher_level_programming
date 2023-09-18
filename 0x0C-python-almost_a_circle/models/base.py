#!/usr/bin/python3
"""This class will be:
the “base” of all other classes in this project."""
import json
import csv
class Base:
    """ The goal of it is to manage id attribute
    in all your future classes and
    to avoid duplicating the same code
    (by extension, same bugs)"""
    __nb_objects = 0
    def __init__(self, id=None):
        """initialize id 
        Args: 
        id<int> public instance
        """
        self.id = id
        if self.id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """return json"""
        if list_dictionaries == None or list_dictionaries == {}:
            return "[]"
        else:
            jsonString = json.dumps(list_dictionaries)
            return jsonString
    
    @classmethod
    def save_to_file(cls, list_objs):
        """return list"""
        file  = cls.__name__ + ".json"
        with open(file, "w") as json_file:
            if list_objs == None:
                json_file.write("[]")
            else:
                list_json = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
                json_file.write(list_json)
    
    @staticmethod
    def from_json_string(json_string):
        """return list"""
        if json_string == None:
            return "[]"
        else:
            list_dict = json.loads(json_string)
            return list_dict

    @classmethod
    def create(cls, **dictionary):
        Rect = cls(1, 2, 3, 4)
        Rect.update(**dictionary)
        return Rect

    @classmethod
    def load_from_file(cls):
        file  = cls.__name__ + ".json"
        try:
            with open(file, "r") as json_newfile:
                json_data = json_newfile.read()
                json_list = cls.from_json_string(json_data)
                instance = [cls.create(**d) for d in json_list]
            return instance
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """return list"""
        file  = cls.__name__ + ".csv"
        with open(file, "w", newline="") as csv_file:
            csvString = csv.writer(csv_file)
            if list_objs == None:
                csv_file.writer.writrow("[]")
            else:
                csvString.writerow(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """return list"""
        file  = cls.__name__ + ".csv"
        with open(file, "r") as csv_file:
            csvString = csv.reader(csv_file)
            return csvString
        