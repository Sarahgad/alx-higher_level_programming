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
        result = style.check_files(['models/square.py'])
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

class test_SquareRaise(unittest.TestCase):
    """test the validation of getter and setter"""

    def test_ValueRaise(self):
        """"test the validation of instantiation"""
        s1 = Square(10, 2)
        with self.assertRaises(ValueError):
            s1.size = -10
        with self.assertRaises(ValueError):
            s1.size = -5
        with self.assertRaises(ValueError):
            s1.x = -7
        with self.assertRaises(ValueError):
            s1.y = -10
        with self.assertRaises(ValueError):
            s1.size = 0
        with self.assertRaises(ValueError):
            s1.size = 0
        with self.assertRaises(ValueError):
            self.s4 = Square(-10, 2, 0)
        with self.assertRaises(ValueError):
            self.s4 = Square(10, -2, 0)
        with self.assertRaises(ValueError):
            self.s4 = Square(10, 2, -3)
        with self.assertRaises(ValueError):
            self.s4 = Square(0, 2, 0)

    def test_TypeStringRaise(self):
        r1 = Square(10, 2)
        with self.assertRaises(TypeError):
            r1.size = "2"
        with self.assertRaises(TypeError):
            r1.size = "hello"
        with self.assertRaises(TypeError):
            r1.x = "2"
        with self.assertRaises(TypeError):
            r1.y = "2"
        with self.assertRaises(TypeError):
            self.r4 = Square("10", 2, 0)
        with self.assertRaises(TypeError):
            self.r4 = Square(10, "2", 0)
        with self.assertRaises(TypeError):
            self.r4 = Square(10, 2, "0")

    def test_TypeTupleRaise(self):
        r1 = Square(10, 2)
        with self.assertRaises(TypeError):
            r1.size = (2,)
        with self.assertRaises(TypeError):
            r1.x = (2,)
        with self.assertRaises(TypeError):
            r1.y = (2,)
        with self.assertRaises(TypeError):
            r1.size = (2,)
        with self.assertRaises(TypeError):
            self.r4 = Square((10,), 2, 0)
        with self.assertRaises(TypeError):
            self.r4 = Square(10, (2,), 0)
        with self.assertRaises(TypeError):
            self.r4 = Square(10, 2, (0,))

    def test_TypeListRaise(self):
        r1 = Square(10, 2)
        with self.assertRaises(TypeError):
            r1.size = [2]
        with self.assertRaises(TypeError):
            r1.size = [2]
        with self.assertRaises(TypeError):
            r1.x = [2]
        with self.assertRaises(TypeError):
            r1.y = [2]
        with self.assertRaises(TypeError):
            self.r4 = Square([10], 2, 0)
        with self.assertRaises(TypeError):
            self.r4 = Square(10, [2], 0)
        with self.assertRaises(TypeError):
            self.r4 = Square(10, 2, [0])

    def test_TypeSetRaise(self):

        r1 = Square(10, 2)

        with self.assertRaises(TypeError):
            r1.size = {2}
        with self.assertRaises(TypeError):
            r1.size = {2}
        with self.assertRaises(TypeError):
            r1.x = {2}
        with self.assertRaises(TypeError):
            r1.y = {2}
        with self.assertRaises(TypeError):
            self.r4 = Square({10}, 2, 0)
        with self.assertRaises(TypeError):
            self.r4 = Square(10, {2}, 0)
        with self.assertRaises(TypeError):
            self.r4 = Square(10, 2, {0})

    def test_TypeDictRaise(self):
        r1 = Square(10, 2)

        with self.assertRaises(TypeError):
            r1.size = {2: 5}
        with self.assertRaises(TypeError):
            r1.size = {2: 5}
        with self.assertRaises(TypeError):
            r1.x = {2: 5}
        with self.assertRaises(TypeError):
            r1.y = {2: 5}
        with self.assertRaises(TypeError):
            self.r4 = Square({'ky': 3}, 2, 0)
        with self.assertRaises(TypeError):
            self.r4 = Square(10, {'ky': 3}, 0)
        with self.assertRaises(TypeError):
            self.r4 = Square(10, 2, {'ky': 3})

    def test_TypefloatRaise(self):
        r1 = Square(10, 2)

        with self.assertRaises(TypeError):
            r1.size = 1.5
        with self.assertRaises(TypeError):
            r1.size = 1.55555555555555555
        with self.assertRaises(TypeError):
            r1.x = 1.5
        with self.assertRaises(TypeError):
            r1.y = 1.5
        with self.assertRaises(TypeError):
            self.r4 = Square(10.5, 2, 0)
        with self.assertRaises(TypeError):
            self.r4 = Square(10, 4.5, 0)
        with self.assertRaises(TypeError):
            self.r4 = Square(10, 2, 5.4)

    def test_TypeBoolenRaise(self):
        r1 = Square(10, 2)
        with self.assertRaises(TypeError):
            r1.size = True
        with self.assertRaises(TypeError):
            r1.size = False
        with self.assertRaises(TypeError):
            r1.x = True
        with self.assertRaises(TypeError):
            r1.y = True
        with self.assertRaises(TypeError):
            self.r4 = Square(True, 2, 0)
        with self.assertRaises(TypeError):
            self.r4 = Square(10, True, 0)
        with self.assertRaises(TypeError):
            self.r4 = Square(10, 2, True)

