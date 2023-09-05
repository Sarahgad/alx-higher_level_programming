#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer

class max_integer_test (unittest.TestCase):
    def test_typeint(self):
        self.assertIsInstance(max_integer(list=[]) ,list)


