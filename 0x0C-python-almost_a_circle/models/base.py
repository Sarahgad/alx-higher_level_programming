#!/usr/bin/python3
"""This class will be:
the “base” of all other classes in this project."""
import json
import csv
import turtle


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
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            jsonString = json.dumps(list_dictionaries)
            return jsonString

    @classmethod
    def save_to_file(cls, list_objs):
        """return list"""
        file = cls.__name__ + ".json"
        with open(file, "w") as json_file:
            if list_objs is None:
                json_file.write("[]")
            else:
                list_json = cls.to_json_string([obj.to_dictionary()
                                                for obj in list_objs])
                json_file.write(list_json)

    @staticmethod
    def from_json_string(json_string):
        """return list"""
        if json_string is None or json_string == "[]":
            return []
        else:
            list_dict = json.loads(json_string)
            return list_dict

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            Rect = cls(1, 2)
        else:
            Rect = cls(1)
        Rect.update(**dictionary)
        return Rect

    @classmethod
    def load_from_file(cls):
        file = cls.__name__ + ".json"
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
        """save to csv"""
        file = cls.__name__ + ".csv"
        with open(file, "w", newline='') as csv_file:
            if list_objs is None or list_objs == []:
                csv_file.write("[]")
            if cls.__name__ == "Rectangle":
                fieldnames = ["id", "width", "height", "x", "y"]
            else:
                fieldnames = ["id", "size", "x", "y"]

            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            for obj in list_objs:
                writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """load from file"""
        file = cls.__name__ + ".csv"
        instances = []
        try:
            with open(file, "r", newline='') as csv_newfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dict = csv.DictReader(csv_newfile, fieldnames=fieldnames)
                list_dict = [dict([k, int(v)] for k, v in d.items())
                             for d in list_dict]
                return [cls.create(**diction) for diction in list_dict]

        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """let's have fun with a turtule"""

        shap = turtle.Turtle()
        shap.shape("turtle")
        shap.color("green")
        shap.speed(1)

        wn = turtle.Screen()
        wn.bgcolor("black")
        wn.title("Sarah's shapes")

        for rect in list_rectangles:
            if rect.width <= 0 or rect.height <= 0:
                continue

            shap.fillcolor("yellow")
            shap.begin_fill()
            for _ in range(2):
                shap.forward(rect.width)
                shap.left(90)
                shap.forward(rect.height)
                shap.left(90)
            shap.end_fill()

        for square in list_squares:
            if square.size <= 0:
                continue

            shap.fillcolor("purple")
            shap.begin_fill()
            for _ in range(4):
                shap.forward(square.size)
                shap.left(90)
            shap.end_fill()

        turtle.done()
