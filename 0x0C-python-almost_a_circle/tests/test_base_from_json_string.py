import unittest
from models.base import Base


class TestFromJsonString(unittest.TestCase):

    def test_from_json_string_empty_string(self):
        # Test when an empty string is provided
        result = Base.from_json_string("")
        self.assertEqual(result, [])

    def test_from_json_string_none(self):
        # Test when None is provided
        result = Base.from_json_string(None)
        self.assertEqual(result, [])

    def test_from_json_string_valid_string(self):
        # Test when a valid JSON-formatted string is provided
        json_string = '[{"id": 1, "name": "Object 1"}, {"id": 2, "name": "Object 2"}]'
        result = Base.from_json_string(json_string)
        expected = [{"id": 1, "name": "Object 1"},
                    {"id": 2, "name": "Object 2"}]
        self.assertEqual(result, expected)

    def test_from_json_string_invalid_string(self):
        # Test when an invalid JSON-formatted string is provided
        json_string = '{"id": 1, "name": "Object 1"}, {"id": 2, "name": "Object 2"}'
        result = Base.from_json_string(json_string)
        self.assertEqual(result, [])

    def test_from_json_string_empty_list_string(self):
        # Test when a string representing an empty list is provided
        json_string = '[]'
        result = Base.from_json_string(json_string)
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
