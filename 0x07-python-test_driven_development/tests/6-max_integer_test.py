#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer

class max_integer_test (unittest.TestCase):
    
    def test_docmaxintegration(self):
        f = max_integer.__doc__
        self.assertTrue(len(f) > 2)

    def test_valuemaxintegration(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 2, -7, 4]), 4)
        self.assertEqual(max_integer([]), None)

    
    def test_none(self):
        """Tests for passing none as argument"""
        with self.assertRaises(TypeError):
            max_integer(None)
    
    def test_typemaxint(self):
        list = [1, 4, "alx", 6, 7] 
        with self.assertRaises(TypeError):
            max_integer(list)
    
    def test_nonelist(self):
        list = []
        self.assertIsNone(max_integer(list), None)


if __name__ == '__main__':
    unittest.main() 
        


