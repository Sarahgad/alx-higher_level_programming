import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import pycodestyle
import sys
import io
"""test cases for Base module"""


class testCodeFormat(unittest.TestCase):

    def test_Squarmodule(self):
        """Test that we conform to PEP-8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/base.py',
                                    'tests/test_models/test_base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


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


class test_to_json_string(unittest.TestCase):
    """test the json string method"""
    def test_baseclass(self):
        list_dictionary = None
        r1 = Base()
        jsonstring = r1.to_json_string(list_dictionary)
        self.assertEqual(jsonstring, '[]')


if __name__ == '__main__':
    """calling the unit test"""
    unittest.main()
