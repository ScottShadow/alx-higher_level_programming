# /usr/bin/python3
import unittest
from models.rectangle import *


class TestRectangle(unittest.TestCase):

    def test_1_init_rectangle_default_id(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 17)

    def test_2_init_rectangle_incremented_id(self):
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 18)

    def test_3_init_rectangle_custom_id(self):
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_4_init_rectangle_invalid_type_for_width(self):
        with self.assertRaises(TypeError):
            r4 = Rectangle('s', 5)

    def test_5_init_rectangle_invalid_type_for_height(self):
        with self.assertRaises(TypeError):
            r5 = Rectangle(5, 's')

    def test_6_init_rectangle_negative_width(self):
        with self.assertRaises(ValueError):
            r6 = Rectangle(-5, 4)

    def test_7_init_rectangle_negative_height(self):
        with self.assertRaises(ValueError):
            r7 = Rectangle(5, -4)

    def test_8_init_rectangle_invalid_type_for_x(self):
        with self.assertRaises(TypeError):
            r8 = Rectangle(5, 4, 'x')

    def test_9_init_rectangle_negative_x(self):
        with self.assertRaises(ValueError):
            r9 = Rectangle(5, 4, -3)

    def test_10_init_rectangle_invalid_type_for_y(self):
        with self.assertRaises(TypeError):
            r10 = Rectangle(5, 4, 3, 'y')

    def test_11_init_rectangle_negative_y(self):
        with self.assertRaises(ValueError):
            r11 = Rectangle(5, 4, 3, -2)

    def test_12_init_rectangle_none_width(self):
        with self.assertRaises(TypeError):
            r12 = Rectangle(None, 4)

    def test_13_init_rectangle_none_height(self):
        with self.assertRaises(TypeError):
            r13 = Rectangle(5, None)

if __name__ == '__main__':
    unittest.main()