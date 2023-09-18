"""the test case for Rectangle class"""
import unittest
import pycodestyle
import sys
import io
from models.rectangle import Rectangle


class TestCodeFormat(unittest.TestCase):

    def test_conformance(self):
        """Test that we conform to PEP-8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/rectangle.py',
                                    'tests/test_models/test_rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class test_initialization(unittest.TestCase):
    """this class test the methods under unittest"""

    def test_initializtion(self):
        """test the  initializtion method"""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)


class test_RectangleRaise(unittest.TestCase):
    """test the validation of getter and setter"""

    def test_ValueRaise(self):
        """"test the validation of instantiation"""
        r1 = Rectangle(10, 2)
        with self.assertRaises(ValueError):
            r1.width = -10
        with self.assertRaises(ValueError):
            r1.height = -5
        with self.assertRaises(ValueError):
            r1.x = -7
        with self.assertRaises(ValueError):
            r1.y = -10
        with self.assertRaises(ValueError):
            r1.width = 0
        with self.assertRaises(ValueError):
            r1.height = 0
        with self.assertRaises(ValueError):
            self.r4 = Rectangle(-10, 2, 0, 0)
        with self.assertRaises(ValueError):
            self.r4 = Rectangle(10, -2, 0, 0)
        with self.assertRaises(ValueError):
            self.r4 = Rectangle(10, 2, -3, 0)
        with self.assertRaises(ValueError):
            self.r4 = Rectangle(10, 2, 0, -3)
        with self.assertRaises(ValueError):
            self.r4 = Rectangle(0, 2, 0, 0)
        with self.assertRaises(ValueError):
            self.r4 = Rectangle(10, 0, 0, 0)

    def test_TypeStringRaise(self):
        r1 = Rectangle(10, 2)
        with self.assertRaises(TypeError):
            r1.width = "2"
        with self.assertRaises(TypeError):
            r1.height = "2"
        with self.assertRaises(TypeError):
            r1.x = "2"
        with self.assertRaises(TypeError):
            r1.y = "2"
        with self.assertRaises(TypeError):
            self.r4 = Rectangle("10", 2, 0, 0)
        with self.assertRaises(TypeError):
            self.r4 = Rectangle(10, "2", 0, 0)
        with self.assertRaises(TypeError):
            self.r4 = Rectangle(10, 2, "0", 0)
        with self.assertRaises(TypeError):
            self.r4 = Rectangle(10, 2, 0, "0")

    def test_TypeTupleRaise(self):
        r1 = Rectangle(10, 2)
        with self.assertRaises(TypeError):
            r1.height = (2,)
        with self.assertRaises(TypeError):
            r1.x = (2,)
        with self.assertRaises(TypeError):
            r1.y = (2,)
        with self.assertRaises(TypeError):
            r1.width = (2,)
        with self.assertRaises(TypeError):
            self.r4 = Rectangle((10,), 2, 0, 0)
        with self.assertRaises(TypeError):
            self.r4 = Rectangle(10, (2,), 0, 0)
        with self.assertRaises(TypeError):
            self.r4 = Rectangle(10, 2, (0,), 0)
        with self.assertRaises(TypeError):
            self.r4 = Rectangle(10, 2, 0, (0,))

    def test_TypeListRaise(self):
        r1 = Rectangle(10, 2)
        with self.assertRaises(TypeError):
            r1.width = [2]
        with self.assertRaises(TypeError):
            r1.height = [2]
        with self.assertRaises(TypeError):
            r1.x = [2]
        with self.assertRaises(TypeError):
            r1.y = [2]
        with self.assertRaises(TypeError):
            self.r4 = Rectangle([10], 2, 0, 0)
        with self.assertRaises(TypeError):
            self.r4 = Rectangle(10, [2], 0, 0)
        with self.assertRaises(TypeError):
            self.r4 = Rectangle(10, 2, [0], 0)
        with self.assertRaises(TypeError):
            self.r4 = Rectangle(10, 2, 0, [0])

    def test_TypeSetRaise(self):

        r1 = Rectangle(10, 2)

        with self.assertRaises(TypeError):
            r1.width = {2}
        with self.assertRaises(TypeError):
            r1.height = {2}
        with self.assertRaises(TypeError):
            r1.x = {2}
        with self.assertRaises(TypeError):
            r1.y = {2}
        with self.assertRaises(TypeError):
            self.r4 = Rectangle({10}, 2, 0, 0)
        with self.assertRaises(TypeError):
            self.r4 = Rectangle(10, {2}, 0, 0)
        with self.assertRaises(TypeError):
            self.r4 = Rectangle(10, 2, {0}, 0)
        with self.assertRaises(TypeError):
            self.r4 = Rectangle(10, 2, 0, {0})

    def test_TypeDictRaise(self):
        r1 = Rectangle(10, 2)

        with self.assertRaises(TypeError):
            r1.width = {2: 5}
        with self.assertRaises(TypeError):
            r1.height = {2: 5}
        with self.assertRaises(TypeError):
            r1.x = {2: 5}
        with self.assertRaises(TypeError):
            r1.y = {2: 5}
        with self.assertRaises(TypeError):
            self.r4 = Rectangle({'ky': 3}, 2, 0, 0)
        with self.assertRaises(TypeError):
            self.r4 = Rectangle(10, {'ky': 3}, 0, 0)
        with self.assertRaises(TypeError):
            self.r4 = Rectangle(10, 2, {'ky': 3}, 0)
        with self.assertRaises(TypeError):
            self.r4 = Rectangle(10, 2, 0, {'ky': 3})

    def test_TypefloatRaise(self):
        r1 = Rectangle(10, 2)

        with self.assertRaises(TypeError):
            r1.width = 1.5
        with self.assertRaises(TypeError):
            r1.height = 1.5
        with self.assertRaises(TypeError):
            r1.x = 1.5
        with self.assertRaises(TypeError):
            r1.y = 1.5
        with self.assertRaises(TypeError):
            self.r4 = Rectangle(10.5, 2, 0, 0)
        with self.assertRaises(TypeError):
            self.r4 = Rectangle(10, 4.5, 0, 0)
        with self.assertRaises(TypeError):
            self.r4 = Rectangle(10, 2, 5.4, 0)
        with self.assertRaises(TypeError):
            self.r4 = Rectangle(10, 2, 0, 2.5)

    def test_TypeBoolenRaise(self):
        r1 = Rectangle(10, 2)
        with self.assertRaises(TypeError):
            r1.width = True
        with self.assertRaises(TypeError):
            r1.height = True
        with self.assertRaises(TypeError):
            r1.x = True
        with self.assertRaises(TypeError):
            r1.y = True
        with self.assertRaises(TypeError):
            self.r4 = Rectangle(True, 2, 0, 0)
        with self.assertRaises(TypeError):
            self.r4 = Rectangle(10, True, 0, 0)
        with self.assertRaises(TypeError):
            self.r4 = Rectangle(10, 2, True, 0)
        with self.assertRaises(TypeError):
            self.r4 = Rectangle(10, 2, 0, True)


