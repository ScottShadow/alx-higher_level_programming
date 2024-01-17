#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle


class TestCreateMethod(unittest.TestCase):
    def test_create_method_with_valid_attributes(self):
        # Test with valid attributes
        valid_attributes = {'width': 10, 'height': 5, 'x': 2, 'y': 3, 'id': 1}
        instance = Rectangle.create(**valid_attributes)
        self.assertIsInstance(instance, Rectangle)
        self.assertEqual(instance.width, valid_attributes['width'])
        self.assertEqual(instance.height, valid_attributes['height'])
        self.assertEqual(instance.x, valid_attributes['x'])
        self.assertEqual(instance.y, valid_attributes['y'])
        self.assertEqual(instance.id, valid_attributes['id'])

    def test_create_method_with_missing_attributes(self):
        # Test with missing attributes
        missing_attributes = {'width': 10, 'height': 5}
        instance = Rectangle.create(**missing_attributes)
        self.assertIsInstance(instance, Rectangle)
        self.assertEqual(instance.width, missing_attributes['width'])
        self.assertEqual(instance.height, missing_attributes['height'])
        # Check default values for missing attributes
        self.assertEqual(instance.x, 0)
        self.assertEqual(instance.y, 0)
        self.assertNotEqual(instance.id, 0)

    def test_create_method_with_invalid_attributes(self):
        # Test with invalid attributes
        invalid_attributes = {'width': 'invalid', 'height': 'invalid',
                              'x': 'invalid', 'y': 'invalid', 'id': 'invalid'}
        instance = Rectangle.create(**invalid_attributes)
        # Check if the instance is still created with default values
        self.assertIsInstance(instance, Rectangle)
        self.assertEqual(instance.width, 1)
        self.assertEqual(instance.height, 1)
        self.assertEqual(instance.x, 0)
        self.assertEqual(instance.y, 0)
        self.assertNotEqual(instance.id, 0)

    def test_create_method_with_empty_attributes(self):
        # Test with empty attributes
        empty_attributes = {}
        instance = Rectangle.create(**empty_attributes)
        self.assertIsInstance(instance, Rectangle)
        # Check default values for all attributes
        self.assertEqual(instance.width, 1)
        self.assertEqual(instance.height, 1)
        self.assertEqual(instance.x, 0)
        self.assertEqual(instance.y, 0)
        self.assertNotEqual(instance.id, 0)


if __name__ == '__main__':
    unittest.main()
