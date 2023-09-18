"""test case for square module"""
import unittest
import pycodestyle
import sys
import io
from models.square import Square


class testCodeFormat(unittest.TestCase):

    def test_Squarmodule(self):
        """Test that we conform to PEP-8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/square.py',
                                    'tests/test_models/test_square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class test_Square(unittest.TestCase):
    """this class test the cases under the Square method"""
    def test_initializtion(self):
        """test the  initializtion method"""
        r1 = Square(10, 2)
        r2 = Square(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

        r3 = Square(10, 2, 0, 12)
        self.assertEqual(r3.id, 12)


if __name__ == '__main__':
    """calling the unit test"""
    unittest.main()
