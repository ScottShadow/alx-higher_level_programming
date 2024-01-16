import unittest
from models.square import Square


class TestSquareUpdate(unittest.TestCase):
    def test_update_with_args(self):
        s1 = Square(5, 2, 3, 1)
        s1.update(10, 20, 30, 40)
        self.assertEqual(str(s1), "[Square] (10) 30/40 - 20")

    def test_update_with_kwargs(self):
        s2 = Square(3, 1, 1, 2)
        s2.update(size=8, x=5, y=7, id=15)
        self.assertEqual(str(s2), "[Square] (15) 5/7 - 8")

    def test_update_with_mixed_args_kwargs(self):
        s3 = Square(4, 0, 0, 3)
        s3.update(9, size=6, x=2, y=4)
        self.assertEqual(str(s3), "[Square] (9) 0/0 - 4")


if __name__ == '__main__':
    unittest.main()
