#!/usr/bin/python3
import unittest
"""Unittest for max_integer([..])
"""
max_integer = __import__('6-max_integer').max_integer


class TestMaxInt(unittest.TestCase):
    max_integer0 = [1, 3, 4]
    max_integer1 = None

    def test_max_integer(self):
        max_integer0 = [1, 3, 4]
        self.assertEqual(max_integer(max_integer0), 4)

    def test_max_integer_type(self):
        max_integer0 = ["la", 34.1, 's']
        max_integer1 = None
        with self.assertRaises(TypeError):
            max_integer(max_integer1)
        self.assertIsInstance(max_integer0, list)

    def test_max_integer_negative_values(self):
        max_integer0 = [-5, -8, -2]
        self.assertEqual(max_integer(max_integer0), -2)

    def test_max_integer_mixed_values(self):
        max_integer0 = [10, "hello", 5, 20, "world"]
        with self.assertRaises(TypeError):
            max_integer(max_integer0)

    def test_max_integer_duplicate_values(self):
        max_integer0 = [7, 7, 7, 7]
        self.assertEqual(max_integer(max_integer0), 7)

    def test_max_integer_single_value(self):
        max_integer0 = [42]
        self.assertEqual(max_integer(max_integer0), 42)

    def test_max_integer_empty_list(self):
        max_integer0 = []
        self.assertIsNone(max_integer(max_integer0))