class test_sqArea(unittest.TestCase):
    """test the area of Rectangle"""

    def test_area(self):
        """test for area method"""
        r1 = Square(10)
        r2 = Square(3)
        r3 = Square(7, 8, 0, 12)
        self.assertEqual(r1.area(), 100)
        self.assertEqual(r2.area(), 9)
        self.assertEqual(r3.area(), 49)

    def test_raisesarea(self):
        with self.assertRaises(TypeError):
            r4 = Square()
        with self.assertRaises(AttributeError):
            Square.area(self)
        with self.assertRaises(TypeError):
            r5 = Square(1, 2, 3, 5, 8)
        with self.assertRaises(UnboundLocalError):
            r5.area(self)

class test_Recdisplay(unittest.TestCase):

    def test_emptyrec(self):
        with self.assertRaises(TypeError):
            r1 = Square()
        with self.assertRaises(TypeError):
            Square.display()

    def test_oneargrec(self):
        with self.assertRaises(TypeError):
            r2 = Square(2, 7, 5, 6, 6, 7)
        with self.assertRaises(TypeError):
            Square.display()    

    def test_print_1(self):
        output = "###\n###\n###\n"
        captured_output = io.StringIO()
        sys.stdout = captured_output
        r1 = Square(3)
        r1.display()
        sys.stdout = sys.__stdout__  # Restore stdout
        self.assertEqual(captured_output.getvalue(), output)

    def test_print_2(self):
        output = "####\n####\n####\n####\n"
        captured_output = io.StringIO()
        sys.stdout = captured_output
        r1 = Square(4)
        r1.display()
        sys.stdout = sys.__stdout__  # Restore stdout
        self.assertEqual(captured_output.getvalue(), output)

class test_stringmethod(unittest.TestCase):
    def test_fullarguments(self):
        r1 = Square(4, 6, 2, 1)
        expected_string = "[Square] (1) 6/2 - 4"
        self.assertEqual(str(r1), expected_string)

    def test_midarguments(self):
        r10 = Square(4, 6, 5, 5)
        expected_string = "[Square] (5) 6/5 - 4"
        self.assertEqual(str(r10), expected_string)

    def test_minarguments(self):
        r11 = Square(6, 5, 7, 23)
        expected_string = "[Square] (23) 5/7 - 6"
        self.assertEqual(str(r11), expected_string)

class test_updateargs(unittest.TestCase):
    def test_regularupdate(self):
        r1 = Square(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual("[Square] (89) 10/10 - 10", str(r1))

class test_to_dictionary(unittest.TestCase):

    def test_format(self):
        r1 = Square(2, 1, 9, 3)
        r1_dictionary = r1.to_dictionary()
        r1_print = {'x': 1, 'y': 9, 'id': 3, 'size': 2}
        self.assertDictEqual(r1_dictionary, r1_print)
        r2 = Square(1)
        r2.update(**r1_dictionary)
        self.assertTrue(r1.__dict__, r2.__dict__)
        self.assertIsNot(r1, r2)

if __name__ == '__main__':
    """calling the unit test"""
    unittest.main()
