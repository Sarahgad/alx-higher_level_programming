#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer

class max_integer_test (unittest.TestCase):
    
    def test_docmaxintegration(self):
        f = max_integer.__doc__
        self.assertTrue(len(f) > 2)

    def test_valuemaxintegration(self):
        """check of the correct value"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 2, -7, 4]), 4)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([3]), 3)
        self.assertEqual(max_integer([4, 2, -7, 1]), 4)
        self.assertEqual(max_integer([1, 3, 4, -7, 2]), 4)
        
    def test_none(self):
        """check for passing none as argument"""
        with self.assertRaises(TypeError):
            max_integer(None)
    
    def test_typemaxint(self):
        """check the type of value"""
        list = [1, 4, "alx", 6, 7] 
        with self.assertRaises(TypeError):
            max_integer(list)
    
    def test_nonelist(self):
        """check the empty list"""
        list = []
        self.assertIsNone(max_integer(list), None)


if __name__ == '__main__':
    """calling the unit test"""
    unittest.main() 
