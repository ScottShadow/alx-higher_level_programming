import unittest
import os
from models.rectangle import Rectangle


class TestSaveToFile(unittest.TestCase):

    def setUp(self):
        self.obj1 = Rectangle(5, 10)
        self.obj2 = Rectangle(8, 15)
        self.obj3 = Rectangle(12, 20)

    def tearDown(self):
        filename = f"{Rectangle.__name__}.json"
        if os.path.exists(filename):
            os.remove(filename)

    def test_save_to_file_single_instance(self):
        Rectangle.save_to_file([self.obj1])

        filename = f"{Rectangle.__name__}.json"
        self.assertTrue(os.path.exists(filename))

        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            self.assertIn('"width": 5', content)
            self.assertIn('"height": 10', content)

    def test_save_to_file_multiple_instances(self):
        Rectangle.save_to_file([self.obj1, self.obj2, self.obj3])

        filename = f"{Rectangle.__name__}.json"
        self.assertTrue(os.path.exists(filename))

        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            self.assertIn('"width": 5', content)
            self.assertIn('"width": 8', content)
            self.assertIn('"width": 12', content)
            self.assertIn('"height": 10', content)
            self.assertIn('"height": 15', content)
            self.assertIn('"height": 20', content)


if __name__ == '__main__':
    unittest.main()