class test_RecArea(unittest.TestCase):
    """test the area of Rectangle"""

    def test_area(self):
        """test for area method"""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(3, 2)
        r3 = Rectangle(7, 8, 0, 0, 12)
        self.assertEqual(r1.area(), 20)
        self.assertEqual(r2.area(), 6)
        self.assertEqual(r3.area(), 56)

    def test_raisesarea(self):
        with self.assertRaises(TypeError):
            r4 = Rectangle()
        with self.assertRaises(AttributeError):
            Rectangle.area(self)
        with self.assertRaises(TypeError):
            r5 = Rectangle(1, 2, 3, 5, 8, 5)
        with self.assertRaises(UnboundLocalError):
            r5.area(self)


class test_Recdisplay(unittest.TestCase):

    def test_emptyrec(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle()
        with self.assertRaises(TypeError):
            Rectangle.display()

    def test_oneargrec(self):
        with self.assertRaises(TypeError):
            r2 = Rectangle(2)
        with self.assertRaises(TypeError):
            Rectangle.display()

    def test_print_1(self):
        output = "#\n#\n#\n"
        captured_output = io.StringIO()
        sys.stdout = captured_output
        r1 = Rectangle(1, 3)
        r1.display()
        sys.stdout = sys.__stdout__  # Restore stdout
        self.assertEqual(captured_output.getvalue(), output)

    def test_print_2(self):
        output = "####\n####\n####\n####\n"
        captured_output = io.StringIO()
        sys.stdout = captured_output
        r1 = Rectangle(4, 4)
        r1.display()
        sys.stdout = sys.__stdout__  # Restore stdout
        self.assertEqual(captured_output.getvalue(), output)


class test_stringmethod(unittest.TestCase):
    def test_fullarguments(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        expected_string = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(str(r1), expected_string)

    def test_midarguments(self):
        r10 = Rectangle(4, 6, 5, 6)
        expected_string = "[Rectangle] (54) 5/6 - 4/6"
        self.assertEqual(str(r10), expected_string)

    def test_minarguments(self):
        r11 = Rectangle(6, 5, 7)
        expected_string = "[Rectangle] (55) 7/0 - 6/5"
        self.assertEqual(str(r11), expected_string)


class test_updateargs(unittest.TestCase):
    def test_regularupdate(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual("[Rectangle] (89) 10/10 - 10/10", str(r1))


class test_to_dictionary(unittest.TestCase):

    def test_format(self):
        r1 = Rectangle(10, 2, 1, 9, 3)
        r1_dictionary = r1.to_dictionary()
        r1_print = {'x': 1, 'y': 9, 'id': 3, 'height': 2, 'width': 10}
        self.assertDictEqual(r1_dictionary, r1_print)
        r2 = Rectangle(1, 1)
        r2.update(**r1_dictionary)
        self.assertTrue(r1.__dict__, r2.__dict__)
        self.assertIsNot(r1, r2)


if __name__ == '__main__':

    """calling the unit test"""
    unittest.main()
