import unittest
from models.rectangle import Rectangle


class TestRectangleArea(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Rectangle.__nb_objects = 0

    def test_1_area_positive_values(self):
        r1 = Rectangle(5, 10)
        self.assertEqual(r1.area(), 50)

    def test_2_area_zero_values(self):
        with self.assertRaises(ValueError):
            r2 = Rectangle(0, 0)

    def test_3_area_negative_values(self):
        with self.assertRaises(ValueError):
            r3 = Rectangle(-5, 8)
            area = r3.area()

    def test_4_area_float_values(self):
        with self.assertRaises(TypeError):
            r4 = Rectangle(3.5, 6)
            area = r4.area()

    def test_5_area_after_update(self):
        r5 = Rectangle(4, 7)
        r5.update(width=8, height=2)
        self.assertEqual(r5.area(), 16)

    def test_6_area_after_multiple_updates(self):
        r6 = Rectangle(3, 5)
        r6.update(width=2)
        r6.update(height=4)
        r6.update(width=3, height=2)
        self.assertEqual(r6.area(), 6)

if __name__ == '__main__':
    unittest.main()