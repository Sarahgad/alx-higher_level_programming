import unittest
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import pycodestyle
import sys
import io
import os
import tempfile
import json
"""test cases for Base module"""


class test_Base(unittest.TestCase):
    """this class to test the methods under the Base class"""

    def test_initialize(self):
        """initialize the class constructor"""
        r1 = Base()
        r2 = Base()
        self.assertEqual(r1.id, r2.id - 1)

    def test_threeargs(self):
        """three args"""
        r1 = Base()
        r2 = Base(12)
        r3 = Base()
        self.assertEqual(r1.id, r3.id - 1)
        self.assertEqual(r2.id, 12)
        self.assertEqual(r3.id, r1.id + 1)
    
    def test_twoarg(self):
        """two args"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_unique(self):
        b1 = Base()
        b2 = Base()
        self.assertNotEqual(b1.id, b2.id)

    def test_id_assignment_with_args(self):
        b1 = Base(10)
        b2 = Base(20)
        self.assertEqual(b1.id, 10)
        self.assertEqual(b2.id, 20)

    def test_id_negative_args(self):
        b1 = Base(-10)
        b2 = Base(-20)
        self.assertEqual(b1.id, -10)
        self.assertEqual(b2.id, -20)

    def test_id_assigment_zero(self):
        b = Base(0)
        self.assertEqual(b.id, 0)


class test_to_json_string(unittest.TestCase):
    """test the json string method"""
    def test_to_json_string_none(self):
        list_dictionary = None
        r1 = Base()
        jsonstring = r1.to_json_string(list_dictionary)
        self.assertEqual(jsonstring, '[]')

    def test_to_json_string_empty(self):
        list_dictionary2 = []
        result = Base.to_json_string(list_dictionary2)
        self.assertEqual(result, '[]')

    def test_to_json_not_empty(self):
        list_of_dictionary = [{"width": 2, "height": 4, "id": 1}, {"width": 3, "height": 5, "id": 2},
                                      {"size": 5, "id": 3}]
        json_string = Base.to_json_string(list_of_dictionary)
        expected_output = '[{"width": 2, "height": 4, "id": 1}, {"width": 3, "height": 5, "id": 2}, {"size": 5, "id": 3}]'
        self.assertEqual(json_string, expected_output)
class TestBase_save_to_file(unittest.TestCase):
    def test_save_to_empty_file(self):
        Square.save_to_file([])
        with open ("Square.json") as file:
            self.assertEqual('[]', file.read())

    def test_save_to_None_file(self):
        Square.save_to_file(None)
        with open ("Square.json") as file:
            self.assertEqual('[]', file.read())

    def test_save_to_empty_Rec(self):
        Rectangle.save_to_file([])
        with open ("Rectangle.json") as file:
            self.assertEqual('[]', file.read())

    def test_save_to_None_Rectangle(self):
        Rectangle.save_to_file(None)
        with open ("Rectangle.json") as file:
            self.assertEqual('[]', file.read())

    def test_save_to_oneRec(self):
        rect = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([rect])
        with open("Rectangle.json") as file:
            self.assertEqual(len(file.read()), 53)


    def test_save_to_TwoRec(self):
        rect1 = Rectangle(10, 7, 2, 8, 5)
        rect2 = Rectangle(4, 5, 6, 8, 7)
        Rectangle.save_to_file([rect1, rect2])
        with open("Rectangle.json") as file:
            self.assertEqual(len(file.read()), 105)

    def test_save_to_oneSeq(self):
        seq = Square(10, 7, 2, 5)
        Square.save_to_file([seq])
        with open("Square.json") as file:
            self.assertEqual(len(file.read()), 39)


    def test_save_to_TwoSq(self):
        sq1 = Square(10, 2, 8, 5)
        sq2 = Square(4, 6, 8, 7)
        Square.save_to_file([sq1, sq2])
        with open("Square.json") as file:
            self.assertEqual(len(file.read()), 77)

class TestBase_loadfromfile(unittest.TestCase):
    """tests for load from file"""
    def test_load_from_emptyfile(self):
        """non exists empty file"""
        if (os.path.exists("Rectangle.json") is True):
            os.remove("Rectangle.json")
        if (os.path.exists("Square.json") is True):
            os.remove("Square.json")
        if (os.path.exists("Base.json") is True):
            os.remove("Base.json")
        result = Rectangle.load_from_file()
        self.assertEqual(result, [])

         

        
if __name__ == '__main__':
    """calling the unit test"""
    unittest.main()
