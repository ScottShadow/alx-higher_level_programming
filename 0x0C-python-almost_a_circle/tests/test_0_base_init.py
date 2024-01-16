import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    @classmethod
    def test_01_setUpClass(cls):
        Base.__nb_objects = 0

    def test_1_init_default_id(self):
        b1 = Base()
        self.assertIsNotNone(b1)
        self.assertEqual(b1.id, 1)

    def test_2_init_incremented_id(self):
        b2 = Base()
        self.assertIsNotNone(b2)
        self.assertEqual(b2.id, 2)

    def test_3_init_custom_id(self):
        b3 = Base(12)
        self.assertIsNotNone(b3)
        self.assertEqual(b3.id, 12)

    def test_4_init_auto_increment_on_none(self):
        b4 = Base(None)
        self.assertIsNotNone(b4)
        self.assertEqual(b4.id, 3)

    def test_5_init_auto_increment_on_string(self):
        b5 = Base("hello")
        self.assertIsNotNone(b5)
        self.assertEqual(b5.id, "hello")

    def test_6_init_custom_id_overrides_increment(self):
        b6 = Base(2)
        self.assertIsNotNone(b6)
        self.assertEqual(b6.id, 2)

    def test_7_init_negative_custom_id(self):
        b7 = Base(-5)
        self.assertIsNotNone(b7)
        self.assertEqual(b7.id, -5)

    def test_8_init_zero_custom_id(self):
        b8 = Base(0)
        self.assertIsNotNone(b8)
        self.assertEqual(b8.id, 0)

    def test_9_init_float_custom_id(self):
        b9 = Base(5.5)
        self.assertIsNotNone(b9)
        self.assertEqual(b9.id, 5.5)


if __name__ == '__main__':
    unittest.main()
