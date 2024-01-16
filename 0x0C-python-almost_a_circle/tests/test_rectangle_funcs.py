import unittest
import sys
import io
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleMethods(unittest.TestCase):
    def test_0_update_with_args(self):
        r1 = Rectangle(5, 5)
        r1.update(10, 20, 30, 40, 50)
        self.assertEqual(str(r1), "[Rectangle] (10) 40/50 - 20/30")

    def test_1_update_with_kwargs(self):
        r2 = Rectangle(3, 3)
        r2.update(width=8, height=12, x=5, y=7, id=15)
        self.assertEqual(str(r2), "[Rectangle] (15) 5/7 - 8/12")

    def test_2_to_dictionary(self):
        r3 = Rectangle(4, 6, 2, 3, 25)
        r3_dict = r3.to_dictionary()
        self.assertEqual(
            r3_dict, {'x': 2, 'y': 3, 'id': 25, 'height': 6, 'width': 4})

    def test_3_display(self):
        r4 = Rectangle(3, 2, 1, 0)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        r4.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), " ###\n ###\n")


if __name__ == '__main__':
    unittest.main()
