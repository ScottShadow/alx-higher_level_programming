import unittest
from models.base import Base


class TestFromJsonString(unittest.TestCase):

    def test_from_json_string_empty_string(self):
        result = Base.from_json_string("")
        self.assertEqual(result, [])

    def test_from_json_string_none(self):
        result = Base.from_json_string(None)
        self.assertEqual(result, [])

    def test_from_json_string_valid_string(self):
        json_string = '[{"id": 1, "name": "Object 1"}, {"id": 2, "name": "Object 2"}]'
        result = Base.from_json_string(json_string)
        expected = [{"id": 1, "name": "Object 1"},
                    {"id": 2, "name": "Object 2"}]
        self.assertEqual(result, expected)

    def test_from_json_string_invalid_string(self):
        json_string = '{"id": 1, "name": "Object 1"}, {"id": 2, "name": "Object 2"}'
        result = Base.from_json_string(json_string)
        self.assertEqual(result, [])

    def test_from_json_string_empty_list_string(self):
        json_string = '[]'
        result = Base.from_json_string(json_string)
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
