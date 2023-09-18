#!/usr/bin/python3
import unittest
from models.base import Base
"""test cases for Base module"""


class test_Base(unittest.TestCase):
    """this class to test the methods under the Base class"""

    def setUp(self):
        self.b1 = Base()
        self.b2 = Base(5)
        self.b3 = Base(-1)
        self.b4 = Base(12)
        self.b5 = Base(0)
        self.b6 = Base(7000000000000000)
        self.b7 = Base()
        self.b8 = Base(3)

    def test_initialize(self):
        """initialize the class constructor"""

        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 5)
        self.assertEqual(self.b3.id, -1)
        self.assertEqual(self.b4.id, 12)
        self.assertEqual(self.b5.id, 0)
        self.assertEqual(self.b6.id, 7000000000000000)
        self.assertEqual(self.b7.id, 2)
        self.assertEqual(self.b8.id, 3)


if __name__ == '__main__':
    """calling the unit test"""
    unittest.main() 
